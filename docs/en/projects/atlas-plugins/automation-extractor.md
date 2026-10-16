# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor is an independently maintained external ATLAS plugin. The
idea comes from the existing Windows tool for splitting `automations.yaml`, but
moves directly into the ATLAS plugin architecture.

## Goal

The plugin analyzes Home Assistant automations safely, exports selected
entries and prepares further editing through File Studio.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Install page: `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- current installable plugin version: `0.1.28`
- User interface in German, English and French; the saved ATLAS language is applied when the plugin opens.

ATLAS Administration accepts the GitHub URL directly. During preview, ATLAS
converts it to the matching `repository.json` address automatically.

Since 0.1.28, analysis counts actual YAML trigger, condition and action entries.
Section headers and nested steps do not add root entries. Modern and classic
syntax are supported. Settings and source automations are unchanged; reading
the system file still creates a safety backup before analysis.

- read `/config/automations.yaml` through the approved File Studio path
- create a safety backup before analyzing the loaded `/config/automations.yaml`,
  stored as `/config/atlas_backups/automations/<date-time>/automations.yaml`
- analyze external `.yaml` and `.yml` uploads
- show id, alias, description, triggers, conditions and actions
- detect service calls from classic `service:` and modern
  `action: domain.service` syntax
- keep single automations with root-level trigger or action fragments as one
  entry instead of creating false duplicate conflicts
- keep time triggers as quoted `HH:MM:SS` values during export and repair
  numeric second values such as `25200` back to `'07:00:00'`
- show analysis hints for missing or duplicate ids/aliases, missing triggers or
  actions and disabled automations
- pre-mark duplicate ids and aliases directly in the automation list as
  conflicts
- show duplicate ids and aliases as conflicts separate from general hints
- filter to automations with hints only
- show detail YAML with File Studio-like highlighting
- limit the automation list to roughly 15 visible entries and keep it
  internally scrollable
- surface related entities, scripts, scenes, helpers and notification targets
- group and filter the automation list by domain, area or device
- configure an export folder target
- export selected automations into one timestamped run folder
- create two files with the same automation filename: `export-version` with
  `id` and `bereinigte-import-version` without `id` for the Home Assistant YAML
  editor
- show an overview of exported automations
- prepare editing exported files through File Studio

## Safety Line

The plugin does not write back into Home Assistant system files. It reads system
YAML or uploaded YAML files, creates a safety backup when opening the real
`automations.yaml`, analyzes the automations and exports separate YAML files.
Manual restore and further editing should continue through File Studio and Home
Assistant's own YAML tools.

## Safe plugin recovery

In **Administration → Plugin Manager → Automation Exporter / Editor → Restore**,
select an existing backup. Review version, direction and compatibility, then use
the action that backs up the current plugin and applies the selected version.
Cancel leaves the installation unchanged. A concurrent change to plugin or
management state requires a fresh preview.

This restores the **plugin package**. It does not roll source automations,
exports, editor projects, trash or history back to earlier data. It neither
imports into Home Assistant automatically nor writes back to `automations.yaml`.

::: info Isolated qualification on 2026-10-16
Actual packages **0.1.27 → 0.1.28 → 0.1.27 → 0.1.28** passed on ATLAS 0.1.312,
including restart, UI preview, cancellation and recovery. A stale preview was
rejected after a real management change. Repository bundles and a complete
isolated fixture archive were retained before changes. Source YAML, existing
exports, project, another plugin, trash and history remained exact. DE/EN/FR
analysis, byte-identical safety backups, export/import pairs with/without ID and
opening exports in File Studio passed. HA version metadata came from a local
test endpoint; this does not qualify real HA authentication, GitHub updates or
data-format migration. **Pi 5 and Proxmox were unchanged during this isolated check.**
:::

::: info Subsequent Pi 5 and Proxmox qualification on 2026-10-16
After fresh local HA backups and additional PC copies, both hosts passed
**installed 0.1.28 → 0.1.27 → original 0.1.28**. The actual older package was
applied through the backend compatibility preview; cancellation and recovery
from the new backup used Administration. Both retain ATLAS 0.1.312 and HA 2026.10.1.

All nine original plugin assets were restored exactly. Checked source automations,
existing exports and automation backups, settings, server projects, other plugins,
trash and history were preserved. Analysis of an uploaded synthetic YAML fixture
was identical before and after recovery. No user automation was exported, executed
or written back to HA; no HA/App restart was needed. This does not qualify a
complete HA restore, data-format migration or a new GitHub release.
:::

Reload Administration and the plugin page after recovery. During testing, the
open Administration briefly reported unsaved shared changes although server
recovery was correct. Reloading showed the shared server state again. Do not
adopt an old local state solely because of that message.

Language and appearance are stored locally. Loaded analysis, selection, filters,
the entered export folder and export overview belong to the current session.
After reloading, load the source again and select the target folder if needed.
Previously saved export files remain available in File Studio.

## Positioning

ATLAS Automation Exporter / Editor complements File Studio: File Studio is the
safe file surface, while Automation Exporter / Editor is the domain-specific
analysis and export surface for automations.
