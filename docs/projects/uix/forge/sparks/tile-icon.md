---
title: Tile Icon Spark
---
# Tile Icon Spark

Der Tile Icon Spark fuegt ein `ha-tile-icon` in ein Forge-Element ein. Du kannst ein MDI-Icon, einen SVG-Pfad, ein Bild oder ein Entity-basiertes State-Icon verwenden.

## Grundnutzung

::: tip
Dieser Spark ist besonders hilfreich, wenn eine Karte ein Tile-aehnliches Zusatzicon braucht, ohne dass du das eigentliche Kartenelement austauschst.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      after: hui-tile-card $ ha-tile-icon
      icon: mdi:star
      color: amber
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `tile-icon` sein. |
| `after` | `string` | `after` oder `before` | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor fuer das Referenzelement. Das Icon wird danach als Geschwisterelement eingefuegt. |
| `before` | `string` | `after` oder `before` | - | UIX-Selektor fuer das Referenzelement. Das Icon wird davor eingefuegt. |
| `icon` | `string` | eine Iconquelle | - | MDI-Icon, z. B. `mdi:star`. Kann auch das Entity-Icon ersetzen, wenn `entity` gesetzt ist. |
| `icon_path` | `string` | eine Iconquelle | - | SVG-Pfad fuer `ha-tile-icon` als `iconPath`, gerendert ueber `ha-svg-icon`. |
| `image_url` | `string` | eine Iconquelle | - | Bild-URL innerhalb des Tile-Icons. |
| `entity` | `string` | eine Iconquelle | - | Entity-ID. Der aktuelle State wird an ein `ha-state-icon` im Icon-Slot uebergeben. |
| `color` | CSS color | nein | - | Farbe des Tile-Icons. Ueberschreibt Entity-State-Farbe. |
| `tap_action` | action | nein | - | Aktion bei Tap. |
| `hold_action` | action | nein | - | Aktion bei langem Druecken. |
| `double_tap_action` | action | nein | - | Aktion bei Doppeltap. |

::: note
Fuer die Iconquelle muss mindestens einer dieser Werte gesetzt sein: `icon`, `icon_path`, `image_url` oder `entity`.

:::
::: tip
Mit `entity` bekommst du Home Assistants native State-Icon-Logik. Mit `icon` oder `image_url` steuerst du das Aussehen selbst.

:::
## Aktionen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      after: hui-tile-card $ ha-tile-info
      icon: mdi:power
      color: red
      entity: switch.fan
      tap_action:
        action: toggle
      hold_action:
        action: more-info
element:
  type: tile
  entity: sensor.room_temperature
```

::: note
Klicks auf das eingefuegte Icon werden getrennt von Aktionen des Ziel- oder Elternelements behandelt.

:::
## Beispiele

### MDI-Icon einfuegen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      after: hui-tile-card $ ha-tile-icon
      icon: mdi:sofa
      color: indigo
element:
  type: tile
  entity: light.living_room
```

### Entity-State-Icon nutzen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      before: hui-tile-card $ ha-tile-info
      entity: binary_sensor.window
      color: state
element:
  type: tile
  entity: climate.living_room
```

### Eigenen SVG-Pfad verwenden

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      after: hui-tile-card $ ha-tile-info
      icon_path: "M12,2A10,10 0 1,0 22,12A10,10 0 0,0 12,2Z"
      color: var(--primary-color)
element:
  type: tile
  entity: sensor.custom_value
```

### Bild-Icon

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      after: hui-tile-card $ ha-tile-icon
      image_url: /local/icons/room.png
element:
  type: tile
  entity: sensor.room_mode
```
