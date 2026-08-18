# C# Projects

This page collects the published C#/.NET tools by UGSo Software.

## HADash

**HADash - Home Assistant Dashboard Toolkit**

HADash is a portable Windows application for reading, backing up and exporting Home Assistant dashboards and individual views.

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
- [Download the current v0.3.4 release](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.4)

## More Project Areas

- [Open MQTT Projects](/en/projects-mqtt/)
- [Open Misc Projects](/en/projects-diverse/)
- [Open ATLAS](/en/projects/atlas/)
