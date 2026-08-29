---
title: Lock Spark
---
# Lock Spark

Der Lock Spark legt eine Sperrebene über ein Forge-Element oder über ein gezieltes Unterelement. Er kann je nach Benutzer, Adminstatus, PIN, Code oder Bestätigung entsperrt werden.

::: tip
Der Spark schützt die Bedienung in der Oberfläche. Er ersetzt keine serverseitige Home-Assistant-Berechtigung.

:::
## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: lock
      locks:
        - pin: 1234
          admins: true
element:
  type: tile
  entity: light.living_room
```

## Ziel mit `for` wählen

Ohne `for` wird das ganze Forge-Element gesperrt. Mit `for` kann ein bestimmtes Element gesperrt werden, zum Beispiel nur das Tile-Icon.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: lock
      for: hui-tile-card $ ha-tile-icon
      locks:
        - pin: 1234
          admins: true
element:
  type: tile
  entity: light.living_room
```

::: warning
Nutze keine PINs für echte Sicherheitsgrenzen. UIX läuft im Browser und kann Bedienfehler vermeiden, aber keine Home-Assistant-Rechte erzwingen.

:::
## Matching-Logik

| Konfiguration | Wen sie trifft |
| --- | --- |
| `users`-Liste vorhanden | Nutzer, deren Name in der Liste steht. Mit `admins: true` zusätzlich Admins. |
| Keine `users`-Liste | Alle Nicht-Admins, die nicht in `except` stehen. |
| Keine `users`-Liste und `admins: true` | Alle Nutzer, Admins und Nicht-Admins, sofern sie nicht in `except` stehen. |

## Konfigurationsreferenz

### Top-Level

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `lock` sein. |
| `for` | string | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor für das Element, über das die Sperre gelegt wird. |
| `action` | string | `tap` | Geste zum Entsperren: `tap`, `hold` oder `double_tap`. |
| `duration` | number oder string | `3000` | Dauer bis zum erneuten Sperren nach erfolgreichem Entsperren. Zahlen sind Millisekunden, Strings z. B. `5s`, `1m`, `500ms`. |
| `icon_locked` | string | `mdi:lock-outline` | Icon im gesperrten Zustand. |
| `icon_unlocked` | string | - | Icon im entsperrten Zustand. Ohne Wert blendet das Schloss aus. |
| `icon_locked_color` | string | `--error-color` | Farbe des gesperrten Icons. |
| `icon_unlocked_color` | string | `--success-color` | Farbe des entsperrten Icons. |
| `icon_position` | object | je nach Ziel | Pixel-Offsets des Icons. Erlaubt `top` oder `bottom` und `left` oder `right`. |
| `icon_size` | number oder string | `24px`, bei `ha-tile-icon` `12px` | Icongröße. `--uix-lock-icon-size` hat Vorrang. |
| `permissive` | boolean | `false` | Bei `true` bleiben Elemente zugänglich, wenn kein Lock-Eintrag zum aktuellen Nutzer passt. |
| `entity` | string | - | Entity-ID für einfache HA-Aktionen in `unlocked_action`. |
| `unlocked_action` | object | - | Aktion direkt nach erfolgreichem Entsperren. |
| `locks` | list | `[]` | Geordnete Liste von Lock-Einträgen. |
| `code_dialog` | object | - | Optionen für den Code- oder Passphrase-Dialog. |

### `code_dialog`

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `title` | string | HA-Standard | Dialogtitel. |
| `submit_text` | string | HA-Standard | Text des Bestätigungsbuttons. |
| `cancel_text` | string | HA-Standard | Text des Abbrechen-Buttons. |

### `unlocked_action`

| Wert | Wirkung |
| --- | --- |
| `action: element_tap` | Löst die `tap_action` des Zielelements aus. |
| `action: element_hold` | Löst die `hold_action` des Zielelements aus. |
| `action: element_double_tap` | Löst die `double_tap_action` des Zielelements aus. |
| Beliebige HA-Aktion | Führt diese Aktion gegen `entity` aus, z. B. `action: toggle`. |

### Lock-Einträge

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `active` | boolean | `true` | Mit `false` wird für passende Nutzer explizit entsperrt. |
| `code` | string oder number | - | Einzugebender Code. Zahlen zeigen das HA-Nummernfeld, Text zeigt ein Passwortfeld. |
| `pin` | string oder number | - | Alias für `code`. |
| `confirmation` | string oder boolean | - | Bestätigungsdialog. `true` nutzt den HA-Standardtext, ein String nutzt eigenen Text. |
| `users` | Liste von Strings | - | Nutzernamen, für die dieser Eintrag gilt. |
| `admins` | boolean | `false` | Additiv. Ohne `users` erfasst `admins: true` alle Nutzer. Mit `users` werden Admins zusätzlich erfasst. |
| `except` | Liste von Strings | - | Ausnahmen, wenn keine `users`-Liste gesetzt ist. |
| `retry_delay` | number oder string | - | Wartezeit zwischen falschen Codeversuchen. |
| `max_retries` | number | - | Anzahl falscher Versuche vor der längeren Sperrzeit. |
| `max_retries_delay` | number oder string | `30000` | Sperrzeit nach `max_retries`, z. B. `30s` oder `5m`. |

## Beispiele

### Gleiche PIN für alle, inklusive Admins

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1234
          admins: true
```

### Keine Sperre für Admins und einen bestimmten Nutzer

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1234
          except:
            - Max
```

### Bestätigung für alle inklusive Admins

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - confirmation: true
          admins: true
```

### PIN für alle, aber nicht für genannte Nutzer

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1234
          admins: true
          except:
            - Wohnzimmer Tablet
            - Admin
```

### Unterschiedliche PINs pro Nutzergruppe

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1111
          users:
            - Kinderzimmer
        - pin: 2222
          users:
            - Wohnzimmer
        - active: false
          admins: true
```

### Nur bestimmte Nutzer sperren

```yaml
forge:
  sparks:
    - type: lock
      permissive: true
      locks:
        - pin: 1234
          users:
            - Gast
```

### Nach Entsperren die Hold-Aktion der Tile Card ausführen

```yaml
forge:
  sparks:
    - type: lock
      unlocked_action:
        action: element_hold
      locks:
        - pin: 1234
element:
  type: tile
  entity: light.living_room
  hold_action:
    action: more-info
```

### Entity direkt nach Entsperren toggeln

```yaml
forge:
  sparks:
    - type: lock
      entity: light.living_room
      unlocked_action:
        action: toggle
      locks:
        - pin: 1234
element:
  type: tile
  entity: light.living_room
```

### Nur Tile-Icon sperren

```yaml
forge:
  sparks:
    - type: lock
      for: hui-tile-card $ ha-tile-icon
      icon_position:
        top: 3
        left: 3
      locks:
        - pin: 1234
element:
  type: tile
  entity: light.living_room
```

### Eigene Dialogtexte

```yaml
forge:
  sparks:
    - type: lock
      code_dialog:
        title: Freigabe erforderlich
        submit_text: Entsperren
        cancel_text: Abbrechen
      locks:
        - pin: 1234
```

## Overlay anpassen

| CSS-Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-lock-z-index` | `10` | Stapelreihenfolge des Overlays. |
| `--uix-lock-display` | `block` | CSS-Display des Overlays. |
| `--uix-lock-opacity` | `0.5` | Deckkraft von Icon und Hintergrund zusammen. |
| `--uix-lock-background` | `transparent` | Hintergrundfarbe im gesperrten Zustand. |
| `--uix-lock-background-unlocked` | `none` | Hintergrundfarbe im entsperrten Zustand. |
| `--uix-lock-background-blocked` | `--uix-lock-background` | Hintergrund, wenn dauerhaft blockiert ist. |
| `--uix-lock-border-radius` | `inherit` | Rundung des Overlays. |
| `--uix-lock-icon-size` | `24px`, bei `ha-tile-icon` `12px` | Größe des Schlossicons. |
| `--uix-lock-icon-background` | `none` | Hintergrund des Iconelements. |
| `--uix-lock-icon-border-radius` | `none`, bei `ha-tile-icon` `50%` | Rundung des Iconelements. |
| `--uix-lock-icon-padding` | `0`, bei `ha-tile-info` `2px` | Innenabstand um das Icon. |
| `--uix-lock-icon-position` | `none` | CSS-`translate`, z. B. `30px 6px`. |
| `--uix-lock-icon-fade-duration` | `2s` | Dauer des Ausblendens, wenn kein `icon_unlocked` gesetzt ist. |
| `--uix-lock-row-background` | `--uix-lock-background` | Hintergrund bei `row`-Mold. |
| `--uix-lock-row-border-radius` | `--uix-lock-border-radius` | Rundung bei `row`-Mold. |
| `--uix-lock-row-outlined-blocked` | `none` | Outline bei dauerhaft blockiertem Row-Mold. |
| `--uix-lock-cursor` | `pointer` | Cursor im Overlay. |
| `--uix-lock-cursor-locked` | `--uix-lock-cursor` | Cursor im gesperrten Zustand. |
| `--uix-lock-cursor-unlocked` | `--uix-lock-cursor` | Cursor im entsperrten Zustand. |
| `--uix-lock-cursor-blocked` | `--uix-lock-cursor` | Cursor bei dauerhaft blockiertem Zustand. |

### Styling-Beispiele

```yaml
uix:
  style: |
    :host {
      --uix-lock-background: rgba(0, 0, 0, 0.35);
      --uix-lock-icon-background: var(--card-background-color);
      --uix-lock-icon-border-radius: 999px;
      --uix-lock-icon-padding: 4px;
    }
```

```yaml
uix:
  style: |
    :host {
      --uix-lock-icon-size: 14px;
      --uix-lock-icon-position: 2px 2px;
    }
```

## Templates

Lock-Werte können Templates nutzen, wenn du Regeln an Zustandswerte koppeln willst.

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: "&#123;&#123; states('input_text.dashboard_pin') &#125;&#125;"
          admins: true
```

::: tip
Für robuste Dashboards ist es meist besser, PINs nicht aus frei sichtbaren Helpern zu lesen. Templates eignen sich eher für `active`, `confirmation` oder Benutzergruppenlogik.
:::
