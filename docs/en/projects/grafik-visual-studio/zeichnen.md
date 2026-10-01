---
title: Drawing with SVG connection lines
---

# Drawing: SVG connection line

The drawing widget appears in the palette as **HA Grafik – Spezial → SVG-Verbindungslinie**. For example, you can visually connect two solar panels to an inverter or merge several flows at a collector point. The line is a visual widget; it does not transfer Home Assistant values itself.

## Draw a connection

1. Add an **SVG-Verbindungslinie** and select it. Both endpoints appear as draggable circles. Drag a free endpoint onto a docking point of another widget. Alternatively, choose a widget and docking point under **Start** and **Ziel**, or enter free X/Y coordinates.
2. Enable the **Andockpunkte** property group on the target widget. Its twelve positions can be enabled individually: left/right at top, center and bottom; top/bottom at one-quarter, center and three-quarter width. Clearing the group checkbox turns off all docking points. Multiple occupancy, maximum connections, lane spacing and persistent visibility are configurable.
3. Choose the **Pfadart**: straight, automatic orthogonal, curve or manual zigzag/multi-point path. Clicking the line opens a centered dialog with **Klick** and **Sammelpunkt**; “Klick” is the default. Confirming with **OK** adds a draggable intermediate point and changes the path to manual multi-point mode. Points can also be named and positioned by X/Y in the properties editor.

An enabled **Sammelpunkt** can be chosen as the start or destination of another line. You can also drag a free line endpoint onto the visible collector point: it snaps into place and stores the connection. Crossing or proximity alone never joins lines. A disabled collector point will not accept a new line. Multiple lines can lead to one enabled collector point. Lines that only touch the point visually must be docked again once.

## Appearance and flow

- **Line:** Base color, second animation color, width, opacity, solid/dashed/dotted pattern, dash and gap lengths, line caps and corner radius.
- **Arrowheads:** Set start and end independently to none, filled or open arrow, or circle; size and color are configurable.
- **Animation:** Two-color flow, moving dashes, pulse or moving light; direction from start to end or reverse, plus duration. With **Animationstakt der Hauptlinie übernehmen** enabled, a branch follows the main line's animation timing while keeping its own colors when the animation is active. If it is coupled to that main line's collector and the main line is not animated, the branch also stops and shows the main line's base color, including its arrowheads. The branch's own color and animation settings remain stored and apply again after detaching. Synchronization offers matching phase or arrival at the collector point. When connected to a collector, animation direction is oriented toward that point automatically.
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
