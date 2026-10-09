---
title: UGSo Blocks for HA
description: Create native Home Assistant automations with visual Blocks.
---
# UGSo Blocks for HA

**Version 0.1.3 · experimental HA app.** Visual Blocks generate native Home Assistant automation YAML. Home Assistant runs the automation. Direct HA entity/action selection is still planned.

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

13 block types including the automation root:

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

Name, description, ID and `single`, `restart`, `queued`, `parallel` modes are available. Queued/parallel support a maximum count. Three examples cover light, battery and evening light.

## Gear icon: extend branches

As in the familiar ioBroker editor, the gear opens a small workspace. Attach **else if** clauses to the if container and optionally add **else**. Then connect conditions and actions in the main block.

- One branch generates `if`/`then`, optionally `else`.
- Multiple branches generate `choose`; else becomes `default`.
- HA runs the first matching branch, skipping any other matching branches.
- Removed clauses detach connected blocks. Reconnect or remove them before exporting.
- YAML import and JSON projects preserve branches. Older projects retain existing else actions.

AND/OR/NOT already supports chained conditions. Triggers and actions also support chains without an additional mutator. Numeric, sun and switching blocks provide dropdown choices. Generic HA action data currently uses JSON; a visual data-field mutator is planned.

## System: status and next steps

Control, toggle, delay and generic actions are available. Dedicated comment, debug, entity picker, state/attribute value, existence/availability, helper and script-control blocks will follow progressively. ioBroker `ack`, adapter instances and datapoint creation have no direct HA counterpart.

The full [comparison and implementation status](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/blocks_for_ha/docs/iobroker-comparison.en.md) is updated with every feature. Catalog and declarative plugins are planned.

## Validation and origin

The editor validates supported structure. Entity IDs are entered manually; installed actions and execution in real HA are not verified. Replace example entities and check actions in HA before use. The editor does not write HA system files.

Built with [Blockly](https://www.blockly.com/). Original HA blocks, not an ioBroker fork. Our code and Blockly: Apache-2.0; YAML library: ISC. License texts are included.
