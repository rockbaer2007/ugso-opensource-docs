---
title: Conversion
description: Value conversion, datetime and JSON with ioBroker comparison.
---
# Conversion

Since **0.1.12**, the category includes nine new blocks. [Conversion blocks with images](./blocks#conversion-added-in-0-1-12). The UI reference is [ioBroker conversion blocks](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_convert.ts). We use the original Blockly library with an original UGSo generator for HA Jinja. Values are converted when the automation runs in Home Assistant.

## ioBroker / UGSo Blocks for HA

| ioBroker | Our block | Behavior / difference |
| --- | --- | --- |
| to number | **To number** | HA `float`: complete numeric values. `21.5` works; `21W` and decimal commas do not. Does not extract numeric prefixes like `parseFloat`. |
| to Boolean | **To Boolean** | HA `bool`: Boolean or recognized values such as true/false, on/off, yes/no and 1/0. Unknown strings are not automatically true. |
| to string | **To string** | Jinja text representation. Boolean becomes `True`/`False`; objects do not receive guaranteed JSON syntax. |
| type of | **Type of** | HA `typeof`, available since HA 2023.4. Python type names such as str, int, float, bool, dict, list and NoneType rather than JavaScript names. |
| to datetime | **To datetime** | ISO text or explicitly selected Unix seconds/milliseconds → datetime in HA local time. Use ISO with Z or a timezone offset. |
| datetime to … | **Datetime to …** | Datetime, ISO/clock/date, Unix number, year/month/day/hour/minute/second/millisecond, weekday, ISO week or time since midnight. Custom format exposes an extra field. |
| format time difference | **Format duration** | Numeric milliseconds (default) or seconds. hh:mm:ss, hh:mm, mm:ss. Preserves negative signs and total hours/minutes above 24/60. |
| JSON to object | **JSON to value** | `from_json`, including arrays and scalar values. Invalid JSON causes a template error rather than an empty fallback object. |
| object to JSON, pretty print | **Value to JSON, pretty print** | `to_json` with indentation checkbox. JSON-serializable values only; convert datetimes to ISO or Unix numbers first. |
| apply JSONata expression | **Pending** | No JSONata runtime adapter in the editor. General HA templates can already contain Jinja object/list access. A real JSONata integration must also exist when HA runs the automation. |

HA behavior references: [float](https://www.home-assistant.io/template-functions/float/), [bool](https://www.home-assistant.io/template-functions/bool/), [typeof](https://www.home-assistant.io/template-functions/typeof/), [from_json](https://www.home-assistant.io/template-functions/from_json/), [to_json](https://www.home-assistant.io/template-functions/to_json/).

## Connections and format fields

Boolean fits conditions and logic. Converted numbers are **runtime numbers**: usable in value comparisons, variables, duration formatting and time block amounts/offsets. Fixed numeric-state thresholds, delays and increment steps still require constant Number blocks, so runtime numbers cannot accidentally dock there. Dynamic HA configuration for those fields is not implemented yet.

Datetimes use the Time connection. **Datetime to …** changes its output type according to the selected format: datetime, runtime number or string. Custom formatting uses Python `strftime` with `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`. ioBroker codes such as `YYYY` are not interchangeable. Localized month/weekday names, other duration formats and custom duration masks are not implemented yet. Weekdays use Monday=1 to Sunday=7; week numbers follow ISO. Fractional duration seconds are truncated rather than rounded.

## Examples

Sensor text → number → compare with 20. A template value reading a sensor feeds To number and a comparison:

```jinja
{{ (float((states('sensor.temperatur'))) > 20) }}
```

JSON text → JSON to value → Value to JSON (pretty print):

```jinja
{{ (('{"wert":21.5}' | from_json) | to_json(pretty_print=true)) }}
```

`3661000` milliseconds formats as `01:01:01`; `-3661000` as `-01:01:01`. Select milliseconds or seconds explicitly. The duration block formats an existing numeric duration; it does not automatically subtract two datetimes.

## Errors, persistence and planned extension

No silent defaults are assigned for invalid numbers, Boolean values or JSON. Specify an intentional fallback in a general HA template when needed. HA variables can interpret template results as native values; a String connection is editor type information, not a guarantee against HA's own result type interpretation.

JSON projects retain block shapes, checkboxes and custom formats. Opening YAML preserves these expressions as general template blocks. Conversions in variable actions can produce runtime objects/arrays; importing raw object/array variable assignments in YAML is still unsupported. The generic HA action currently accepts static JSON data; conversion blocks cannot plug directly into those action data yet.

**Planned:** extend object/list access, then evaluate an optional JSONata runtime adapter. Browser-only evaluation would not reproduce an automation's later execution in HA.

Verification covers Blockly/YAML roundtrips, connections and Jinja execution with mocked HA helper contracts. Execution on a real HA system has not been verified.
