---
description: Learn about other styling techniques including using mod-card for troublesome custom cards.
---

> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `master` / **9.0.0**, revision [f63ebbd](https://github.com/Lint-Free-Technology/uix/commit/f63ebbdda5294fe0b9d31d89d4942496ebe55722), reviewed 5 November 2026. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Other styling

Cards that don't have a `<ha-element>` can still be styled by using the supplied `custom:mod-card` card. This is only necessary in **very very few** instances, and likely to bring more problems than it solves. Most likely your card contains another card, in which case **that** is the one you should apply the styles to.

::: details Use custom:mod-card with caution
```yaml
type: custom:mod-card
card:
  type: custom:beloved-custom-card
  ...
uix:
  style: |
    ha-card {
      ...
    }
```
The mod-card will create a `<ha-card>` element and put your card inside that. The card will be styled transparent with no border or background.
:::
