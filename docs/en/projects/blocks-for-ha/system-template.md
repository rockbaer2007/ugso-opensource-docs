---
title: System values and Template builder
description: Shared entity values, app and automation controls, and readable templates.
---

# System values and Template builder

Available since **0.1.62**, fully translated into DE/EN/FR. System blocks provide values for Templates as well. Reuse existing text, math and variable blocks.

Since **0.1.63**, Template has direct value sockets in vertical rows, similar to ioBroker's Write file block. All Template blocks have no gear; inputs match their respective types.

## System

| Block | Purpose |
| --- | --- |
| Entity ID | Select an entity and connect its ID to another block. |
| Value of entity | Fixed HA selection: state, name, unit, attribute, last changed or last updated. |
| Value of entity ID | Connect an ID from an Entity ID, text or variable block. |
| Read once into variable | Save a snapshot, then execute the enclosed actions. This is not a trigger. The variable is also available to subsequent HA steps. |
| Control app | Start, stop or restart. Select installed apps through Supervisor or enter the slug manually. |
| Control automation | Enable, disable, toggle or run now. |

![Entity value](/assets/blocks-for-ha/blocks/en/ugso_entity_value.png)
![Dynamic entity value](/assets/blocks-for-ha/blocks/en/ugso_entity_value_dynamic.png)
![Snapshot](/assets/blocks-for-ha/blocks/en/ugso_entity_snapshot.png)
![Control automation](/assets/blocks-for-ha/blocks/en/ugso_automation_control.png)
![Control app](/assets/blocks-for-ha/blocks/en/ugso_app_control.png)

Select **Attribute** and enter its name; the appropriate row appears automatically. States are often text. Use **Conversion → to number** before calculations where needed. Missing attributes and timestamps yield `none`; a missing state yields HA's `unknown`. **Fallback** can handle these values.

The **Control automation** gear adds **Connect entity ID**, **Check conditions** and **Stop running actions**. A connected ID replaces the fixed selection. Condition checking applies to “run now”; stopping applies to “disable”. Without an explicit option, HA defaults apply: triggering skips conditions, disabling stops running actions. Enabling listens for triggers rather than immediately running actions.

**Control app** requires Supervisor and administrator privileges. The application receives read access to Supervisor for the selection list; start/stop/restart only happen when the exported automation executes in HA. Without Supervisor, the slug remains editable, but the action is unavailable there. Export: `hassio.app_start`, `hassio.app_stop`, `hassio.app_restart` with `data.app`.

## Build a Template

1. Attach **Templates → Template** to a value input such as “Message”.
2. Connect ordinary **Text** directly to **Part 1**.
3. Connect an **Entity value from System** or **Number format** directly to **Part 2**.
4. Filling the final input automatically adds another socket. Top-to-bottom order determines output order. Empty inputs are skipped and retain their position for undo/redo.

Example: text `Temperature: ` → entity value `sensor.temperature` through **Number format** with the math number `1` for decimal places → text ` °C`. Example result: `Temperature: 21.6 °C`.

![Template](/assets/blocks-for-ha/blocks/en/ugso_template_builder.png)
![New line as a value](/assets/blocks-for-ha/blocks/en/ugso_template_linebreak.png)
![Number format](/assets/blocks-for-ha/blocks/en/ugso_number_format.png)
![Conditional output](/assets/blocks-for-ha/blocks/en/ugso_template_conditional.png)

| Addition | Meaning |
| --- | --- |
| Number format | 0–10 decimal places, using a decimal point. Use a math number for the count. Connect a fallback directly to its optional value input; invalid numbers otherwise produce empty text. |
| Value otherwise | Fallback for `unknown`, `unavailable`, `none` and empty text. Keeps `0` and `false`. |
| New line | Starts a new line here. |
| if / then / else | Connect a Boolean condition to “if” and the respective values to “then” and “else”. Connect another Template for multiple parts in a branch. Empty branches produce empty text. |

Attach formatting directly around the value it affects. Text, numbers, entity values, newlines and conditional values use value sockets; “if” accepts only Boolean blocks. Action chains cannot connect to these inputs. Jinja characters inside ordinary text remain literal text. Older Output chains automatically migrate to direct values when loaded in the editor, retaining branches and disabled parts. Old block types remain readable for project compatibility but are no longer listed in the menu.

**Right-click → Template preview / Jinja** shows generated code and asks HA to render current values. This is a snapshot, executes no actions and requires an accessible HA connection. Without a connection, the preview is explicitly unavailable. Credentials stay on the server. Project JSON preserves blocks, connections and gear choices. YAML contains native Jinja; YAML import may restore it as a free template block. HA may interpret pure numbers or lists in template results as native values.

References: [HA automation actions](https://www.home-assistant.io/docs/automation/automation_integration_actions/), [Supervisor](https://www.home-assistant.io/integrations/hassio/), [Jinja in HA](https://www.home-assistant.io/docs/templating/).
