---
title: SVG LineBox – collect and pass line values
---

# SVG LineBox

From Studio 0.1.136, the output line also offers an automatic SVG LineBox divisor with its own target speed (0.05–5 cycles/s, default 1). This keeps motion adjustable even for large sums. This option is independent of numeric-entity divisor automation; see [SVG-Line](./svg-line).

**SVG LineBox**, under **HA Grafik – Spezial**, collects numeric values from connected SVG-Lines, calculates a signed sum, and can pass it to outgoing lines and optionally a Home Assistant number helper. Its box is visible in the editor. At runtime the box disappears, and active lines meet visually at its center.

## Set it up in the editor

1. Add an **SVG LineBox** and the **SVG-Lines** you need.
2. Enable **Docking points** on the LineBox and activate only the positions you need. All twelve start disabled. **All points** switches them together; each can also be toggled individually.
3. Under **Ports**, each active point gets a role: **Input**, **Neutral**, or **Output**. **Neutral** is the default and does not participate in calculations. Disabled points have no role setting.
4. Connect incoming SVG-Lines to input ports and another SVG-Line to an output port. From Studio 0.1.126, a line can take its value from a numeric widget connected at the other end, such as Number. Alternatively select a **Numeric entity** under **Animation → Direction source**; this explicit line source takes priority.
5. On the output port, enable **Pass calculated value**. On the outgoing line, enable **Animation**. Both are needed for the sum to control its direction and speed.

The twelve docking positions are the same as on other widgets: left/right at top, center, bottom; top/bottom at one-quarter, center, three-quarter width. Multiple lines can connect to one point. The **Input**/**Output** role determines the function, not just the line's visual direction.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="Editing an SVG LineBox">
  <source src="/videos/grafik-visual-studio/linebox_edit.mp4" type="video/mp4">
  <a href="/videos/grafik-visual-studio/linebox_edit.mp4">Open the editor video</a>
</video>

[Open the editor video directly](/videos/grafik-visual-studio/linebox_edit.mp4)

## How the sum is calculated

The LineBox counts visible SVG-Lines connected to **Input** ports with valid numeric values. An explicit line numeric entity takes priority; otherwise a connected numeric widget or enabled LineBox output supplies the value. Number's multiplier is applied without rounding to its display precision. Manual input-line animation stays independent of numeric handoff. For explicit line values, a line ending at the box contributes its signed value; a line starting at the box contributes the same value with its sign reversed. Automatically sourced widget values are adjusted for line orientation. Each line is counted at most once. Missing or invalid states are skipped; if no valid input remains, there is no calculated value. Zero is valid. Internal feedback cycles are stopped.

**Example without extra helpers:** Connect Number with 125 and Number with 79 to two input ports: the LineBox shows **204**. Connect its enabled output to another Number, Red Number, Gauge or Bar. Select **Value source → Value from docking point**, choose the **Input docking point**, and enable it under **Docking points**. The display uses the value directly; multiple valid lines on that point are summed with signs. Missing input displays `--`. The other sources are **Home Assistant entity / preview** (existing behavior) and **Preview value** (ignores a configured entity).

Example: two input lines end at the box with values `1000` and `-300`. The sum is `700`. For an outgoing line that starts at an **Output** port with **Pass calculated value** enabled, `700` flows from start to end. If the outgoing line ends at the box, the sign is reversed to match its orientation. It keeps its own colors, arrowheads, and line style. If its animation is disabled, it stays still even with a forwarded value; zero or no valid input also stops it. With the outgoing line's **SVG LineBox divisor (on handoff)** set to `100`, `700 ÷ 100 = 7` cycles/s. Numeric animation is capped at 0.05–20 cycles/s.

A **Neutral** port contributes neither input nor output. Disable **Pass calculated value** on an output if the connected SVG-Line should use its own animation settings again. Merely crossing lines does not connect them.

## Junction and runtime appearance

Active lines are routed to the center of the invisible box at runtime. The **Junction** group controls their presentation:

| Setting | Effect |
| --- | --- |
| **Show circle** | Shows or hides a circle over the line ends. It is on by default and appears when at least two visible lines are connected. |
| **Diameter (px)** | Requested circle diameter, 4–100 px; the circle grows if thick lines need more coverage. |
| **Fill color**, **border color**, **border width (px)** | Circle colors and border thickness, from 0–20 px. |
| **Show output value** | **Off** (default), **Above the circle**, or **Below the circle**. Displays the signed input sum; an em dash means no valid input. The value can also appear with the circle hidden. |

The value display updates during slider movement at runtime. The circle sits above the connected lines and covers their angular ends.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="SVG LineBox at runtime">
  <source src="/videos/grafik-visual-studio/linebox_runtime.mp4" type="video/mp4">
  <a href="/videos/grafik-visual-studio/linebox_runtime.mp4">Open the runtime video</a>
</video>

[Open the runtime video directly](/videos/grafik-visual-studio/linebox_runtime.mp4)

## Optional Home Assistant number helper

Passing the sum to outgoing lines is internal and needs no helper. To use the sum elsewhere in Home Assistant, enable **Also write to number helper** under **Number helper output** and select an existing `input_number.*` helper. The app writes only when the value changes at runtime; brief changes are coalesced. Set the helper's allowed range to cover the possible sum. Writing is rejected if that same helper is also a numeric input source for this LineBox, preventing direct feedback. No write occurs without a valid input.

The first version reads numeric entities through input lines. There is no separate entity control for each LineBox port yet. The former palette name **Linebox** remains searchable; saved projects retain the technical `linebox` type and existing custom widget names.

For path, color, arrowhead, and animation controls, see [SVG-Line](./svg-line).
