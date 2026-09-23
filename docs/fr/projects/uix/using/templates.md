---
description: Learn all about using templates.
---
# Modèles

Tous les styles peuvent contenir des [modèles Jinja2](https://www.home-assistant.io/docs/configuration/templating/), qui seront traités par le moteur de Home Assistant.

UI eXtension met également les variables suivantes à disposition des modèles :

- `config` - The entire configuration of the card, entity or badge - (`config.entity` may be of special interest)
- `user` - The name of the currently logged in user
- `browser` - The `browser_id` of your browser, if you have [browser_mod](https://github.com/thomasloven/hass-browser_mod) installed
- `hash` - Whatever comes after `#` in the current URL. UIX watches for location changes through `location-changed` and `popstate` events so templates will be rebound with the updated `hash` (this can be disabled in Integration Options → Performance settings via **Disable hash template variable and updates**, which also makes `hash` unavailable)
- `panel` - various information about the panel in view, be it a lovelace dashboard or another panel view. `panel` is a dictionary containing the following panel attributes with example values shown.
  - `panel.fullUrlPath`: "uix/another-test-view"
  - `panel.panelComponentName`: "lovelace"
  - `panel.panelIcon`: "mdi:card-bulleted-outline"
  - `panel.panelNarrow`: true
  - `panel.panelRequireAdmin`: false
  - `panel.panelTitle`: "UIX"
  - `panel.panelUrlPath`: "uix"
  - `panel.viewNarrow`: true
  - `panel.viewTitle`: "Test View"
  - `panel.viewUrlPath`: "another-test-view"
  - `panel.globalTheme`: "Red theme"
  - `panel.theme`: "Blue theme"

::: info Panel theme variables
`panel.theme` is set when the dashboard view has a theme set directly, otherwise is `None`. `panel.globalTheme` is the global Home Assistant theme currently applied. The effective UIX theme is not part of the `panel` dictionary.

:::
Vous pouvez déboguer les modèles UIX Jinja2 en plaçant le commentaire <code v-pre>{# uix.debug #}</code> n'importe où dans votre modèle. Vous verrez les messages de débogage lors de la liaison du modèle, de la mise à jour de valeur, de la réutilisation, de la déliaison et du désabonnement final. Chaque modèle reste abonné dans le cache pendant 20 secondes afin de faciliter l'application des modèles et d'améliorer légèrement la vitesse lorsque vous passez d'une vue à l'autre ou utilisez le même modèle sur des cartes de vues différentes.

## Macros

UI eXtension prend en charge les [macros Jinja2 réutilisables](https://jinja.palletsprojects.com/en/stable/templates/#macros), définies au niveau d'une carte ou d'un thème, qui sont ajoutées au début de chaque modèle de la carte.

### Définir des macros sur une carte

Les macros sont définies sous `uix.macros` dans la configuration de la carte. Une macro sans `returns` produit son modèle directement sous forme de chaîne. Utilisez-la pour insérer une valeur textuelle (par exemple une couleur CSS ou un nom d'icône) dans le modèle :

```yaml
type: tile
entity: light.living_room
uix:
  macros:
    state_color:
      params:
        - entity_id
        - name: color_on
          default: "'yellow'"
        - name: color_off
          default: "'gray'"
      template: "{{ color_on if is_state(entity_id, 'on') else color_off }}"
  style: |
    ha-card {
      background: {{ state_color(config.entity) }};
    }
```

Chaque entrée de macro accepte les clés suivantes :

| Key | Required | Description |
| --- | -------- | ----------- |
| `template` | Yes | The Jinja2 template body of the macro. |
| `params` | No | A list of parameters the macro accepts. Each entry is either a plain string (parameter name) or a mapping with `name` and `default` keys (see below). |
| `returns` | No | Set to `true` to make the macro callable as a function using Home Assistant's `as_function` filter. When `true`, use `<code v-pre>{%- do returns(<value>) -%}</code>` inside the template to return a typed value (boolean, number, etc.). |

Chaque élément de `params` peut être :

- A **plain string** — just the parameter name: `- entity_id`
- A **mapping** with `name` and `default` — the parameter name and its Jinja2 default expression:

```yaml
params:
  - entity_id
  - name: color_on
    default: "'yellow'"
  - name: color_off
    default: "'gray'"
```

Cela génère la signature de macro Jinja2 suivante :

```jinja
{% macro state_color(entity_id, color_on = 'yellow', color_off = 'gray') %}
{{ color_on if is_state(entity_id, 'on') else color_off }}
{% endmacro %}
```

La valeur `default` est insérée telle quelle comme expression Jinja2. Encadrez les valeurs textuelles d'apostrophes à l'intérieur de la chaîne YAML (par exemple `"'yellow'"`).

### Macros avec `returns`

Lorsqu'une macro produit son résultat directement (sans `returns`), celui-ci est toujours une chaîne : même <code>&#123;&#123; is_state(entity_id, "on") &#125;&#125;</code> renvoie la chaîne `"True"` ou `"False"`, et toute chaîne non vide est considérée comme vraie par Jinja2. Pour renvoyer une valeur booléenne ou numérique qui fonctionne correctement dans les conditions et les comparaisons, utilisez `returns: true`.

Avec `returns: true`, la macro suit la convention [`as_function`](https://www.home-assistant.io/docs/configuration/templating/#as_function) de Home Assistant : son nom interne devient `macro_<name>`, avec `returns` comme dernier paramètre, puis elle est exposée sous le nom `<name>` au moyen du filtre `as_function`. L'appelable `returns` est injecté automatiquement lorsque la macro est appelée comme une fonction :

```yaml
type: tile
entity: light.living_room
uix:
  macros:
    is_on:
      params:
        - entity_id
      returns: true
      template: "{%- do returns(is_state(entity_id, 'on')) -%}"
  style: |
    ha-card {
      --tile-color: {{ 'yellow' if is_on(config.entity) else 'gray' }} !important;
    }
```

Cela génère le bloc Jinja2 suivant, ajouté au début de chaque modèle :

```jinja
{% macro macro_is_on(entity_id, returns) %}
{%- do returns(is_state(entity_id, 'on')) -%}
{% endmacro %}
{% set is_on = macro_is_on | as_function %}
```

### Composer des macros

Les macros peuvent appeler d'autres macros définies dans la même carte. UIX détecte automatiquement ces dépendances et inclut toutes les macros nécessaires dans le résultat, même si seul l'appel à la macro externe apparaît dans le modèle principal.

```yaml
type: tile
entity: light.living_room
uix:
  macros:
    color_for_state:
      params:
        - entity_id
      template: "{{ 'green' if is_state(entity_id, 'on') else 'red' }}"
    border_style:
      params:
        - entity_id
      template: "2px solid {{ color_for_state(entity_id) }}"
  style: |
    ha-card {
      border: {{ border_style(config.entity) }};
    }
```

Even though only `border_style` is used in the style template, `color_for_state` is also included because `border_style` references it. This generates the following Jinja2 block prepended to every template:

```jinja
{% macro color_for_state(entity_id) %}
{{ 'green' if is_state(entity_id, 'on') else 'red' }}
{% endmacro %}
{% macro border_style(entity_id) %}
2px solid {{ color_for_state(entity_id) }}
{% endmacro %}
```

### Importer des macros depuis des fichiers de modèles personnalisés

En plus de définir les macros directement, vous pouvez importer des macros depuis les [modèles réutilisables de Home Assistant](https://www.home-assistant.io/docs/configuration/templating/#reusing-templates) enregistrés dans `/config/custom_templates/*.jinja`. Pour cela, indiquez le nom du fichier (une simple chaîne) comme valeur de l'entrée de macro, au lieu d'un objet de définition :

```yaml
type: tile
entity: light.living_room
uix:
  macros:
    state_color: "my_macros.jinja"
  style: |
    ha-card {
      background: {{ state_color(config.entity) }};
    }
```

Cela génère l'instruction d'importation suivante, ajoutée au début de chaque modèle :

```jinja
{% from 'my_macros.jinja' import state_color %}
```

La macro `state_color` doit être définie dans `/config/custom_templates/my_macros.jinja`. Chaque entrée de `macros` importe la macro portant son nom ; vous pouvez donc importer plusieurs macros depuis un même fichier ou depuis différents fichiers :

```yaml
uix:
  macros:
    state_color: "my_macros.jinja"
    is_on: "my_macros.jinja"
    format_date: "utils.jinja"
```

::: tip Using template file macros
Tous les fichiers de modèles doivent porter l'extension `.jinja` et faire moins de 5 Mio. Les modèles du dossier `/config/custom_templates` sont chargés au démarrage de Home Assistant. Pour les recharger sans redémarrer Home Assistant, exécutez l'action `homeassistant.reload_custom_templates`.

:::
Inline and file-import macros can be freely mixed within the same card.

### Macros de thème

Vous pouvez également définir des macros dans un thème afin qu'elles soient disponibles pour toutes les cartes qui l'utilisent. Consultez [Thèmes - Macros](themes.md#macros) pour en savoir plus.

Les macros définies sur une carte sont prioritaires sur celles du thème portant le même nom ; une carte peut ainsi remplacer une macro du thème.

## Billets

Les billets sont des valeurs YAML nommées qui deviennent des constantes simples dans les modèles — utilisables **sans parenthèses**, contrairement aux macros. Ils sont disponibles dans les modèles UIX Styling et UIX Forge. Les valeurs textuelles peuvent référencer d'autres billets avec la syntaxe `{name}` ; l'ordre des déclarations n'a pas d'importance.

### Billets dans UIX Styling

Définissez les billets sous `uix.billets` dans une carte. Chaque billet est inséré sous la forme d'une instruction `<code v-pre>{%- set name = value -%}</code>` avant chaque modèle de style de cette carte :

#### Billet interpolation

String billet values may reference other billets using `{name}` syntax — a simple substitution performed before the billets are turned into Jinja2 variables. Use `{name[N]}` to reference element `N` (0-indexed) from a list billet:

```yaml
uix:
  billets:
    room: "bed"                         # plain string
    entity_id: "light.{room}_light"     # → "light.bed_light"
    scenes:
      - bright
      - dim
    default_scene: "{scenes[0]}"        # → "bright"
  style: |
    ha-card { content: "{{ entity_id }} / {{ default_scene }}"; }
```

Billet references are resolved in dependency order, so declaration order does not matter:

```yaml
billets:
  entity: "light.{room}_light" # → "light.bedroom_light"  (resolved after room)
  room: "{base}room"           # → "bedroom"  (resolved after base)
  base: "bed"
```

::: note Circular references
Si des billets se référencent en boucle, directement ou par une chaîne de références, aucun billet de cette boucle ne peut être résolu. UIX consigne une erreur pour chacun et conserve leurs valeurs telles quelles.

:::
```yaml
type: custom:uix-forge
entity: light.bed_light
forge:
  mold: card
  grid_options:
    columns: 7
  billets:
    my_color: teal
    max_brightness: 255
    tags:
      - living_room
      - ambient
element:
  type: tile
  entity: "{{ config.entity }}"
  name: "{{ my_color | capitalize }} light"
  tap_action:
    action: perform-action
    perform_action: light.turn_on
    target:
      entity_id: "{{ config.entity }}"
    data:
      brightness: "{{ max_brightness }}"
  uix:
    style: |
      ha-card {
        --tile-color: {{ my_color }} !important;
      }
      ha-tile-info span:nth-of-type(2):after {
      {%- if is_state_attr(config.entity, 'brightness', max_brightness) -%}
        content: ' - {{ tags | join(', ') }} - MAX';
        font-weight: 900;
      {%- else -%}
        content: ' - {{ tags | join(', ') }}';
      {% endif -%}
      }
```

![Example using billets](../assets/page-assets/forge/billets.gif)

In templates, billets are used as plain constants:

```jinja
{{ accent_color }}         {# teal #}
{{ max_level + 1 }}        {# 101 #}
{{ tags | join(', ') }}    {# living_room, ambient #}
```

### Billets dans UIX Forge

Avec [UIX Forge](../forge/index.md), les billets définis sous `forge.billets` sont disponibles dans tous les modèles Forge **ainsi que** dans tout style `uix:` de la carte Forge ou de l'élément généré. Ils sont fusionnés avec les billets définis directement dans la configuration `uix:` ; ceux-ci restent prioritaires.

Consultez la référence complète [UIX Forge — Billets](../forge/forge.md#billets), qui décrit les types pris en charge et le comportement de remplacement des fonderies.
