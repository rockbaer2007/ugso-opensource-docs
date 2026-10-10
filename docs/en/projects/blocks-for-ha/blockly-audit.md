---
title: Blockly comparison, colours and functions
description: All standard categories compared with ioBroker and our Home Assistant output.
---
# Blockly comparison, colours and functions

## Action functions and conditional results since 0.1.47

In **Functions**, define an action function beside the automation. Use a valid name without spaces, add up to eight distinct ASCII parameters with the cog, and insert HA actions into the body. Its call block appears automatically in the same category; connect every argument. Read parameters using variable blocks from **Variables**, for example as a log message, pause duration or variable assignment value.

Export produces a native HA `sequence`. Each call receives its own internal parameter bindings; arguments are evaluated at the call. Nested calls are supported; recursion and empty bodies are rejected. Parameter bindings do not overwrite equally named HA variables. Other assignments in the body remain normal HA assignments. Free Jinja/JSON text fields keep their normal HA context and are not rewritten to local parameters; connect variable blocks instead. **Stop** still stops the entire HA run.

**If / return / otherwise** produces a conditional Jinja value. Only the selected branch is evaluated. Connect it to a value function’s return socket or another value input. Both branches and the condition are required. This is not an early return from an action sequence.

JSON projects retain definitions, parameters, calls and layout. YAML contains expanded steps or expressions; importing YAML reconstructs those steps, not the original function definitions. [Block images](./blocks#functions-since-0-1-47). The tables below also document the historical 0.1.15 comparison.

Version **0.1.15**, October 10, 2026: **111 supported block types**. Three colour calculations and three original Blockly types for value functions/parameters are new. Function definitions may sit beside the automation; other disconnected blocks still prevent export.

## Sources and method

We compared our installed **Blockly 13.3.0** standard blocks, the original [Blockly block library](https://github.com/raspberrypifoundation/blockly/tree/4195d60c610bec4b4b186aa22d58cb16beb42dfa/blocks), the [ioBroker default toolbox](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/index.html) and its [Blockly bridge](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/src/Components/blockly-plugins/bridge.ts). These links pin the reviewed commits.

**Registered, offered in the menu and exportable here are different states.** ioBroker imports the complete standard library. Registered blocks need not appear in its default toolbox. Screenshots may also show an older toolbox. Text reverse is now included in ioBroker's menu; atan2 is absent there but registered through the library import. This does not prove ioBroker cannot execute atan2.

## All standard categories

| Category / original types | ioBroker default menu | UGSo / HA and remaining variants |
| --- | --- | --- |
| Logic: `controls_if`, `controls_ifelse`, `logic_compare`, `logic_operation`, `logic_negate`, `logic_boolean`, `logic_null`, `logic_ternary` | Included, plus custom multi-AND/OR, cases, range and fallback | Comparisons, groups, If/Else-if/Else, conditional values, ranges and cases implemented. Own blocks combine shape variants. |
| Loops: `controls_repeat`, `controls_repeat_ext`, `controls_whileUntil`, `controls_for`, `controls_forEach` | Included, mainly repeat with value input | Count/while/until/for-each and fixed integer counting bounds implemented. Dynamic/fractional counting bounds pending. |
| Loop control: `controls_flow_statements` | break / continue | Local break/continue pending. Stop run ends the whole HA run and is not a replacement. |
| Math: `math_number`, `math_arithmetic`, `math_single`, `math_trig`, `math_constant`, `math_number_property`, `math_round`, `math_on_list`, `math_modulo`, `math_constrain`, `math_random_int`, `math_random_float`, `math_change` | Included, plus fixed decimal places | Own arithmetic/statistics/rounding/random/variable-change blocks. Prime tests, standard deviation, modes including ties and infinity pending. Not all dropdown variants have parity. |
| Math: `math_atan2` | Not offered; registered in library | Four-quadrant angle already implemented. |
| Text: `text`, `text_join`, `text_append`, `text_length`, `text_isEmpty`, `text_indexOf`, `text_charAt`, `text_getSubstring`, `text_changeCase`, `text_trim`, `text_count`, `text_replace`, `text_reverse` | Included, plus multiline, newline, contains and number formatting | Implemented including reverse. Substring currently uses start-based bounds; further positions and ioBroker number formatting pending. |
| Text: `text_print`, `text_prompt`, `text_prompt_ext` | Not offered | Output through HA Log action. Browser prompts would not provide later HA runtime input. |
| Lists: `lists_create_empty`, `lists_create_with`, `lists_repeat`, `lists_length`, `lists_isEmpty`, `lists_indexOf`, `lists_getIndex`, `lists_setIndex`, `lists_getSublist`, `lists_split`, `lists_sort`, `lists_reverse` | Included; empty list is a variant | Create with 0–100 inputs, repeat, search/get/set/remove/insert, sublist, split/join, sort/reverse implemented. Combined get-and-remove and further end/random positions pending. |
| Variables: `variables_get`, `variables_set`, typed variants `variables_get_dynamic`, `variables_set_dynamic` | Dynamic VARIABLE category, no VARIABLE_DYNAMIC category | Create/get/set/change implemented. Type selection/typed-variable-modal remains planned. Original getter additionally supported for function parameters. |
| Functions: `procedures_defreturn`, `procedures_callreturn`, `procedures_defnoreturn`, `procedures_callnoreturn`, `procedures_ifreturn` | Dynamic PROCEDURE category | New original value definition/call with parameters and return value. Actions without a return use existing HA Script calls; no local action functions or early return. |
| Colour: picker/random/rgb/blend from field-colour | All four included | Picker plus random/RGB/blend now in own category; own HA generators instead of JavaScript. |

Internal mutator helpers are not independent user blocks. Older aliases are covered by their corresponding function. ioBroker's additional System, Actions, Sendto, Date/Time, Conversion, Trigger, Timeouts and Object categories extend its script engine. Existing counterparts are documented under [Date/time](./time), [Conversion](./conversion), [Timeouts/objects/logic](./flow) and [Collections](./collections). Other adapters and third-party installations are outside this default comparison. Sendto/JSONata and named JavaScript timer handles are not presented as native HA features.

## Using colours

**Farbe** offers picker, random colour, RGB percentages and blending. Percentages clamp to 0–100 and the ratio to 0–1. Channels convert to 0–255, rounding positive half values upward. Ratio 0 selects colour 1, ratio 1 colour 2; red/blue at 0.5 produces `[128, 0, 128]`. No gamma correction.

Unlike the original JavaScript colour blocks, calculated values are **HA RGB lists**, not hex strings. Connect to **Light → Colour** or a variable assignment. A fixed picker still exports a native RGB list; calculations produce a template in `data.rgb_color`. Saved RGB variables can be connected too. Exactly three numeric channels in 0–255 are required; convert hex strings deliberately first. Invalid values produce template errors.

Blending evaluates each directly connected colour block once. Store changing numeric/template inputs, especially the ratio, in a variable first: generated type checks or reused function parameters can evaluate expressions repeatedly. Randomness is not cryptographic. Generators use the documented HA helpers [zip](https://www.home-assistant.io/template-functions/zip/), [multiply](https://www.home-assistant.io/template-functions/multiply/) and [add](https://www.home-assistant.io/template-functions/add/). The reference describes current HA; check availability on older installations.

## Using value functions

1. Open **Funktionen** and drag a definition onto the workspace.
2. Name it `double`; add parameter `x` through the original cog editor.
3. Connect **Variable x × Number 2** as the return value. Variable getters read parameters.
4. Reopen the category: the `double` call with input `x` appears dynamically. Connect 21 and assign the call to a variable.

Export expands the Jinja expression with argument 21; it creates no JavaScript/Python function. Up to eight distinct parameters; ASCII letters/digits/underscores, starting with a letter or underscore. Nested calls follow the general expression-depth limit. Recursion, missing arguments/returns, duplicate names and action bodies prevent export. Within a value function parameters override equally named automation variables. Outside, normal HA variables and scope apply. Connector colours alone do not guarantee runtime return types; a condition requires a Boolean result.

JSON projects retain definitions, parameters and calls. YAML stores expanded meaning and reopens as templates; definitions cannot be reconstructed from it. Planned Developer Tools imports for arbitrary block/template packages remain a separate roadmap item.

Verified: project/YAML roundtrips, colour boundaries, immutable Jinja with simulated HA helpers, original function mutator, dynamic menu and browser reload. Execution in an actual Home Assistant installation remains untested.

[Images and individual block descriptions](./blocks) · [Original field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) · [Custom Blockly blocks](https://developers.google.com/blockly/guides/create-custom-blocks/overview)
