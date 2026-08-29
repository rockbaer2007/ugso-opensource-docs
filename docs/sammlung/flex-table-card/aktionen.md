---
title: flex-table-card Aktionen
description: Zellaktionen, Tap-Actions und Edit-Actions der flex-table-card.
---
# Aktionen

Spalten koennen Home-Assistant-Aktionen ausloesen. Unterstuetzt werden typische Lovelace-Aktionen wie `more-info`, `toggle`, `perform-action`, `navigate`, `url`, `assist` und auch `fire-dom-event`.

## More-info beim Tippen

```yaml
type: custom:flex-table-card
title: Lichter
entities:
  include: light.*
columns:
  - name: Name
    data: name
    tap_action:
      action: more-info
  - name: Status
    data: state
```

## Aktion mit Spaltenwerten

Innerhalb einer Zeile koennen Werte anderer Spalten referenziert werden.

| Referenz | Bedeutung |
| --- | --- |
| `cell[n]` | sichtbare Spalte mit Index `n` |
| `col[n]` | Spalte mit Index `n`, auch wenn sie versteckt ist |

```yaml
type: custom:flex-table-card
title: Navigation
entities:
  include: sensor.room_*
columns:
  - name: Raum
    data: name
  - name: Pfad
    data: dashboard_path
    hidden: true
  - name: Oeffnen
    data: name
    tap_action:
      action: navigate
      navigation_path: col[1]
```

## Hinweis zu alten Begriffen

Home Assistant nutzt heute `action` und `perform-action`. Alte Begriffe wie `call-service`, `service` oder `service_data` sollten fuer Spaltenaktionen nicht mehr genutzt werden.

