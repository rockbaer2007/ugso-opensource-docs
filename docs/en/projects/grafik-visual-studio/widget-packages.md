---
title: Widget package interface
description: Create and install local widget packages for HA Grafik Visual Studio.
---

# Widget package interface

## External Industrial set: Gauge/Poti

Studio **0.1.223** adds the API 0.2 host renderer `industrial-gauge`. The optional **UGSo Industrial 0.1.0** set starts with **Gauge/Poti – 270°**. [Download the package](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) and install it through **Settings → Widget packages → Local**. It is not installed automatically and contains no executable package code.

The square widget starts at **64 × 64 px**. Without an input, runtime supports rotary control by mouse, touch or keyboard. An entity or enabled signal input selects read-only gauge mode; an unavailable input remains an error. Signal input takes precedence over the entity. Choose ticks with emphasized zero or a color ring with ascending upper limits. Negative bounds, initial value, tick division and an independent control step are configurable. The final band ends at the maximum.

Output to `number.*` or `input_number.*` is committed on release or continuously while dragging; changed gauge values are forwarded. The entity must be available and writable. Input and output entities must differ. Visible and visually hidden value lines use the existing dataflow. Editor interaction and writes are disabled.

Industrial styling adds four corner screws and a **2 px CSS border**. Studio **0.1.224** applies **General CSS → Corner radius (px)** to this frame. **Housing snap points** offers four independently enabled corners and one spacing value for all sides. With 1 px on each neighbor, the gap is 2 px; single widgets snap when dragged. Set the color in **Settings → General → Editor and dock points → Housing snap point color**. Existing package 0.1.0 remains usable. Signal ports stay separate; automatic port relocation follows later. [Source and instructions](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial).

## Further interface changes

Studio **0.1.228** groups **Show value**, **Unit**, **Value position**, **Font size (px)** and **Font color** under **Value display**. Choose **Center** or **Bottom**. The bottom position sits below the rotary knob. Defaults are bottom, 12 px and a light font color; font size remains constant when resizing the widget. Existing industrial package 0.1.0 does not need reinstalling.

Studio **0.1.227** makes **Show value** display the reading with its unit. An empty unit uses the Home Assistant input entity's `unit_of_measurement`. Invalid color thresholds or scales no longer hide an available reading; the warning remains in the tooltip. After changing scale limits, adjust the color thresholds to fit the range in ascending order.

Studio **0.1.226** adds a checked-by-default **1:1 aspect ratio** checkbox under **Size** for Gauge/Poti. Width and height stay equal during dragging and typed changes, with both property fields updating. Uncheck it for independent dimensions, each at least 64 px. Re-enabling the lock uses the larger dimension for both sides. Existing widgets remain square by default; package 0.1.0 remains usable.

Studio **0.1.225** applies the color selected in **Settings → General → Editor and dock points → Output point** to Value Converter, LineBox and LineBox Math outputs as well. Occupied Math outputs retain that color. Signal outputs and housing snap points have separate color settings.

From **0.1.208**, clicking **Install** without risk confirmation highlights the checkbox in red and scrolls it into view. Checking it clears the highlight.

From **0.1.207**, opening this tab automatically reloads the catalog and current installation status. Removing a package listed in the catalog makes it installable again, even if it was originally installed locally. Newly approved packages appear the next time the tab opens.

Since **0.1.205**, catalog packages and locally installed widget packages appear as **two cards side by side**, each with an icon. The installed package icon is used when available; otherwise a widget icon is shown. Refresh and removal actions remain available for installed packages.

Since **0.1.206**, the more compact **Local / Catalog / GitHub** selector stays visible at the top while scrolling. The entire tab uses **one shared scroll area**; catalog and installed package lists no longer have nested scroll areas.

From Studio **0.1.204**, **Settings → Widget packages** offers **Local / Catalog / GitHub** sources. The [UGSo catalog](https://visualstudio.ugso-software.de/?kind=widget&lang=en) shows descriptions, licenses, minimum Studio versions and installed versions. Test packages carry an orange notice. GitHub supports direct public `.wg` file links, including blob, raw and release links; a repository homepage is not sufficient. Installation requires explicit risk confirmation. Catalog downloads verify SHA-256 and the selected package ID/version before the normal package validation. Settings remain open after installation, while the palette and package list refresh. Standalone helper tools such as the Packer are downloaded through the catalog link.

From Studio 0.1.203, API 0.2 supports `technic-status-list`: up to ten read-only HA rows using the bindings and numeric/AND/OR options from `technic-room`. `valueOffset` and `containerPaddingLeft` control columns and padding. Typography inherits CSS; overflowing rows scroll. The package remains declarative. See [Technic](technic.md#status-list).

From Studio 0.1.202, API 0.2 supports `technic-temperature` with five HA bindings, dial bounds, step and colors. The fixed host checks live capabilities and step grids before `climate.set_temperature` or `input_number.set_value`. History reads HA Recorder for at most three entities, 24 hours or seven days, returning at most 720 points per series. Packages still contain no executable scripts or HA tokens. See [Technic](technic.md#thermostat-temperature).

From Studio 0.1.201, API 0.2 supports `technic-clock` for browser-local time and independently configured dates. The host updates text with one shared ticker. Date names use `Intl`; the space separator is stored as `separator=space`. No entity binding or executable package file is required.

From Studio 0.1.200, API 0.2 supports the `technic-room` host renderer: up to ten read-only HA status rows, numeric formatting, Boolean AND/OR inputs and a local `targetPage`. Room popups survive live updates; navigation and removal close them. Runtime constrains dialog dimensions and prevents recursive embedding. The package contains no executable scripts.

From Studio 0.1.187, **interface 0.2** adds declarative charts alongside 0.1 text widgets. The optional [Weather and Heating](weather-heating.md) set uses this extension. External sets automatically receive an unused palette color separated from existing hues. Assignments remain in this browser across reloads, removal and reinstallation; Basic and built-in sets retain their colors.

## Interface 0.1: text

Starting with Studio 0.1.89, you can install ZIP-based packages ending in `.wg`. Existing `.wg.zip` files remain supported; the extension and manifest must both identify a widget package.

Under **Settings → Widget packages → Local**, you can install a local `.wg` or `.wg.zip` file. Interface 0.1 accepts validated, declarative text widgets. From Studio 0.1.204, they appear directly as a separate set in the palette and work in both editor and runtime. Installation does not execute package code.

## Interface 0.2: chart

The manifest uses `apiVersion: "0.2"` and `render: {"kind":"chart","valueKey":"headline"}`. Declare `headline` as a text field with a default. Instances save definition version 0.2. Manifest and validated icons remain the only allowed package files; Studio uses its own SVG renderer.

The fixed property keys and limits are listed in the [chart contract](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md#widget-paket-schnittstelle-02). It supports up to ten JSON series, line/bar charts, left/right axes, time/category axes and read-only HA state/attribute bindings. Executable formatters and write actions are excluded. Existing 0.1 text packages remain supported.

## Build a package

The ZIP contains a UTF-8 `manifest.json` at its root and optionally referenced SVG or PNG images under `icons/`. From Studio 0.1.197, optional `LICENSE.txt` and `README.md` UTF-8 files of at most 50 KB each are also accepted. They are never executed or displayed as HTML in Studio. No other files are allowed. Package IDs use dot-separated parts, such as `example.widgets`; widget types use the package namespace, such as `example.widgets/label`. Package versions have the form `x.y.z`. A package contains 1 to 30 widgets; each appears as its own entry in the package's palette set.

From Studio 0.1.197, interface 0.2 supports `render: {"kind":"technic-window","valueKey":"heading"}`. The fixed host reads `contactEntityId`, `coverEntityId` (`current_position`, `supported_features`) and `modeEntityId`; `invertContact`, `invertCover`, `invertMode` invert these values. Runtime writes are limited to position control of an available `cover` entity and an `input_boolean`/`switch` mode helper. See [UGSo Technic](technic.md).

From Studio 0.1.198, interface 0.2 adds `render: {"kind":"technic-switch","valueKey":"heading"}`. `entityId` is evaluated using `valueType` bool or number; runtime writes are limited to switch/light/input_boolean or input_number with 0/1. `readOnly` prevents operation. `iconKey`, `iconScale`, `colorAN`/`colorAUS` and caption options configure the fixed renderer.

From Studio 0.1.199, interface 0.2 adds `render: {"kind":"technic-light","valueKey":"heading"}`. `powerEntityId` and `brightnessEntityId` are read separately; brightness comes from light.brightness or a numeric helper. `linkPowerDimmer` links power and percent. The fixed host validates all targets for `/api/light-dimmer`; identical light bindings are combined into one call. Separate targets use sequential HA actions.

```json
{
  "format": "ha-grafik-widget-package",
  "apiVersion": "0.1",
  "id": "example.widgets",
  "name": "Example Widgets",
  "version": "1.0.0",
  "license": "MIT",
  "widgets": [{
    "type": "example.widgets/label",
    "label": "Label",
    "defaults": { "text": "Hello" },
    "propertyGroups": [{
      "label": "Content",
      "fields": [{ "key": "text", "label": "Text", "type": "text" }]
    }],
    "render": { "kind": "text", "valueKey": "text" }
  }]
}
```

`valueKey` points to an editable text or number field. Property field types are `text`, `number`, `checkbox`, `color`, `range` and `select`. Each property needs a matching value in `defaults`. The Studio supplies the shared **General** and **Visibility** groups. A package or widget may also specify `"icon": "icons/name.svg"` or `.png`; the referenced image must be included in the ZIP. Widgets without an image use the built-in SVG text symbol.

The ZIP limit is 2 MB, the manifest limit is 200 KB, and each image is limited to 50 KB. PNG images are limited to 1024 × 1024 pixels; SVG files are checked for inert shapes and attributes. Package and widget images may be SVG or PNG, while Studio action buttons retain their SVG symbols.

## Install and manage

From Studio 0.1.194, interface 0.2 supports `render: {"kind":"heating-params","valueKey":"chosenRoomEntityId"}`. The host reads eight independent `*EntityId` bindings for heating period, holiday, presence, party, guests, holiday at home/vacation away and fireplace mode. `chosenRoomEntityId` is an optional text display. Unbound `*Preview` Boolean values apply only in the editor. Runtime writes are limited to available `input_boolean`/`switch` entities; `readOnly` blocks every row. See [Weather and Heating](weather-heating.md).

From Studio 0.1.193, interface 0.2 supports `render: {"kind":"landlord-notification","valueKey":"messageSubject"}`. The fixed host provides a runtime message form. `notificationService` selects a specific `notify.*` action; `notify.send_message` requires `notifyEntityId`. `messageType` describes the configured channel and `messageSubject` provides the text heading. Submission happens only on Send, never in the editor. Priority is included as text; drafts remain outside the project format. See [Weather and Heating](weather-heating.md).

From Studio 0.1.192, interface 0.2 also supports `render: {"kind":"window-overview","valueKey":"windowPreview"}`. The host reads a JSON room list using `entityId` and optional `tableAttribute`. `openCountEntityId` and optional `openCountAttribute` provide a separate open room count. Without a list binding, the preview value is used; without a count binding, only a fully known, non-empty list is counted. Unknown readings remain unknown. See [Weather and Heating](weather-heating.md).

From Studio 0.1.191, interface 0.2 also supports `render: {"kind":"meteored","valueKey":"meteoredWidgetId"}`. This fixed host mode loads the official Meteored loader in an isolated runtime frame; `enableReload` controls hourly reloading. Packages still contain no scripts or custom loader URLs. The editor shows a configuration preview. Users must configure their provider ID and allowed domain.

From Studio 0.1.190, interface 0.2 also supports `render: {"kind":"room-table","valueKey":"tablePreview"}`. The host reads `entityId` and optional `tableAttribute`, or uses the declared preview value without a binding. It rebuilds passive HTML table elements and selected formatting; executable content and external resources are removed. This mode requires Studio 0.1.190 or later. The optional [Weather and Heating](weather-heating.md) package is the reference implementation.

1. Create a ZIP named, for example, `my-package.wg` with the files above. `my-package.wg.zip` remains supported.
2. Select the local ZIP under **Settings → Widget packages**.
3. Review its package ID, version, API version, widget count and license. Use **Reload** to make the set appear in the palette.

From Studio 0.1.188, the local import may install a higher package version if its identity and all existing widget definitions remain exactly unchanged. It may add new widgets even while existing package widgets are used. Saved projects are not modified. Changes to existing definitions, identical versions and downgrades are rejected. **Remove** remains blocked while any project uses a widget type from that package. GitHub installation and automatic updates are not available yet. Custom scripts, Home Assistant state binding and write actions remain outside interface 0.1.

Later extensions should preserve existing widget behavior. See the complete [widget rules in the source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md).
