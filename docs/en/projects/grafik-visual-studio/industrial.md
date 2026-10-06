---
title: UGSo Industrial – Gauge/Poti
description: Installation and settings for the external Industrial package for Grafik Visual Studio.
---

# UGSo Industrial – Gauge/Poti

The external **UGSo Industrial 0.1.0** package contains **Gauge/Poti – 270°**: an instrument for displaying readings or controlling values with a virtual rotary knob. Industrial styling adds a housing, corner screws and a frame. **Studio 0.1.230 or newer** is recommended for all settings described here.

## Images

| Rotary control with ticks | Gauge with a color ring |
| --- | --- |
| ![Industrial rotary control with ticks and a bottom reading](/images/grafik-visual-studio/industrial-poti.png) | ![Industrial gauge with a color ring and centered solar power reading](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| No input: virtual rotary control with a negative scale minimum and **15 °C** below the knob. | With input: **823 W** solar power on a 0–1000 W scale, colored bands and centered value display. |

The images show runtime with example data, not live measurements.

## Installation

[Download the package](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) and install it through **Settings → Widget packages → Local**. The optional package uses API 0.2 and contains no executable package code. Basic functionality requires Studio 0.1.223; newer settings are provided by Studio updates. Package 0.1.0 does not need reinstalling for these settings.

[Source code and package instructions on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## Data and controls

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
