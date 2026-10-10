---
title: Themes and zoom
description: Saved theme selection and an additional fit control in the Blockly editor.
---
# Themes and zoom

Since **0.1.16**, the toolbar above the workspace includes a **Theme selector**. It affects Blockly categories, flyouts and blocks. The surrounding application UI remains unchanged. There are still 111 block types.

| Choice | Appearance | Upstream source |
| --- | --- | --- |
| UGSo Standard | Existing UGSo group colours, dark menu and light flyout | Own UGSo adaptation based on Blockly Classic |
| Dark | Dark workspace and flyout, with a distinct category-menu background | [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| Modern | Original Modern palette with stronger borders and UGSo extension groups | [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| Tritanopia | Original standard-group palette plus colours for HA-specific groups | [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |

Tritanopia is intended for people with this colour-vision deficiency. Own UGSo blocks and categories now use theme styles instead of fixed colours. Light blocks get dark labels, dark blocks light labels; editable fields remain separately readable. Selected categories have a dark background and light text across palettes. Category names and block labels remain available for orientation. This does not certify complete accessibility.

![Dark in the UGSo editor](/assets/blocks-for-ha/themes/dark.png)

![Tritanopia in the UGSo editor](/assets/blocks-for-ha/themes/tritanopia.png)

## Switching and saving

Themes switch immediately without rebuilding the workspace. Blocks, connections, positions and YAML remain intact. The choice is saved separately from the project in this browser and restored after reload. Project files and YAML do not transfer this display preference to another browser. Unknown preferences fall back to UGSo Standard; when browser storage is blocked, switching still works for the current session.

The existing **Geras renderer** remains active for all themes, preserving connection geometry and controls. Upstream Modern recommends Zelos/Thrasos; here its colour/border palette is used and checked with Geras. Renderer selection is not an additional option in this version.

## Fit all blocks

Original [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) adds the four-arrow icon next to the zoom controls. Clicking fits blocks to the available workspace. The control is reachable with Tab and works with Enter/Space. Zoom changes the view, not the automation.

The existing upper **Einpassen** button remains and caps enlargement at the compact default scale. The plugin uses ordinary Blockly fitting within existing zoom limits. On small screens, the theme toolbar may wrap; the workspace remains scrollable.

All four additional original plugins are pinned to **13.3.0**, integrated with Blockly **13.3.0**, and licensed under Apache-2.0. The six existing plugins remain on 13.2.0. Packages are bundled locally without external theme files or CDN dependencies. Upstream links and notices are also in the [block catalog](./blocks).

Verified: four themes, labels on light Tritanopia blocks, unchanged project/YAML output, saved choice, unknown/blocked storage preferences, fitting and mobile width. This display change does not alter HA execution.
