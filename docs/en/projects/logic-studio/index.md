---
title: Logic Studio
description: HA Logic Studio Pro 0.1.23 with a live runtime, Blocks JS, and function block diagrams for Home Assistant.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.12 – public test update, 8 November 2026.** Both interface and documentation now support **DE/EN/FR**. Logic Studio is a standalone HA app for visual function-block plans, independent of Grafik Visual Studio and Blocks for HA. The React Flow canvas retains custom blocks, typed connections, zoom and MiniMap; libraries and licenses are bundled locally.

::: warning Test release
Install on a test system first and create a full backup beforehand. Native detail properties currently use JSON. The app does not write automations/scripts back to HA or control devices. Review and install generated output yourself.
:::

[GitHub test release and ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.12) · [Source in the shared repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## HA Logic Studio Pro 0.1.23

HA Logic Studio Pro is a separate Home Assistant app in the shared UGSo repository. **0.1.23** is a public test update for the live runtime. Make a full backup and try the update on a test system first.

### Changes since 0.1.12

- **Project tree and editors:** Projects and folders are stored on the server per HA user. Existing browser projects can be migrated on first launch from the original browser. JavaScript and TypeScript have syntax highlighting, line numbers and their own toolbars. The project picker, tree and filters use matching icons and colors. Blocks A and Blocks JS have separate filters. The automatic project pane width can still be adjusted with the handle.
- **Blocks A and Blocks JS:** Both use the bundled Blocks for HA catalog. Blocks A exports HA automations as YAML. Blocks JS generates JavaScript for the test run and runtime. Unrecognized ioBroker blocks are retained as placeholders and prevent code generation until replaced. Map ioBroker object IDs to Home Assistant entity IDs.
- **Function block diagram:** Simulation, one-second step and reset have icons in the top toolbar. Output format and preview sit on the right. Connections can be moved to another target input, and signal values appear at the input.
- **Server runtime:** Play starts JavaScript, transpiled TypeScript or Blocks JS on the HA server. Stop and restart are available in the editor. Runtime status and logs remain available across browsers. The separate **test run** uses simulated states and events. HA YAML scripts and automations can be exported and run in Home Assistant after import.

### Configure the live runtime

Under **Settings → Apps → HA Logic Studio Pro → Configuration**, add the required entries, save and restart the app. The lists start empty. Example for a dedicated test helper:

```yaml
runtime_read_entities: []
runtime_write_entities:
  - input_boolean.logic_studio_runtime_test
runtime_events:
  - logic_studio_runtime_test
```

Write access also allows reads. `ha.readState` and `ha.readAttribute` return the latest values confirmed by HA. `ha.onState`, `ha.onAttribute` and `ha.onEvent` respond to authorized changes and events. `ha.callAction` supports switching, setting number, text and select helpers, and pressing buttons on a single authorized target. `ha.schedule` handles time patterns and fixed times with optional weekdays in the HA time zone.

Scripts need to be started again after an app restart. On connection loss or a rejected action, the runtime stops the script and logs the error. Astronomical triggers and automatic reconnection are pending.

**Verified on .193 with HA 2026.11.1:** The runtime read a helper state and attribute, turned the helper on with a schedule and turned it off in response to a real HA event. Both state changes were reported. An imported Blocks JS schedule ran every two seconds. Earlier tests verified start, stop, restart and continued execution after leaving Studio with JavaScript and TypeScript.

### 0.1.26 · FBD Runtime

Use **Play** to run a function block diagram on the HA server. **Automatic** responds to changes in authorized states and attributes; **Fixed cycle** evaluates the diagram every 100 to 60,000 ms. Simulation and YAML export are separate. **Save** commits the draft; **Cancel** restores the last saved version. The toolbar is available in DE/EN/FR.

On .193, starting in automatic mode turned the test helper on, and the 200 ms cycle turned it off again. Stop and discarding an unsaved change were also verified. Both modes were additionally tested locally with input changes.

[GitHub test update and ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.26) · [App in the shared repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_logic_studio_pro)

## Test installation from GitHub

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Under **Settings → Apps → App store → Repositories**, add the URL below. If “UGSo HA Apps” is already configured, check for updates instead.
2. Select and install **UGSo Logic Studio**. Enable advanced mode in your HA profile if experimental apps are hidden.
3. Start it and open its web UI. Supports **HA OS/Supervised**, **amd64 and aarch64**. The first container build may take several minutes. This is not a HACS/Marketplace frontend package.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Keep an existing local test installation:** GitHub and local apps have different repository IDs and separate data. Export your old plan using **Projekt** as JSON, then use **Öffnen** in the GitHub app. There is no automatic migration or uninstall. Each app retains its project and palette settings under `/data`.

**Update an existing GitHub app:** Back up first, check for updates in the app manager and choose **UGSo Logic Studio → Update**. Keep the app installed: `/data`, entity IDs and existing plans are preserved. Do not uninstall or switch app IDs. On .193, the original plan, favorites, recent blocks and collapsed categories remained intact after the update.

## Language, toolbar and documentation

Choose **Language → Deutsch / English / Français** in the header. Menus, block descriptions, entity picker and import/export dialogs switch without reloading. The choice is saved with browser/app preferences. **Custom names, entity IDs, values, port names and generated YAML/JavaScript code are not translated.**

**Documentation** on the right lists implemented keyboard shortcuts and, when a block is selected, its description and input/output ports. **Ctrl+Z / Ctrl+Y**: undo/redo; **Delete**: delete selection; **Esc**: cancel a connection/close a menu. Use Tab and Enter/Space to select and connect ports. Debugger commands from the ioBroker reference editor are not presented as implemented features.

The toolbar groups **Undo/redo → Project → Simulation → Output**. The three simulation buttons have equal dimensions and separate borders. The project menu also offers **New project** and **Load example**. Open entity selection using the icon **beside HA entity ID** in STATE_IN/STATE_OUT properties; the previous top entity button is removed.

![German documentation view on .193 with the original plan intact](/images/logic-studio/0.1.12-193-de-documentation.png)

![English documentation view of the same plan on .193](/images/logic-studio/0.1.12-193-en-documentation.png)

![French documentation view of the same plan on .193](/images/logic-studio/0.1.12-193-fr-documentation.png)

## Two kinds of plan

| Plan | Purpose and output |
| --- | --- |
| Dataflow | Typed inputs/outputs, logic, math, selection, latches, edges, timers and counters. 33 implemented types; other reference types are marked templates. Export HA automation YAML, HA script YAML or a JavaScript function with a host interface. |
| Native HA flow | Import automations, scripts and blueprints as nested blocks. 53 additional HA types cover triggers, conditions, branches, loops, waits, variables and blueprint inputs. Export native HA YAML only. |

Dataflow simulation uses demo/snapshot values. Persistent blocks need the documented HA text helpers or a JavaScript memory host. Native HA flows are neither executed in the editor nor automatically translated to JavaScript. The JavaScript output is not an ioBroker script.

## Drag connections and overview

Hold the mouse button on a colored pin, drag to a matching opposite pin and release. The cursor becomes a crosshair and a wire preview follows the mouse. Compatible targets are highlighted green; incompatible or occupied inputs are marked red. Dragging from an input back to an output also works. **Esc** or releasing on empty canvas cancels; **Undo** removes a newly created wire.

**BOOL connects only to BOOL.** Identical signal types are compatible, with additional `INT → REAL` widening. Explicit `ANY` pins are universal. Numbers and text are not silently converted to BOOL. Each input accepts exactly one wire; incompatible types, matching pin directions, self-connections and cycles are rejected with an explanation. For keyboard operation, select the output with Tab/Enter, then select the input and press Enter.

![Compatible BOOL pins connected by mouse on .193](/images/logic-studio/0.1.7-bool-verbunden.png)

![STRING to BOOL is rejected with a clear type error](/images/logic-studio/0.1.7-typ-abgewiesen.png)

The bottom-right **MiniMap** shows colored block positions and the visible viewport. Drag inside it to navigate and use the wheel to zoom. Drag empty canvas to pan; **+/−** change the zoom and **Alles anzeigen** fits all blocks. Drag a block by its header. The **React Flow** attribution remains visible at the bottom right. Since 0.1.8 the library actually runs in the editor; domain logic, type validation and exporters remain independent Logic Studio components.

![React Flow canvas with preserved original plan and MiniMap on .193](/images/logic-studio/0.1.8-react-flow-193.jpg)

![Local React Flow test with typed blocks](/images/logic-studio/0.1.8-react-flow-local.jpg)

The following images additionally document the earlier 0.1.7 tests.

![Overview with block positions and visible viewport on .193](/images/logic-studio/0.1.7-miniuebersicht.png)

## Import and editing

Open **HA importieren**, choose automations/scripts/blueprints, and use **Aus HA einlesen**, a YAML/JSON file or pasted text. Select an entry, review its preview, then choose **Import übernehmen**. Save your existing plan as JSON first; project and source-file backups are also created.

The HA configuration mount is **read-only**. The app reads `automations.yaml`, `scripts.yaml` and blueprint files. Before parsing, sources are copied to `/data/ha-source-backups/<timestamp>/` using their original names. `secrets.yaml` is not opened; `!secret` and `!include` remain unresolved. Import referenced include files manually.

Orange **FLOW** wires represent execution order and branches: branch output → **DO**, then **NEXT → DO**. Yellow **VALUE/REF** wires show blueprint parameters and their `!input` usage. Properties contain HA configuration and branch paths as JSON. Parameter/field keys must be unique. Unknown sections remain **YAML_ORIGINAL**; missing wires can block export.

![Import preview of existing HA blueprints](/images/logic-studio/blueprint-import.png)

Each block’s **⋮ menu** offers **Eigenschaften** (properties), **Duplizieren** (duplicate) and **Löschen** (delete). Duplication copies properties without wires. Deletion removes associated wires; undo restores them. Search, favorites and recently used blocks help navigation.

![Per-block three-dot menu](/images/logic-studio/block-menu.png)

## Validation and limits

**0.1.12 on .193 / HA Core 2026.10.4:** Updated the local app from 0.1.8 after a full backup. DE/EN/FR, documentation and real HA entity selection passed. French survived browser reload, app restart and loading the saved app project again; German was restored afterwards. Project JSON differs **only in version**: all five blocks, three connections, names, values and positions are identical. Generated YAML is identical in EN and FR. No devices controlled. **31 Node and nine Python tests** passed. Older reports below remain as history.

![German restored after the successful app restart on .193](/images/logic-studio/0.1.12-193-neustart-de.png)

**0.1.8 on .193 / HA Core 2026.10.4:** Updated the existing local app after a full backup. Typed mouse connections, STRING→BOOL rejection, occupied inputs, move/undo, duplicate, zoom and MiniMap passed. The entity picker reads HA entities; a nested script with If/Then/Else, Delay and Stop was imported and exported with its structure preserved. The original plan was restored and compared after reload: **all IDs, positions, parameters and three wires unchanged**, along with favorites, recent blocks and collapsed categories. No devices were controlled. Docker build and container HTTP smoke test passed, as did **29 Node and eight Python tests**. Screenshots show the German UI. Light/dark switching was not manually retested in this step.

The **0.1.5** functional baseline was tested on **.193 / HA Core 2026.10.4**: actual blueprint import, automation/script/blueprint fixtures, semantically identical YAML exports and menu actions. **0.1.6** is its first public packaging. 22 Node and eight Python tests cover export, persistence, nested flows and safe source import; GitHub checks also build the container.

**0.1.7 on .193 / HA Core 2026.10.4:** Real mouse-drag tests passed for BOOL → BOOL and the reverse direction. STRING → BOOL and an occupied input were rejected. Overview, click navigation and Home were verified. The original plan was restored and compared with its backup: **five blocks, three wires and all palette preferences preserved**, including after the local update to 0.1.7. Full HA and separate plan/settings backups were created first; no devices were controlled. **26 Node and eight Python tests** currently pass. Screenshots show the German UI.

The editor does not provide complete HA semantic validation: verify targets, templates and selectors in HA. Comments, YAML anchors and formatting are not reconstructed. Import limits: **1 MB, 200 blocks, 500 wires**, bounded nesting and up to 250 blueprint files in standard folders. Controllers, calendar and custom subplans partly remain templates.

For local tests, extract the entire release ZIP, install Python 3.10+ and `requirements.txt`, then run **Start-Demo.cmd** on Windows. `http://127.0.0.1:4180/` shows demo entities without connecting to HA. The ZIP also contains `addon/logic_studio/` for local app installations.

[Report issues on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues) with versions, architecture and a minimal anonymized example. Do not publish credentials, personal automations or full backups. Further guides and the test report are included. MIT license; extracted block metadata attribution is in `THIRD-PARTY.txt`.
