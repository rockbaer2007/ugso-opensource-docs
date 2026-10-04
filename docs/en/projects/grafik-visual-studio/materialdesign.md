---
title: Material Design
description: External Material Design widget package for Grafik Visual Studio.
---

# Material Design

The external [UGSo Material Design](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign) starts with **Preview Color Schemes**. Package **0.1.0** requires Studio **0.1.210** or newer and uses MIT. It is inspired by [ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign); the typhosj and Scrounger copyright and license are included.

The preview displays all **26 palette rows**. Classic uses a white surface; Material 3 supports light and dark surfaces. Swatches remain identical across styles. The heading and widget size are configurable; scroll to reach additional rows and wide palettes.

- **Design style:** Classic, Material 3 or Project default.
- **Project default:** select the style under Settings → General → Material Design.
- **Color theme:** Project default follows the page's light/dark theme; Light and Dark override it for this widget.

The widget reads no Home Assistant entity and writes no states. Studio's page theme replaces ioBroker's `__mdwThemeDark` binding. The ioBroker “Use theme” button is not a Studio theme import.

## Test package registration

The `.wg` file and SHA-256 are in the repository's `dist/` folder. Submit through **Widget registration** in the [package catalog](https://visualstudio.ugso-software.de/?lang=en), with ID `ugso.materialdesign`, version `0.1.0`, MIT license, repository URL and minimum Studio version `0.1.210`. The package appears in Studio only after review and approval. It is not automatically seeded as a bundled package.

For local testing, use Settings → Widget packages → Local. For GitHub installation, use the direct `.wg` file URL. Further widgets will be added progressively using screenshots and exports.
