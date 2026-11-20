---
title: State Badge Spark
---
# State Badge Spark

Der State Badge Spark fügt ein Home-Assistant-`state-badge` in ein Forge-Element ein. Das Badge zeigt das native Icon, Entity-Picture oder den Kamera-Status einer Entity.

## Grundnutzung

::: warning Hinweis zum geprüften Quellstand
Im dokumentierten Quellstand fällt ein leeres `after` auf das Standardziel der Blank Card zurück. Es deaktiviert dieses Ziel nicht. Verwende dort eine ausdrückliche Platzierung mit `after`; ein leeres `after` ermöglicht `before` nicht zuverlässig. Das ist ein [Quellcodebefund](https://github.com/Lint-Free-Technology/uix/blob/fb36536e5836d595637fbf3bc253d5fc0d3ed8d6/src/forge/sparks/uix-spark-state-badge.ts), kein neuer Browsertest.
:::

::: tip
Für reine Overlay-Marker ist oft der [Overlay Icon Spark](./overlay-icon) passender. `state-badge` ist richtig, wenn du Home Assistants native Entity-Darstellung einbetten willst.

:::
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

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `state-badge` sein. |
| `after` | `string` | `after` oder `before` | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor für das Referenzelement. Das Badge wird danach als Geschwisterelement eingefügt. |
| `before` | `string` | `after` oder `before` | - | UIX-Selektor für das Referenzelement. Das Badge wird davor eingefügt. |
| `entity` | `string` | für nativen Entitätszustand | - | Entity-ID. Der aktuelle State wird an `state-badge` übergeben. Ein festes Override-Icon oder -Bild kann auch ohne Entität verwendet werden. |
| `override_icon` | `string` | nein | - | MDI-Icon, das das Standardicon ersetzt. Kann mit `entity` kombiniert werden. |
| `override_image` | `string` | nein | - | Bild-URL, die das Icon vollständig ersetzt. Kann mit `entity` kombiniert werden. |
| `color` | string | nein | - | Iconfarbe für aktive Zustände. Erlaubt `state`, `none`, Home-Assistant-Farbtoken oder Hexcode. |

::: note
Genau einer der beiden Schlüssel `after` oder `before` muss gesetzt sein. Das Badge wird als Geschwisterelement eingefügt, nicht als Kind.

:::
::: tip
Wenn Home Assistant die Entity bereits mit Bild oder Kamera darstellt, übernimmt `state-badge` diese native Darstellung automatisch.

:::
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

### Icon überschreiben

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

### Bild überschreiben

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

Mit `color: none` bleibt die normale Darstellung ohne aktive Färbung erhalten.

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

- Für den nativen Entitätszustand ist `entity` nötig. Bei einem festen `override_icon` oder `override_image` kann die Entität im geprüften Quellstand fehlen; die ursprüngliche Pflichtangabe war zu allgemein.
- Genau einer von `after` und `before` sollte gesetzt sein.
- Wenn das Badge nicht sichtbar ist, prüfe den DOM-Pfad und ob das Referenzelement vorhanden ist.
