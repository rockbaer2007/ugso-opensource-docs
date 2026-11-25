---
title: Sprachstand der Dokumentation
sidebar: false
aside: false
---

# Sprachstand der Dokumentation

DE / EN / FR · 2026-11-25

Alle deutschen Referenzseiten sind jetzt auch in EN und FR mit Inhalt vorhanden. Die 128 Platzhalter wurden ersetzt und die 20 fehlenden französischen Seiten ergänzt.

Geprüft wurden sämtliche Markdown-Inhaltsseiten, ohne diese drei erzeugten Berichtsseiten: vorhandene Sprachfassungen, Platzhalter, Versionsnennungen, Überschriften, Codebeispiele und auflösbare lokale Seiten-/Bildverweise. Unterschiedliche Versionslisten oder Textlängen sind Prüfhinweise, kein automatischer Beweis für veraltete Inhalte. „Inhalt vorhanden“ bestätigt keine vollständige oder sprachlich geprüfte Übersetzung. Das Inventar prüft Upstream-Releases nicht automatisch; separat dokumentierte Quellenabgleiche wie bei UIX bleiben maßgeblich.

## Bestandsaufnahme

| Sprache | Seiten vorhanden | Fehlende Seiten | Platzhalter | Offene Prüfhinweise |
| --- | ---: | ---: | ---: | ---: |
| DE | 254 | 0 | 0 | 0 |
| EN | 254 | 0 | 0 | 3 |
| FR | 254 | 0 | 0 | 1 |

**Technischer Abgleich vom 2026-11-25:** Vorhandene Einzelbewertungen sind an die aktuellen Datei-Prüfsummen gebunden; Änderungen erfordern eine erneute Prüfung. Echte Lücken und widersprüchliche Angaben werden korrigiert, bewusst unterschiedliche Versionshistorien und redaktionelle Gliederungen mit Begründung eingeordnet. Die Tabelle zeigt die noch offenen Hinweise; der JSON-Bericht behält die automatischen Rohsignale bei. „0 offen“ bedeutet geprüft und eingeordnet, nicht wortgleiche Übersetzungen. [Dokumentierte Einzelbewertungen](/documentation-review.json).


Die Ergänzungen wurden mit Übersetzungsunterstützung erstellt und technisch gegen die deutsche Vorlage geprüft: Code, Bezeichner, Tabellen und Bilder. 14 weitere Inhaltslücken wurden als ergänzende Referenz geschlossen; vorhandene Seiten und Links bleiben erhalten. Das ist keine vollständige sprachliche Zertifizierung. Verbleibende Prüfhinweise betreffen auch bewusst unterschiedliche Zusammenfassungen und historische Versionsangaben.

Der vollständige JSON-Bericht enthält für jede Seite die Pfade, SHA-256-Prüfsummen, Versionsunterschiede, Strukturwerte und nicht aufgelöste lokale Verweise.

[JSON](/documentation-audit.json)

[UIX DE](/projects/uix/translation-status) · [UIX EN](/en/projects/uix/translation-status) · [UIX FR](/fr/projects/uix/translation-status)

**Erweiterter Abgleich vom 20.11.2026: 186 EN- und 220 FR-Seiten.** Alle zuvor nur als „Inhalt vorhanden“ ausgewiesenen Dateien wurden vollständig technisch mit ihrer Referenz verglichen: Versionen, Codeblöcke, technische Bezeichner und Verweise. Abweichungen wurden einzeln eingeordnet; eine automatische Sprachsuche wurde durch die Korrektur der gefundenen englischen Textreste ergänzt. **„Technisch abgeglichen“ ist keine vollständige sprachliche oder satzweise Inhaltsfreigabe.** „Unterschied geprüft“ bleibt die frühere Bewertung struktureller Abweichungen. „Erneut prüfen“ erscheint, sobald sich eine der beiden Dateien ändert. [Prüfumfang und Einzelbewertungen](/documentation-content-review.json).

Korrigiert wurden französische UIX-Textreste in Konzepten, Makros, Themes und Kamera-Hintergründen, ein JavaScript-Syntaxfehler im Entwicklerbeispiel sowie sieben Sprungmarken und zwei Videolinks. Die Rückfallregel für `active: false` beim Lock Spark ist in DE/FR präzisiert. Beispiele, Medien und vorhandene Anker bleiben erhalten.

## Inhaltliche Prüfung

**Inhaltlich geprüft** bedeutet: Abschnitte und Aussagen wurden auf Bedeutung, Vollständigkeit, Voraussetzungen, Einschränkungen und den Zweck der Beispiele mit der Referenz verglichen. Gefundene Fehlübersetzungen oder Widersprüche wurden korrigiert. Dies ist kein neuer App-Live-Test und keine rechtliche Zertifizierung. Noch nicht so geprüfte Seiten behalten ihren technischen Status. [Einzelbewertungen](/documentation-semantic-review.json).

| Sprache | Geprüft | Noch offen |
| --- | ---: | ---: |
| EN | 248 | 6 |
| FR | 248 | 6 |

## Vollständiges Seiteninventar

| Deutsche Referenz | EN | FR |
| --- | --- | --- |
| [blog/beitragsvorlage.md](/blog/beitragsvorlage) | [Inhaltlich geprüft](/en/blog/post-template) | [Inhaltlich geprüft](/fr/blog/post-template) |
| [blog/index.md](/blog/) | [Inhaltlich geprüft](/en/blog/) | [Inhaltlich geprüft](/fr/blog/) |
| [blog/posts/atlas-runtime-foundation.md](/blog/posts/atlas-runtime-foundation) | [Inhaltlich geprüft](/en/blog/posts/atlas-runtime-foundation) | [Inhaltlich geprüft](/fr/blog/posts/atlas-runtime-foundation) |
| [blog/posts/hadash-preview.md](/blog/posts/hadash-preview) | [Inhaltlich geprüft](/en/blog/posts/hadash-preview) | [Inhaltlich geprüft](/fr/blog/posts/hadash-preview) |
| [blog/snippets/blockly.md](/blog/snippets/blockly) | [Inhaltlich geprüft](/en/blog/snippets/blockly) | [Inhaltlich geprüft](/fr/blog/snippets/blockly) |
| [blog/snippets/home-assistant-yaml.md](/blog/snippets/home-assistant-yaml) | [Inhaltlich geprüft](/en/blog/snippets/home-assistant-yaml) | [Inhaltlich geprüft](/fr/blog/snippets/home-assistant-yaml) |
| [blog/snippets/index.md](/blog/snippets/) | [Inhaltlich geprüft](/en/blog/snippets/) | [Inhaltlich geprüft](/fr/blog/snippets/) |
| [blog/snippets/iobroker-blockly.md](/blog/snippets/iobroker-blockly) | [Inhaltlich geprüft](/en/blog/snippets/iobroker-blockly) | [Inhaltlich geprüft](/fr/blog/snippets/iobroker-blockly) |
| [blog/snippets/javascript.md](/blog/snippets/javascript) | [Inhaltlich geprüft](/en/blog/snippets/javascript) | [Inhaltlich geprüft](/fr/blog/snippets/javascript) |
| [blog/snippets/lovelace.md](/blog/snippets/lovelace) | [Inhaltlich geprüft](/en/blog/snippets/lovelace) | [Inhaltlich geprüft](/fr/blog/snippets/lovelace) |
| [eep/index.md](/eep/) | [Inhaltlich geprüft](/en/eep/) | [Inhaltlich geprüft](/fr/eep/) |
| [eep/ini-edit-translate-2026/index.md](/eep/ini-edit-translate-2026/) | [Inhaltlich geprüft](/en/eep/ini-edit-translate-2026/) | [Inhaltlich geprüft](/fr/eep/ini-edit-translate-2026/) |
| [eep/projektduplicator-2026/index.md](/eep/projektduplicator-2026/) | [Inhaltlich geprüft](/en/eep/projektduplicator-2026/) | [Inhaltlich geprüft](/fr/eep/projektduplicator-2026/) |
| [impressum/index.md](/impressum/) | [Inhaltlich geprüft](/en/impressum/) | [Inhaltlich geprüft](/fr/impressum/) |
| [index.md](/) | [Inhaltlich geprüft](/en/) | [Inhaltlich geprüft](/fr/) |
| [iobroker/publish-assistant/index.md](/iobroker/publish-assistant/) | [Inhaltlich geprüft](/en/iobroker/publish-assistant/) | [Inhaltlich geprüft](/fr/iobroker/publish-assistant/) |
| [iobroker/widgets/ugso-spezial/index.md](/iobroker/widgets/ugso-spezial/) | [Inhaltlich geprüft](/en/iobroker/widgets/ugso-spezial/) | [Inhaltlich geprüft](/fr/iobroker/widgets/ugso-spezial/) |
| [projects-diverse/index.md](/projects-diverse/) | [Inhaltlich geprüft](/en/projects-diverse/) | [Inhaltlich geprüft](/fr/projects-diverse/) |
| [projects-mqtt/index.md](/projects-mqtt/) | [Erneut prüfen](/en/projects-mqtt/) | [Erneut prüfen](/fr/projects-mqtt/) |
| [projects/atlas-plugins/automation-extractor.md](/projects/atlas-plugins/automation-extractor) | [Inhaltlich geprüft](/en/projects/atlas-plugins/automation-extractor) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/automation-extractor) |
| [projects/atlas-plugins/demo-repository.md](/projects/atlas-plugins/demo-repository) | [Inhaltlich geprüft](/en/projects/atlas-plugins/demo-repository) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/demo-repository) |
| [projects/atlas-plugins/developers/compatibility.md](/projects/atlas-plugins/developers/compatibility) | [Inhaltlich geprüft](/en/projects/atlas-plugins/developers/compatibility) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/developers/compatibility) |
| [projects/atlas-plugins/developers/index.md](/projects/atlas-plugins/developers/) | [Inhaltlich geprüft](/en/projects/atlas-plugins/developers/) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/developers/) |
| [projects/atlas-plugins/developers/manifest.md](/projects/atlas-plugins/developers/manifest) | [Inhaltlich geprüft](/en/projects/atlas-plugins/developers/manifest) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/developers/manifest) |
| [projects/atlas-plugins/developers/publishing.md](/projects/atlas-plugins/developers/publishing) | [Inhaltlich geprüft](/en/projects/atlas-plugins/developers/publishing) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/developers/publishing) |
| [projects/atlas-plugins/developers/runtime.md](/projects/atlas-plugins/developers/runtime) | [Inhaltlich geprüft](/en/projects/atlas-plugins/developers/runtime) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/developers/runtime) |
| [projects/atlas-plugins/file-studio.md](/projects/atlas-plugins/file-studio) | [Inhaltlich geprüft](/en/projects/atlas-plugins/file-studio) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/file-studio) |
| [projects/atlas-plugins/gepruefte-plugins.md](/projects/atlas-plugins/gepruefte-plugins) | [Inhaltlich geprüft](/en/projects/atlas-plugins/verified-plugins) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/verified-plugins) |
| [projects/atlas-plugins/homeassistant-card-editor.md](/projects/atlas-plugins/homeassistant-card-editor) | [Inhaltlich geprüft](/en/projects/atlas-plugins/homeassistant-card-editor) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/homeassistant-card-editor) |
| [projects/atlas-plugins/icon-library.md](/projects/atlas-plugins/icon-library) | [Inhaltlich geprüft](/en/projects/atlas-plugins/icon-library) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/icon-library) |
| [projects/atlas-plugins/icon-studio.md](/projects/atlas-plugins/icon-studio) | [Inhaltlich geprüft](/en/projects/atlas-plugins/icon-studio) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/icon-studio) |
| [projects/atlas-plugins/index.md](/projects/atlas-plugins/) | [Inhaltlich geprüft](/en/projects/atlas-plugins/) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/) |
| [projects/atlas-plugins/plugin-template.md](/projects/atlas-plugins/plugin-template) | [Inhaltlich geprüft](/en/projects/atlas-plugins/plugin-template) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/plugin-template) |
| [projects/atlas-plugins/repository-format.md](/projects/atlas-plugins/repository-format) | [Inhaltlich geprüft](/en/projects/atlas-plugins/repository-format) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/repository-format) |
| [projects/atlas-plugins/terminal.md](/projects/atlas-plugins/terminal) | [Inhaltlich geprüft](/en/projects/atlas-plugins/terminal) | [Inhaltlich geprüft](/fr/projects/atlas-plugins/terminal) |
| [projects/atlas/card-editor.md](/projects/atlas/card-editor) | [Technisch abgeglichen](/en/projects/atlas/card-editor) | [Inhalt vorhanden · Unterschied geprüft](/fr/projects/atlas/card-editor) |
| [projects/atlas/entwicklungsstand.md](/projects/atlas/entwicklungsstand) | [Inhaltlich geprüft](/en/projects/atlas/development-status) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/atlas/development-status) |
| [projects/atlas/frontend.md](/projects/atlas/frontend) | [Inhaltlich geprüft](/en/projects/atlas/frontend) | [Inhaltlich geprüft](/fr/projects/atlas/frontend) |
| [projects/atlas/homeassistant.md](/projects/atlas/homeassistant) | [Inhaltlich geprüft](/en/projects/atlas/homeassistant) | [Inhaltlich geprüft](/fr/projects/atlas/homeassistant) |
| [projects/atlas/index.md](/projects/atlas/) | [Inhaltlich geprüft](/en/projects/atlas/) | [Inhaltlich geprüft](/fr/projects/atlas/) |
| [projects/atlas/linux.md](/projects/atlas/linux) | [Inhaltlich geprüft](/en/projects/atlas/linux) | [Inhaltlich geprüft](/fr/projects/atlas/linux) |
| [projects/atlas/plugins.md](/projects/atlas/plugins) | [Inhaltlich geprüft](/en/projects/atlas/plugins) | [Inhaltlich geprüft](/fr/projects/atlas/plugins) |
| [projects/atlas/tablet-test.md](/projects/atlas/tablet-test) | [Inhaltlich geprüft](/en/projects/atlas/tablet-test) | [Inhaltlich geprüft](/fr/projects/atlas/tablet-test) |
| [projects/atlas/tablet-uix-dauertest.md](/projects/atlas/tablet-uix-dauertest) | [Inhaltlich geprüft](/en/projects/atlas/tablet-uix-dauertest) | [Inhaltlich geprüft](/fr/projects/atlas/tablet-uix-dauertest) |
| [projects/atlas/uebersicht.md](/projects/atlas/uebersicht) | [Inhaltlich geprüft](/en/projects/atlas/overview) | [Inhaltlich geprüft](/fr/projects/atlas/overview) |
| [projects/automation-status-card/index.md](/projects/automation-status-card/) | [Inhaltlich geprüft](/en/projects/automation-status-card/) | [Inhaltlich geprüft](/fr/projects/automation-status-card/) |
| [projects/blocks-for-ha/advanced.md](/projects/blocks-for-ha/advanced) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/advanced) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/advanced) |
| [projects/blocks-for-ha/blockly-audit.md](/projects/blocks-for-ha/blockly-audit) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/blockly-audit) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/blockly-audit) |
| [projects/blocks-for-ha/blocks.md](/projects/blocks-for-ha/blocks) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/blocks) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/blocks) |
| [projects/blocks-for-ha/catalog/index.md](/projects/blocks-for-ha/catalog/) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/catalog/) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/catalog/) |
| [projects/blocks-for-ha/catalog/sensor-light.md](/projects/blocks-for-ha/catalog/sensor-light) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/catalog/sensor-light) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/catalog/sensor-light) |
| [projects/blocks-for-ha/collections.md](/projects/blocks-for-ha/collections) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/collections) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/collections) |
| [projects/blocks-for-ha/conversion.md](/projects/blocks-for-ha/conversion) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/conversion) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/conversion) |
| [projects/blocks-for-ha/custom-blocks.md](/projects/blocks-for-ha/custom-blocks) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/custom-blocks) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/custom-blocks) |
| [projects/blocks-for-ha/entities.md](/projects/blocks-for-ha/entities) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/entities) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/entities) |
| [projects/blocks-for-ha/flow.md](/projects/blocks-for-ha/flow) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/flow) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/flow) |
| [projects/blocks-for-ha/index.md](/projects/blocks-for-ha/) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/blocks-for-ha/) |
| [projects/blocks-for-ha/system-template.md](/projects/blocks-for-ha/system-template) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/system-template) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/system-template) |
| [projects/blocks-for-ha/themes.md](/projects/blocks-for-ha/themes) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/themes) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/themes) |
| [projects/blocks-for-ha/time.md](/projects/blocks-for-ha/time) | [Inhaltlich geprüft](/en/projects/blocks-for-ha/time) | [Inhaltlich geprüft](/fr/projects/blocks-for-ha/time) |
| [projects/callmebot-signal/index.md](/projects/callmebot-signal/) | [Inhaltlich geprüft](/en/projects/callmebot-signal/) | [Inhaltlich geprüft](/fr/projects/callmebot-signal/) |
| [projects/callmebot/index.md](/projects/callmebot/) | [Inhaltlich geprüft](/en/projects/callmebot/) | [Inhaltlich geprüft](/fr/projects/callmebot/) |
| [projects/dashboard-user-manager/index.md](/projects/dashboard-user-manager/) | [Inhaltlich geprüft](/en/projects/dashboard-user-manager/) | [Inhaltlich geprüft](/fr/projects/dashboard-user-manager/) |
| [projects/festtags-card-editor/index.md](/projects/festtags-card-editor/) | [Inhalt vorhanden](/en/projects/festtags-card-editor/) | [Inhalt vorhanden](/fr/projects/festtags-card-editor/) |
| [projects/fritzbox-to-mqtt/beispiele.md](/projects/fritzbox-to-mqtt/beispiele) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/examples) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/examples) |
| [projects/fritzbox-to-mqtt/entitaeten.md](/projects/fritzbox-to-mqtt/entitaeten) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/entities) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/entities) |
| [projects/fritzbox-to-mqtt/fehlersuche.md](/projects/fritzbox-to-mqtt/fehlersuche) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/troubleshooting) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/troubleshooting) |
| [projects/fritzbox-to-mqtt/index.md](/projects/fritzbox-to-mqtt/) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/) |
| [projects/fritzbox-to-mqtt/installation.md](/projects/fritzbox-to-mqtt/installation) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/installation) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/installation) |
| [projects/fritzbox-to-mqtt/konfiguration.md](/projects/fritzbox-to-mqtt/konfiguration) | [Inhaltlich geprüft](/en/projects/fritzbox-to-mqtt/configuration) | [Inhaltlich geprüft](/fr/projects/fritzbox-to-mqtt/configuration) |
| [projects/grafik-visual-studio/basic.md](/projects/grafik-visual-studio/basic) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/basic) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/basic) |
| [projects/grafik-visual-studio/bildergalerie.md](/projects/grafik-visual-studio/bildergalerie) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/bildergalerie) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/bildergalerie) |
| [projects/grafik-visual-studio/calendar-plus.md](/projects/grafik-visual-studio/calendar-plus) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/calendar-plus) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/calendar-plus) |
| [projects/grafik-visual-studio/datenfluss.md](/projects/grafik-visual-studio/datenfluss) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/datenfluss) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/datenfluss) |
| [projects/grafik-visual-studio/devices-tablet.md](/projects/grafik-visual-studio/devices-tablet) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/devices-tablet) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/devices-tablet) |
| [projects/grafik-visual-studio/editor.md](/projects/grafik-visual-studio/editor) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/editor) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/editor) |
| [projects/grafik-visual-studio/energy.md](/projects/grafik-visual-studio/energy) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/energy) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/energy) |
| [projects/grafik-visual-studio/ha-quellen-climate.md](/projects/grafik-visual-studio/ha-quellen-climate) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/ha-quellen-climate) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/ha-quellen-climate) |
| [projects/grafik-visual-studio/index.md](/projects/grafik-visual-studio/) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/) |
| [projects/grafik-visual-studio/industrial.md](/projects/grafik-visual-studio/industrial) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/industrial) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/industrial) |
| [projects/grafik-visual-studio/interaktiv.md](/projects/grafik-visual-studio/interaktiv) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/interaktiv) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/interaktiv) |
| [projects/grafik-visual-studio/materialdesign.md](/projects/grafik-visual-studio/materialdesign) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/materialdesign) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/materialdesign) |
| [projects/grafik-visual-studio/packer.md](/projects/grafik-visual-studio/packer) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/packer) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/packer) |
| [projects/grafik-visual-studio/palette-runtime.md](/projects/grafik-visual-studio/palette-runtime) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/palette-runtime) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/palette-runtime) |
| [projects/grafik-visual-studio/printer.md](/projects/grafik-visual-studio/printer) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/printer) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/printer) |
| [projects/grafik-visual-studio/solar.md](/projects/grafik-visual-studio/solar) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/solar) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/solar) |
| [projects/grafik-visual-studio/svg-line.md](/projects/grafik-visual-studio/svg-line) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/svg-line) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/svg-line) |
| [projects/grafik-visual-studio/svg-linebox-math.md](/projects/grafik-visual-studio/svg-linebox-math) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/svg-linebox-math) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/svg-linebox-math) |
| [projects/grafik-visual-studio/svg-linebox.md](/projects/grafik-visual-studio/svg-linebox) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/svg-linebox) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/svg-linebox) |
| [projects/grafik-visual-studio/technic.md](/projects/grafik-visual-studio/technic) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/technic) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/technic) |
| [projects/grafik-visual-studio/tool-pakete.md](/projects/grafik-visual-studio/tool-pakete) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/tool-packages) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/tool-packages) |
| [projects/grafik-visual-studio/weather-heating.md](/projects/grafik-visual-studio/weather-heating) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/weather-heating) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/weather-heating) |
| [projects/grafik-visual-studio/widget-pakete.md](/projects/grafik-visual-studio/widget-pakete) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/widget-packages) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/widget-packages) |
| [projects/grafik-visual-studio/widgets.md](/projects/grafik-visual-studio/widgets) | [Technisch abgeglichen](/en/projects/grafik-visual-studio/widgets) | [Technisch abgeglichen](/fr/projects/grafik-visual-studio/widgets) |
| [projects/grafik-visual-studio/zeichnen.md](/projects/grafik-visual-studio/zeichnen) | [Inhaltlich geprüft](/en/projects/grafik-visual-studio/zeichnen) | [Inhaltlich geprüft](/fr/projects/grafik-visual-studio/zeichnen) |
| [projects/hadash/ansicht-exportieren.md](/projects/hadash/ansicht-exportieren) | [Inhaltlich geprüft](/en/projects/hadash/export-view) | [Inhaltlich geprüft](/fr/projects/hadash/export-view) |
| [projects/hadash/backups-und-json.md](/projects/hadash/backups-und-json) | [Inhaltlich geprüft](/en/projects/hadash/backups-and-json) | [Inhaltlich geprüft](/fr/projects/hadash/backups-and-json) |
| [projects/hadash/dashboard-einlesen.md](/projects/hadash/dashboard-einlesen) | [Inhaltlich geprüft](/en/projects/hadash/import-dashboard) | [Inhaltlich geprüft](/fr/projects/hadash/import-dashboard) |
| [projects/hadash/erste-schritte.md](/projects/hadash/erste-schritte) | [Inhaltlich geprüft](/en/projects/hadash/getting-started) | [Inhaltlich geprüft](/fr/projects/hadash/getting-started) |
| [projects/hadash/index.md](/projects/hadash/) | [Inhaltlich geprüft](/en/projects/hadash/) | [Inhaltlich geprüft](/fr/projects/hadash/) |
| [projects/hadash/portable-nutzung.md](/projects/hadash/portable-nutzung) | [Inhaltlich geprüft](/en/projects/hadash/portable-usage) | [Inhaltlich geprüft](/fr/projects/hadash/portable-usage) |
| [projects/heizoel-to-mqtt/beispiele.md](/projects/heizoel-to-mqtt/beispiele) | [Inhaltlich geprüft](/en/projects/heizoel-to-mqtt/examples) | [Inhaltlich geprüft](/fr/projects/heizoel-to-mqtt/examples) |
| [projects/heizoel-to-mqtt/entitaeten.md](/projects/heizoel-to-mqtt/entitaeten) | [Inhaltlich geprüft](/en/projects/heizoel-to-mqtt/entities) | [Inhaltlich geprüft](/fr/projects/heizoel-to-mqtt/entities) |
| [projects/heizoel-to-mqtt/index.md](/projects/heizoel-to-mqtt/) | [Inhaltlich geprüft](/en/projects/heizoel-to-mqtt/) | [Inhaltlich geprüft](/fr/projects/heizoel-to-mqtt/) |
| [projects/heizoel-to-mqtt/installation.md](/projects/heizoel-to-mqtt/installation) | [Inhaltlich geprüft](/en/projects/heizoel-to-mqtt/installation) | [Inhaltlich geprüft](/fr/projects/heizoel-to-mqtt/installation) |
| [projects/heizoel-to-mqtt/konfiguration.md](/projects/heizoel-to-mqtt/konfiguration) | [Inhaltlich geprüft](/en/projects/heizoel-to-mqtt/configuration) | [Inhaltlich geprüft](/fr/projects/heizoel-to-mqtt/configuration) |
| [projects/index.md](/projects/) | [Inhaltlich geprüft](/en/projects/) | [Inhaltlich geprüft](/fr/projects/) |
| [projects/logic-studio/index.md](/projects/logic-studio/) | [Technisch abgeglichen](/en/projects/logic-studio/) | [Technisch abgeglichen](/fr/projects/logic-studio/) |
| [projects/logic-studio/user-guide.md](/projects/logic-studio/user-guide) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide) |
| [projects/logic-studio/user-guide/blocks-a.md](/projects/logic-studio/user-guide/blocks-a) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/blocks-a) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/blocks-a) |
| [projects/logic-studio/user-guide/blocks-js.md](/projects/logic-studio/user-guide/blocks-js) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/blocks-js) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/blocks-js) |
| [projects/logic-studio/user-guide/feedback.md](/projects/logic-studio/user-guide/feedback) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/feedback) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/feedback) |
| [projects/logic-studio/user-guide/function-plan.md](/projects/logic-studio/user-guide/function-plan) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/function-plan) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/function-plan) |
| [projects/logic-studio/user-guide/ha-yaml.md](/projects/logic-studio/user-guide/ha-yaml) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/ha-yaml) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/ha-yaml) |
| [projects/logic-studio/user-guide/javascript.md](/projects/logic-studio/user-guide/javascript) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/javascript) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/javascript) |
| [projects/logic-studio/user-guide/rules.md](/projects/logic-studio/user-guide/rules) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/rules) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/rules) |
| [projects/logic-studio/user-guide/typescript.md](/projects/logic-studio/user-guide/typescript) | [Inhaltlich geprüft](/en/projects/logic-studio/user-guide/typescript) | [Inhaltlich geprüft](/fr/projects/logic-studio/user-guide/typescript) |
| [projects/mqtt-client/index.md](/projects/mqtt-client/) | [Inhaltlich geprüft](/en/projects/mqtt-client/) | [Inhaltlich geprüft](/fr/projects/mqtt-client/) |
| [projects/mqtt-client/iobroker-roles.md](/projects/mqtt-client/iobroker-roles) | [Inhaltlich geprüft](/en/projects/mqtt-client/iobroker-roles) | [Inhaltlich geprüft](/fr/projects/mqtt-client/iobroker-roles) |
| [projects/parcel-to-mqtt/beispiele.md](/projects/parcel-to-mqtt/beispiele) | [Inhaltlich geprüft](/en/projects/parcel-to-mqtt/examples) | [Inhaltlich geprüft](/fr/projects/parcel-to-mqtt/examples) |
| [projects/parcel-to-mqtt/entitaeten.md](/projects/parcel-to-mqtt/entitaeten) | [Inhaltlich geprüft](/en/projects/parcel-to-mqtt/entities) | [Inhaltlich geprüft](/fr/projects/parcel-to-mqtt/entities) |
| [projects/parcel-to-mqtt/index.md](/projects/parcel-to-mqtt/) | [Inhaltlich geprüft](/en/projects/parcel-to-mqtt/) | [Inhaltlich geprüft](/fr/projects/parcel-to-mqtt/) |
| [projects/parcel-to-mqtt/installation.md](/projects/parcel-to-mqtt/installation) | [Inhaltlich geprüft](/en/projects/parcel-to-mqtt/installation) | [Inhaltlich geprüft](/fr/projects/parcel-to-mqtt/installation) |
| [projects/parcel-to-mqtt/konfiguration.md](/projects/parcel-to-mqtt/konfiguration) | [Inhaltlich geprüft](/en/projects/parcel-to-mqtt/configuration) | [Inhaltlich geprüft](/fr/projects/parcel-to-mqtt/configuration) |
| [projects/sidebar-colors/index.md](/projects/sidebar-colors/) | [Inhaltlich geprüft](/en/projects/sidebar-colors/) | [Inhaltlich geprüft](/fr/projects/sidebar-colors/) |
| [projects/sidebar-manager/index.md](/projects/sidebar-manager/) | [Inhaltlich geprüft](/en/projects/sidebar-manager/) | [Inhaltlich geprüft](/fr/projects/sidebar-manager/) |
| [projects/uix/broker/broker.md](/projects/uix/broker/broker) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/broker) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/broker) |
| [projects/uix/broker/directives.md](/projects/uix/broker/directives) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/directives) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/directives) |
| [projects/uix/broker/examples.md](/projects/uix/broker/examples) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/examples) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/examples) |
| [projects/uix/broker/index.md](/projects/uix/broker/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/) |
| [projects/uix/broker/interaction-anchors.md](/projects/uix/broker/interaction-anchors) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/interaction-anchors) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/interaction-anchors) |
| [projects/uix/broker/realms.md](/projects/uix/broker/realms) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/realms) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/realms) |
| [projects/uix/broker/rules.md](/projects/uix/broker/rules) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/broker/rules) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/broker/rules) |
| [projects/uix/concepts/application.md](/projects/uix/concepts/application) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/concepts/application) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/concepts/application) |
| [projects/uix/concepts/context.md](/projects/uix/concepts/context) | [Inhaltlich geprüft · Prüfhinweise](/en/projects/uix/concepts/context) | [Inhaltlich geprüft](/fr/projects/uix/concepts/context) |
| [projects/uix/concepts/dom.md](/projects/uix/concepts/dom) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/concepts/dom) | [Inhaltlich geprüft](/fr/projects/uix/concepts/dom) |
| [projects/uix/concepts/index.md](/projects/uix/concepts/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/concepts/) | [Inhaltlich geprüft](/fr/projects/uix/concepts/) |
| [projects/uix/contributing.md](/projects/uix/contributing) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/contributing) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/contributing) |
| [projects/uix/debugging/cache.md](/projects/uix/debugging/cache) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/debugging/cache) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/debugging/cache) |
| [projects/uix/debugging/cards.md](/projects/uix/debugging/cards) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/debugging/cards) | [Inhaltlich geprüft](/fr/projects/uix/debugging/cards) |
| [projects/uix/debugging/index.md](/projects/uix/debugging/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/debugging/) | [Inhaltlich geprüft](/fr/projects/uix/debugging/) |
| [projects/uix/debugging/templates.md](/projects/uix/debugging/templates) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/debugging/templates) | [Inhaltlich geprüft](/fr/projects/uix/debugging/templates) |
| [projects/uix/developers/cards.md](/projects/uix/developers/cards) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/developers/cards) | [Inhaltlich geprüft](/fr/projects/uix/developers/cards) |
| [projects/uix/developers/index.md](/projects/uix/developers/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/developers/) | [Inhaltlich geprüft](/fr/projects/uix/developers/) |
| [projects/uix/developers/themes.md](/projects/uix/developers/themes) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/developers/themes) | [Inhaltlich geprüft](/fr/projects/uix/developers/themes) |
| [projects/uix/extras/always-patch-ha-card.md](/projects/uix/extras/always-patch-ha-card) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/always-patch-ha-card) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/always-patch-ha-card) |
| [projects/uix/extras/custom-sidebar-panels.md](/projects/uix/extras/custom-sidebar-panels) | [Inhaltlich geprüft · Prüfhinweise](/en/projects/uix/extras/custom-sidebar-panels) | [Inhaltlich geprüft](/fr/projects/uix/extras/custom-sidebar-panels) |
| [projects/uix/extras/dialog-styling-delay.md](/projects/uix/extras/dialog-styling-delay) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/dialog-styling-delay) | [Inhaltlich geprüft](/fr/projects/uix/extras/dialog-styling-delay) |
| [projects/uix/extras/disable-entity-picture-image-override.md](/projects/uix/extras/disable-entity-picture-image-override) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/disable-entity-picture-image-override) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/disable-entity-picture-image-override) |
| [projects/uix/extras/disable-icon-styling.md](/projects/uix/extras/disable-icon-styling) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/disable-icon-styling) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/disable-icon-styling) |
| [projects/uix/extras/frontend-states-throttling.md](/projects/uix/extras/frontend-states-throttling) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/frontend-states-throttling) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/frontend-states-throttling) |
| [projects/uix/extras/hash-template-variable-updates.md](/projects/uix/extras/hash-template-variable-updates) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/hash-template-variable-updates) | [Inhaltlich geprüft](/fr/projects/uix/extras/hash-template-variable-updates) |
| [projects/uix/extras/index.md](/projects/uix/extras/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/) |
| [projects/uix/extras/style-custom-panels.md](/projects/uix/extras/style-custom-panels) | [Inhaltlich geprüft](/en/projects/uix/extras/style-custom-panels) | [Inhaltlich geprüft](/fr/projects/uix/extras/style-custom-panels) |
| [projects/uix/extras/style-frame-panels.md](/projects/uix/extras/style-frame-panels) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/style-frame-panels) | [Inhaltlich geprüft](/fr/projects/uix/extras/style-frame-panels) |
| [projects/uix/extras/uix-actions.md](/projects/uix/extras/uix-actions) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/extras/uix-actions) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/extras/uix-actions) |
| [projects/uix/faq.md](/projects/uix/faq) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/faq) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/faq) |
| [projects/uix/forge/forge.md](/projects/uix/forge/forge) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/forge) | [Inhaltlich geprüft](/fr/projects/uix/forge/forge) |
| [projects/uix/forge/foundries.md](/projects/uix/forge/foundries) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/foundries) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/foundries) |
| [projects/uix/forge/index.md](/projects/uix/forge/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/) |
| [projects/uix/forge/sparks/attribute.md](/projects/uix/forge/sparks/attribute) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/attribute) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/sparks/attribute) |
| [projects/uix/forge/sparks/background.md](/projects/uix/forge/sparks/background) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/background) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/background) |
| [projects/uix/forge/sparks/badge.md](/projects/uix/forge/sparks/badge) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/badge) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/badge) |
| [projects/uix/forge/sparks/button.md](/projects/uix/forge/sparks/button) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/button) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/sparks/button) |
| [projects/uix/forge/sparks/event.md](/projects/uix/forge/sparks/event) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/event) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/event) |
| [projects/uix/forge/sparks/form.md](/projects/uix/forge/sparks/form) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/form) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/form) |
| [projects/uix/forge/sparks/grid.md](/projects/uix/forge/sparks/grid) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/grid) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/grid) |
| [projects/uix/forge/sparks/index.md](/projects/uix/forge/sparks/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/sparks/) |
| [projects/uix/forge/sparks/lock.md](/projects/uix/forge/sparks/lock) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/lock) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/lock) |
| [projects/uix/forge/sparks/map.md](/projects/uix/forge/sparks/map) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/map) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/map) |
| [projects/uix/forge/sparks/more-info.md](/projects/uix/forge/sparks/more-info) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/more-info) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/more-info) |
| [projects/uix/forge/sparks/overlay-icon.md](/projects/uix/forge/sparks/overlay-icon) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/overlay-icon) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/overlay-icon) |
| [projects/uix/forge/sparks/search.md](/projects/uix/forge/sparks/search) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/search) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/search) |
| [projects/uix/forge/sparks/state-badge.md](/projects/uix/forge/sparks/state-badge) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/state-badge) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/state-badge) |
| [projects/uix/forge/sparks/theme.md](/projects/uix/forge/sparks/theme) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/theme) | [Inhaltlich geprüft](/fr/projects/uix/forge/sparks/theme) |
| [projects/uix/forge/sparks/tile-icon.md](/projects/uix/forge/sparks/tile-icon) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/tile-icon) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/sparks/tile-icon) |
| [projects/uix/forge/sparks/tooltip.md](/projects/uix/forge/sparks/tooltip) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/forge/sparks/tooltip) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/forge/sparks/tooltip) |
| [projects/uix/guides.md](/projects/uix/guides) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/guides) | [Inhaltlich geprüft](/fr/projects/uix/guides) |
| [projects/uix/index.md](/projects/uix/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/) | [Inhaltlich geprüft](/fr/projects/uix/) |
| [projects/uix/license.md](/projects/uix/license) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/license) | [Inhaltlich geprüft](/fr/projects/uix/license) |
| [projects/uix/quick-start.md](/projects/uix/quick-start) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/quick-start) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/quick-start) |
| [projects/uix/translation-status.md](/projects/uix/translation-status) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/translation-status) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/translation-status) |
| [projects/uix/using/apps.md](/projects/uix/using/apps) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/apps) | [Inhaltlich geprüft](/fr/projects/uix/using/apps) |
| [projects/uix/using/cards.md](/projects/uix/using/cards) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/cards) | [Inhaltlich geprüft · Unterschied geprüft](/fr/projects/uix/using/cards) |
| [projects/uix/using/custom-panels.md](/projects/uix/using/custom-panels) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/custom-panels) | [Inhaltlich geprüft](/fr/projects/uix/using/custom-panels) |
| [projects/uix/using/custom-sidebar-panels.md](/projects/uix/using/custom-sidebar-panels) | [Inhaltlich geprüft](/en/projects/uix/using/custom-sidebar-panels) | [Inhaltlich geprüft](/fr/projects/uix/using/custom-sidebar-panels) |
| [projects/uix/using/entities.md](/projects/uix/using/entities) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/entities) | [Inhaltlich geprüft](/fr/projects/uix/using/entities) |
| [projects/uix/using/icons.md](/projects/uix/using/icons) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/icons) | [Inhaltlich geprüft](/fr/projects/uix/using/icons) |
| [projects/uix/using/images.md](/projects/uix/using/images) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/images) | [Inhaltlich geprüft](/fr/projects/uix/using/images) |
| [projects/uix/using/index.md](/projects/uix/using/) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/) | [Inhaltlich geprüft](/fr/projects/uix/using/) |
| [projects/uix/using/other.md](/projects/uix/using/other) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/other) | [Inhaltlich geprüft](/fr/projects/uix/using/other) |
| [projects/uix/using/section-backgrounds.md](/projects/uix/using/section-backgrounds) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/section-backgrounds) | [Inhaltlich geprüft](/fr/projects/uix/using/section-backgrounds) |
| [projects/uix/using/templates.md](/projects/uix/using/templates) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/templates) | [Inhaltlich geprüft](/fr/projects/uix/using/templates) |
| [projects/uix/using/themes.md](/projects/uix/using/themes) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/themes) | [Inhaltlich geprüft](/fr/projects/uix/using/themes) |
| [projects/uix/using/view-backgrounds.md](/projects/uix/using/view-backgrounds) | [Inhaltlich geprüft · Unterschied geprüft](/en/projects/uix/using/view-backgrounds) | [Inhaltlich geprüft](/fr/projects/uix/using/view-backgrounds) |
| [projects/ultimate-timer/beispiele.md](/projects/ultimate-timer/beispiele) | [Inhaltlich geprüft](/en/projects/ultimate-timer/examples) | [Inhaltlich geprüft](/fr/projects/ultimate-timer/examples) |
| [projects/ultimate-timer/funktionsweise.md](/projects/ultimate-timer/funktionsweise) | [Inhaltlich geprüft](/en/projects/ultimate-timer/how-it-works) | [Inhaltlich geprüft](/fr/projects/ultimate-timer/how-it-works) |
| [projects/ultimate-timer/index.md](/projects/ultimate-timer/) | [Inhaltlich geprüft](/en/projects/ultimate-timer/) | [Inhaltlich geprüft](/fr/projects/ultimate-timer/) |
| [projects/ultimate-timer/installation.md](/projects/ultimate-timer/installation) | [Inhaltlich geprüft](/en/projects/ultimate-timer/installation) | [Inhaltlich geprüft](/fr/projects/ultimate-timer/installation) |
| [projects/ultimate-timer/konfiguration.md](/projects/ultimate-timer/konfiguration) | [Inhaltlich geprüft](/en/projects/ultimate-timer/configuration) | [Inhaltlich geprüft](/fr/projects/ultimate-timer/configuration) |
| [projects/usb-extender/index.md](/projects/usb-extender/) | [Inhalt vorhanden](/en/projects/usb-extender/) | [Inhalt vorhanden](/fr/projects/usb-extender/) |
| [sammlung/calendar-card-pro/beispiele.md](/sammlung/calendar-card-pro/beispiele) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/beispiele) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/beispiele) |
| [sammlung/calendar-card-pro/entwicklung.md](/sammlung/calendar-card-pro/entwicklung) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/entwicklung) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/entwicklung) |
| [sammlung/calendar-card-pro/features.md](/sammlung/calendar-card-pro/features) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/features) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/features) |
| [sammlung/calendar-card-pro/index.md](/sammlung/calendar-card-pro/) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/) |
| [sammlung/calendar-card-pro/installation.md](/sammlung/calendar-card-pro/installation) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/installation) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/installation) |
| [sammlung/calendar-card-pro/konfiguration.md](/sammlung/calendar-card-pro/konfiguration) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/konfiguration) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/konfiguration) |
| [sammlung/calendar-card-pro/lizenz-und-stand.md](/sammlung/calendar-card-pro/lizenz-und-stand) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/lizenz-und-stand) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/lizenz-und-stand) |
| [sammlung/calendar-card-pro/nutzung.md](/sammlung/calendar-card-pro/nutzung) | [Inhaltlich geprüft](/en/collection/calendar-card-pro/nutzung) | [Inhaltlich geprüft](/fr/collection/calendar-card-pro/nutzung) |
| [sammlung/dashboard-layout-card-v2/index.md](/sammlung/dashboard-layout-card-v2/) | [Inhaltlich geprüft](/en/collection/dashboard-layout-card-v2/) | [Inhaltlich geprüft](/fr/collection/dashboard-layout-card-v2/) |
| [sammlung/flex-table-card/aktionen.md](/sammlung/flex-table-card/aktionen) | [Inhaltlich geprüft](/en/collection/flex-table-card/aktionen) | [Inhaltlich geprüft](/fr/collection/flex-table-card/aktionen) |
| [sammlung/flex-table-card/beispiele-aus-forum.md](/sammlung/flex-table-card/beispiele-aus-forum) | [Inhaltlich geprüft](/en/collection/flex-table-card/beispiele-aus-forum) | [Inhaltlich geprüft](/fr/collection/flex-table-card/beispiele-aus-forum) |
| [sammlung/flex-table-card/css.md](/sammlung/flex-table-card/css) | [Inhaltlich geprüft](/en/collection/flex-table-card/css) | [Inhaltlich geprüft](/fr/collection/flex-table-card/css) |
| [sammlung/flex-table-card/datenquellen.md](/sammlung/flex-table-card/datenquellen) | [Inhaltlich geprüft](/en/collection/flex-table-card/datenquellen) | [Inhaltlich geprüft](/fr/collection/flex-table-card/datenquellen) |
| [sammlung/flex-table-card/externe-daten.md](/sammlung/flex-table-card/externe-daten) | [Inhaltlich geprüft](/en/collection/flex-table-card/externe-daten) | [Inhaltlich geprüft](/fr/collection/flex-table-card/externe-daten) |
| [sammlung/flex-table-card/formatierung.md](/sammlung/flex-table-card/formatierung) | [Inhaltlich geprüft](/en/collection/flex-table-card/formatierung) | [Inhaltlich geprüft](/fr/collection/flex-table-card/formatierung) |
| [sammlung/flex-table-card/grundlagen.md](/sammlung/flex-table-card/grundlagen) | [Inhaltlich geprüft](/en/collection/flex-table-card/grundlagen) | [Inhaltlich geprüft](/fr/collection/flex-table-card/grundlagen) |
| [sammlung/flex-table-card/header-footer.md](/sammlung/flex-table-card/header-footer) | [Inhaltlich geprüft](/en/collection/flex-table-card/header-footer) | [Inhaltlich geprüft](/fr/collection/flex-table-card/header-footer) |
| [sammlung/flex-table-card/index.md](/sammlung/flex-table-card/) | [Inhaltlich geprüft](/en/collection/flex-table-card/) | [Inhaltlich geprüft](/fr/collection/flex-table-card/) |
| [sammlung/flex-table-card/installation.md](/sammlung/flex-table-card/installation) | [Inhaltlich geprüft](/en/collection/flex-table-card/installation) | [Inhaltlich geprüft](/fr/collection/flex-table-card/installation) |
| [sammlung/flex-table-card/paketliste.md](/sammlung/flex-table-card/paketliste) | [Inhaltlich geprüft](/en/collection/flex-table-card/paketliste) | [Inhaltlich geprüft](/fr/collection/flex-table-card/paketliste) |
| [sammlung/flex-table-card/referenz.md](/sammlung/flex-table-card/referenz) | [Inhaltlich geprüft](/en/collection/flex-table-card/referenz) | [Inhaltlich geprüft](/fr/collection/flex-table-card/referenz) |
| [sammlung/flex-table-card/sortierung.md](/sammlung/flex-table-card/sortierung) | [Inhaltlich geprüft](/en/collection/flex-table-card/sortierung) | [Inhaltlich geprüft](/fr/collection/flex-table-card/sortierung) |
| [sammlung/frosted-glass-manager/index.md](/sammlung/frosted-glass-manager/) | [Inhaltlich geprüft](/en/collection/frosted-glass-manager/) | [Inhaltlich geprüft](/fr/collection/frosted-glass-manager/) |
| [sammlung/frosted-glass-theme/index.md](/sammlung/frosted-glass-theme/) | [Inhaltlich geprüft](/en/collection/frosted-glass-theme/) | [Inhaltlich geprüft](/fr/collection/frosted-glass-theme/) |
| [sammlung/ha-2026-11-kompatibilitaet.md](/sammlung/ha-2026-11-kompatibilitaet) | [Inhaltlich geprüft](/en/collection/ha-2026-11-compatibility) | [Inhaltlich geprüft](/fr/collection/ha-2026-11-compatibility) |
| [sammlung/ha-apps.md](/sammlung/ha-apps) | [Inhaltlich geprüft](/en/collection/ha-apps) | [Inhaltlich geprüft](/fr/collection/ha-apps) |
| [sammlung/ha-automation-exporter/index.md](/sammlung/ha-automation-exporter/) | [Inhaltlich geprüft](/en/collection/ha-automation-exporter/) | [Inhaltlich geprüft](/fr/collection/ha-automation-exporter/) |
| [sammlung/ha-blueprints.md](/sammlung/ha-blueprints) | [Inhaltlich geprüft](/en/collection/ha-blueprints) | [Inhaltlich geprüft](/fr/collection/ha-blueprints) |
| [sammlung/ha-cards.md](/sammlung/ha-cards) | [Inhaltlich geprüft](/en/collection/ha-cards) | [Inhaltlich geprüft](/fr/collection/ha-cards) |
| [sammlung/ha-dashboard.md](/sammlung/ha-dashboard) | [Inhaltlich geprüft](/en/collection/ha-dashboard) | [Inhaltlich geprüft](/fr/collection/ha-dashboard) |
| [sammlung/ha-empfehlungen.md](/sammlung/ha-empfehlungen) | [Inhaltlich geprüft](/en/collection/ha-recommendations) | [Inhaltlich geprüft](/fr/collection/ha-recommendations) |
| [sammlung/ha-integrationen.md](/sammlung/ha-integrationen) | [Inhaltlich geprüft](/en/collection/ha-integrations) | [Inhaltlich geprüft](/fr/collection/ha-integrations) |
| [sammlung/ha-tools.md](/sammlung/ha-tools) | [Inhaltlich geprüft](/en/collection/ha-tools) | [Inhaltlich geprüft](/fr/collection/ha-tools) |
| [sammlung/hacs-dokus.md](/sammlung/hacs-dokus) | [Inhaltlich geprüft](/en/collection/hacs-docs) | [Inhaltlich geprüft](/fr/collection/hacs-docs) |
| [sammlung/index.md](/sammlung/) | [Inhaltlich geprüft](/en/collection/) | [Inhaltlich geprüft](/fr/collection/) |
| [sammlung/mushroom/beispiele.md](/sammlung/mushroom/beispiele) | [Inhaltlich geprüft](/en/collection/mushroom/beispiele) | [Inhaltlich geprüft](/fr/collection/mushroom/beispiele) |
| [sammlung/mushroom/entwicklung.md](/sammlung/mushroom/entwicklung) | [Inhaltlich geprüft](/en/collection/mushroom/entwicklung) | [Inhaltlich geprüft](/fr/collection/mushroom/entwicklung) |
| [sammlung/mushroom/fehlersuche.md](/sammlung/mushroom/fehlersuche) | [Inhaltlich geprüft](/en/collection/mushroom/fehlersuche) | [Inhaltlich geprüft](/fr/collection/mushroom/fehlersuche) |
| [sammlung/mushroom/index.md](/sammlung/mushroom/) | [Inhaltlich geprüft](/en/collection/mushroom/) | [Inhaltlich geprüft](/fr/collection/mushroom/) |
| [sammlung/mushroom/installation.md](/sammlung/mushroom/installation) | [Inhaltlich geprüft](/en/collection/mushroom/installation) | [Inhaltlich geprüft](/fr/collection/mushroom/installation) |
| [sammlung/mushroom/karten.md](/sammlung/mushroom/karten) | [Inhaltlich geprüft](/en/collection/mushroom/karten) | [Inhaltlich geprüft](/fr/collection/mushroom/karten) |
| [sammlung/mushroom/lizenz-und-stand.md](/sammlung/mushroom/lizenz-und-stand) | [Inhaltlich geprüft](/en/collection/mushroom/lizenz-und-stand) | [Inhaltlich geprüft](/fr/collection/mushroom/lizenz-und-stand) |
| [sammlung/mushroom/nutzung.md](/sammlung/mushroom/nutzung) | [Inhaltlich geprüft](/en/collection/mushroom/nutzung) | [Inhaltlich geprüft](/fr/collection/mushroom/nutzung) |
| [sammlung/neomorphix-uix/index.md](/sammlung/neomorphix-uix/) | [Inhaltlich geprüft](/en/collection/neomorphix-uix/) | [Inhaltlich geprüft](/fr/collection/neomorphix-uix/) |
| [sammlung/testsysteme.md](/sammlung/testsysteme) | [Inhaltlich geprüft](/en/collection/test-systems) | [Inhaltlich geprüft](/fr/collection/test-systems) |
| [sammlung/weitere-beispiele.md](/sammlung/weitere-beispiele) | [Inhaltlich geprüft](/en/collection/interesting-examples) | [Inhaltlich geprüft](/fr/collection/interesting-examples) |
| [sammlung/zendure-ha/entitaeten.md](/sammlung/zendure-ha/entitaeten) | [Inhaltlich geprüft](/en/collection/zendure-ha/entitaeten) | [Inhaltlich geprüft](/fr/collection/zendure-ha/entitaeten) |
| [sammlung/zendure-ha/fehlersuche.md](/sammlung/zendure-ha/fehlersuche) | [Inhaltlich geprüft](/en/collection/zendure-ha/fehlersuche) | [Inhaltlich geprüft](/fr/collection/zendure-ha/fehlersuche) |
| [sammlung/zendure-ha/fuse-group.md](/sammlung/zendure-ha/fuse-group) | [Inhaltlich geprüft](/en/collection/zendure-ha/fuse-group) | [Inhaltlich geprüft](/fr/collection/zendure-ha/fuse-group) |
| [sammlung/zendure-ha/index.md](/sammlung/zendure-ha/) | [Inhaltlich geprüft](/en/collection/zendure-ha/) | [Inhaltlich geprüft](/fr/collection/zendure-ha/) |
| [sammlung/zendure-ha/installation.md](/sammlung/zendure-ha/installation) | [Inhaltlich geprüft](/en/collection/zendure-ha/installation) | [Inhaltlich geprüft](/fr/collection/zendure-ha/installation) |
| [sammlung/zendure-ha/lokales-mqtt.md](/sammlung/zendure-ha/lokales-mqtt) | [Inhaltlich geprüft](/en/collection/zendure-ha/lokales-mqtt) | [Inhaltlich geprüft](/fr/collection/zendure-ha/lokales-mqtt) |
| [sammlung/zendure-ha/manager.md](/sammlung/zendure-ha/manager) | [Inhaltlich geprüft](/en/collection/zendure-ha/manager) | [Inhaltlich geprüft](/fr/collection/zendure-ha/manager) |
