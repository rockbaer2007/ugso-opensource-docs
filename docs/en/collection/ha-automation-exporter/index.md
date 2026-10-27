---
title: Home Assistant Automation Exporter
description: English documentation for the Windows tool for exporting individual Home Assistant automations from automations.yaml.
---
<a id="current-focus"></a>

# Home Assistant Automation Exporter {#home-assistant-automation-exporter}

The **Home Assistant Automation Exporter** is a portable Windows tool that can be used to read a Home Assistant file `automations.yaml` and export it to individual YAML files.

This is helpful if automations are to be saved separately, passed on, documented or later imported back into Home Assistant individually.

![Home Assistant Automation Exporter](/images/ha-automation-exporter/automations-exporter.png)

## Project {#projekt}

| Entry | Link |
| --- | --- |
| GitHub repository | [rockbaer2007/ha-automation-exporter](https://github.com/rockbaer2007/ha-automation-exporter) |
| Current Release | [Download v0.3.4](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.4) |
| Platform | Windows |
| base | C# / .NET 9 |

## Features {#funktionen}

- Opens a Windows interface without a command line.
- Shows the program version in the window title.
- Reads a Home Assistant `automations.yaml`.
- Searches automations by alias, ID, filename or YAML content.
- Shows all automations in a table with selection fields.
- Opens detailed views with recognized entities and full YAML code.
- Exports selected automations as individual `.yaml` files.
- Opens the selected export folder directly in Windows Explorer.
- Stores settings portably next to the EXE in `HaAutomationExporter.settings.json`.

## Requirements {#voraussetzungen}

For use as a finished release:

- Windows
- Download the current release file from GitHub

For development or starting from source code:

- Windows
- .NET 9 SDK
- Repository cloned locally

```powershell
dotnet run --project .\HaAutomationExporter.csproj
```

## Service {#bedienung}

1. Start the program.
2. Select the Home Assistant file `automations.yaml`.
3. Optionally change the export folder in the settings.
4. Select automations in the table.
5. Check individual automations via `Details`.
6. Export selected automations.
7. Import the generated YAML files into Home Assistant if necessary.

## Detailed view {#detailansicht}

In the detailed view, an automation can be checked before exporting. This is particularly useful when many automations have similar names or when you want to control templates and entities.

![Automation Details: Entities](/images/ha-automation-exporter/details-entities.png)

The **Entities** tab shows recognized Home Assistant entities with source, line number and context. Template hits are recognized heuristically.

![Automation Details: YAML](/images/ha-automation-exporter/details-yaml.png)

The **YAML** tab shows the complete automation code and contains a copy function.

## Export for Home Assistant {#export-fur-home-assistant}

The exported files are prepared to make them easier to use individually in Home Assistant.

The exporter removes the leading top line `id:` and normalizes different YAML notations:

| exit | Export |
| --- | --- |
| `triggers` | `trigger` |
| `conditions` | `condition` |
| `actions` | `action` |
| `- trigger: ...` | `- platform: ...` |
| Service actions | `- service: domain.service` |

This allows automations from different Home Assistant versions, GitHub examples or forum posts to be exported more consistently.

## Languages {#sprachen}

The interface supports:

- system
- German
- English
- French
- Spanish
- Polish
- Russian

The `System` option detects the Windows language for `de`, `en`, `fr`, `es`, `pl`, and `ru`. System languages that are not supported fall back to English.

## Command line {#kommandozeile}

The project is built as a Windows application so that it starts without a console window. Arguments can still be processed internally.

```powershell
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export pool
```

The graphical interface is intended for normal use.

## Notes {#hinweise}

- Before importing into Home Assistant, each exported automation should be briefly checked.
- Automations with complex templates may require manual control.
- The original file `automations.yaml` is only read and not changed.
- The export folder should be outside of the productive Home Assistant configuration until the files are checked.
