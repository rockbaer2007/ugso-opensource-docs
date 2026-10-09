---
title: UGSo Blocks for HA
description: Create native Home Assistant automations with visual Blocks.
---
# UGSo Blocks for HA

**Version 0.1.6 · experimental HA app.** Visual Blocks generate native Home Assistant automation YAML. Home Assistant runs the automation. Direct HA entity/action selection is still planned.

Blocks use classic Blockly puzzle shapes (Geras) with compact text. Initial fitting and the fit button cap small automations at 80 percent. Manual zoom can enlarge the view further. Reference: [Original Blockly examples](https://raspberrypifoundation.github.io/blockly-samples/).

## Install from the HA app store

Add or refresh `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` in the app store. Install **UGSo Blocks for HA**, start it and select **Open Web UI**. The app supports amd64 and aarch64 and serves the editor through HA ingress. No additional token is needed to open it. It does not yet access HA entities or write HA system files.

## Start and files

Code lives beside Grafik Visual Studio in the [shared repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha). In `blocks_for_ha`, using Node.js 22.12 or newer:

```sh
npm install
npm run dev
```

Editor: `http://127.0.0.1:4180/`. Preview, copy, download and reopen supported YAML as Blocks. Files must contain one automation object or a list with one entry. Unsupported structures are rejected. JSON projects also retain block positions; the browser persists the latest project locally.

## ioBroker / our Blocks: existing features

18 block types including the automation root:

| ioBroker concept | UGSo Blocks for HA | HA output |
| --- | --- | --- |
| Script container | Automation | `triggers`, `conditions`, `actions` |
| State trigger | State reached | `trigger: state` |
| Numeric trigger check | Above/below threshold crossing | `trigger: numeric_state` |
| Schedule | Time | `trigger: time` |
| Astro | Sunrise/sunset | `trigger: sun` |
| System start, different lifecycle | HA starts | `trigger: homeassistant` |
| State comparison | State is | `condition: state` |
| Numeric comparison | Number above/below | `condition: numeric_state` |
| AND/OR/NOT | All/at least one/none of the conditions | `and`, `or`, `not` |
| Control/toggle | On/off/toggle | Appropriate entity-domain action |
| Adapter action | Generic HA action | `action`, optional entity target and JSON data |
| Pause | Wait seconds | `delay` |
| If/else if/else | Extensible if block | `if` or `choose` |
| Number | Number value block, also used as a shadow default | Constant threshold or delay |
| Text | Text value block with shadow | Log message |
| Debug output | Log with severity | `system_log.write` |
| Control script | Start/stop/call and wait | `script.turn_on`, `script.turn_off` or direct call |
| Update state, different semantics | Refresh entity | `homeassistant.update_entity` |

Name, description, ID and `single`, `restart`, `queued`, `parallel` modes are available. Queued/parallel support a maximum count. Three examples cover light, battery and evening light.

## System blocks added in version 0.1.6

The **System** category contains three new action blocks. **Values** also includes a green **Text** block with a String output for the log message input. Numbers and conditions cannot connect to this input.

| ioBroker | Our block | Controls and HA behavior |
| --- | --- | --- |
| Debug output | Log | Editable text shadow or text block; Info, Warning, Error, Debug or Critical dropdown. Generates `system_log.write`. |
| Control script | HA script | Enter script ID; choose start without waiting, stop, or call and wait. |
| Update state | Refresh entity | Requests a refresh through `homeassistant.update_entity`. Does not set state and has no ioBroker `ack` semantics. |
| Text | Text value block | Editable log message, retained in projects and YAML. |

**Start without waiting** generates `script.turn_on` and lets the automation continue. **Stop** generates `script.turn_off`. **Call and wait** generates a direct `script.name` call: the automation waits for completion and errors can propagate to the caller. Script parameters still use the generic HA action.

YAML import recognizes exact supported System action shapes. Additional data such as a custom logger or script variables remains in the generic HA action. Refresh behavior depends on integration support. Log messages are written when HA executes the automation; Info and Debug may be filtered by HA logging configuration.

References: [HA system log](https://www.home-assistant.io/integrations/system_log/), [HA scripts](https://www.home-assistant.io/integrations/script/), [HA Core actions](https://www.home-assistant.io/integrations/homeassistant/).

## Gear icon: extend branches

As in the familiar ioBroker editor, the gear opens a small workspace. Attach **else if** clauses to the if container and optionally add **else**. Then connect conditions and actions in the main block.

- One branch generates `if`/`then`, optionally `else`.
- Multiple branches generate `choose`; else becomes `default`.
- HA runs the first matching branch, skipping any other matching branches.
- Removed clauses detach connected blocks. Reconnect or remove them before exporting.
- YAML import and JSON projects preserve branches. Older projects retain existing else actions.

AND/OR/NOT has its own gear for 1–100 condition value inputs. Triggers and actions support chains. Sun, comparison and switching choices use dropdowns. Generic HA action data currently uses JSON; a visual data-field mutator is planned.

## Connections and controls

The category menu is dark and the block flyout is light. Values are green, triggers orange, conditions purple and actions blue. Category markers identify each block group; the selected category has an additional highlight.

- **Left output / right value input:** Conditions produce Boolean values for the automation condition slot, if/else-if and AND/OR/NOT. Numbers produce Number values for thresholds and delays. Type checks reject incompatible connections.
- **Previous / next:** Triggers and actions each form their own statement chains and cannot be mixed.
- **Statement cavity:** Then/else slots accept action sequences. Conditions belong in value inputs.
- **Shadow numbers:** Thresholds and delays have editable defaults that can be replaced by number blocks. Removing a replacement restores the default. Log messages use String text blocks with editable shadows. Sensor and entity value blocks are not implemented yet.
- **Context menu:** Right-click or long-press for Blockly actions such as duplicate, comment, collapse, disable, delete and help. Help links to the documentation. Comments remain in JSON projects; YAML comment export is not implemented.
- **Disable:** Disabled actions, triggers and conditions are omitted from export. Required content remains required: missing triggers, empty if conditions or empty action branches prevent export.
- **Trash:** Delete blocks, open the trash and drag deleted blocks back to the workspace. History lasts for the current session. Undo/redo is also available.
- **Insertion marker:** Blockly previews the potential connection while dragging.

Projects from version 0.1.4 and earlier are upgraded automatically. Old condition chains become AND groups preserving their YAML meaning. Existing supported YAML files remain importable.

## Blockly library and tracked development status

We already use the original **Blockly 13.3.0** library rather than building a separate block engine. Blockly provides the workspace, category toolbox and flyouts, typed connections, shadow blocks, mutators, context menu, zoom, trash and insertion markers. HA block definitions, structural validation, project migration and the YAML generator are UGSo code. No ioBroker JavaScript is executed.

The [original workspace and block-parts documentation](https://docs.blockly.com/guides/get-started/workspace-anatomy/) and [Blockly examples](https://raspberrypifoundation.github.io/blockly-samples/) guide familiar interaction patterns. Library updates require connection, import/export and browser checks.

| Task | Status in 0.1.6 / next step |
| --- | --- |
| Connection geometry and type checks | Boolean conditions and Number values use side connections; triggers/actions use separate statement chains |
| Extensible blocks | If and AND/OR/NOT implemented; visual action-data fields planned |
| Default values | Shadow numbers and text blocks implemented; entity value blocks pending |
| Sensor values and attributes | Pending; include appropriate HA template output and type conversion |
| Editor controls | Context menu, help, disable, trash recovery, zoom and insertion markers available |
| Comments | Retained in projects; YAML comments and dedicated comment block pending |
| Menu and block colors | Dark category menu, light flyout and distinct group colors implemented |
| ioBroker categories | Review progressively, starting with System; update comparison for every feature |
| Publishing and updates | Every new HA app starts in the shared repository with installable packaging; bump package and UI versions together |
| HA connection, catalog and plugins | Pending; managed connection and declarative extensions planned |

This page tracks implemented features and outstanding tasks together and is maintained with each extension.

## System: status and next steps

Control, toggle, delay, generic actions, logging, script control and entity refresh are available. Dedicated comment, entity picker, state/attribute value, existence/availability and helper blocks will follow progressively. ioBroker `ack`, adapter instances and datapoint creation have no direct HA counterpart.

The full [comparison and implementation status](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/blocks_for_ha/docs/iobroker-comparison.en.md) is updated with every feature. Catalog and declarative plugins are planned.

## Validation and origin

The editor validates supported structure. Entity IDs are entered manually; installed actions and execution in real HA are not verified. Replace example entities and check actions in HA before use. The editor does not write HA system files.

Built with [Blockly](https://www.blockly.com/). Original HA blocks, not an ioBroker fork. Our code and Blockly: Apache-2.0; YAML library: ISC. License texts are included.
