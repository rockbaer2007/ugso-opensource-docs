---
title: UGSo Printer – Printer and cartridges
description: Independent printer widget set with status and up to six evenly distributed cartridges.
---

# UGSo Printer

**UGSo Printer 0.1.0** is an independent external widget set by **rockbaer2007** for **Grafik Visual Studio 0.1.261 or newer**. It displays a printer with its current status and **1–6 ink or toner cartridges**. Cartridge graphics automatically occupy equally sized columns across the available widget width, including after resizing.

The screenshot shows the runtime with test data.

![UGSo Printer with six cartridges and a low-level warning](/images/grafik-visual-studio/printer-six.png)

## Original project

Inspired by [HA Printer Card by ADNPolymerase](https://github.com/ADNPolymerase/ha-printer-card), published under the [MIT license](https://github.com/ADNPolymerase/ha-printer-card/blob/main/LICENSE). The original is a Lovelace card. UGSo Printer uses original SVG artwork, its own Studio renderer and explicitly selected Home Assistant entities. No upstream source or artwork is bundled. It appears as a separate palette set and does not belong to Industrial.

## Installation

1. Update Grafik Visual Studio to **0.1.261 or newer**.
2. [Download ugso.printer.wg](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/printer/ugso.printer.wg).
3. Install under **Settings → Widget packages → Local**.
4. Add **UGSo Printer → Drucker** from the palette and select status and supply entities using **…**.

The package contains one declarative widget definition, an original palette icon, instructions and an MIT license. It contains no executable package code. [Source and package instructions](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/printer).

## Settings

| Section | Settings |
| --- | --- |
| Printer | Caption, status entity, model `mfp` (multifunction), `inkjet` or `office`. |
| Cartridges | Count **1–6**, ink or toner appearance, low threshold **0–100 %**, default **20 %**. |
| Cartridge 1–6 | Individual percentage entity, caption and color. The first N entries are active. Later bindings remain saved and are polled again when the count is increased. |
| Status message | Optional display. Separate entity, otherwise the printer entity's `state_message` or `state_reason`. |
| Additional values | Optional power and page-counter entities. |
| Colors and size | Background, text and printing-state color. Default **480 × 440 px**, minimum **240 × 280 px**. |

The count determines distribution; individual cartridge X positions are unnecessary. Long captions are truncated when space is limited. Tooltips retain full names and values. All six property groups remain available so further cartridges can be prepared.

## Status and readings

Common states map to ready, printing, sleep, warning, stopped, offline or unknown. While printing, the sheet moves and the LED blinks. Browser reduced-motion preferences disable these animations. Errors and jams take priority; a supply warning alone does not stop the printing animation.

Editor and runtime read the same current Home Assistant values. Missing or invalid levels display **—**, rather than 0 %. Valid numbers are clamped to **0–100 %**. At or below the threshold, the cartridge and its reading are highlighted, with affected names listed below.

## Scope of this version

This first version uses explicitly selected entities. It has no automatic device/supply discovery, wear parts, socket control, test printing or printer web links. All bindings are read-only. The separately available original card offers further features.
