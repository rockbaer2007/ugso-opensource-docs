---
title: Translation status
description: Scope of canonical UIX documentation updates reviewed in German, English and French.
---
# Translation status

## Translation content review — 26 October 2026

All **64 canonical pages** were checked again against [English source `26e54e6`](https://github.com/Lint-Free-Technology/uix/tree/26e54e6d4973231a393933e6479ed1b03cc86cd3/docs/source). The `dev` source has not changed since the previous review; the original website still identifies **9.0.0-beta.2**. The stable baseline remains **8.4.0**.

- Corrected German section-background variables/configuration, the `custom:mod-card` fallback warning, template-debug marker and 20-second cache cooldown.
- Added full Badge and Broker Badge/Lock/Action Handler examples in DE/FR. Corrected the French Tooltip arrow-size theme fallback and added its theme-debugging context.
- Expanded German Foundry anchors/includes/secrets/merge and empty-billet examples, throttling, section/footer constraints, Background adapters, Map filtering, Event merging and embedded More-info. Corrected Lock/Overlay position defaults and Overlay border radius.
- The [page review record](/projects/uix/translation-review.json) preserves source and translation hashes. Page counterparts, table keys and the added examples were checked; build/link/media/language checks run separately. Copied technical examples and configuration identifiers retain their original spelling.

DE/FR remain editorial translations with some condensed sections. This is not independent translation certification or a Home Assistant runtime test. EN language navigation continues to open the original documentation in a separate tab.

## Full review — 22 October 2026

All **64 canonical Markdown pages** were compared against frozen [English revision `26e54e6`](https://github.com/Lint-Free-Technology/uix/tree/26e54e6d4973231a393933e6479ed1b03cc86cd3/docs/source). Since the previous `e2e0701` preview review, only the Forge reference, Foundries and Forge overview changed; the other 61 source pages are unchanged. The stable release remains **8.4.0**; the reviewed preview is **9.0.0-beta.2**.

- **EN:** all 64 pages now contain the full original English content instead of placeholders. Admonitions, anchors, links and media are adapted for this site with CC BY 4.0 attribution. The [review manifest](/projects/uix/canonical-review.json) records source/output hashes; code blocks are compared with normalized outer indentation, trailing whitespace and line endings.
- **DE/FR:** added Broker Badge, Text content, Lock and Action handler; extended Forge type anchors, Foundry native bases and blank badges. French Tooltip gains missing options, scrolling and current CSS defaults.
- **DE:** corrected Foundry examples (`uix_foundries`, top-level `foundry`, `forge.billets`, Native type matching, Spark merging and macro `returns`) and Card-mod compatibility/migration FAQ through 4.2.1. Added browser event actions, cache retention, integration dependencies, state throttling, billet precedence and missing Spark CSS options.
- Every canonical page has DE/EN/FR counterparts. The legacy English `style-custom-panels` route links to `style-frame-panels`. Missing original media are included; language links, references and local images are checked.

This is a source/content/documentation review. DE/FR remain editorial translations rather than line-identical copies or independently certified translations. No HA system was accessed or changed. Stable metadata remains 8.4.0; preview version/revision are separate. The earlier targeted Forge review is preserved below as history.

## Forge review — 22 October 2026

Canonical `dev` [change `1badf70befb9`](https://github.com/Lint-Free-Technology/uix/commit/1badf70befb9c9d3d7b06c0eced75af7d552aff1) adds the Forge visual editor availability note for **9.0.0-beta.2**. Our pages lacked the corresponding editor section. A source-reviewed summary now covers Native, Forge, Element, Foundry and Export in **DE/EN/FR**, including `element_base`/`element`, type anchors, null/disable semantics and YAML-only limits.

The English Forge page is no longer a placeholder for this section. The full canonical reference remains linked. This is not a complete retranslation of all UIX pages or all `dev` changes. Stable baseline, release metadata and footer remain unchanged; the previous broader preview review through 9.0.0-beta.0 is separate from this targeted Forge review. Documentation-only update, without HA installation or runtime testing.

Earlier review history remains on the [German status page](/projects/uix/translation-status) and [French status page](/fr/projects/uix/translation-status).
