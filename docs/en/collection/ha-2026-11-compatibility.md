---
title: HA 2026.11 compatibility review
description: Confirmed checks, local tests and remaining findings for UGSo extensions on Home Assistant 2026.11.
---
# HA 2026.11 compatibility review

**As of 2026-11-05 · Core 2026.11.0 · Frontend 20261028.4 · ARM test system (Pi 5) (port 80).**

This overview distinguishes live checks, user confirmations and local tests. It does not certify every feature or hardware variant. The initial review changed no software versions; the subsequent sidebar correction is documented separately below.

## ATLAS and plugins

| Package | Result and scope |
| --- | --- |
| ATLAS App **0.1.334**, Card Editor **0.2.0-alpha.115** | Live: Ingress, hub with six active plugins, editor, HA connection with 35 live entities and existing project list loaded. All 431 HA-package tests, 74 app/frontend tests and TypeScript checks across eleven workspace packages passed. |
| File Studio **0.1.52** | Live: file tree, editor interface and approved paths load. Four package tests and catalog validation passed. Existing files were not edited. |
| Automation Exporter / Editor **0.1.28** | Live: system automation file read after its own backup; no existing automations present. Nine local tests passed. No writes to HA system files. |
| Terminal **0.1.10** | Interface checked live. **The user confirmed on 2026-11-05: ATLAS Terminal works.** This supplements the initial interface-only check; it does not separately validate every SSH target or Oh My Posh theme. |
| Icon Library **0.1.9** | Live: 7,447 MDI icons (7.4.47) load and search responds. Ten tests and package validation passed. |
| Icon Studio **0.1.17** | Live: collection, SVG preview and drawing interface load. Fifteen tests and package validation passed; existing collection unchanged. |

The ATLAS app also passed read-only validation of 523 package files. The isolated Python contract test for the HA integration could not run locally because Home Assistant was not importable; Docker was not running. A complete new project write/restore/HACS round trip was outside this review.

## Other HA extensions

| Package | Result and limitation |
| --- | --- |
| [Dashboard Layout Card V2 **0.1.181**](/en/collection/dashboard-layout-card-v2/) | Separate live test passed: add/edit cards in the second section, floating Add button, header/footer and full reload. |
| [Automation Status Card **0.1.3**](/en/projects/automation-status-card/) | Live checks passed: rendering, on/off with state confirmation, running execution, trace request, normal completion, checkboxes, select/deselect all and reload. Bubble/Mushroom single-automation examples rendered. Twenty-one local tests passed. Failures and runtime warnings were not deliberately triggered again on 2026.11. |
| [Sidebar Manager **0.1.9**](/en/projects/sidebar-manager/) | Updated on the ARM test system (Pi 5) from 0.1.7 to **0.1.9**. Live checks passed: entry/group text and icon colors in the native edit dialog, opacity, Cancel, Save, theme reset and a full reload. All 72 local tests passed. Disposable test objects removed; exported layout matches the original backup. |
| [Sidebar Colors **0.1.1**](/en/projects/sidebar-colors/) | **0.1.1** fixes the same row selector. All 27 local tests passed, including DOM regressions for legacy/new HA elements and Save/Cancel. Not additionally installed alongside Manager on the ARM test system (Pi 5). |
| [Dashboard User Manager **0.1.11**](/en/projects/dashboard-user-manager/) | Live: 19 views and four users loaded; no changes saved. **Open: additional loading warning for the old `lovelace` dashboard.** Root cause not fully established. Thirty-three Python and nineteen Node app tests passed. |
| [HA Grafik Visual Studio **0.1.296**](/en/projects/grafik-visual-studio/) | 109 Python and 388 Node tests passed. No dedicated live test on the ARM test system (Pi 5), where the app is not installed. |
| [Blocks for HA **0.1.66**](/en/projects/blocks-for-ha/) | Ten Python and 172 Node tests passed; seven optional tests skipped. No live test on the ARM test system (Pi 5). |
| [MQTT Client **0.1.17**](/en/projects/mqtt-client/) | Thirty-six Python tests passed; two tests requiring a separate MQTT broker skipped. No new live test against an external broker. |
| [CallMeBot Whatsapp **0.1.6**](/en/projects/callmebot/) / [Signal **0.1.2**](/en/projects/callmebot-signal/) | 17/18 Python tests and three request-ID tests each passed. No messages sent to actual recipients. |
| Tabbed Card V2 / Editor **0.1.7**, HA integration **0.1.3** | JavaScript/Python syntax checked; no live qualification of the uninstalled extension. |
| [FRITZ!Box to MQTT **0.1.41**](/en/projects/fritzbox-to-mqtt/) / [Heating Oil to MQTT **0.1.15**](/en/projects/heizoel-to-mqtt/) | Python syntax checked; devices, data source and MQTT Discovery not tested live. |
| Materialdesign widget package / [Ultimate Timer Blueprint](/en/projects/ultimate-timer/) | Included in the inventory; no new complete live functional test. |

## Known findings and next checks

**Fixed in Sidebar Manager 0.1.9 and Sidebar Colors 0.1.1:** color application now supports legacy `ha-md-list-item` and new `ha-list-item-button`. Manager live-tested on the ARM test system (Pi 5): entry/group text and icon colors, opacity, Cancel, Save, theme reset and a full reload. All 72 Manager and 27 Colors tests pass. Colors was tested separately locally, not loaded alongside Manager on the ARM test system (Pi 5). Stored color settings need no migration.

The User Manager's `lovelace` loading warning requires a separate investigation. Failed reads must still never count as empty dashboards. The warning has not yet been conclusively attributed to a 2026.11 regression.

Uninstalled apps and untested write, restore, device or broker workflows need additional live checks. Third-party projects such as UIX, Calendar Card Pro, Zendure and Frosted Glass were not fully audited here.

## Backup and cleanup

A fresh full backup was created first. The owned test automation performed only a delay, with no automatic triggers or device actions. The test automation and dashboard were removed; existing settings, projects, plugins and “Test für APP” were preserved. Following explicit approval to delete the oldest backup, exactly three full backups remain; app-update and PC backups were retained.

## References

- [Official HA 2026.11 changes](https://www.home-assistant.io/blog/2026/11/04/release-202611/)
- [Frontend components in 2026.11](https://contributors.home-assistant.io/blog/2026/10/28/frontend-component-updates-2026.11/)
- [Config-entry returns: booleans remain supported for custom integrations](https://contributors.home-assistant.io/blog/2026/10/23/config-entry-methods-return-none/)
- [Original display editor 20261028.4](https://github.com/home-assistant/frontend/blob/20261028.4/src/components/ha-items-display-editor.ts)
