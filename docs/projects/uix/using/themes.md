---
title: Themes
description: UIX Themes verwenden.
---
# Themes

## Einstieg

Zuerst müssen Themes in Home Assistant aktiviert sein. Üblich ist ein Ordner `/config/themes/` und folgender Eintrag in `configuration.yaml`:

```yaml
frontend:
  themes: !include_dir_merge_named themes/
```

Nach einem Neustart von Home Assistant kannst du Theme-Dateien in diesem Ordner ablegen und sie über den Frontend-Service `reload_theme` neu laden.

Theme-Dateien sind normalerweise YAML-Dokumente mit vielen themefähigen Home-Assistant-Variablen.

`/config/themes/red.yaml`

```yaml
red-theme:
  primary-color: red
  ha-card-border-radius: 20px
```

::: tip Theme-Name
Der Theme-Name muss in der ersten Zeile stehen. Alle weiteren Werte werden eine Ebene eingerückt.
:::

![Red theme example](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-red.png)

## Einfaches UIX-Theme

::: info Theme-Variable
Das Theme **muss** eine Variable `uix-theme` definieren. Ihr Wert wählt die Theme-Definition, die UIX für Styles, Makros und [Schriftarten](#fonts) nutzt. Normalerweise entspricht `uix-theme` dem Home-Assistant-Theme-Namen, kann aber auch auf ein anderes Theme zeigen, wenn dessen UIX-Konfiguration wiederverwendet werden soll.

```yaml
my-awesome-theme:
  uix-theme: my-awesome-theme
```

```yaml
theme-mods:
  # UIX theme variables, styles and macros

my-awesome-theme:
  uix-theme: theme-mods
```
:::

`/config/themes/red.yaml`

```yaml
red-theme:
  uix-theme: red-theme

  primary-color: red
  primary-text-color: white
  ha-card-border-radius: 20
```

Sobald `uix-theme` gesetzt ist, können UIX-Theme-Variablen global genutzt werden. Dafür gibt es Variablen der Form `uix-<thing>`, wobei `<thing>` eine der [Theme-Variablen](#theme-variablen) ist.

Wenn zum Beispiel jede Zeile einer Entities-Karte einen Rahmen bekommen soll, könnte man es pro Row schreiben:

```yaml
type: entities
entities:
  - entity: light.bed_light
    uix:
      style: |
        :host {
          display: block;
          border: 1px solid black;
        }
  - entity: light.ceiling_lights
    uix:
      style: |
        :host {
          display: block;
          border: 1px solid black;
        }
```

Eleganter ist derselbe Stil im Theme:

```yaml
red-theme:
  uix-theme: red-theme

  uix-row: |
    :host {
      display: block;
      border: 1px solid black;
    }
```

![Red theme row border example](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-red-black-rows-border.png)

::: tip `uix-<thing>`-Variablen
`uix-<thing>`-Variablen enthalten CSS-Code als String. Sie müssen mit `|` oder `>` beginnen und mindestens eine Ebene eingerückt sein.
:::

Wie bei direktem UIX-Styling können Jinja2-Templates verwendet werden:

```yaml
red-theme:
  uix-theme: red-theme

  uix-row: |
    :host {
      display: block;
      border: 1px solid {% if is_state(config.entity, 'on') %} red {% else %} black {% endif %};
    }
```

![Red theme with template row borders](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-red-red-rows-template.png)

## Klassen

UIX kann CSS-Klassen auf Elemente setzen. Diese Klassen können im Theme genutzt werden.

```yaml
red-theme:
  uix-theme: red-theme

  uix-row: |
    :host(.teal) {
      background: teal;
    }
    :host(.purple) {
      background: purple;
    }
```

```yaml
type: entities
entities:
  - entity: light.bed_light
  - entity: light.ceiling_lights
    uix:
      class: teal
  - entity: light.kitchen_lights
    uix:
      class: purple
```

![Red theme with classes](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-red-classes.png)

## Shadow DOM navigieren

Wie bei UIX-Styles direkt an einer Karte kann auch in Theme-Variablen durch Shadow-DOM-Strukturen navigiert werden. Dafür wird `uix-<thing>-yaml` verwendet. Die Syntax ist dieselbe wie bei verschachtelten UIX-Style-Pfaden.

```yaml
red-theme:
  uix-theme: red-theme

  uix-row-yaml: |
    hui-generic-entity-row $ state-badge $: |
      @keyframes pulse {
        50% {
          opacity: 0.5;
        }
      }
      ha-state-icon {
        animation: pulse 2s infinite;
      }
```

::: tip Theme-Variablen müssen Strings sein
Auch wenn der Wert einer `uix-<thing>-yaml`-Variable selbst YAML enthält, muss er aus Sicht des Home-Assistant-Themes ein String sein, der wiederum weitere Strings enthält.
:::

## Lokales Theme-Override mit `uix.theme`

Mit `uix.theme` kann ein einzelnes gestyltes Element, zum Beispiel Karte, Row, Badge oder Element, ein anderes Home-Assistant-Theme verwenden als das global aktive Theme. `uix.theme` hat Vorrang vor dem geerbten Theme für diesen UIX-Knoten.

Haupt-Theme für rote Rows:

```yaml
row-red:
  uix-theme: row-red
  uix-row-yaml: |
    hui-generic-entity-row $: |
      .info {
        color: red;
      }
```

Override-Theme für blaue Rows:

```yaml
row-blue-override:
  uix-theme: row-blue-override
  uix-row-yaml: |
    hui-generic-entity-row $: |
      .info {
        color: blue;
      }
```

Entities-Karte mit Theme-Override für eine Row:

```yaml
type: entities
title: Lights
entities:
  - entity: light.bed_light
  - entity: light.ceiling_lights
  - entity: light.kitchen_lights
    uix:
      theme: row-blue-override
```

![UIX Theme override example](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-local-override.png)

::: warning Theme-Overrides bewusst einsetzen
Styling und Theming in Home Assistant können komplex werden. Eine CSS-Variable kann gesetzt sein und trotzdem nicht dort wirken, wo man sie erwartet. Wird beispielsweise `--primary-text-color` auf eine Entities Row gesetzt, kann der Text trotzdem unverändert bleiben, weil die tatsächliche Farbe weiter oben am `ha-card`-Element der Entities-Karte gesetzt wird.
:::

## Von `uix-<thing>` auf `uix-<thing>-yaml` wechseln

::: tip Priorität von UIX-Theme-Variablen
`uix-<thing>-yaml` hat immer Vorrang vor `uix-<thing>`. Ist die `-yaml`-Variante vorhanden, wird `uix-<thing>` nicht verwendet.
:::

Wenn ein Theme mit einfachen CSS-Strings in `uix-<thing>` beginnt und später Shadow-DOM-Pfade braucht, kann auf `uix-<thing>-yaml` gewechselt werden. Der Root-YAML-Selektor `.:` steht dabei für den aktuellen Kontext.

```yaml
red-theme:
  uix-theme: red-theme

  primary-color: red
  ha-card-border-radius: 20px

  uix-row-yaml: |
    .: |
      :host {
        display: block;
        border: 1px solid {% if is_state(config.entity, 'on') %} red {% else %} black {% endif %};
      }
      :host(.teal) {
        background: teal;
      }
      :host(.purple) {
        background: purple;
      }
    hui-generic-entity-row $ state-badge $: |
      @keyframes pulse {
        50% {
          opacity: 0.5;
        }
      }
      ha-state-icon {
        animation: pulse 2s infinite;
      }
```

## Theme-Variablen

- `uix-card`
- `uix-row`
- `uix-glance`
- `uix-badge`
- `uix-heading-badge`
- `uix-assist-chip`
- `uix-element`
- `uix-entity-marker`
- `uix-root`
- `uix-view`
- `uix-more-info`
- `uix-sidebar`
- `uix-config`
- `uix-panel-custom`
- `uix-top-app-bar-fixed`
- `uix-dialog`
- `uix-toast`
- `uix-grid-section`
- `uix-calendar`
- `uix-todo`
- `uix-history`
- `uix-states-history-charts`
- `uix-drawer`
- `uix-view-background`
- `uix-persistent-notification-item`

Zusätzlich gibt es jeweils auch `<variable>-yaml`.

## Schriftarten {#fonts}

`uix-fonts` lädt Webfonts beim Auswählen eines globalen Themes. UIX erstellt [`FontFace`-Objekte](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace) und registriert sie in `document.fonts`. Die Schriften stehen Home-Assistant-Komponenten auch in Shadow Roots zur Verfügung. Diese Option lädt nur Schriften; Theme-Variablen oder UIX-Styles bestimmen deren Verwendung.

Home-Assistant-Theme-Werte müssen Zeichenketten sein. Schreibe die Zuordnung in einen `|`-Block:

```yaml
retro-theme:
  uix-theme: retro-theme
  uix-fonts: |
    ChicagoFLF:
      source: url("https://cdn.jsdelivr.net/npm/@sakun/system.css@0.1.11/fonts/ChicagoFLF.woff2") format("woff2")
    dashboard-regular:
      family: My Dashboard Font
      source: url("/local/fonts/dashboard-regular.woff2") format("woff2")
      descriptors:
        weight: "400"
        style: normal
        display: swap
    dashboard-bold:
      family: My Dashboard Font
      source: url("/local/fonts/dashboard-bold.woff2") format("woff2")
      descriptors:
        weight: "700"

  ha-font-family-body: '"ChicagoFLF", sans-serif'
  ha-font-family-heading: '"ChicagoFLF", sans-serif'
  uix-card: |
    ha-card {
      font-family: "ChicagoFLF", sans-serif;
    }
```

| Schlüssel | Erforderlich | Beschreibung |
| --- | --- | --- |
| `family` | Nein | CSS-Schriftfamilie; standardmäßig der Zuordnungsschlüssel. Mehrere Schriftschnitte können denselben Familiennamen verwenden. |
| `source` | Ja | CSS-Schriftquelle, z. B. `url("/local/fonts/example.woff2") format("woff2")`. Unterstützt kommagetrennte Fallbacks und `local("Font Name")`. Verwende Schriftdateien, keine CSS-Stylesheet-URL eines Anbieters. |
| `descriptors` | Nein | `FontFace`-Deskriptoren mit JavaScript-Namen: `weight`, `style`, `stretch`, `display`, `unicodeRange`, `featureSettings`, `variationSettings`, `ascentOverride`, `descentOverride`, `lineGapOverride`. Werte sind Zeichenketten; `weight` akzeptiert auch Zahlen. |

Verwende einen eigenen Eintrag je Stärke oder Stil. Variable Fonts können einen Bereich wie `weight: "100 900"` angeben. Dateien unter `/config/www/fonts/` werden unter `/local/fonts/` ausgeliefert. Entfernte Server müssen ursprungsübergreifende Schriftanfragen erlauben. Die Deskriptoren entsprechen der Browser-API `FontFace`; die Unterstützung für `variationSettings`, `ascentOverride`, `descentOverride` und `lineGapOverride` variiert, Safari kann einzelne Werte ignorieren.

Schriften folgen dem **globalen Home-Assistant-Theme**, einschließlich `modes.light` und `modes.dark`. Das `uix-fonts` eines Modus ersetzt die Basiszuordnung; `uix-fonts: "{}"` verwendet keine eigenen Schriften. Zeigt `uix-theme` auf ein anderes Theme, wird dessen Schriftzuordnung verwendet. Alte `card-mod-theme`-Referenzen werden unterstützt. Ein nur für eine View, Karte oder über `uix.theme` gewähltes Theme lädt keine Schriften.

UIX lädt Schriften, ohne die Styles aufzuhalten, und registriert identische Einträge einmal. Theme-Wechsel oder Neuladen entfernen nicht mehr benötigte UIX-Registrierungen, auch noch ladende Schriften. Registrierungen von Home Assistant oder anderen Integrationen bleiben erhalten. Ungültige Einträge und fehlgeschlagene Downloads erzeugen Konsolenwarnungen, ohne andere Schriften oder Styles zu blockieren. Lade die Themes neu, um fehlgeschlagene Downloads erneut zu versuchen.

`uix-fonts` akzeptiert eine statische YAML-Zuordnung ohne Templates. Es fügt weder CSS noch `<style>`-Elemente in den Dokumentkopf ein.

## Dialoge

`uix-dialog` und `uix-dialog-yaml` gelten für Styles, die im Dialog-Element verwurzelt sind. Das kann `ha-dialog`, `ha-adaptive-dialog` oder `ha-drawer` sein. Dialoge erhalten außerdem eine Klasse `type-<dialog-type>`, wobei `<dialog-type>` der Elementname ohne `ha-`-Prefix ist.

Der Home-Assistant-Dialogmanager legt Dialoge im Shadow Root des obersten `<home-assistant>`-Elements ab. Der aktive Dialog ist das letzte Kind dieses Shadow Roots. Um das Ziel zu prüfen, sollte dieses letzte Kind im Browser-Inspector angesehen werden.

## Makros

Themes können wiederverwendbare Jinja2-Makros definieren, die allen Karten mit diesem Theme zur Verfügung stehen. Makros werden unter `uix-macros-yaml` als YAML-Dictionary definiert. Siehe [Templates - Makros](./templates#makros) für die vollständige Makro-Konfiguration.

```yaml
my-awesome-theme:
  uix-theme: my-awesome-theme

  uix-macros-yaml: |
    is_on:
      params:
        - entity_id
      returns: true
      template: "{%- do returns(is_state(entity_id, 'on')) -%}"
    badge_color:
      params:
        - entity_id
        - name: color_on
          default: "'var(--state-active-color)'"
        - name: color_off
          default: "'var(--state-inactive-color)'"
      template: "{{ color_on if is_on(entity_id) else color_off }}"
```

Badge-Beispiel mit Standardwerten für `badge_color()`:

```yaml
badges:
  - type: entity
    entity: light.bed_light
    tap_action:
      action: toggle
    uix:
      style: |
        ha-badge {
          --badge-color: {{ badge_color(config.entity) }} !important;
        }
```

![Example using theme macros with defaults](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-macros-badge-1.gif)

Badge-Beispiel mit gesetztem benanntem Parameter `color_on='red'`:

```yaml
badges:
  - type: entity
    entity: light.bed_light
    tap_action:
      action: toggle
    uix:
      style: |
        ha-badge {
          --badge-color: {{ badge_color(config.entity, color_on='red') }} !important;
        }
```

![Example using theme macros with defaults](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/using/theme-macros-badge-2.gif)

Makros auf Kartenebene (`uix.macros`) haben Vorrang vor Theme-Makros mit demselben Namen.

::: warning
Theme-Makros sind nur in UIX-Styling-Templates verfügbar, nicht in UIX-Forge-`element`- oder `forge`-Templates. Nutze UIX Forge [Global Foundries](../forge/foundries#global-foundries), um `forge.macros` global oder pro `mold` zu definieren.
:::

## Community-Beispiele

Ausführliche Community- und Fremdbeispiele werden bewusst außerhalb der UIX-Dokumentation gesammelt, damit diese Doku nah am Originalprojekt bleibt.

- [Weitere interessante Beispiele: UIX Theme-Sammlung](/sammlung/weitere-beispiele#uix-theme-sammlung-von-mariusthvdb)
