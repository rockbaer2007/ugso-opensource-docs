---
title: Tooltip Spark
---
# Tooltip Spark

Der Tooltip Spark hängt einen gestylten Tooltip an ein Element im Forge-Ergebnis. Der Inhalt kann normaler Text, HTML oder ein Template sein.

Er verwendet Home Assistants `wa-tooltip`, unterstützt zwölf Positionen und liegt durch die Popover-API des Browsers über anderen Oberflächenebenen. `for` verwendet die [DOM-Navigation](../../concepts/dom), einschließlich `$` für Shadow Roots. Nur das erste passende Element erhält den Tooltip. Ohne `for` wird die Wurzel des erzeugten Elements verwendet; bei einer Blank Card ist dies `uix-forge-blank-card $ div.content`.

::: info Versionsstand
Die Grundfunktion gehört zur stabilen Basis UIX 8.2.0. Die nachfolgend gekennzeichneten Ergänzungen wurden bis UIX 8.3.0-beta.8 abgeglichen.
:::

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
      content: "<b>Status:</b> {{ states(config.element.entity) }}"
      placement: bottom
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `tooltip` sein. |
| `for` | string | nein | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor für das Zielelement. |
| `content` | string | nein | `""` | HTML-Inhalt des Tooltips. |
| `placement` | string | nein | `top` | Position relativ zum Ziel: `top`, `top-start`, `top-end`, `bottom`, `bottom-start`, `bottom-end`, `left`, `left-start`, `left-end`, `right`, `right-start`, `right-end`. |
| `distance` | number | nein | `8` | Abstand zwischen Tooltip und Ziel in Pixeln. |
| `skidding` | number | nein | `0` | Versatz entlang der Achse des Zielelements in Pixeln. |
| `show_delay` | number | nein | `150` | Wartezeit bis zum Anzeigen in Millisekunden. |
| `hide_delay` | number | nein | `150` | Wartezeit bis zum Ausblenden in Millisekunden. |
| `trigger` | string | nein | `"hover focus"` | Ab 8.3.0-beta.8: durch Leerzeichen getrennte Aktivierungsarten `hover`, `focus`, `click` oder `manual`. |
| `open` | boolean | nein | `false` | Ab 8.3.0-beta.8: Öffnungszustand beim Ändern der Spark-Konfiguration setzen; besonders für `trigger: manual`. |
| `without_arrow` | boolean | nein | `false` | Bei `true` wird der Richtungspfeil ausgeblendet. |

::: tip
Mit dem [DOM-Helfer `uix_forge_path($0)`](../../concepts/dom) lässt sich der passende `for`-Pfad ermitteln.

Wenn ein Element bereits ein natives `title`-Attribut besitzt, kann der [Attribute Spark](./attribute) es entfernen, damit nicht zwei Tooltips gleichzeitig erscheinen.

:::
Ab 8.3.0-beta.8 bleibt ein mit `hover` aktivierter Tooltip geöffnet, wenn der Zeiger vom Ziel in seinen Inhalt bewegt wird. Damit lassen sich Inhalte mit `--uix-tooltip-max-height` begrenzen und mit `--uix-tooltip-overflow: auto` scrollen. `manual` öffnet den Tooltip nicht automatisch; setze dafür `open: true`:

```yaml
forge:
  sparks:
    - type: tooltip
      trigger: manual
      open: true
      content: Dieser Tooltip wird über die Spark-Konfiguration geöffnet
```

## Templates im Inhalt

`content` ist Teil der Forge-Konfiguration und wird als Template verarbeitet. Entitätszustände, `config` und die übrigen [UIX-Templatevariablen](../../using/templates) stehen zur Verfügung.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card
      content: |
        <strong>{{ state_attr(config.element.entity, 'friendly_name') }}</strong><br>
        Status: {{ states(config.element.entity) }}
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
      content: Haustür seit {{ relative_time(states.binary_sensor.front_door.last_changed) }}
      placement: bottom
element:
  type: entity
  entity: binary_sensor.front_door
```

## Aussehen anpassen

::: note
Der Tooltip wird als Geschwisterelement seines Ziels eingefügt. Setze CSS-Variablen deshalb auf einem gemeinsamen übergeordneten Element. Im Beispiel liegt das Ziel `ha-card` im Shadow Root des mit `:host` gestylten Tile-Elements. Die Variablen können auch aus einem Theme stammen.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: tooltip
      for: hui-tile-card $ ha-card
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

::: info Geänderte Standardwerte ab 8.3.0-beta.6
Hintergrund, Schriftgröße und -gewicht, Padding, Radius und Schatten orientieren sich an Home Assistants Tooltip-Design. Ab beta.7 ergänzt `--ha-tooltip-text-color` die Textfarben-Fallbackkette. Die Tabelle zeigt den Stand beta.8; bei UIX 8.2.0 gelten unter anderem `--secondary-background-color`, `--ha-font-size-s`, `--ha-font-weight-normal`, `8px` Padding, `--ha-border-radius-sm` und `--ha-card-box-shadow`.
:::

| CSS-Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-tooltip-background-color` | `var(--ha-tooltip-background-color, var(--ha-color-surface-default))` | Hintergrundfarbe. |
| `--uix-tooltip-content-color` | `var(--ha-tooltip-text-color, var(--primary-text-color))` | Textfarbe. |
| `--uix-tooltip-font-family` | `--ha-font-family-body` | Schriftfamilie. |
| `--uix-tooltip-font-size` | `--ha-font-size-m` | Schriftgröße. |
| `--uix-tooltip-font-weight` | `--ha-font-weight-medium` | Schriftgewicht. |
| `--uix-tooltip-line-height` | `--ha-line-height-condensed` | Zeilenhöhe. |
| `--uix-tooltip-padding` | `var(--ha-tooltip-padding, var(--ha-space-2))` | Innenabstand; standardmäßig weiterhin 8 px. |
| `--uix-tooltip-border-radius` | `--ha-border-radius-md` | Rundung. |
| `--uix-tooltip-arrow-size` | `var(--ha-tooltip-arrow-size, 8px)` | Pfeilgröße. Zum Ausblenden `without_arrow: true`, `--ha-tooltip-arrow-size: 0px` oder `--uix-tooltip-arrow-size: 0px` verwenden. |
| `--uix-tooltip-border-width` | nicht gesetzt | Rahmenbreite. |
| `--uix-tooltip-border-color` | nicht gesetzt | Rahmenfarbe. |
| `--uix-tooltip-border-style` | nicht gesetzt | Rahmenstil. |
| `--uix-tooltip-max-width` | `30ch` | Maximale Breite. |
| `--uix-tooltip-max-height` | `none` | Ab beta.8: maximale Höhe des Inhalts. |
| `--uix-tooltip-overflow` | `visible` | Ab beta.8: Überlaufverhalten; `auto` macht begrenzte Inhalte scrollbar. |
| `--uix-tooltip-show-duration` | `100ms` | Dauer der Einblendanimation. |
| `--uix-tooltip-hide-duration` | `100ms` | Dauer der Ausblendanimation. |
| `--uix-tooltip-opacity` | `1` | Deckkraft. |
| `--uix-tooltip-box-shadow` | `var(--ha-tooltip-box-shadow, var(--ha-box-shadow-m))` | Schatten. |
| `--uix-tooltip-text-align` | `center` | Textausrichtung. |
| `--uix-tooltip-text-decoration` | `none` | Textdekoration. |
| `--uix-tooltip-text-transform` | `none` | Texttransformation. |
| `--uix-tooltip-overflow-wrap` | `normal` | Umbruchverhalten langer Inhalte. |
