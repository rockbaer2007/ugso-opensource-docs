---
title: Drawing with SVG connection lines
---

# Drawing: SVG connection line

The drawing widget appears in the palette as **HA Grafik – Spezial → SVG-Verbindungslinie**. For example, you can visually connect two solar panels to an inverter or merge several flows at a collector point. The line is a visual widget; it does not transfer Home Assistant values itself.

## Draw a connection

1. Add an **SVG-Verbindungslinie** and select it. Both endpoints appear as draggable circles. Drag a free endpoint onto a docking point of another widget. Alternatively, choose a widget and docking point under **Start** and **Ziel**, or enter free X/Y coordinates.
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
