---
title: UGSo Special
description: Animated SVG lines and summing nodes for ioBroker VIS 2.
---

# UGSo Special

**UGSo Special** visualizes data flows in VIS 2, such as power readings from several devices. The set contains two widgets.

## Widgets

- **SVG-Line** connects points with straight, right-angle or waypoint routes. Colors, dash lengths and arrowheads are configurable. Positive values animate forward, negative values reverse the direction, and zero stops the animation. Speed can be fixed or proportional to the absolute value.
- **SVG LineBox** adds up to four input lines and an optional correction value. It can send the total to up to two output lines or write it in the runtime view to an existing writable numeric state under `0_userdata.0`. If a selected input is unavailable, the node waits for its value.

In the editor, drag a yellow endpoint to snap it to another line or LineBox. An endpoint with an arrowhead cannot snap. Snapping aligns the graphics; configure value routing separately in the LineBox.

## Installation

### Catalogue preparation 0.1.34

This release includes complete release notes in all eleven catalogue languages, corrected package dependencies, automated linting and ioBroker package checks. Releases use GitHub Actions with npm provenance. bluefox is listed as an npm co-owner. Inclusion in the official catalogue remains pending; widget features and existing projects are preserved.

The package is now named `iobroker.vis-2-widgets-ugso-special`.
Export existing VIS 2 projects as a backup, install the new package and restart VIS 2.
Check the projects before removing the previous package.
Widget template IDs and the internal federation name are retained.

A running VIS 2 installation is required. Install the widget set from its GitHub URL in ioBroker Admin (expert mode). Restart VIS 2 after updates to load the new version. Both widgets appear under **UGSo Special** in the editor palette.

- [GitHub](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special)
- [Releases](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special/releases)
- [npm](https://www.npmjs.com/package/iobroker.vis-2-widgets-ugso-special)
