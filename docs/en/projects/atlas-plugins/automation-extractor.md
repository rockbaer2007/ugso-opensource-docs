# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor is the next independent ATLAS plugin. The
idea comes from the existing Windows tool for splitting `automations.yaml`, but
moves directly into the ATLAS plugin architecture.

## Goal

The plugin should analyze Home Assistant automations safely, export selected
entries and prepare further editing through File Studio.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Install page: `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- current installable plugin version: `0.1.16`

ATLAS Administration accepts the GitHub URL directly. During preview, ATLAS
converts it to the matching `repository.json` address automatically.

- read `/config/automations.yaml` through the approved File Studio path
- create a safety backup before reading the real `/config/automations.yaml`,
  stored as `/config/atlas_backups/automations/<date-time>/automations.yaml`
- analyze external `.yaml` and `.yml` uploads
- show id, alias, description, triggers, conditions and actions
- detect service calls from classic `service:` and modern
  `action: domain.service` syntax
- show analysis hints for missing or duplicate ids/aliases, missing triggers or
  actions and disabled automations
- filter to automations with hints only
- show detail YAML with File Studio-like highlighting
- limit the automation list to roughly 15 visible entries and keep it
  internally scrollable
- surface related entities, scripts, scenes, helpers and notification targets
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

## Positioning

ATLAS Automation Exporter / Editor complements File Studio: File Studio is the
safe file surface, while Automation Exporter / Editor is the domain-specific
analysis and export surface for automations.
