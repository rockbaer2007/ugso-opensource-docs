---
title: Calendar Card Pro Installation
description: Install Calendar Card Pro via HACS or manually.
---
<a id="calendar-card-pro-installation"></a>
<a id="current-focus"></a>

# Installation {#installation}

## HACS installation {#hacs-installation}

The recommended way is HACS.

1. Check whether HACS is installed.
2. Open **HACS** in Home Assistant.
3. Open the three-dot menu at the top right.
4. Open **Custom Repositories**.
5. Enter repository: `https://github.com/alexpfau/calendar-card-pro`
6. Set type to `Dashboard`.
7. Install Calendar Card Pro.
8. Reload Home Assistant. If the old card still appears, refresh the resource cache; deleting saved website data is not necessary.

This menu sequence follows the [HACS custom repository instructions](https://hacs.dev/docs/faq/custom_repositories/).

Direct link:

[Open Calendar Card Pro in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=alexpfau&repository=calendar-card-pro&category=plugin)

## Manual installation {#manuelle-installation}

When installing manually, both release files must be loaded:

- `calendar-card-pro.js`
- `editor.js`

Both files belong in the same subfolder, for example:

```text
/config/www/calendar-card-pro/
```

Afterwards only `calendar-card-pro.js` is entered as a resource. The card loads the editor itself when it is needed.

```yaml
url: /local/calendar-card-pro/calendar-card-pro.js
type: module
```

::: tip Why a separate folder?
`editor.js` is a common file name. A separate subfolder prevents naming conflicts with other manually installed cards.
:::

## Requirements {#voraussetzungen}

Calendar Card Pro requires at least one calendar entity in Home Assistant, for example:

```text
calendar.family
calendar.work
calendar.personal
```

Without calendar integration, there are no appointments for the card to display.
