---
title: Calendar Card Pro Beispiele
description: Praxisbeispiele für Calendar Card Pro in Home Assistant.
---
# Beispiele

## Einfache Konfiguration

Zeigt Termine aus einem Kalender und passt sich automatisch an Theme sowie Hell-/Dunkelmodus an.

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/example_1_basic_native.png" alt="Einfache Calendar Card Pro Konfiguration" width="600">

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
days_to_show: 3
show_location: false
show_month: false
```

## Mehrere Kalender Mit Kompaktem Modus

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

## Mehrere Kalender Mit Eigener Gestaltung

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/example_3_custom_styling.png" alt="Calendar Card Pro mit eigener Gestaltung" width="600">

```yaml
type: custom:calendar-card-pro
entities:
  - entity: calendar.family
    accent_color: '#ff6c92'
  - entity: calendar.work
    accent_color: '#1e88e5'
  - entity: calendar.personal
    accent_color: '#43a047'
days_to_show: 5
compact_events_to_show: 5
event_background_opacity: 20
vertical_line_width: 5px
event_spacing: 6px
```

## Wochennummern Und Trennlinien

```yaml
type: custom:calendar-card-pro
entities:
  - entity: calendar.personal
    accent_color: '#03a9f4'
  - entity: calendar.family
    accent_color: '#ff6c92'
days_to_show: 5
compact_events_to_show: 5
vertical_line_width: 5px
event_spacing: 5px
show_week_numbers: iso
week_separator_width: 1px
week_separator_color: '#03a9f450'
month_separator_width: 1.5px
month_separator_color: var(--secondary-text-color)
```

## Wochenansicht Als Spalten

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/example_column_week.png" alt="Calendar Card Pro Wochenansicht als Spalten" width="600">

```yaml
type: custom:calendar-card-pro
entities:
  - entity: calendar.family
    color: '#e67c73'
  - entity: calendar.work
    color: '#03a9f4'
view: column
days_to_show: 7
show_week_numbers: iso
today_indicator: true
empty_day_text: 'Alles erledigt'
column:
  min_day_width: 150
  min_days_to_show: 3
  min_days_fallback: list
  show_location: false
  event_font_size: 12px
  day_header_separator_width: 1px
```

## Umfangreiche Konfiguration

```yaml
type: custom:calendar-card-pro

entities:
  - entity: calendar.family
    color: '#ffdaea'
  - entity: calendar.work
    color: '#b3ffd9'
start_date: today
days_to_show: 10
compact_events_to_show: 10
language: de

title: Kalender
title_font_size: 26px
title_color: '#baf1ff'

background_color: '#eeeeee50'
accent_color: '#baf1ff'
vertical_line_width: 0px
day_spacing: 10px
additional_card_spacing: 0px

day_separator_width: 2px
day_separator_color: '#baf1ff80'

date_vertical_alignment: middle
weekday_font_size: 14px
weekday_color: '#baf1ff'
day_font_size: 32px
day_color: '#baf1ff'
show_month: true
month_font_size: 12px
month_color: '#baf1ff'

show_past_events: false
event_font_size: 14px
event_color: '#baf1ff'
time_24h: true
time_two_digit_hours: false
show_end_time: true
time_font_size: 12px
time_color: '#baf1ff'
time_icon_size: 14px
show_location: true
remove_location_country: true
location_font_size: 12px
location_color: '#baf1ff'
location_icon_size: 14px

tap_action:
  action: expand
hold_action:
  action: navigate
  navigation_path: calendar

refresh_interval: 15
```
