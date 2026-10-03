---
title: HA Grafik Visual Studio
description: A different kind of Home Assistant dashboard, with its current development status and editor guide.
---

# HA Grafik Visual Studio

**A different kind of Home Assistant dashboard.** Grafik Visual Studio is an experimental Home Assistant app with a freeform editing surface and a separate runtime. It is still in early development; its project format and controls may change. It is not yet intended for production dashboards.

[Editor and keyboard shortcuts](./editor) · [All 63 widgets](./widgets) · [SVG-Line](./svg-line) · [SVG LineBox with videos](./svg-linebox) · [SVG LineBox Math](./svg-linebox-math) · [Widget package interface](./widget-packages) · [Tool package interface](./tool-packages) · [Package packer](./packer) · [Source and Home Assistant app](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio)

![HA Grafik Visual Studio editor with widget palette and SVG connection lines](/images/grafik-visual-studio/editor-zeichnung.png)

*Editor view with drawn connection lines. [Open the full-resolution image](/images/grafik-visual-studio/editor-zeichnung.png).*

## What works today

- Manage multiple projects and named pages, each with its own size, background and widgets. The runtime presents visible pages separately.
- Place, move, resize and name widgets on a scrollable canvas, and arrange them with z-index. The editor supports multiple selection, alignment, size matching, copy/paste and undo/redo.
- Use 63 widgets from “HA Grafik – Basis”, “HA Grafik – Interaktiv”, “HA Grafik – Spezial” and “HA Grafik – Datenfluss”. These include HTML, images, numbers, controls, tables, calendars, dashboard embedding, SVG lines, calculations and converters. The palette shows a preview or icon appropriate to each type.
- Edit layout, CSS, “Generell”, visibility and docking-point properties. The editor widget filter uses the “Filterwort” property in “Generell”.
- Draw connection lines with intermediate points, explicitly enabled collector points, colors, arrowheads and animations. Lines that cross do not connect automatically.
- Select files from Home Assistant's `/config/www/studio` folder and upload supported files. The file browser automatically creates this root folder when opened. If write permissions are missing, it displays instructions for creating the folder manually. Widget image selection uses the same folder; applied and copied paths start with `/local/studio/`. The entity browser can search entities and current states and insert entity IDs into widget fields.
- The Files search field searches filenames and paths across all `/config/www/studio` subfolders, independently of the open folder and without case sensitivity. Results show image previews and relative paths; file-type filters and image insertion remain available. Clearing the search restores the open folder listing.
- Individual and all-widget checkboxes immediately update the editor selection. The selection list stays in front of all widgets and provides Copy and Delete buttons for the checked widgets; deletion uses the confirmation dialog. Signal images, extra controls and docking points are disabled for new widgets and can be enabled when needed.
- Drag any selected widget to move the entire selection together, including after copying and pasting. Selected SVG lines and intermediate points move with the selection while existing attachments remain intact. Locked widgets block the shared move. Each drag can be undone as one operation.
- Deleting widgets opens a confirmation dialog listing their IDs. Cancel or Escape aborts deletion. “Suppress this question for the next 5 minutes” skips subsequent deletion prompts for five minutes in the open editor. Deletion remains undoable.
- Save changes automatically after a configurable delay (five seconds by default) or save manually. Widgets can be exported and imported as JSON.
- The interface follows Home Assistant's language: German when HA is set to German, English otherwise. Under **Settings → Language**, each browser can choose **Automatic**, **German** or **English**. Project and widget content is left unchanged.

## Updates through 0.1.158

The [widget reference](./widgets) now explains the VIS2-inspired value lists, Bool HTML/Checkbox/Select, Table, HTML State, Bar, HTML/navigation, filters, String and Input val, with screenshots. CSS General stays enabled for every widget. Migration hints can be switched off under Settings → General.

**Dashboard in widget** under Special embeds an HA dashboard up to 800 × 640 pixels. **View in widget** continues to embed Studio pages. [Data flow](./datenfluss) provides Value connection, Value converter and Value calculation; [LineBox Math](./svg-linebox-math) supports four calculations and configurable presentation.

## Planned: Calendar JSON integration

A dedicated Home Assistant integration is planned to expose HA calendars as JSON event lists for calendar widgets and other consumers. The sensor state will contain the event count; the full list will be stored in the `events` attribute. Date range and refresh interval should be configurable. Event Calendar already supports `calendar.*` directly; the reusable integration has not been implemented yet.

## Current limitations

In the runtime, Sensor, String, Red Number, Bar, Gauge and Bool HTML read a bound Home Assistant entity every five seconds; visibility rules use those states too. A Switch widget can control `switch`, `light` and `input_boolean` through HA service actions and then displays the confirmed HA state. Other data and control widgets still use local sample values. Selecting an entity ID there does not yet provide live binding. Visibility's “Nur für Gruppen” option and `multi-views` behavior are not fully implemented. The editor filter affects only the editor view.

The app provides one standard Home Assistant Ingress entry. Separate sidebar entries for editor and runtime require the additional experimental integration from `custom_components/ha_grafik_visual_studio`, which requires Home Assistant OS or Supervised with Supervisor. The [repository README](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/README.md) explains the installation.

The interface draws inspiration from VIS2. Grafik Visual Studio is an independent implementation; it does not ship VIS2 code or widgets.
