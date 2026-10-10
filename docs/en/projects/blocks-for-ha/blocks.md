---
title: Block catalog
description: All UGSo Blocks for HA with images, functionality and original plugins.
---

# Block catalog

Since 0.1.17, entity fields open a search dialog. [Load, select and manually enter entities](./entities). The current catalog contains 148 types.

Version **0.1.39**: 148 block types. Images show actual UGSo editor blocks. Guides and ioBroker comparison: [Date and time](./time), [Conversion](./conversion). Dropdown variants do not count as additional types.

Triggers are orange, conditions purple, values green and actions blue. Side connections are typed; triggers and actions form separate vertical chains. Entity IDs are searched or entered manually.

## Colours and value functions since 0.1.15

[Usage, HA output and full source comparison](./blockly-audit).

| Block | Image | Function |
| --- | --- | --- |
| **Random colour**<br><code>ugso_colour_random</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_colour_random.png" alt="Random colour" style="max-width:280px;max-height:180px"> | Three random RGB channels in 0–255. New on each evaluation; not cryptographic. |
| **RGB colour**<br><code>ugso_colour_rgb</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_colour_rgb.png" alt="RGB colour" style="max-width:280px;max-height:180px"> | Clamp percentages to 0–100 and convert to RGB channels. 100/50/0 gives [255,128,0]. |
| **Blend colours**<br><code>ugso_colour_blend</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_colour_blend.png" alt="Blend colours" style="max-width:280px;max-height:180px"> | Linear RGB blend, 0–1 share of colour 2. Red/blue at 0.5 gives [128,0,128], without gamma correction. |
| **Define value function**<br><code>procedures_defreturn</code> | <img src="/assets/blocks-for-ha/blocks/en/procedures_defreturn.png" alt="Define value function" style="max-width:280px;max-height:180px"> | Original Blockly editor, cog for up to eight parameters, return required. No actions. Jinja expansion during export. |
| **Call value function**<br><code>procedures_callreturn</code> | <img src="/assets/blocks-for-ha/blocks/en/procedures_callreturn.png" alt="Call value function" style="max-width:280px;max-height:180px"> | Appears dynamically in Functions. Argument inputs follow parameters. Result as value or Boolean condition; no recursion. |
| **Original parameter getter**<br><code>variables_get</code> | <img src="/assets/blocks-for-ha/blocks/en/variables_get.png" alt="Original parameter getter" style="max-width:280px;max-height:180px"> | Original Blockly getter, e.g. from definition context menu. Reads parameters inside functions, HA variables otherwise. Own getter remains usable. |

## Math, text, lists and counting loops since 0.1.14

[Original Blockly / ioBroker / HA: mapping, examples and limitations](./collections).

| Block | Image | Function |
| --- | --- | --- |
| **Arithmetic**<br><code>ugso_math_arithmetic</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_arithmetic.png" alt="Arithmetic" style="max-width:280px;max-height:180px"> | Add, subtract, multiply, divide or raise to a power; numeric values required. |
| **Single-number math**<br><code>ugso_math_single</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_single.png" alt="Single-number math" style="max-width:280px;max-height:180px"> | Square root, absolute value, negation, natural/base-10 log and powers of e/10. |
| **Trigonometry**<br><code>ugso_math_trig</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_trig.png" alt="Trigonometry" style="max-width:280px;max-height:180px"> | sin/cos/tan use degrees; inverse functions return degrees. |
| **Constants**<br><code>ugso_math_constant</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_constant.png" alt="Constants" style="max-width:280px;max-height:180px"> | Pi, e, golden ratio, square root of 2 and of one half. |
| **Number property**<br><code>ugso_math_property</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_property.png" alt="Number property" style="max-width:280px;max-height:180px"> | Even, odd, whole, positive, negative or divisible by a nonzero divisor. |
| **Round**<br><code>ugso_math_round</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_round.png" alt="Round" style="max-width:280px;max-height:180px"> | Round normally/up/down to 0–10 decimal places. Half ties follow HA/Jinja even rounding. |
| **Math on list**<br><code>ugso_math_list</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_list.png" alt="Math on list" style="max-width:280px;max-height:180px"> | Sum, min, max, mean, median or random element; empty sum is 0, other empty results null. |
| **Modulo**<br><code>ugso_math_modulo</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_modulo.png" alt="Modulo" style="max-width:280px;max-height:180px"> | Remainder with Jinja rules; negative results may differ from JavaScript. |
| **Constrain**<br><code>ugso_math_clamp</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_clamp.png" alt="Constrain" style="max-width:280px;max-height:180px"> | Clamp between two limits; reversed limits are sorted. |
| **Random integer**<br><code>ugso_math_random_int</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_random_int.png" alt="Random integer" style="max-width:280px;max-height:180px"> | Inclusive integer limits, at most 10000 choices. |
| **Random fraction**<br><code>ugso_math_random_fraction</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_random_fraction.png" alt="Random fraction" style="max-width:280px;max-height:180px"> | 0 up to but excluding 1, in increments of 0.00001; evaluated anew each time. |
| **atan2 angle**<br><code>ugso_math_atan2</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_math_atan2.png" alt="atan2 angle" style="max-width:280px;max-height:180px"> | Additional Blockly standard operation; four-quadrant angle in degrees. |
| **Newline**<br><code>ugso_text_newline</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_newline.png" alt="Newline" style="max-width:280px;max-height:180px"> | Actual LF, CRLF or CR newline value. |
| **Join text**<br><code>ugso_text_join</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_join.png" alt="Join text" style="max-width:280px;max-height:180px"> | 0–100 inputs combined as text; gear or +/− controls the input count. |
| **Append text**<br><code>ugso_text_append</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_append.png" alt="Append text" style="max-width:280px;max-height:180px"> | Assign a new value to an already initialized text variable. |
| **Text length**<br><code>ugso_text_length</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_length.png" alt="Text length" style="max-width:280px;max-height:180px"> | Count Unicode code points rather than JavaScript UTF-16 units. |
| **Text empty**<br><code>ugso_text_empty</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_empty.png" alt="Text empty" style="max-width:280px;max-height:180px"> | Check whether text has length zero. |
| **Contains text**<br><code>ugso_text_contains</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_contains.png" alt="Contains text" style="max-width:280px;max-height:180px"> | Case-sensitive literal substring check. |
| **Find text**<br><code>ugso_text_index</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_index.png" alt="Find text" style="max-width:280px;max-height:180px"> | First/last position, counted from 1; missing result is 0. |
| **Get character**<br><code>ugso_text_char</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_char.png" alt="Get character" style="max-width:280px;max-height:180px"> | From start/end, first/last/random character; out of range returns empty text. |
| **Substring**<br><code>ugso_text_slice</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_slice.png" alt="Substring" style="max-width:280px;max-height:180px"> | Inclusive bounds, counted from 1; reversed/invalid bounds return empty text. |
| **Text case**<br><code>ugso_text_case</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_case.png" alt="Text case" style="max-width:280px;max-height:180px"> | Upper/lower/title case using Unicode rules. |
| **Trim text**<br><code>ugso_text_trim</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_trim.png" alt="Trim text" style="max-width:280px;max-height:180px"> | Remove leading/trailing/both whitespace, including tabs and newlines. |
| **Count text**<br><code>ugso_text_count</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_count.png" alt="Count text" style="max-width:280px;max-height:180px"> | Non-overlapping matches; empty search returns 0. |
| **Replace text**<br><code>ugso_text_replace</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_replace.png" alt="Replace text" style="max-width:280px;max-height:180px"> | Replace all literal matches; empty search leaves input unchanged. |
| **Reverse text**<br><code>ugso_text_reverse</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text_reverse.png" alt="Reverse text" style="max-width:280px;max-height:180px"> | Additional standard operation; reverses code points, not grapheme clusters. |
| **Repeat list item**<br><code>ugso_list_repeat</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_repeat.png" alt="Repeat list item" style="max-width:280px;max-height:180px"> | Create a list with 0–10000 repetitions. |
| **Find list item**<br><code>ugso_list_index</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_index.png" alt="Find list item" style="max-width:280px;max-height:180px"> | First/last occurrence, counted from 1; missing result is 0. Uses Python equality. |
| **Get list item**<br><code>ugso_list_get</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_get.png" alt="Get list item" style="max-width:280px;max-height:180px"> | From start/end, first/last/random item; out of range or empty returns null. |
| **Set/insert list item**<br><code>ugso_list_set</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_set.png" alt="Set/insert list item" style="max-width:280px;max-height:180px"> | Assign a new list value. Index starts at 1; insertion allows length+1. Invalid index leaves list unchanged. |
| **Remove list item**<br><code>ugso_list_remove</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_remove.png" alt="Remove list item" style="max-width:280px;max-height:180px"> | Assign a new list without the item at the 1-based index. Invalid index leaves list unchanged. |
| **Sublist**<br><code>ugso_list_slice</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_slice.png" alt="Sublist" style="max-width:280px;max-height:180px"> | Copy inclusive 1-based bounds; invalid/reversed bounds return an empty list. |
| **Split/join**<br><code>ugso_list_split</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_split.png" alt="Split/join" style="max-width:280px;max-height:180px"> | Split text by a literal delimiter or join list as text; empty delimiter splits code points. |
| **Sort list**<br><code>ugso_list_sort</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_sort.png" alt="Sort list" style="max-width:280px;max-height:180px"> | New numeric/text/case-insensitive sorted list, ascending/descending; numeric mode requires numbers. |
| **Reverse list**<br><code>ugso_list_reverse</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_reverse.png" alt="Reverse list" style="max-width:280px;max-height:180px"> | New reversed list; original stays unchanged. |
| **Count with variable**<br><code>ugso_for_range</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_for_range.png" alt="Count with variable" style="max-width:280px;max-height:180px"> | Fixed integer limits and nonzero step, ascending/descending, at most 10000 iterations; native HA repeat.for_each. |
| **For each with variable**<br><code>ugso_foreach_variable</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_foreach_variable.png" alt="For each with variable" style="max-width:280px;max-height:180px"> | Assign the named variable from repeat.item before each iteration body. |

## Flow, objects and lists added in 0.1.13

[ioBroker / original Blockly / native HA comparison and limitations](./flow).

| Block | Image | Function |
| --- | --- | --- |
| **Pause**<br><code>ugso_pause</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_pause.png" alt="Pause" style="max-width:280px;max-height:180px"> | Explicit duration unit, constant or runtime number. Native HA delay. |
| **Wait until**<br><code>ugso_wait</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_wait.png" alt="Wait until" style="max-width:280px;max-height:180px"> | Boolean condition with timeout and continuation checkbox; stops on timeout when unchecked. |
| **Stop this run**<br><code>ugso_stop</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_stop.png" alt="Stop this run" style="max-width:280px;max-height:180px"> | Reason and optional error checkbox. Ends the whole run, including outer loops. |
| **Repeat count**<br><code>ugso_repeat</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_repeat.png" alt="Repeat count" style="max-width:280px;max-height:180px"> | C-shaped body for HA repeat.count; repeat.index is the 1-based index. |
| **Repeat while/until**<br><code>ugso_repeat_while</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_repeat_while.png" alt="Repeat while/until" style="max-width:280px;max-height:180px"> | Boolean input and action body. While checks before; until after. Include a pause in the body. |
| **For each item**<br><code>ugso_foreach</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_foreach.png" alt="For each item" style="max-width:280px;max-height:180px"> | Iterate a list; current value through template repeat.item, index through repeat.index. |
| **New object**<br><code>ugso_object_new</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_new.png" alt="New object" style="max-width:280px;max-height:180px"> | 0–100 named attributes using gear/+−. Dictionary value, not an HA entity. |
| **Attribute of object**<br><code>ugso_object_get</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_get.png" alt="Attribute of object" style="max-width:280px;max-height:180px"> | Read a dictionary key; missing key returns null. Requires a dictionary. |
| **Object has attribute**<br><code>ugso_object_has</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_has.png" alt="Object has attribute" style="max-width:280px;max-height:180px"> | Boolean test for a dictionary key. |
| **Object attributes**<br><code>ugso_object_keys</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_keys.png" alt="Object attributes" style="max-width:280px;max-height:180px"> | Key list for list operations and for-each. |
| **Set attribute in variable**<br><code>ugso_object_set</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_set.png" alt="Set attribute in variable" style="max-width:280px;max-height:180px"> | Variable selector and value socket; assigns a dictionary copy with the changed key. Initialize as an object first. |
| **Remove attribute from variable**<br><code>ugso_object_remove</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_object_remove.png" alt="Remove attribute from variable" style="max-width:280px;max-height:180px"> | Reassigns without the key. Does not mutate other variables or entity attributes. |
| **Range comparison**<br><code>ugso_logic_range</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_logic_range.png" alt="Range comparison" style="max-width:280px;max-height:180px"> | Independent &lt; or ≤ for each bound; numbers and runtime numbers. |
| **Fallback value**<br><code>ugso_logic_default</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_logic_default.png" alt="Fallback value" style="max-width:280px;max-height:180px"> | Select null/undefined or empty/false/zero; null mode preserves valid zero and false. |
| **Case selection**<br><code>ugso_case</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_case.png" alt="Case selection" style="max-width:280px;max-height:180px"> | 1–100 cases using gear/+− and action bodies. First match wins; optional populated default body. |
| **Create list**<br><code>ugso_list_new</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_new.png" alt="Create list" style="max-width:280px;max-height:180px"> | 0–100 arbitrary items using gear/+−, including nested values. |
| **List length**<br><code>ugso_list_length</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_length.png" alt="List length" style="max-width:280px;max-height:180px"> | List length as a runtime number. Strings and dictionaries are not lists. |
| **List is empty**<br><code>ugso_list_empty</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_list_empty.png" alt="List is empty" style="max-width:280px;max-height:180px"> | Boolean test for a list with no items. |

## Conversion added in 0.1.12

[Guide, ioBroker comparison and pending JSONata](./conversion).

| Block | Image | Function |
| --- | --- | --- |
| **To number**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_number.png" alt="To number" style="max-width:280px;max-height:180px"> | HA float without fallback; complete numeric input with decimal point. Runtime number for variables, comparisons and time calculations. |
| **To Boolean**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_boolean.png" alt="To Boolean" style="max-width:280px;max-height:180px"> | HA bool for recognized Boolean/text values. Boolean output for conditions and logic. |
| **To string**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_string.png" alt="To string" style="max-width:280px;max-height:180px"> | Jinja text representation of a value; not JSON serialization. |
| **Type of**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_type.png" alt="Type of" style="max-width:280px;max-height:180px"> | HA typeof returns Python names such as str, float, bool, dict. HA 2023.4 or newer. |
| **To datetime**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_datetime.png" alt="To datetime" style="max-width:280px;max-height:180px"> | ISO text or Unix seconds/milliseconds to HA local datetime. Typed Time output. |
| **Datetime to …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_date_format.png" alt="Datetime to …" style="max-width:280px;max-height:180px"> | Datetime, formatted text, Unix number or date component. Selection changes output type; custom format shows a field. |
| **Format duration**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_duration.png" alt="Format duration" style="max-width:280px;max-height:180px"> | Duration in milliseconds or seconds to hh:mm:ss, hh:mm, mm:ss. Preserves sign and total hours/minutes. |
| **JSON to value**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_from_json.png" alt="JSON to value" style="max-width:280px;max-height:180px"> | JSON text to object, list or scalar. Invalid JSON causes an HA error. |
| **Value to JSON**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_convert_to_json.png" alt="Value to JSON" style="max-width:280px;max-height:180px"> | JSON serialization with indentation checkbox. Format datetimes first. |

## Date and time added in 0.1.11

Purple time blocks use a typed datetime socket. [Usage, boundary rules and comparison](./time).

| Block | Image | Function |
| --- | --- | --- |
| **Clock comparison**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_compare.png" alt="Clock comparison" style="max-width:280px;max-height:180px"> | Fixed HH:mm/HH:mm:ss; comparison or period. End field appears for between/outside. |
| **Clock comparison with inputs**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_compare_input.png" alt="Clock comparison with inputs" style="max-width:280px;max-height:180px"> | Text boundaries; uncheck current time to expose a datetime socket. Overnight periods supported. |
| **Current datetime**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_now.png" alt="Current datetime" style="max-width:280px;max-height:180px"> | HA local date, time and timezone. Typed Time output. |
| **Calendar start**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_boundary.png" alt="Calendar start" style="max-width:280px;max-height:180px"> | Start of today, tomorrow, week (Monday), month or year. |
| **Next sun event**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_sun.png" alt="Next sun event" style="max-width:280px;max-height:180px"> | Rise, set, dawn, dusk, solar noon or midnight from sun.sun, with minute offset. May be tomorrow. |
| **Shift datetime**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_shift.png" alt="Shift datetime" style="max-width:280px;max-height:180px"> | Datetime plus/minus number in milliseconds, seconds, minutes, hours or days. |
| **Format datetime**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_format.png" alt="Format datetime" style="max-width:280px;max-height:180px"> | Clock time, date, date/time, ISO with timezone or Unix seconds. |

## Other blocks

| Block | Editor image | Function |
| --- | --- | --- |
| **Automation**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_automation.png" alt="Automation" style="max-width:280px;max-height:180px"> | Root with triggers, optional condition and action chain. Name, ID, description and mode are edited outside the block. |
| **State reached**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_state_trigger.png" alt="State reached" style="max-width:280px;max-height:180px"> | Starts when the entity reaches the entered state. Generates `trigger: state` with `to`. |
| **Numeric threshold trigger**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_numeric_trigger.png" alt="Numeric threshold trigger" style="max-width:280px;max-height:180px"> | Starts on threshold crossing, not continuously. Number threshold; `trigger: numeric_state`. |
| **Time**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_time_trigger.png" alt="Time" style="max-width:280px;max-height:180px"> | Daily time trigger, HH:MM or HH:MM:SS; `trigger: time`. |
| **Sunrise/sunset**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_sun_trigger.png" alt="Sunrise/sunset" style="max-width:280px;max-height:180px"> | Sunrise or sunset dropdown; `trigger: sun`. |
| **HA starts**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_start_trigger.png" alt="HA starts" style="max-width:280px;max-height:180px"> | Starts when Home Assistant starts; `trigger: homeassistant`. |
| **State is**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_state_condition.png" alt="State is" style="max-width:280px;max-height:180px"> | Boolean condition: entity has the specified state; `condition: state`. |
| **Numeric condition**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_numeric_condition.png" alt="Numeric condition" style="max-width:280px;max-height:180px"> | Boolean above/below threshold condition; `condition: numeric_state`. |
| **AND / OR / NOT**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_logic_condition.png" alt="AND / OR / NOT" style="max-width:280px;max-height:180px"> | Combines 1–100 conditions. Plus/minus adds or removes the last input; gear reorders. `and`, `or`, `not`. |
| **Today’s date**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_date_condition.png" alt="Today’s date" style="max-width:280px;max-height:180px"> | Date picker with equals/on-or-after/on-or-before, including year. HA template compares today in HA’s time zone. Not a trigger. |
| **Number**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_number.png" alt="Number" style="max-width:280px;max-height:180px"> | General numeric value. Fits thresholds and delays; destination-specific validation still applies. |
| **Percentage**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_percent.png" alt="Percentage" style="max-width:280px;max-height:180px"> | Slider and exact input for integers 0–100. Number output, e.g. charge level or brightness. |
| **Multiline text**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_text.png" alt="Multiline text" style="max-width:280px;max-height:180px"> | String value for logs. Enter inserts a newline; Shift+Enter commits. Three visible lines; full text is retained. |
| **Colour**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_colour.png" alt="Colour" style="max-width:280px;max-height:180px"> | Hex colour picker; exports an RGB list to lights, variables or colour calculations. Colour/Value output; fixed numeric inputs remain incompatible. |
| **On / off / toggle**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_switch_action.png" alt="On / off / toggle" style="max-width:280px;max-height:180px"> | Entity-domain action: `turn_on`, `turn_off` or `toggle`. Entity must support the action. |
| **Generic HA action**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_service_action.png" alt="Generic HA action" style="max-width:280px;max-height:180px"> | Action name, optional single entity target, JSON object data. Supports parameters not exposed by dedicated blocks. |
| **Wait seconds**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_delay_action.png" alt="Wait seconds" style="max-width:280px;max-height:180px"> | Delay of 0–86400 integer seconds. Number input with shadow default. |
| **If / else if / else**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_if_action.png" alt="If / else if / else" style="max-width:280px;max-height:180px"> | Plus/minus adds or removes the last else-if branch; S toggles else. Gear reorders. `if` or `choose`, first matching branch. |
| **Log output**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_log_action.png" alt="Log output" style="max-width:280px;max-height:180px"> | Text message and severity dropdown; `system_log.write`. HA may filter Info/Debug. |
| **Control HA script**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_script_action.png" alt="Control HA script" style="max-width:280px;max-height:180px"> | Start without waiting, stop, or call and wait. `script.turn_on`, `script.turn_off` or `script.name`. |
| **Refresh entity**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_update_action.png" alt="Refresh entity" style="max-width:280px;max-height:180px"> | `homeassistant.update_entity` requests a refresh. Does not set state; support depends on integration. |
| **Control helper**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_helper_action.png" alt="Control helper" style="max-width:280px;max-height:180px"> | Switch/counter/timer type controls the action dropdown. Entity ID must match. Timer uses configured duration; parameters use generic action. |
| **Light with colour**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_colour_action.png" alt="Light with colour" style="max-width:280px;max-height:180px"> | Light entity, Colour input and brightness 0–100. Generates `light.turn_on` with `rgb_color` and `brightness_pct`. Device must support colours. |

Minus or disabling else detaches connected blocks instead of deleting them. Reconnect or remove them before YAML export. Undo restores inputs and connections. Shadow values reappear when a replacement value block is removed.

## Variable and template blocks added in 0.1.8

| Block | Editor image | Function |
| --- | --- | --- |
| **Set variable**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_variable_set.png" alt="Set variable" style="max-width:280px;max-height:180px"> | Action block: assign a number, text/template, Boolean or null to the selected variable. Generates native HA `variables`. Place before subsequent reads. |
| **Read variable**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_variable_get.png" alt="Read variable" style="max-width:280px;max-height:180px"> | Side String connector; generates <code v-pre>{{ name }}</code> for log messages and further assignments. Dropdown supports rename/delete. |
| **Template value**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_template.png" alt="Template value" style="max-width:280px;max-height:180px"> | Multiline Jinja template with String connector for log messages or variable assignments. HA evaluates the template during execution; Blocks does not execute it. |
| **Template condition**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_template_condition.png" alt="Template condition" style="max-width:280px;max-height:180px"> | Boolean connector for Only if, If and logical groups. Generates `condition: template` with `value_template`. HA must evaluate it as true; not a trigger. |

## Using variables and templates

### Increment and decrement added in 0.1.10

| Block | Editor image | Function |
| --- | --- | --- |
| **Change variable by …**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_variable_change.png" alt="Change variable by" style="max-width:280px;max-height:180px"> | Variable dropdown and Number input with default step `1`. Adds the step to a previously assigned numeric variable. Negative steps decrease; `0` and fractional steps are supported. Native HA variable assignment using Jinja. |

The **Variablen** menu dynamically offers **Set**, **Change by** and **Read** for each created variable. Example action chain: **Set test to 10 → Change test by 1 → Log Info message Read test**. The message then uses `11`; a step of `-2` changes `10` to `8`.

Assign a number before incrementing. Undefined variables, text (including `"10"`), Boolean and null are not automatically converted or initialized as `0`; Jinja evaluation in HA fails for those values. Creating a variable alone does not assign it. JSON retains the increment block; importing our exact YAML output recreates it. Other calculation templates remain template blocks. The planned typed-variable dialog is still pending.

Choose **Variablen → Variable erstellen …** in the German editor to create, for example, `leistung`. Names use ASCII letters, digits and `_`, with no leading digit. Place Set variable in **Dann** and connect a number or template. Connect Read variable to a subsequent log message. Creating a name alone does not assign a value. Variables belong to the HA automation run; they are not persistent helpers.

Example: **Set leistung to Template** containing <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>, followed by **Log Info message Read leistung**. HA reads the sensor during assignment and uses that value in the next step. A template condition can check <code v-pre>{{ states('sensor.leistung') | float(0) > 100 }}</code>.

Renaming updates variable blocks. References in free-form Jinja text must be changed manually. Action variables become available after assignment, not in preceding automation conditions. Blocks validates structure and YAML, not Jinja syntax or HA entities. Import supports text/template, number, Boolean or null for each variable value. Multiple entries are supported since 0.1.34 in the grouped JSON block; list/object values and automation-level variables remain rejected. [Native HA variables and scope](https://www.home-assistant.io/docs/scripts/#define-variables).

## Logic blocks added in 0.1.9

| Block | Editor image | Function |
| --- | --- | --- |
| **Compare**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_compare.png" alt="Compare" style="max-width:280px;max-height:180px"> | Compares two values using =, ≠, &lt;, ≤, &gt; or ≥. Accepts numbers, text, variables and single template expressions. Boolean result exported as an HA template condition or variable value. |
| **Compact AND / OR**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_binary_logic.png" alt="Compact AND OR" style="max-width:280px;max-height:180px"> | Two Boolean inputs. Generates native HA `and`/`or` groups as conditions and parenthesized Jinja as variable values. Expandable groups remain available. |
| **NOT**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_not.png" alt="NOT" style="max-width:280px;max-height:180px"> | Negates a Boolean condition. Native HA `not` group as condition, Jinja `not` as variable value. |
| **true / false**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_boolean.png" alt="true false" style="max-width:280px;max-height:180px"> | Boolean constant with dropdown for conditions and variables. Assignments retain native YAML Boolean types. |
| **null**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_null.png" alt="null" style="max-width:280px;max-height:180px"> | No value: YAML `null` in assignments, Jinja `none` in expressions. Different from `0` and `false`; not a Boolean condition. |
| **If → value → otherwise value**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ternary.png" alt="Conditional value" style="max-width:280px;max-height:180px"> | Selects one of two values using a Boolean condition. For variables, log messages and comparisons; generates a Jinja expression, not an action sequence. |

**Example:** Assign `leistung` first. Then use **Set meldung to If**, with **Compare Variable leistung &gt; Number 100** as test, text **High power** as true value and **Low power** as false value. Follow with **Log Info message Variable meldung**. HA evaluates the choice during execution.

Comparisons do not automatically convert types: number `20` differs from text `"20"`. Convert sensor states with `float` or `int` where appropriate. Expression inputs accept a single Jinja output, for example <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>. Multiline statements and mixed text remain supported in standalone template value blocks. Dynamic choices are not supported as fixed numeric thresholds or delays.

JSON projects preserve block shapes and connections. YAML preserves native meaning: reopening maps comparisons and value choices to template blocks and AND/OR/NOT to condition groups. [HA logical conditions](https://www.home-assistant.io/docs/scripts/conditions/#logical-conditions).

## Original plugins and integration

The six existing plugins are pinned to **13.2.0**, the four theme/zoom plugins and workspace search to **13.3.0**, all bundled locally with Blockly **13.3.0**. License: Apache-2.0. Links below lead directly to upstream repositories. HA blocks, YAML adapters and plus/minus controls are UGSo code.

| Originalplugin | Usage / status |
| --- | --- |
| [workspace-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/workspace-search) | Finds placed blocks in the workspace; separate from toolbox search. Available since 0.1.21. |
| [toolbox-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) | Search at the bottom of the menu, German search hints; results preserve dropdowns and shadows. |
| [field-multilineinput](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) | Used by Text; newlines remain in projects and YAML. |
| [field-slider](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) | Used by Percentage; 0–100 with exact numeric entry. |
| [field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) | Used by Colour; converts hex to RGB for lights. Random/RGB/blend use own HA generators since 0.1.15. |
| [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) | Dark workspace/flyout, part of the saved theme selector. |
| [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) | Original palette with stronger borders; own blocks use theme styles. |
| [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) | Original standard-group palette, matching UGSo extension colours and adaptive label contrast. |
| [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) | Additional fit control next to zoom controls; keyboard accessible. |
| [field-date](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) | Used by date comparison; UGSo subclass guards the deferred picker call. |
| [field-dependent-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) | Used by Helper; type determines actions. No live HA selection. |
| [block-plus-minus](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-plus-minus) | Interaction implemented in our HA blocks; original plugin is not installed. Gear remains available. |
| [block-dynamic-connection](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-dynamic-connection) | Not integrated yet. Automatic growing connections, text joining and lists are planned. |

The colour field also uses the transitive dependency [field-grid-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-grid-dropdown). HA output is generated by our adapters; bundled JavaScript generators are not used.

[Back to overview](/en/projects/blocks-for-ha/)

Custom blocks since 0.1.18 extend the 148 native types. [Editor](./custom-blocks) and [package catalog](./catalog/).

## Trigger IDs and multiple targets

Since **0.1.28**: **States as JSON list**, e.g. `["1_single","1_double"]`; optional trigger IDs on every standard trigger; **Triggered by ID** as a native trigger condition (single ID or JSON list). Generic HA actions support **Targets as JSON list**, optional metadata and explicitly preserved empty data objects. Four-button automations with four `choose` branches can be fully imported.

**Single automation · HA editor** output omits the top-level `id`. Trigger IDs remain. Projects and **automations.yaml list** output retain an existing automation ID.

| Block | Image | Description |
| --- | --- | --- |
| **Triggered by ID**<br><code>ugso_trigger_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_trigger_condition.png" alt="Triggered by ID" style="max-width:280px;max-height:180px"> | `condition: trigger` · `id` |

[Home Assistant: Trigger IDs](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Trigger condition](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

## Pool pumps, events and multiple times

Since **0.1.30**: enable **Times as JSON list** for several fixed times, e.g. `["10:00:00","13:00:00","19:00:00"]`. **Any change** omits `to`; **Entities as JSON list** watches multiple entities. Without `to`, HA also reacts to attribute changes. Event triggers support e.g. `timer.finished` with an optional JSON data filter. Native time conditions preserve `before`/`after`: fixed times, after inclusive and before exclusive, including overnight windows. Equal bounds mean all day. Time helpers, time templates and weekday filters remain outside the supported import. The full pool-pump automation retains multiline timer templates and nested `choose` branches.

| Block | Image | Description |
| --- | --- | --- |
| **Event trigger**<br><code>ugso_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_event_trigger.png" alt="Event trigger" style="max-width:280px;max-height:180px"> | `trigger: event` · `event_type` · `event_data` |
| **Native HA time condition**<br><code>ugso_native_time_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_native_time_condition.png" alt="Native HA time condition" style="max-width:280px;max-height:180px"> | `condition: time` · `before` · `after` |

[Home Assistant: triggers](https://www.home-assistant.io/docs/automation/trigger/) · [Time condition](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

## Temperature changed

Since **0.1.31**, the new block supports native temperature.changed. Target (JSON): entity_id string or list. Threshold (JSON): type any, above, below, between or outside. any requires only type; above/below require value, between/outside value_min and value_max. Numbers: number plus unit_of_measurement (°C/°F). References: entity (sensor, number or input_number). Optional trigger ID. Since 0.1.39, area, device, floor and label targets are supported. MQTT topics, qos/retain/evaluate_payload and multiline JSON/Jinja payloads are preserved.

| Block | Image | Description |
| --- | --- | --- |
| **Temperature changed**<br><code>ugso_temperature_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_temperature_trigger.png" alt="Temperature changed" style="max-width:280px;max-height:180px"> | temperature.changed |

[Home Assistant: temperature.changed](https://www.home-assistant.io/triggers/temperature.changed/)

## Calendars and response variables

**0.1.32:** `calendar.event_started` / `calendar.event_ended`. Target: JSON object with `entity_id` as text or a list. Options are optional: `offset` with combined days, hours, minutes and seconds or `HH:MM:SS`; `offset_type` is `before` or `after`. Zero offsets, omitted options and optional trigger IDs are retained.

The **Response variable (optional)** field in **HA action** generates `response_variable`, for example `termine` for `calendar.get_events`. An empty field omits it from YAML. The full holiday automation retains both calendars, HA startup, zeitpunkt/termin_aktiv variables, multiline Jinja templates, choose/default and queued mode. Home Assistant processes calendars and templates.

| Block | Image | Function |
| --- | --- | --- |
| **Calendar event starts/ends**<br><code>ugso_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_calendar_trigger.png" alt="Calendar event starts/ends" style="max-width:280px;max-height:180px"> | calendar.event_started / calendar.event_ended |

[Home Assistant: calendar.event_started](https://www.home-assistant.io/triggers/calendar.event_started/) · [calendar.event_ended](https://www.home-assistant.io/triggers/calendar.event_ended/) · [calendar.get_events](https://www.home-assistant.io/actions/calendar.get_events/)

## Numeric triggers with hold duration

Since **0.1.33**, **Number above/below threshold** accepts multiple entities: enable **Entities as JSON list** and enter, for example, `["sensor.temp_1","sensor.temp_2"]`. Without the checkbox, the single entity remains active. **Hold duration (JSON)** with **enabled** generates optional `for`: for example `{"hours":0,"minutes":1,"seconds":0}`, `60` or `"00:01:00"`. Combined days/hours/minutes/seconds/milliseconds, zero entries and HA output templates are retained. Disabling the checkbox omits `for`. Still exactly one fixed numeric threshold (above or below); trigger IDs and choose branches are preserved.

Home Assistant fires after a threshold crossing once the value has remained on that side of the threshold for the whole duration. Restarting HA or reloading automations resets a running hold timer. [Home Assistant: numeric_state](https://www.home-assistant.io/triggers/numeric_state/).

## Multiple variables in one action

Since **0.1.34**, the **Variables** menu includes **Set variables (JSON)**. The JSON object contains 1–100 variable names with text, HA template, number, Boolean or null values. Multiple entries remain a single native `variables` action, including their order. Single assignments still use the existing Set block. Since 0.1.39, list/object values and automation-level variables are supported; see [Extended HA and Jinja](./advanced). Edit names and templates directly in JSON; the Blockly rename dialog does not change this free-form JSON text. Imported names are also registered in Blockly.

The timer example retains h/m, both watched entities, the condition and restart mode. Omitted conditions become an empty list.

| Block | Image | Function |
| --- | --- | --- |
| **Set variables (JSON)**<br><code>ugso_variables_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_variables_action.png" alt="Set variables (JSON)" style="max-width:280px;max-height:180px"> | Native HA variables as a JSON object. |

[Home Assistant: variables](https://www.home-assistant.io/docs/scripts/#variables)

## Delay as duration text or template

Since **0.1.35**, Blocks imports native `delay` duration strings into the new block under **Timeouts**. Examples: `00:00:02`, `01:30` (one hour and 30 minutes), `00:00:00.250` or an HA output template. The duration remains a string in YAML and the saved project. The current HA run waits before continuing with subsequent actions. Existing seconds and unit blocks remain available. This extension applies to `delay`, not the wait-until block timeout.

The timer-reset example first turns off timer_reset, waits two seconds and then turns off both targets. The entity ID input_boolean.timer_runing is preserved exactly as provided.

| Block | Image | Function |
| --- | --- | --- |
| **Wait duration text / template**<br><code>ugso_delay_text</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_delay_text.png" alt="Wait duration text / template" style="max-width:280px;max-height:180px"> | Native delay duration string / HA template. |

[Home Assistant: delay](https://www.home-assistant.io/docs/scripts/#wait-for-time-to-pass-delay)

## Dynamic HA action names

Since **0.1.36**, the first field in **HA action** accepts a static action name or a Jinja template. The field supports multiline editing. Examples: `input_boolean.turn_on`, `input_boolean.turn_` followed by a Jinja expression, or a full if/else template. Target, data, metadata and response variable retain their existing fields. Templates and line breaks survive import, project storage and YAML export.

The Shelly example retains the action prefix `input_boolean.turn_` combined with the state lookup and the nested choose branches. Home Assistant evaluates the action name at runtime; it must then resolve to an available service name. Blocks checks static names and template delimiters, not Jinja syntax or runtime results. Target entities must still be fixed IDs; templating the entire data object is outside this extension.

[Home Assistant: choosing the action with a template](https://www.home-assistant.io/docs/scripts/perform-actions/#choosing-the-action-with-a-template)


## Time pattern trigger

Since **0.1.37**, **Triggers** includes a native `time_pattern` block. Its JSON field can contain `{"seconds":"/30"}` to match seconds 0 and 30 of each minute. Optional keys are `hours`, `minutes` and `seconds`; at least one is required. Fixed values: hours 0–23, minutes/seconds 0–59, as numbers or strings without leading zeroes. `*` matches every value; `/n` matches values divisible by n (n > 0 within the field range). Omitted units and number/string types remain unchanged; Home Assistant applies its runtime defaults. An optional trigger ID is supported.

The LCD automation with four `input_text.set_value` actions and `mode: restart` passes full round-trip checks: Jinja, formatting, slicing, padding and line breaks are preserved. Home Assistant executes the templates and schedule.

| Block | Type |
| --- | --- |
| ![Time pattern (JSON)](/assets/blocks-for-ha/blocks/en/ugso_time_pattern_trigger.png) | `ugso_time_pattern_trigger` |

[Home Assistant: time_pattern](https://www.home-assistant.io/triggers/time_pattern/).


## Dynamic target entities

Since **0.1.39**, **Target** in the generic **HA action** accepts a static entity ID or an HA template, such as `{{ ziel_tv }}`. Its entity dialog supports multiline input. The JSON target list can also combine static IDs and templates. Jinja remains unchanged and is evaluated by Home Assistant at execution time. Imported dynamic targets use the generic HA action because specialized switching blocks cannot reliably determine the domain.

The bedroom-TV automation with a multiline summer-mode variable, 21:30 and 00:30 triggers and two choose branches is verified. Target templates, variable text and time conditions survive import, project reload and export. Entity fields in triggers and conditions still require static IDs.

[Home Assistant: templates in action targets](https://www.home-assistant.io/docs/scripts/perform-actions/#setting-targets-and-options-with-a-template).


## Extended HA and Jinja since 0.1.39

[Anleitung / Guide](./advanced).

| Block | Image | Function |
| --- | --- | --- |
| **HA state**<br><code>ugso_ha_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_state_trigger.png" alt="HA state" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA numeric_state**<br><code>ugso_ha_numeric_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_numeric_state_trigger.png" alt="HA numeric_state" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA time**<br><code>ugso_ha_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_time_trigger.png" alt="HA time" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA sun**<br><code>ugso_ha_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_sun_trigger.png" alt="HA sun" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA homeassistant**<br><code>ugso_ha_homeassistant_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_homeassistant_trigger.png" alt="HA homeassistant" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA mqtt**<br><code>ugso_ha_mqtt_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_mqtt_trigger.png" alt="HA mqtt" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA template**<br><code>ugso_ha_template_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_template_trigger.png" alt="HA template" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA webhook**<br><code>ugso_ha_webhook_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_webhook_trigger.png" alt="HA webhook" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA zone**<br><code>ugso_ha_zone_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_zone_trigger.png" alt="HA zone" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA device**<br><code>ugso_ha_device_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_device_trigger.png" alt="HA device" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA tag**<br><code>ugso_ha_tag_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_tag_trigger.png" alt="HA tag" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA conversation**<br><code>ugso_ha_conversation_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_conversation_trigger.png" alt="HA conversation" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA geo_location**<br><code>ugso_ha_geo_location_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_geo_location_trigger.png" alt="HA geo_location" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA calendar**<br><code>ugso_ha_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_calendar_trigger.png" alt="HA calendar" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA event**<br><code>ugso_ha_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_event_trigger.png" alt="HA event" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA trigger (extended)**<br><code>ugso_ha_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_trigger.png" alt="HA trigger (extended)" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA condition (extended)**<br><code>ugso_ha_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_condition.png" alt="HA condition (extended)" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA step (extended)**<br><code>ugso_ha_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_ha_action.png" alt="HA step (extended)" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA action target type target data step options**<br><code>ugso_target_action</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_target_action.png" alt="HA action target type target data step options" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **HA integration target options enabled**<br><code>ugso_integration_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_integration_trigger.png" alt="HA integration target options enabled" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Action group**<br><code>ugso_sequence</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_sequence.png" alt="Action group" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Parallel branch 1 branch 2**<br><code>ugso_parallel</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_parallel.png" alt="Parallel branch 1 branch 2" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Wait for trigger options**<br><code>ugso_wait_trigger</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_wait_trigger.png" alt="Wait for trigger options" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Continue only if**<br><code>ugso_condition_step</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_condition_step.png" alt="Continue only if" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Fire event data**<br><code>ugso_fire_event</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_fire_event.png" alt="Fire event data" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Assist responds**<br><code>ugso_assist_response</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_assist_response.png" alt="Assist responds" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Activate scene**<br><code>ugso_scene</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_scene.png" alt="Activate scene" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Jinja (experimental)**<br><code>ugso_jinja_value</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_jinja_value.png" alt="Jinja (experimental)" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
| **Jinja condition (experimental)**<br><code>ugso_jinja_condition</code> | <img src="/assets/blocks-for-ha/blocks/en/ugso_jinja_condition.png" alt="Jinja condition (experimental)" style="max-width:280px;max-height:180px"> | Extended HA fields or original Jinja. Supported structure is checked; verify integration and execution in HA. |
