---
title: Templates
description: Templates in UIX verwenden.
---
# Templates

Alle Styles können [Jinja2-Templates](https://www.home-assistant.io/docs/configuration/templating/) enthalten, die vom Home-Assistant-Backend verarbeitet werden.

UI eXtension stellt Templates zusätzlich diese Variablen bereit:

- `config`: die komplette Konfiguration der Karte, Entity oder Badge. `config.entity` ist oft besonders nützlich.
- `user`: der Name des aktuell angemeldeten Nutzers.
- `browser`: die `browser_id` deines Browsers, wenn [browser_mod](https://github.com/thomasloven/hass-browser_mod) installiert ist.
- `hash`: alles, was nach `#` in der aktuellen URL steht. UIX beobachtet `location-changed` und `popstate`, sodass Templates bei geändertem `hash` neu gebunden werden. Das kann in den Integrationsoptionen unter Performance deaktiviert werden.
- `panel`: Informationen über das aktuell sichtbare Panel oder Dashboard.

Beispielwerte in `panel`:

- `panel.fullUrlPath`: `"uix/another-test-view"`
- `panel.panelComponentName`: `"lovelace"`
- `panel.panelIcon`: `"mdi:card-bulleted-outline"`
- `panel.panelNarrow`: `true`
- `panel.panelRequireAdmin`: `false`
- `panel.panelTitle`: `"UIX"`
- `panel.panelUrlPath`: `"uix"`
- `panel.viewNarrow`: `true`
- `panel.viewTitle`: `"Test View"`
- `panel.viewUrlPath`: `"another-test-view"`
- `panel.globalTheme`: `"Red theme"`
- `panel.theme`: `"Blue theme"`

::: info Panel-Theme-Variablen
`panel.theme` ist gesetzt, wenn die Dashboard-Ansicht direkt ein Theme nutzt, sonst ist es `None`. `panel.globalTheme` ist das global angewendete Home-Assistant-Theme. Das effektiv genutzte UIX-Theme ist nicht Teil des `panel`-Dictionary.
:::

Templates können mit dem Kommentar <code v-pre>{# uix.debug #}</code> debuggt werden. UIX zeigt dann Meldungen beim Binden, Aktualisieren, Wiederverwenden, Lösen und endgültigen Abmelden des Templates. Templates bleiben für eine kurze Cooldown-Zeit im Cache, was beim Wechsel zwischen Views oder bei mehrfach verwendeten Templates etwas Geschwindigkeit bringen kann.

## Makros

UI eXtension unterstützt wiederverwendbare [Jinja2-Makros](https://jinja.palletsprojects.com/en/stable/templates/#macros). Sie können auf Kartenebene oder über Themes definiert werden und werden jedem Template der Karte vorangestellt.

### Makros auf einer Karte definieren

Makros werden unter `uix.macros` definiert. Ein Makro ohne `returns` rendert sein Template inline als String. Nutze das, wenn du einen Textwert wie eine CSS-Farbe oder einen Icon-Namen direkt in das Template einsetzen möchtest.

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

Jeder Makro-Eintrag unterstützt diese Schlüssel:

| Schlüssel | Pflicht | Beschreibung |
| --- | --- | --- |
| `template` | Ja | Der Jinja2-Template-Body des Makros. |
| `params` | Nein | Liste der Parameter. Ein Eintrag ist entweder ein String oder ein Mapping mit `name` und `default`. |
| `returns` | Nein | Mit `true` wird das Makro über Home Assistants `as_function`-Filter als Funktion aufrufbar. Im Template wird dann <code v-pre>{%- do returns(&lt;wert&gt;) -%}</code> verwendet. |

Einträge in `params` können einfache Strings oder Mappings sein:

```yaml
params:
  - entity_id
  - name: color_on
    default: "'yellow'"
  - name: color_off
    default: "'gray'"
```

Daraus entsteht sinngemäß diese Jinja2-Signatur:

```jinja
{% macro state_color(entity_id, color_on = 'yellow', color_off = 'gray') %}
{{ color_on if is_state(entity_id, 'on') else color_off }}
{% endmacro %}
```

Der `default`-Wert wird unverändert als Jinja2-Ausdruck eingefügt. Strings sollten innerhalb des YAML-Strings mit einfachen Anführungszeichen notiert werden, zum Beispiel `"'yellow'"`.

### Makros mit `returns`

Ein inline renderndes Makro ohne `returns` gibt immer einen String zurück. Auch <code v-pre>{{ is_state(entity_id, "on") }}</code> ergibt dann den String `"True"` oder `"False"`, und nicht leere Strings sind in Jinja2 wahr. Wenn ein tatsächlicher Boolean oder eine Zahl zurückgegeben werden soll, nutze `returns: true`.

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

Intern wird daraus ein Makro nach Home-Assistant-`as_function`-Konvention:

```jinja
{% macro macro_is_on(entity_id, returns) %}
{%- do returns(is_state(entity_id, 'on')) -%}
{% endmacro %}
{% set is_on = macro_is_on | as_function %}
```

### Makros zusammensetzen

Makros können andere Makros derselben Karte aufrufen. UIX erkennt diese Abhängigkeiten automatisch und fügt alle benötigten Makros ein, auch wenn im Haupttemplate nur das äußerste Makro verwendet wird.

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

Obwohl nur `border_style` im Style-Template steht, wird `color_for_state` ebenfalls eingebunden.

```jinja
{% macro color_for_state(entity_id) %}
{{ 'green' if is_state(entity_id, 'on') else 'red' }}
{% endmacro %}
{% macro border_style(entity_id) %}
2px solid {{ color_for_state(entity_id) }}
{% endmacro %}
```

### Makros aus Custom-Template-Dateien importieren

Zusätzlich zu inline definierten Makros können Makros aus [wiederverwendbaren Home-Assistant-Templates](https://www.home-assistant.io/docs/configuration/templating/#reusing-templates) in `/config/custom_templates/*.jinja` importiert werden. Setze dazu den Makro-Eintrag als Dateiname statt als Makro-Objekt:

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

Daraus entsteht:

```jinja
{% from 'my_macros.jinja' import state_color %}
```

Das Makro `state_color` muss in `/config/custom_templates/my_macros.jinja` definiert sein. Jeder Eintrag in `macros` importiert sein eigenes Makro:

```yaml
uix:
  macros:
    state_color: "my_macros.jinja"
    is_on: "my_macros.jinja"
    format_date: "utils.jinja"
```

::: tip Template-Datei-Makros verwenden
Alle Template-Dateien müssen die Endung `.jinja` haben und kleiner als 5 MiB sein. Templates im Ordner `/config/custom_template` werden beim Home-Assistant-Start geladen. Ohne Neustart können sie mit der Aktion `homeassistant.reload_custom_templates` neu geladen werden.
:::

Inline-Makros und aus Dateien importierte Makros können in derselben Karte gemischt werden.

### Theme-Makros

Makros können auch in einem Theme definiert werden, damit sie allen Karten zur Verfügung stehen, die dieses Theme nutzen. Details stehen unter [Themes - Makros](./themes#makros).

Makros auf Kartenebene haben Vorrang vor Theme-Makros mit demselben Namen. So kann eine einzelne Karte ein Theme-Makro überschreiben.

## Billets

Billets sind benannte YAML-Werte, die zu einfachen Template-Konstanten werden. Anders als Makros werden sie **ohne Klammern** verwendet. Sie sind in UIX Styling und UIX Forge Templates verfügbar. Billet-Strings dürfen andere Billets per `{name}` referenzieren; die Deklarationsreihenfolge spielt keine Rolle.

### Billets in UIX Styling

Billets werden auf einer Karte unter `uix.billets` definiert. Jedes Billet wird als <code v-pre>{%- set name = value -%}</code> vor jedes Style-Template dieser Karte gesetzt.

#### Billet-Interpolation

String-Werte können andere Billets über `{name}` referenzieren. Mit `{name[N]}` kann Element `N` einer Liste referenziert werden.

```yaml
uix:
  billets:
    room: "bed"
    entity_id: "light.{room}_light"
    scenes:
      - bright
      - dim
    default_scene: "{scenes[0]}"
  style: |
    ha-card { content: "{{ entity_id }} / {{ default_scene }}"; }
```

Billet-Referenzen werden in Abhängigkeitsreihenfolge aufgelöst:

```yaml
billets:
  entity: "light.{room}_light"
  room: "{base}room"
  base: "bed"
```

::: info Zirkuläre Referenzen
Wenn Billets sich direkt oder indirekt gegenseitig referenzieren, können die beteiligten Werte nicht aufgelöst werden. UIX protokolliert einen Fehler und lässt die Werte unverändert.
:::

### Billets in UIX Forge

Billets können auch in UIX Forge verwendet werden, um wiederkehrende Werte wie Farben, Entity-IDs, Helligkeiten oder Tags an einer zentralen Stelle zu definieren.

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
```
