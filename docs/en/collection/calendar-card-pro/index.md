---
title: Calendar Card Pro
description: German Calendar Card Pro documentation entry in the UGSo Open Source collection.
---
# Calendar Card Pro

This is the collection entry for the German Calendar Card Pro documentation.

The German documentation is maintained as an unofficial translation and practical guide. The original Calendar Card Pro project and documentation remain authoritative.

| Field | Value |
| --- | --- |
| German documentation | [Calendar Card Pro German docs](/sammlung/calendar-card-pro/) |
| Original project | [alexpfau/calendar-card-pro](https://github.com/alexpfau/calendar-card-pro) |
| Original documentation | [calendar-card-pro.alexpfau.com](https://calendar-card-pro.alexpfau.com) |
| Tracked source commit | [`a3b01138daa44947f6673c33fe700e5ef4a08957`](https://github.com/alexpfau/calendar-card-pro/commit/a3b01138daa44947f6673c33fe700e5ef4a08957) |
| Release | `v4.1.0` |
| License | MIT |

The source files are checked daily by a scheduled GitHub Action so the German documentation can be updated when the original documentation changes.

:::: details Detailed reference from the German documentation

## Calendar Card Pro {#reference-calendar-card-pro}

Calendar Card Pro is a modern, highly customizable calendar card for Home Assistant. It displays upcoming events efficiently and clearly, supporting multiple calendars, compact views, column views, weather, templates, actions, all-day event badges, per-calendar filters and a visual editor.

::: warning Unofficial English documentation
This documentation is an unofficial English working translation and practical documentation. The original Calendar Card Pro project and its English documentation remain authoritative.
:::

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/header.png" alt="Calendar Card Pro Vorschau" width="100%">

| field | Value |
| --- | --- |
| Original project | [alexpfau/calendar-card-pro](https://github.com/alexpfau/calendar-card-pro) |
| Original documentation | [calendar-card-pro.alexpfau.com](https://calendar-card-pro.alexpfau.com) |
| Checked commit | [`a3b01138daa44947f6673c33fe700e5ef4a08957`](https://github.com/alexpfau/calendar-card-pro/commit/a3b01138daa44947f6673c33fe700e5ef4a08957) |
| Release | [`v4.1.0`](https://github.com/alexpfau/calendar-card-pro/releases/tag/v4.1.0) |
| License | [MIT](https://github.com/alexpfau/calendar-card-pro/blob/main/LICENSE) |
| Status | English documentation with installation, usage, features, reference, examples and change checking |

### Content {#inhalt}

- [Installation](/en/collection/calendar-card-pro/installation)
- [Usage](/en/collection/calendar-card-pro/nutzung)
- [Features](/en/collection/calendar-card-pro/features)
- [Configuration Reference](/en/collection/calendar-card-pro/konfiguration)
- [Examples](/en/collection/calendar-card-pro/beispiele)
- [Development and Contribution](/en/collection/calendar-card-pro/entwicklung)
- [License and Source](/en/collection/calendar-card-pro/lizenz-und-stand)

### What is the card for? {#wofur-ist-die-karte-gedacht}

Calendar Card Pro is intended for dashboards on which calendar events should be displayed in an easy-to-read, compact and visually clean manner. The card is particularly interesting if several calendars are to be merged, appointments should be differentiated by color according to calendar or a weekly view is needed as a column layout.

The card requires at least one home assistant entity of type `calendar.*`. According to the original, CalDAV and Google Calendar were particularly tested; in principle, the card works with integrations that provide calendar entities.

::::
