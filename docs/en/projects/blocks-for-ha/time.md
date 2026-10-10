---
title: Date and time
description: Time blocks, HA timezone and ioBroker comparison.
---
# Date and time

Since **0.1.11**, the category includes seven additional blocks. [All blocks with images](./blocks#date-and-time-added-in-0-1-11). The editor uses the original Blockly library; HA Jinja generation is an original UGSo implementation. References: [ioBroker JavaScript adapter time blocks](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_time.ts) and [Blockly block definitions](https://docs.blockly.com/guides/create-custom-blocks/define/block-definitions/).

## ioBroker / UGSo Blocks for HA

| ioBroker | Our block / implementation |
| --- | --- |
| Current time comparison with fixed clock time | **Clock comparison**: less, less/equal, greater, greater/equal, equal, between and outside. End field appears for periods. |
| Current time checkbox and plugged-in value | **Clock comparison with inputs**: text blocks for start/end. Uncheck current time to expose a datetime socket. |
| Current time as Date object or formatted value | **Current datetime** plus separate **formatter**, preventing formatted text from entering datetime calculations. |
| Calculated time | **Calendar start**: today, tomorrow, week (Monday), month and year. Other ioBroker calendar boundaries are not implemented yet. |
| Astro event time with offset | **Next sun event**: rise, set, dawn, dusk, solar noon and midnight, with positive/negative minute offset. |
| Calculate time, base ± number and unit | **Shift datetime**: datetime ± number; milliseconds, seconds, minutes, hours or days. |

## Connections and use

Comparisons return **Boolean**, fitting conditions, AND/OR/NOT and If. Datetimes have a typed **Time connection**: current time, calendar start, sun event and time calculation can nest. Numeric blocks supply offset/amount; formatted clock text supplies comparison boundaries. Formatting supports HH:mm, HH:mm:ss, ISO date, German date, date/time, ISO with timezone and Unix seconds.

Example: **Current datetime → Shift datetime (+ 30 minutes) → Format (HH:mm)**, then assign to a variable:

```jinja
{{ (now() + timedelta(minutes=30)).strftime("%H:%M") }}
```

**Between 22:00 and 06:00** includes the overnight period. Start is included, end excluded. Equal boundaries describe an empty period; outside is its complement. Fixed clock times must be HH:mm or HH:mm:ss. Dynamic text boundaries must provide the same format at runtime; invalid values cause an HA template error. Comparison has second precision: equal 12:00 means 12:00:00 and is not a reliable time trigger.

## Execution and limitations

Templates execute **in Home Assistant**. The browser builds YAML and does not run a scheduling engine. Functions use HA's configured timezone: [HA date/time functions](https://www.home-assistant.io/template-functions/#date-time). Calendar starts use local midnight; day arithmetic follows the local calendar, including DST changes. Adding 24 hours does not guarantee 24 elapsed UTC hours across a timezone transition.

Sun values come from [HA Sun integration attributes](https://www.home-assistant.io/integrations/sun/#sensors). They represent the **next event**, which may be tomorrow. UTC values are converted to HA local time before calculation/formatting. Missing values, such as an unavailable integration or uncomputable event, cause a template error rather than a fabricated fallback time.

A comparison checks the clock **when its condition is evaluated**. It does not start the automation or wait for the target time. Use a time or sun trigger for that. The new sun value block does not replace a sun trigger.

**Blocks project JSON** preserves block shapes, selections and dynamic sockets. **Opening YAML** retains the time templates but displays them as general template blocks. A datetime previously assigned to an HA variable may become text; our variable getter therefore has no Time connection. Nest datetime blocks directly or, since **0.1.12**, connect the getter through **To datetime**. [Conversion and units](./conversion). Converted runtime numbers now also fit datetime amounts and sun offsets.

Verification covers Blockly/YAML roundtrips, typed connections, dynamic fields and Jinja checks for overnight boundaries and DST. Execution on a real HA system has not been verified.
