---
title: 3D Printer Card
description: Compact Home Assistant card for Klipper and Moonraker with profiles, camera and temperature charts.
---

# 3D Printer Card

[Deutsch](/projects/3d-printer-card/) · [Français](/fr/projects/3d-printer-card/)

**Version 0.1.7. Works only with Klipper and Moonraker.** Install and configure the [Moonraker integration](https://github.com/marcolivierarsenault/moonraker-home-assistant) for each printer. The card uses its HA entities without a separate login or printer connection.

## Installation

[![Open in Marketplace](/images/3d-printer-card/marketplace.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=3d-printer-card&category=plugin)

1. Back up settings. Install and configure the [Moonraker integration in Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=marcolivierarsenault&repository=moonraker-home-assistant&category=integration).
2. Add `https://github.com/rockbaer2007/3d-printer-card` as a custom **Dashboard** repository in Marketplace and download it. Not yet listed in the default Marketplace catalog.
3. Check `/hacsfiles/3d-printer-card/3d-printer-card.js` is registered as a **JavaScript module**, then reload the browser. Replace an existing local resource instead of loading both versions.
4. Add **3D Printer Card** to a dashboard. Its technical type remains `custom:moonraker-display-card`.

Manual installation: copy the release JS file to `/config/www/3d-printer-card/` and register `/local/3d-printer-card/3d-printer-card.js?v=0.1.7` as a JavaScript module. No HA restart needed. Replace all example entities with your own.

## Display and profiles

- State, filename, progress, elapsed/remaining/projected time, ETA and layers, plus speed, fan and messages.
- Nozzle/bed actual and target temperatures in one chart; board/pad actual temperatures in another. History requires those entities in HA Recorder.
- Live camera on the right at approximately one third of the width, with an optional thumbnail. Narrow displays stack the content.
- Compact fields, shallow charts, 24-column default and automatic height. Use a sections view; panel views force full width.
- Up to 20 printer profiles with independent entities and cameras.

Open **Profil hinzufügen** (add profile) or **Profil bearbeiten** (edit profile). Select the printer's `current_print_state` sensor under **Drucker erkennen** to detect its prefix. Choose cameras and adjust mappings using native HA selectors. Click **Profil übernehmen**, then **Speichern** in the outer editor. Editor labels are currently German; documentation is DE/EN/FR. Existing profiles remain compatible.

## Screenshots in use

These screenshots show the card and its German-language editor. Click an image to open it at full size.

### Overview with camera and temperature charts

[![3D Printer Card for the Ender3 V2: status, progress, timing, camera on the right and nozzle, bed and system temperature charts](/images/3d-printer-card/card-overview.png)](/images/3d-printer-card/card-overview.png)

### Card editor with profile selection and preview

[![Visual card editor with printer profile selection, add and edit profile buttons, and the preview on the right](/images/3d-printer-card/card-editor.jpeg)](/images/3d-printer-card/card-editor.jpeg)

### Add a printer profile

[![Add printer profile dialog with profile name, print-state entity, detected prefix, camera and model thumbnail](/images/3d-printer-card/profile-add.png)](/images/3d-printer-card/profile-add.png)

### Edit a printer profile

[![Ender3 V2 profile editor with HA entity selection, camera, model thumbnail and expandable status, temperature and print-time mappings](/images/3d-printer-card/profile-edit.png)](/images/3d-printer-card/profile-edit.png)

## Cancellation and verification

Read-only except for **Cancel print**, using the existing HA button for an active/paused print and a ready printer. Confirmation and a fresh state check are required. Profile changes send no commands. No filament consumption or lifetime statistics.

Verified with real entities on HA 2026.11.3: display, camera, charts and profile editing while preserving settings. Also 16 automated tests and browser tests at 390, 800 and 1500 pixels with no overflow or unwanted service calls. No real running print was cancelled during testing.

## Downloads

Ready-to-copy forum posts: [Deutsch](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forenbeitrag-de.md) · [English](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forum-post-en.md).

- [GitHub and full guide](https://github.com/rockbaer2007/3d-printer-card)
- [Release 0.1.7 with ZIP and JavaScript](https://github.com/rockbaer2007/3d-printer-card/releases/tag/v0.1.7)
- [Changelog](https://github.com/rockbaer2007/3d-printer-card/blob/main/CHANGELOG.md)

MIT license. Independent frontend project, separate from the Moonraker integration.
