---
title: Material Design
description: Material Design 1.1.0 for Studio 0.1.292 with DE/EN/FR and compatible updates.
---

# Material Design

**Package 1.1.0 · Studio 0.1.292 or newer · 49 widgets · MIT.** Independent renderers inspired by [ioBroker VIS2 Material Design by typhosj/Scrounger](https://github.com/typhosj/ioBroker.vis2-materialdesign). Original MDI assignments remain local SVGs. Technical package ID: <code>ugso.materialdesign</code>.

[Deutsch](/projects/grafik-visual-studio/materialdesign) · [Français](/fr/projects/grafik-visual-studio/materialdesign) · [Source](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign)

## Installation and preserved settings

1. Export the existing Studio project as JSON.
2. Update Studio to **0.1.292 or newer** and restart.
3. [Download Material Design 1.1.0](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/dist/ugso.materialdesign-1.1.0.wg). Install through **Settings → Widget packages → Local**, or use the direct GitHub file URL.
4. The package updates additively. Reload the page and check the existing project.

Installation **never rewrites project files**. Existing fields, defaults, order and technical IDs remain protected. New fields/groups and choices are appended. Colors, text, dimensions, entity assignments and disabled groups stay saved. Older published packages remain available.

Old **State Multi** widgets retain their value cycle. Multiple-target writing is an explicitly selected mode. Old Advanced Views retain mapped values; page name/ID and numeric index are additional modes. New widgets include the corresponding original modes. Design style changes never alter targets.

## Languages and appearance

**Material language** follows Studio or selects **German, English or French** for the widget and its Material properties. User text, page IDs and entity IDs are never translated. The overall Studio interface remains DE/EN; French is offered for Material here.

**Classic**, **Material 3** and **Project default** remain selectable. Color scheme follows the page or forces Light/Dark. Explicit colors, font sizes and spacing take precedence. The preview retains 26 palettes and the original white Classic background.

## Widgets and original-style features

| Family | Features and controls |
| --- | --- |
| Buttons / Icon Buttons | State labels/colors/icons, pressed color, momentary mode, bounded addition, new window, navigation and timed unlock |
| State Multi | Previous cycle or multiple entities with separate values and delays |
| Checkbox / Switch | Custom ON/OFF or boolean mode, label position and actual switch track/thumb |
| Input / Select / Autocomplete | Input shapes, affixes, hints/counters, icons, hover/selection colors, keyboard and mask: # = digit, A = letter, * = letter/digit |
| Slider / Slider Round | Effective handle/track sizes, limits/step, ticks, working entity, write during interaction or on release, arc/start angle |
| Progress | Linear/circular, determinate/indeterminate, size/rotation, threshold colors and value text |
| Value / Icon / Version | Number/boolean/text/date/duration, factor/offset, conditions, link and change effect; static or state icon; actual package version |
| HTML Card | Title/subtitle, image, card layouts, colors, image refresh and isolated HTML |
| List / Icon List / Table / Alerts | Subtexts, navigation/links/controls, JSON status bars, image columns, column formatting, fixed header, sorting and acknowledgement |
| Four charts | Bars, pie/doughnut, JSON and Recorder; up to four Y axes, stacks, filled/stepped lines, tooltips, labels, palettes and legend positions |
| Calendar | Month/week/day/year/list, week numbers, colors and time grid in DE/EN/FR |
| Top App Bar | Modal/permanent/automatic drawer, child entries and selected index; previous page links remain a separate mode |
| Grid/Masonry / Advanced Views | Responsive columns, per-view visibility, mappings/name/index, boolean indices 0/1, preload and retained child views |

**Show advanced options** reveals details without deleting hidden values. Set counts for targets, views, series or menu items.

## Home Assistant and data

Validated HA actions support <code>switch/input_boolean</code>, <code>number/input_number</code>, <code>text/input_text</code>, <code>select/input_select</code>, <code>button/input_button</code> with <code>PRESS</code>, light brightness, fan percentage and cover position. States, options and ranges are checked. Sensors, attributes and unavailable entities remain displays.

Multiple-target actions are sequential and stop on errors or page changes. Completed actions are not rolled back. Arbitrary HA services and executable ioBroker bindings are unsupported.

Top App Bar **State mode** writes its index to its entity. **Advanced View in Widget 8**, sharing that entity and using **Index mode**, displays the corresponding local Studio page. Without an entity, use existing Studio data flow; separate local preview values are not shared automatically.

Lists read editor rows or JSON; tables use configured column keys. Optional list HTML is sanitized: no scripts, event handlers or active embeds. HTML cards remain sandboxed. External sites may block iframes.

Charts accept <code>axisLabels/graphs</code>, <code>labels/datasets</code> or point lists. Recorder is limited to **ten entities and 1–168 hours**. The X axis respects actual time spacing. Aggregation: none, average, minimum, maximum, sum or last value, with a minute interval. Missing states are not invented.

No automatic ioBroker project import: HA entities, Recorder and Studio pages replace object IDs, history adapters and VIS views. SVG charts and renderers are independent implementations; universal pixel identity is not claimed.

## Checks and publishing

Browser checks cover all 49 entries in DE/EN/FR, Classic/Material 3 and Light/Dark plus interaction. Real package upgrades retain old project files byte-identically. Check actual HA device functions in your own installation.

[Comparison project](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/materialdesign-widgetvergleich.json) · [Initial audit](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/AUDIT-2026-10-12.md)

Register **1.1.0**, minimum Studio **0.1.292**, ID <code>ugso.materialdesign</code> and MIT in the [package catalog](https://visualstudio.ugso-software.de/?lang=en). Publishing to GitHub does not automatically approve a catalog entry. Checksum: <code>dist/SHA256SUMS</code>.
