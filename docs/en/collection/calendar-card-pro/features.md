---
title: Calendar Card Pro Features
description: English overview of the most important Calendar Card Pro functions.
---
<a id="calendar-card-pro-features"></a>
<a id="current-focus"></a>

# Features {#features}

## Visual editor {#visueller-editor}

The card has a visual editor. According to the original, this was rebuilt in version `4.0.0` and divided into several areas. It offers settings search, custom value filters, calendar related settings, and column view exceptions. Since `4.1.0`, the editor can duplicate calendar blocks so that a calendar can be used multiple times with different filters, colors or event types.

## Multiple calendars {#mehrere-kalender}

Multiple calendars can be displayed in a card. Each calendar can have its own colors and display options.

Since `4.1.0`, a calendar can also be divided according to appointment type. With `event_type: timed` only appointments with a time are displayed, with `event_type: all_day` only all-day appointments are displayed. This means that the same calendar can be integrated twice and colored differently.

```yaml
entities:
  - entity: calendar.family
    label: Familie ganztägig
    event_type: all_day
    accent_color: "#ff9800"
  - entity: calendar.family
    label: Familie Termine
    event_type: timed
    accent_color: "#03a9f4"
```

## Compact view {#kompakte-ansicht}

`compact_events_to_show` and `compact_days_to_show` can be used to limit how many appointments or days are directly visible. With `tap_action: expand` you can switch between compact and expanded view.

## Column view {#spaltenansicht}

With `view: column`, days are displayed side by side as columns. This is particularly suitable for weekly overviews on broad dashboards.

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
view: column
days_to_show: 7
column:
  min_day_width: 150
  min_days_to_show: 3
  min_days_fallback: list
```

If there is not enough width, the card may collapse columns or fall back into list view.

## Dynamic start date {#dynamisches-startdatum}

`start_date` can be a fixed date or a relative expression.

Examples:

| Value | Meaning |
| --- | --- |
| `today` | Start today |
| `today+7` | Start in seven days |
| `start_of_week` | Start at the beginning of the week |
| `monday+1w` | Monday of next week |
| `saturday` | Start on Saturday |

## Multi-day appointments {#mehrtagige-termine}

With `split_multiday_events`, multi-day appointments can be displayed on each affected day. This is particularly useful in the column view because each column represents a day.

There is additional control for all-day appointments: `allday_expires_at` causes all-day appointments in a calendar to disappear at a time on the last day if `show_past_events` is deactivated. This is useful for garbage collection or reminder calendars, for example.

```yaml
entities:
  - entity: calendar.waste
    label: Abfall
    allday_expires_at: "10:00"
```

## Weekdays And Weekends {#wochentage-und-wochenenden}

With `days_of_week` a calendar can be restricted to working days or weekends. For split multi-day appointments, each day displayed is evaluated individually.

```yaml
entities:
  - entity: calendar.school
    days_of_week: weekdays
  - entity: calendar.family
    days_of_week: weekends
```

## All day badges {#ganztags-badges}

With `allday_badge`, all-day appointments can be displayed as a badge. `title` places the badge around the title, `time` replaces the all day line next to the clock icon. `allday_badge_style` controls the shape, `allday_badge_color` controls the color.

```yaml
allday_badge: title
allday_badge_style: subtle
allday_badge_color: accent
```

## Filters and text replacement {#filter-und-textersetzung}

By default, `blocklist` and `allowlist` read the title. With `filter_field` they can be applied to `location` or `description` instead.

`replace_field`, `replace_pattern` and `replace_with` change the text displayed when the card is rendered without changing the original appointment in the calendar.

```yaml
entities:
  - entity: calendar.work
    filter_field: location
    allowlist: teams.microsoft.com
    replace_field: title
    replace_with: Besetzt
```

## Location icon {#orts-icon}

Microsoft Teams appointments can appear automatically with a Teams icon instead of a card pin. `location_icon` can set its own icon per calendar or force the normal marker again with `mdi:map-marker-outline`.

## Weather integration {#wetterintegration}

A Home Assistant weather entity can be integrated with `weather`. Weather data can appear in the day header, next to appointments or in both places.

```yaml
weather:
  entity: weather.home
  position: both
  date:
    show_high_temp: true
    show_low_temp: true
  event:
    show_temp: true
    show_conditions: true
```

## Actions {#aktionen}

The card supports `tap_action` and `hold_action`. This can be used, for example, to open details, expand the card, carry out navigation or call up a service.

## Templates {#templates}

The title can contain Home Assistant templates. There are also placeholders such as number of appointments or next appointment that can be used for dynamic titles.

## Theming {#theming}

Calendar Card Pro is theme-aware and can be customized using options and CSS variables. `card-mod` can be used for deeper styling.

## Performance {#performance}

According to the original, the card uses intelligent updating and caching. Version `4.0.0` reduces the download because the editor is loaded separately and avoids duplicate calendar queries.
