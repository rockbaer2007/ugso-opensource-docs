---
title: State Badge Spark
---
# State Badge Spark

Der State Badge Spark fuegt ein Home-Assistant-`state-badge` in ein Forge-Element ein. Das Badge zeigt das native Icon, Entity-Picture oder den Kamera-Status einer Entity.

## Grundnutzung

!!! tip
    Fuer reine Overlay-Marker ist oft der [Overlay Icon Spark](./overlay-icon) passender. `state-badge` ist richtig, wenn du Home Assistants native Entity-Darstellung einbetten willst.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: binary_sensor.window
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `state-badge` sein. |
| `after` | `string` | `after` oder `before` | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor fuer das Referenzelement. Das Badge wird danach als Geschwisterelement eingefuegt. |
| `before` | `string` | `after` oder `before` | - | UIX-Selektor fuer das Referenzelement. Das Badge wird davor eingefuegt. |
| `entity` | `string` | ja | - | Entity-ID. Der aktuelle State wird an `state-badge` uebergeben. |
| `override_icon` | `string` | nein | - | MDI-Icon, das das Standardicon ersetzt. Kann mit `entity` kombiniert werden. |
| `override_image` | `string` | nein | - | Bild-URL, die das Icon vollstaendig ersetzt. Kann mit `entity` kombiniert werden. |
| `color` | string | nein | - | Iconfarbe fuer aktive Zustaende. Erlaubt `state`, `none`, Home-Assistant-Farbtoken oder Hexcode. |

!!! note
    Genau einer der beiden Schluessel `after` oder `before` muss gesetzt sein. Das Badge wird als Geschwisterelement eingefuegt, nicht als Kind.

!!! tip
    Wenn Home Assistant die Entity bereits mit Bild oder Kamera darstellt, uebernimmt `state-badge` diese native Darstellung automatisch.

## Beispiele

### Badge nach Tile-Icon

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: sensor.outdoor_temperature
element:
  type: tile
  entity: light.living_room
```

### Badge vor Textbereich

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      before: hui-tile-card $ ha-tile-info
      entity: binary_sensor.front_door
      color: state
element:
  type: tile
  entity: lock.front_door
```

### Icon ueberschreiben

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: sensor.energy_today
      override_icon: mdi:flash
      color: amber
element:
  type: tile
  entity: sensor.energy_today
```

### Bild ueberschreiben

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: person.max
      override_image: /local/persons/max.png
element:
  type: tile
  entity: person.max
```

## Farbe

`color` kann Home Assistants State-Farbe nutzen oder eine feste Farbe setzen.

```yaml
forge:
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: binary_sensor.motion
      color: state
```

```yaml
forge:
  sparks:
    - type: state-badge
      after: hui-tile-card $ ha-tile-icon
      entity: sensor.energy_today
      color: green
```

Mit `color: none` bleibt die normale Darstellung ohne aktive Faerbung erhalten.

## Unterschied zu Overlay Icon

| Bedarf | Geeigneter Spark |
| --- | --- |
| Natives Home-Assistant-State-Badge | `state-badge` |
| Kleines Icon als Overlay | `overlay-icon` |
| Bild oder Icon frei positionieren | `overlay-icon` |
| Entity-Picture wie Home Assistant anzeigen | `state-badge` |

## Mit Blank Card

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: state-badge
      after: uix-forge-blank-card $ div.content
      entity: sensor.outdoor_temperature
element:
  type: custom:uix-forge-blank-card
```

## Fehlerquellen

- `entity` ist Pflicht, auch wenn `override_icon` oder `override_image` gesetzt ist.
- Genau einer von `after` und `before` sollte gesetzt sein.
- Wenn das Badge nicht sichtbar ist, pruefe den DOM-Pfad und ob das Referenzelement vorhanden ist.
