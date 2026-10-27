---
title: Calendar Card Pro configuration
description: English configuration reference for Calendar Card Pro.
---
<a id="calendar-card-pro-configuration"></a>
<a id="current-focus"></a>

# Configuration reference {#konfigurationsreferenz}

This page maps the option groups of the original reference. The original English reference remains relevant for detailed examples.

## New In v4.1.0 {#neu-in-v4-1-0}

Version `4.1.0` adds several calendar-related controls:

- `event_type` separates appointments with time from all-day appointments.
- `filter_field` makes `blocklist` and `allowlist` work on title, location or description.
- `replace_field`, `replace_pattern` and `replace_with` change the displayed text without changing the calendar event itself.
- `allday_expires_at` causes all-day appointments in a calendar to expire earlier in the day.
- `days_of_week` limits a calendar to working days or weekends.
- `allday_badge`, `allday_badge_style` and `allday_badge_color` control the new badge display for all-day appointments.

## Basic settings {#grundeinstellungen}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `entities` | array | required | List of calendar entities, optionally with own settings per calendar. |
| `view` | string | `list` | Layout: `list` for days one below the other, `column` for days next to one another. |
| `start_date` | string | today | Start date as `YYYY-MM-DD` or relative expression like `today+7`, `start_of_week`, `monday+1w`. |
| `days_to_show` | number | `3` | Number of days displayed. |
| `event_type` | string | `all` | Appointment type: `all`, `timed` or `all_day`. Can be set globally or per calendar. |
| `compact_days_to_show` | number | - | Number of days in compact mode. |
| `compact_events_to_show` | number | - | Number of appointments in compact mode. |
| `compact_events_complete_days` | boolean | `false` | Shows all appointments for days on which at least one appointment is visible. |
| `show_empty_days` | boolean | `false` | Show days without appointments. In the column view, `true` by default. |
| `hide_when_empty` | boolean | `false` | Hide card if there are no upcoming appointments. |
| `empty_day_text` | string | localized default | Custom text for empty days or completely empty cards. |
| `filter_duplicates` | boolean | `false` | Hide duplicate events if title, start, end and location are the same. |
| `split_multiday_events` | boolean | `false` | Show multi-day appointments on each affected day. In the column view, `true` by default. |
| `language` | string | System, fallback `en` | Language of the card texts, automatically recognized by Home Assistant. |
| `column` | object | inherits top-level values | Special display options for `view: column`. |

## For column view only {#nur-fur-die-spaltenansicht}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `column.day_header_gap` | string | `8px` | Distance between day head and first appointment. |
| `column.day_header_separator_width` | string | `0px` | Width of line under day header. |
| `column.day_header_separator_color` | string | `var(--divider-color)` | Color of the line under the day header. |
| `column.min_day_width` | number | `140` | Smallest column width in pixels. |
| `column.min_days_to_show` | number | `days_to_show` | Minimum number of visible columns. |
| `column.min_days_fallback` | string | `list` | Behavior if there is not enough space: `list` or `cramp`. |

## Options have no effect in the column view {#optionen-ohne-wirkung-in-der-spaltenansicht}

These options remain relevant for the list view, but do not work directly in the column view:

`date_vertical_alignment`, `today_indicator_position`, `compact_events_to_show`, `compact_days_to_show`, `compact_events_complete_days`, calendar related `split_multiday_events`.

## Calendar related options {#kalenderbezogene-optionen}

An entry in `entities` can only be an entity ID or an object with its own settings.

| option | Description |
| --- | --- |
| `entity` | Calendar entity, for example `calendar.family`. |
| `label` | Own labeling of the calendar. |
| `label_type` | Controls how the caption is read. |
| `color` | Calendar color. |
| `accent_color` | Accent color for line and optional backgrounds. |
| `label_icon_color` | Color for label/icon. |
| `show_time` | Show time for this calendar. |
| `show_location` | Show location for this calendar. |
| `location_icon` | Icon for location information for this calendar, for example `mdi:office-building`; can override automatic Teams discovery. |
| `show_description` | Show description for this calendar. |
| `compact_events_to_show` | Compact limit for this calendar. |
| `blocklist` | Exclude terms or patterns. |
| `allowlist` | Show only matching terms or patterns. |
| `filter_field` | Field for `blocklist`/`allowlist`: `title`, `location` or `description`. |
| `replace_field` | Text replacement field: `title`, `location` or `description`. |
| `replace_pattern` | Regex pattern to replace or remove in the selected field. |
| `replace_with` | replacement text; without `replace_pattern` the entire field is replaced. |
| `split_multiday_events` | Split multi-day appointments for this calendar. |
| `event_type` | Calendar-related appointment type: `all`, `timed` or `all_day`. |
| `allday_expires_at` | Time in format `HH:MM` from which all-day appointments in this calendar are considered past. |
| `days_of_week` | Limitation to `weekdays` or `weekends`. |

## Headers {#header}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | string | - | Map title, may contain Home Assistant templates. |
| `title_font_size` | string | `--calendar-card-font-size-title` | Title font size. |
| `title_color` | string | `--calendar-card-color-title` | Title color. |

## Layout And Spacing {#layout-und-abstande}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `background_color` | string | `--ha-card-background` | Background color of the card. |
| `accent_color` | string | `#03a9f4` | Accent color of the vertical line and optional appointment/all day badges. |
| `vertical_line_width` | string | `2px` | Vertical line width. |
| `day_spacing` | string | `10px` | Distance between days or columns. |
| `event_spacing` | string | `4px` | Inner spacing within an appointment. |
| `additional_card_spacing` | string | `0px` | Additional space at the top/bottom of the card. |
| `height` | string | `auto` | Exact fixed card height. |
| `max_height` | string | `none` | Maximum card height as content grows. |

## Week numbers and dividing lines {#wochennummern-und-trennlinien}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `show_week_numbers` | string | `null` | Show week numbers: `iso`, `simple` or disabled. |
| `show_current_week_number` | boolean | `true` | Show week number for current/first week. |
| `week_number_font_size` | string | `12px` | Week number font size. |
| `week_number_color` | string | `var(--primary-text-color)` | Week number text color. |
| `week_number_background_color` | string | `#03a9f450` | Week number background color. |
| `first_day_of_week` | string | `system` | Start of week: `monday`, `sunday` or `system`. |
| `day_separator_width` | string | `0px` | dividing line between days. |
| `day_separator_color` | string | `var(--secondary-text-color)` | Tag separator color. |
| `week_separator_width` | string | `0px` | dividing line between weeks. |
| `week_separator_color` | string | `#03a9f450` | Color of the week separator line. |
| `month_separator_width` | string | `0px` | dividing line between months. |
| `month_separator_color` | string | `var(--primary-text-color)` | Color of the month separator line. |

## Today marker {#heute-markierung}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `today_indicator` | boolean/string | `false` | Today tag: `true`, `dot`, `pulse`, `glow`, MDI icon, emoji or image path. |
| `today_indicator_position` | string | `15% 50%` | Position in CSS format. |
| `today_indicator_color` | string | `#03a9f4` | Color of the marking. |
| `today_indicator_size` | string | `6px` | Size of the mark. |

## Date column {#datumsspalte}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `date_vertical_alignment` | string | `middle` | Vertical alignment: `top`, `middle`, `bottom`. |
| `weekday_font_size` | string | `14px` | Font size of the day of the week. |
| `weekday_color` | string | `--primary-text-color` | Color of the day of the week. |
| `day_font_size` | string | `26px` | Font size of the day number. |
| `day_color` | string | `--primary-text-color` | Color of the day number. |
| `show_month` | boolean | `true` | Show month names. |
| `month_font_size` | string | `12px` | Font size of the month. |
| `month_color` | string | `--primary-text-color` | month color. |
| `weekend_weekday_color` | string | inherits `weekday_color` | Weekday color on weekends. |
| `weekend_day_color` | string | inherits `day_color` | Weekend day number color. |
| `weekend_month_color` | string | inherits `month_color` | Monthly color on the weekend. |
| `today_weekday_color` | string | inherits weekend/standard | Weekday color for today. |
| `today_day_color` | string | inherits weekend/standard | Day number color for today. |
| `today_month_color` | string | inherits weekend/standard | Monthly color for today. |

## Appointment column {#terminspalte}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `event_background_opacity` | number | `0` | Background opacity for appointments with accent color, 0-100. |
| `event_icon_vertical_alignment` | string | `top` | Vertical icon orientation: `top`, `middle`, `bottom`. |
| `show_past_events` | boolean | `false` | Show appointments that have already ended. |
| `show_countdown` | boolean | `false` | Show countdown to appointment. |
| `show_countdown_allday` | boolean | `true` | Show countdown for all-day appointments too. |
| `show_multiday_allday_time` | boolean | `true` | Show time line for all-day appointments lasting several days; it carries the end date information. |
| `allday_badge` | string | `off` | Full Day Badge Location: `off`, `title` or `time`. |
| `allday_badge_style` | string | `subtle` | Badge style: `subtle`, `outline`, `tinted` or `filled`. |
| `allday_badge_color` | string | `accent` | Badge color: `accent`, `text` or a CSS color. |
| `show_progress_bar` | boolean | `false` | Show progress bar for ongoing appointments. |
| `progress_bar_color` | string | `var(--secondary-text-color)` | Color of the progress bar. |
| `progress_bar_height` | string | calculated | Height of the progress bar. |
| `progress_bar_width` | string | per layout | Width of progress bar. |
| `empty_day_color` | string | `--primary-text-color` | Color for text on empty days. |
| `event_font_size` | string | `14px` | Font size of the appointment title. |
| `title_max_lines` | number | `0` | Maximum lines for appointment titles, `0` = unlimited. |
| `event_color` | string | `--primary-text-color` | Color of the appointment title. |
| `show_time` | boolean | `true` | Show appointment time. |
| `show_single_allday_time` | boolean | `true` | Show time display for individual all-day appointments. |
| `time_24h` | boolean | System | Use 24-hour format. |
| `time_two_digit_hours` | boolean | `false` | Show hours in double digits. |
| `show_end_time` | boolean | `true` | Show end time. |
| `time_icon_size` | string | `14px` | Clock icon size. |
| `time_font_size` | string | `12px` | Font size of the time. |
| `time_color` | string | `--secondary-text-color` | color of time. |
| `time_max_lines` | number | `0` | Maximum lines for time text. |
| `show_location` | boolean | `true` | Show location. |
| `show_location_allday` | boolean | `true` | Show locations even for all-day appointments if `show_location` is active. |
| `remove_location_country` | boolean/string | `false` | Remove country names from locations, optionally via regex string. |
| `location_icon_size` | string | `14px` | Location icon size. |
| `location_font_size` | string | `12px` | Font size of the location. |
| `location_color` | string | `--secondary-text-color` | Color of the place. |
| `location_max_lines` | number | `0` | Maximum rows for location. |
| `show_description` | boolean | `false` | Show description. |
| `show_description_allday` | boolean | `true` | Show descriptions even for all-day appointments if `show_description` is active. |
| `description_icon_size` | string | `14px` | Description icon size. |
| `description_font_size` | string | `12px` | Description font size. |
| `description_color` | string | `--secondary-text-color` | Color of description. |
| `description_max_lines` | number | `0` | Maximum lines for description. |

## Weather {#wetter}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `weather` | object | - | Weather configuration. |
| `weather.entity` | string | - | Weather entity for forecasts. |
| `weather.position` | string | `date` | Position: `none`, `date`, `event`, `both`. |
| `weather.date` | object | - | Weather display in the day header. |
| `weather.event` | object | - | Weather display next to appointments. |

`weather.date` accepted: `show_conditions`, `show_high_temp`, `show_low_temp`, `show_uv_index`, `uv_index_threshold`, `icon_size`, `font_size`, `color`.

`weather.event` accepted: `show_conditions`, `show_temp`, `show_uv_index`, `uv_index_threshold`, `daily_forecast_fallback`, `max_lines`, `icon_size`, `font_size`, `color`.

## Actions {#aktionen}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `tap_action` | object | `none` | Action when tapping the card. |
| `hold_action` | object | `none` | Action while holding the card. |

Depending on the action, action parameters can be:

`action`, `navigation_path`, `service`, `service_data`, `url_path`, `open_tab`.

## Cache And Update {#cache-und-aktualisierung}

| option | Type | Default | Description |
| --- | --- | --- | --- |
| `refresh_interval` | number | `30` | Minutes between data updates. |
| `refresh_on_navigate` | boolean | `true` | Reload when switching between dashboard views. |
