---
title: UIX Forge
description: Deutsche Referenz für UIX Forge, Molds, Templates, Billets, Styling und Sparks
---
# UIX Forge

UIX Forge erzeugt Home-Assistant-Frontend-Elemente aus YAML und erweitert sie optional mit Sparks. Damit kannst du Karten, Zeilen, Badges, Picture-Elements, Sections, Footer und Card-Features erzeugen, ohne eine eigene Custom Card schreiben zu müssen.

::: tip In UIX Forge einhüllen
Forge ist besonders nützlich, wenn eine bestehende Karte fast passt, aber ein Button, Tooltip, Lock, Hintergrund, More-info-Bereich oder ein anderes Zusatzverhalten fehlt.

:::
## Grundstruktur

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
```

`forge` beschreibt, wie und in welchem Kontext das Element erzeugt wird. `element` enthält die eigentliche Home-Assistant-Konfiguration. Optional kann `uix` Styling für das erzeugte Element enthalten.

## Forge-Optionen

| Schlüssel | Typ | Templates | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `mold` | string | nein | Pflicht | Art des erzeugten Elements. Standard-Molds: `card`, `badge`, `row`, `picture-element`, `section`, `footer`, `card-feature`. Cross-Context-Molds: `card_as_row`, `card_as_badge`, `row_as_card`, `row_as_badge`, `badge_as_card`, `badge_as_row`, `badge_as_picture_element`. |
| `macros` | mapping | nein | - | Template-Makros, die allen Templates in der Forge-Konfiguration zur Verfügung stehen. Sie werden auch an `uix`-Konfigurationen in Forge und erzeugtem Element weitergegeben. |
| `billets` | mapping | nein | - | Benannte YAML-Werte als Template-Konstanten für alle Templates in der Forge-Konfiguration. |
| `hidden` | boolean | ja | `false` | Blendet das Element aus, wenn der Wert wahr ist. |
| `grid_options` | mapping | ja | - | Lovelace-Grid-Optionen wie `rows` und `columns`, nur für `mold: card`. |
| `show_error` | boolean | nein | `false` | Bei `true` wird bei Fehlern die Lovelace-Fehlerkarte angezeigt, statt das Element zu verstecken. |
| `template_nesting` | string | nein | `"<<>>"` | Vier Zeichen zum Escapen verschachtelter Templates. Standard: `<<...>>` für `&#123;&#123;...&#125;&#125;` und `<%...%>` für `&#123;%...%&#125;`. |
| `sparks` | list | ja | `[]` | Liste von [Spark-Konfigurationen](./sparks/), die an das erzeugte Element angehängt werden. |
| `delayed_hass` | boolean | nein | - | Verzögert die Übergabe des `hass`-Objekts, bis die Karte geladen ist. Hilft bei manchen Custom Cards, z. B. ApexCharts. |

::: warning
Nicht jede Option ist in jedem Mold sinnvoll. `grid_options` wird zum Beispiel nur bei `mold: card` beachtet.

:::
## Element-Konfiguration

`element` ist die YAML-Konfiguration des Home-Assistant-Elements, das Forge erzeugen soll.

::: details Forge-Beispiel
```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: sensor.outdoor_temperature
```

:::
Bei `mold: card` entspricht `element` einer normalen Lovelace-Karte. Bei `mold: row` entspricht es einer Entity-Row. Bei `mold: badge` entspricht es einem Badge.

### Entity-Konfiguration im Element

Viele Home-Assistant-Elemente erwarten `entity`. Forge reicht diese Konfiguration unverändert weiter.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.kitchen
  name: Kueche
```

### Blank-Card-Konfiguration

Eine Blank Card ist nützlich, wenn du ein leeres Ziel für Sparks oder UIX-Styling brauchst.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: custom:uix-forge-blank-card
```

Mit Inhalt:

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.living_room
    - type: tile
      entity: sensor.living_room_temperature
```

Mit Sparks:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      columns: 2
      gap: 8
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.living_room
    - type: tile
      entity: light.kitchen
```

::: tip
Bei Blank Cards zeigen viele Sparks standardmäßig auf `uix-forge-blank-card $ div.content`.

:::
## Template-Variablen und Makros

| Kontext | Template-Variablen |
| --- | --- |
| Templates in Forge und Element, außer `uix`-Styling | Forge-Konfiguration: `config.forge`; Element-Konfiguration: `config.element`; `config.entity`, falls in globaler `uix-forge`-Konfiguration enthalten. |
| Templates im Forge-`uix`-Styling | Forge-Konfiguration: `config.forge`; Element-Konfiguration: `config.element`; `config.entity`, falls enthalten. |
| Templates im `uix`-Styling des Elements | Forge-Konfiguration nicht verfügbar; Element-Konfiguration als `config`; `config.entity`, falls enthalten. |

::: tip
Makros eignen sich für wiederholte CSS- oder YAML-Schnipsel, etwa Farben, Zustandslabels oder DOM-Pfade.

:::
::: warning
In VitePress muss Jinja-Syntax in Markdown-Beispielen escaped werden. In echtem Home-Assistant-YAML schreibst du natürlich normale Jinja-Klammern.

:::
### Vollbeispiel mit Makro

```yaml
type: custom:uix-forge
forge:
  mold: card
  macros:
    state_color: |
      &#123;% macro state_color(entity) -%&#125;
      &#123;&#123; 'var(--success-color)' if is_state(entity, 'on') else 'var(--disabled-color)' &#125;&#125;
      &#123;%- endmacro %&#125;
element:
  type: tile
  entity: light.living_room
uix:
  style: |
    ha-card {
      border-color: &#123;&#123; state_color(config.element.entity) &#125;&#125;;
    }
```

### Billets

Billets sind benannte YAML-Werte, die in Templates als Konstanten genutzt werden können. Sie sind praktisch für Defaults, Farben, Entity-IDs oder Textbausteine.

::: warning
Billets sind Konfiguration, keine sichere Geheimnisablage. Für sensible Werte nutze Home-Assistant-Secrets oder passende Backend-Mechanismen.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  billets:
    main_entity: light.living_room
    accent_color: var(--primary-color)
element:
  type: tile
  entity: "&#123;&#123; main_entity &#125;&#125;"
uix:
  style: |
    ha-card {
      border-color: &#123;&#123; accent_color &#125;&#125;;
    }
```

#### Billet-Typen

| YAML-Typ | Beispiel | Jinja2-Typ | Nutzung im Template |
| --- | --- | --- | --- |
| Leer (`~` oder `null`) | `my_billet: ~` | `none` | `&#123;&#123; my_billet &#125;&#125;` ergibt leer |
| String | `my_billet: hello` | `str` | `&#123;&#123; my_billet &#125;&#125;` ergibt `hello` |
| Zahl | `my_billet: 42` | `int` oder `float` | `&#123;&#123; my_billet + 1 &#125;&#125;` ergibt `43` |
| Boolean | `my_billet: true` | `bool` | `&#123;% if my_billet %&#125;...&#123;% endif %&#125;` |
| Liste | `my_billet: [1, 2, 3]` | `list` | `&#123;&#123; my_billet | join(', ') &#125;&#125;` |
| Mapping | `my_billet: {a: 1}` | `dict` | `&#123;&#123; my_billet.a &#125;&#125;` |

#### Billet-Interpolation

Billets können andere Billets referenzieren.

```yaml
forge:
  billets:
    room: living_room
    entity: "light.&#123;&#123; room &#125;&#125;"
element:
  type: tile
  entity: "&#123;&#123; entity &#125;&#125;"
```

Mehrere Werte können zusammengesetzt werden:

```yaml
forge:
  billets:
    domain: sensor
    object_id: outdoor_temperature
    entity: "&#123;&#123; domain &#125;&#125;.&#123;&#123; object_id &#125;&#125;"
```

::: note Zirkuläre Referenzen
Billets dürfen sich nicht gegenseitig endlos referenzieren. Halte Abhängigkeiten einfach und eindeutig.

:::
#### Billets und Foundries

Foundries können Billets definieren, die einzelne Forge-Instanzen überschreiben. Das ist der bevorzugte Weg für wiederverwendbare Kartenmuster.

## Templates im Element ignorieren

Manche erzeugten Elemente enthalten selbst Jinja-ähnliche Syntax. Dann musst du verschachtelte Templates escapen, damit Forge sie nicht zu früh auswertet.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: markdown
  content: |
    << states('sensor.outdoor_temperature') >>
```

::: warning Templates ignorieren und mehrere Forge-Schichten
Wenn mehrere Forge-Schichten ineinander liegen, braucht jede zusätzliche Ebene ein weiteres Paar Nesting-Zeichen.

:::
### Template-Nesting

Mit `template_nesting` legst du fest, welche Zeichen für verschachtelte Jinja-Ausdrücke verwendet werden.

```yaml
forge:
  template_nesting: "<<>>"
element:
  type: markdown
  content: "<< states('sensor.outdoor_temperature') >>"
```

#### Mehrere Verschachtelungsebenen

Bei zwei Ebenen nutzt du ein weiteres Klammerpaar, zum Beispiel `<<< ... >>>` für den inneren Ausdruck.

#### Template-Nesting und Makros

Makros können ebenfalls verschachtelte Templates ausgeben. Wichtig ist, dass die Ebene, die das Template auswerten soll, die Syntax erkennt.

::: tip
Wenn ein Template zu früh ausgewertet wird, ist das fast immer ein Nesting-Problem.

:::
#### Billets in verschachtelten Templates

Billets stehen auch in verschachtelten Templates zur Verfügung, sofern sie auf der auswertenden Ebene sichtbar sind.

::: note Von decluttering-card kommend?
Forge deckt viele Muster ab, die sonst mit `decluttering-card` gebaut werden. Der wichtigste Unterschied: Forge erzeugt echte Home-Assistant-Elemente und kann zusätzlich Sparks anwenden.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  billets:
    entity: light.living_room
element:
  type: tile
  entity: "&#123;&#123; entity &#125;&#125;"
```

```jinja
&#123;% if is_state(entity, 'on') %&#125;
  eingeschaltet
&#123;% endif %&#125;
```

::: tip
Halte Vorlagen klein. Wenn ein Template schwer lesbar wird, lagere wiederholte Teile in Makros oder Foundries aus.

:::
### Nutzung mit Auto-Entities

Forge kann mit `custom:auto-entities` kombiniert werden, wenn automatisch gefundene Entities als erzeugte Karten, Reihen oder Badges eingesetzt werden sollen.

```yaml
type: custom:auto-entities
card:
  type: vertical-stack
card_param: cards
filter:
  include:
    - domain: light
      options:
        type: custom:uix-forge
        forge:
          mold: card
        element:
          type: tile
          entity: this.entity_id
```

::: tip
Bei Auto-Entities ist es besonders wichtig, mit Fallbacks zu arbeiten, weil nicht jede Entity dieselben Attribute besitzt.

:::
## UIX-Styling

Forge kann sowohl die erzeugte Karte als auch deren innere Elemente mit UIX stylen.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
uix:
  style: |
    ha-card {
      border: 1px solid var(--primary-color);
    }
```

### Element-Styling

`uix` auf oberster Ebene stylt das Forge-Ergebnis. `uix` innerhalb von `element` gehört zur eigentlichen Elementkonfiguration.

::: warning
Die verfügbaren Template-Variablen unterscheiden sich je nach Ebene. Im Element-`uix` ist die Elementkonfiguration als `config` sichtbar, nicht als `config.element`.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
  uix:
    style: |
      ha-card {
        color: var(--primary-text-color);
      }
```

### Theme-Styling

UIX-Themes können Forge-Molds gezielt stylen. Nutze die bekannten Variablen wie `uix-card`, `uix-row`, `uix-badge` oder spezifischere Klassen.

## Sections

Forge kann Sections für die neue Dashboard-Section-Ansicht erzeugen.

```yaml
type: custom:uix-forge
forge:
  mold: section
element:
  type: heading
  heading: Wohnzimmer
```

```yaml
# Nur Hauptkonfiguration fuer Sections. Visibility wird nicht unterstuetzt.
type: custom:uix-forge
forge:
  mold: section
element:
  type: grid
  cards:
    - type: tile
      entity: light.living_room
```

::: warning
Section-Konfiguration folgt den Home-Assistant-Regeln für Sections. Nicht jede Kartenoption ist dort gültig.

:::
## Footer

Mit `mold: footer` kann Forge einen Footer erzeugen, der unten im Viewport sitzt.

::: note
Footer sind für kompakte, dauerhaft sichtbare Bedienelemente gedacht. Sie sollten nicht zu viel Inhalt aufnehmen.

:::
| Schlüssel | Typ | Templates | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `max_width` | string | nein | `600` | Maximale Breite des Footers in Pixeln. |

```yaml
type: custom:uix-forge
forge:
  mold: footer
  max_width: 600
element:
  type: horizontal-stack
  cards:
    - type: button
      entity: light.living_room
    - type: button
      entity: light.kitchen
```

Footer-Variablen:

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-forge-footer-border-width` | `1px` | Rahmenbreite der erzeugten Karte im Footer. |
| `--uix-forge-footer-bottom` | `var(--ha-space-2)` | Abstand vom unteren Viewport-Rand. |
| `--uix-forge-footer-padding` | `0 var(--ha-space-2)` | Padding des Footer-Containers. |

### Visibility

```yaml
type: custom:uix-forge
forge:
  mold: footer
  hidden: "&#123;&#123; is_state('input_boolean.hide_footer', 'on') &#125;&#125;"
element:
  type: button
  entity: input_boolean.hide_footer
```

## Card Features

Mit `mold: card-feature` können Card-Feature-Elemente erzeugt werden, die in Cards verwendet werden.

```yaml
type: custom:uix-forge
forge:
  mold: card-feature
element:
  type: toggle
```

In einer Tile Card:

```yaml
type: tile
entity: light.living_room
features:
  - type: custom:uix-forge
    forge:
      mold: card-feature
    element:
      type: toggle
```

## Cross-Context-Molds

Cross-Context-Molds erzeugen ein Element in einem Kontext, lassen es aber in einem anderen Kontext auftreten.

| Mold | Erzeugt | Verhält sich wie |
| --- | --- | --- |
| `card_as_row` | `hui-card` | Row in `entities` oder `fold-entity-row` |
| `card_as_badge` | `hui-card` | Badge in einem Badge-Container |
| `row_as_card` | Row-Element | Karte im Kartengrid |
| `row_as_badge` | Row-Element | Badge in einem Badge-Container |
| `badge_as_card` | `hui-badge` | Karte im Kartengrid |
| `badge_as_row` | `hui-badge` | Row in `entities` oder `fold-entity-row` |
| `badge_as_picture_element` | `hui-badge` | Picture-Element in einer Picture-Elements-Karte |

### `card_as_row`: Karte als Zeile einbetten

```yaml
type: entities
entities:
  - type: custom:uix-forge
    forge:
      mold: card_as_row
    element:
      type: tile
      entity: light.living_room
```

### Badge als Picture-Element einbetten

```yaml
type: picture-elements
image: /local/floorplan.png
elements:
  - type: custom:uix-forge
    forge:
      mold: badge_as_picture_element
    element:
      type: entity
      entity: light.living_room
    style:
      top: 40%
      left: 60%
```

::: tip Visibility
Wenn Sichtbarkeit benötigt wird, prüfe zuerst, ob Home Assistant sie in diesem Kontext direkt unterstützt. Forge kann Elemente ausblenden, aber manche Container erwarten trotzdem bestimmte Elementformen.

:::
## Praxis: welche Mold für welchen Zweck?

| Ziel | Geeignete Mold | Typischer Einsatz |
| --- | --- | --- |
| Normale Dashboard-Karte | `card` | Tile, Entities, Markdown, Map, Custom Cards |
| Zeile in Entities-Karte | `row` | Entity-Row, Template-Entity-Row, Fold-Entity-Row |
| Badge im Kopfbereich | `badge` | Entity-Badge, Status-Badge, Shortcut-Badge |
| Element in Picture-Elements | `picture-element` | Marker, Badge, Button auf Grundriss |
| Abschnitt in Sections View | `section` | Heading, Grid oder Section-Inhalt |
| Fester unterer Bereich | `footer` | Schnellaktionen, Navigation, Raumumschalter |
| Feature in Tile Card | `card-feature` | Toggle, Slider oder andere Feature-Elemente |

Cross-Context-Molds nutzt du nur, wenn Home Assistant ein Element in einem anderen Kontext erwartet als die Karte, die du eigentlich erzeugen möchtest. Das ist mächtig, aber auch empfindlicher gegen Änderungen im Frontend.

## Komplettes Forge-Beispiel

Dieses Beispiel kombiniert Template, Billets, Sparks und UIX-Styling:

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 8
    rows: 1
  billets:
    entity: light.living_room
    label: Wohnzimmer
  sparks:
    - type: tooltip
      for: hui-tile-card $ ha-tile-icon
      content: "&#123;&#123; label &#125;&#125;: &#123;&#123; states(entity) &#125;&#125;"
    - type: button
      after: hui-tile-card $ ha-tile-info
      label: Umschalten
      entity: "&#123;&#123; entity &#125;&#125;"
      tap_action:
        action: toggle
    - type: overlay-icon
      for: hui-tile-card $ ha-tile-icon
      icon: "&#123;&#123; 'mdi:check' if is_state(entity, 'on') else 'mdi:minus' &#125;&#125;"
      icon_background: "&#123;&#123; 'var(--success-color)' if is_state(entity, 'on') else 'var(--disabled-color)' &#125;&#125;"
element:
  type: tile
  entity: "&#123;&#123; entity &#125;&#125;"
  name: "&#123;&#123; label &#125;&#125;"
uix:
  style: |
    ha-card {
      border: 1px solid var(--divider-color);
    }
    ha-button {
      margin-left: auto;
    }
```

## Fehleranzeige und Fehlersuche

Mit `show_error: true` zeigt Forge bei Problemen die Lovelace-Fehlerkarte. Das ist beim Entwickeln hilfreich, weil falsche Molds, ungültiges YAML oder fehlende Entities sonst nur als verschwundenes Element wirken können.

```yaml
type: custom:uix-forge
forge:
  mold: card
  show_error: true
element:
  type: tile
  entity: sensor.does_not_exist
```

Nach dem Debuggen kannst du `show_error` wieder entfernen oder auf `false` setzen.

## `hidden` mit Templates

`hidden` kann als Boolean oder Template genutzt werden.

```yaml
type: custom:uix-forge
forge:
  mold: card
  hidden: "&#123;&#123; not is_state('input_boolean.show_lights', 'on') &#125;&#125;"
element:
  type: tile
  entity: light.living_room
```

Bei Template-Ausdrücken sollte das Ergebnis klar wahr oder falsch sein. Nutze einfache Bedingungen und Fallbacks.

## `grid_options`

`grid_options` wird an Lovelace weitergegeben, wenn Forge eine Karte erzeugt.

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 6
    rows: 2
element:
  type: tile
  entity: sensor.energy_today
```

Das beeinflusst die Position und Größe der Karte in Home Assistants Grid-Layout, nicht das interne Layout der Karte. Für internes Layout ist der [Grid Spark](./sparks/grid) gedacht.

## `delayed_hass`

Einige Custom Cards reagieren empfindlich, wenn `hass` sehr früh gesetzt wird. `delayed_hass` wartet, bis die Karte geladen ist.

```yaml
type: custom:uix-forge
forge:
  mold: card
  delayed_hass: true
element:
  type: custom:apexcharts-card
  graph_span: 24h
  series:
    - entity: sensor.energy_today
```

Setze diese Option nur, wenn du sie wirklich brauchst, zum Beispiel bei Konsolenfehlern oder fehlerhaft initialisierten Custom Cards.

## Sparks kombinieren

Sparks werden in der Reihenfolge verarbeitet, in der sie in `forge.sparks` stehen. Wenn ein Spark ein Element erzeugt und ein anderer Spark dieses Element verwenden soll, muss der erzeugende Spark vorher stehen.

```yaml
forge:
  mold: card
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-info
      label: Mehr
      entity: light.living_room
      tap_action:
        action: more-info
    - type: tooltip
      for: hui-tile-card $ ha-button
      content: Details oeffnen
```

## Forge mit Reihen

`mold: row` erzeugt eine Zeile für Karten, die Row-Elemente erwarten.

```yaml
type: entities
entities:
  - type: custom:uix-forge
    forge:
      mold: row
      sparks:
        - type: tooltip
          content: Direkte UIX-Zeile
    element:
      type: custom:template-entity-row
      entity: light.living_room
      name: Wohnzimmer
```

## Forge mit Badges

`mold: badge` erzeugt ein Badge für den Dashboard-Kopfbereich.

```yaml
badges:
  - type: custom:uix-forge
    forge:
      mold: badge
      sparks:
        - type: tooltip
          content: Haustuerstatus
    element:
      type: entity
      entity: binary_sensor.front_door
```

## Forge mit Picture-Elements

```yaml
type: picture-elements
image: /local/floorplan.png
elements:
  - type: custom:uix-forge
    forge:
      mold: picture-element
      sparks:
        - type: lock
          locks:
            - confirmation: Licht schalten?
    element:
      type: state-icon
      entity: light.living_room
    style:
      top: 45%
      left: 55%
```

## Empfehlungen

- Starte mit einer minimalen Forge-Konfiguration und füge danach Sparks hinzu.
- Nutze `show_error: true`, solange du an einer neuen Forge-Struktur arbeitest.
- Halte DOM-Selektoren so genau wie nötig und so kurz wie möglich.
- Verwende Billets für Werte, die pro Instanz austauschbar bleiben sollen.
- Verwende Foundries, sobald du dieselbe Forge-Struktur mehrfach brauchst.
- Nutze Cross-Context-Molds nur dort, wo Home Assistant wirklich einen anderen Kontext verlangt.

## Verwandte Seiten

- [Foundries](./foundries) für wiederverwendbare Forge-Vorlagen.
- [Sparks](./sparks/) für optionale Verhalten.
- [DOM-Navigation](../concepts/dom) für Selektoren mit Shadow-DOM-Wechseln.
- [Templates](../using/templates) für Jinja-Variablen, Makros und Hash-Werte.
