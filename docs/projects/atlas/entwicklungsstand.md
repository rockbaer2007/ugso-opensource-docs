# Entwicklungsstand

## Aktueller Stand

Die grundlegende Repository- und Dokumentationsstruktur ist eingerichtet.

Abgeschlossen sind unter anderem:

- Monorepo-Struktur mit `pnpm` Workspaces
- Governance- und Architektur-Dokumente
- Bereinigung der Events- und Contracts-Schicht
- öffentliche Event-Verträge
- Referenzimplementierung `DefaultEventBus`
- Heartbeat- und EventBus-Grundlagen
- Atlas Administration mit Plugin-Verwaltung, Capability-Freigaben,
  Home-Assistant-Verbindung, Add-on-Update-Hinweisen und vorbereitetem
  Seitenleisten-Helfer
- Plugin-Hub mit Startlogik fuer 0, 1 oder mehrere aktive Plugins,
  dynamischen Plugin-URLs, URL- und `panel_iframe`-Kopie sowie standardmäßig
  eingeklappten Fähigkeitslisten pro Plugin
- Home Assistant Card Editor mit Simple-/Expert-Workflow, HACS-nahem Export,
  Problembericht, dreispaltigem Import-/Entitaetenbereich und getrennten
  `X`-, `Y`- und Zoom-Reglern fuer das quadratische Expert-Raster
- Snapshot und Pre-Release-Tag für den Event-Stand
- ATLAS File Studio als zweites Plugin mit `/config`-Standard, optionaler
  `/addons`-Freigabe, YAML-Prüfung, Upload/Download, Backups, Verlauf mit
  Vergleich und Wiederherstellung, Suchfiltern, Mehrfachauswahl,
  Drag-and-drop-Upload, Papierkorb, Favoriten, Dateityp-Icons und
  secret-freiem Problembericht mit GitHub-Issue-Link
- ATLAS Automation Exporter / Editor als eigenständiges GitHub-installierbares
  Plugin mit System-`automations.yaml`, YAML-Upload, Zeitstempel-Export,
  Exportübersicht, File-Studio-Anbindung und Analysehinweisen für fehlende oder
  doppelte IDs/Aliasse, fehlende Trigger/Actions und deaktivierte Automationen;
  Service-Aufrufe werden sowohl aus `service:` als auch aus modernem
  `action: domain.service` erkannt, die Detail-YAML wird farbig dargestellt und
  lange Automationslisten scrollen intern

## Aktueller Sprint

Der aktuelle Entwicklungsschwerpunkt ist:

```text
ATLAS File Studio, Automation Exporter / Editor und Home-Assistant-App/Add-on-Workflow
```

Der Schwerpunkt liegt auf sicheren Home-Assistant-Dateiworkflows,
versionierten Add-on-Veröffentlichungen und nachvollziehbaren Plugin-Updates.
Der aktuelle Home-Assistant-App/Add-on-Stand ist `0.1.126`.

## Bereits vorbereitete Architekturentscheidungen

Zu den vorbereiteten Themen gehören:

- Kernel Contracts
- Service Container
- Dependency Injection
- Service Descriptor
- Event-Verträge
- Referenzimplementierungen

## Nächste Ziele

Geplant sind:

1. Runtime Foundation stabilisieren
2. Service-Lebenszyklen definieren
3. Dependency Injection vervollständigen
4. Diagnose- und Fehlerpfade ausbauen
5. Plugin-Verträge vorbereiten
6. Separate Plugin-Dokumentation für Erstellung, Lebenszyklus, Extension APIs, Beispiele und Veröffentlichung vorbereiten
7. Home-Assistant-Anbindung entwickeln
8. Renderer- und Theme-Schichten erweitern
9. ATLAS File Studio als installierbares Plugin weiter ausbauen, insbesondere spätere echte Home-Assistant-Reload-Aktionen
10. ATLAS Automation Exporter / Editor als weiteres Plugin ausbauen: System-`automations.yaml`, YAML-Upload, Exportuebersicht und File-Studio-Bearbeitung

## Langfristige Perspektive

Nach Abschluss der grundlegenden Runtime soll ATLAS als technische Basis für weitere UGSo-Projekte dienen.

Geplante Folgeprojekte sind:

- **Lovelace UV Card**: eine Home-Assistant-/Lovelace-Card für UV-Index, Schutzstatus, Grenzwerte und visuelle Dashboard-Ausgabe. Als Inspiration ist `filipnet/haos-uv-index` vorgemerkt: relevant sind UV-Index-Sensoren, farbcodierte Risikostufen, WHO-nahe Schutzempfehlungen, Mushroom-kompatible Darstellung und optionale Benachrichtigungs-Automationen. Die Umsetzung soll eine eigene UGSo/ATLAS-Card bleiben.

::: info Hinweis
Die Roadmap kann sich während der Entwicklung ändern. Die Seite beschreibt den aktuellen Planungsstand.
:::
