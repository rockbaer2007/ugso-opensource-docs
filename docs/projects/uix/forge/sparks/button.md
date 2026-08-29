---
title: Button Spark
---
# Button Spark

Der Button Spark fügt in ein Forge-Element einen Home-Assistant-Button ein. Der Button kann als Textbutton, als Iconbutton oder als Kombination aus Text mit Start- und End-Icon erscheinen.

Mögliche Inhalte:

- Textlabel mit `label`
- Icon anstelle des Labels mit `icon`
- führendes Icon mit `start_icon`
- nachgestelltes Icon mit `end_icon`

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-icon
      label: Toggle
      entity: light.living_room
      tap_action:
        action: toggle
element:
  type: tile
  entity: light.living_room
```

::: tip
Mit dem DOM-Helfer [`uix_forge_path()`](../../concepts/dom#uix_forge_path0-forge-helper) findest du den richtigen Pfad für `after` oder `before` leichter.

:::
## Konfiguration

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `button` sein. |
| `after` | `string` | `after` oder `before` | Bei Blank-Card-Konfiguration `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor für das Referenzelement. Der Button wird als Geschwisterelement nach dem Treffer eingefügt. |
| `before` | `string` | `after` oder `before` | - | UIX-Selektor für das Referenzelement. Der Button wird als Geschwisterelement vor dem Treffer eingefügt. |
| `entity` | `string` | nein | - | Entity-ID für Aktionen wie `toggle`. Für entitybasierte Aktionen erforderlich. |
| `icon` | `string` | nein | - | MDI-Icon im Label-Slot, z. B. `mdi:lightbulb`. Nicht zusammen mit `label` nutzen. |
| `color` | `string` | nein | - | Iconfarbe im reinen Iconmodus, z. B. `red` oder `var(--primary-color)`. |
| `label` | `string` | nein | `""` | Text im Button. Nicht zusammen mit `icon` nutzen. |
| `start_icon` | `string` | nein | - | MDI-Icon vor dem Label, z. B. `mdi:play`. |
| `end_icon` | `string` | nein | - | MDI-Icon nach dem Label, z. B. `mdi:chevron-right`. |
| `variant` | `string` | nein | `brand`, bei `icon` `neutral` | Farbvariante: `brand`, `neutral`, `danger`, `warning`, `success`. |
| `appearance` | `string` | nein | `accent`, bei `icon` `plain` | Darstellung: `accent`, `filled`, `plain`. |
| `size` | `string` | nein | - | Buttongröße: `s` oder `m`. |
| `tap_action` | action | nein | - | Aktion bei Klick oder Tap. |
| `hold_action` | action | nein | - | Aktion bei langem Drücken. |
| `double_tap_action` | action | nein | - | Aktion bei Doppelklick oder Double Tap. |

::: note
Genau einer der beiden Schlüssel `after` oder `before` muss gesetzt sein.

Der Spark verwendet das erste Element, das durch `after` oder `before` gefunden wird.

Das eingefügte `ha-button` landet in einem umschließenden `<div>` im gleichen Parent wie das Zielelement. Es wird also als Geschwisterelement eingefügt, nicht als Kind.

`icon` und `label` schließen sich gegenseitig aus. Wenn `icon` gesetzt ist, wird `label` ignoriert.

UIX setzt standardmäßig ein Margin von `-6px`, damit der Button in vielen Home-Assistant-Bereichen sauber ausgerichtet ist. Das Margin kann über `--uix-button-margin` angepasst werden.

:::
## Aktionen

Der Button nutzt die normalen Home-Assistant-Aktionen. In einer Tile Card werden Klickereignisse des Buttons von der Tile-eigenen Aktion getrennt. Es feuern also nur die Aktionen, die am Button selbst konfiguriert sind.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-icon
      label: Wohnzimmer
      entity: light.living_room_rgbww_lights
      tap_action:
        action: toggle
      hold_action:
        action: more-info
element:
  type: tile
  entity: light.bed_light
```

## CSS-Variablen

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-button-label-text-wrap` | `wrap` | Steuert den Zeilenumbruch des Buttonlabels. Setze `nowrap`, wenn Labels nicht umbrechen sollen. |
| `--uix-button-margin` | `-6px` | Steuert das Margin des eingefügten Buttons. |

## Beispiele

Button nach dem Tile-Icon mit End-Icon:

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 9
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-icon
      label: Wohnzimmer
      end_icon: mdi:lightbulb-fluorescent-tube-outline
      entity: light.living_room_rgbww_lights
      tap_action:
        action: toggle
  uix:
    style: |
      :host {
        --uix-button-label-text-wrap: nowrap;
      }
element:
  type: tile
  entity: light.bed_light
```


Button vor dem Tile-Icon mit Danger-Variante:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: button
      before: hui-tile-card $ ha-tile-icon
      label: Ausschalten
      variant: danger
      appearance: plain
      entity: light.living_room
      tap_action:
        action: call-service
        service: light.turn_off
        target:
          entity_id: light.living_room
element:
  type: tile
  entity: light.bed_light
```


Button mit Start- und End-Icon:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-icon
      start_icon: mdi:play
      label: Szene
      end_icon: mdi:chevron-right
      tap_action:
        action: perform-action
        perform_action: light.turn_off
        target:
          entity_id: light.living_room_rgbww_lights
element:
  type: tile
  entity: light.bed_light
```


Reiner Iconbutton:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: button
      before: hui-tile-card $ ha-tile-info
      icon: mdi:lightbulb
      color: var(--red-color)
      entity: light.living_room_rgbww_lights
      tap_action:
        action: toggle
element:
  type: tile
  entity: light.bed_light
  uix:
    style: |
      ha-button {
        --ha-icon-button-size: 36px;
      }
```


Button zusammen mit einem [Tooltip Spark](./tooltip):

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 12
    rows: 1
  sparks:
    - type: tooltip
      for: hui-tile-card $ ha-button
      content: Speziellen Schalter umschalten
    - type: button
      after: hui-tile-card $ ha-tile-info
      label: Druecken
      variant: neutral
      appearance: plain
      end_icon: mdi:test-tube
      entity: input_boolean.test_boolean
      tap_action:
        action: toggle
      hold_action:
        action: more-info
element:
  type: tile
  entity: light.bed_light
  vertical: false
  features_position: bottom
  uix:
    style: |
      ha-tile-info {
        flex: 2;
      }
      ha-button {
        margin-top: -2px;
        flex: 1;
      }
```


## Variante und Darstellung

Home Assistant stellt verschiedene Kombinationen aus `variant` und `appearance` bereit. Die Namen bleiben in YAML englisch, weil sie direkt an `ha-button` weitergereicht werden.

::: info Button-Varianten und Darstellungen
:::
