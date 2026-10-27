---
title: Interactive widgets
description: Universal, radial slider and Inventwo comparison from Studio 0.1.295.
---

# Interactive widgets

**Studio 0.1.296:** The remaining 62 widget types also provide DE/EN/FR properties and messages, optional Climate controls, and checks for HA sources, attributes and units. Existing projects and package versions remain valid; new groups start disabled. [Guide and limits](./ha-quellen-climate). Simulated checks do not replace tests with real devices or the Companion app.

**Studio 0.1.295** adds the main functional groups from the [Inventwo VIS-2 review](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/inventwo-interactive-audit-2026-10-12.md). [Deutsch](/projects/grafik-visual-studio/interaktiv) · [Français](/fr/projects/grafik-visual-studio/interaktiv).

## Universal

In addition to switching and the existing state cycle, choose fixed button values, hold values restoring the previous state, bounded increase/decrease, Studio page navigation, configurable page dialogs or HTTP requests. Legacy buttons keep cycling unless a new option is explicitly selected. Existing property groups and settings are retained.

Default/individual state content now also includes **Embedded view**, **Color picker** and **Analog clock**. Views support fit-to-size and recursion protection. Color box/wheel, HSV/RGB sliders and optional alpha/Kelvin are available. HEX, HEX8, RGB, HSL, HSV and CIE xy can go to text helpers; HA lights receive validated RGB/Kelvin commands. Alpha applies to HEX8, not HA RGB. The clock uses browser time with optional numbers/seconds and configurable colors.

**Interactive language** selects DE/EN/FR for Universal and radial sliders independently of the shell. User text, entity/page names and technical values are preserved.

## Radial slider and previews

Track, active track and thumb support CSS colors or `linear-gradient(90deg, red, rgb(255,200,0) 50%, green)`, with percentage stops and directions such as `to top`. Style inheritance and existing solid colors remain valid.

Interactive previews fill their frames since 0.1.294. From 0.1.295 Material Design icons and their symbol area are also larger in the sidebar/selector. Only the Studio update is required.

## Behavior and limits

HTTP GET runs in the browser with a 15-second timeout, without Studio credentials or a server proxy. CORS and mixed-content rules apply. The navigation PIN is an interface barrier stored in the project, not authorization. Browser/network failure may prevent hold-value restoration; critical devices need a HA-side timeout.

Studio uses HA entities and project pages. Separate arbitrary ioBroker color-component bindings and every Inventwo clock detail are not reproduced; exact pixel parity is not claimed. The overall shell remains DE/EN. [Detailed DE/EN/FR guide](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/universal-0.1.295.md).
