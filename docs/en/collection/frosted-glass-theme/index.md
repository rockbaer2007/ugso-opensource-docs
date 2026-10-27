---
title: Frosted Glass Theme
description: English short note about Frosted Glass Theme for Home Assistant.
---
<a id="current-focus"></a>

# Frosted Glass Theme {#frosted-glass-theme}

Frosted Glass Theme is a modern theme for Home Assistant. It relies on transparent cards, blurring, rounded surfaces, light and dark versions as well as optional Lite versions without blur for weaker devices.

::: warning Unofficial note
This page is not official documentation of the project. It summarizes the most important installation and usage instructions in English. The original repository remains authoritative.
:::

| field | Value |
| --- | --- |
| Original project | [wessamlauf/homeassistant-frosted-glass-themes](https://github.com/wessamlauf/homeassistant-frosted-glass-themes) |
| Verified commit | [`8cb950369e64444bcdc068f7f90283d58f65d80d`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/commit/8cb950369e64444bcdc068f7f90283d58f65d80d) |
| Release | [`v1.3`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/releases/tag/v1.3) |
| License | [MIT](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/blob/main/LICENSE) |
| Category | HA Dashboard -> Themes |

## Installation {#installation}

The theme can be installed via HACS.

1. Install HACS if not already installed.
2. Install `card-mod` or `UIX`.
3. Install Frosted Glass Theme via HACS.
4. Restart Home Assistant.
5. Select the theme in the user profile.

Direct link:

[Open Frosted Glass Theme in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=WessamLauf&repository=homeassistant-frosted-glass-themes&category=theme)

::: warning card-mod or UIX required
The theme requires `card-mod` or `UIX` for blur and styling effects to work correctly.
:::

## Variants {#varianten}

The repository contains several theme files:

- `Frosted Glass.yaml`
- `Frosted Glass Light.yaml`
- `Frosted Glass Dark.yaml`
- `Frosted Glass Lite.yaml`
- `Frosted Glass Light Lite.yaml`
- `Frosted Glass Dark Lite.yaml`

The Lite versions do without blur effects. This is particularly useful on older tablets, weak hardware or when dropdowns are displayed incorrectly due to blur effects.

## Theme Manager {#theme-manager}

There is a separate integration project to customize colors and background images:

- [Frosted Glass Theme Manager and UIX Trial Variant](/en/collection/frosted-glass-manager/)

## Known clues {#bekannte-hinweise}

- Text-only Markdown cards still receive the theme's glass/border styling.
- Blur can interfere with dropdowns in HACS or deeper Home Assistant menus.
- `stack-in-card` can be difficult due to deeply nested styles.
- Lite versions are usually the better choice on low-performance devices.

Disarm Plain Markdown Card using `card_mod`:

```yaml
card_mod:
  style: |
    ha-card {
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
      box-shadow: none !important;
      border: none !important;
    }
    ha-card::before {
      content: none !important;
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
    }
```
