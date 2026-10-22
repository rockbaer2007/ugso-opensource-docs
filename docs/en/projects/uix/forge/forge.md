---
title: UIX Forge
description: UIX Forge visual editor preview for cards and badges, based on the canonical English documentation.
---
# UIX Forge

UIX Forge combines template-driven Home Assistant elements, Sparks and UIX styling. The [canonical English reference](https://github.com/Lint-Free-Technology/uix/blob/1badf70befb9c9d3d7b06c0eced75af7d552aff1/docs/source/forge/forge.md) is authoritative. This condensed guide covers the newly documented editor; it does not replace the full reference.

## Visual editor — Cards and Badges {#visual-editor-cards-and-badges}

::: info Preview available in UIX 9.0.0-beta.2
Canonical revision `1badf70` explicitly marks the Forge visual editor as available in **9.0.0-beta.2**, separate from this site's stable 8.4.0 documentation baseline.
:::

Choose a HA card or badge, edit it with its normal HA editor, then add Forge templates, Sparks, UIX styling and Foundries. Without a selection, Forge uses its built-in blank card or badge. That automatic type choice and the selected editor tab are not saved in the dashboard configuration.

### Native

**Choose/Change native element** explicitly selects or replaces the Native element while preserving Forge template values. Cancel leaves the picker without a selection; normal HA cancellation and dashboard undo remain available after selecting. The incomplete **Manual** choice is not saved without a concrete type. Switching code/visual mode is disabled without a suitable HA visual editor.

The collapsed styling section edits the contents of `element_base.uix`, without an outer `uix:` key. Outer HA card visibility/layout controls are blocked; use `forge.hidden` and `forge.grid_options`. Copy an ordinary card in HA and use **Paste configuration** in Forge's Native picker to preserve its complete configuration, native templates and UIX styles in `element_base`. Only Forge-controlled changes belong in `element`.

### Forge

The complete Forge YAML remains available in code mode. Visual mode contains:

- **General:** `mold` locked to `card`/`badge`, `hidden` and grid rows/columns. Templates remain source; literal numbers and booleans retain their types. A whole `grid_options` template stays intact until explicitly replaced with row/column values. **Control** holds `show_error`, `template_nesting`, `delayed_hass`; the styling section edits the contents of `forge.uix`.
- **Billets:** local names and scalar values; `~` means `null`. Resolved Foundry billets appear separately for overrides. Mappings and lists remain in code mode.
- **Macros:** names, return status, parameters with optional scalar defaults and template source. Numbers, booleans and null survive. `custom_templates` imports remain in code mode; resolved Foundry macros appear separately.
- **Sparks:** choose a registered Spark and its supported options. Values remain template/code text, YAML objects/lists or explicit `null`. New options begin as null; replacing existing sources with an object or null requires confirmation. Full configuration and removal remain available in code mode.

Forge, Native and styling YAML editors retain typed source, comments and temporarily invalid YAML. Invalid YAML is not written into the configuration.

### Element

This tab edits the `element` overlay; Native retains `element_base`. The path table supports editing, enabling/disabling and removal. New custom paths start as active `null`. The separate styling section edits the contents of `element.uix`.

**Apply** writes a valid draft, enables a disabled template and stays open. **Apply & exit** applies changes and returns to the table, or simply returns if unchanged. **Exit** confirms unapplied changes. Invalid YAML stays editable but disables both apply actions. String templates use HA's template editor and test control; enter bare source without extra YAML quotes.

**Convert to object mapping** confirms and starts an empty object. **Set to null** explicitly clears the matching base value. Use **Disable** or **Remove** to use the base instead. An empty string is a distinct valid replacement, not null or removal. Disabling retains source in `element` and its path in `element_disabled_paths`. A disabled parent suppresses its subtree while preserving child states. Arrays and structural templates are edited as whole replacements.

With a base present, its top-level `type` is not a template field. Enable/disable requires a Native selection; valid inherited disabled paths stay intact. Converting an existing direct Card/Badge Forge moves only `element.type` into `element_base.type`.

### Foundry

The picker shows resolved `forge.mold` and `element.type`. A mold mismatch is red, disabled and last. A type mismatch requires confirmation and clears local Native configuration while retaining Element values. Invalid, missing or cyclic inheritance chains are omitted. Dynamic or non-string types and inherited `element_base` remain YAML-only.

A read-only, 200px-high YAML view displays the resolved named Foundry and its named ancestors, excluding global Foundries and local card values. A concrete Foundry type sets and locks the Native type. Clear or replace the Foundry to change it. Global type anchors are protected too; changes exposing an incompatible global type are refused.

A notice below the tabs names the active Foundry. Direct `config.entity` references in Forge/Element templates or the selected Foundry expose **Global Forge entity (in use)** for the outer Forge entity. It is not passed to the wrapped element. Macro-only references cannot be inferred; set the outer `entity` in YAML for those.

### Export

Copy-only Foundry YAML preserves `foundry: <name>`, local Native `element_base` and active Element values, including unchanged native templates. It does not evaluate templates or save a Foundry. Global Foundries, outer `entity` and disabled paths are excluded; an empty `forge.sparks` list is omitted. Only take Foundry `element_base` from this export rather than hand-authoring it. Clearing inherited Forge arrays is not offered visually.

Rows, picture elements, card features, cross-context molds, dynamic types and configurations that cannot safely be represented still require YAML. See the canonical reference above for the full YAML reference and examples.
