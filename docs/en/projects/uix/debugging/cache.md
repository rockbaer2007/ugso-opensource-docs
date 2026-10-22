---
title: Clearing cache
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision [26e54e6](https://github.com/Lint-Free-Technology/uix/commit/26e54e6d4973231a393933e6479ed1b03cc86cd3), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Clearing Home Assistant Frontend application cache

If at any time you need to clear the Home Assistant Frontend Application cache, which is used in addition to Browser cache, you can use a custom action to clear the Home Assistant Application cache and reload the Browser. This can be very convenient especially for devices where the option is hidden in a debugging menu and will also clear more than just the Frontend Application cache (e.g. localStorage which clears out many stored items like Browser Mod Browser ID).

See [`clear_cache`](../extras/uix-actions.md#clear-cache-clearing-home-assistant-frontend-cache) UIX action.
