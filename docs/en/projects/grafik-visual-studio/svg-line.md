---
title: SVG-Line – draw and animate connections
---

# SVG-Line

From Studio 0.1.136, **automatic divisor adjustment** is available for numeric entities and LineBox outputs. It keeps animation at an adjustable speed as power changes. See **Automatic divisor adjustment: how and why** below for setup and calculation details.

Find **SVG-Line** under **HA Grafik – Spezial**. It visually connects widgets, routes paths around corners, and can animate a value flow. A line can start or end at a widget docking point, an explicitly enabled collector point on another SVG-Line, or free coordinates. The line itself is not a Home Assistant entity; an optional entity controls its animation.

## Connect widgets

1. Add SVG-Line and select it. Its start and end appear as draggable circles.
2. Enable **Docking points** on the target widget and activate the positions you need. New widgets start with all twelve positions off: left/right at top, center and bottom; top/bottom at one-quarter, center and three-quarter width. **All points** switches them together. More than one line can occupy the same point.
3. Drag a line endpoint onto an active docking point. Alternatively, choose the widget and point under **Start** and **Target**. **Active collector point instead** chooses a collector on another SVG-Line; **Free X/Y** positions an unattached end.

| Editor action | Result |
| --- | --- |
| Drag a free endpoint | Moves the start or end. Arrow keys move a focused point by 1 pixel, or 10 pixels with `Shift`. |
| Hold `Ctrl` and drag a docked endpoint | Detaches and moves it. `Ctrl` plus an arrow key also works. |
| Drag an intermediate point | Changes a manual multi-point path. |
| Drag the line itself | Moves the entire line and detaches its existing start/target docking. |
| Click the line without dragging | Opens the **Intermediate point** / **Collector point** choice; **OK** inserts the point. |

## Paths and collector points

Under **Path and collector points**, **Path mode** offers **Straight**, **Automatic orthogonal**, **Curve**, and **Manual zigzag/multi-point path**. **Corner radius** rounds corners where the chosen path supports them. **Intermediate and collector points** lets you name, position, and edit points. Adding a point by clicking changes the path to manual multi-point mode.

An **intermediate point** only bends the path. An enabled **collector point** accepts other SVG-Lines. Drag their free endpoint onto the visible collector or select it in the properties. Several lines can share one collector. Crossing or touching lines never join automatically. A disabled collector cannot accept a new connection.

## Line and arrowheads

| Group | Controls |
| --- | --- |
| **Line** | **Base color**, **animation color**, **width** (1–40 px), **opacity**, **style** (solid, dashed, dotted), **dash length**, **gap length**, and **line caps** (round, butt, square). |
| **Arrowheads** | Configure start and end independently: none, filled arrow, open arrow, or circle. Set **size** and **color**. The displayed marker ends swap when the flow reverses. |

## Animation and direction source

Enable **Animation** and choose two-color flow, moving dashes, pulse, or moving light. Exactly one **direction source** applies:

| Source | Direction and speed |
| --- | --- |
| **Manual** | Start → end or end → start, with a **duration** of 0.2–20 seconds per cycle. When joined to a collector, manual flow points towards it. |
| **Numeric entity** | Positive values flow start → end, negative values reverse it, and `0` stops. Absolute value ÷ **divisor** (default `1`) gives cycles per second, limited to 0.05–20. Example: `1000 W ÷ 100 = 10` cycles/s. |
| **Boolean entity** | `on`/`true`/`1` runs forward; `off`/`false`/`0` runs backward. **Invert Boolean direction** swaps this mapping. **Duration** sets the rate. |

Unavailable or invalid entity states stop the animation. The selected state refreshes in both editor and runtime. An **SVG LineBox** output can pass its calculated signed value to the line. This overrides the chosen direction source, but the outgoing line still needs **Animation enabled**. A zero or missing input stops it. Its **SVG LineBox divisor (on handoff)** sets the rate; the line keeps its own colors and style. See the [SVG LineBox guide](./svg-linebox).

## Automatic divisor adjustment: how and why

With a fixed divisor, animation speed increases with the input value. For example, divisor `100` turns `10 W` into only `0.1` cycles/s, but `1500 W` into `15` cycles/s. Increasing the divisor slows high-power appliances such as heating or a cooker, while making small values very slow. Reducing it speeds up small values and can make large values difficult to follow visually.

Automation therefore adjusts the divisor whenever the value changes, using the selected **target speed**. It uses no fixed power bands and also works above 15,000. The calculation is:

```text
Automatic divisor = absolute input value / target speed
Animation speed = absolute input value / automatic divisor
```

At **1 cycle/s**, the results are:

| Input value | Automatic divisor | Speed |
| --- | --- | --- |
| 10 | 10 | 1 cycle/s |
| 100 | 100 | 1 cycle/s |
| 1500 | 1500 | 1 cycle/s |
| 15,000 | 15,000 | 1 cycle/s |

This keeps motion similarly readable at low and high power. With automation enabled, speed represents the chosen target speed; it no longer indicates power magnitude. The sign still determines direction. Zero, missing values and invalid states stop animation.

### Setup

1. Select SVG-Line and enable animation under **Animation**.
2. For a Home Assistant numeric source, choose **Direction source → Numeric entity**, enter the entity and enable **Automatically adjust divisor (numeric entity)**.
3. For a connected **SVG LineBox** or **SVG LineBox Math** output, enable **Automatically adjust divisor (SVG LineBox)** instead. This forwarded value takes precedence over the selected direction source.
4. Set the corresponding **target speed**. The default is **1 cycle/s**, with a range of **0.05–5 cycles/s**. A target of `0.5` means two seconds per cycle; `2` means half a second. Start at `1` and adjust it for your line style and dash spacing.

Both automation settings are independent and initially disabled. Each manual divisor remains stored and takes effect again when its automation is disabled. **Manual** and **Boolean entity** modes still use their configured duration. Main-line animation inheritance continues to apply to ordinary branches; an actively forwarded LineBox value sets its outgoing line's own timing.

Cycles per second measure animation repetitions, not pixel speed. Line style, animation style and dash spacing affect visible motion. Automation provides a stable rate, while the target speed remains adjustable for each line.

## Main line, crossings, and stacking

**Main line / flow group** assigns a line to another. **Inherit main-line animation timing (keep own colors)** adopts the timing and animation style while retaining the branch's colors during active flow. **Synchronization** offers **same phase** or **arrive at collector together**. When a branch is connected to a collector of a non-animated main line, it stops and displays the main line's base color, including arrowheads. Detaching restores its saved settings.

Under **Crossing and z-index**, choose **overlay**, **gap**, or **bridge/arc**, and **automatic**, **above**, **below**, or **manual** stacking. A higher z-index appears in front of a lower one. **Pass clicks through** affects runtime interaction. Neither crossing style nor z-index connects lines; use a collector or [SVG LineBox](./svg-linebox) for that.

SVG-Line remains experimental. Crossing effects and synchronized animation can vary with path shape and browser.
