---
title: Tool package interface
description: Create and install local editor tools for HA Grafik Visual Studio.
---

# Tool package interface 0.1

Under **Settings → Tools**, you can install a local `*.tp.zip`. Tool packages extend the editor, not the widget palette or runtime. Interface 0.1 supports one declarative action: setting the current page's background color. **Run** opens a preview; only **Apply** commits the change. **Undo** can revert it, and normal project saving persists it. Installation itself does not run an action.

## Build a package

The ZIP contains a UTF-8 `manifest.json` and optionally referenced SVG or PNG images under `icons/`. No other files are allowed. Package IDs use dot-separated parts; tool IDs use the package namespace. Package versions have the form `x.y.z`. A package contains 1 to 20 tools.

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

1. Create a ZIP such as `page-color.tp.zip` with `manifest.json` and any referenced images.
2. Select it under **Settings → Tools**. The list shows the package ID, version, license and tools.
3. Open the tool preview with **Run** and confirm the page change with **Apply**.

Packages can be removed from the Tools tab. Custom scripts, Home Assistant services, external URLs, GitHub installation and updates are not part of 0.1 yet. See the planned compatibility and extension points in the [tool rules in the source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/tool-rules.md).
