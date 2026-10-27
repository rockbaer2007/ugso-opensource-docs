---
title: Mushroom troubleshooting
description: Common Mushroom Card Problems and First Troubleshooting Steps.
---
<a id="mushroom-troubleshooting"></a>
<a id="current-focus"></a>

# Troubleshooting {#fehlersuche}

## New Changes Are Not Visible {#neue-anderungen-sind-nicht-sichtbar}

1. Check whether Home Assistant is up to date.
2. Check whether the latest Mushroom version is installed in HACS.
3. Check the browser console to see whether the expected mushroom version is actually being loaded.
4. Clear cache.
5. Remove mushroom resource.
6. Uninstall Mushroom from HACS.
7. Reinstall Mushroom.
8. Reload browser and Home Assistant app.

Direct link to Lovelace resources:

[Open Home Assistant Resources](https://my.home-assistant.io/redirect/lovelace_resources/)

## Card Mod Not Working {#card-mod-funktioniert-nicht}

The Mushroom repository does not provide general support for `card-mod` configurations.

The maintainer points to this status thread:

- [State of card mod support](https://github.com/piitaya/lovelace-mushroom/issues/1366)

## Card Cannot Be Found {#karte-wird-nicht-gefunden}

Typical causes:

- Resource missing or pointing to wrong path.
- Browser cache is still loading an old file.
- HACS installation did not load completely.
- YAML uses incorrect map type.

Example of a correct manual resource entry:

```yaml
resources:
  - url: /local/mushroom.js
    type: module
```
