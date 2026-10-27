---
title: Mushroom installation
description: Install Mushroom via HACS or manually in Home Assistant.
---
<a id="mushroom-installation"></a>
<a id="current-focus"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

Mushroom is available through HACS.

1. Install HACS if it is not already present.
2. Open HACS in Home Assistant.
3. Search for `Mushroom`.
4. Download repository.
5. Reload the browser if Home Assistant does not yet display the new card.

Direct link for Home Assistant:

[Open Mushroom in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=piitaya&repository=lovelace-mushroom)

## Manual installation {#manuelle-installation}

1. Download `mushroom.js` from the latest release.
2. Place the file in the Home Assistant folder `config/www`.
3. Enter resource in the dashboard.

Resource via the interface:

1. Open **Settings**.
2. Open **Dashboards**.
3. Open the menu with further options.
4. Select **Resources**.
5. Add resource.
6. Set URL to `/local/mushroom.js`.
7. Set resource type to `JavaScript Module`.

::: tip hint
If the **Resources** menu item is not visible, advanced mode must be activated in the user profile.
:::

Resource via YAML:

```yaml
lovelace:
  resources:
    - url: /local/mushroom.js
      type: module
```

## After Installation {#nach-der-installation}

After installation, you will find the cards under Custom Cards when editing a dashboard. The card names typically start with `Custom: Mushroom`.
