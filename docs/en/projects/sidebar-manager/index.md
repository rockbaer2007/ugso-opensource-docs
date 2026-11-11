---
title: Sidebar Manager
description: Folders, colors, opacity and links in the Home Assistant sidebar. Version 0.1.11, DE/EN/FR.
---
# Sidebar Manager

## New in 0.1.11: Aligned sidebar icons

Group and custom-link icons now measure 24 × 24 px. In the collapsed sidebar, they share the same horizontal center as native Home Assistant icons.

Verified on .177 with Home Assistant 2026.11.0 on 11 November 2026. Group icons align with the Overview icon in both sidebar layouts. The Logs, Automations, and States link icons are centered in the collapsed sidebar. The user test also passed.

## New in 0.1.10: Home Assistant shortcuts

::: warning Marketplace requires Home Assistant 2026.11.0
**The Marketplace shortcut is offered only on HA 2026.11.0 or newer.** It is hidden on older or unknown versions. The package minimum remains **HA 2026.10.3**; other presets are independent of this requirement. The link does not install Marketplace or grant additional permissions.
:::

Open **Edit sidebar → Manage groups and links → Home Assistant shortcuts**, choose a folder and click **Add**. The section uses two columns on desktop and one on narrow screens.

| Shortcut | Default icon | Target |
| --- | --- | --- |
| Logs | `mdi:history` | `/config/logs` |
| Automations | `mdi:robot` | `/config/automation/dashboard` |
| Entities | `mdi:shape` | `/config/entities` |
| **Marketplace · HA 2026.11.0+** | `mdi:store` | `/marketplace/browse?group=status` |
| Labels | `mdi:label` | `/config/labels` |
| States | `mdi:list-status` | `/config/tools/state` |
| Actions | `mdi:run` | `/config/tools/action` |

**Icons are editable defaults for new links.** Existing links are reused by URL and retain their custom names and icons, including legacy States URLs at `/developer-tools/state`. Existing groups, colors, order and VIS/dashboard settings are not migrated or reset. **Save** in the Manager applies link settings; **Cancel** discards the open draft.

::: tip Verified on .177 with HA 2026.11.0 · 8 November 2026
Following a fresh full backup, the desktop two-column layout, four new destinations, default icons, folder assignment, Cancel, Save and full reload passed. Temporary test links removed; user preferences, colors, groups, test dashboard and resources exactly match the PC backup. **73 automated tests** pass, including Marketplace version boundaries. Mobile layout and older HA versions were not separately live-tested.
:::

![Two-column Home Assistant shortcuts in Sidebar Manager 0.1.10, tested on .177; German test interface](/images/sidebar-manager/shortcuts-0110-177.png)

::: info HA 2026.11: color preview fixed
Version **0.1.9** fixes missing text/icon colors in the native edit dialog, including group colors. Verified on .177 (port 80), Core 2026.11.0 / frontend 20261028.4: colors, opacity, Cancel, Save, theme reset and a full reload. All 72 automated tests pass. Disposable group/link removed; the exported layout again matches the pre-test backup. Existing settings and “Test für APP” are preserved.
:::

[Scope, results and remaining findings](/en/collection/ha-2026-11-compatibility).

<img src="/images/packages/projects-sidebar-manager.svg" width="80" height="80" alt="Sidebar Manager" />


**0.1.11 · Home Assistant ≥ 2026.10.3 · DE / EN / FR · MIT**

Organize Home Assistant's sidebar with folders, colors, opacity and custom links, directly from **Edit sidebar**. Move main entries and folders with the native drag handles. No HA core files are replaced.


[GitHub](https://github.com/rockbaer2007/ha-sidebar-manager) · [Release 0.1.11](https://github.com/rockbaer2007/ha-sidebar-manager/releases/tag/v0.1.11) · [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=ha-sidebar-manager&category=plugin)

## New in 0.1.8: links in the sidebar editor

::: info Verification status, 2 November 2026
**0.1.8: successful functional verification confirmed by the user on 2 November 2026.** Links, colors, moving entries and the Link/Ext. link labels work. Syntax checks, the build and **70 automated tests** also pass. Existing screenshots show earlier verification stages. Codex did not perform an additional independent HA runtime test for this release; the user’s test host and HA version were not separately specified.
:::

Custom internal and external links now also appear in **Edit sidebar**. Links without a saved position initially appear at the end; existing ordering is respected. Hidden links remain available for editing.

- **Color field:** the same color/opacity picker used for HA entries. **Theme color** removes the override. Saved link colors apply immediately when sidebar rows are created.
- **Link type:** the settings button displays **Link** for internal targets and **Ext. link** for external HTTP(S) targets, instead of the folder name. Clicking opens that link’s settings. Its folder assignment is preserved and also shown in the tooltip.
- **Drag handle:** reorder links alongside other entries, including within their assigned folder. Dragging alone does not change folder membership; choose the folder in the link settings. Keyboard sorting remains available.
- **Eye:** hide or show a link without deleting it or its settings.
- **Save/Cancel:** apply or discard color, visibility and order changes in the HA editing dialog. General link settings are still saved in the Manager.

Link ordering and visibility remain in `ugso_sidebar_manager_v1`; colors stay in the existing `ugso_sidebar_colors_v1` record. Custom link IDs never enter HA’s native saved panel order. Existing settings, opening modes and missing panels are preserved.

Local checks exercise the built JavaScript package with simulated HA storage, DE/EN/FR labels, color selection, Save/Cancel, sorting, preserved folder membership and recovery after a failed save. The user confirmed successful functional verification on 2 November 2026; this acceptance is recorded separately from the automated tests.

## Install with HACS / Marketplace

This is a frontend plugin, not a Supervisor app or a dashboard card. Add `https://github.com/rockbaer2007/ha-sidebar-manager` as a custom repository in HACS, category **Dashboard** (`plugin` internally), and download Sidebar Manager. A public repository is not automatically included in the default catalog. The package uses a HACS-compatible structure for Marketplace.

::: tip Marketplace installation confirmed
On **5 November 2026**, the user confirmed successful installation through **Marketplace**. This supplements the documented Sidebar Manager 0.1.9 checks. The exact Marketplace version was not separately specified; this does not certify every version.
:::

[Open in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=ha-sidebar-manager&category=plugin)

Back up HA first. Merge this into the **existing** `frontend:` section of `configuration.yaml`, keeping themes and other modules:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/ha-sidebar-manager/ha-sidebar-manager.js
```

Remove or disable the old Sidebar Colors and Sidebar Organizer module entries; load only Sidebar Manager. Check the configuration, restart HA and reload the browser. A dashboard resource alone does not load the extension reliably when another HA page is opened first.

## Manual installation

Download `ha-sidebar-manager.js` from Releases and copy it to `/config/www/ha-sidebar-manager/ha-sidebar-manager.js`. Use this module URL instead:

```yaml
frontend:
  extra_module_url:
    - /local/ha-sidebar-manager/ha-sidebar-manager.js
```

Do not load the manual and HACS copies together. The ZIP includes the same bundle, configuration examples, license and DE/EN/FR instructions. Existing versioned local installations such as `/local/ugso-sidebar-manager/0.1.7/ha-sidebar-manager.js` can keep that path if the matching file is present. For updates, retain your chosen path and reload the browser.

## Websites inside HA

New-tab links work without additional configuration. For **Display on the right (iframe)**, also merge this entry into `configuration.yaml` or its existing `panel_custom` list:

```yaml
panel_custom:
  - name: ugso-sidebar-web
    url_path: ugso-sidebar-web
    module_url: /hacsfiles/ha-sidebar-manager/ha-sidebar-manager.js
    embed_iframe: false
    require_admin: false
```

For manual installation, change `module_url` to `/local/ha-sidebar-manager/ha-sidebar-manager.js`. It must match your frontend module URL. Validate and restart HA. No `sidebar_title` is set: this registers a hidden host panel, not another menu entry. See `panel-custom.example.yaml` and `panel-custom.manual.example.yaml` in the release ZIP.

The target website must allow embedding. CSP/X-Frame-Options, HTTPS-to-HTTP restrictions or the website's own login can prevent display. A new-tab alternative remains available. No HA token is passed to the website. Registering the host panel does not change permissions on HA's destination pages.

## Use

Hold the sidebar heading to open **Edit sidebar**. Color fields, eye buttons and the native drag handles remain available. **Manage groups and links** opens the Manager. The interface follows your HA language: German, English or French, with English fallback.

- Choose entry colors and opacity; **Theme color** clears an override. The checkerboard indicates transparency.
- Create folders with names, MDI icons, colors and initial expanded/collapsed state. Assign existing main-menu entries or custom links to folders; choose **Main menu** to move them back.
- Drag folders between main entries in the native editor. Group membership is preserved: the folder and its children move together. Keyboard sorting is also available (Alt+Up/Down on a row).
- Bottom-pinned folders also appear at the bottom in the editor. Moving one before a normal menu block releases its bottom pin; Cancel preserves the original pin and position.
- Set the folder separator to **0–4 px**. Zero means off. It appears only while the group is expanded, at the end of the block, in the icon's color/opacity, with 1 px spacing above and below.
- Add Logs, Automations, Entities, Labels, States and Actions with a selectable folder; Marketplace is additionally available from HA 2026.11.0. Matching existing links are reused; names and MDI icons remain editable.
- Own internal links are pale yellow in settings; external HTTP(S) links are light blue. Choose a new tab or iframe for external links. Older links retain their previous same-window behavior until edited. These settings highlights do not replace custom sidebar colors.
- The Manager's **Save** commits its layout. Color/native order edits in the underlying HA dialog require that dialog's **Save**. Cancel discards the respective open draft.

Settings, profile and notifications remain native. Hiding an entry or changing its group does not grant or restrict access.

## Screenshots and verification

Color picker and group settings:

![Color picker](/images/sidebar-manager/farbwaehler-177.png)

![Folder settings](/images/sidebar-manager/web-link-016-177.png)

Actual 0.1.7 folder placement and collapsed separator on the authorized .177 test system:

![Saved folder position](/images/sidebar-manager/ordnerposition-017-177.png)

![Collapsed folder without separator](/images/sidebar-manager/trennlinie-eingeklappt-017-177.png)

![Website on the right inside HA](/images/sidebar-manager/web-panel-016-177.png)

0.1.7 was verified on HA **2026.10.4**, port 80: Save/Cancel, moving a bottom-pinned test folder, browser reload, folder membership and expanded-only separators. Earlier tests cover colors, opacity, custom links, iframe/new-tab opening and layout export/import. Existing settings and the protected test dashboard were preserved; temporary test objects were removed. **60 automated tests pass.** The color/link screenshots also illustrate unchanged functionality from 0.1.6. [Detailed test history](https://github.com/rockbaer2007/ha-sidebar-manager/blob/main/docs/TESTING.md).

HA 2026.10.3 is the intended minimum, not a separate live-tested installation. No live compatibility claim is made for every external website or Marketplace version.

## Preserve settings and switch safely

1. Create a full HA backup. Export existing Organizer settings and Manager/color backups where available.
2. Disable the previous sidebar module entries without deleting their files or user settings. Install only one Sidebar Manager copy.
3. Existing Sidebar Colors data stays under `ugso_sidebar_colors_v1`. Manager layouts stay under `ugso_sidebar_manager_v1`, per authenticated HA user and synchronized between clients.
4. Organizer YAML/layout import is **not implemented**. Keep its export and recreate the desired folders/links manually. No automatic Organizer migration is claimed.

Missing panels remain stored. Read failures and unsupported schemas never write defaults. Before writes, the previous layout is saved in local browser storage; blocked storage prevents saving. Concurrent edits are checked before writes; uncertain confirmations are read back rather than blindly retried. This is not an atomic server-side compare-and-swap.

Manager JSON export/import covers folders, links, labels, icons, visibility, pinning, order and separator settings, not access tokens or native HA preferences. Entry colors keep their separate backup. Reset affects the open Manager draft until saved. To roll back, restore the previous module entry, restart HA and reload the browser; leave stored user settings intact.

## Development and scope

Node 22 or newer: `npm ci`, `npm run check`, `npm run build`, `npm test`. Tagged releases build the self-contained JS and installable ZIP automatically.

Native sidebar internals can change with HA frontend updates. No per-device layouts, arbitrary CSS/templates, automatic Organizer migration or configurable header/width are included. Pinned items remain within the scrollable main navigation.

Original UGSo implementation based on Sidebar Colors. [Sidebar Organizer by Viet Ngoc](https://github.com/ngocjohn/sidebar-organizer) is a behavioral reference; no Organizer source is embedded. MIT license: see [LICENSE](https://github.com/rockbaer2007/ha-sidebar-manager/blob/main/LICENSE).
