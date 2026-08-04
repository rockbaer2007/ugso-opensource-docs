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
2. ein minimales Beispiel-Plugin definieren
3. Manifest- und Lifecycle-Beispiele ergänzen
4. Home-Assistant-spezifische Plugin-Erweiterungen dokumentieren
5. Publishing-Checkliste ausarbeiten
