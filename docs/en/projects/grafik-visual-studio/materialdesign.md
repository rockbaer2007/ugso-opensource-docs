---
title: Material Design
description: External Material Design widget package for Grafik Visual Studio.
---

# Material Design

## Dialog (package 0.2.0, Studio 0.1.211 or later)

The second widget opens another local Studio page in a modal. Select the target under **General → View**. Editor clicks select the widget; runtime clicks open the dialog. Self-embedding and recursive page chains are blocked.

Without **Show advanced options**, only General and Dialog layout are visible. Enabling it reveals Button layout, Header layout and Dialog footer button layout. Hiding these groups preserves their values. Size, edge spacing, colors, backdrop and fullscreen threshold are configurable. Close using the button, Escape or optional outside click.

A boolean entity can also open the dialog. Closing turns off `switch` or `input_boolean` triggers. Other entities remain unchanged and require a new off/on transition to reopen after local dismissal. Vibration and click sound depend on browser/device support. Symbols use text/Unicode without importing ioBroker's image catalog or theme objects.

The catalog website must accept the `material-dialog` renderer for package 0.2.0. The local website update replaces only `src/package.php`. Submit version 0.2.0 with minimum Studio version 0.1.211 through the registration form, then review and approve it.

The external [UGSo Material Design](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign) starts with **Preview Color Schemes**. Package **0.1.0** requires Studio **0.1.210** or newer and uses MIT. It is inspired by [ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign); the typhosj and Scrounger copyright and license are included.

The preview displays all **26 palette rows**. Classic uses a white surface; Material 3 supports light and dark surfaces. Swatches remain identical across styles. The heading and widget size are configurable; scroll to reach additional rows and wide palettes.

- **Design style:** Classic, Material 3 or Project default.
- **Project default:** select the style under Settings → General → Material Design.
- **Color theme:** Project default follows the page's light/dark theme; Light and Dark override it for this widget.

The widget reads no Home Assistant entity and writes no states. Studio's page theme replaces ioBroker's `__mdwThemeDark` binding. The ioBroker “Use theme” button is not a Studio theme import.

## Test package registration

The `.wg` file and SHA-256 are in the repository's `dist/` folder. Submit through **Widget registration** in the [package catalog](https://visualstudio.ugso-software.de/?lang=en), with ID `ugso.materialdesign`, version `0.1.0`, MIT license, repository URL and minimum Studio version `0.1.210`. The package appears in Studio only after review and approval. It is not automatically seeded as a bundled package.

For local testing, use Settings → Widget packages → Local. For GitHub installation, use the direct `.wg` file URL. Further widgets will be added progressively using screenshots and exports.
