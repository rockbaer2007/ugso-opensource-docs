---
description: Information for developers of themes and integrations.
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision [26e54e6](https://github.com/Lint-Free-Technology/uix/commit/26e54e6d4973231a393933e6479ed1b03cc86cd3), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Developers - Themes & Integrations

When using UI eXtension in a theme please **DO NOT** attempt to ship any part of the UI eXtension integration standalone. Always guide your theme users to the UI eXtension Quick Start Guide to install the integration.

When using UI eXtension alongside another custom integration, please set UI eXtension as a dependency in your `manifest.json`. That way users will be required to install UI eXtension before they can use your integration.

If you have any question please start a [GitHub discussion](https://github.com/Lint-Free-Technology/uix/discussions).
