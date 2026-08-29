---
title: Overlay Icon Spark
---
# Overlay Icon Spark

Der Overlay Icon Spark legt ein Icon, ein Bild oder ein zustandsgetriebenes Entity-Icon über ein Ziel. Typische Einsätze sind kleine Statusmarker, Badges auf Tile-Icons oder visuelle Hinweise auf Buttons.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      for: hui-tile-card $ ha-tile-icon
      icon: mdi:star
      icon_position:
        top: 2
        left: 30
element:
  type: tile
  entity: light.living_room
```

## Konfigurationsreferenz

### Top-Level

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `overlay-icon` sein. |
| `for` | string | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor für das Ziel. |
| `icon` | string | - | MDI- oder Custom-Icon. Nutze entweder `icon` oder `image_url`. |
| `image_url` | string | - | Statisches Bild als Overlay. `media-source://` wird unterstuetzt. Nutze entweder `icon` oder `image_url`. |
| `entity` | string | - | Rendert ein zustandsbasiertes `ha-state-icon`. Wenn `entity` gesetzt ist, werden `icon` und `image_url` ignoriert. |
| `value` | string | - | Überschreibt den State-Wert, der für das Entity-Icon verwendet wird. |
| `color` | string | `state` | Iconfarbe für aktive Entity-Zustände. Erlaubt `state`, `none`, Home-Assistant-Farbtoken oder Hexcode. |
| `icon_color` | string | Bei `ha-tile-icon` `var(--white-color)`, sonst `var(--primary-color)` | CSS-Farbe des Icons. Überschreibt `color`. |
| `icon_position` | object | je nach Ziel | Position des Icons innerhalb des Overlays. Zahlen werden als Pixel behandelt. |
| `icon_size` | number oder string | Bei `ha-tile-icon` `12px`, sonst `24px` | Größe des Icons. |
| `icon_background` | CSS background | Bei `ha-tile-icon` `var(--primary-color)`, sonst nicht gesetzt | Expliziter CSS-Hintergrund des Icons. |

## Overlay anpassen

| CSS-Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-overlay-icon-z-index` | `1` | Stapelreihenfolge des Overlays. |
| `--uix-overlay-icon-display` | `block` | CSS-Display des Overlays. |
| `--uix-overlay-icon-opacity` | Bei `ha-tile-icon` `1`, sonst `0.5` | Deckkraft von Icon und Hintergrund. |
| `--uix-overlay-icon-border-radius` | `inherit` | Rundung des Overlays. |
| `--uix-overlay-icon-row-border-radius` | `--uix-overlay-icon-border-radius` | Rundung bei `row`-Mold. |
| `--uix-overlay-icon-border` | `unset` | CSS-Border. |
| `--uix-overlay-icon-size` | `24px`, bei `ha-tile-icon` `12px` | Icontextgröße, überschreibt `icon_size`. |
| `--uix-overlay-icon-color` | Bei `ha-tile-icon` `var(--white-color)`, sonst `var(--primary-color)` | Iconfarbe. |
| `--uix-overlay-icon-background` | Bei `ha-tile-icon` `var(--primary-color)`, sonst `transparent` | Iconhintergrund, wenn `icon_background` nicht gesetzt ist. |
| `--uix-overlay-icon-padding` | Bei `ha-tile-icon` `2px`, sonst `0` | Innenabstand um das Icon. |
| `--uix-overlay-icon-position` | `none` | Zusätzliches CSS-`translate`, z. B. `30px 6px`. |

::: warning
`right` und `bottom` werden intern in `left` beziehungsweise `top` mit `calc()` umgerechnet. Wenn die Position nicht passt, teste zuerst mit `top` und `left`.

:::
::: note
Wenn `entity` gesetzt ist, erzeugt Home Assistant das Icon aus Domain, Device-Class und State. Das ist ideal für echte Statusmarker.

:::
## Beispiele

### Badge auf Tile-Icon

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      for: hui-tile-card $ ha-tile-icon
      icon: mdi:alert
      icon_color: var(--white-color)
      icon_background: var(--error-color)
      icon_position:
        top: 2
        left: 30
element:
  type: tile
  entity: light.living_room
```

### Zustandsgetriebenes Overlay-Icon mit Wert

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      for: hui-tile-card $ ha-tile-icon
      entity: binary_sensor.window
      value: "on"
element:
  type: tile
  entity: light.living_room
```

### Zahl der eingeschalteten Lichter auf Button anzeigen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      for: hui-button-card
      icon: "mdi:numeric-&#123;&#123; [states.light | selectattr('state', 'eq', 'on') | list | count, 9] | min &#125;&#125;"
      icon_position:
        top: 4
        right: 4
element:
  type: button
  entity: light.living_room
```

### Bild aus Media Source als Popover-Badge

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      image_url: media-source://media_source/local/icons/warning.png
      icon_position:
        top: -8
        right: -8
element:
  type: tile
  entity: sensor.warning_count
uix:
  style: |
    :host {
      --uix-overlay-icon-size: 28px;
      --uix-overlay-icon-background: var(--card-background-color);
      --uix-overlay-icon-border-radius: 999px;
      --uix-overlay-icon-padding: 4px;
    }
```

### Overlay auf Button-Icon

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: overlay-icon
      for: hui-button-card $ ha-state-icon
      icon: mdi:check
      icon_position:
        bottom: 0
        right: 0
element:
  type: button
  entity: input_boolean.ready
```

### Overlay in `custom:template-entity-row`

```yaml
type: custom:uix-forge
forge:
  mold: row
  sparks:
    - type: overlay-icon
      for: hui-generic-entity-row
      entity: binary_sensor.front_door
element:
  type: custom:template-entity-row
  entity: sensor.front_door_status
```

## Positionierung

`icon_position` nimmt Zahlen oder CSS-Werte. Zahlen werden als Pixel interpretiert.

```yaml
icon_position:
  top: 4
  right: 4
```

Mit CSS-Werten:

```yaml
icon_position:
  bottom: "0.25rem"
  left: "calc(100% - 18px)"
```

Wenn du zusätzlich `--uix-overlay-icon-position` setzt, wird diese CSS-Translation mit `icon_position` kombiniert.

## Entity-Farbe

```yaml
forge:
  sparks:
    - type: overlay-icon
      entity: binary_sensor.motion
      color: state
```

`color: none` deaktiviert die automatische State-Farbe. Mit `icon_color` setzt du eine feste Farbe.

```yaml
forge:
  sparks:
    - type: overlay-icon
      entity: binary_sensor.motion
      color: none
      icon_color: var(--primary-text-color)
```

## Bild-Overlay

```yaml
forge:
  sparks:
    - type: overlay-icon
      image_url: /local/icons/package.png
      icon_position:
        top: -6
        right: -6
```

## Typische Overlay-Muster

| Muster | Konfiguration |
| --- | --- |
| Kleines Badge auf Tile-Icon | `for: hui-tile-card $ ha-tile-icon`, `icon_size: 12` |
| Warnsymbol auf Karte | `for: element`, `icon: mdi:alert`, `icon_background: var(--error-color)` |
| State-Marker | `entity` plus `color: state` |
| Bildmarker | `image_url` plus CSS-Variablen für Größe und Hintergrund |

## Fehlerquellen

- Wenn `entity` gesetzt ist, werden `icon` und `image_url` ignoriert.
- Wenn das Overlay hinter anderen Elementen liegt, erhöhe `--uix-overlay-icon-z-index`.
- Wenn `right` oder `bottom` nicht wie erwartet wirken, teste zuerst mit `top` und `left`.
