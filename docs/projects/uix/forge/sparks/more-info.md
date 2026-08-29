---
title: More-info Spark
---
# More-info Spark

Der More-info Spark fügt Home Assistants More-info-Inhalt direkt in ein Forge-Element ein. So kannst du den bekannten Detailbereich einer Entity in Karten, Stacks oder Shortcuts einbetten.

::: note
Der Spark nutzt Home-Assistant-Frontend-Elemente. Dadurch kann sich das genaue Aussehen mit Home-Assistant-Versionen ändern.

:::
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

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `more-info` sein. |
| `after` | `string` | nein | Bei Blank Card `uix-forge-blank-card $ div.content`, sonst `""`. | UIX-Selektor für das Referenzelement. Der More-info-Inhalt wird danach als Geschwisterelement eingefügt. |
| `before` | `string` | nein | - | UIX-Selektor für das Referenzelement. Der Inhalt wird davor eingefügt. |
| `entity` | `string` | nein | `element.entity` | Entity-ID für den eingebetteten More-info-Bereich. Ohne Wert nutzt UIX die Entity des Forge-Elements, falls vorhanden. |
| `info` | `boolean` | nein | `true` | Wenn `false`, wird der Hauptinhalt `ha-more-info-info` nicht angezeigt. Nuetzlich zusammen mit `details: true`. |
| `details` | `boolean` | nein | `false` | Fuegt einen einklappbaren `ha-more-info-details`-Bereich unter dem Hauptinhalt hinzu. |

::: note
Nutze entweder `after` oder `before`, wenn die Position exakt sein soll. Ohne klares Referenzelement kann der More-info-Bereich je nach Karte an einer unerwarteten Stelle erscheinen.

:::
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
| `--uix-more-info-details-head-height` | `40px` | Höhe der Details-Toggle-Zeile. |
| `--uix-more-info-details-head-padding` | `0 var(--ha-space-4, 16px)` | Innenabstand der Details-Toggle-Zeile. |
| `--uix-more-info-details-head-gap` | `var(--ha-space-2, 8px)` | Abstand zwischen Aktionsbuttons. |
| `--uix-more-info-details-outer-padding` | `0 var(--ha-space-6, 24px) var(--ha-space-6, 24px)` | Außenabstand um den Detailsbereich. |
| `--uix-more-info-details-no-info-outer-padding` | `var(--ha-space-6, 24px)` | Abstand, wenn nur Details ohne Hauptinfo angezeigt werden. |
| `--uix-more-info-details-toggle-width` | `32px` | Größe der Details-Iconbuttons. |
| `--uix-more-info-details-transition-duration` | `350ms` | Dauer für Dropdown, Toggle-Icon und YAML-Button-Fade. |
| `--uix-more-info-details-toggle-color` | `var(--primary-text-color)` | Farbe der Details-Aktionsbuttons. |
| `--uix-more-info-details-max-height` | `unset` | Maximale Höhe des geöffneten Detailsbereichs. Bei gesetzter Höhe wird Overflow scrollbar. |

## Bedienung und Styling-Hinweise

### YAML-Details-Fullscreen-Button

Der Detailsbereich kann einen YAML-Button für die Vollansicht enthalten. Wenn du sehr kompakte Karten baust, plane dafür genug Platz ein oder begrenze den Detailsbereich über `--uix-more-info-details-max-height`.

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

## Nur Details anzeigen

Mit `info: false` und `details: true` blendest du den Hauptbereich aus und zeigst nur den Detailsbereich.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: more-info
      after: hui-tile-card
      entity: climate.living_room
      info: false
      details: true
element:
  type: tile
  entity: climate.living_room
```

## Andere Entity als die Karte

Der Spark kann eine andere Entity anzeigen als das erzeugte Element.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: more-info
      after: hui-tile-card
      entity: sensor.energy_today
element:
  type: tile
  entity: light.living_room
```

## Mit Template-Entity

```yaml
type: custom:uix-forge
forge:
  mold: card
  billets:
    details_entity: sensor.outdoor_temperature
  sparks:
    - type: more-info
      after: hui-tile-card
      entity: "&#123;&#123; details_entity &#125;&#125;"
      details: true
element:
  type: tile
  entity: sensor.outdoor_temperature
```

## Layout-Tipps

| Ziel | Einstellung |
| --- | --- |
| Detailsbereich begrenzen | `--uix-more-info-details-max-height` setzen |
| Nur Details zeigen | `info: false`, `details: true` |
| Abstand reduzieren | Padding-Variablen anpassen |
| More-info nach einer Karte anzeigen | `after` auf das Kartenelement setzen |

## Fehlerquellen

- Wenn keine Entity gefunden wird, prüfe `entity` oder `element.entity`.
- Wenn der Inhalt an falscher Stelle erscheint, setze `after` oder `before` explizit.
- Wenn Details zu groß werden, begrenze die Höhe mit `--uix-more-info-details-max-height`.
