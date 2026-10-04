---
title: Material Design
description: External Material Design widget package for Grafik Visual Studio.
---

# Material Design

## Complete widget catalog (package 1.0.0, Studio 0.1.215 or later)

The external package now contains **49 widget entries**. Besides palette preview and dialogs, it includes every button/icon-button variant, Input, Select, Autocomplete, Checkbox, Switch, Slider, Slider Round, Value, HTML Card, Icon, Installed Version, linear/circular progress, List, Icon List, Table, Alerts, four charts, Calendar, Top App Bar, Grid/Masonry Views and both Advanced View variants.

**Autocomplete:** Choose editor entries, a JSON list, semicolon-separated values or Home Assistant entity options. Write mode accepts free text; select mode rejects unknown entries. Typing filters the menu; arrow keys, Enter and Escape work. Advanced options add input layout, prefix/suffix, helper text, counter, icons and menu colors/fonts. “Refill fields from entity” copies the name, unit, options and available slider limits.

**Data and actions:** Toggles use switch/input_boolean, numeric/text writes use input_number/input_text and selection uses select/input_select. Sensors and attributes stay read-only. Values/actions without an entity work locally for previews. Lists support editor/JSON rows; tables sort from their headers. Alerts acknowledge a local queue, writable JSON entity or separate acknowledgment entity. JSON Chart accepts `axisLabels/graphs`, `labels/datasets` or point lists. History reads HA Recorder for up to ten entities and 1–168 hours. Calendar and page layouts use existing Studio features; recursive page chains are blocked.

An [importable comparison project](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/materialdesign-widgetvergleich.json) provides nine widget pages plus a reference page without real HA entities. Exact visual parity and detailed options are reviewed widget by widget afterwards. ioBroker theme IDs, adapter states and bindings are not imported automatically; multiple Y axes, stacked bars, ioBroker timed locks and HTML list text are currently absent. HTML cards isolate markup in a sandbox.

Register package **1.0.0**, minimum Studio **0.1.215**, MIT license. The website requires **0.1.13** to recognize `material-widget` and packages with up to 64 widgets, 40 property groups and a 500 KB manifest. Previously published versions stay immutable. The first three definitions remain compatible with additive updates from 0.3.0.

## Dialog iFrame (package 0.3.0, Studio 0.1.214 or later)

The third widget opens an HTTP/HTTPS source or relative path in a dialog. **General**, **iFrame settings** and **Dialog layout** remain visible in compact mode. Advanced options add button, header and footer layouts; hiding them preserves existing values.

Configure the source and horizontal/vertical scrolling under **iFrame settings**. **Seamless** removes the border. The default sandbox allows scripts/forms; **Disable sandbox** explicitly removes the restriction. Cross-origin scrolling depends on the browser and embedded content. The target site's CSP or X-Frame-Options may prevent embedding. Studio does not provide a proxy.

Button or boolean triggers, fullscreen threshold and closing behavior follow the local page dialog. The editor does not open dialogs. Studio's page theme replaces ioBroker theme objects.

Register package **0.3.0** with minimum Studio version **0.1.214**. The catalog requires website update **0.1.12** to recognize `material-iframe-dialog`. The already approved 0.2.0 version remains unchanged.

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
