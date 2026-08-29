---
title: More-info Spark
---
# More-info Spark

Der More-info Spark fuegt Home Assistants More-info-Inhalt direkt in ein Forge-Element ein. So kannst du den bekannten Detailbereich einer Entity in Karten, Stacks oder Shortcuts einbetten.

!!! note
    Der Spark nutzt Home-Assistant-Frontend-Elemente. Dadurch kann sich das genaue Aussehen mit Home-Assistant-Versionen aendern.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: more-info
      after: hui-tile-card
      entity: light.living_room
element:
  type: tile
  entity: light.living_room
```

## Mit Details

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: more-info
      after: hui-tile-card
      entity: light.living_room
      details: true
element:
  type: tile
  entity: light.living_room
```

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `more-info` sein. |
| `after` | `string` | nein | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor fuer das Referenzelement. Der More-info-Inhalt wird danach als Geschwisterelement eingefuegt. |
| `before` | `string` | nein | - | UIX-Selektor fuer das Referenzelement. Der Inhalt wird davor eingefuegt. |
| `entity` | `string` | nein | `element.entity` | Entity-ID fuer den eingebetteten More-info-Bereich. Ohne Wert nutzt UIX die Entity des Forge-Elements, falls vorhanden. |
| `info` | `boolean` | nein | `true` | Wenn `false`, wird der Hauptinhalt `ha-more-info-info` nicht angezeigt. Nuetzlich zusammen mit `details: true`. |
| `details` | `boolean` | nein | `false` | Fuegt einen einklappbaren `ha-more-info-details`-Bereich unter dem Hauptinhalt hinzu. |

!!! note
    Nutze entweder `after` oder `before`, wenn die Position exakt sein soll. Ohne klares Referenzelement kann der More-info-Bereich je nach Karte an einer unerwarteten Stelle erscheinen.

## Theme-Styling

```yaml
my-theme:
  uix-theme: my-theme
  uix-card: |
    uix-more-info {
      --uix-more-info-details-max-height: 360px;
    }
```

## CSS-Variablen

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-more-info-details-head-height` | `40px` | Hoehe der Details-Toggle-Zeile. |
| `--uix-more-info-details-head-padding` | `0 var(--ha-space-4, 16px)` | Innenabstand der Details-Toggle-Zeile. |
| `--uix-more-info-details-head-gap` | `var(--ha-space-2, 8px)` | Abstand zwischen Aktionsbuttons. |
| `--uix-more-info-details-outer-padding` | `0 var(--ha-space-6, 24px) var(--ha-space-6, 24px)` | Aussenabstand um den Detailsbereich. |
| `--uix-more-info-details-no-info-outer-padding` | `var(--ha-space-6, 24px)` | Abstand, wenn nur Details ohne Hauptinfo angezeigt werden. |
| `--uix-more-info-details-toggle-width` | `32px` | Groesse der Details-Iconbuttons. |
| `--uix-more-info-details-transition-duration` | `350ms` | Dauer fuer Dropdown, Toggle-Icon und YAML-Button-Fade. |
| `--uix-more-info-details-toggle-color` | `var(--primary-text-color)` | Farbe der Details-Aktionsbuttons. |
| `--uix-more-info-details-max-height` | `unset` | Maximale Hoehe des geoeffneten Detailsbereichs. Bei gesetzter Hoehe wird Overflow scrollbar. |

## Bedienung und Styling-Hinweise

### YAML-Details-Fullscreen-Button

Der Detailsbereich kann einen YAML-Button fuer die Vollansicht enthalten. Wenn du sehr kompakte Karten baust, plane dafuer genug Platz ein oder begrenze den Detailsbereich ueber `--uix-more-info-details-max-height`.

### Padding des More-info-Hauptinhalts

```yaml
uix:
  style: |
    uix-more-info ha-more-info-info {
      padding: 0 16px;
    }
```

### Padding des Detailsinhalts

```yaml
uix:
  style: |
    :host {
      --uix-more-info-details-outer-padding: 8px 16px 16px;
    }
```

## Nutzung mit Standardkarten

### Shortcut-Karte im Vertical Stack

```yaml
type: vertical-stack
cards:
  - type: custom:uix-forge
    forge:
      mold: card
      sparks:
        - type: more-info
          after: hui-card
          entity: light.living_room
          details: true
    element:
      type: button
      entity: light.living_room
      name: Wohnzimmer
```
