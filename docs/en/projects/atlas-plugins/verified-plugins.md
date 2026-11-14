# Verified Plugins

**HA 2026.11, 2026-11-05:** Hub and interfaces of all six plugins checked on the [ARM test system (Pi 5)](/en/collection/test-systems#testsystem-arm). Card Editor connects to HA; File Studio loads paths, Automation Exporter reads after backup, Icon Library loads MDI and Icon Studio its SVG interface. **The user confirms ATLAS Terminal works.** This extends the basic review without changing experimental product status or validating every feature.

[Scope, results and remaining findings](/en/collection/ha-2026-11-compatibility).

This page collects ATLAS plugins that are either visibly recommended or tracked as new external submissions. Verified plugins have at least been checked for manifest quality, launch URL, icon, obvious secret leaks and unsafe path grants.

::: warning Note
ATLAS is still in development. Even verified plugins do not replace your own review before production use.
:::

## Verified Plugins

| Icon | Name | Status | Link |
| --- | --- | --- | --- |
| 🧩 | ATLAS Home Assistant Card Editor | verified | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/homeassistant-card-editor">Details</a> |
| 🗂️ | ATLAS File Studio | verified | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/file-studio">Details</a> |
| 🖥️ | ATLAS Terminal | experimental | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/terminal">Details</a> |
| ⚙️ | ATLAS Automation Exporter / Editor | experimental | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/automation-extractor">Details</a> |
| 🎨 | ATLAS Icon Studio | experimental | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/icon-studio">Details</a> |
| 🔎 | ATLAS Icon Library | experimental | <a class="atlas-plugin-table-button" href="/en/projects/atlas-plugins/icon-library">Details</a> |

## New/Unreviewed Plugins

| Icon | Name | Status | Link |
| --- | --- | --- | --- |
| - | No external submissions yet | unreviewed | - |

## Status Values

| Status | Meaning |
| --- | --- |
| verified | The plugin has been reviewed at a basic level and matches the current ATLAS state. |
| experimental | The plugin is usable, but behavior or contracts are still changing visibly. |
| unreviewed | The plugin has been submitted or found, but not reviewed by ATLAS yet. |
| outdated | The plugin no longer matches the current ATLAS state. |
| rejected | The plugin is not recommended for technical, legal or security reasons. |
