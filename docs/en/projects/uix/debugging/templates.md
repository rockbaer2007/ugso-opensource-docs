> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `master` / **9.0.0**, revision [f63ebbd](https://github.com/Lint-Free-Technology/uix/commit/f63ebbdda5294fe0b9d31d89d4942496ebe55722), reviewed 5 November 2026. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.

# Debugging Templates

  You can debug UIX Jinja2 templates by placing the comment `{# uix.debug #}` anywhere in your template. You will see debug messages on template binding, value updated, reuse, unbinding and final unsubscribing. Any template is kept subscribed in cache for a 20s cooldown period to assist with template application, which can bring a slight speed improvement when switching back and forth to views, or using the same template on cards on different views.
