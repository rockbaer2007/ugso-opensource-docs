---
description: Learn about UI eXtension concepts such as DOM navigation and how UIX patches and applies to UI elements in Home Assistant.
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.8**, revision [e4a1caa](https://github.com/Lint-Free-Technology/uix/commit/e4a1caa6437f88282cfe04d768d3c11df387fc42), reviewed 2 November 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# UIX Concepts

UI eXtension does its magic by patching various functions of HTML elements used by Home Assistant Frontend to inject a UIX styling node, `<uix-node>` where styles are injected into the DOM. To get the most out of UIX you can either use [UIX Guides](../guides.md) to follow what others have created, or work it out yourself.

## Concept resources

- [DOM navigation](dom.md)
- [UIX application](application.md)
