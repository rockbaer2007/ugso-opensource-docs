# Open Source Projects

This page collects the published projects by UGSo Software.

## HADash

**HADash - Home Assistant Dashboard Toolkit**

HADash is a portable Windows application for reading, backing up and exporting
Home Assistant dashboards and individual views.

- [Open the HADash documentation](./hadash/)
- [Open HADash on GitHub](https://github.com/rockbaer2007/HADash)

## Home Assistant Automation Exporter

**Home Assistant Automation Exporter**

The Home Assistant Automation Exporter is a portable Windows application for splitting an `automations.yaml` file into separate YAML files. Its compact UI lists all automations with checkboxes, provides a dedicated settings dialog for export folder and language, and exports only the selected automations.

![Home Assistant Automation Exporter](/images/ha-automation-exporter/automations-exporter.png)

Use **Details** or double-click an automation to open a detail window with two tabs:

- **Entities** lists detected Home Assistant entities with source, line number and context. Entities found inside templates are detected heuristically and marked as template matches.
- **YAML** shows the full code of the selected automation and includes a copy button.

The export folder and language are managed in the settings dialog, keeping the main view compact. The UI supports **German**, **English**, **French**, **Spanish**, **Polish** and **Russian**. The language can be detected automatically through the **System** setting based on the Windows UI language or selected manually; unsupported system languages fall back to English.

For examples from GitHub, forums and other open source projects, the exporter handles different Home Assistant YAML spellings. Older and newer automation definitions such as `trigger`/`triggers`, `condition`/`conditions`, `action`/`actions`, `- trigger: state` and `- action: switch.turn_on` are normalized automatically during export into an import-friendly single automation format.

![Automation details with entities](/images/ha-automation-exporter/details-entities.png)

![Automation details with YAML code](/images/ha-automation-exporter/details-yaml.png)

- [Open Automation Exporter on GitHub](https://github.com/rockbaer2007/ha-automation-exporter)
- [Download the current v0.3.1 release](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.1)

## Ultimate Timer

**Ultimate Timer V3.2.4 FINAL CLEAN**

A powerful hybrid timer blueprint for Home Assistant with reliable STOP logic,
persistent DONE status and optional MQTT support.

- [Open the Ultimate Timer documentation](./ultimate-timer/)
- [Open the repository on GitHub](https://github.com/rockbaer2007/ha-ultimate-timer-blueprint)

## ATLAS

**ATLAS - Modular Application Framework**

ATLAS is a modular TypeScript framework for reusable applications, plugins and
Home-Assistant-oriented tools.

The project is currently in active development. The focus is on the Runtime
Foundation, events, services and dependency injection.

- [Open the ATLAS project page](./atlas/)
- [View the architecture](./atlas/overview)
- [View the development status](./atlas/development-status)

## More Projects

Additional documentation for ESPHome, Lovelace components and the planned
Lovelace UV Card will follow.
