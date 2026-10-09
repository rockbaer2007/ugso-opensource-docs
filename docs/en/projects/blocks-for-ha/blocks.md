---
title: Block catalog
description: All UGSo Blocks for HA with images, functionality and original plugins.
---
# Block catalog

Version **0.1.7**: 23 block types. Images show actual UGSo editor blocks. Dropdown variants do not count as additional types.

Triggers are orange, conditions purple, values green and actions blue. Side connections are typed; triggers and actions form separate vertical chains. Entity IDs are currently entered manually.

| Block | Editor image | Function |
| --- | --- | --- |
| **Automation**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/ugso_automation.png" alt="Automation" style="max-width:280px;max-height:180px"> | Root with triggers, optional condition and action chain. Name, ID, description and mode are edited outside the block. |
| **State reached**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_state_trigger.png" alt="State reached" style="max-width:280px;max-height:180px"> | Starts when the entity reaches the entered state. Generates `trigger: state` with `to`. |
| **Numeric threshold trigger**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_numeric_trigger.png" alt="Numeric threshold trigger" style="max-width:280px;max-height:180px"> | Starts on threshold crossing, not continuously. Number threshold; `trigger: numeric_state`. |
| **Time**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_trigger.png" alt="Time" style="max-width:280px;max-height:180px"> | Daily time trigger, HH:MM or HH:MM:SS; `trigger: time`. |
| **Sunrise/sunset**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_sun_trigger.png" alt="Sunrise/sunset" style="max-width:280px;max-height:180px"> | Sunrise or sunset dropdown; `trigger: sun`. |
| **HA starts**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_start_trigger.png" alt="HA starts" style="max-width:280px;max-height:180px"> | Starts when Home Assistant starts; `trigger: homeassistant`. |
| **State is**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_state_condition.png" alt="State is" style="max-width:280px;max-height:180px"> | Boolean condition: entity has the specified state; `condition: state`. |
| **Numeric condition**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_numeric_condition.png" alt="Numeric condition" style="max-width:280px;max-height:180px"> | Boolean above/below threshold condition; `condition: numeric_state`. |
| **AND / OR / NOT**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_logic_condition.png" alt="AND / OR / NOT" style="max-width:280px;max-height:180px"> | Combines 1–100 conditions. Plus/minus adds or removes the last input; gear reorders. `and`, `or`, `not`. |
| **Today’s date**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_date_condition.png" alt="Today’s date" style="max-width:280px;max-height:180px"> | Date picker with equals/on-or-after/on-or-before, including year. HA template compares today in HA’s time zone. Not a trigger. |
| **Number**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/ugso_number.png" alt="Number" style="max-width:280px;max-height:180px"> | General numeric value. Fits thresholds and delays; destination-specific validation still applies. |
| **Percentage**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/ugso_percent.png" alt="Percentage" style="max-width:280px;max-height:180px"> | Slider and exact input for integers 0–100. Number output, e.g. charge level or brightness. |
| **Multiline text**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/ugso_text.png" alt="Multiline text" style="max-width:280px;max-height:180px"> | String value for logs. Enter inserts a newline; Shift+Enter commits. Three visible lines; full text is retained. |
| **Colour**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/ugso_colour.png" alt="Colour" style="max-width:280px;max-height:180px"> | Hex colour picker with Colour output for the light action. Dedicated type rejects text and number connections. |
| **On / off / toggle**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_switch_action.png" alt="On / off / toggle" style="max-width:280px;max-height:180px"> | Entity-domain action: `turn_on`, `turn_off` or `toggle`. Entity must support the action. |
| **Generic HA action**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_service_action.png" alt="Generic HA action" style="max-width:280px;max-height:180px"> | Action name, optional single entity target, JSON object data. Supports parameters not exposed by dedicated blocks. |
| **Wait seconds**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_delay_action.png" alt="Wait seconds" style="max-width:280px;max-height:180px"> | Delay of 0–86400 integer seconds. Number input with shadow default. |
| **If / else if / else**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_if_action.png" alt="If / else if / else" style="max-width:280px;max-height:180px"> | Plus/minus adds or removes the last else-if branch; S toggles else. Gear reorders. `if` or `choose`, first matching branch. |
| **Log output**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_log_action.png" alt="Log output" style="max-width:280px;max-height:180px"> | Text message and severity dropdown; `system_log.write`. HA may filter Info/Debug. |
| **Control HA script**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_script_action.png" alt="Control HA script" style="max-width:280px;max-height:180px"> | Start without waiting, stop, or call and wait. `script.turn_on`, `script.turn_off` or `script.name`. |
| **Refresh entity**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_update_action.png" alt="Refresh entity" style="max-width:280px;max-height:180px"> | `homeassistant.update_entity` requests a refresh. Does not set state; support depends on integration. |
| **Control helper**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_helper_action.png" alt="Control helper" style="max-width:280px;max-height:180px"> | Switch/counter/timer type controls the action dropdown. Entity ID must match. Timer uses configured duration; parameters use generic action. |
| **Light with colour**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_colour_action.png" alt="Light with colour" style="max-width:280px;max-height:180px"> | Light entity, Colour input and brightness 0–100. Generates `light.turn_on` with `rgb_color` and `brightness_pct`. Device must support colours. |

Minus or disabling else detaches connected blocks instead of deleting them. Reconnect or remove them before YAML export. Undo restores inputs and connections. Shadow values reappear when a replacement value block is removed.

## Original plugins and integration

The six integrated original plugins are pinned to **13.2.0** and bundled locally with Blockly **13.3.0**. License: Apache-2.0. Links below lead directly to upstream repositories. HA blocks, YAML adapters and plus/minus controls are UGSo code.

| Originalplugin | Usage / status |
| --- | --- |
| [toolbox-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) | Search at the bottom of the menu, German search hints; results preserve dropdowns and shadows. |
| [field-multilineinput](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) | Used by Text; newlines remain in projects and YAML. |
| [field-slider](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) | Used by Percentage; 0–100 with exact numeric entry. |
| [field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) | Used by Colour; converts hex to RGB for lights. Blend/random remain pending. |
| [field-date](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) | Used by date comparison; UGSo subclass guards the deferred picker call. |
| [field-dependent-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) | Used by Helper; type determines actions. No live HA selection. |
| [block-plus-minus](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-plus-minus) | Interaction implemented in our HA blocks; original plugin is not installed. Gear remains available. |
| [block-dynamic-connection](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-dynamic-connection) | Not integrated yet. Automatic growing connections, text joining and lists are planned. |

The colour field also uses the transitive dependency [field-grid-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-grid-dropdown). HA output is generated by our adapters; bundled JavaScript generators are not used.

[Back to overview](/en/projects/blocks-for-ha/)
