---
title: flex-table-card actions
description: Cell actions, tap actions and edit actions of the flex-table-card.
---
<a id="flex-table-card-actions"></a>
<a id="current-focus"></a>

# Actions {#aktionen}

Columns can trigger Home Assistant actions. Typical Lovelace actions such as `more-info`, `toggle`, `perform-action`, `navigate`, `url`, `assist` and also `fire-dom-event` are supported.

## More info while typing {#more-info-beim-tippen}

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

## Action with column values {#aktion-mit-spaltenwerten}

Values from other columns can be referenced within a row.

| Reference | Meaning |
| --- | --- |
| `cell[n]` | visible column with index `n` |
| `col[n]` | Column with index `n` even if hidden |

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

## Note on old terms {#hinweis-zu-alten-begriffen}

Home Assistant today uses `action` and `perform-action`. Old terms like `call-service`, `service` or `service_data` should no longer be used for column actions.
