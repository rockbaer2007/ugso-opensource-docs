---
title: Calendar Card Per Usage
description: Use Calendar Card Pro in the Home Assistant dashboard.
---
<a id="calendar-card-pro-usage"></a>
<a id="current-focus"></a>

# Usage {#nutzung}

## Add card via editor {#karte-per-editor-hinzufugen}

1. Open dashboard.
2. Edit dashboard.
3. Add new card.
4. Search for `Calendar`.
5. Select Calendar Card Pro.
6. Open the three-dot menu of the card.
7. Select **Configure** to open the visual editor.

From Home Assistant `2026.6`, according to the original, the card can also be suggested in the **By entity** tab if a `calendar.*` entity is selected.

## Quick start via YAML {#schnellstart-per-yaml}

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
days_to_show: 3
show_location: false
show_month: false
```

`calendar.family` needs to be replaced with its own calendar entity.

## Multiple calendars {#mehrere-kalender}

```yaml
type: custom:calendar-card-pro
title: Termine
entities:
  - entity: calendar.family
    color: '#ff6c92'
  - entity: calendar.work
    color: '#86ebda'
  - entity: calendar.personal
    color: '#c2ffb3'
days_to_show: 7
compact_events_to_show: 3
tap_action:
  action: expand
```

## Typical applications {#typische-einsatzfalle}

- Family calendar in the dashboard
- Work and private calendars in one view
- Weekly overview in columns
- Appointments with weather forecast
- compact calendar card for wall tablets
- dynamic titles with next appointment or number of appointments
