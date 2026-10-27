---
title: NeoMorphix UIX
description: English short note for the NeoMorphix UIX Home Assistant theme.
---
<a id="current-focus"></a>

# NeoMorphix UIX {#neomorphix-uix}

NeoMorphix UIX is a UIX variant of the NeuMorphix Home Assistant theme. It relies on soft shadows, round surfaces and a slightly three-dimensional look for dashboards.

::: warning Unofficial note
This page is not official documentation of the project. It summarizes the most important installation and usage instructions in English. The original repository remains authoritative.
:::

| field | Value |
| --- | --- |
| Original project | [yakidd/NeumorphixHome](https://github.com/yakidd/NeumorphixHome) |
| Verified commit | [`269c298e47b02faaac4f08c8c9dfccf49d70d860`](https://github.com/yakidd/NeumorphixHome/commit/269c298e47b02faaac4f08c8c9dfccf49d70d860) |
| Release | [`1.0.3`](https://github.com/yakidd/NeumorphixHome/releases/tag/1.0.3) |
| UIX fork | [rockbaer2007/NeoMorphix-UIX](https://github.com/rockbaer2007/NeoMorphix-UIX/tree/experiment/uix-theme-variant) |
| License | according to README: WITH |
| Category | HA Dashboard -> Themes |

## Installation {#installation}

NeoMorphix UIX is based on NeuMorphix and is prepared as a HACS theme variant.

[![Open NeoMorphix UIX in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=NeoMorphix-UIX&category=theme)

1. Install HACS if not already installed.
2. <a href="https://uix.lf.technology/quick-start/" target="_blank" rel="noopener noreferrer">UIX Install</a>.
3. Install the NeoMorphix UIX fork as a theme via HACS.
4. Restart Home Assistant.
5. Select a NeoMorphix UIX variant in the user profile or dashboard settings.

The theme integration must be active for Home Assistant:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

The original NeuMorphix version uses card-mod. NeoMorphix UIX requires UIX instead.

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

## Variants {#varianten}

The original project provides two theme files:

- `themes/neumorphix.yaml`
- `themes/neumorphix-inset.yaml`

This includes six theme variants:

- `neumorphix-light`
- `neumorphix-dark`
- `neumorphix-claude`
- `neumorphix-light-inset`
- `neumorphix-dark-inset`
- `neumorphix-claude-inset`

`Raised` acts like a raised surface. `Inset` appears to be pressed in or embedded in the surface.

## UIX variant {#uix-variante}

A supplementary branch was created for UIX, which does not replace the original card-mod files, but adds additional UIX theme files:

- [UIX branch in fork](https://github.com/rockbaer2007/NeoMorphix-UIX/tree/experiment/uix-theme-variant)
- [Pull Request to Original Project](https://github.com/yakidd/NeumorphixHome/pull/4)

The UIX branch adds:

- `themes/NeoMorphix UIX.yaml`
- `themes/NeoMorphix UIX Inset.yaml`

The additional theme names are:

- `NeoMorphix UIX Light`
- `NeoMorphix UIX Dark`
- `NeoMorphix UIX Claude`
- `NeoMorphix UIX Light Inset`
- `NeoMorphix UIX Dark Inset`
- `NeoMorphix UIX Claude Inset`

Technically, the additional files were mapped to UIX theme keys:

- `card-mod-theme` -> `uix-theme`
- `card-mod-root-yaml` -> `uix-root-yaml`
- `card-mod-sidebar-yaml` -> `uix-drawer-yaml`

## Notes {#hinweise}

- The original project lists MIT as a license in the README, but does not have a separate `LICENSE` file in the repository.
- The UIX variant is intended as a supplement. The existing card mod files remain unchanged.
- With the inset variants, the main settings page of Home Assistant may react differently because this interface is rendered differently than normal dashboards.
