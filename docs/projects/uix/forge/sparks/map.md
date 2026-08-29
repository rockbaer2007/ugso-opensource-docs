---
title: Map Spark
---
# Map Spark

Der Map Spark erweitert Home-Assistant-Karten mit Kartenfunktionen wie Zoom-Speicher, automatischem Einpassen, Tour-Modus, Verlaufsslider und Entity-Filter.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      memory: true
      fit_map: true
element:
  type: map
  entities:
    - person.max
    - device_tracker.phone
```

## Konfiguration

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `map` sein. |
| `memory` | boolean | `false` | Speichert Zoom und Kartenmitte vor Updates und stellt sie danach wieder her. |
| `fit_map` | boolean | `false` | Passt die Karte einmal an alle Entities an, sobald sie sichtbar ist. Nuetzlich fuer beim Laden versteckte Karten. |
| `tour` | boolean oder object | `false` | Aktiviert Tour-Modus. `true` nutzt Standards, ein Objekt passt die Tour an. |
| `hours_to_show` | boolean oder object | `false` | Aktiviert einen Slider fuer `hours_to_show`. `true` nutzt Standards. |
| `entity_filter` | boolean oder object | `false` | Aktiviert ein Dropdown zum Ein- und Ausblenden von Entities. `true` nutzt Standards. |

### `tour`

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `period` | string oder number | `10s` | Aufenthaltsdauer an jedem Punkt. Zahlen sind Millisekunden, Strings z. B. `30s` oder `2m`. |
| `zoom` | number | `14` | Standard-Zoom fuer Tourpunkte. |
| `icon_pause` | string | `mdi:pause` | Icon, wenn die Tour laeuft. |
| `icon_play` | string | `mdi:play` | Icon, wenn die Tour pausiert ist. |
| `icon_position` | object | `{bottom: 10px, right: 10px}` | CSS-Position des Buttons. Zahlen werden als Pixel behandelt. |
| `poi` | list | nicht gesetzt | Liste der Punkte. Ohne Liste werden die Entities der `ha-map` genutzt. |

Punkte in `poi`:

| Schluessel | Typ | Beschreibung |
| --- | --- | --- |
| `entity` | string | Entity-ID. Muss in der `entities`-Liste der Karte vorhanden sein. Latitude und Longitude kommen aus den State-Attributen. |
| `latitude` | number | Breitengrad, erforderlich wenn keine `entity` gesetzt ist. |
| `longitude` | number | Laengengrad, erforderlich wenn keine `entity` gesetzt ist. |
| `zoom` | number | Zoom nur fuer diesen Punkt. |

### `hours_to_show`

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `min` | number | `0` | Minimaler Stundenwert. |
| `max` | number | `24` | Maximaler Stundenwert. |
| `step` | number | `1` | Schrittweite. |
| `position` | object | `{bottom: 10px, right: 10px}` | CSS-Position der Slider-Kapsel. |
| `tooltip_distance` | number | `20` | Abstand des Slider-Tooltips vom Thumb in Pixeln. |

### `entity_filter`

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `position` | object | `{bottom: 10px, right: 10px}` | CSS-Position des Filterbuttons. |
| `size` | string | `s` | Buttongroesse, z. B. `s`, `m`, `l`. |
| `variant` | string | `neutral` | Buttonvariante, z. B. `brand`, `neutral`, `danger`, `warning`, `success`. |
| `appearance` | string | `filled` | Darstellung, z. B. `accent`, `filled`, `plain`. |
| `icon` | string | `mdi:filter-variant` | Start-Icon des Buttons. |
| `label` | string | `Filter` | Buttontext. Leer setzen, um den Text auszublenden. |
| `group` | boolean oder object | `false` | Gruppiert Entities nach Domain. `true` nutzt Standardlabels, ein Objekt setzt eigene Labels. |

#### Gruppierung

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `persons` | string | `Persons` | Label fuer `person`-Entities. |
| `trackers` | string | `Trackers` | Label fuer `device_tracker`-Entities. |
| `zones` | string | `Zones` | Label fuer `zone`-Entities. |

## CSS-Variablen

### Tour

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-map-tour-icon-color` | `var(--primary-color)` | Iconfarbe. |
| `--uix-map-tour-icon-ring-color` | `var(--uix-map-tour-icon-color)` | Farbe des Countdown-Rings. |
| `--uix-map-tour-icon-background` | `rgba(255,255,255,0.8)` | Buttonhintergrund. |
| `--uix-map-tour-icon-box-shadow` | `0 1px 5px rgba(0,0,0,0.4)` | Schatten des Iconcontainers. |
| `--uix-map-tour-icon-width` | `auto` | Buttonbreite. |
| `--uix-map-tour-icon-height` | `auto` | Buttonhoehe. |
| `--uix-map-tour-icon-border-radius` | `9999px` | Rundung des Buttons. |
| `--uix-map-tour-icon-z-index` | `1000` | Stapelreihenfolge. Leaflet-Kontrollen nutzen ebenfalls `1000`. |

### Hours to Show

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-map-slider-background` | `rgba(255,255,255,0.8)` | Hintergrund der Slider-Kapsel. |
| `--uix-map-slider-text-color` | `var(--primary-text-color, #212121)` | Textfarbe des Dauerlabels. |
| `--uix-map-slider-width` | `100px` | Breite des Sliders. |
| `--uix-map-slider-border-radius` | `9999px` | Rundung der Kapsel. |
| `--uix-map-slider-padding` | `4px 12px` | Innenabstand. |
| `--uix-map-slider-box-shadow` | `0 1px 5px rgba(0,0,0,0.4)` | Schatten. |
| `--uix-map-slider-z-index` | `1000` | Overlay-Ebene. |
| `--uix-map-slider-label-min-width` | `28px` | Mindestbreite des Labels. |
| `--uix-map-slider-thumb-size` | nicht gesetzt | Hoehe und Breite des Thumbs zusammen. |
| `--uix-map-slider-thumb-height` | `16px` | Thumb-Hoehe. |
| `--uix-map-slider-thumb-width` | `16px` | Thumb-Breite. |
| `--uix-map-slider-track-size` | `4px` | Dicke der Slider-Spur. |
| `--uix-map-slider-track-color` | `var(--disabled-color)` | Grundfarbe der Spur. |
| `--uix-map-slider-indicator-color` | `var(--primary-color)` | Farbe der aktiven Anzeige. |
| `--uix-map-slider-thumb-color` | `var(--uix-map-slider-indicator-color)` | Thumb-Farbe. |
| `--uix-map-slider-tooltip-background-color` | `var(--secondary-background-color)` | Hintergrund des Tooltips. |

### Entity Filter

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-map-entity-filter-background` | `rgba(255,255,255,0.8)` | Hintergrund des Filtercontainers. |
| `--uix-map-entity-filter-padding` | `4px` | Innenabstand. |
| `--uix-map-entity-filter-border-radius` | `9999px` | Rundung. |
| `--uix-map-entity-filter-box-shadow` | `0 1px 5px rgba(0,0,0,0.4)` | Schatten. |
| `--uix-map-entity-filter-z-index` | `1000` | Overlay-Ebene. |
| `--uix-map-entity-filter-dropdown-min-width` | `180px` | Mindestbreite des Dropdowns. |
| `--uix-map-entity-filter-item-icon-color` | `var(--ha-color-fill-neutral-loud-resting)` | Farbe des Check-Icons. |
| `--uix-map-entity-filter-item-icon-checked-color` | `var(--uix-map-entity-filter-item-icon-color, var(--primary-color))` | Farbe des Check-Icons im ausgewaehlten Zustand. |

## Wie es funktioniert

Der Spark erweitert die vorhandene `ha-map`-Karte im Frontend. Er speichert UI-Zustand lokal im laufenden Dashboard, blendet zusaetzliche Overlays ein und setzt Werte wie `hours_to_show` direkt an der Karte.

::: note
Der Spark arbeitet mit der gerenderten Home-Assistant-Karte. Wenn Home Assistant intern Markup aendert, kann ein Update der UIX-Selektoren oder des Sparks erforderlich werden.

:::
## Beispiele

### `fit_map` mit Auto-Entities

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      fit_map: true
element:
  type: custom:auto-entities
  card:
    type: map
  filter:
    include:
      - domain: person
```

### Tour mit Standardwerten

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      tour: true
element:
  type: map
  entities:
    - person.max
    - person.erika
```

### Tour mit eigener POI-Liste

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      tour:
        period: 20s
        zoom: 15
        poi:
          - entity: person.max
          - latitude: 50.356
            longitude: 7.589
            zoom: 13
element:
  type: map
  entities:
    - person.max
```

### Tour-Button stylen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      tour: true
element:
  type: map
  entities:
    - person.max
uix:
  style: |
    :host {
      --uix-map-tour-icon-background: var(--card-background-color);
      --uix-map-tour-icon-color: var(--primary-color);
    }
```

### Verlaufsslider

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      hours_to_show:
        min: 0
        max: 48
        step: 1
element:
  type: map
  hours_to_show: 6
  entities:
    - device_tracker.phone
```

### Entity-Filter

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: map
      entity_filter:
        label: Filter
        group:
          persons: Personen
          trackers: Tracker
          zones: Zonen
element:
  type: map
  entities:
    - person.max
    - device_tracker.phone
    - zone.home
```

## `memory` im Detail

`memory` verhindert, dass die Karte bei jedem Home-Assistant-Update auf den urspruenglichen Ausschnitt zurueckspringt.

```yaml
forge:
  sparks:
    - type: map
      memory: true
```

Das ist besonders nuetzlich, wenn viele Tracker aktualisiert werden oder wenn die Karte in einer Live-Ansicht lange offen bleibt.

## `fit_map` im Detail

`fit_map` passt die Karte an alle sichtbaren Entities an, sobald die Map sichtbar ist. Das hilft bei Karten, die beim Laden in Tabs, Expandern oder Conditional Cards versteckt sind.

```yaml
forge:
  sparks:
    - type: map
      fit_map: true
```

## Tour mit Entity- und Koordinatenpunkten

```yaml
forge:
  sparks:
    - type: map
      tour:
        period: 15s
        zoom: 14
        poi:
          - entity: person.max
          - entity: device_tracker.car
            zoom: 16
          - latitude: 50.356
            longitude: 7.589
            zoom: 13
```

Entity-POIs muessen in der `entities`-Liste der `map`-Karte stehen, damit Home Assistant sie kennt.

## Slider positionieren

```yaml
forge:
  sparks:
    - type: map
      hours_to_show:
        min: 0
        max: 72
        step: 6
        position:
          bottom: 12
          left: 12
```

## Filter ohne Label

```yaml
forge:
  sparks:
    - type: map
      entity_filter:
        label: ""
        icon: mdi:filter
        position:
          top: 12
          right: 12
```

## Filtergruppen deutsch benennen

```yaml
forge:
  sparks:
    - type: map
      entity_filter:
        group:
          persons: Personen
          trackers: Geraete
          zones: Zonen
```

## Styling-Beispiel fuer alle Overlays

```yaml
uix:
  style: |
    :host {
      --uix-map-tour-icon-background: var(--card-background-color);
      --uix-map-slider-background: var(--card-background-color);
      --uix-map-entity-filter-background: var(--card-background-color);
      --uix-map-slider-box-shadow: var(--ha-card-box-shadow);
      --uix-map-entity-filter-box-shadow: var(--ha-card-box-shadow);
    }
```

## Hinweise

| Funktion | Wann sinnvoll |
| --- | --- |
| `memory` | Wenn Nutzer manuell zoomen oder verschieben |
| `fit_map` | Wenn die Karte beim Laden versteckt ist |
| `tour` | Fuer Uebersichten mehrerer Personen, Fahrzeuge oder Orte |
| `hours_to_show` | Fuer Tracker-Verlauf direkt in der Karte |
| `entity_filter` | Wenn viele Entities in einer Map liegen |
