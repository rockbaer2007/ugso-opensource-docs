---
description: Learn about UI eXtension concepts such as DOM navigation and how UIX patches and applies to UI elements in Home Assistant.
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.1.0-beta.2**, revision [509b2c2](https://github.com/Lint-Free-Technology/uix/commit/509b2c2475ce6b574876a8353f88aedf87e7b2e3), reviewed 2026-11-09. Stable baseline on this site: **9.0.0**. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# UIX Concepts

UI eXtension does its magic by patching various functions of HTML elements used by Home Assistant Frontend to inject a UIX styling node, `<uix-node>` where styles are injected into the DOM. To get the most out of UIX you can either use [UIX Guides](../guides.md) to follow what others have created, or work it out yourself.

## Concept resources

- [DOM navigation](dom.md)
- [UIX application](application.md)
- [UIX contexts](context.md)
