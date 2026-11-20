---
title: Documentation language status
sidebar: false
aside: false
---

# Documentation language status

DE / EN / FR · 2026-11-20

All German reference pages now have English and French content. The 128 placeholder pages have been replaced and the 20 missing French pages added.

Every Markdown content page was inventoried, excluding these three generated reports: locale coverage, placeholder text, version mentions, headings, code examples and resolvable local page/image references. Different version lists or text lengths are review signals, not automatic evidence of outdated content. “Content present” does not certify a complete or linguistically reviewed translation. The inventory does not automatically audit upstream releases; separately documented source comparisons, such as UIX, remain authoritative for that scope.

## Inventory

| Language | Existing pages | Missing pages | Placeholders | Open review findings |
| --- | ---: | ---: | ---: | ---: |
| DE | 252 | 0 | 0 | 0 |
| EN | 252 | 0 | 0 | 0 |
| FR | 252 | 0 | 0 | 0 |

**Technical comparison of 2026-11-20:** Existing assessments are bound to current file hashes; changes require another review. Actual gaps and contradictions are corrected, while intentional differences in version history and editorial structure have recorded explanations. The table shows outstanding findings; raw automatic signals remain in the JSON report. “0 open” means reviewed and classified, not word-for-word identity. [Recorded assessments](/documentation-review.json).


The additions were created with translation assistance and checked technically against the German source: code, identifiers, tables and images. Fourteen further content gaps were filled with supplementary references while preserving existing pages and links. This is not a complete linguistic certification. Remaining review signals also include intentionally different summaries and historical version mentions.

The complete JSON report records paths, SHA-256 hashes, version differences, structural metrics and unresolved local references for every page.

[JSON](/documentation-audit.json)

[UIX DE](/projects/uix/translation-status) · [UIX EN](/en/projects/uix/translation-status) · [UIX FR](/fr/projects/uix/translation-status)

**Extended comparison of 2026-11-20: 187 EN and 221 FR pages.** Every file previously labelled only “Content present” was technically compared in full against its reference: versions, code blocks, technical identifiers and links. Differences were individually classified; automatic language screening was followed by corrections to the English prose found in French pages. **“Technically compared” is not a full linguistic or sentence-by-sentence content approval.** “Difference reviewed” retains the earlier structural assessment. “Recheck required” appears when either file changes. [Scope and individual assessments](/documentation-content-review.json).

Corrections include English prose left in French UIX concepts, macros, themes and camera backgrounds, a JavaScript syntax error in the developer example, seven anchor links and two video links. The Lock Spark active:false fallback is clarified in DE/FR. Examples, media and existing anchors are preserved.

## Content review

**Content reviewed** means sections and statements were compared with the reference for meaning, completeness, prerequisites, limitations and the purpose of examples. Identified mistranslations or contradictions were corrected. This is not a new application live test or legal certification. Pages not yet reviewed this way retain their technical status. [Individual assessments](/documentation-semantic-review.json).

| Language | Reviewed | Pending |
| --- | ---: | ---: |
| EN | 182 | 70 |
| FR | 182 | 70 |

## Complete page inventory

| German reference | EN | FR |
| --- | --- | --- |
| [blog/beitragsvorlage.md](/blog/beitragsvorlage) | [Content reviewed](/en/blog/post-template) | [Content reviewed](/fr/blog/post-template) |
| [blog/index.md](/blog/) | [Content reviewed](/en/blog/) | [Content reviewed](/fr/blog/) |
| [blog/posts/atlas-runtime-foundation.md](/blog/posts/atlas-runtime-foundation) | [Content reviewed](/en/blog/posts/atlas-runtime-foundation) | [Content reviewed](/fr/blog/posts/atlas-runtime-foundation) |
| [blog/posts/hadash-preview.md](/blog/posts/hadash-preview) | [Content reviewed](/en/blog/posts/hadash-preview) | [Content reviewed](/fr/blog/posts/hadash-preview) |
| [blog/snippets/blockly.md](/blog/snippets/blockly) | [Content reviewed](/en/blog/snippets/blockly) | [Content reviewed](/fr/blog/snippets/blockly) |
| [blog/snippets/home-assistant-yaml.md](/blog/snippets/home-assistant-yaml) | [Content reviewed](/en/blog/snippets/home-assistant-yaml) | [Content reviewed](/fr/blog/snippets/home-assistant-yaml) |
| [blog/snippets/index.md](/blog/snippets/) | [Content reviewed](/en/blog/snippets/) | [Content reviewed](/fr/blog/snippets/) |
| [blog/snippets/iobroker-blockly.md](/blog/snippets/iobroker-blockly) | [Content reviewed](/en/blog/snippets/iobroker-blockly) | [Content reviewed](/fr/blog/snippets/iobroker-blockly) |
| [blog/snippets/javascript.md](/blog/snippets/javascript) | [Content reviewed](/en/blog/snippets/javascript) | [Content reviewed](/fr/blog/snippets/javascript) |
| [blog/snippets/lovelace.md](/blog/snippets/lovelace) | [Content reviewed](/en/blog/snippets/lovelace) | [Content reviewed](/fr/blog/snippets/lovelace) |
| [eep/index.md](/eep/) | [Content reviewed](/en/eep/) | [Content reviewed](/fr/eep/) |
| [eep/ini-edit-translate-2026/index.md](/eep/ini-edit-translate-2026/) | [Technically compared](/en/eep/ini-edit-translate-2026/) | [Technically compared](/fr/eep/ini-edit-translate-2026/) |
| [eep/projektduplicator-2026/index.md](/eep/projektduplicator-2026/) | [Content reviewed](/en/eep/projektduplicator-2026/) | [Content reviewed](/fr/eep/projektduplicator-2026/) |
| [impressum/index.md](/impressum/) | [Content reviewed](/en/impressum/) | [Content reviewed](/fr/impressum/) |
| [index.md](/) | [Content reviewed](/en/) | [Content reviewed](/fr/) |
| [iobroker/publish-assistant/index.md](/iobroker/publish-assistant/) | [Content reviewed](/en/iobroker/publish-assistant/) | [Content reviewed](/fr/iobroker/publish-assistant/) |
| [iobroker/widgets/ugso-spezial/index.md](/iobroker/widgets/ugso-spezial/) | [Content reviewed](/en/iobroker/widgets/ugso-spezial/) | [Content reviewed](/fr/iobroker/widgets/ugso-spezial/) |
| [projects-diverse/index.md](/projects-diverse/) | [Content reviewed](/en/projects-diverse/) | [Content reviewed](/fr/projects-diverse/) |
| [projects-mqtt/index.md](/projects-mqtt/) | [Content reviewed](/en/projects-mqtt/) | [Content reviewed](/fr/projects-mqtt/) |
| [projects/atlas-plugins/automation-extractor.md](/projects/atlas-plugins/automation-extractor) | [Content reviewed](/en/projects/atlas-plugins/automation-extractor) | [Content reviewed](/fr/projects/atlas-plugins/automation-extractor) |
| [projects/atlas-plugins/demo-repository.md](/projects/atlas-plugins/demo-repository) | [Content reviewed](/en/projects/atlas-plugins/demo-repository) | [Content reviewed](/fr/projects/atlas-plugins/demo-repository) |
| [projects/atlas-plugins/developers/compatibility.md](/projects/atlas-plugins/developers/compatibility) | [Content reviewed](/en/projects/atlas-plugins/developers/compatibility) | [Content reviewed](/fr/projects/atlas-plugins/developers/compatibility) |
| [projects/atlas-plugins/developers/index.md](/projects/atlas-plugins/developers/) | [Content reviewed](/en/projects/atlas-plugins/developers/) | [Content reviewed](/fr/projects/atlas-plugins/developers/) |
| [projects/atlas-plugins/developers/manifest.md](/projects/atlas-plugins/developers/manifest) | [Content reviewed](/en/projects/atlas-plugins/developers/manifest) | [Content reviewed](/fr/projects/atlas-plugins/developers/manifest) |
| [projects/atlas-plugins/developers/publishing.md](/projects/atlas-plugins/developers/publishing) | [Content reviewed](/en/projects/atlas-plugins/developers/publishing) | [Content reviewed](/fr/projects/atlas-plugins/developers/publishing) |
| [projects/atlas-plugins/developers/runtime.md](/projects/atlas-plugins/developers/runtime) | [Content reviewed](/en/projects/atlas-plugins/developers/runtime) | [Content reviewed](/fr/projects/atlas-plugins/developers/runtime) |
| [projects/atlas-plugins/file-studio.md](/projects/atlas-plugins/file-studio) | [Technically compared](/en/projects/atlas-plugins/file-studio) | [Technically compared](/fr/projects/atlas-plugins/file-studio) |
| [projects/atlas-plugins/gepruefte-plugins.md](/projects/atlas-plugins/gepruefte-plugins) | [Content reviewed](/en/projects/atlas-plugins/verified-plugins) | [Content reviewed](/fr/projects/atlas-plugins/verified-plugins) |
| [projects/atlas-plugins/homeassistant-card-editor.md](/projects/atlas-plugins/homeassistant-card-editor) | [Content reviewed](/en/projects/atlas-plugins/homeassistant-card-editor) | [Content reviewed](/fr/projects/atlas-plugins/homeassistant-card-editor) |
| [projects/atlas-plugins/icon-library.md](/projects/atlas-plugins/icon-library) | [Content reviewed](/en/projects/atlas-plugins/icon-library) | [Content reviewed](/fr/projects/atlas-plugins/icon-library) |
| [projects/atlas-plugins/icon-studio.md](/projects/atlas-plugins/icon-studio) | [Content reviewed](/en/projects/atlas-plugins/icon-studio) | [Content reviewed](/fr/projects/atlas-plugins/icon-studio) |
| [projects/atlas-plugins/index.md](/projects/atlas-plugins/) | [Technically compared](/en/projects/atlas-plugins/) | [Technically compared](/fr/projects/atlas-plugins/) |
| [projects/atlas-plugins/plugin-template.md](/projects/atlas-plugins/plugin-template) | [Content reviewed](/en/projects/atlas-plugins/plugin-template) | [Content reviewed](/fr/projects/atlas-plugins/plugin-template) |
| [projects/atlas-plugins/repository-format.md](/projects/atlas-plugins/repository-format) | [Content reviewed](/en/projects/atlas-plugins/repository-format) | [Content reviewed](/fr/projects/atlas-plugins/repository-format) |
| [projects/atlas-plugins/terminal.md](/projects/atlas-plugins/terminal) | [Content reviewed](/en/projects/atlas-plugins/terminal) | [Content reviewed](/fr/projects/atlas-plugins/terminal) |
| [projects/atlas/card-editor.md](/projects/atlas/card-editor) | [Technically compared](/en/projects/atlas/card-editor) | [Content present · Difference reviewed](/fr/projects/atlas/card-editor) |
| [projects/atlas/entwicklungsstand.md](/projects/atlas/entwicklungsstand) | [Technically compared](/en/projects/atlas/development-status) | [Content present · Difference reviewed](/fr/projects/atlas/development-status) |
| [projects/atlas/frontend.md](/projects/atlas/frontend) | [Technically compared](/en/projects/atlas/frontend) | [Technically compared](/fr/projects/atlas/frontend) |
| [projects/atlas/homeassistant.md](/projects/atlas/homeassistant) | [Technically compared](/en/projects/atlas/homeassistant) | [Technically compared](/fr/projects/atlas/homeassistant) |
| [projects/atlas/index.md](/projects/atlas/) | [Content reviewed](/en/projects/atlas/) | [Content reviewed](/fr/projects/atlas/) |
| [projects/atlas/linux.md](/projects/atlas/linux) | [Technically compared](/en/projects/atlas/linux) | [Technically compared](/fr/projects/atlas/linux) |
| [projects/atlas/plugins.md](/projects/atlas/plugins) | [Content reviewed](/en/projects/atlas/plugins) | [Content reviewed](/fr/projects/atlas/plugins) |
| [projects/atlas/tablet-test.md](/projects/atlas/tablet-test) | [Content reviewed](/en/projects/atlas/tablet-test) | [Content reviewed](/fr/projects/atlas/tablet-test) |
| [projects/atlas/tablet-uix-dauertest.md](/projects/atlas/tablet-uix-dauertest) | [Content reviewed](/en/projects/atlas/tablet-uix-dauertest) | [Content reviewed](/fr/projects/atlas/tablet-uix-dauertest) |
| [projects/atlas/uebersicht.md](/projects/atlas/uebersicht) | [Content reviewed](/en/projects/atlas/overview) | [Content reviewed](/fr/projects/atlas/overview) |
| [projects/automation-status-card/index.md](/projects/automation-status-card/) | [Technically compared](/en/projects/automation-status-card/) | [Technically compared](/fr/projects/automation-status-card/) |
| [projects/blocks-for-ha/advanced.md](/projects/blocks-for-ha/advanced) | [Technically compared](/en/projects/blocks-for-ha/advanced) | [Technically compared](/fr/projects/blocks-for-ha/advanced) |
| [projects/blocks-for-ha/blockly-audit.md](/projects/blocks-for-ha/blockly-audit) | [Technically compared](/en/projects/blocks-for-ha/blockly-audit) | [Technically compared](/fr/projects/blocks-for-ha/blockly-audit) |
| [projects/blocks-for-ha/blocks.md](/projects/blocks-for-ha/blocks) | [Technically compared](/en/projects/blocks-for-ha/blocks) | [Technically compared](/fr/projects/blocks-for-ha/blocks) |
| [projects/blocks-for-ha/catalog/index.md](/projects/blocks-for-ha/catalog/) | [Content reviewed](/en/projects/blocks-for-ha/catalog/) | [Content reviewed](/fr/projects/blocks-for-ha/catalog/) |
| [projects/blocks-for-ha/catalog/sensor-light.md](/projects/blocks-for-ha/catalog/sensor-light) | [Content reviewed](/en/projects/blocks-for-ha/catalog/sensor-light) | [Content reviewed](/fr/projects/blocks-for-ha/catalog/sensor-light) |
| [projects/blocks-for-ha/collections.md](/projects/blocks-for-ha/collections) | [Technically compared](/en/projects/blocks-for-ha/collections) | [Technically compared](/fr/projects/blocks-for-ha/collections) |
| [projects/blocks-for-ha/conversion.md](/projects/blocks-for-ha/conversion) | [Content reviewed](/en/projects/blocks-for-ha/conversion) | [Content reviewed](/fr/projects/blocks-for-ha/conversion) |
| [projects/blocks-for-ha/custom-blocks.md](/projects/blocks-for-ha/custom-blocks) | [Content reviewed](/en/projects/blocks-for-ha/custom-blocks) | [Content reviewed](/fr/projects/blocks-for-ha/custom-blocks) |
| [projects/blocks-for-ha/entities.md](/projects/blocks-for-ha/entities) | [Technically compared](/en/projects/blocks-for-ha/entities) | [Technically compared](/fr/projects/blocks-for-ha/entities) |
| [projects/blocks-for-ha/flow.md](/projects/blocks-for-ha/flow) | [Technically compared](/en/projects/blocks-for-ha/flow) | [Technically compared](/fr/projects/blocks-for-ha/flow) |
| [projects/blocks-for-ha/index.md](/projects/blocks-for-ha/) | [Technically compared](/en/projects/blocks-for-ha/) | [Content present · Difference reviewed](/fr/projects/blocks-for-ha/) |
| [projects/blocks-for-ha/system-template.md](/projects/blocks-for-ha/system-template) | [Technically compared](/en/projects/blocks-for-ha/system-template) | [Technically compared](/fr/projects/blocks-for-ha/system-template) |
| [projects/blocks-for-ha/themes.md](/projects/blocks-for-ha/themes) | [Technically compared](/en/projects/blocks-for-ha/themes) | [Technically compared](/fr/projects/blocks-for-ha/themes) |
| [projects/blocks-for-ha/time.md](/projects/blocks-for-ha/time) | [Technically compared](/en/projects/blocks-for-ha/time) | [Technically compared](/fr/projects/blocks-for-ha/time) |
| [projects/callmebot-signal/index.md](/projects/callmebot-signal/) | [Content reviewed](/en/projects/callmebot-signal/) | [Content reviewed](/fr/projects/callmebot-signal/) |
| [projects/callmebot/index.md](/projects/callmebot/) | [Technically compared](/en/projects/callmebot/) | [Technically compared](/fr/projects/callmebot/) |
| [projects/dashboard-user-manager/index.md](/projects/dashboard-user-manager/) | [Technically compared](/en/projects/dashboard-user-manager/) | [Technically compared](/fr/projects/dashboard-user-manager/) |
| [projects/fritzbox-to-mqtt/beispiele.md](/projects/fritzbox-to-mqtt/beispiele) | [Content reviewed](/en/projects/fritzbox-to-mqtt/examples) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/examples) |
| [projects/fritzbox-to-mqtt/entitaeten.md](/projects/fritzbox-to-mqtt/entitaeten) | [Content reviewed](/en/projects/fritzbox-to-mqtt/entities) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/entities) |
| [projects/fritzbox-to-mqtt/fehlersuche.md](/projects/fritzbox-to-mqtt/fehlersuche) | [Content reviewed](/en/projects/fritzbox-to-mqtt/troubleshooting) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/troubleshooting) |
| [projects/fritzbox-to-mqtt/index.md](/projects/fritzbox-to-mqtt/) | [Content reviewed](/en/projects/fritzbox-to-mqtt/) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/) |
| [projects/fritzbox-to-mqtt/installation.md](/projects/fritzbox-to-mqtt/installation) | [Content reviewed](/en/projects/fritzbox-to-mqtt/installation) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/installation) |
| [projects/fritzbox-to-mqtt/konfiguration.md](/projects/fritzbox-to-mqtt/konfiguration) | [Content reviewed](/en/projects/fritzbox-to-mqtt/configuration) | [Content reviewed](/fr/projects/fritzbox-to-mqtt/configuration) |
| [projects/grafik-visual-studio/basic.md](/projects/grafik-visual-studio/basic) | [Content reviewed](/en/projects/grafik-visual-studio/basic) | [Content reviewed](/fr/projects/grafik-visual-studio/basic) |
| [projects/grafik-visual-studio/bildergalerie.md](/projects/grafik-visual-studio/bildergalerie) | [Content reviewed](/en/projects/grafik-visual-studio/bildergalerie) | [Content reviewed](/fr/projects/grafik-visual-studio/bildergalerie) |
| [projects/grafik-visual-studio/calendar-plus.md](/projects/grafik-visual-studio/calendar-plus) | [Technically compared](/en/projects/grafik-visual-studio/calendar-plus) | [Technically compared](/fr/projects/grafik-visual-studio/calendar-plus) |
| [projects/grafik-visual-studio/datenfluss.md](/projects/grafik-visual-studio/datenfluss) | [Technically compared](/en/projects/grafik-visual-studio/datenfluss) | [Technically compared](/fr/projects/grafik-visual-studio/datenfluss) |
| [projects/grafik-visual-studio/devices-tablet.md](/projects/grafik-visual-studio/devices-tablet) | [Content reviewed](/en/projects/grafik-visual-studio/devices-tablet) | [Content reviewed](/fr/projects/grafik-visual-studio/devices-tablet) |
| [projects/grafik-visual-studio/editor.md](/projects/grafik-visual-studio/editor) | [Technically compared](/en/projects/grafik-visual-studio/editor) | [Technically compared](/fr/projects/grafik-visual-studio/editor) |
| [projects/grafik-visual-studio/energy.md](/projects/grafik-visual-studio/energy) | [Technically compared](/en/projects/grafik-visual-studio/energy) | [Technically compared](/fr/projects/grafik-visual-studio/energy) |
| [projects/grafik-visual-studio/ha-quellen-climate.md](/projects/grafik-visual-studio/ha-quellen-climate) | [Content reviewed](/en/projects/grafik-visual-studio/ha-quellen-climate) | [Content reviewed](/fr/projects/grafik-visual-studio/ha-quellen-climate) |
| [projects/grafik-visual-studio/index.md](/projects/grafik-visual-studio/) | [Technically compared](/en/projects/grafik-visual-studio/) | [Technically compared](/fr/projects/grafik-visual-studio/) |
| [projects/grafik-visual-studio/industrial.md](/projects/grafik-visual-studio/industrial) | [Technically compared](/en/projects/grafik-visual-studio/industrial) | [Technically compared](/fr/projects/grafik-visual-studio/industrial) |
| [projects/grafik-visual-studio/interaktiv.md](/projects/grafik-visual-studio/interaktiv) | [Content reviewed](/en/projects/grafik-visual-studio/interaktiv) | [Content reviewed](/fr/projects/grafik-visual-studio/interaktiv) |
| [projects/grafik-visual-studio/materialdesign.md](/projects/grafik-visual-studio/materialdesign) | [Technically compared](/en/projects/grafik-visual-studio/materialdesign) | [Technically compared](/fr/projects/grafik-visual-studio/materialdesign) |
| [projects/grafik-visual-studio/packer.md](/projects/grafik-visual-studio/packer) | [Technically compared](/en/projects/grafik-visual-studio/packer) | [Technically compared](/fr/projects/grafik-visual-studio/packer) |
| [projects/grafik-visual-studio/palette-runtime.md](/projects/grafik-visual-studio/palette-runtime) | [Content reviewed](/en/projects/grafik-visual-studio/palette-runtime) | [Content reviewed](/fr/projects/grafik-visual-studio/palette-runtime) |
| [projects/grafik-visual-studio/printer.md](/projects/grafik-visual-studio/printer) | [Technically compared](/en/projects/grafik-visual-studio/printer) | [Technically compared](/fr/projects/grafik-visual-studio/printer) |
| [projects/grafik-visual-studio/solar.md](/projects/grafik-visual-studio/solar) | [Technically compared](/en/projects/grafik-visual-studio/solar) | [Technically compared](/fr/projects/grafik-visual-studio/solar) |
| [projects/grafik-visual-studio/svg-line.md](/projects/grafik-visual-studio/svg-line) | [Technically compared](/en/projects/grafik-visual-studio/svg-line) | [Technically compared](/fr/projects/grafik-visual-studio/svg-line) |
| [projects/grafik-visual-studio/svg-linebox-math.md](/projects/grafik-visual-studio/svg-linebox-math) | [Technically compared](/en/projects/grafik-visual-studio/svg-linebox-math) | [Technically compared](/fr/projects/grafik-visual-studio/svg-linebox-math) |
| [projects/grafik-visual-studio/svg-linebox.md](/projects/grafik-visual-studio/svg-linebox) | [Technically compared](/en/projects/grafik-visual-studio/svg-linebox) | [Technically compared](/fr/projects/grafik-visual-studio/svg-linebox) |
| [projects/grafik-visual-studio/technic.md](/projects/grafik-visual-studio/technic) | [Technically compared](/en/projects/grafik-visual-studio/technic) | [Technically compared](/fr/projects/grafik-visual-studio/technic) |
| [projects/grafik-visual-studio/tool-pakete.md](/projects/grafik-visual-studio/tool-pakete) | [Technically compared](/en/projects/grafik-visual-studio/tool-packages) | [Technically compared](/fr/projects/grafik-visual-studio/tool-packages) |
| [projects/grafik-visual-studio/weather-heating.md](/projects/grafik-visual-studio/weather-heating) | [Technically compared](/en/projects/grafik-visual-studio/weather-heating) | [Technically compared](/fr/projects/grafik-visual-studio/weather-heating) |
| [projects/grafik-visual-studio/widget-pakete.md](/projects/grafik-visual-studio/widget-pakete) | [Technically compared](/en/projects/grafik-visual-studio/widget-packages) | [Technically compared](/fr/projects/grafik-visual-studio/widget-packages) |
| [projects/grafik-visual-studio/widgets.md](/projects/grafik-visual-studio/widgets) | [Technically compared](/en/projects/grafik-visual-studio/widgets) | [Technically compared](/fr/projects/grafik-visual-studio/widgets) |
| [projects/grafik-visual-studio/zeichnen.md](/projects/grafik-visual-studio/zeichnen) | [Technically compared](/en/projects/grafik-visual-studio/zeichnen) | [Technically compared](/fr/projects/grafik-visual-studio/zeichnen) |
| [projects/hadash/ansicht-exportieren.md](/projects/hadash/ansicht-exportieren) | [Content reviewed](/en/projects/hadash/export-view) | [Content reviewed](/fr/projects/hadash/export-view) |
| [projects/hadash/backups-und-json.md](/projects/hadash/backups-und-json) | [Content reviewed](/en/projects/hadash/backups-and-json) | [Content reviewed](/fr/projects/hadash/backups-and-json) |
| [projects/hadash/dashboard-einlesen.md](/projects/hadash/dashboard-einlesen) | [Content reviewed](/en/projects/hadash/import-dashboard) | [Content reviewed](/fr/projects/hadash/import-dashboard) |
| [projects/hadash/erste-schritte.md](/projects/hadash/erste-schritte) | [Content reviewed](/en/projects/hadash/getting-started) | [Content reviewed](/fr/projects/hadash/getting-started) |
| [projects/hadash/index.md](/projects/hadash/) | [Content reviewed](/en/projects/hadash/) | [Content reviewed](/fr/projects/hadash/) |
| [projects/hadash/portable-nutzung.md](/projects/hadash/portable-nutzung) | [Content reviewed](/en/projects/hadash/portable-usage) | [Content reviewed](/fr/projects/hadash/portable-usage) |
| [projects/heizoel-to-mqtt/beispiele.md](/projects/heizoel-to-mqtt/beispiele) | [Content reviewed](/en/projects/heizoel-to-mqtt/examples) | [Content reviewed](/fr/projects/heizoel-to-mqtt/examples) |
| [projects/heizoel-to-mqtt/entitaeten.md](/projects/heizoel-to-mqtt/entitaeten) | [Content reviewed](/en/projects/heizoel-to-mqtt/entities) | [Content reviewed](/fr/projects/heizoel-to-mqtt/entities) |
| [projects/heizoel-to-mqtt/index.md](/projects/heizoel-to-mqtt/) | [Content reviewed](/en/projects/heizoel-to-mqtt/) | [Content reviewed](/fr/projects/heizoel-to-mqtt/) |
| [projects/heizoel-to-mqtt/installation.md](/projects/heizoel-to-mqtt/installation) | [Content reviewed](/en/projects/heizoel-to-mqtt/installation) | [Content reviewed](/fr/projects/heizoel-to-mqtt/installation) |
| [projects/heizoel-to-mqtt/konfiguration.md](/projects/heizoel-to-mqtt/konfiguration) | [Content reviewed](/en/projects/heizoel-to-mqtt/configuration) | [Content reviewed](/fr/projects/heizoel-to-mqtt/configuration) |
| [projects/index.md](/projects/) | [Content reviewed](/en/projects/) | [Content reviewed](/fr/projects/) |
| [projects/logic-studio/index.md](/projects/logic-studio/) | [Technically compared](/en/projects/logic-studio/) | [Technically compared](/fr/projects/logic-studio/) |
| [projects/logic-studio/user-guide.md](/projects/logic-studio/user-guide) | [Content reviewed](/en/projects/logic-studio/user-guide) | [Content reviewed](/fr/projects/logic-studio/user-guide) |
| [projects/logic-studio/user-guide/blocks-a.md](/projects/logic-studio/user-guide/blocks-a) | [Content reviewed](/en/projects/logic-studio/user-guide/blocks-a) | [Content reviewed](/fr/projects/logic-studio/user-guide/blocks-a) |
| [projects/logic-studio/user-guide/blocks-js.md](/projects/logic-studio/user-guide/blocks-js) | [Content reviewed](/en/projects/logic-studio/user-guide/blocks-js) | [Content reviewed](/fr/projects/logic-studio/user-guide/blocks-js) |
| [projects/logic-studio/user-guide/feedback.md](/projects/logic-studio/user-guide/feedback) | [Content reviewed](/en/projects/logic-studio/user-guide/feedback) | [Content reviewed](/fr/projects/logic-studio/user-guide/feedback) |
| [projects/logic-studio/user-guide/function-plan.md](/projects/logic-studio/user-guide/function-plan) | [Content reviewed](/en/projects/logic-studio/user-guide/function-plan) | [Content reviewed](/fr/projects/logic-studio/user-guide/function-plan) |
| [projects/logic-studio/user-guide/ha-yaml.md](/projects/logic-studio/user-guide/ha-yaml) | [Content reviewed](/en/projects/logic-studio/user-guide/ha-yaml) | [Content reviewed](/fr/projects/logic-studio/user-guide/ha-yaml) |
| [projects/logic-studio/user-guide/javascript.md](/projects/logic-studio/user-guide/javascript) | [Content reviewed](/en/projects/logic-studio/user-guide/javascript) | [Content reviewed](/fr/projects/logic-studio/user-guide/javascript) |
| [projects/logic-studio/user-guide/rules.md](/projects/logic-studio/user-guide/rules) | [Content reviewed](/en/projects/logic-studio/user-guide/rules) | [Content reviewed](/fr/projects/logic-studio/user-guide/rules) |
| [projects/logic-studio/user-guide/typescript.md](/projects/logic-studio/user-guide/typescript) | [Content reviewed](/en/projects/logic-studio/user-guide/typescript) | [Content reviewed](/fr/projects/logic-studio/user-guide/typescript) |
| [projects/mqtt-client/index.md](/projects/mqtt-client/) | [Technically compared](/en/projects/mqtt-client/) | [Technically compared](/fr/projects/mqtt-client/) |
| [projects/mqtt-client/iobroker-roles.md](/projects/mqtt-client/iobroker-roles) | [Technically compared](/en/projects/mqtt-client/iobroker-roles) | [Technically compared](/fr/projects/mqtt-client/iobroker-roles) |
| [projects/parcel-to-mqtt/beispiele.md](/projects/parcel-to-mqtt/beispiele) | [Content reviewed](/en/projects/parcel-to-mqtt/examples) | [Content reviewed](/fr/projects/parcel-to-mqtt/examples) |
| [projects/parcel-to-mqtt/entitaeten.md](/projects/parcel-to-mqtt/entitaeten) | [Content reviewed](/en/projects/parcel-to-mqtt/entities) | [Content reviewed](/fr/projects/parcel-to-mqtt/entities) |
| [projects/parcel-to-mqtt/index.md](/projects/parcel-to-mqtt/) | [Content reviewed](/en/projects/parcel-to-mqtt/) | [Content reviewed](/fr/projects/parcel-to-mqtt/) |
| [projects/parcel-to-mqtt/installation.md](/projects/parcel-to-mqtt/installation) | [Content reviewed](/en/projects/parcel-to-mqtt/installation) | [Content reviewed](/fr/projects/parcel-to-mqtt/installation) |
| [projects/parcel-to-mqtt/konfiguration.md](/projects/parcel-to-mqtt/konfiguration) | [Content reviewed](/en/projects/parcel-to-mqtt/configuration) | [Content reviewed](/fr/projects/parcel-to-mqtt/configuration) |
| [projects/sidebar-colors/index.md](/projects/sidebar-colors/) | [Technically compared](/en/projects/sidebar-colors/) | [Technically compared](/fr/projects/sidebar-colors/) |
| [projects/sidebar-manager/index.md](/projects/sidebar-manager/) | [Technically compared](/en/projects/sidebar-manager/) | [Technically compared](/fr/projects/sidebar-manager/) |
| [projects/uix/broker/broker.md](/projects/uix/broker/broker) | [Content reviewed · Difference reviewed](/en/projects/uix/broker/broker) | [Content reviewed · Difference reviewed](/fr/projects/uix/broker/broker) |
| [projects/uix/broker/directives.md](/projects/uix/broker/directives) | [Content present · Difference reviewed](/en/projects/uix/broker/directives) | [Content present · Difference reviewed](/fr/projects/uix/broker/directives) |
| [projects/uix/broker/examples.md](/projects/uix/broker/examples) | [Content present · Difference reviewed](/en/projects/uix/broker/examples) | [Content present · Difference reviewed](/fr/projects/uix/broker/examples) |
| [projects/uix/broker/index.md](/projects/uix/broker/) | [Content reviewed · Difference reviewed](/en/projects/uix/broker/) | [Content reviewed · Difference reviewed](/fr/projects/uix/broker/) |
| [projects/uix/broker/interaction-anchors.md](/projects/uix/broker/interaction-anchors) | [Content reviewed · Difference reviewed](/en/projects/uix/broker/interaction-anchors) | [Content reviewed · Difference reviewed](/fr/projects/uix/broker/interaction-anchors) |
| [projects/uix/broker/realms.md](/projects/uix/broker/realms) | [Content reviewed · Difference reviewed](/en/projects/uix/broker/realms) | [Content reviewed · Difference reviewed](/fr/projects/uix/broker/realms) |
| [projects/uix/broker/rules.md](/projects/uix/broker/rules) | [Content present · Difference reviewed](/en/projects/uix/broker/rules) | [Content present · Difference reviewed](/fr/projects/uix/broker/rules) |
| [projects/uix/concepts/application.md](/projects/uix/concepts/application) | [Content reviewed · Difference reviewed](/en/projects/uix/concepts/application) | [Content reviewed · Difference reviewed](/fr/projects/uix/concepts/application) |
| [projects/uix/concepts/context.md](/projects/uix/concepts/context) | [Content reviewed](/en/projects/uix/concepts/context) | [Content reviewed](/fr/projects/uix/concepts/context) |
| [projects/uix/concepts/dom.md](/projects/uix/concepts/dom) | [Content present · Difference reviewed](/en/projects/uix/concepts/dom) | [Technically compared](/fr/projects/uix/concepts/dom) |
| [projects/uix/concepts/index.md](/projects/uix/concepts/) | [Content reviewed · Difference reviewed](/en/projects/uix/concepts/) | [Content reviewed](/fr/projects/uix/concepts/) |
| [projects/uix/contributing.md](/projects/uix/contributing) | [Content present · Difference reviewed](/en/projects/uix/contributing) | [Content present · Difference reviewed](/fr/projects/uix/contributing) |
| [projects/uix/debugging/cache.md](/projects/uix/debugging/cache) | [Content reviewed · Difference reviewed](/en/projects/uix/debugging/cache) | [Content reviewed · Difference reviewed](/fr/projects/uix/debugging/cache) |
| [projects/uix/debugging/cards.md](/projects/uix/debugging/cards) | [Content reviewed · Difference reviewed](/en/projects/uix/debugging/cards) | [Content reviewed](/fr/projects/uix/debugging/cards) |
| [projects/uix/debugging/index.md](/projects/uix/debugging/) | [Content reviewed · Difference reviewed](/en/projects/uix/debugging/) | [Content reviewed](/fr/projects/uix/debugging/) |
| [projects/uix/debugging/templates.md](/projects/uix/debugging/templates) | [Content reviewed · Difference reviewed](/en/projects/uix/debugging/templates) | [Content reviewed](/fr/projects/uix/debugging/templates) |
| [projects/uix/developers/cards.md](/projects/uix/developers/cards) | [Content reviewed · Difference reviewed](/en/projects/uix/developers/cards) | [Content reviewed](/fr/projects/uix/developers/cards) |
| [projects/uix/developers/index.md](/projects/uix/developers/) | [Content reviewed · Difference reviewed](/en/projects/uix/developers/) | [Content reviewed](/fr/projects/uix/developers/) |
| [projects/uix/developers/themes.md](/projects/uix/developers/themes) | [Content reviewed · Difference reviewed](/en/projects/uix/developers/themes) | [Content reviewed](/fr/projects/uix/developers/themes) |
| [projects/uix/extras/always-patch-ha-card.md](/projects/uix/extras/always-patch-ha-card) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/always-patch-ha-card) | [Content reviewed · Difference reviewed](/fr/projects/uix/extras/always-patch-ha-card) |
| [projects/uix/extras/custom-sidebar-panels.md](/projects/uix/extras/custom-sidebar-panels) | [Content reviewed](/en/projects/uix/extras/custom-sidebar-panels) | [Content reviewed](/fr/projects/uix/extras/custom-sidebar-panels) |
| [projects/uix/extras/dialog-styling-delay.md](/projects/uix/extras/dialog-styling-delay) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/dialog-styling-delay) | [Content reviewed](/fr/projects/uix/extras/dialog-styling-delay) |
| [projects/uix/extras/disable-entity-picture-image-override.md](/projects/uix/extras/disable-entity-picture-image-override) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/disable-entity-picture-image-override) | [Content reviewed · Difference reviewed](/fr/projects/uix/extras/disable-entity-picture-image-override) |
| [projects/uix/extras/disable-icon-styling.md](/projects/uix/extras/disable-icon-styling) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/disable-icon-styling) | [Content reviewed · Difference reviewed](/fr/projects/uix/extras/disable-icon-styling) |
| [projects/uix/extras/frontend-states-throttling.md](/projects/uix/extras/frontend-states-throttling) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/frontend-states-throttling) | [Content reviewed · Difference reviewed](/fr/projects/uix/extras/frontend-states-throttling) |
| [projects/uix/extras/hash-template-variable-updates.md](/projects/uix/extras/hash-template-variable-updates) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/hash-template-variable-updates) | [Content reviewed](/fr/projects/uix/extras/hash-template-variable-updates) |
| [projects/uix/extras/index.md](/projects/uix/extras/) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/) | [Content reviewed · Difference reviewed](/fr/projects/uix/extras/) |
| [projects/uix/extras/style-custom-panels.md](/projects/uix/extras/style-custom-panels) | [Content reviewed](/en/projects/uix/extras/style-custom-panels) | [Content reviewed](/fr/projects/uix/extras/style-custom-panels) |
| [projects/uix/extras/style-frame-panels.md](/projects/uix/extras/style-frame-panels) | [Content reviewed · Difference reviewed](/en/projects/uix/extras/style-frame-panels) | [Content reviewed](/fr/projects/uix/extras/style-frame-panels) |
| [projects/uix/extras/uix-actions.md](/projects/uix/extras/uix-actions) | [Content present · Difference reviewed](/en/projects/uix/extras/uix-actions) | [Content present · Difference reviewed](/fr/projects/uix/extras/uix-actions) |
| [projects/uix/faq.md](/projects/uix/faq) | [Content reviewed · Difference reviewed](/en/projects/uix/faq) | [Content reviewed · Difference reviewed](/fr/projects/uix/faq) |
| [projects/uix/forge/forge.md](/projects/uix/forge/forge) | [Content present · Difference reviewed](/en/projects/uix/forge/forge) | [Technically compared](/fr/projects/uix/forge/forge) |
| [projects/uix/forge/foundries.md](/projects/uix/forge/foundries) | [Content present · Difference reviewed](/en/projects/uix/forge/foundries) | [Content present · Difference reviewed](/fr/projects/uix/forge/foundries) |
| [projects/uix/forge/index.md](/projects/uix/forge/) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/) | [Content reviewed · Difference reviewed](/fr/projects/uix/forge/) |
| [projects/uix/forge/sparks/attribute.md](/projects/uix/forge/sparks/attribute) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/attribute) | [Content reviewed · Difference reviewed](/fr/projects/uix/forge/sparks/attribute) |
| [projects/uix/forge/sparks/background.md](/projects/uix/forge/sparks/background) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/background) | [Technically compared](/fr/projects/uix/forge/sparks/background) |
| [projects/uix/forge/sparks/badge.md](/projects/uix/forge/sparks/badge) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/badge) | [Technically compared](/fr/projects/uix/forge/sparks/badge) |
| [projects/uix/forge/sparks/button.md](/projects/uix/forge/sparks/button) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/button) | [Content present · Difference reviewed](/fr/projects/uix/forge/sparks/button) |
| [projects/uix/forge/sparks/event.md](/projects/uix/forge/sparks/event) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/event) | [Content reviewed](/fr/projects/uix/forge/sparks/event) |
| [projects/uix/forge/sparks/form.md](/projects/uix/forge/sparks/form) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/form) | [Technically compared](/fr/projects/uix/forge/sparks/form) |
| [projects/uix/forge/sparks/grid.md](/projects/uix/forge/sparks/grid) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/grid) | [Technically compared](/fr/projects/uix/forge/sparks/grid) |
| [projects/uix/forge/sparks/index.md](/projects/uix/forge/sparks/) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/) | [Content reviewed · Difference reviewed](/fr/projects/uix/forge/sparks/) |
| [projects/uix/forge/sparks/lock.md](/projects/uix/forge/sparks/lock) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/lock) | [Technically compared](/fr/projects/uix/forge/sparks/lock) |
| [projects/uix/forge/sparks/map.md](/projects/uix/forge/sparks/map) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/map) | [Technically compared](/fr/projects/uix/forge/sparks/map) |
| [projects/uix/forge/sparks/more-info.md](/projects/uix/forge/sparks/more-info) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/more-info) | [Content reviewed](/fr/projects/uix/forge/sparks/more-info) |
| [projects/uix/forge/sparks/overlay-icon.md](/projects/uix/forge/sparks/overlay-icon) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/overlay-icon) | [Technically compared](/fr/projects/uix/forge/sparks/overlay-icon) |
| [projects/uix/forge/sparks/search.md](/projects/uix/forge/sparks/search) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/search) | [Content reviewed](/fr/projects/uix/forge/sparks/search) |
| [projects/uix/forge/sparks/state-badge.md](/projects/uix/forge/sparks/state-badge) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/state-badge) | [Content reviewed](/fr/projects/uix/forge/sparks/state-badge) |
| [projects/uix/forge/sparks/theme.md](/projects/uix/forge/sparks/theme) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/theme) | [Content reviewed](/fr/projects/uix/forge/sparks/theme) |
| [projects/uix/forge/sparks/tile-icon.md](/projects/uix/forge/sparks/tile-icon) | [Content reviewed · Difference reviewed](/en/projects/uix/forge/sparks/tile-icon) | [Content reviewed · Difference reviewed](/fr/projects/uix/forge/sparks/tile-icon) |
| [projects/uix/forge/sparks/tooltip.md](/projects/uix/forge/sparks/tooltip) | [Content present · Difference reviewed](/en/projects/uix/forge/sparks/tooltip) | [Content present · Difference reviewed](/fr/projects/uix/forge/sparks/tooltip) |
| [projects/uix/guides.md](/projects/uix/guides) | [Content reviewed · Difference reviewed](/en/projects/uix/guides) | [Content reviewed](/fr/projects/uix/guides) |
| [projects/uix/index.md](/projects/uix/) | [Content reviewed · Difference reviewed](/en/projects/uix/) | [Content reviewed](/fr/projects/uix/) |
| [projects/uix/license.md](/projects/uix/license) | [Content reviewed · Difference reviewed](/en/projects/uix/license) | [Content reviewed](/fr/projects/uix/license) |
| [projects/uix/quick-start.md](/projects/uix/quick-start) | [Content reviewed · Difference reviewed](/en/projects/uix/quick-start) | [Content reviewed · Difference reviewed](/fr/projects/uix/quick-start) |
| [projects/uix/translation-status.md](/projects/uix/translation-status) | [Content present · Difference reviewed](/en/projects/uix/translation-status) | [Content present · Difference reviewed](/fr/projects/uix/translation-status) |
| [projects/uix/using/apps.md](/projects/uix/using/apps) | [Content reviewed · Difference reviewed](/en/projects/uix/using/apps) | [Content reviewed](/fr/projects/uix/using/apps) |
| [projects/uix/using/cards.md](/projects/uix/using/cards) | [Content reviewed · Difference reviewed](/en/projects/uix/using/cards) | [Content reviewed · Difference reviewed](/fr/projects/uix/using/cards) |
| [projects/uix/using/custom-panels.md](/projects/uix/using/custom-panels) | [Content reviewed · Difference reviewed](/en/projects/uix/using/custom-panels) | [Content reviewed](/fr/projects/uix/using/custom-panels) |
| [projects/uix/using/custom-sidebar-panels.md](/projects/uix/using/custom-sidebar-panels) | [Content reviewed](/en/projects/uix/using/custom-sidebar-panels) | [Content reviewed](/fr/projects/uix/using/custom-sidebar-panels) |
| [projects/uix/using/entities.md](/projects/uix/using/entities) | [Content reviewed · Difference reviewed](/en/projects/uix/using/entities) | [Content reviewed](/fr/projects/uix/using/entities) |
| [projects/uix/using/icons.md](/projects/uix/using/icons) | [Content reviewed · Difference reviewed](/en/projects/uix/using/icons) | [Content reviewed](/fr/projects/uix/using/icons) |
| [projects/uix/using/images.md](/projects/uix/using/images) | [Content reviewed · Difference reviewed](/en/projects/uix/using/images) | [Content reviewed](/fr/projects/uix/using/images) |
| [projects/uix/using/index.md](/projects/uix/using/) | [Content reviewed · Difference reviewed](/en/projects/uix/using/) | [Content reviewed](/fr/projects/uix/using/) |
| [projects/uix/using/other.md](/projects/uix/using/other) | [Content reviewed · Difference reviewed](/en/projects/uix/using/other) | [Content reviewed](/fr/projects/uix/using/other) |
| [projects/uix/using/section-backgrounds.md](/projects/uix/using/section-backgrounds) | [Content reviewed · Difference reviewed](/en/projects/uix/using/section-backgrounds) | [Content reviewed](/fr/projects/uix/using/section-backgrounds) |
| [projects/uix/using/templates.md](/projects/uix/using/templates) | [Content present · Difference reviewed](/en/projects/uix/using/templates) | [Technically compared](/fr/projects/uix/using/templates) |
| [projects/uix/using/themes.md](/projects/uix/using/themes) | [Content present · Difference reviewed](/en/projects/uix/using/themes) | [Technically compared](/fr/projects/uix/using/themes) |
| [projects/uix/using/view-backgrounds.md](/projects/uix/using/view-backgrounds) | [Content present · Difference reviewed](/en/projects/uix/using/view-backgrounds) | [Technically compared](/fr/projects/uix/using/view-backgrounds) |
| [projects/ultimate-timer/beispiele.md](/projects/ultimate-timer/beispiele) | [Content reviewed](/en/projects/ultimate-timer/examples) | [Content reviewed](/fr/projects/ultimate-timer/examples) |
| [projects/ultimate-timer/funktionsweise.md](/projects/ultimate-timer/funktionsweise) | [Content reviewed](/en/projects/ultimate-timer/how-it-works) | [Content reviewed](/fr/projects/ultimate-timer/how-it-works) |
| [projects/ultimate-timer/index.md](/projects/ultimate-timer/) | [Content reviewed](/en/projects/ultimate-timer/) | [Content reviewed](/fr/projects/ultimate-timer/) |
| [projects/ultimate-timer/installation.md](/projects/ultimate-timer/installation) | [Content reviewed](/en/projects/ultimate-timer/installation) | [Content reviewed](/fr/projects/ultimate-timer/installation) |
| [projects/ultimate-timer/konfiguration.md](/projects/ultimate-timer/konfiguration) | [Content reviewed](/en/projects/ultimate-timer/configuration) | [Content reviewed](/fr/projects/ultimate-timer/configuration) |
| [sammlung/calendar-card-pro/beispiele.md](/sammlung/calendar-card-pro/beispiele) | [Content reviewed](/en/collection/calendar-card-pro/beispiele) | [Content reviewed](/fr/collection/calendar-card-pro/beispiele) |
| [sammlung/calendar-card-pro/entwicklung.md](/sammlung/calendar-card-pro/entwicklung) | [Content reviewed](/en/collection/calendar-card-pro/entwicklung) | [Content reviewed](/fr/collection/calendar-card-pro/entwicklung) |
| [sammlung/calendar-card-pro/features.md](/sammlung/calendar-card-pro/features) | [Content reviewed](/en/collection/calendar-card-pro/features) | [Content reviewed](/fr/collection/calendar-card-pro/features) |
| [sammlung/calendar-card-pro/index.md](/sammlung/calendar-card-pro/) | [Content reviewed](/en/collection/calendar-card-pro/) | [Content reviewed](/fr/collection/calendar-card-pro/) |
| [sammlung/calendar-card-pro/installation.md](/sammlung/calendar-card-pro/installation) | [Content reviewed](/en/collection/calendar-card-pro/installation) | [Content reviewed](/fr/collection/calendar-card-pro/installation) |
| [sammlung/calendar-card-pro/konfiguration.md](/sammlung/calendar-card-pro/konfiguration) | [Technically compared](/en/collection/calendar-card-pro/konfiguration) | [Technically compared](/fr/collection/calendar-card-pro/konfiguration) |
| [sammlung/calendar-card-pro/lizenz-und-stand.md](/sammlung/calendar-card-pro/lizenz-und-stand) | [Content reviewed](/en/collection/calendar-card-pro/lizenz-und-stand) | [Content reviewed](/fr/collection/calendar-card-pro/lizenz-und-stand) |
| [sammlung/calendar-card-pro/nutzung.md](/sammlung/calendar-card-pro/nutzung) | [Content reviewed](/en/collection/calendar-card-pro/nutzung) | [Content reviewed](/fr/collection/calendar-card-pro/nutzung) |
| [sammlung/dashboard-layout-card-v2/index.md](/sammlung/dashboard-layout-card-v2/) | [Technically compared](/en/collection/dashboard-layout-card-v2/) | [Technically compared](/fr/collection/dashboard-layout-card-v2/) |
| [sammlung/flex-table-card/aktionen.md](/sammlung/flex-table-card/aktionen) | [Content reviewed](/en/collection/flex-table-card/aktionen) | [Content reviewed](/fr/collection/flex-table-card/aktionen) |
| [sammlung/flex-table-card/beispiele-aus-forum.md](/sammlung/flex-table-card/beispiele-aus-forum) | [Technically compared](/en/collection/flex-table-card/beispiele-aus-forum) | [Technically compared](/fr/collection/flex-table-card/beispiele-aus-forum) |
| [sammlung/flex-table-card/css.md](/sammlung/flex-table-card/css) | [Content reviewed](/en/collection/flex-table-card/css) | [Content reviewed](/fr/collection/flex-table-card/css) |
| [sammlung/flex-table-card/datenquellen.md](/sammlung/flex-table-card/datenquellen) | [Content reviewed](/en/collection/flex-table-card/datenquellen) | [Content reviewed](/fr/collection/flex-table-card/datenquellen) |
| [sammlung/flex-table-card/externe-daten.md](/sammlung/flex-table-card/externe-daten) | [Content reviewed](/en/collection/flex-table-card/externe-daten) | [Content reviewed](/fr/collection/flex-table-card/externe-daten) |
| [sammlung/flex-table-card/formatierung.md](/sammlung/flex-table-card/formatierung) | [Content reviewed](/en/collection/flex-table-card/formatierung) | [Content reviewed](/fr/collection/flex-table-card/formatierung) |
| [sammlung/flex-table-card/grundlagen.md](/sammlung/flex-table-card/grundlagen) | [Content reviewed](/en/collection/flex-table-card/grundlagen) | [Content reviewed](/fr/collection/flex-table-card/grundlagen) |
| [sammlung/flex-table-card/header-footer.md](/sammlung/flex-table-card/header-footer) | [Content reviewed](/en/collection/flex-table-card/header-footer) | [Content reviewed](/fr/collection/flex-table-card/header-footer) |
| [sammlung/flex-table-card/index.md](/sammlung/flex-table-card/) | [Content reviewed](/en/collection/flex-table-card/) | [Content reviewed](/fr/collection/flex-table-card/) |
| [sammlung/flex-table-card/installation.md](/sammlung/flex-table-card/installation) | [Content reviewed](/en/collection/flex-table-card/installation) | [Content reviewed](/fr/collection/flex-table-card/installation) |
| [sammlung/flex-table-card/paketliste.md](/sammlung/flex-table-card/paketliste) | [Content reviewed](/en/collection/flex-table-card/paketliste) | [Content reviewed](/fr/collection/flex-table-card/paketliste) |
| [sammlung/flex-table-card/referenz.md](/sammlung/flex-table-card/referenz) | [Content reviewed](/en/collection/flex-table-card/referenz) | [Content reviewed](/fr/collection/flex-table-card/referenz) |
| [sammlung/flex-table-card/sortierung.md](/sammlung/flex-table-card/sortierung) | [Content reviewed](/en/collection/flex-table-card/sortierung) | [Content reviewed](/fr/collection/flex-table-card/sortierung) |
| [sammlung/frosted-glass-manager/index.md](/sammlung/frosted-glass-manager/) | [Content reviewed](/en/collection/frosted-glass-manager/) | [Content reviewed](/fr/collection/frosted-glass-manager/) |
| [sammlung/frosted-glass-theme/index.md](/sammlung/frosted-glass-theme/) | [Content reviewed](/en/collection/frosted-glass-theme/) | [Content reviewed](/fr/collection/frosted-glass-theme/) |
| [sammlung/ha-2026-11-kompatibilitaet.md](/sammlung/ha-2026-11-kompatibilitaet) | [Technically compared](/en/collection/ha-2026-11-compatibility) | [Technically compared](/fr/collection/ha-2026-11-compatibility) |
| [sammlung/ha-apps.md](/sammlung/ha-apps) | [Content reviewed](/en/collection/ha-apps) | [Content reviewed](/fr/collection/ha-apps) |
| [sammlung/ha-automation-exporter/index.md](/sammlung/ha-automation-exporter/) | [Content reviewed](/en/collection/ha-automation-exporter/) | [Content reviewed](/fr/collection/ha-automation-exporter/) |
| [sammlung/ha-blueprints.md](/sammlung/ha-blueprints) | [Content reviewed](/en/collection/ha-blueprints) | [Content reviewed](/fr/collection/ha-blueprints) |
| [sammlung/ha-cards.md](/sammlung/ha-cards) | [Content reviewed](/en/collection/ha-cards) | [Content reviewed](/fr/collection/ha-cards) |
| [sammlung/ha-dashboard.md](/sammlung/ha-dashboard) | [Content reviewed](/en/collection/ha-dashboard) | [Content reviewed](/fr/collection/ha-dashboard) |
| [sammlung/ha-empfehlungen.md](/sammlung/ha-empfehlungen) | [Content reviewed](/en/collection/ha-recommendations) | [Content reviewed](/fr/collection/ha-recommendations) |
| [sammlung/ha-integrationen.md](/sammlung/ha-integrationen) | [Content reviewed](/en/collection/ha-integrations) | [Content reviewed](/fr/collection/ha-integrations) |
| [sammlung/ha-tools.md](/sammlung/ha-tools) | [Content reviewed](/en/collection/ha-tools) | [Content reviewed](/fr/collection/ha-tools) |
| [sammlung/hacs-dokus.md](/sammlung/hacs-dokus) | [Content reviewed](/en/collection/hacs-docs) | [Content reviewed](/fr/collection/hacs-docs) |
| [sammlung/index.md](/sammlung/) | [Content reviewed](/en/collection/) | [Content reviewed](/fr/collection/) |
| [sammlung/mushroom/beispiele.md](/sammlung/mushroom/beispiele) | [Content reviewed](/en/collection/mushroom/beispiele) | [Content reviewed](/fr/collection/mushroom/beispiele) |
| [sammlung/mushroom/entwicklung.md](/sammlung/mushroom/entwicklung) | [Content reviewed](/en/collection/mushroom/entwicklung) | [Content reviewed](/fr/collection/mushroom/entwicklung) |
| [sammlung/mushroom/fehlersuche.md](/sammlung/mushroom/fehlersuche) | [Content reviewed](/en/collection/mushroom/fehlersuche) | [Content reviewed](/fr/collection/mushroom/fehlersuche) |
| [sammlung/mushroom/index.md](/sammlung/mushroom/) | [Content reviewed](/en/collection/mushroom/) | [Content reviewed](/fr/collection/mushroom/) |
| [sammlung/mushroom/installation.md](/sammlung/mushroom/installation) | [Content reviewed](/en/collection/mushroom/installation) | [Content reviewed](/fr/collection/mushroom/installation) |
| [sammlung/mushroom/karten.md](/sammlung/mushroom/karten) | [Content reviewed](/en/collection/mushroom/karten) | [Content reviewed](/fr/collection/mushroom/karten) |
| [sammlung/mushroom/lizenz-und-stand.md](/sammlung/mushroom/lizenz-und-stand) | [Content reviewed](/en/collection/mushroom/lizenz-und-stand) | [Content reviewed](/fr/collection/mushroom/lizenz-und-stand) |
| [sammlung/mushroom/nutzung.md](/sammlung/mushroom/nutzung) | [Content reviewed](/en/collection/mushroom/nutzung) | [Content reviewed](/fr/collection/mushroom/nutzung) |
| [sammlung/neomorphix-uix/index.md](/sammlung/neomorphix-uix/) | [Content reviewed](/en/collection/neomorphix-uix/) | [Content reviewed](/fr/collection/neomorphix-uix/) |
| [sammlung/testsysteme.md](/sammlung/testsysteme) | [Content reviewed](/en/collection/test-systems) | [Content reviewed](/fr/collection/test-systems) |
| [sammlung/weitere-beispiele.md](/sammlung/weitere-beispiele) | [Content reviewed](/en/collection/interesting-examples) | [Content reviewed](/fr/collection/interesting-examples) |
| [sammlung/zendure-ha/entitaeten.md](/sammlung/zendure-ha/entitaeten) | [Content reviewed](/en/collection/zendure-ha/entitaeten) | [Content reviewed](/fr/collection/zendure-ha/entitaeten) |
| [sammlung/zendure-ha/fehlersuche.md](/sammlung/zendure-ha/fehlersuche) | [Content reviewed](/en/collection/zendure-ha/fehlersuche) | [Content reviewed](/fr/collection/zendure-ha/fehlersuche) |
| [sammlung/zendure-ha/fuse-group.md](/sammlung/zendure-ha/fuse-group) | [Content reviewed](/en/collection/zendure-ha/fuse-group) | [Content reviewed](/fr/collection/zendure-ha/fuse-group) |
| [sammlung/zendure-ha/index.md](/sammlung/zendure-ha/) | [Content reviewed](/en/collection/zendure-ha/) | [Content reviewed](/fr/collection/zendure-ha/) |
| [sammlung/zendure-ha/installation.md](/sammlung/zendure-ha/installation) | [Content reviewed](/en/collection/zendure-ha/installation) | [Content reviewed](/fr/collection/zendure-ha/installation) |
| [sammlung/zendure-ha/lokales-mqtt.md](/sammlung/zendure-ha/lokales-mqtt) | [Content reviewed](/en/collection/zendure-ha/lokales-mqtt) | [Content reviewed](/fr/collection/zendure-ha/lokales-mqtt) |
| [sammlung/zendure-ha/manager.md](/sammlung/zendure-ha/manager) | [Content reviewed](/en/collection/zendure-ha/manager) | [Content reviewed](/fr/collection/zendure-ha/manager) |
