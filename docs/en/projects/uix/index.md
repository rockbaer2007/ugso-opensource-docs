---
title: About
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.2.0-beta.1**, revision [9528baa](https://github.com/Lint-Free-Technology/uix/commit/9528baaee9cedc2cfb862cda2d6391b8a1fc647c), reviewed 2026-11-23. Stable baseline on this site: **9.1.0**. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# UI eXtension for Home Assistant

![light-logo-icon](/projects/uix/assets/images/mixed.png)

## What is UI eXtension?

::: info Card-mod users
If you are migrating from Card-mod check out the [FAQ](/en/projects/uix/faq) where most of your questions will be answered. If you need to ask anything further, use the [GitHub discussions](https://github.com/Lint-Free-Technology/uix/discussions).

:::

With an ever growing number of features that go beyond cards and dashboards, UI eXtension (UIX) was created to keep pushing the boundaries of custom CSS across your Home Assistant UI. UIX comes from the heritage of [card-mod](https://github.com/thomasloven/lovelace-card-mod) by [@thomasloven](https://github.com/thomasloven)

UI eXtension consists of [UIX Styling](./using/index.md), [UIX Forge](./forge/index.md) and [UIX Broker](./broker/index.md). [UIX Styling](./using/index.md) allows for applying CSS styles to (nearly) any Home Assistant Frontend element. [UIX Forge](./forge/index.md) provides a way to forge Home Assistant elements (cards, badges, rows etc.) allowing for templates for all of the element's configuration, as well as additional advanced augmentation of the element through [UIX Forge Sparks](./forge/sparks/index.md). UIX Broker turns browser events, keyboard shortcuts, and Home Assistant event-bus events into declarative interactions. An interaction selects a browser element, checks optional rules, then runs directives in their configured order.

## 🚀 Quick Start

Go to [Quick Start](./quick-start.md) for installation instructions and a short guide on making your first UIX Styling and UIX Forge.

## ➡️ Next up

- [Using UIX Styling](./using/index.md)
- [Using UIX Forge](./forge/index.md)
- [FAQ](/en/projects/uix/faq)
