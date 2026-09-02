# ATLAS Plugins

Diese Rubrik sammelt alles, was nicht den ATLAS-Kern selbst beschreibt, sondern installierbare Erweiterungen: Plugin-Verträge, Repository-Format, Veröffentlichung, Update-Verhalten und einzelne Plugin-Seiten.

::: warning Entwicklungsstand
Die Plugin-Schnittstellen sind noch in Arbeit. Die Seiten dokumentieren den aktuellen ATLAS-Stand und werden mit stabileren Verträgen weiter ausgebaut.
:::

## Einstieg

- [Repository-Format](./repository-format): Struktur einer `repository.json`, Pflichtfelder, ATLAS-Kennung und Beispiel.
- [Home Assistant Card Editor](./homeassistant-card-editor): erstes offizielles ATLAS-Referenz-Plugin.
- [ATLAS File Studio](./file-studio): zweites unabhängiges ATLAS-Plugin für freigegebene Home-Assistant-Dateipfade.
- [Automation Extractor](./automation-extractor): geplantes Plugin zum Analysieren und späteren Aufteilen von Home-Assistant-Automationen.
- [Demo-Repository](./demo-repository): öffentliches Test-Repository für Administration, Hub und Installationsfluss.

## Ziel

ATLAS-Plugins sollen die Plattform erweitern, ohne Kernpakete direkt zu verändern. Dazu gehören Home-Assistant-nahe Werkzeuge, Card-Editoren, Diagnoseflächen, Renderer, Themes, Provider und später auch Community-Erweiterungen.

## Lebenszyklus

Ein Plugin soll nachvollziehbar installiert, geprüft, aktiviert, aktualisiert und entfernt werden können:

1. Manifest lesen
2. Abhängigkeiten prüfen
3. Plugin registrieren
4. Services, Commands oder UI-Flächen bereitstellen
5. Aktivieren
6. Diagnose- und Statusdaten melden
7. Deaktivieren oder sauber entfernen

## Aktueller technischer Anker

Der aktuelle Einstieg ist der Runtime-Adapter. Ein `RuntimePlugin` kann mit `createRuntimeModuleFromPlugin()` in ein ATLAS-Runtime-Modul übersetzt werden. `RuntimePluginCatalog` stellt die Discovery-Fläche bereit, während die Administration Plugins sichtbar macht, Versionen vergleicht und lokale Installationen vorbereitet.

Der Plugin-Hub folgt inzwischen einer klaren Startregel: Wenn keine Plugins installiert sind, verweist er auf die Administration. Bei genau einem aktiven Plugin öffnet ATLAS dieses Plugin direkt. Bei zwei oder mehr aktiven Plugins zeigt ATLAS die Auswahlseite. Geplante oder deaktivierte Plugins dürfen sichtbar sein, werden aber nicht automatisch gestartet.

Atlas Administration kann außerdem Seitenleisten-Einträge für Home Assistant vorbereiten. Der Dialog listet die aktuellen Plugins dynamisch, zeigt Name, URL, Version, Status und Icon-Vorschlag und kopiert einen fertigen `panel_iframe`-Block für die `configuration.yaml`. Alternativ können dieselben Werte für ein Home-Assistant-Dashboard vom Typ `Webseite` genutzt werden.

Der Plugin-Hub öffnet diesen Dialog direkt und zeigt bei startbaren Plugins die direkte Seitenleisten-URL. Für ATLAS File Studio ist das die Plugin-URL unter `/plugin-assets/file-studio/index.html` am ATLAS-App-Port beziehungsweise über die entsprechende Home-Assistant-Ingress-/Webseiten-Adresse.

## Veröffentlichungsregeln

Veröffentlichbare Plugins brauchen eindeutige Namen, klare Versionsangaben, dokumentierte Abhängigkeiten, sichere Demo- oder Fallback-Daten, nachvollziehbare Build-Artefakte und Hinweise für ATLAS, Home Assistant oder HACS-nahe Nutzung.

## Geplante Plugins

Der nächste vorgemerkte Plugin-Kandidat ist der Automation Extractor. Er soll die bisherige Windows-Idee in ATLAS bringen und zuerst lesend arbeiten: Automationen erkennen, Abhängigkeiten anzeigen und sichere Export- oder Refactoring-Schritte vorbereiten.
