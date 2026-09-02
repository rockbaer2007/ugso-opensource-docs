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

- read `/config/automations.yaml` through the approved File Studio path
- analyze external `.yaml` and `.yml` uploads
- show id, alias, description, triggers, conditions and actions
- surface related entities, scripts, scenes, helpers and notification targets
- configure an export folder target
- export selected automations as individual YAML files
- create timestamped export filenames: `name_dd_mm_yy-hh_mm_ss.yaml`
- show an overview of exported automations
- prepare editing exported files through File Studio
- run later refactoring steps only with backup, validation, diff preview and a recovery path

## Safety Line

The first stage stays intentionally conservative. The plugin reads system YAML
or uploaded YAML files, analyzes them and prepares downloads. Writing changes
back into Home Assistant files belongs to a later stage once backup, YAML
validation, diff preview and restore paths are in place.

## Positioning

ATLAS Automation Exporter / Editor complements File Studio: File Studio is the
safe file surface, while Automation Exporter / Editor is the domain-specific
analysis and export surface for automations.
