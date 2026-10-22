---
title: Always patch ha-card (Experimental)
description: Learn how to enable the patching of ha-card at all times with this experimental setting
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision [26e54e6](https://github.com/Lint-Free-Technology/uix/commit/26e54e6d4973231a393933e6479ed1b03cc86cd3), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Always patch ha-card

By default, UIX does not patch `ha-card` if it cannot find a card config in the first Frontend or custom element in its ancestor DOM tree. This experimental option allows for always patching ha-card element so theme variable `uix-card(-yaml)` can apply. `ha-card` without config may be used on config or custom panels.

When `ha-card` is patched without config the class `type-generic-card` will be added to `ha-card`.

## Setting via the integration UI

The option is **unset by default**. To set the option:

1. In Home Assistant, go to **Settings → Devices & Services → UI eXtension → Configure**.
2. Select **Experimental settings** from the menu.
3. Toggle **Always patch ha-card** on.
4. Save.

The setting is available immediately across all connected browser sessions. A page reload may be required for the setting to take effect.

## Behavior when set

When this option is set:

- `ha-card` is always patched even when there is no card config available.
- When patched in this way the class `type-generic-card` will be added to `ha-card`.
