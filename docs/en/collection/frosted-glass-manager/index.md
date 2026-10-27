---
title: Frosted Glass Theme Manager
description: Notes on the Frosted Glass Theme Manager and the tested UIX test variant.
---
<a id="current-focus"></a>

# Frosted Glass Theme Manager {#frosted-glass-theme-manager}

The Frosted Glass Theme Manager is a home assistant custom integration for generating customized Frosted Glass theme files. Colors and background images can be set via the Home Assistant interface.

::: warning Unofficial note
This page is not official documentation of the project. The original repository remains authoritative.
:::

| field | Value |
| --- | --- |
| Original project | [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager) |
| Fork with UIX test variant | [rockbaer2007/frosted-glass-manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager) |
| Pull Request | [wessamlauf/frosted-glass-manager#15](https://github.com/wessamlauf/frosted-glass-manager/pull/15) |
| Category | HA integrations |

## Original Manager {#original-manager}

The original manager creates Frosted Glass theme files for normal use with card-mod.

[![Open Frosted Glass Theme Manager in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wessamlauf&repository=frosted-glass-manager&category=integration)

Repositories:

- [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager)

## UIX test variant {#uix-testvariante}

For installations that use UIX instead of card-mod, there is a tested UIX working version as a fork.

[![Open Frosted Glass UIX Theme Manager in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=frosted-glass-manager&category=integration)

Repositories:

- [Frosted Glass UIX Theme Manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager)

The UIX test variant uses its own Home Assistant integration identifier:

- `frosted_glass_uix_manager`

It creates its own theme files and therefore does not conflict with the normal Frosted Glass file names:

- `Frosted Glass UIX Custom.yaml`
- `Frosted Glass UIX Custom Lite.yaml`

The standard backgrounds are supplied locally and copied to Home Assistant when started:

- `config/www/frosted-glass-uix/frosted-glass-light-background.jpg`
- `config/www/frosted-glass-uix/frosted-glass-dark-background.jpg`

They are integrated into the generated themes via `/local/frosted-glass-uix/...`. This means that the standard optics are not dependent on an external CDN.

## Note {#hinweis}

The UIX test variant has already been tested in practice, but remains an experimental variant. For general questions about the original project, you should continue to use the original repository.
