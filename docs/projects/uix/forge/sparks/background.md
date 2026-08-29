---
title: Background Spark
---
# Background Spark

Der Background Spark fuegt einem Forge-Element eine eigene Hintergrundebene hinzu. Der Vordergrund bleibt davon getrennt, sodass du Hintergrundbild, Kamera, Video, Farbe und Deckkraft steuern kannst, ohne die Lesbarkeit des eigentlichen Elements direkt zu veraendern.

| Quelle | Schluessel | Beschreibung |
| --- | --- | --- |
| Kamera | `camera_entity` | Live-Stream ueber `ha-camera-stream`. Unterstuetzt Zoom, Pan und Position. Zeigt waehrend des Ladens einen Spinner. |
| Entity Picture | `image_entity` | Liest `entity_picture` aus einer Entity und signiert die URL. Zeigt waehrend des Ladens einen Spinner. |
| Video | `video_url` | Fuegt ein `<video>`-Element ein, automatisch startend, stumm und geloopt. Unterstuetzt `media-source://`-URIs. |
| Bild-URL | `image_url` | Statisches Bild als `background-image`. Unterstuetzt `media-source://`-URIs. |
| Farbe oder CSS-Shorthand | `background` | Beliebiger CSS-`background`-Wert oder Mapping einzelner Background-Eigenschaften. |

!!! tip
    Nutze `opacity`, um nur den Hintergrund abzudunkeln. Wenn du stattdessen das ganze Zielelement transparent machst, werden auch Text, Icons und Controls beeinflusst.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      for: hui-tile-card
      image_url: /local/backgrounds/living-room.jpg
      background:
        size: cover
        position: center
      opacity: 0.35
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `background` sein. |
| `for` | string | Bei Blank-Card-Konfiguration `uix-forge-blank-card $ div.content`, sonst `element`. | UIX-Selektor fuer das Zielelement. |
| `camera_entity` | string | - | Entity-ID einer `camera.*`-Entity fuer einen Live-Hintergrund. |
| `camera_zoom` | string oder number | - | CSS-Zoom oder Skalierung, z. B. `1.5` oder `"150%"`. |
| `camera_pan_x` | string oder number | - | CSS-Verschiebung auf der X-Achse, z. B. `"10%"` oder `"-20px"`. |
| `camera_pan_y` | string oder number | - | CSS-Verschiebung auf der Y-Achse. |
| `camera_position` | string | `center` | Positionierung des Streams: `center`, `top`, `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right`. |
| `camera_stream_cache_ms` | number | `20000` | Wie lange ein `ha-camera-stream` nach dem Entfernen im Cache bleibt. So kann ein Stream beim naechsten Aufbau wiederverwendet werden. |
| `image_entity` | string | - | Entity-ID, deren Attribut `entity_picture` als Hintergrundbild genutzt wird. |
| `video_url` | string | - | Video-URL. `media-source://` wird unterstuetzt. |
| `image_url` | string | - | Bild-URL. `media-source://` wird unterstuetzt. |
| `background` | string oder object | - | CSS-`background`-Shorthand oder Mapping einzelner Eigenschaften. Bei `image_entity` oder `image_url` koennen Objektwerte wie `position` und `size` das Bildlayout ueberschreiben. |
| `opacity` | number | - | CSS-Deckkraft der Hintergrundebene von `0` bis `1`. |
| `dissolve_target` | string oder list | - | Macht das Zielelement transparent, damit der Spark-Hintergrund sichtbar wird. |
| `class` | string | - | Zusaetzliche CSS-Klasse fuer den Hintergrundcontainer `<div>`. |

!!! tip
    Fuer Kameras empfiehlt sich ein explizites Seitenverhaeltnis oder eine klare Hoehe am Zielcontainer. Sonst kann der Stream je nach Karte ungewohnt zugeschnitten wirken.

## `background` als Mapping

| Schluessel | CSS-Eigenschaft |
| --- | --- |
| `color` | `background-color` |
| `image` | `background-image` |
| `position` | `background-position` |
| `size` | `background-size` |
| `repeat` | `background-repeat` |
| `attachment` | `background-attachment` |
| `origin` | `background-origin` |
| `clip` | `background-clip` |

```yaml
forge:
  sparks:
    - type: background
      for: hui-tile-card
      image_url: /local/backgrounds/room.jpg
      background:
        size: cover
        position: center
        repeat: no-repeat
```

## `dissolve_target`

`dissolve_target` entfernt oder reduziert den bestehenden Hintergrund des Zielelements. Das ist besonders wichtig bei Karten, deren eigenes `ha-card` sonst ueber der neuen Hintergrundebene liegt.

```yaml
forge:
  sparks:
    - type: background
      for: hui-tile-card
      image_url: /local/backgrounds/room.jpg
      dissolve_target:
        - background
        - box-shadow
```

```yaml
forge:
  sparks:
    - type: background
      for: hui-tile-card
      background: var(--primary-color)
      dissolve_target: opacity(0.5)
```

## Media-Source-URIs

Lokale Medien aus Home Assistant koennen ueber `media-source://` eingebunden werden.

```yaml
image_url: media-source://media_source/local/backgrounds/room.jpg
```

```yaml
video_url: media-source://media_source/local/videos/ambient.mp4
```

## Adapter

### Card-Adapter

Bei normalen Karten arbeitet der Spark mit dem erzeugten Kartenelement. Wenn kein `for` gesetzt ist, steht `element` fuer das Root-Element des Forge-Ergebnisses.

### Section-Adapter

Bei Sections kann der Hintergrund auf den Section-Container gelegt werden.

```yaml
type: custom:uix-forge
forge:
  mold: section
  sparks:
    - type: background
      image_url: /local/backgrounds/section.jpg
      background:
        size: cover
        position: center
element:
  type: heading
  heading: Wohnzimmer
```

## Beispiele

### Live-Kamera als Hintergrund

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      for: hui-tile-card
      camera_entity: camera.front_door
      camera_position: center
      camera_zoom: 1.2
      opacity: 0.55
      dissolve_target:
        - background
        - box-shadow
element:
  type: tile
  entity: binary_sensor.front_door_motion
```

### Entity Picture als Hintergrund

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      for: hui-tile-card
      image_entity: person.max
      background:
        size: cover
        position: center
      opacity: 0.3
element:
  type: tile
  entity: person.max
```

### Video-Hintergrund

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      video_url: /local/videos/fireplace.mp4
      opacity: 0.4
element:
  type: tile
  entity: sensor.living_room_temperature
```

### Statisches Bild

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      image_url: /local/backgrounds/kitchen.jpg
      background:
        size: cover
        position: 50% 35%
element:
  type: tile
  entity: light.kitchen
```

### Vollstaendiger CSS-Background

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      background: linear-gradient(135deg, rgba(0,0,0,.6), rgba(0,0,0,.1)), url("/local/backgrounds/room.jpg") center / cover no-repeat
element:
  type: tile
  entity: light.living_room
```

### Zustandsabhaengige Hintergrundfarbe

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      background: "&#123;&#123; 'var(--error-color)' if is_state('binary_sensor.window', 'on') else 'var(--success-color)' &#125;&#125;"
      opacity: 0.16
element:
  type: tile
  entity: binary_sensor.window
```

### Hintergrundcontainer mit UIX stylen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      class: soft-background
      image_url: /local/backgrounds/room.jpg
element:
  type: tile
  entity: light.living_room
uix:
  style: |
    .soft-background {
      filter: saturate(0.8);
    }
```

### Dashboard-Header erweitern

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: background
      for: ha-card
      image_url: /local/backgrounds/header.jpg
      background:
        size: cover
        position: center
      opacity: 0.35
element:
  type: heading
  heading: Zuhause
```
