---
title: Drawing with SVG-Line and Linebox
---

# Drawing: SVG-Line and Linebox

The line widget appears in the palette as **HA Grafik – Spezial → SVG-Line**. For example, you can visually connect two solar panels to an inverter or merge several flows at a collector point. SVG-Line can read a Home Assistant entity to control its animation; Linebox can add values from several lines and pass the result to an outgoing line.

## Draw a connection

1. Add an **SVG-Line** and select it. Both endpoints appear as draggable circles. Drag a free endpoint onto a docking point of another widget. Alternatively, choose a widget and docking point under **Start** and **Ziel**, or enter free X/Y coordinates.
2. Enable the **Andockpunkte** property group on the target widget. New widgets start with all twelve positions off. **All points** switches them on or off together and shows a mixed state when only some are selected. Each position can also be enabled individually: left/right at top, center and bottom; top/bottom at one-quarter, center and three-quarter width. The checkbox in the group heading enables or disables the entire section. Multiple occupancy, maximum connections, lane spacing and persistent visibility are configurable.
3. Choose the **Pfadart**: straight, automatic orthogonal, curve or manual zigzag/multi-point path. Clicking the line opens a centered dialog with **Intermediate point** and **Collector point**; “Intermediate point” is the default. Confirming with **OK** adds a draggable intermediate point and changes the path to manual multi-point mode. Points can also be named and positioned by X/Y in the properties editor.

An enabled **Sammelpunkt** can be chosen as the start or destination of another line. You can also drag a free line endpoint onto the visible collector point: it snaps into place and stores the connection. Crossing or proximity alone never joins lines. A disabled collector point will not accept a new line. Multiple lines can lead to one enabled collector point. Lines that only touch the point visually must be docked again once.

## Appearance and flow

- **Line:** Base color, second animation color, width, opacity, solid/dashed/dotted pattern, dash and gap lengths, line caps and corner radius.
- **Arrowheads:** Set start and end independently to none, filled or open arrow, or circle; size and color are configurable.
- **Animation:** Two-color flow, moving dashes, pulse or moving light. **Direction source** selects exactly one mode: **Manual** with direction and duration, **Numeric entity**, or **Boolean entity**. A positive number flows from start to end, a negative number reverses it, and zero stops the animation. Absolute value divided by **Divisor** (default 1) gives cycles per second, clamped to 0.05–20; for example, 1000 W ÷ 100 = 10 cycles/s. Boolean `on`/`true`/`1` means forward, while `off`/`false`/`0` means reverse; this mapping can be inverted. Missing or invalid states stop the flow. Arrowheads follow the active direction. The runtime refreshes the selected Home Assistant entity regularly. With **Animationstakt der Hauptlinie übernehmen** enabled, a branch follows the main line's animation timing while keeping its own colors when the animation is active. If it is coupled to that main line's collector and the main line is not animated, the branch also stops and shows the main line's base color, including its arrowheads. The branch's own color and animation settings remain stored and apply again after detaching. Synchronization offers matching phase or arrival at the collector point. In manual mode, a collector connection automatically orients the animation toward that point.
- **Crossing and stacking:** Overlay, visual gap or bridge/arc, plus automatic, above, below or manual z-index. A higher z-index is visually in front of a lower one; it does not create a connection.

## Editing

| Action | Control |
| --- | --- |
| Move a free endpoint | Drag its circle or focus it and use arrow keys; `Shift` changes the step from 1 to 10 pixels. |
| Detach a docked endpoint | Hold `Ctrl` and drag its circle; `Ctrl` plus an arrow key also works. |
| Move an intermediate point | Select the line and drag the point. |
| Move the whole line | Press and drag the line. Existing start/end docking is detached. |
| Add a line point | Click the line without dragging, choose a point type and confirm with **OK**. |

This widget is experimental. Crossing effects and synchronized animation may still need refinement for some paths and browsers.

## Linebox as an invisible distributor

The editor regularly refreshes the states of selected numeric and Boolean entities. This lets you check SVG-Line animation and the calculated Linebox value before switching to runtime.

**HA Grafik – Spezial → Linebox** can be moved and configured in the editor. Its box stays invisible at runtime, while connected lines meet at its center. By default, a circle covers their angular ends. Under **Junction**, you can hide the circle or set its diameter, fill color, border color, and border width. With thick lines, the circle grows as needed to keep covering their ends. **Show output value** offers **Off** (default), **Above the circle**, and **Below the circle**. The label shows the signed sum of the inputs and updates during slider movement at runtime. Linebox has the same twelve docking positions as other widgets, all initially off. Under **Docking points**, enable only the positions you need. Under **Ports**, each enabled point then gets one role: **Input**, **Neutral**, or **Output**. Neutral is the default and does not affect the calculation. Disabled points have no role control. Their separate docking positions remain in the editor; neutral ports do not join the common point.

To test it, dock two SVG-Lines to input ports and a third SVG-Line to an output port. For both incoming lines, select **Numeric entity** as the animation direction source and enter a valid Home Assistant entity ID. Lines ending at Linebox add their signed values: `1000` and `-300` produce `700`. A line starting at Linebox and assigned to an input contributes with the opposite sign. Missing or invalid states are ignored.

Set the outgoing port to **Output** and enable **Pass calculated value**, which is initially off. Enable animation on the outgoing SVG-Line. Its direction and speed now follow the sum. **Linebox divisor (on handoff)** sets the ratio: `700` with divisor `100` yields 7 cycles/s. The line retains its own colors, arrowheads, and line style. A sum of `0`, or no valid input, stops its animation. Turn off value passing at the port to restore the outgoing line's own animation controls.

Calculation and handoff normally stay internal. Under **Number helper output**, you can also write the sum to an `input_number` helper for use elsewhere in Home Assistant. Internal handoff remains active. The helper is written only when the sum changes; a helper that also feeds an input of the same Linebox is rejected to prevent direct feedback. Configure the helper's allowed range to cover possible sums.

This first version uses numeric entities on incoming lines. Separate entity control for each Linebox port is not yet available.
