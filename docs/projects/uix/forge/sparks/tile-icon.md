---
title: Tile Icon Spark
---
# Tile Icon Spark

Der Tile Icon Spark fügt ein `ha-tile-icon` in ein Forge-Element ein. Du kannst ein MDI-Icon, einen SVG-Pfad, ein Bild oder ein Entity-basiertes State-Icon verwenden.

::: warning Hinweis zum geprüften Quellstand
Im dokumentierten Quellstand fällt ein leeres `after` auf das Standardziel der Blank Card zurück. Es deaktiviert dieses Standardziel nicht. Ein leeres `after` ist deshalb kein verlässlicher Weg, `before` bei einer Blank Card zu verwenden. Nutze dort eine ausdrückliche Platzierung mit `after`. Das ist ein [Quellcodebefund](https://github.com/Lint-Free-Technology/uix/blob/fb36536e5836d595637fbf3bc253d5fc0d3ed8d6/src/forge/sparks/uix-spark-tile-icon.ts), kein neuer Browsertest.
:::

## Grundnutzung

::: tip
Dieser Spark ist besonders hilfreich, wenn eine Karte ein Tile-ähnliches Zusatzicon braucht, ohne dass du das eigentliche Kartenelement austauschst.

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

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `tile-icon` sein. |
| `after` | `string` | `after` oder `before` | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor für das Referenzelement. Das Icon wird danach als Geschwisterelement eingefügt. |
| `before` | `string` | `after` oder `before` | - | UIX-Selektor für das Referenzelement. Das Icon wird davor eingefügt. |
| `icon` | `string` | eine Iconquelle | - | MDI-Icon, z. B. `mdi:star`. Kann auch das Entity-Icon ersetzen, wenn `entity` gesetzt ist. |
| `icon_path` | `string` | eine Iconquelle | - | SVG-Pfad für `ha-tile-icon` als `iconPath`, gerendert über `ha-svg-icon`. |
| `image_url` | `string` | eine Iconquelle | - | Bild-URL innerhalb des Tile-Icons. |
| `entity` | `string` | eine Iconquelle | - | Entity-ID. Der aktuelle State wird an ein `ha-state-icon` im Icon-Slot übergeben. |
| `color` | CSS color | nein | - | Farbe des Tile-Icons. Überschreibt Entity-State-Farbe. |
| `tap_action` | action | nein | - | Aktion bei Tap. |
| `hold_action` | action | nein | - | Aktion bei langem Drücken. |
| `double_tap_action` | action | nein | - | Aktion bei Doppeltap. |

::: note
Für die Iconquelle muss mindestens einer dieser Werte gesetzt sein: `icon`, `icon_path`, `image_url` oder `entity`.

`entity` darf zusätzlich mit `icon` kombiniert werden, um das Symbol zu ersetzen. Die Aussage im Original, es sei immer genau eine Quelle erlaubt, widerspricht dieser unterstützten Kombination.

:::
::: tip
Mit `entity` bekommst du Home Assistants native State-Icon-Logik. Mit `icon` oder `image_url` steuerst du das Aussehen selbst.

:::
## Aktionen

Mit `entity` kann schon die native Standardaktion beim Antippen eine unterstützte Entität schalten oder aktivieren, auch ohne ausdrücklich konfigurierte Aktion. Für eine reine Zustandsanzeige setze `tap_action: {action: none}`. Dies folgt aus dem gemeinsamen Tile-Icon-Helfer des dokumentierten Quellstands.

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
Klicks auf das eingefügte Icon werden getrennt von Aktionen des Ziel- oder Elternelements behandelt.

Der Spark trifft das erste passende Element und fügt das Icon als Geschwisterelement ein. Bei `before` vor einem bestehenden Tile-Icon muss der Selektor das neu eingefügte Icon ausschließen, etwa über `:not([data-uix-forge-tile-icon-id])`, damit Aktualisierungen nicht das eigene Icon auswählen.

:::
## Beispiele

### MDI-Icon einfügen

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

### Tief verschachtelte Ziele erreichen

Der UIX-Selektor kann mit `$` Shadow-Root-Grenzen überqueren. Der DOM-Helfer `uix_forge_path()` unterstützt die Pfadsuche.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tile-icon
      before: hui-alarm-panel-card $$ ha-input
      icon: mdi:star
      color: red
element:
  type: alarm-panel
  states: []
  entity: alarm_control_panel.security
```

![Tief verschachtelte Ziele erreichen](/projects/uix/assets/page-assets/forge/sparks/tile-icon-nested.png)
