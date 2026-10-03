---
title: UGSo Technic
description: Install the external Technic widget set and connect Window – Wall to Home Assistant.
---

# UGSo Technic

**Inspired by the [ioBroker Technic Widgets by Sefina-DS](https://github.com/Sefina-DS/ioBroker.vis-2-widgets-technic).** An independent implementation for Home Assistant.

From **Studio 0.1.197**, you can install **UGSo Technic 1.0.0**. This first package contains **Window – Wall**. The other six widgets from the original set are not included yet.

## Installation

Download [ugso.technic.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/technic/ugso.technic.wg). Open **Settings → Widget packages → Install local .wg / .wg.zip** and select the file. After reloading, the set appears with an automatically assigned unused color. It remains independent of built-in widgets and Weather and Heating.

The [source and reproducible package build](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/technic) are public. The download includes `README.md` and `LICENSE.txt`, including the full MIT license and original attribution `Copyright (c) 2026 Sefina-DS`.

## Window – Wall

**General** configures the caption, **Show caption**, top/bottom caption position, icon size (10–100%), left/right handle and icon color. The default size is 120 × 160 pixels. **Read only** disables control.

**Data points** provides three independent HA bindings:

| Original field | Studio field | Home Assistant |
| --- | --- | --- |
| `oid_kontakt` | Opening contact: entity | for example `binary_sensor.garage_window`; `on` means open |
| `oid_rollo` | Blind: cover entity | for example `cover.garage_blind`; reads `current_position` |
| `oid_modus` | Mode: entity | for example `input_boolean.blind_manual`; off = automatic, on = manual |

Each binding has its own inversion. **Invert blind** reverses both display and written position (`100 − position`). Normally 0 means closed and 100 means open. Unknown values remain unknown after inversion. The contact is read-only. An optional **A/M** symbol displays the mode; `?` indicates an unknown mode.

![Installed Technic set and HA bindings in the editor](/images/grafik-visual-studio/technic-window-editor.png)

## Controls

In runtime, clicking the window opens a dialog with a position slider, quick values **0 / 25 / 50 / 75 / 100%** and an optional mode toggle. Keyboard control is supported; Escape or **Close** dismisses the dialog. The blind action uses only `cover.set_cover_position` for the selected entity. Availability and SET_POSITION support in `supported_features` are checked before writing. Mode writes only target available `input_boolean` or `switch` entities. Sensors remain read-only displays.

The mode helper represents the switch only: configure the actual blind automation in Home Assistant. No automation is generated or disabled. Failed actions display a retry message; pending actions are not sent twice.

![Runtime dialog with blind position and mode controls](/images/grafik-visual-studio/technic-window-runtime.png)

## Preview and export

**Preview** provides open-window, blind-position and manual-mode values. These apply only to unbound displays in the editor. Bound entities use live values. In runtime, unbound or missing values remain unknown and never use preview fallbacks. Editor clicks never trigger HA control actions.

All display settings, three entity bindings, inversions, preview values and read-only state remain in project and widget exports. Verification used simulated HA entities; real blind control needs testing with your hardware.
