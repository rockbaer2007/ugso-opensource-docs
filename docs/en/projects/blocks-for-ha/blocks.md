---
title: Block catalog
description: All UGSo Blocks for HA with images, functionality and original plugins.
---
# Block catalog

Version **0.1.12**: 50 block types. Images show actual UGSo editor blocks. Guides and ioBroker comparison: [Date and time](./time), [Conversion](./conversion). Dropdown variants do not count as additional types.

Triggers are orange, conditions purple, values green and actions blue. Side connections are typed; triggers and actions form separate vertical chains. Entity IDs are currently entered manually.

## Conversion added in 0.1.12

[Guide, ioBroker comparison and pending JSONata](./conversion).

| Block | Image | Function |
| --- | --- | --- |
| **To number**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_number.png" alt="To number" style="max-width:280px;max-height:180px"> | HA float without fallback; complete numeric input with decimal point. Runtime number for variables, comparisons and time calculations. |
| **To Boolean**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_boolean.png" alt="To Boolean" style="max-width:280px;max-height:180px"> | HA bool for recognized Boolean/text values. Boolean output for conditions and logic. |
| **To string**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_string.png" alt="To string" style="max-width:280px;max-height:180px"> | Jinja text representation of a value; not JSON serialization. |
| **Type of**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_type.png" alt="Type of" style="max-width:280px;max-height:180px"> | HA typeof returns Python names such as str, float, bool, dict. HA 2023.4 or newer. |
| **To datetime**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_datetime.png" alt="To datetime" style="max-width:280px;max-height:180px"> | ISO text or Unix seconds/milliseconds to HA local datetime. Typed Time output. |
| **Datetime to …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_date_format.png" alt="Datetime to …" style="max-width:280px;max-height:180px"> | Datetime, formatted text, Unix number or date component. Selection changes output type; custom format shows a field. |
| **Format duration**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_duration.png" alt="Format duration" style="max-width:280px;max-height:180px"> | Duration in milliseconds or seconds to hh:mm:ss, hh:mm, mm:ss. Preserves sign and total hours/minutes. |
| **JSON to value**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_from_json.png" alt="JSON to value" style="max-width:280px;max-height:180px"> | JSON text to object, list or scalar. Invalid JSON causes an HA error. |
| **Value to JSON**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_to_json.png" alt="Value to JSON" style="max-width:280px;max-height:180px"> | JSON serialization with indentation checkbox. Format datetimes first. |

## Date and time added in 0.1.11

Purple time blocks use a typed datetime socket. [Usage, boundary rules and comparison](./time).

| Block | Image | Function |
| --- | --- | --- |
| **Clock comparison**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_compare.png" alt="Clock comparison" style="max-width:280px;max-height:180px"> | Fixed HH:mm/HH:mm:ss; comparison or period. End field appears for between/outside. |
| **Clock comparison with inputs**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_compare_input.png" alt="Clock comparison with inputs" style="max-width:280px;max-height:180px"> | Text boundaries; uncheck current time to expose a datetime socket. Overnight periods supported. |
| **Current datetime**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_now.png" alt="Current datetime" style="max-width:280px;max-height:180px"> | HA local date, time and timezone. Typed Time output. |
| **Calendar start**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_boundary.png" alt="Calendar start" style="max-width:280px;max-height:180px"> | Start of today, tomorrow, week (Monday), month or year. |
| **Next sun event**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_sun.png" alt="Next sun event" style="max-width:280px;max-height:180px"> | Rise, set, dawn, dusk, solar noon or midnight from sun.sun, with minute offset. May be tomorrow. |
| **Shift datetime**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_shift.png" alt="Shift datetime" style="max-width:280px;max-height:180px"> | Datetime plus/minus number in milliseconds, seconds, minutes, hours or days. |
| **Format datetime**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_format.png" alt="Format datetime" style="max-width:280px;max-height:180px"> | Clock time, date, date/time, ISO with timezone or Unix seconds. |

## Other blocks

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

## Variable and template blocks added in 0.1.8

| Block | Editor image | Function |
| --- | --- | --- |
| **Set variable**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_set.png" alt="Set variable" style="max-width:280px;max-height:180px"> | Action block: assign a number, text/template, Boolean or null to the selected variable. Generates native HA `variables`. Place before subsequent reads. |
| **Read variable**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_get.png" alt="Read variable" style="max-width:280px;max-height:180px"> | Side String connector; generates <code v-pre>{{ name }}</code> for log messages and further assignments. Dropdown supports rename/delete. |
| **Template value**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/ugso_template.png" alt="Template value" style="max-width:280px;max-height:180px"> | Multiline Jinja template with String connector for log messages or variable assignments. HA evaluates the template during execution; Blocks does not execute it. |
| **Template condition**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_template_condition.png" alt="Template condition" style="max-width:280px;max-height:180px"> | Boolean connector for Only if, If and logical groups. Generates `condition: template` with `value_template`. HA must evaluate it as true; not a trigger. |

## Using variables and templates

### Increment and decrement added in 0.1.10

| Block | Editor image | Function |
| --- | --- | --- |
| **Change variable by …**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_change.png" alt="Change variable by" style="max-width:280px;max-height:180px"> | Variable dropdown and Number input with default step `1`. Adds the step to a previously assigned numeric variable. Negative steps decrease; `0` and fractional steps are supported. Native HA variable assignment using Jinja. |

The **Variablen** menu dynamically offers **Set**, **Change by** and **Read** for each created variable. Example action chain: **Set test to 10 → Change test by 1 → Log Info message Read test**. The message then uses `11`; a step of `-2` changes `10` to `8`.

Assign a number before incrementing. Undefined variables, text (including `"10"`), Boolean and null are not automatically converted or initialized as `0`; Jinja evaluation in HA fails for those values. Creating a variable alone does not assign it. JSON retains the increment block; importing our exact YAML output recreates it. Other calculation templates remain template blocks. The planned typed-variable dialog is still pending.

Choose **Variablen → Variable erstellen …** in the German editor to create, for example, `leistung`. Names use ASCII letters, digits and `_`, with no leading digit. Place Set variable in **Dann** and connect a number or template. Connect Read variable to a subsequent log message. Creating a name alone does not assign a value. Variables belong to the HA automation run; they are not persistent helpers.

Example: **Set leistung to Template** containing <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>, followed by **Log Info message Read leistung**. HA reads the sensor during assignment and uses that value in the next step. A template condition can check <code v-pre>{{ states('sensor.leistung') | float(0) > 100 }}</code>.

Renaming updates variable blocks. References in free-form Jinja text must be changed manually. Action variables become available after assignment, not in preceding automation conditions. Blocks validates structure and YAML, not Jinja syntax or HA entities. Import supports one text/template, number, Boolean or null per variable action. Multiple entries, lists/objects and automation-level variables are not yet supported and are rejected during import. [Native HA variables and scope](https://www.home-assistant.io/docs/scripts/#define-variables).

## Logic blocks added in 0.1.9

| Block | Editor image | Function |
| --- | --- | --- |
| **Compare**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/ugso_compare.png" alt="Compare" style="max-width:280px;max-height:180px"> | Compares two values using =, ≠, &lt;, ≤, &gt; or ≥. Accepts numbers, text, variables and single template expressions. Boolean result exported as an HA template condition or variable value. |
| **Compact AND / OR**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/ugso_binary_logic.png" alt="Compact AND OR" style="max-width:280px;max-height:180px"> | Two Boolean inputs. Generates native HA `and`/`or` groups as conditions and parenthesized Jinja as variable values. Expandable groups remain available. |
| **NOT**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/ugso_not.png" alt="NOT" style="max-width:280px;max-height:180px"> | Negates a Boolean condition. Native HA `not` group as condition, Jinja `not` as variable value. |
| **true / false**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/ugso_boolean.png" alt="true false" style="max-width:280px;max-height:180px"> | Boolean constant with dropdown for conditions and variables. Assignments retain native YAML Boolean types. |
| **null**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/ugso_null.png" alt="null" style="max-width:280px;max-height:180px"> | No value: YAML `null` in assignments, Jinja `none` in expressions. Different from `0` and `false`; not a Boolean condition. |
| **If → value → otherwise value**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/ugso_ternary.png" alt="Conditional value" style="max-width:280px;max-height:180px"> | Selects one of two values using a Boolean condition. For variables, log messages and comparisons; generates a Jinja expression, not an action sequence. |

**Example:** Assign `leistung` first. Then use **Set meldung to If**, with **Compare Variable leistung &gt; Number 100** as test, text **High power** as true value and **Low power** as false value. Follow with **Log Info message Variable meldung**. HA evaluates the choice during execution.

Comparisons do not automatically convert types: number `20` differs from text `"20"`. Convert sensor states with `float` or `int` where appropriate. Expression inputs accept a single Jinja output, for example <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>. Multiline statements and mixed text remain supported in standalone template value blocks. Dynamic choices are not supported as fixed numeric thresholds or delays.

JSON projects preserve block shapes and connections. YAML preserves native meaning: reopening maps comparisons and value choices to template blocks and AND/OR/NOT to condition groups. [HA logical conditions](https://www.home-assistant.io/docs/scripts/conditions/#logical-conditions).

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
