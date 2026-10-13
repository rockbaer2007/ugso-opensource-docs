# Entwicklungsstand

## Aktueller Stand

Stand **13.10.2026**: Framework **0.2.0-alpha.88**, HA-App **0.1.288**. Die vier
vereinbarten Stabilisierungspunkte sind abgeschlossen. Die Abschlussprüfung
umfasst 870 Workspace-Tests, fünf ergänzende Tests, alle Typprüfungen und Builds
sowie 15 isolierte Browser-Prüfpunkte in DE/EN/FR. Ältere Admin-Einstellungen,
Repository-Einträge, Darstellung und aktive Plugin-IDs bleiben bei der geprüften
Migration erhalten; Geheimnisse werden verschlüsselt übernommen.

A1 ist an der echten HA-Installation geprüft: Supervisor-Update von 0.1.287 auf
0.1.288, zusätzlicher Neustart und Ingress für alle sechs installierten Plugins.
Administrationseinstellungen, aktive Plugins und die vollständige
Editor-Konfiguration stimmen vor und nach Update und Neustart überein, abgesehen
vom Exportzeitpunkt. Ein lokales verschlüsseltes HA-Backup wurde vorher erstellt.
0.1.288 korrigiert die Laufzeit-Versionsanzeige in Administration; HA-Optionen
und Plugin-Verträge bleiben unverändert. Der Editor verbindet sich erneut und
lädt echte Entitäten und Lovelace-Ressourcen. Der vorhandene Expert-Arbeitsbereich
war leer; größere gefüllte Projekte bleiben A5. Hardware-Aktionen, Mobilbrowser,
ARM64 und sämtliche plugininternen Projektformate sind damit nicht geprüft.
Nur der Card Editor ist das integrierte ATLAS-Referenzplugin; eigenständige
Plugins werden separat gepflegt.

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
  eingeklappten Fähigkeitslisten und Seitenleisten-URLs pro Plugin; Card
  Editor, Administration und Plugin-Assets laufen über App-/Ingress-fähige
  ATLAS-Routen statt nur über separate Entwicklungsports
- Home Assistant Card Editor mit direktem Expert-Workflow, HACS-nahem Export,
  Problembericht, dreispaltigem Import-/Entitätenbereich und getrennten
  `X`-, `Y`- und Zoom-Reglern für das quadratische Expert-Raster
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

## Aktueller Schwerpunkt

Der aktuelle Entwicklungsschwerpunkt ist:

```text
ATLAS Card Editor, Runtime und Erhalt bestehender Einstellungen und Plugins
```

Die nächste Priorität ist A2: ARM64/Raspberry Pi und Mobilbrowser prüfen.
Der aktuelle Home-Assistant-App/Add-on-Stand ist `0.1.288`. Administration und
Plugin-Hub unterstützen Deutsch, Englisch und Französisch und teilen ihre
gespeicherte Spracheinstellung über die getrennten App-Ports hinweg.

## Bereits vorbereitete Architekturentscheidungen

Zu den vorbereiteten Themen gehören:

- Kernel Contracts
- Service Container
- Dependency Injection
- Service Descriptor
- Event-Verträge
- Referenzimplementierungen

## Nächste Ziele

Offen sind die folgenden ATLAS-Punkte:

1. **A2 – ARM64 und Mobilbrowser:** Raspberry Pi und mobile Bedienung einschließlich Layout, Dialogen und Import/Export prüfen.
2. **A3 – Simple/Expert klären:** Den vorgesehenen sichtbaren Wechsel mit dem bisherigen Expert-Start abgleichen; bestehende Projekte erhalten.
3. **A5 – Produktionsreife:** Renderer, Theme und Plugin-APIs mit größeren realen Projekten, Live-Updates, Wiederverbindung und Kompatibilität prüfen und ausbauen.
4. **A6 – Französische Doku:** Unvollständige FR-Seiten übersetzen und DE/EN/FR strukturell und fachlich abgleichen.
5. **A7 – Weitere Bereitstellung:** Linux-/systemd-Installer und native ATLAS-Integration in HA/HACS auf derselben Laufzeit vorbereiten.

**A1 – Echtes HA prüfen und A4 – Roadmap bereinigen sind erledigt.** Abgeschlossene Funktionen bleiben in
der Historie dokumentiert und sind keine offenen Aufgaben. Eigenständige Plugins
führen ihre Implementierungsaufgaben in ihren eigenen Projekten.
Die verbindliche offene Liste steht in der [ATLAS-Roadmap](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

## Langfristige Perspektive

Nach Abschluss der grundlegenden Runtime soll ATLAS als technische Basis für weitere UGSo-Projekte dienen.

Geplante Folgeprojekte sind:

- **Lovelace UV Card**: eine Home-Assistant-/Lovelace-Card für UV-Index, Schutzstatus, Grenzwerte und visuelle Dashboard-Ausgabe. Als Inspiration ist `filipnet/haos-uv-index` vorgemerkt: relevant sind UV-Index-Sensoren, farbcodierte Risikostufen, WHO-nahe Schutzempfehlungen, Mushroom-kompatible Darstellung und optionale Benachrichtigungs-Automationen. Die Umsetzung soll eine eigene UGSo/ATLAS-Card bleiben.

::: info Hinweis
Die Roadmap kann sich während der Entwicklung ändern. Die Seite beschreibt den aktuellen Planungsstand.
:::
