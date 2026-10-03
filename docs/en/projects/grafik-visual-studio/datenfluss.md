---
title: Data flow – values, conversion and calculation
---

# HA Grafik – Data flow

From Studio **0.1.141**, the dedicated **HA Grafik – Data flow** palette contains three widgets. Calculations and conversions run in the browser on each display computer. Home Assistant supplies entity values; internal processing requires no additional HA entities. The visualization must remain open.

| Widget | Editor | Runtime |
| --- | --- | --- |
| **Value connection** | Simple SVG line without animation, directed from start to destination | Invisible; continues passing values |
| **Value converter** | Widget and dedicated radio-button dialog with input/output types and preview | Always invisible; conversion remains active |
| **Value calculation** | Same editor as [SVG LineBox Math](./svg-linebox-math), with four calculations and ports A–P | Invisible by default; calculations and outputs remain active |

Value connection and Value calculation internally reuse the SVG-Line and SVG-LineBox-Math types, preserving docking, movement, copying, project import/export and shared calculation logic. SVG LineBox Math also supports **Hide in runtime**. Disable this option on Value calculation if you want to display its calculation widget.

## Connecting a source

From **0.1.143**, new Data flow widgets start with all CSS groups disabled; Value calculation also disables **Display** by default. Calculation and conversion remain enabled. Enable these groups when needed; disabled CSS fields are omitted from exports. New Value connections have no arrowheads at either end. Previously saved widgets retain their settings.

1. On a widget with an entity or preview value, enable **Enable output point** under **Data flow**. Use the **Top**, **Bottom**, **Right** or **Left** radio buttons to select the center of that edge; right is the default. This single output works independently of **Docking points** and can be disabled. Set its separate color under **Settings → Output point**. The point is visible only in the editor; forwarding stays active in runtime. Widgets without an available value, such as plain borders, provide no value. Existing docking configurations are preserved; LineBox, LineBox Math and converters continue using their own ports.
2. Add a **Value connection**: start at the source output and end at the converter or receiver input. Values always follow this direction, even without visible arrowheads; animation is disabled.
3. Open **Edit conversion**, select the converter's input and output, and enable **Enable selected input/output docking points**. New ports remain disabled until explicitly enabled.
4. Choose a conversion and check the preview. For a regular receiver, enable **Receive value from data flow** and its input port. Number can alternatively use its existing numeric docking input, which continues summing multiple numeric values.

A converter and general data-flow input accept **exactly one source per input**. Multiple outgoing connections can distribute a result to different receivers. The converter does not sum strings or switch states. LineBox Math retains its own summation of multiple numeric connections.

## Converter dialog

![Converter dialog with radio buttons and preview for temperature text to number](/images/grafik-visual-studio/dataflow-converter-dialog.png)

| Conversion | Settings and output |
| --- | --- |
| Number → text | 0–10 decimal places, decimal point/comma, optional unit |
| Text → number | Recognize decimal points/commas and trailing units; output a number |
| Switch state → number | On → 1, off → 0; optional inversion |
| Number → switch state | On when value ≥ threshold, otherwise off; optional inversion |
| Switch state → text | Custom on/off text; optional inversion |
| Normalize switch state | Accept `on/off`, `true/false` or `1/0`; output real Booleans, numbers or `on/off` text |
| Scale number | `value * factor + offset`, optional target unit; e.g. °C → °F using factor 1.8 and offset 32 |

Switch-state parsing ignores case and surrounding whitespace. Unknown states are reported. Only settings relevant to the selected conversion are shown. Changes apply after **Apply** and support Undo.

## Units and errors

`23,5 °C` splits into numeric value **23.5** and unit **°C**. A plain value uses HA's `unit_of_measurement` metadata or the widget unit. If neither exists, configure a fallback unit. A unit already present in the text takes precedence and is never appended twice. **Include unit in text** is optional. Unit recognition alone does not perform conversion; explicitly select **Scale number** and configure factor, offset and target unit.

Empty values, `unknown`, `unavailable`, invalid numbers, unknown switch states, inactive inputs, multiple sources and feedback cycles produce errors. No value is output by default. **Enable fallback on error** starts disabled; enabling it outputs the configured fallback text, without automatically converting that text into a number or Boolean.

Example: temperature display `23,5 °C` → **Text → number** converter → Value calculation `A * 2` → Number **47.0**. Runtime shows only the temperature display and Number. Results are passed internally and are not automatically stored in Home Assistant. The current basic threshold has no hysteresis and switches directly at its boundary.
