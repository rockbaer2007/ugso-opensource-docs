---
description: Your FAQ for UI eXtension answered here.
hide:
  - toc
  - navigation
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision [26e54e6](https://github.com/Lint-Free-Technology/uix/commit/26e54e6d4973231a393933e6479ed1b03cc86cd3), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# FAQ

## How do I best migrate from Card-mod?

- Uninstall card-mod.
- If you use extra_module_url for card-mod resource, remove and restart Home Assistant.
- Proceed to follow the [UI eXtension quick start guide](./quick-start.md).

::: tip Add UI eXtension as a Service
UI eXtension is an integration and needs to be added as a Service once you have downloaded by HACS. Make sure you don't miss the **Add UI eXtension service** step. This is something you may miss if you are not accustomed to adding integrations like UIX as a Service.

:::

::: details UI Lovelace Minimalist may load card-mod resource
If you have UI Lovelace Minimalist installed it may load card-mod resource. Due to load order of integrations, UI eXtension cannot check for this conflict. To continue to use UI Lovelace Minimalist with UI eXtension you need to turn off UI Lovelace Minimalist config option `Include custom card resources it's depending on` and load any required custom cards through HACS or manually.

![UI Minimalist custom card option](/projects/uix/assets/page-assets/faq/ui-minimalist-option.png)

:::

## Is UI eXtension a drop in replacement for Card-mod?

Yes, UI eXtension is a drop in replacement for Card-mod versions up to 4.2.1. All Card-mod card and themes configurations are supported. While you are encouraged to update to use `uix:` in your cards and `uix-<thing>(-yaml)` for your themes, it is not required.

## Is UI eXtension just Card-mod with different documentation?

No, UI eXtension code has been updated so that UIX is primary domain and config key. Card-mod keys are supported but overridden by `uix:`.

::: details UI eXtension differences from Card-mod
- Config key for cards is `uix:`.
- Theme key is `uix-theme:`.
- Theme `thing` keys are `uix-<thing>(-yaml):`.
- HTML node for UI eXtension is `<uix-node>` and properties of the node all refer to `uix`.
- You can use `{# uix.debug #}` to debug templates.
- All debug console messages will start with `UIX`.

:::

## Is there a list of differences between Card-mod and UI eXtension?

Yes, see the table below.

<!-- markdownlint-disable MD033 -->
| Feature | Card-mod | UIX |
| --- | :---: | :---: |
| Correctly loads `...-yaml` theme variables | ❌<br>Since 2026.8.0 | Yes |
| Correctly handles `...-more-info(-yaml)` theme variable | ❌<br>Since 2026.3.0 | Yes |
| Correctly patches adaptive dialogs for `...-dialog(-yaml)` theme variable | ❌<br>Since 2026.3.0 | Yes |
| [DOM inspection helpers](/en/projects/uix/concepts/dom#dom-inspection-helpers) | No | Yes |
| [Host/element path selection](/en/projects/uix/concepts/dom#hostelement-path-selection) | No | Yes |
| [Express search selector](/en/projects/uix/concepts/dom#express-search-selector) | No | Yes |
| [Forge](/en/projects/uix/forge/) (custom lovelace element) | No | Yes |
| [Forge - Foundries](/en/projects/uix/forge/foundries) (reusable forges) | No | Yes |
| [Forge - Macros](/en/projects/uix/using/templates#macros) (reusable jinja templates) | No | Yes |
| [Forge - Sparks](/en/projects/uix/forge/sparks/) (self-contained behaviours that augment forged elements) | No | Yes |
| [Broker](/en/projects/uix/broker/) (create declarative frontend event interactions) | No | Yes |
| [Frontend state throttling](/en/projects/uix/extras/frontend-states-throttling) (optional) | No | Yes |
| [Dialog Styling delay](/en/projects/uix/extras/dialog-styling-delay) (optional) | No | Yes |
| [Dashboard view backgrounds](/en/projects/uix/using/view-backgrounds) | No | Yes |
| [Section backgrounds](/en/projects/uix/using/section-backgrounds) | No | Yes |
| [View backgrounds](/en/projects/uix/using/view-backgrounds) | No | Yes |
| [Icon styling - entity override](/en/projects/uix/using/icons#specifying-for-an-entity-override) | No | Yes |
| [Styling entity images](/en/projects/uix/using/images) | No | Yes |
| [Styling custom panels](/en/projects/uix/using/custom-panels) (including those loaded as iFrames) | No | Yes |
| [Styling app and ingress panels](/en/projects/uix/using/apps) (including those loaded as iFrames) | No | Yes |
| Reload/Clear cache popup | No | Yes |
| Expansive documentation including visual examples | Limited | Yes |
| Mod-Card | Yes | Yes |
| CSS styling in themes | Yes | Yes |
| Reload/Clear cache service/action | Yes | Yes |
| Provides variables (e.g current user) | Yes | Yes |
| CSS styling | Yes | Yes |
| Resource url | Yes | N/A |

## Does UI eXtension have resource URL issues?

No, being an integration, UI eXtension manages its resource URLs directly. You don't need to do anything to have UI eXtension run at peak performance. UI eXtension dynamically adds its Frontend resource, `uix.js`, as an extra module, as well as adding a Dashboard resource in case you use CAST. UI eXtension will add its version to these resources automatically each time the integration loads.

## Does UI eXtension need manual cache clear after upgrade for Browsers and device Companion Apps?

UI eXtension will show a toast message when it detects that a reload is needed to clear caches, with a convenient `Reload Now` button and auto reload after 60s.

::: info
While the Auto reload code is in 8.1.0, auto Reload will be available when you next update. When you install 8.1.0, device will still be running 8.0.1 code which does not have the auto reload feature.

:::

## Can the reload toast message be suppressed?

No, the toast messages exist to satisfy the requirement of Frontend UIX JavaScript code matching the UIX integration code.

The toast is shown when UIX has been changed and Home Assistant has restarted, but the browser is still running a cached UIX bundle from a different version.

An auto reload happens after 60 seconds, allowing unattended kiosks to update their Frontend code.

::: tip
After updating UIX, restart Home Assistant when you are ready to activate the update. Until then, UIX continues serving the version that was loaded when Home Assistant started.

:::

## How do I uninstall UI eXtension?

Uninstallation of UI eXtension is a two step process. First, remove the service entry in Devices & services. Next uninstall the integration either using HACS or manually removing the `uix` folder from `custom_components` directory if you installed manually.
