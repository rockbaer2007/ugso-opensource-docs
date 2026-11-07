---
title: Translation status
description: Scope of canonical UIX documentation updates reviewed in German, English and French.
---
# Translation status


## Review on 7 November 2026: desktop tabs in preview 9.1.0-beta.0

Reviewed notifications: [1d53592](https://github.com/Lint-Free-Technology/uix/commit/1d53592b241ec8666b34d67056671bb37d1c2a1f) / [e7b5bdd](https://github.com/Lint-Free-Technology/uix/commit/e7b5bdd811a53960e9559c53a354c7855c537286). The complete archived `dev` source tree contains **65** canonical Markdown pages. Only [Custom sidebar panels](./extras/custom-sidebar-panels) changed in content since `f63ebbd`; 64 pages, navigation and media are unchanged. Content comparison accounts for different line endings.

**Open in new tab (desktop only)** applies to internal HA paths in desktop browsers. Companion navigates within the app; website URLs do not use this option. If the desktop browser blocks the new tab, the HA path opens in the current tab. This new behavior is explicitly documented **from 9.1.0-beta.0**. **9.0.0 / HA 2026.11.0 or later** remains the stable baseline; the preview is not presented as a stable release.

EN is synchronized with the changed source page; DE/FR and their overviews are updated. Unchanged English pages retain their still-valid older source notices. Source and translation manifests are updated. This is a documentation review, not a new HA runtime test.


## Review of 5 November 2026 against UIX 9.0.0

All **65** canonical source pages were compared with [`master f63ebbd`](https://github.com/Lint-Free-Technology/uix/commit/f63ebbdda5294fe0b9d31d89d4942496ebe55722). Since our recorded `e4a1caa` baseline, **eight pages changed** and 57 remained identical. `dev ef414d9` contains identical documentation, including navigation and media. Notifications `fa4a427`, `5c253f9`, `4768bff`, `f63ebbd` and `99293d1` are covered. No additional documentation differences were found on the current branches.

- **UIX 9.0.0** became stable on 4 November 2026 and requires **Home Assistant 2026.11.0 or later**. Current pages now identify the former preview features as stable.
- **Marketplace** installs UIX and adds its service. Manual setup has separate instructions. Marketplace removal also removes Foundries, custom sidebar panels and service settings.
- **Frame panels** now use `a0d7b954_tailscale` in the example. The former HACS styling example was removed from the current reference.
- **Contributions** distinguish `feat!:`/`BREAKING CHANGE: ...` for major releases from `feat(major):` for minor releases.
- **Forge, popover timeout and sidebar links** are stable 9.0.0 features. Landing pages, footers, metadata and the English source mirror are synchronized. The notified Forge animation was checked against the source.

The previous documentation and original sources were backed up. Verification covers source changes, translations, technical identifiers, code, media and links. This documentation review does not include a Home Assistant runtime test.

## Review of 2 November 2026: 9.0.0-beta.8 preview

Notifications `f769f06`, `2782a71`, `1f69b99` and `e4a1caa` were reviewed through [canonical revision e4a1caa](https://github.com/Lint-Free-Technology/uix/commit/e4a1caa6437f88282cfe04d768d3c11df387fc42). Comparing all **65** source pages identified three changed pages and one relocated page. English is synchronized; German and French cover the changes.

- [Popover timeout](./extras/uix-actions#popover-show-an-anchored-home-assistant-popover), from **beta.7**: milliseconds, `0`–`2147483647`, individual timer unaffected by interaction, no footer actions or form submission on expiry.
- [Custom sidebar panels](./extras/custom-sidebar-panels), external targets and new tabs from **beta.8**: accepted URL schemes, return to the previous HA page, and current-tab fallback when blocked.
- Page/navigation moved to **Extras**; old routes remain as compatibility links. Landing pages, footers and review records updated. Reviewed cache clarification preserved.
- **Stable remains 8.4.0 / HA 2026.10.0 minimum**. New preview additions require **HA 2026.11.0b0 or later**. Historical feature versions remain unchanged.

Previous sources backed up. Source, identifier, code-example, build and link checks; no HA runtime test.

## Review of 31 October 2026: 65 source pages, 9.0.0-beta.6 preview

The notified revisions [`964f440`](https://github.com/Lint-Free-Technology/uix/commit/964f4402b6f263a5deac53327b825a85cb3e3e72), [`e6fb84d`](https://github.com/Lint-Free-Technology/uix/commit/e6fb84dd715ea4bac9a330357705897ea8d44690) and [`25aec39`](https://github.com/Lint-Free-Technology/uix/commit/25aec397f873e566c2ead0201d819595854405ab) were compared with the previous reviewed source. All **65** source paths are covered. English was synchronized; German and French cover the actual content changes.

- Complete translated [custom sidebar panels](./using/custom-sidebar-panels) page, available **from 9.0.0-beta.6**, including setup, administrator option, internal targets, stable URLs, editing/deleting, personal order and history behavior. Added to indexes and navigation.
- Forge migration explicitly names **Convert to visual editor** and moves only `element.type` to `element_base.type`.
- Upstream also removed the forced automation YAML-mode examples. DE/FR retain them only in a clearly historical collapsed section for existing links.
- Landing pages, footers, review records and `llms.txt` now agree. **Stable remains 8.4.0**, released 7 October 2026, revision `71b8ccd`, requiring **Home Assistant 2026.10.0**. **9.0.0-beta.6 / e6fb84d** identifies the separately reviewed documentation preview. Historical introduction versions and cache clarifications are preserved.

Backed up before editing. Source comparison, page coverage, technical identifiers, build and local links/language metadata are checked; unchanged pages were not retranslated and no Home Assistant runtime test was performed.

## Content review of 27 October 2026

The remaining DE/EN/FR inventory findings have [individual assessments](/documentation-review.json). The canonical English preview is retained. Two contradictory cache paragraphs were corrected against the implementation: `clear-cache` preserves `localStorage` and the Browser Mod identity. The source/code record now explicitly documents these editorial corrections.

Eighteen French reference pages include 199 additional configurations from the German examples, with French headings and unchanged technical values. Missing theme, Foundry, DOM-path and browser-override explanations were added, and a remaining English theme paragraph was translated into French. Historical version annotations and different editorial structures are recorded as reviewed differences. Stable and preview documentation remain distinct. This review does not constitute a new Home Assistant runtime test.

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
