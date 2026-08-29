---
title: Background Spark
---
# Background Spark

Der Background Spark fügt einem Forge-Element eine eigene Hintergrundebene hinzu. Der Vordergrund bleibt davon getrennt, sodass du Hintergrundbild, Kamera, Video, Farbe und Deckkraft steuern kannst, ohne die Lesbarkeit des eigentlichen Elements direkt zu verändern.

| Quelle | Schlüssel | Beschreibung |
| --- | --- | --- |
| Kamera | `camera_entity` | Live-Stream über `ha-camera-stream`. Unterstützt Zoom, Pan und Position. Zeigt während des Ladens einen Spinner. |
| Entity Picture | `image_entity` | Liest `entity_picture` aus einer Entity und signiert die URL. Zeigt während des Ladens einen Spinner. |
| Video | `video_url` | Fuegt ein `<video>`-Element ein, automatisch startend, stumm und geloopt. Unterstützt `media-source://`-URIs. |
| Bild-URL | `image_url` | Statisches Bild als `background-image`. Unterstützt `media-source://`-URIs. |
| Farbe oder CSS-Shorthand | `background` | Beliebiger CSS-`background`-Wert oder Mapping einzelner Background-Eigenschaften. |

::: tip
Nutze `opacity`, um nur den Hintergrund abzudunkeln. Wenn du stattdessen das ganze Zielelement transparent machst, werden auch Text, Icons und Controls beeinflusst.

:::
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

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `background` sein. |
| `for` | string | Bei Blank-Card-Konfiguration `uix-forge-blank-card $ div.content`, sonst `element`. | UIX-Selektor für das Zielelement. |
| `camera_entity` | string | - | Entity-ID einer `camera.*`-Entity für einen Live-Hintergrund. |
| `camera_zoom` | string oder number | - | CSS-Zoom oder Skalierung, z. B. `1.5` oder `"150%"`. |
| `camera_pan_x` | string oder number | - | CSS-Verschiebung auf der X-Achse, z. B. `"10%"` oder `"-20px"`. |
| `camera_pan_y` | string oder number | - | CSS-Verschiebung auf der Y-Achse. |
| `camera_position` | string | `center` | Positionierung des Streams: `center`, `top`, `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right`. |
| `camera_stream_cache_ms` | number | `20000` | Wie lange ein `ha-camera-stream` nach dem Entfernen im Cache bleibt. So kann ein Stream beim nächsten Aufbau wiederverwendet werden. |
| `image_entity` | string | - | Entity-ID, deren Attribut `entity_picture` als Hintergrundbild genutzt wird. |
| `video_url` | string | - | Video-URL. `media-source://` wird unterstuetzt. |
| `image_url` | string | - | Bild-URL. `media-source://` wird unterstuetzt. |
| `background` | string oder object | - | CSS-`background`-Shorthand oder Mapping einzelner Eigenschaften. Bei `image_entity` oder `image_url` können Objektwerte wie `position` und `size` das Bildlayout überschreiben. |
| `opacity` | number | - | CSS-Deckkraft der Hintergrundebene von `0` bis `1`. |
| `dissolve_target` | string oder list | - | Macht das Zielelement transparent, damit der Spark-Hintergrund sichtbar wird. |
| `class` | string | - | Zusätzliche CSS-Klasse für den Hintergrundcontainer `<div>`. |

::: tip
Für Kameras empfiehlt sich ein explizites Seitenverhältnis oder eine klare Höhe am Zielcontainer. Sonst kann der Stream je nach Karte ungewohnt zugeschnitten wirken.

:::
## `background` als Mapping

| Schlüssel | CSS-Eigenschaft |
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

`dissolve_target` entfernt oder reduziert den bestehenden Hintergrund des Zielelements. Das ist besonders wichtig bei Karten, deren eigenes `ha-card` sonst über der neuen Hintergrundebene liegt.

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

Lokale Medien aus Home Assistant können über `media-source://` eingebunden werden.

```yaml
image_url: media-source://media_source/local/backgrounds/room.jpg
```

```yaml
video_url: media-source://media_source/local/videos/ambient.mp4
```

## Adapter

### Card-Adapter

Bei normalen Karten arbeitet der Spark mit dem erzeugten Kartenelement. Wenn kein `for` gesetzt ist, steht `element` für das Root-Element des Forge-Ergebnisses.

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

### Vollständiger CSS-Background

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

### Zustandsabhängige Hintergrundfarbe

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

## Positionierung und Lesbarkeit

Hintergründe liegen hinter dem eigentlichen Element. Wenn Text oder Icons schlecht lesbar sind, kombiniere Bild, Deckkraft und Overlay-Farbe.

```yaml
forge:
  sparks:
    - type: background
      image_url: /local/backgrounds/room.jpg
      background:
        size: cover
        position: center
      opacity: 0.45
element:
  type: tile
  entity: sensor.room_status
uix:
  style: |
    ha-card {
      color: var(--white-color);
      text-shadow: 0 1px 2px rgba(0,0,0,.6);
    }
```

## Kamera-Zoom und Pan

Bei Live-Kameras kannst du Ausschnitt und Fokus steuern.

```yaml
forge:
  sparks:
    - type: background
      camera_entity: camera.driveway
      camera_zoom: 1.6
      camera_pan_x: "-8%"
      camera_pan_y: "4%"
      camera_position: center
      opacity: 0.5
```

## Mehrere Hintergründe

Wenn du mehrere Background Sparks nutzt, entscheidet die Reihenfolge und das CSS der Container. Meist ist ein einzelner Spark mit CSS-Shorthand klarer.

```yaml
forge:
  sparks:
    - type: background
      background: "linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.15)), url('/local/backgrounds/night.jpg') center / cover no-repeat"
```

## Typische Probleme

| Problem | Ursache | Lösung |
| --- | --- | --- |
| Bild sichtbar, Text schlecht lesbar | Hintergrund zu hell oder zu kontrastreich | `opacity`, `text-shadow` oder dunkles Gradient nutzen |
| Hintergrund nicht sichtbar | Zielkarte hat eigenen Hintergrund | `dissolve_target` auf `background` setzen |
| Kamera startet langsam | Stream wird neu aufgebaut | `camera_stream_cache_ms` erhöhen |
| Bild falsch zugeschnitten | `background-size` oder Position fehlt | `background.size` und `background.position` setzen |
| Medienbibliothek funktioniert nicht | URI falsch | `media-source://media_source/local/...` prüfen |

## Template-Quellen

Hintergrundquellen können aus States oder Attributen kommen.

```yaml
forge:
  sparks:
    - type: background
      image_url: "&#123;&#123; state_attr('sensor.current_room', 'background') | default('/local/backgrounds/default.jpg') &#125;&#125;"
      background:
        size: cover
        position: center
```

## Wann nicht verwenden?

Nutze den Background Spark nicht für rein dekorative Überladung. Er ist am stärksten, wenn der Hintergrund echte Information trägt, zum Beispiel Kamera, Raumfoto, Coverbild oder klarer Zustandskontrast.

## Kombination mit Sections

Bei Sections sollte der Hintergrund dezent bleiben, weil Sections oft mehrere Karten zusammenfassen.

```yaml
type: custom:uix-forge
forge:
  mold: section
  sparks:
    - type: background
      image_url: /local/backgrounds/living-room-wide.jpg
      background:
        size: cover
        position: center
      opacity: 0.2
element:
  type: heading
  heading: Wohnzimmer
```

## Kombination mit Lock Spark

Ein Hintergrund kann zusammen mit einem Lock Spark genutzt werden. Die Reihenfolge ist wichtig, wenn beide Sparks denselben Bereich betreffen.

```yaml
forge:
  sparks:
    - type: background
      image_url: /local/backgrounds/garage.jpg
      opacity: 0.35
    - type: lock
      locks:
        - confirmation: Garagentor bedienen?
          admins: true
```

## Kamera-Cache verstehen

`camera_stream_cache_ms` hält einen entfernten Kamera-Stream kurzzeitig verbunden. Dadurch muss Home Assistant beim erneuten Aufbau nicht sofort einen neuen Stream aushandeln.

| Wert | Wirkung |
| --- | --- |
| `0` | Kein Cache |
| `5000` | Kurzer Cache für schnelle Re-Renders |
| `20000` | Standardwert |
| `60000` | Längerer Cache für langsame Views oder Tabs |

Ein längerer Cache kann flüssiger wirken, hält aber den Stream länger aktiv.

## Hintergrund über CSS-Variablen

Du kannst Hintergrundwerte auch über Theme-Variablen oder UIX-Variablen steuern.

```yaml
forge:
  sparks:
    - type: background
      background:
        color: var(--uix-room-background, var(--card-background-color))
```

```yaml
uix:
  style: |
    :host {
      --uix-room-background: rgba(25, 118, 210, 0.12);
    }
```
