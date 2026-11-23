---
title: Clearing cache
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.2.0-beta.1**, revision [9528baa](https://github.com/Lint-Free-Technology/uix/commit/9528baaee9cedc2cfb862cda2d6391b8a1fc647c), reviewed 2026-11-23. Stable baseline on this site: **9.1.0**. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Clearing Home Assistant Frontend application cache

Use the custom action to clear the Home Assistant frontend application cache and reload the browser, particularly on devices where the normal cache control is hidden in a debugging menu. **`localStorage` remains untouched**, including stored values such as the Browser Mod browser ID. Clearing this cache is different from deleting all browser or app data.

::: info Editorial clarification
The archived upstream prose was contradictory about `localStorage`. The [implementation of `clear_cache()` in the reviewed revision](https://github.com/Lint-Free-Technology/uix/blob/26e54e6d4973231a393933e6479ed1b03cc86cd3/src/ll-custom-actions.ts#L224-L242) deletes Cache Storage entries and reloads the page; it does not clear `localStorage`.
:::

See [`clear_cache`](../extras/uix-actions.md#clear-cache-clearing-home-assistant-frontend-cache) UIX action.
