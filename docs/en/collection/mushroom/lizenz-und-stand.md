---
title: Mushroom license and source status
description: Sources, license information and change checking for the Mushroom documentation.
---
<a id="mushroom-lizenz-und-quellenstand"></a>
<a id="current-focus"></a>

# License and source status {#lizenz-und-quellenstand}

| field | Value |
| --- | --- |
| Original project | [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom) |
| Checked commit | [`6f8f1eaed3dc5cff94cd7ac5de64d921c6fb4101`](https://github.com/piitaya/lovelace-mushroom/commit/6f8f1eaed3dc5cff94cd7ac5de64d921c6fb4101) |
| Mushroom version | `5.2.2` according to `package.json` |
| License notice | `LICENSE` calls Apache-2.0, `package.json` calls ISC |
| Documentation status | Unofficial English working translation and practical documentation |

## Labeling {#kennzeichnung}

These pages are not official Mushroom documentation. They are an English-language reading aid and practical documentation.

The original project and original English files remain authoritative.

## Change checking {#anderungsprufung}

The GitHub Action `Check Mushroom docs upstream` regularly checks whether relevant files in the original repository have changed.

To be monitored:

- `README.md`
- `docs/cards/*.md`
- `docs/badges/*.md`
- `package.json`
- `LICENSE`

When relevant files change, the action creates an issue with a comparison link and file list.
