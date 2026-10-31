---
title: UIX Broker
description: Create declarative frontend event interactions for Home Assistant with UIX Broker.
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.6**, revision [e6fb84d](https://github.com/Lint-Free-Technology/uix/commit/e6fb84dd715ea4bac9a330357705897ea8d44690), reviewed 31 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# UIX Broker

UIX Broker turns browser events, keyboard shortcuts, and Home Assistant event-bus events into declarative interactions. An interaction selects a browser element, checks optional rules, then runs directives in their configured order. The `block` directive is an exception: it blocks the initiating event synchronously before the remaining directives run.

```text
Realm → Listen → Interaction anchor → Rules (Optional anchors) → Directives (Optional anchors)
```

Use UIX Broker when an interface behaviour can be configured rather than written as a custom card, script, or patch. UIX Broker can react to a click, customise an event before redispatching it, focus an element, update an object property, and invoke a safe element method. It can also add buttons, badges, text, tile icons, tooltips, and unlock challenges; bind or run Home Assistant actions; render templates; evaluate JavaScript; and pause between operations.

```yaml
uix_broker:
  - realm: browser
    listen: click
    anchor: target
    rules:
      - ".action-button"
    directives:
      - type: block
      - type: event
        name: another-action
        data:
          source: action-button
```

## UIX Broker guides

- [Broker](./broker.md) — interaction structure, configuration sources, lifecycle, and debugging.
- [Realms](./realms.md) — browser events, keyboard shortcuts, and Home Assistant event-bus events.
- [Interaction Anchors](./interaction-anchors.md) — composed event-path and `select_tree` element selection.
- [Rules](./rules.md) — host-element, captured-data, browser-identity, user, administrator-status, URL-fragment, search-parameter, and panel matching.
- [Directives](./directives.md) — `block`, `property`, `event`, `call`, `button`, `badge`, `text-content`, `tile-icon`, `tooltip`, `lock`, `action-handler`, `action`, `template`, `javascript`, and `wait`.
- [Examples](./examples.md) — examples. Also see [UIX Guides](https://uix-guides.lf.technology), where further detailed examples may be published.

::: info
For browser-identity matching, [Browser Mod](https://github.com/thomasloven/hass-browser_mod) is required.
:::
