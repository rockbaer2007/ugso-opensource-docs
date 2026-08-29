---
title: Grid Spark
---
# Grid Spark

Der Grid Spark setzt CSS Grid auf einen Container innerhalb eines Forge-Elements. Damit lassen sich die direkten Kinder eines Zielcontainers sauber in Spalten, Zeilen und benannte Bereiche verteilen.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: hui-tile-card
      columns: 2
      gap: 8px
element:
  type: tile
  entity: light.living_room
```

::: tip
Der Spark wirkt auf die direkten Kinder des Zielcontainers. Wenn sich scheinbar nichts aendert, pruefe im Browser-Inspektor, ob `for` wirklich den Container trifft, dessen Kinder du anordnen willst.

:::
## Konfiguration

### Basiseigenschaften

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `grid` sein. |
| `for` | `string` | nein | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor fuer den Zielcontainer. `$` wechselt in Shadow Roots. |
| `columns` | `number` oder `string` | nein | - | `grid-template-columns`. Eine Zahl wird zu `repeat(n, 1fr)`, ein String wird unveraendert verwendet. |
| `rows` | `number` oder `string` | nein | - | `grid-template-rows`. Gleiche Kurzform wie `columns`. |
| `gap` | `number` oder `string` | nein | - | Abstand fuer Zeilen und Spalten. Zahlen werden als Pixel interpretiert. |
| `column_gap` | `number` oder `string` | nein | - | Nur Spaltenabstand. |
| `row_gap` | `number` oder `string` | nein | - | Nur Zeilenabstand. |
| `auto_rows` | `string` | nein | - | Wert fuer `grid-auto-rows`, z. B. `minmax(100px, auto)`. |
| `auto_columns` | `string` | nein | - | Wert fuer `grid-auto-columns`. |
| `auto_flow` | `string` | nein | - | Wert fuer `grid-auto-flow`: `row`, `column`, `row dense` oder `column dense`. |
| `justify_items` | `string` | nein | - | Wert fuer `justify-items`: `start`, `end`, `center`, `stretch`. |
| `align_items` | `string` | nein | - | Wert fuer `align-items`: `start`, `end`, `center`, `stretch`. |
| `justify_content` | `string` | nein | - | Wert fuer `justify-content`. |
| `align_content` | `string` | nein | - | Wert fuer `align-content`. |
| `place_items` | `string` | nein | - | Kurzform fuer `<align-items> / <justify-items>`. |
| `place_content` | `string` | nein | - | Kurzform fuer `<align-content> / <justify-content>`. |
| `areas` | `string` | nein | - | Wert fuer `grid-template-areas`, z. B. `'"header header" "main sidebar"'`. |
| `elements` | `list[string]` | nein | `[]` | Namen fuer `grid-area`, die den direkten Kindern der Reihe nach zugewiesen werden. |
| `media_queries` | `list` | nein | `[]` | Responsive Ueberschreibungen, siehe unten. |

### Media Queries

| Schluessel | Typ | Pflicht | Beschreibung |
| --- | --- | --- | --- |
| `query` | `string` | ja | Normale CSS-Media-Query, z. B. `"(min-width: 768px)"`. |
| Grid-Eigenschaften | - | nein | Beliebige Grid-Eigenschaften wie `columns`, `rows`, `gap`, `areas`, `align_items` usw. |

::: tip
Die Werte in `media_queries` ueberschreiben nur die dort gesetzten Eigenschaften. Nicht genannte Eigenschaften bleiben aus der Basiskonfiguration erhalten.

:::
## Beispiele

### Zwei Spalten

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: hui-tile-card
      columns: 2
      gap: 12px
element:
  type: entities
  entities:
    - light.living_room
    - sensor.living_room_temperature
```

### Feste und flexible Spalten

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: hui-tile-card
      columns: "64px 1fr auto"
      align_items: center
      column_gap: 12px
element:
  type: tile
  entity: light.living_room
```

### Benannte Bereiche

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: uix-forge-blank-card $ div.content
      areas: '"icon name" "icon state"'
      columns: "48px 1fr"
      rows: "auto auto"
      gap: 4px 12px
      elements:
        - icon
        - name
        - state
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.living_room
```

### Responsive Umschaltung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: uix-forge-blank-card $ div.content
      columns: 1
      gap: 8
      media_queries:
        - query: "(min-width: 768px)"
          columns: 2
          gap: 12px
        - query: "(min-width: 1200px)"
          columns: "1fr 1fr 1fr"
          gap: 16px
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.kitchen
    - type: tile
      entity: light.living_room
    - type: tile
      entity: light.office
```

### Ausrichtung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      for: hui-tile-card
      columns: "auto 1fr"
      place_items: "center / stretch"
      gap: 10px
element:
  type: tile
  entity: sensor.energy_today
```

::: note
Der Grid Spark ersetzt keine komplette Dashboard-Layout-Engine. Er ist fuer das Layout innerhalb des erzeugten Elements gedacht.

:::
## `columns` und `rows` als Kurzform

Zahlen werden als gleich breite Tracks interpretiert.

```yaml
forge:
  sparks:
    - type: grid
      columns: 3
      rows: 2
```

Das entspricht sinngemaess:

```css
grid-template-columns: repeat(3, 1fr);
grid-template-rows: repeat(2, 1fr);
```

Strings werden direkt als CSS-Wert verwendet:

```yaml
forge:
  sparks:
    - type: grid
      columns: "minmax(80px, 160px) 1fr auto"
      rows: "auto minmax(120px, 1fr)"
```

## `elements` und Reihenfolge

`elements` vergibt `grid-area`-Namen an die direkten Kinder des Zielcontainers. Die Reihenfolge entspricht der DOM-Reihenfolge.

```yaml
forge:
  sparks:
    - type: grid
      areas: '"title actions" "content content"'
      columns: "1fr auto"
      elements:
        - title
        - actions
        - content
```

Wenn weniger Namen als Kinder vorhanden sind, bleiben die restlichen Kinder ohne `grid-area`. Wenn mehr Namen vorhanden sind, werden die ueberzaehligen Namen ignoriert.

## Typische Grid-Werte

| Ziel | Wert |
| --- | --- |
| Zwei gleich breite Spalten | `columns: 2` |
| Icon plus Text | `columns: "40px 1fr"` |
| Text plus Aktion | `columns: "1fr auto"` |
| Kompakte Kacheln | `columns: "repeat(auto-fit, minmax(120px, 1fr))"` |
| Gleichmaessiger Abstand | `gap: 8` |
| Unterschiedlicher Abstand | `gap: "6px 12px"` |

## Responsive Bereiche

```yaml
forge:
  sparks:
    - type: grid
      areas: '"title" "content" "actions"'
      columns: 1
      media_queries:
        - query: "(min-width: 900px)"
          areas: '"title actions" "content content"'
          columns: "1fr auto"
```

## Fehlerquellen

| Problem | Ursache | Loesung |
| --- | --- | --- |
| Grid wirkt nicht | `for` trifft kein Container-Element | DOM mit Inspektor pruefen |
| Kinder bleiben untereinander | Zielcontainer hat keine direkten Kinder | Einen tieferen Container waehlen |
| Bereiche passen nicht | `areas` und `elements` stimmen nicht zusammen | DOM-Reihenfolge pruefen |
| Mobile Ansicht zu eng | Feste Spalten | `media_queries` oder `minmax()` nutzen |
