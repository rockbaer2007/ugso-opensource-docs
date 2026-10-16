# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor ist ein eigenständiges, extern gepflegtes ATLAS-Plugin.
Die Idee basiert auf dem bisherigen Windows-Werkzeug zum Aufteilen von
`automations.yaml`, wandert aber direkt in die ATLAS-Plugin-Architektur.

## Ziel

Das Plugin analysiert Home-Assistant-Automationen sicher, exportiert
ausgewählte Einträge und bereitet die weitere Bearbeitung über File Studio vor.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- aktueller installierbarer Plugin-Stand: `0.1.28`
- Benutzeroberfläche auf Deutsch, Englisch und Französisch; die gespeicherte ATLAS-Sprache wird beim Öffnen übernommen.

In ATLAS Administration kann direkt die GitHub-URL eingefügt werden. ATLAS
wandelt sie beim Prüfen automatisch in die passende `repository.json`-Adresse
um.

Seit 0.1.28 zählt die Analyse die tatsächlichen YAML-Einträge von Triggern,
Bedingungen und Aktionen. Abschnittsköpfe und verschachtelte Schritte zählen
nicht als zusätzliche Haupteinträge. Moderne und klassische Schreibweisen
werden unterstützt. Einstellungen und Quellautomationen bleiben unverändert;
beim Laden wird vor der Analyse weiterhin eine Sicherheitskopie angelegt.

- `/config/automations.yaml` automatisch über den freigegebenen File-Studio-Pfad lesen
- beim Laden der echten `/config/automations.yaml` vor der Analyse eine Sicherheitskopie
  unter `/config/atlas_backups/automations/<datum-zeit>/automations.yaml`
  anlegen
- fremde `.yaml`- und `.yml`-Dateien per Upload analysieren
- ID, Alias, Beschreibung, Trigger, Conditions und Actions anzeigen
- Service-Aufrufe aus klassischem `service:` und modernem
  `action: domain.service` erkennen
- einzelne Automationen mit Trigger- oder Action-Fragmenten auf Root-Ebene als
  einen Eintrag behalten, statt daraus falsche Mehrfachkonflikte zu erzeugen
- Zeittrigger beim Export als quoted `HH:MM:SS` erhalten und numerische
  Sekundenwerte wie `25200` wieder als `'07:00:00'` ausgeben
- Analysehinweise für fehlende oder doppelte IDs/Aliasse, fehlende Trigger oder
  Actions und deaktivierte Automationen anzeigen
- doppelte IDs und Aliasse direkt in der Automationsliste als Konflikte
  vormarkieren
- doppelte IDs und Aliasse als Konflikte getrennt von allgemeinen Hinweisen
  anzeigen
- nur Automationen mit Hinweisen filtern
- Detail-YAML farbig wie im File Studio darstellen
- Automationsliste auf ungefähr 15 sichtbare Einträge begrenzen und intern
  scrollbar halten
- beteiligte Entitäten, Scripts, Szenen, Helfer und Benachrichtigungsziele sichtbar machen
- Automationsliste nach Domain, Bereich oder Gerät gruppieren und filtern
- Export-Ordner als Zielvorgabe festlegen
- ausgewählte Automationen in einen Laufordner mit Datum und Uhrzeit
  exportieren
- pro Automation zwei Dateien mit gleichem Namen erzeugen:
  `export-version` mit `id` und `bereinigte-import-version` ohne `id` für den
  Home-Assistant-YAML-Editor
- exportierte Automationen in einer Übersicht anzeigen
- Bearbeitung der exportierten Dateien über File Studio vorbereiten

## Sicherheitslinie

Das Plugin schreibt nicht in Home-Assistant-Systemdateien zurück. Es liest
System-YAML oder hochgeladene YAML-Dateien, legt beim Öffnen der echten
`automations.yaml` eine Sicherheitskopie an, analysiert die Automationen und
exportiert getrennte YAML-Dateien. Manuelle Wiederherstellung und spätere
Bearbeitung laufen über File Studio und die Home-Assistant-YAML-Werkzeuge.

## Sichere Plugin-Wiederherstellung

In **Administration → Plugin-Manager → Automation Exporter / Editor →
Wiederherstellen** eine vorhandene Sicherung auswählen. Version, Richtung und
Kompatibilität in der Vorschau prüfen und erst dann **Sichern und übernehmen**
ausführen. ATLAS sichert dabei auch die aktuell installierte Plugin-Version.
**Abbrechen** lässt die Installation unverändert. Nach einer zwischenzeitlichen
Änderung am Plugin-/Verwaltungsstand muss eine neue Vorschau erstellt werden.

Damit wird das **Plugin-Paket** wiederhergestellt. Quellautomationen, exportierte
Dateien, Editor-Projekte sowie Papierkorb und Historie werden dadurch nicht auf
einen früheren Datenstand zurückgesetzt. Es gibt keinen automatischen Import
nach Home Assistant und kein Zurückschreiben in `automations.yaml`.

::: info Isoliert geprüft am 16.10.2026
Mit ATLAS 0.1.312 wurden echte Pakete **0.1.27 → 0.1.28 → 0.1.27 → 0.1.28**
geprüft, einschließlich Neustart, UI-Vorschau, Abbruch und Übernahme. Eine
veraltete Vorschau wurde nach einer echten Verwaltungsänderung zurückgewiesen.
Vorher wurden Repositories und die vollständigen isolierten Testdaten gesichert.
Quell-YAML, vorhandene Exporte, Projekt, anderes Plugin, Papierkorb und Historie
blieben beim Dateivergleich erhalten. Analyse in DE/EN/FR, bytegleiche
Sicherheitskopien, Exportpaare mit/ohne ID und Öffnen im File Studio bestanden.
Die HA-Version kam von einem lokalen Testendpunkt; das ist kein Test einer echten
HA-Verbindung, eines GitHub-Updates oder einer Datenformat-Migration.
**Pi 5 und Proxmox wurden weder abgefragt noch verändert.** Native Tests bleiben offen.
:::

Sprache und Darstellung werden lokal gespeichert. Geladene Analyse, Auswahl,
Filter, eingegebener Export-Ordner und Exportübersicht gehören zur aktuellen
Sitzung. Nach Neuladen die Quelle erneut laden und den Zielordner bei Bedarf
erneut wählen. Bereits gespeicherte Exportdateien bleiben erhalten und können
im File Studio geöffnet werden.

## Einordnung

ATLAS Automation Exporter / Editor ergänzt File Studio: File Studio ist die
sichere Dateioberfläche, der Automation Exporter / Editor ist die fachliche
Analyse- und Exportoberfläche für Automationen.
