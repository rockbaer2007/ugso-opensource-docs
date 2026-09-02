# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor ist das naechste eigenstaendige ATLAS-Plugin.
Die Idee basiert auf dem bisherigen Windows-Werkzeug zum Aufteilen von
`automations.yaml`, wandert aber direkt in die ATLAS-Plugin-Architektur.

## Ziel

Das Plugin soll Home-Assistant-Automationen sicher analysieren, ausgewaehlte
Eintraege exportieren und die weitere Bearbeitung ueber File Studio vorbereiten.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- aktueller installierbarer Plugin-Stand: `0.1.5`

In ATLAS Administration kann direkt die GitHub-URL eingefuegt werden. ATLAS
wandelt sie beim Pruefen automatisch in die passende `repository.json`-Adresse
um.

- `/config/automations.yaml` automatisch ueber den freigegebenen File-Studio-Pfad lesen
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
- beteiligte Entitaeten, Scripts, Szenen, Helfer und Benachrichtigungsziele sichtbar machen
- Export-Ordner als Zielvorgabe festlegen
- ausgewaehlte Automationen als einzelne YAML-Dateien exportieren
- Export-Dateinamen mit Zeitstempel erzeugen: `name_dd_mm_yy-hh_mm_ss.yaml`
- exportierte Automationen in einer Uebersicht anzeigen
- Bearbeitung der exportierten Dateien ueber File Studio vorbereiten
- spaetere Refactoring-Schritte nur mit Backup, Pruefung und Vorschau ausfuehren

## Sicherheitslinie

Die erste Stufe bleibt bewusst konservativ. Das Plugin liest System-YAML oder
hochgeladene YAML-Dateien, analysiert sie und bereitet Downloads vor. Schreibende
Aenderungen an Home-Assistant-Dateien gehoeren erst in eine spaetere Stufe, wenn
Backup, YAML-Pruefung, Diff-Vorschau und Wiederherstellungspfad vorhanden sind.

## Einordnung

ATLAS Automation Exporter / Editor ergaenzt File Studio: File Studio ist die
sichere Dateioberflaeche, der Automation Exporter / Editor ist die fachliche
Analyse- und Exportoberflaeche fuer Automationen.
