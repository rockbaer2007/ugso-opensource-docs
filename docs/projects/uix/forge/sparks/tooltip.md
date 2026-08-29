---
title: Tooltip Spark
---
# Tooltip Spark

Der Tooltip Spark haengt einen gestylten Tooltip an ein Element im Forge-Ergebnis. Der Inhalt kann normaler Text, HTML oder ein Template sein.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card $ ha-tile-icon
      content: Wohnzimmer-Licht
element:
  type: tile
  entity: light.living_room
```

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card
      content: "<b>Status:</b> &#123;&#123; states(config.element.entity) &#125;&#125;"
      placement: bottom
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `tooltip` sein. |
| `for` | string | nein | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor fuer das Zielelement. |
| `content` | string | nein | `""` | HTML-Inhalt des Tooltips. |
| `placement` | string | nein | `top` | Position relativ zum Ziel: `top`, `top-start`, `top-end`, `bottom`, `bottom-start`, `bottom-end`, `left`, `left-start`, `left-end`, `right`, `right-start`, `right-end`. |
| `distance` | number | nein | `8` | Abstand zwischen Tooltip und Ziel in Pixeln. |
| `skidding` | number | nein | `0` | Versatz entlang der Achse des Zielelements in Pixeln. |
| `show_delay` | number | nein | `150` | Wartezeit bis zum Anzeigen in Millisekunden. |
| `hide_delay` | number | nein | `150` | Wartezeit bis zum Ausblenden in Millisekunden. |
| `without_arrow` | boolean | nein | `false` | Bei `true` wird der Richtungspfeil ausgeblendet. |

!!! tip
    Wenn ein Element bereits ein natives `title`-Attribut besitzt, kann der [Attribute Spark](./attribute) es entfernen, damit nicht zwei Tooltips gleichzeitig erscheinen.

## Templates im Inhalt

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card
      content: |
        <strong>&#123;&#123; state_attr(config.element.entity, 'friendly_name') &#125;&#125;</strong><br>
        Status: &#123;&#123; states(config.element.entity) &#125;&#125;
element:
  type: tile
  entity: sensor.outdoor_temperature
```

## Tooltip auf einem Badge

```yaml
# Badge im Dashboard-Header
type: custom:uix-forge
forge:
  mold: badge
  sparks:
    - type: tooltip
      content: Haustuer seit &#123;&#123; relative_time(states.binary_sensor.front_door.last_changed) &#125;&#125;
      placement: bottom
element:
  type: entity
  entity: binary_sensor.front_door
```

## Aussehen anpassen

!!! note
    Tooltip-Styles werden ueber CSS-Variablen gesetzt. Das ist stabiler als interne Tooltip-Elemente direkt zu stylen.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card
      content: Fenster offen
element:
  type: tile
  entity: binary_sensor.window
uix:
  style: |
    :host {
      --uix-tooltip-background-color: var(--error-color);
      --uix-tooltip-content-color: var(--white-color);
      --uix-tooltip-border-radius: 8px;
    }
```

### CSS-Variablen

| CSS-Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-tooltip-background-color` | `--secondary-background-color` | Hintergrundfarbe. |
| `--uix-tooltip-content-color` | `--primary-text-color` | Textfarbe. |
| `--uix-tooltip-font-family` | `--ha-font-family-body` | Schriftfamilie. |
| `--uix-tooltip-font-size` | `--ha-font-size-s` | Schriftgroesse. |
| `--uix-tooltip-font-weight` | `--ha-font-weight-normal` | Schriftgewicht. |
| `--uix-tooltip-line-height` | `--ha-line-height-condensed` | Zeilenhoehe. |
| `--uix-tooltip-padding` | `8px` | Innenabstand. |
| `--uix-tooltip-border-radius` | `--ha-border-radius-sm` | Rundung. |
| `--uix-tooltip-arrow-size` | `8px` | Groesse des Richtungspfeils. |
| `--uix-tooltip-border-width` | nicht gesetzt | Rahmenbreite. |
| `--uix-tooltip-border-color` | nicht gesetzt | Rahmenfarbe. |
| `--uix-tooltip-border-style` | nicht gesetzt | Rahmenstil. |
| `--uix-tooltip-max-width` | `30ch` | Maximale Breite. |
| `--uix-tooltip-show-duration` | `100ms` | Dauer der Einblendanimation. |
| `--uix-tooltip-hide-duration` | `100ms` | Dauer der Ausblendanimation. |
| `--uix-tooltip-opacity` | `1` | Deckkraft. |
| `--uix-tooltip-box-shadow` | `--ha-card-box-shadow` | Schatten. |
| `--uix-tooltip-text-align` | `center` | Textausrichtung. |
| `--uix-tooltip-text-decoration` | `none` | Textdekoration. |
| `--uix-tooltip-text-transform` | `none` | Texttransformation. |
| `--uix-tooltip-overflow-wrap` | `normal` | Umbruchverhalten langer Inhalte. |
