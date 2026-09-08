# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor ist das nächste eigenständige ATLAS-Plugin.
Die Idee basiert auf dem bisherigen Windows-Werkzeug zum Aufteilen von
`automations.yaml`, wandert aber direkt in die ATLAS-Plugin-Architektur.

## Ziel

Das Plugin analysiert Home-Assistant-Automationen sicher, exportiert
ausgewählte Einträge und bereitet die weitere Bearbeitung über File Studio vor.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- aktueller installierbarer Plugin-Stand: `0.1.16`

In ATLAS Administration kann direkt die GitHub-URL eingefügt werden. ATLAS
wandelt sie beim Prüfen automatisch in die passende `repository.json`-Adresse
um.

- `/config/automations.yaml` automatisch über den freigegebenen File-Studio-Pfad lesen
- beim Lesen der echten `/config/automations.yaml` zuerst eine Sicherheitskopie
  unter `/config/atlas_backups/automations/<datum-zeit>/automations.yaml`
  anlegen
- fremde `.yaml`- und `.yml`-Dateien per Upload analysieren
- ID, Alias, Beschreibung, Trigger, Conditions und Actions anzeigen
- Service-Aufrufe aus klassischem `service:` und modernem
  `action: domain.service` erkennen
- Analysehinweise für fehlende oder doppelte IDs/Aliasse, fehlende Trigger oder
  Actions und deaktivierte Automationen anzeigen
- nur Automationen mit Hinweisen filtern
- Detail-YAML farbig wie im File Studio darstellen
- Automationsliste auf ungefähr 15 sichtbare Einträge begrenzen und intern
  scrollbar halten
- beteiligte Entitäten, Scripts, Szenen, Helfer und Benachrichtigungsziele sichtbar machen
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

## Einordnung

ATLAS Automation Exporter / Editor ergänzt File Studio: File Studio ist die
sichere Dateioberfläche, der Automation Exporter / Editor ist die fachliche
Analyse- und Exportoberfläche für Automationen.
