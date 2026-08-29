---
title: Overlay Icon Spark
---
# Overlay Icon Spark

Der Overlay Icon Spark legt ein Icon, ein Bild oder ein zustandsgetriebenes Entity-Icon ueber ein Ziel. Typische Einsaetze sind kleine Statusmarker, Badges auf Tile-Icons oder visuelle Hinweise auf Buttons.

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

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `overlay-icon` sein. |
| `for` | string | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor fuer das Ziel. |
| `icon` | string | - | MDI- oder Custom-Icon. Nutze entweder `icon` oder `image_url`. |
| `image_url` | string | - | Statisches Bild als Overlay. `media-source://` wird unterstuetzt. Nutze entweder `icon` oder `image_url`. |
| `entity` | string | - | Rendert ein zustandsbasiertes `ha-state-icon`. Wenn `entity` gesetzt ist, werden `icon` und `image_url` ignoriert. |
| `value` | string | - | Ueberschreibt den State-Wert, der fuer das Entity-Icon verwendet wird. |
| `color` | string | `state` | Iconfarbe fuer aktive Entity-Zustaende. Erlaubt `state`, `none`, Home-Assistant-Farbtoken oder Hexcode. |
| `icon_color` | string | Bei `ha-tile-icon` `var(--white-color)`, sonst `var(--primary-color)` | CSS-Farbe des Icons. Ueberschreibt `color`. |
| `icon_position` | object | je nach Ziel | Position des Icons innerhalb des Overlays. Zahlen werden als Pixel behandelt. |
| `icon_size` | number oder string | Bei `ha-tile-icon` `12px`, sonst `24px` | Groesse des Icons. |
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
| `--uix-overlay-icon-size` | `24px`, bei `ha-tile-icon` `12px` | Icontextgroesse, ueberschreibt `icon_size`. |
| `--uix-overlay-icon-color` | Bei `ha-tile-icon` `var(--white-color)`, sonst `var(--primary-color)` | Iconfarbe. |
| `--uix-overlay-icon-background` | Bei `ha-tile-icon` `var(--primary-color)`, sonst `transparent` | Iconhintergrund, wenn `icon_background` nicht gesetzt ist. |
| `--uix-overlay-icon-padding` | Bei `ha-tile-icon` `2px`, sonst `0` | Innenabstand um das Icon. |
| `--uix-overlay-icon-position` | `none` | Zusaetzliches CSS-`translate`, z. B. `30px 6px`. |

!!! warning
    `right` und `bottom` werden intern in `left` beziehungsweise `top` mit `calc()` umgerechnet. Wenn die Position nicht passt, teste zuerst mit `top` und `left`.

!!! note
    Wenn `entity` gesetzt ist, erzeugt Home Assistant das Icon aus Domain, Device-Class und State. Das ist ideal fuer echte Statusmarker.

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
