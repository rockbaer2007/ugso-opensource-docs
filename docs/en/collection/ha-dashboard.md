---
title: HA Dashboard
description: Dashboard themes, layout ideas and visual extensions for Home Assistant.
---
# HA Dashboard

This section collects Home Assistant dashboard topics that are not individual cards and not integrations.

## Dashboard Extensions

| Project | Status | Note |
| --- | --- | --- |
| [Dashboard Layout Card V2](https://github.com/rockbaer2007/lovelace-layout-card-v2) | experimental | Fork of Lovelace layout-card with dedicated V2 layout types, side tab menu, optional icon-only mode, submenu column, subviews, new subviews defaulting to Sections V2, home entry, theme inheritance from the home view, clock/date display, optional analog hour/minute marks, colors, border opacity, 3D frames, dividers that inherit colors from the previous divider, popup notification button in icon-only mode, status values and optional hiding of the Home Assistant header/sidebar. |

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


#### Required Helpers

Only the features enabled in the menu need helpers. Create them in Home Assistant under **Settings > Devices & services > Helpers**.

| Entity | Helper type | Purpose | Required? |
| --- | --- | --- | --- |
| `input_text.dashboard_notification` | Text | Optional dashboard notification text. Empty, `unknown` and `unavailable` hide the notification. | Only when `menu.notify.enabled` is used. |
| `input_boolean.dashboard_holiday` | Toggle | Optional day-symbol indicator for holidays. | Only when the day symbol should react to holidays. |
| `input_boolean.dashboard_birthday` | Toggle | Optional day-symbol indicator for birthdays. | Only when the day symbol should react to birthdays. |
| `input_boolean.dashboard_christmas` | Toggle | Optional day-symbol indicator for Advent/Christmas. | Only when the day symbol should react to Advent/Christmas. |

Status values do not require special helpers. They can use any readable Home Assistant entity, for example sensors, binary sensors or template sensors.

![Dashboard Layout Card V2 notification and status values](/images/dashboard-layout-card-v2/notify-and-status.png)

At viewport widths up to and including 600 pixels, menu buttons show icons only. Icon-only mode can also be enabled manually, for example for kiosk tablets or wall displays. In this mode, clock, date and status values are hidden; notifications remain available through a compact popup button.

Menu entries can have submenus. The submenu is rendered as its own icon column next to the main menu and only shows the subpages of the currently selected main menu entry. The first submenu button can act as the start page for the main menu entry or be disabled so the main entry jumps directly to the first subpage. Submenu buttons currently inherit the main button style, and the submenu background can be configured separately.

Main menu, submenu and home entries can optionally define their own colors. Supported overrides are icon color, active icon color, icon background, active icon background, button color and active button color per entry. Empty fields continue to use the global menu style.

The matching YAML fields are `icon_color`, `icon_active_color`, `icon_background_color`, `icon_background_active_color`, `tab_color` and `active_tab_color`. A reset button can clear only these color overrides of the selected entry when needed; the page, path, icon, submenu and global colors remain unchanged.

Menu, card, notification and status borders have separate opacity sliders. Divider entries can also use their own opacity for the divider color and 3D effect. This makes it easier to tune visible frames, transparent glass styling and compact kiosk layouts.

The editor window opens wider by default at 80 percent of the viewport width and can be expanded to 95 percent by double-clicking the top bar. The global style tab is named **Styles Global**. It also includes the active icon-field color, icon size up to 64 pixels, with saved px values from `menu.style.icon_size` and older `menu.icon_size` locations loaded from the current Lovelace view back into the slider and number field, normalized on save and applied with forced visual scaling and opacity controls for the global menu background color and the separate submenu background. A stored value such as `icon_size: 48px` appears as `48` in the editor and is saved back as a px value. The separate **Farben** tab stores up to 20 color favorites that can then be selected in all color fields, including divider color and divider 3D effect; the **Farben speichern** button writes only these favorites without applying other open editor changes.

The Backup tab can export the current dashboard state as a YAML file to the local computer. The export does not modify Home Assistant and is useful as a backup before larger tests or design changes. The tab is also prepared for a later YAML import action.


### YAML language override for screenshots

For documentation screenshots or language testing, the displayed UI language can be forced directly in YAML. This option is intentionally not shown in the editor.

```yaml
debug:
  language: de # de, en or fr
```

Without `debug.language`, the card uses the Home Assistant or browser language automatically and falls back to English.

### Current Editor Options

| Tab | Options |
| --- | --- |
| Menü | Menu position (`left`, `none`, `right`), menu title and global icon-only mode for kiosk/tablet layouts. |
| Hauptseite | Show or hide the home entry, home title, path, icon, per-home icon/button colors, maximum Sections V2 columns, dense section placement, extra top spacing and theme inheritance from the home view. |
| Anzeige | Clock mode (`none`, `digital`, `analog`), analog hour marks, minute marks and seconds hand, date visibility, weekday mode (`none`, `short`, `long`), weekend color, clock/ring color, analog mark and hand colors, holiday/birthday/christmas helper entities and day-symbol size. |
| Seiten | Main menu pages, spacers and dividers; title, path, icon, layout type, maximum columns, per-entry colors, reset to global colors, first submenu button behavior, divider color, divider 3D frame color, divider opacity and divider height. |
| Submenü | Subpages for the selected main page with title, path, icon, layout type, maximum columns, per-entry colors and reset to global colors. The submenu tab appears when the selected main entry has subpages. |
| Meldungen | Optional notification popup based on a text helper, notification border color and opacity, optional status values with up to four entity rows, labels, units, status border color and status border opacity. |
| Styles Global | Clock size, date size, weekday wrap size, tab/text/hover colors, menu border color and opacity, tab 3D frame color, card/content border color and opacity, card 3D frame color, shared 3D offset, icon color, active icon color, icon field color, active icon field color, icon shape, icon size, menu background mode (`none`, `color`, `image`), menu background color and opacity, menu background image, submenu background color and submenu background opacity. |
| Farben | Up to 20 reusable color favorites. The dedicated **Farben speichern** button saves only the favorites. |
| Backup | Export the current dashboard editor state as YAML to the local computer. |
| Erweitert | Home Assistant chrome settings, optional always-visible admin controls, visible user list and advanced JSON editing for page data. |

## Themes

| Project | Status | Note |
| --- | --- | --- |
| [Frosted Glass Theme](/sammlung/frosted-glass-theme/) | reviewed | Modern Home Assistant theme with glass styling, HACS installation, card-mod or UIX requirement and Lite variants. |
| [NeoMorphix UIX](/sammlung/neomorphix-uix/) | reviewed | Neumorphic Home Assistant theme with light, dark, Claude and inset variants; UIX variants are proposed as a PR. |
