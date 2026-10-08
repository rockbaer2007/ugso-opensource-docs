---
title: UGSo Calendar +
description: Independent calendar widget set with automatic discovery, upcoming events and a details popup.
---

# UGSo Calendar +

**UGSo Calendar + 0.1.0** is an independent external widget set by **rockbaer2007** for **Grafik Visual Studio 0.1.266 or newer**. It discovers all available Home Assistant calendars automatically and displays upcoming events as a compact card or expanded list. All calendars are enabled initially.

Runtime with sample data:

![UGSo Calendar + with colored date tiles, day groups and upcoming events](/images/grafik-visual-studio/calendar-plus.png)

## Original project

Inspired by **[calendar-card-plus by xBourner](https://github.com/xBourner/calendar-card-plus)**, published under the [MIT license](https://github.com/xBourner/calendar-card-plus/blob/main/LICENSE), Copyright (c) 2026 xBourner. UGSo Calendar + uses an independent Studio implementation and its own palette icon. No original source code or images are included. This set is independent of Industrial and the separately usable original Lovelace card.

## Installation

1. Update Studio to **0.1.266 or newer**.
2. [Download ugso.calendar-plus.wg](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/calendar-plus/ugso.calendar-plus.wg).
3. Install under **Settings → Widget packages → Local**.
4. Drag **UGSo Calendar + → Calendar +** from the palette onto the page.

The package contains declarative data, an icon, instructions and the MIT license. Studio provides the fixed `calendar-plus` host renderer; there are no executable package scripts. [Source and package instructions](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/calendar-plus).

## My calendars

All available `calendar.*` entities are discovered, including calendars without a registry entry. Registry entries disabled in Home Assistant are omitted. **My calendars** provides a section for each calendar with its entity ID, **Show/Hide**, **Color** and optional **Background color**. There is no manual calendar count.

Visibility and colors are saved by entity ID. Newly discovered calendars are enabled automatically; hidden calendars are not queried for events. The number of discovered calendars is unlimited. Requests use batches of at most 20 calendars through the Home Assistant interface.

## Settings

| Section | Setting |
| --- | --- |
| Configuration | Heading, **1–90 days** lookahead, **1–20** visible events, expand events, details popup, dividers. |
| Grouping | By day, additionally by calendar; optionally show empty days. |
| Upcoming events | Show/hide relative labels such as “Tomorrow”, “In 2 days” or “In progress”. |
| Text & visibility | Individually show/hide calendar name, date, location, duration, time and weekday; full/short weekday; swap month and weekday in the date tile. |
| Colors | Automatic browser theme or fixed light/dark mode, accent color and **10–24 px** font size. Per-calendar colors and backgrounds are configured separately. |
| Size | Default **480 × 460 px**, minimum **260 × 180 px**; the event list scrolls when space is limited. |

With the expanded list disabled, one event remains visible. In runtime, clicking an event or **All events** opens the details popup with up to 100 events. Full dates, location and description appear when available. Content is rendered as plain text. **Close**, Escape or clicking outside closes the popup.

## Data and refresh

Editor and runtime read events through `calendar.get_events`. All-day events respect the exclusive end date; expired events are removed. Refresh runs every 60 seconds while the page is visible and manually through **↻** in runtime. Calendar discovery is refreshed as well.

“No calendars found”, “All calendars hidden”, “No upcoming events” and a loading error are separate states. An error is not presented as an empty calendar. Language follows the Studio **DE/EN** setting automatically; custom headings and event content stay unchanged.

## Scope of this version

This version reads events. **New event**, editing and deleting are not included yet. Calendars must be available in Home Assistant; there is no direct ICS/Google sign-in. Installing the original card through HACS is not required.
