---
title: Lock Spark
---
# Lock Spark

Der Lock Spark legt eine Sperrebene ueber ein Forge-Element oder ueber ein gezieltes Unterelement. Er kann je nach Benutzer, Adminstatus, PIN, Code oder Bestaetigung entsperrt werden.

::: tip
Der Spark schuetzt die Bedienung in der Oberflaeche. Er ersetzt keine serverseitige Home-Assistant-Berechtigung.

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

## Ziel mit `for` waehlen

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
Nutze keine PINs fuer echte Sicherheitsgrenzen. UIX laeuft im Browser und kann Bedienfehler vermeiden, aber keine Home-Assistant-Rechte erzwingen.

:::
## Matching-Logik

| Konfiguration | Wen sie trifft |
| --- | --- |
| `users`-Liste vorhanden | Nutzer, deren Name in der Liste steht. Mit `admins: true` zusaetzlich Admins. |
| Keine `users`-Liste | Alle Nicht-Admins, die nicht in `except` stehen. |
| Keine `users`-Liste und `admins: true` | Alle Nutzer, Admins und Nicht-Admins, sofern sie nicht in `except` stehen. |

## Konfigurationsreferenz

### Top-Level

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | string | - | Muss `lock` sein. |
| `for` | string | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor fuer das Element, ueber das die Sperre gelegt wird. |
| `action` | string | `tap` | Geste zum Entsperren: `tap`, `hold` oder `double_tap`. |
| `duration` | number oder string | `3000` | Dauer bis zum erneuten Sperren nach erfolgreichem Entsperren. Zahlen sind Millisekunden, Strings z. B. `5s`, `1m`, `500ms`. |
| `icon_locked` | string | `mdi:lock-outline` | Icon im gesperrten Zustand. |
| `icon_unlocked` | string | - | Icon im entsperrten Zustand. Ohne Wert blendet das Schloss aus. |
| `icon_locked_color` | string | `--error-color` | Farbe des gesperrten Icons. |
| `icon_unlocked_color` | string | `--success-color` | Farbe des entsperrten Icons. |
| `icon_position` | object | je nach Ziel | Pixel-Offsets des Icons. Erlaubt `top` oder `bottom` und `left` oder `right`. |
| `icon_size` | number oder string | `24px`, bei `ha-tile-icon` `12px` | Icongroesse. `--uix-lock-icon-size` hat Vorrang. |
| `permissive` | boolean | `false` | Bei `true` bleiben Elemente zugaenglich, wenn kein Lock-Eintrag zum aktuellen Nutzer passt. |
| `entity` | string | - | Entity-ID fuer einfache HA-Aktionen in `unlocked_action`. |
| `unlocked_action` | object | - | Aktion direkt nach erfolgreichem Entsperren. |
| `locks` | list | `[]` | Geordnete Liste von Lock-Eintraegen. |
| `code_dialog` | object | - | Optionen fuer den Code- oder Passphrase-Dialog. |

### `code_dialog`

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `title` | string | HA-Standard | Dialogtitel. |
| `submit_text` | string | HA-Standard | Text des Bestaetigungsbuttons. |
| `cancel_text` | string | HA-Standard | Text des Abbrechen-Buttons. |

### `unlocked_action`

| Wert | Wirkung |
| --- | --- |
| `action: element_tap` | Loest die `tap_action` des Zielelements aus. |
| `action: element_hold` | Loest die `hold_action` des Zielelements aus. |
| `action: element_double_tap` | Loest die `double_tap_action` des Zielelements aus. |
| Beliebige HA-Aktion | Fuehrt diese Aktion gegen `entity` aus, z. B. `action: toggle`. |

### Lock-Eintraege

| Schluessel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `active` | boolean | `true` | Mit `false` wird fuer passende Nutzer explizit entsperrt. |
| `code` | string oder number | - | Einzugebender Code. Zahlen zeigen das HA-Nummernfeld, Text zeigt ein Passwortfeld. |
| `pin` | string oder number | - | Alias fuer `code`. |
| `confirmation` | string oder boolean | - | Bestaetigungsdialog. `true` nutzt den HA-Standardtext, ein String nutzt eigenen Text. |
| `users` | Liste von Strings | - | Nutzernamen, fuer die dieser Eintrag gilt. |
| `admins` | boolean | `false` | Additiv. Ohne `users` erfasst `admins: true` alle Nutzer. Mit `users` werden Admins zusaetzlich erfasst. |
| `except` | Liste von Strings | - | Ausnahmen, wenn keine `users`-Liste gesetzt ist. |
| `retry_delay` | number oder string | - | Wartezeit zwischen falschen Codeversuchen. |
| `max_retries` | number | - | Anzahl falscher Versuche vor der laengeren Sperrzeit. |
| `max_retries_delay` | number oder string | `30000` | Sperrzeit nach `max_retries`, z. B. `30s` oder `5m`. |

## Beispiele

### Gleiche PIN fuer alle, inklusive Admins

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1234
          admins: true
```

### Keine Sperre fuer Admins und einen bestimmten Nutzer

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: 1234
          except:
            - Max
```

### Bestaetigung fuer alle inklusive Admins

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - confirmation: true
          admins: true
```

### PIN fuer alle, aber nicht fuer genannte Nutzer

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

### Nach Entsperren die Hold-Aktion der Tile Card ausfuehren

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
| `--uix-lock-icon-size` | `24px`, bei `ha-tile-icon` `12px` | Groesse des Schlossicons. |
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

Lock-Werte koennen Templates nutzen, wenn du Regeln an Zustandswerte koppeln willst.

```yaml
forge:
  sparks:
    - type: lock
      locks:
        - pin: "&#123;&#123; states('input_text.dashboard_pin') &#125;&#125;"
          admins: true
```

::: tip
Fuer robuste Dashboards ist es meist besser, PINs nicht aus frei sichtbaren Helpern zu lesen. Templates eignen sich eher fuer `active`, `confirmation` oder Benutzergruppenlogik.
:::
