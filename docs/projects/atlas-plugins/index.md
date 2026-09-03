# ATLAS Plugins

Diese Rubrik sammelt alles, was nicht den ATLAS-Kern selbst beschreibt, sondern installierbare Erweiterungen: Plugin-Verträge, Repository-Format, Veröffentlichung, Update-Verhalten und einzelne Plugin-Seiten.

::: warning Entwicklungsstand
Die Plugin-Schnittstellen sind noch in Arbeit. Die Seiten dokumentieren den aktuellen ATLAS-Stand und werden mit stabileren Verträgen weiter ausgebaut.
:::

## Einstieg

- [Repository-Format](./repository-format): Struktur einer `repository.json`, Pflichtfelder, ATLAS-Kennung und Beispiel.
- [Home Assistant Card Editor](./homeassistant-card-editor): erstes offizielles ATLAS-Referenz-Plugin.
- [ATLAS File Studio](./file-studio): zweites unabhängiges ATLAS-Plugin für freigegebene Home-Assistant-Dateipfade.
- [ATLAS Automation Exporter / Editor](./automation-extractor): neues Plugin zum Analysieren, Exportieren und spaeteren Bearbeiten von Home-Assistant-Automationen.
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

Der Plugin-Hub kann außerdem Seitenleisten-Einträge für Home Assistant vorbereiten. Der Dialog listet die aktuellen Plugins dynamisch, zeigt Name, URL, Version, Status und Icon-Vorschlag und kopiert wahlweise nur die URL oder einen fertigen `panel_iframe`-Block für die `configuration.yaml`. Die URL-Kopie ist für Home-Assistant-Dashboards vom Typ `Webseite` gedacht. Lange Fähigkeitslisten und Seitenleisten-URLs bleiben auf Plugin-Karten standardmäßig eingeklappt, damit der Hub auch mit vielen Plugins kompakt bleibt.

Card Editor, Administration und lokale Plugin-Assets werden im Add-on-Betrieb über ATLAS-App-Routen ausgeliefert. Dadurch bleiben Home-Assistant-Ingress-Basispfade in Hub- und Seitenleisten-URLs erhalten und andere Rechner im Netzwerk müssen die separaten Entwicklungsports nicht direkt erreichen.

Für ATLAS File Studio nutzt der Hub die Plugin-URL unter `/plugin-assets/file-studio/index.html` am ATLAS-App-Port beziehungsweise über die entsprechende Home-Assistant-Ingress-/Webseiten-Adresse. Diese URL wird auch dann vorbereitet, wenn ein älterer gespeicherter Plugin-Stand noch keine Start-URL enthält.

Neue lokale Plugins bekommen ebenfalls automatisch eine Start-URL, wenn ihr Plugin-Ordner eine `index.html` enthält und im Manifest kein `entry` gesetzt ist. ATLAS veröffentlicht dann `/plugin-assets/<plugin-ordner>/index.html`, sodass Nutzer direkt zwischen Hub und Home-Assistant-Seitenleiste wählen können.

## Veröffentlichungsregeln

Veröffentlichbare Plugins brauchen eindeutige Namen, klare Versionsangaben, dokumentierte Abhängigkeiten, sichere Demo- oder Fallback-Daten, nachvollziehbare Build-Artefakte und Hinweise für ATLAS, Home Assistant oder HACS-nahe Nutzung.

## Geplante Plugins

Der naechste Plugin-Kandidat ist jetzt als ATLAS Automation Exporter / Editor gestartet. Er bringt die bisherige Windows-Idee in ATLAS: Automationen erkennen, Abhaengigkeiten anzeigen, einzelne YAML-Dateien mit Zeitstempel exportieren und die weitere Bearbeitung ueber File Studio vorbereiten.
