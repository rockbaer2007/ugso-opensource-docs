---
title: HA Dashboard
description: Dashboard themes, layout ideas and visual extensions for Home Assistant.
---
# HA Dashboard

This section collects Home Assistant dashboard topics that are not individual cards and not integrations.

## Dashboard Extensions

| Project | Status | Note |
| --- | --- | --- |
| [Dashboard Layout Card V2](https://github.com/rockbaer2007/lovelace-layout-card-v2) | experimental | Fork of Lovelace layout-card with dedicated V2 layout types, side tab menu, subviews, new subviews defaulting to Sections V2, home entry, theme inheritance from the home view, clock/date display, optional analog hour/minute marks, colors, 3D frames, dividers that inherit colors from the previous divider, notification box, status values and optional hiding of the Home Assistant header/sidebar. |

![Dashboard Layout Card V2 view](/images/dashboard-layout-card-v2/view.png)

The V2 layouts appear in the normal Home Assistant view layout selector next to
the standard layouts.

![Dashboard Layout Card V2 view layout selection](/images/dashboard-layout-card-v2/view-layout-selection.png)

Sections V2 views behave close to Home Assistant's native Sections view in edit
mode. Sections can be moved with the three-line drag handle, and the new order
is saved back to the view.

<video controls src="/images/dashboard-layout-card-v2/demo.mp4" style="width: 100%; border-radius: 8px;"></video>

Note: Portrait images work best for menu backgrounds. A practical aspect ratio is about `1:2.5` width:height. Other formats are supported, but `cover` may crop them depending on the visible menu area. Only use images you own or images with a compatible free/open-source license.

### Notification And Status Values

The optional notification box appears above the status values in the side menu. A text helper such as `input_text.dashboard_notification` is recommended. While the entity is missing, empty, `unknown` or `unavailable`, the box remains hidden. If the helper does not exist yet, the editor shows a short hint explaining how to create the text helper.

![Dashboard Layout Card V2 missing helper hint](/images/dashboard-layout-card-v2/notify-helper-missing.png)

As soon as the helper contains text, the message appears in the menu, for example for faults, maintenance notes or short dashboard-wide alerts. Up to four status values can be shown below it. Numeric values are formatted compactly with at most one decimal place.

![Dashboard Layout Card V2 notification and status values](/images/dashboard-layout-card-v2/notify-and-status.png)

At viewport widths up to and including 600 pixels, menu buttons show icons only. Desktop keeps the text labels. Entries without a custom icon use a dashboard icon on mobile; page names remain available as tooltips and to screen readers.

## Themes

| Project | Status | Note |
| --- | --- | --- |
| [Frosted Glass Theme](/sammlung/frosted-glass-theme/) | reviewed | Modern Home Assistant theme with glass styling, HACS installation, card-mod or UIX requirement and Lite variants. |
| [NeoMorphix UIX](/sammlung/neomorphix-uix/) | reviewed | Neumorphic Home Assistant theme with light, dark, Claude and inset variants; UIX variants are proposed as a PR. |
