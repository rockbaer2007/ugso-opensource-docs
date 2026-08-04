# Plugin-Dokumentation

ATLAS soll langfristig als erweiterbare Plattform funktionieren. Die Plugin-Dokumentation beschreibt deshalb nicht nur eine einzelne API, sondern den gesamten Weg von der Idee bis zur verteilbaren Erweiterung.

::: warning Planungsstand
Die Plugin-Schnittstellen sind noch in Arbeit. Diese Seite hält den Zielrahmen fest und wird mit den stabilen Verträgen Schritt für Schritt konkretisiert.
:::

## Ziel

Plugins sollen ATLAS erweitern können, ohne Kernpakete oder bestehende Anwendungen direkt zu verändern.

Geplante Einsatzbereiche sind:

- Home-Assistant-nahe Werkzeuge wie Card-Editoren, Diagnoseflächen und Lovelace-Helfer
- eigenständige UGSo-Projekte wie der geplante UGSo Thread Monitor
- wiederverwendbare Provider, Renderer, Themes und Devtools-Erweiterungen
- optionale Community-Erweiterungen mit klaren Verträgen

## Plugin-Lebenszyklus

Ein Plugin soll später einen nachvollziehbaren Lebenszyklus besitzen:

1. Manifest lesen
2. Abhängigkeiten prüfen
3. Plugin registrieren
4. Services, Commands oder UI-Flächen bereitstellen
5. Aktivieren
6. Diagnose- und Statusdaten melden
7. Deaktivieren oder sauber entfernen

Die Dokumentation wird diese Schritte mit Beispielen begleiten, sobald die Verträge stabil sind.

## Aktueller technischer Anker

Der erste technische Schritt ist ein Runtime-Adapter. Ein `RuntimePlugin` kann mit `createRuntimeModuleFromPlugin()` in ein vorhandenes ATLAS Runtime-Modul übersetzt werden. Dadurch nutzt ein Plugin denselben Start-, Diagnose- und Shutdown-Weg wie andere Runtime-Module.

Der Adapter bewahrt Plugin-Metadaten, Extension Points und bereitgestellte Fähigkeiten. Optionale Plugin-Hooks wie `deactivate()` und `dispose()` werden über den Runtime-Shutdown ausgeführt.

Mit `RuntimePluginCatalog` gibt es außerdem eine erste Discovery-Fläche. Sie registriert Plugins nach ID, stellt beschreibende Metadaten bereit und kann Plugins nach Extension Point oder bereitgestellter Capability finden.

`createRuntimePluginAdministrationView()` bereitet die spätere Atlas Administration vor. Die Funktion erzeugt aus Plugin-Katalogdaten eine Verwaltungsansicht mit Statuswerten wie `available`, `active` und `disabled` sowie Aktionen wie `inspect`, `activate`, `deactivate` und `export-package`.

Mit `createRuntimePluginInstallPackage()` gibt es auch den ersten Paketvertrag. Er erzeugt eine Paketbeschreibung mit `atlas-plugin.json`, `README.md` und optionalen Zusatzdateien, die später von der Administration oder einem Archiv-Builder als installierbares Paket ausgegeben werden kann.

`parseRuntimePluginInstallPackage()` liest diese Paketbeschreibung wieder als validierten Descriptor ein. Dabei wird kein Plugin-Code ausgeführt. Die Administration kann importierte Pakete dadurch sicher anzeigen, prüfen, erneut exportieren und wieder aus der lokalen Importliste entfernen, bevor später echte Installations- und Aktivierungswege ergänzt werden. Aktivierungszustände werden in der lokalen Demo-Administration gemerkt, damit Plugin-Listen einen Reload überstehen.

## Erstes Referenz-Plugin

Der Home Assistant Card Editor wird als erstes offizielles ATLAS-Referenz-Plugin behandelt. Er ist damit nicht nur eine Demo, sondern der praktische Nachweis, dass Plugin-Lebenszyklus, Discovery, Administration, Import/Export und Paketbau zusammen funktionieren.

Im Atlas-Code stellt `createHomeAssistantCardEditorPlugin()` diesen Editor als `RuntimePlugin` bereit. Bei der Aktivierung registriert das Plugin einen Service mit Card Targets, Editor-Templates, Bubble-Button-Typen und Fähigkeiten, die später in der Atlas Administration angezeigt werden können.

Zusätzlich erzeugt `createHomeAssistantCardEditorPluginInstallPackage()` ein erstes Installpaket für dieses Referenz-Plugin. Es enthält ein Plugin-Manifest, eine README und ein Beispiel für eine Home-Assistant-Card-Konfiguration.

Als Referenz-Plugin nutzt der Editor folgende Extension Points:

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

Dadurch entsteht ein echtes Beispiel für weitere Plugins: sichtbar in der Atlas Administration, aktivierbar über den Plugin-Katalog und exportierbar als installierbares Paket.

## Geplante Extension-Flächen

Die ersten Extension-Flächen sollen sich an den bestehenden ATLAS-Paketen orientieren:

| Bereich | Geplante Erweiterung |
|---|---|
| Runtime | Services, Lifecycle-Hooks und Aktivierungsregeln |
| Home Assistant | Card-Targets, Entity-Auswahl, Ressourcenprüfung und Exportpfade |
| Renderer | Render-Adapter und Zielflächen |
| Theme | Tokens, Theme-Varianten und visuelle Presets |
| Devtools | Diagnosepanels, Inspektoren und Entwicklungshelfer |

## Struktur einer Plugin-Doku

Eine vollständige Plugin-Doku soll später folgende Kapitel enthalten:

- Plugin-Grundlagen
- Manifest und Metadaten
- Lebenszyklus und Aktivierung
- Service-Registrierung
- Extension APIs
- Home-Assistant-spezifische Erweiterungen
- Beispiele
- Tests
- Versionierung
- Veröffentlichung und HACS-/Paket-Hinweise

## Atlas Administration

Für die Verwaltung von Plugins ist eine eigene Atlas-Administration als Weboberfläche geplant. Sie soll nicht nur installierte Plugins anzeigen, sondern den gesamten Arbeitsfluss rund um Plugins unterstützen.

Der erste sichtbare Schritt ist eine eigene minimale Administration auf Port `4175`, getrennt vom Home-Assistant-Card-Editor auf Port `4174`. Sie liest den Runtime-Plugin-Katalog, zeigt den Home Assistant Card Editor als erstes Referenz-Plugin, stellt Status, Version, Extension Points und Fähigkeiten dar und bietet erste Aktionen wie Prüfen, Aktivieren, Deaktivieren, Paket exportieren und Paket importieren.

Die Administration ist außerdem der zentrale Ort für sensible Verbindungseinstellungen. Home-Assistant-Tokens sollen dort verwaltet und bei `Save settings` lokal gespeichert werden können. Der lokale Admin-Server stellt gespeicherte Verbindungseinstellungen dem Card Editor bereit, damit Reloads und direkte Editor-Aufrufe funktionieren. Der Card Editor erhält den Token nur als Übergabe an die aktive Browser-Sitzung und kann optional nach dieser Übergabe automatisch verbinden. Plugins bekommen später nur freigegebene Kontextdaten wie Home-Assistant-URL, WebSocket-Pfad, erlaubte Ressourcenpfade und deklarierte Fähigkeiten, aber keinen rohen Access Token.

Geplante Funktionen sind:

- installierte Plugins anzeigen, aktivieren und deaktivieren
- Plugin-Status, Versionen, Abhängigkeiten und Diagnosemeldungen prüfen
- neue Plugins über einen Wizard oder eine Vorlage erstellen
- Plugin-Manifeste und Extension Points bearbeiten
- Plugins importieren und exportieren
- installierbare Pakete erzeugen, zum Beispiel ZIP- oder HACS-nahe Bundles
- Demo-Daten, Beispielkonfigurationen und README-Dateien für Pakete mitliefern

Die Administration soll langfristig als zentrale Oberfläche für Plugin-Verwaltung, Paketbau und Qualitätsprüfung dienen.

## Beispielrichtung

Ein einfaches Plugin könnte später etwa:

- ein Manifest bereitstellen
- einen Service registrieren
- einen Home-Assistant-Card-Typ anbieten
- Ressourcenabhängigkeiten beschreiben
- Beispiel-Entities oder Demo-Daten mitliefern

So bleibt eine Erweiterung installierbar, testbar und nachvollziehbar.

## Veröffentlichungsregeln

Für veröffentlichbare Plugins sind geplant:

- eindeutige Paket- und Plugin-Namen
- klare Versionsangaben
- dokumentierte Abhängigkeiten
- sichere Demo- oder Fallback-Daten
- nachvollziehbare Build- und Export-Artefakte
- Hinweise für Home Assistant, HACS oder eigenständige ATLAS-Nutzung

## Nächste Schritte

Die nächsten Doku-Schritte sind:

1. Plugin-Verträge im Atlas-Repo stabilisieren
2. den Home Assistant Card Editor als erstes Referenz-Plugin modellieren
3. Manifest- und Lifecycle-Beispiele ergänzen
4. Home-Assistant-spezifische Plugin-Erweiterungen dokumentieren
5. Atlas-Administration für Plugin-Verwaltung und Paketbau beschreiben
6. Publishing-Checkliste ausarbeiten
