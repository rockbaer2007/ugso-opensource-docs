# Geprüfte Plugins

**HA 2026.11, 05.11.2026:** Hub und Oberflächen aller sechs Plugins auf dem [Testsystem ARM (Pi 5)](/sammlung/testsysteme#testsystem-arm) geprüft. Card Editor verbindet sich mit HA; File Studio lädt die Pfade, der Automation Exporter liest nach Sicherung, die Icon Bibliothek lädt MDI und Icon Studio die SVG-Oberfläche. **ATLAS Terminal funktioniert laut Anwenderbestätigung.** Dies erweitert die Grundprüfung, ändert jedoch keine experimentellen Produktstatus und ersetzt keine Prüfung sämtlicher Funktionen.

[Prüfumfang, Ergebnisse und offene Punkte](/sammlung/ha-2026-11-kompatibilitaet).

Diese Seite sammelt ATLAS-Plugins, die sichtbar empfohlen oder als neue externe Einreichung beobachtet werden. Geprüfte Plugins wurden mindestens auf Manifest, Start-URL, Icon, offensichtliche Secret-Leaks und unsichere Pfadfreigaben kontrolliert.

::: warning Hinweis
ATLAS befindet sich in Entwicklung. Auch geprüfte Plugins ersetzen keine eigene Prüfung vor dem produktiven Einsatz.
:::

## Geprüfte Plugins

| Icon | Name | Status | Link |
| --- | --- | --- | --- |
| 🧩 | ATLAS Home Assistant Card Editor | geprüft | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/homeassistant-card-editor">Details</a> |
| 🗂️ | ATLAS File Studio | geprüft | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/file-studio">Details</a> |
| 🖥️ | ATLAS Terminal | experimentell | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/terminal">Details</a> |
| ⚙️ | ATLAS Automation Exporter / Editor | experimentell | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/automation-extractor">Details</a> |
| 🎨 | ATLAS Icon Studio | experimentell | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/icon-studio">Details</a> |
| 🔎 | ATLAS Icon Library | experimentell | <a class="atlas-plugin-table-button" href="/projects/atlas-plugins/icon-library">Details</a> |

## Neue/ungeprüfte Plugins

| Icon | Name | Status | Link |
| --- | --- | --- | --- |
| - | Noch keine externen Einreichungen | ungeprüft | - |

## Statuswerte

| Status | Bedeutung |
| --- | --- |
| geprüft | Plugin wurde grundlegend geprüft und passt zum aktuellen ATLAS-Stand. |
| experimentell | Plugin ist nutzbar, aber Funktion oder Vertrag ändern sich noch sichtbar. |
| ungeprüft | Plugin wurde eingereicht oder gefunden, aber noch nicht von ATLAS geprüft. |
| veraltet | Plugin passt nicht mehr zum aktuellen ATLAS-Stand. |
| abgelehnt | Plugin wird wegen technischer, rechtlicher oder Sicherheitsgründe nicht empfohlen. |
