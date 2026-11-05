---
title: HA Cards
description: Documentation and examples for Home Assistant cards.
---
# HA Cards

**HA 2026.11 review, 2026-11-05:** Automation Status Card 0.1.3 and Dashboard Layout Card V2 0.1.181 pass the documented live checks. Other UGSo extensions have different verification levels and some open findings.

[Scope, results and remaining findings](/en/collection/ha-2026-11-compatibility).

This section is for Lovelace and HACS cards that are maintained with examples.

## Used And Reviewed HA Cards

| Project | Documentation status | Note |
| --- | --- | --- |
| <img class="package-icon" src="/images/automation-status-card/icon.svg" width="32" height="32" alt="" aria-hidden="true"> [Automation Status Card](/en/projects/automation-status-card/) | Complete | 0.1.3: automatic list, configurable rows/scrolling, optional controls, checkbox selection and run/trace diagnostics. DE/EN/FR; additional live test on HA 2026.11.0 passed on 2026-11-05, with scope linked above. |
| [Bubble Card](https://github.com/Clooos/Bubble-Card/blob/main/i18n/README.de.md) | German available upstream | External German README maintained in the Bubble Card project, linked here instead of duplicated. |
| [Calendar Card Pro](./calendar-card-pro/) | Complete | Documentation in DE/EN/FR with installation, features, reference, examples and upstream change checks. |
| [Mushroom Cards](./mushroom/) | Complete | Documentation in DE/EN/FR with installation, card overview, examples and upstream change checks. |
| [flex-table-card](./flex-table-card/) | Complete | Documentation in DE/EN/FR with installation, reference and practical examples. |
| bar-card | review later | Repository is available locally and can be evaluated next. |
| sidebar-card | review later | Repository is available locally and can be evaluated next. |

## Separate UIX reference

UIX is not listed as a regular HA Cards entry here. It remains a separate documentation area.

- [UIX English reference](/en/projects/uix/)

## Documentation checklist

A card guide should include HACS and manual installation, a quick start, a complete configuration reference, practical Home Assistant examples, version/source/license information and a clear unofficial-documentation notice for external projects.
