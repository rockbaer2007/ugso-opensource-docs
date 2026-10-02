---
title: Tool package interface
description: Create and install local editor tools for HA Grafik Visual Studio.
---

# Tool package interface 0.1

Starting with Studio 0.1.89, you can install ZIP-based packages ending in `.tp`. Existing `.tp.zip` files remain supported; the extension and manifest must both identify a tool package.

Under **Settings → Tools**, you can install a local `*.tp.zip`. Installed tools also appear as icons in two rows of the editor toolbar; its toolbox icon opens the Tools tab for management. Tool packages extend the editor, not the widget palette or runtime. Interface 0.1 supports one declarative action: setting the current page's background color. Clicking a toolbar tool icon or **Run** in the Tools tab opens a preview; only **Apply** commits the change. **Undo** can revert it, and normal project saving persists it. Installation itself does not run an action.

## UGSo Colorpicker 1.0.0

**Update 1.1.0 (Studio 0.1.111):** **Save favorite** is available alongside Copy. The separate **Favorites** tab holds up to 15 colors with HEX and names, automatically saved locally in this browser on each change. Duplicate colors do not consume another slot. At capacity, a yellow **Favorites full** message appears and Save is disabled. Delete entries individually; later entries shift forward, leaving free slots at the end. Selecting a favorite returns its color to the picker for copying.

[Download Colorpicker 1.1.0](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-colorpicker-v1.1.0).

This practical add-on tool requires **HA Grafik Visual Studio 0.1.109 or newer**. Download [ugso-colorpicker-1.0.0.tp from the release](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-colorpicker-v1.0.0) and install it under **Settings → Tools**. Open the color-wheel toolbar icon or click **Run**.

- Choose hue and saturation on the wheel; adjust brightness separately or enter HEX directly.
- Select **HEX** or **Color name** and click **Copy**. If browser clipboard access is unavailable, select and copy the output manually.
- The 31,918 names from [meodai/color-names](https://github.com/meodai/color-names) are bundled locally; no internet connection is required. Exact and nearest matches are distinguished using RGB distance.
- Names are labels, not CSS color values. Copy HEX for widget color fields.
- No project or Home Assistant permissions are required; the tool does not modify projects. Left/right arrow keys change hue and up/down change saturation on the wheel.

The new declarative `color-picker` action uses `capabilities: []`. Studio supplies the dialog and color-name data; the data-only package activates the tool. Older Studio versions do not support this action. License and attribution links are available in the dialog. The existing `set-page-background` action remains unchanged.

## Build a package

The ZIP contains a UTF-8 `manifest.json` and optionally referenced SVG or PNG images under `icons/`. No other files are allowed. Package IDs use dot-separated parts; the tool ID uses the package namespace. Package versions have the form `x.y.z`. A tool package contains exactly one tool.

```json
{
  "format": "ha-grafik-tool-package",
  "apiVersion": "0.1",
  "id": "example.tools",
  "name": "Example Tools",
  "version": "1.0.0",
  "license": "MIT",
  "tools": [{
    "id": "example.tools/background",
    "definitionVersion": "0.1",
    "label": "Page color",
    "description": "Sets the current page background.",
    "context": "page",
    "capabilities": ["project.read", "project.write"],
    "action": { "kind": "set-page-background", "defaultColor": "#224466" }
  }]
}
```

`defaultColor` is a six-digit hex color and can be changed in the preview. The listed capabilities apply only to this confirmed editor action; they do not grant package code general write access. A package or tool may optionally reference `"icon": "icons/name.svg"` or `.png`. The file must be present in the ZIP; Studio action buttons continue to use SVG symbols.

The ZIP limit is 2 MB, the manifest limit is 200 KB, and each image is limited to 50 KB. PNG images are limited to 1024 × 1024 pixels; SVG files are checked for inert content.

## Install and manage

1. Create a ZIP such as `page-color.tp` with `manifest.json` and any referenced images. `page-color.tp.zip` remains supported.
2. Select it under **Settings → Tools**. The list shows the package ID, version, license and included tool.
3. Open the preview from the tool icon in the editor toolbar or with **Run** in the Tools tab, then confirm the page change with **Apply**.

Packages can be removed from the Tools tab. Custom scripts, Home Assistant services, external URLs, GitHub installation and updates are not part of 0.1 yet. See the planned compatibility and extension points in the [tool rules in the source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/tool-rules.md).
