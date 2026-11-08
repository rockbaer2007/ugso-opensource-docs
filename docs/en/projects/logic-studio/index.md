---
title: Logic Studio
description: First public test release of the visual function-block editor for Home Assistant.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.6 – first public test release, 8 November 2026.** Logic Studio is a standalone HA app for visual function-block plans, independent of Grafik Visual Studio and Blocks for HA. The editor currently uses **German**; this guide is available in **DE/EN/FR**.

::: warning Test release
Install on a test system first and create a full backup beforehand. Native detail properties currently use JSON. The app does not write automations/scripts back to HA or control devices. Review and install generated output yourself.
:::

[GitHub test release and ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.6) · [Source in the shared repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## Test installation from GitHub

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Under **Settings → Apps → App store → Repositories**, add the URL below. If “UGSo HA Apps” is already configured, check for updates instead.
2. Select and install **UGSo Logic Studio**. Enable advanced mode in your HA profile if experimental apps are hidden.
3. Start it and open its web UI. Supports **HA OS/Supervised**, **amd64 and aarch64**. The first container build may take several minutes. This is not a HACS/Marketplace frontend package.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Keep an existing local test installation:** GitHub and local apps have different repository IDs and separate data. Export your old plan using **Projekt** as JSON, then use **Öffnen** in the GitHub app. There is no automatic migration or uninstall. Each app retains its project and palette settings under `/data`.

## Two kinds of plan

| Plan | Purpose and output |
| --- | --- |
| Dataflow | Typed inputs/outputs, logic, math, selection, latches, edges, timers and counters. 33 implemented types; other reference types are marked templates. Export HA automation YAML, HA script YAML or a JavaScript function with a host interface. |
| Native HA flow | Import automations, scripts and blueprints as nested blocks. 53 additional HA types cover triggers, conditions, branches, loops, waits, variables and blueprint inputs. Export native HA YAML only. |

Dataflow simulation uses demo/snapshot values. Persistent blocks need the documented HA text helpers or a JavaScript memory host. Native HA flows are neither executed in the editor nor automatically translated to JavaScript. The JavaScript output is not an ioBroker script.

## Import and editing

Open **HA importieren**, choose automations/scripts/blueprints, and use **Aus HA einlesen**, a YAML/JSON file or pasted text. Select an entry, review its preview, then choose **Import übernehmen**. Save your existing plan as JSON first; project and source-file backups are also created.

The HA configuration mount is **read-only**. The app reads `automations.yaml`, `scripts.yaml` and blueprint files. Before parsing, sources are copied to `/data/ha-source-backups/<timestamp>/` using their original names. `secrets.yaml` is not opened; `!secret` and `!include` remain unresolved. Import referenced include files manually.

Orange **FLOW** wires represent execution order and branches: branch output → **DO**, then **NEXT → DO**. Yellow **VALUE/REF** wires show blueprint parameters and their `!input` usage. Properties contain HA configuration and branch paths as JSON. Parameter/field keys must be unique. Unknown sections remain **YAML_ORIGINAL**; missing wires can block export.

![Import preview of existing HA blueprints](/images/logic-studio/blueprint-import.png)

Each block’s **⋮ menu** offers **Eigenschaften** (properties), **Duplizieren** (duplicate) and **Löschen** (delete). Duplication copies properties without wires. Deletion removes associated wires; undo restores them. Search, favorites and recently used blocks help navigation.

![Per-block three-dot menu](/images/logic-studio/block-menu.png)

## Validation and limits

The **0.1.5** functional baseline was tested on **.193 / HA Core 2026.10.4**: actual blueprint import, automation/script/blueprint fixtures, semantically identical YAML exports and menu actions. **0.1.6** is its first public packaging. 22 Node and eight Python tests cover export, persistence, nested flows and safe source import; GitHub checks also build the container.

The editor does not provide complete HA semantic validation: verify targets, templates and selectors in HA. Comments, YAML anchors and formatting are not reconstructed. Import limits: **1 MB, 200 blocks, 500 wires**, bounded nesting and up to 250 blueprint files in standard folders. Controllers, calendar and custom subplans partly remain templates.

For local tests, extract the entire release ZIP, install Python 3.10+ and `requirements.txt`, then run **Start-Demo.cmd** on Windows. `http://127.0.0.1:4180/` shows demo entities without connecting to HA. The ZIP also contains `addon/logic_studio/` for local app installations.

[Report issues on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues) with versions, architecture and a minimal anonymized example. Do not publish credentials, personal automations or full backups. Further guides and the test report are included. MIT license; extracted block metadata attribution is in `THIRD-PARTY.txt`.
