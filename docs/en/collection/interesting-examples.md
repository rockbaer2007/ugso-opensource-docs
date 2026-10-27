---
title: Interesting Examples
description: Community examples and external references for Home Assistant, UIX and Lovelace.
---
# Interesting Examples

This page collects external community examples, gists and useful ideas that are not part of a specific project translation.

Keeping these examples in the collection avoids mixing unofficial additions into documentation that should stay close to the original project.

## UIX Theme Collection by Mariusthvdb

Mariusthvdb maintains a broad UIX theme example as a GitHub Gist:

- [UIX themes by Mariusthvdb](https://gist.github.com/Mariusthvdb/ecdd6ac6776d501b09e859888b01a9c6)

The gist includes global UIX theme variables, reusable `uix-macros-yaml`, entity icon and color rules, sidebar and header styling, badges, view styling, animations and state colors.

::: warning Community example
This example is not part of the official UIX documentation and is tailored to the author's Home Assistant installation. Use it as inspiration and review entities, labels, colors, macros and UIX version before applying it.
:::

:::: details Detailed reference from the German documentation

## More interesting examples {#weitere-interessante-beispiele}

Here we collect external practical examples, community gists and interesting ideas that are not directly part of a project or translation documentation.

This page is deliberately separated from the individual project documentation. This means that translations remain close to the original, while helpful additional ideas can still be found.

### UIX theme collection by Mariusthvdb {#uix-theme-sammlung-von-mariusthvdb}

A comprehensive practical example for UIX themes is maintained as Gist by Mariusthvdb:

- [UIX themes by Mariusthvdb](https://gist.github.com/Mariusthvdb/ecdd6ac6776d501b09e859888b01a9c6)

The Gist shows, among other things:

- global UIX theme variables
- `uix-macros-yaml` with reusable macros
- Icon and color rules for entities
- Sidebar, header, badge and view styling
- Animations and state colors

::: warning Community example
This example is not part of the official UIX documentation and is highly tailored to the author's own Home Assistant installation. Use it as a collection of ideas and adapt entities, labels, colors, macros and UIX version to your installation.
:::

Small excerpts can serve as a guide. The complete YAML should be taken directly from the Gist and checked before use.

```yaml
theme-mods:
  uix-top-app-bar-fixed: |
    header.top-app-bar {
      background: var(--header-background);
      color: var(--text-color-off);
    }

  uix-macros-yaml: |
    power_color:
      template: >
        {% for entity in label_entities('power') %}
        --uix-icon-color-for-{{ entity.replace('.','_') }}:
        {{ 'var(--success-color)' if states(entity)|int(0) < 2500 else 'var(--alert-color)' }};
        {% endfor %}
```

::::
