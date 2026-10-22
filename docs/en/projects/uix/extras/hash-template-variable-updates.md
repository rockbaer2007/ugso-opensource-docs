---
title: Disable hash template variable and updates
description: Learn how to disable hash template variable updates and when to use this performance option
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision [26e54e6](https://github.com/Lint-Free-Technology/uix/commit/26e54e6d4973231a393933e6479ed1b03cc86cd3), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Disable hash template variable and updates

By default, UIX exposes `hash` as a template variable and updates templates when the URL hash (`#...`) changes. UIX provides an option to disable this behavior to avoid hash-driven rebinds and Forge updates.

## Setting via the integration UI

The option is **unset by default**. To set the option:

1. In Home Assistant, go to **Settings → Devices & Services → UI eXtension → Configure**.
2. Select **Performance settings** from the menu.
3. Toggle **Disable hash template variable and updates** on.
4. Save.

The setting takes effect immediately across all connected browser sessions — no page reload required.

## Behavior when set

When this option is set:

- The `hash` template variable is **not available**.
- Hash-only URL changes do **not** trigger UIX template rebinds.
- Hash-only URL changes do **not** trigger UIX Forge updates.

::: warning
Any template that references `hash` without default will error while this option is set because `hash` variable is unavailable. If you wish to have this option both set and unset you will need to set a default if you use `hash` variable in templates. e.g. <code v-pre>{{ hash | default(&quot;&quot;) }}</code> or is using in more complex templates set a local variable and then use that variable. `{% set hashWithDefault = hash | default("") %}`
:::
