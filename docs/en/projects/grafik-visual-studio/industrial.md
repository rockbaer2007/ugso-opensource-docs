---
title: UGSo Industrial – Widgets
description: Installation and settings for the external Industrial package for Grafik Visual Studio.
---

# UGSo Industrial – Widgets

The external **UGSo Industrial 0.3.0** package contains **Gauge/Poti – 270°**, **Toggle switches – 1 to 4** and **Rocker switches – 1 to 4**. Industrial styling adds a housing, corner screws and a frame. **Studio 0.1.235 or newer** is required for all settings described here, including rocker switches.

## Images

| Rotary control with ticks | Gauge with a color ring |
| --- | --- |
| ![Industrial rotary control with ticks and a bottom reading](/images/grafik-visual-studio/industrial-poti.png) | ![Industrial gauge with a color ring and centered solar power reading](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| No input: virtual rotary control with a negative scale minimum and **15 °C** below the knob. | With input: **823 W** solar power on a 0–1000 W scale, colored bands and centered value display. |

The images show runtime with example data, not live measurements.

## Installation

[Download the package](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) and install it through **Settings → Widget packages → Local**. The optional package uses API 0.2 and contains no executable package code. Package 0.3.0 requires Studio 0.1.235 for rocker switches. Updating preserves existing Gauge/Poti and toggle definitions.

[Source code and package instructions on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## Rocker switches – 1 to 4

Package **0.3.0** and Studio **0.1.235** add rocker switches as a copy of the toggle widget using transparent PNG artwork. Select **White/Gray**, **Red**, **Black** or **Green** for each channel under **Switch 1** through **Switch 4 → Switch color**. A single widget can combine different colors; its artwork follows each channel's on/off state.

![Four rocker switches with independently selected colors](/images/grafik-visual-studio/industrial-rockers.png)

All toggle settings apply: captions, additional ON/OFF, 1/0 or EIN/AUS legends, LED colors, entities, E1–E4/A1–A4, six housing snap points, screws, frame and spacing. Printed O/I symbols remain part of the artwork. Aspect ratio is 1:1 to 4:1 with at least 64 px per channel. Controls are enabled only in runtime.

## Gauge/Poti: data and controls

The following scale and value-display sections describe Gauge/Poti. Toggle switches have a dedicated section at the end of this page.

- **No input:** rotary control in runtime with mouse, touch or keyboard. Initial value and control step are configurable.
- **Entity or signal input:** read-only gauge. An enabled signal input takes precedence over the entity. An unavailable input is shown as a missing reading.
- **Output:** `number.*` or `input_number.*`, on release or continuously while dragging. Changed gauge readings are also forwarded. The entity must be available and writable; input and output entities must differ.
- **Value lines:** visible and visually hidden connections use the existing dataflow.

Editor interaction and writes are disabled; open runtime to control values.

## Scale and color bands

Choose **ticks** with emphasized zero or a **color ring**. Minimum, maximum, tick division and an independent control step are configurable; negative bounds are supported.

Color bands use ascending **upper limits** within the scale. The final band ends at the maximum. For solar power from 0 to 1000 W, four bands could end at **250 / 500 / 750 / 1000**. Adjust band limits after changing the scale range. Invalid limits do not hide an available reading; the warning remains in the tooltip.

## Value display

The dedicated **Value display** group contains:

| Setting | Effect |
| --- | --- |
| Show value | Display the reading and unit in the instrument. |
| Unit | Custom unit, such as W. Empty uses the Home Assistant input entity's `unit_of_measurement`. |
| Value position | **Center** or **Bottom**; bottom sits below the rotary knob. |
| Font size (px) | Default 12 px; remains constant when resizing the widget. |
| Font color | Configurable color, light by default. |

Value/unit display was added in Studio 0.1.227; dedicated display settings were added in 0.1.228.

## Housing and colors

Studio **0.1.231** adds **Enable screws** directly below **Industrial styling**. Screws are enabled by default and can be disabled independently while industrial styling is active. Turning industrial styling back on also enables the screws again. Without industrial styling, screws are hidden and the checkbox is disabled.

**Industrial styling** adds four corner screws, the housing background and frame. Scale and pointer colors are independently configurable. **General CSS → Corner radius (px)** controls frame rounding.

From Studio 0.1.230, **Customize frame width** works as follows:

- **Unchecked:** use the existing 2 px frame width.
- **Checked:** set a custom **Frame width (px)** from 1 to 16 px.
- Disabling the override retains the custom value and keeps the frame visible.

**Frame color** is independently configurable. Disabling industrial styling hides the housing frame.

## Size

The widget starts at **64 × 64 px**. The checked-by-default **1:1 aspect ratio** option, available since Studio 0.1.226, keeps width and height equal during typed changes and dragging. Uncheck it for independent dimensions, each at least 64 px. Re-enabling the lock uses the larger dimension for both sides.

## Housing snap points

Since Studio 0.1.224, **Housing snap points** offers four independently enabled corners and one spacing value for all sides. With 1 px on each neighbor, the gap is 2 px; single widgets snap when dragged.

Set the color in **Settings → General → Editor and dock points → Housing snap point color**. Signal ports stay separate. Automatic port relocation to free housing sides will follow later.

## Toggle switches – 1 to 4

Since **Studio 0.1.236**, toggle bank width includes the space between channels: **height × channel count + 2 × all-side spacing × (channel count − 1)**. At 64 px height and 1 px spacing, widths are **64 / 130 / 196 / 262 px**. Channel centers and E/A ports align with individual widgets below. Width input and resizing include the extra spacing. This change initially applies only to toggle switches; rocker sizing is unchanged. Updating Studio is sufficient; package 0.3.0 is unchanged.

Package **0.2.0** and Studio **0.1.232** add one to four independently controlled switches side by side. **Number of switches** sets the width/height ratio from **1:1 to 4:1**. Minimum height and width per channel are 64 px; typed changes and resizing preserve the ratio.

![Four industrial toggle switches with small LEDs and three plate legends](/images/grafik-visual-studio/industrial-switches.png)

*Runtime with example data: custom captions, green LEDs and ON/OFF, 1/0 and EIN/AUS plates. Since Studio 0.1.233, the metallic lever uses the transparent PNG supplied by rockbaer2007 and is fully visible in both positions. The LED remains CSS artwork. Updating Studio is sufficient; package 0.2.0 does not need reinstalling.*

Each **Switch 1** through **Switch 4** group has a static **Caption**, **Plate legend** with **ON/OFF**, **1/0** or **EIN/AUS**, initial state and individual LED on/off colors. The LED sits above the caption; entities never change the plate text. Font size and color are available under **Caption**.

| Connection per channel | Behavior |
| --- | --- |
| Input entity | Feedback for lever and LED. When no input is configured, the output entity provides feedback. |
| Input port | Above its channel, independently enabled; takes precedence over the entity. |
| Output entity | Controls `switch.*`, `light.*` or `input_boolean.*`. Without a separate output, a compatible input entity is controlled. |
| Output port | Below its channel, independently enabled. Supplies the last command as a boolean value, or the current state before the first command. |

Unbound switches work locally. Missing feedback disables control. The editor never sends commands. Housing, screws, frame and housing snap settings also apply. To add the toggle switches, update the optional package locally to **0.2.0**; existing Gauge/Poti definitions are retained.

### Ports E1–E4 and A1–A4

Since **Studio 0.1.234**, editor signal ports are labeled **E1–E4** (input above each switch) and **A1–A4** (output below each switch). Only ports for the configured switch count are shown. Each port is enabled independently and follows the central input/output colors; existing connections are preserved.

The switch has six independent **Housing snap points**: four corners plus **Left center** and **Right center**. Including signal ports, this provides **8 / 10 / 12 / 14 available points** for one to four switches. Housing points snap with the configured spacing and housing color; they do not carry signal values. Points and port labels appear only in the editor. Updating Studio is sufficient; package **0.2.0** remains unchanged.
