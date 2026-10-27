---
title: flex-table-card installation
description: Installation of the flex-table-card via HACS or manually.
---
<a id="flex-table-card-installation"></a>
<a id="current-focus"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

The recommended installation runs via HACS.

1. Open Home Assistant.
2. Open HACS.
3. Search for `flex-table`.
4. Install the card.
5. Reload Home Assistant if HACS prompts.

The card type is then available in Lovelace as a custom card:

```yaml
type: custom:flex-table-card
```

## Manual installation {#manuelle-installation}

Manual installation is intended more for developers or special cases.

1. Load file `flex-table-card.js` from the original repository.
2. Place the file in the Home Assistant folder `www`.
3. Enter resource in Lovelace.

```yaml
resources:
  - type: module
    url: /local/flex-table-card.js
```

With HACS, the resource is usually maintained automatically or via the HACS note.

## Quick test {#schnelltest}

```yaml
type: custom:flex-table-card
title: Sensoren
entities:
  include: sensor.*
max_rows: 10
columns:
  - name: Name
    data: name
  - name: Status
    data: state
```
