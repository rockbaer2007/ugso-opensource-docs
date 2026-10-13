# Entwicklungsstand

## Getestete Hardwarevarianten

| Variante | Testumgebung |
| --- | --- |
| amd64 | Home Assistant in einer virtuellen Maschine unter Proxmox |
| ARM64 | Home Assistant auf einem echten Raspberry Pi 5 mit 8 GB RAM |

Diese Angaben beschreiben die getesteten Installationen; der Umfang und die
noch offenen Prüfungen sind im folgenden Entwicklungsstand dokumentiert.

## Aktueller Stand

**A2 und A3 sind abgeschlossen (13.10.2026).** Der Benutzer hat die aktuellen
ARM64-/Mobilprüfungen als ausreichend akzeptiert. Echte iOS-/Safari-Geräte wurden
nicht getestet; Chrome-Simulatoren sind separat dokumentiert. Der Card Editor
bleibt ausschließlich im Expert-Workflow. Simple-Modus und Umschalter werden
nicht wieder eingeführt; unterstützte ältere Projektimporte bleiben erhalten.

0.1.290 verkürzt die Tablet-Card-Liste auf ein scrollbares Fenster mit zwei
Cards nebeneinander und ordnet die zugehörigen Aktionsbuttons in zwei Spalten an.

0.1.291 klappt „Raster & Zoom“ mobil standardmäßig ein und stellt die
Titelbedienung auf Tablets in eine Reihe; auf Smartphones stehen beide
Titelbuttons nebeneinander unter dem Feld. Alle Werte bleiben erhalten.

0.1.292 entfernt die verbliebene Startmodus-Auswahl aus HA-Konfiguration und
Administration und übernimmt alte Simple-Einstellungen als Expert.

Stand **13.10.2026**: Framework **0.2.0-alpha.88**, HA-App **0.1.292**. Die vier
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

A2 ist in Emulation geprüft: HA-Images für amd64 und ARM64 sowie ein mobiler
Chromium-Touch-Kontext mit 360×800, 390×844, 844×390 und 768×1024 Pixeln in
DE/EN/FR. 0.1.289 behebt Überläufe in Administration und Editor und passt die
Problembericht-, YAML-Import- und Exportdialoge an schmale Bildschirme an.
Einstellungen, gefüllte Testprojekte und Plugin-Daten bleiben durch Sprachwechsel,
JSON/HACS-Import und Neustart erhalten. Ein x86-Host emuliert ARM64; echte
Raspberry-Pi-Leistung sowie Android/iOS, Touch-Drag/Resize, Bildschirmtastatur
und native Datei-/Download-Dialoge bleiben offen. Die reale HA-Installation
wurde für diese isolierten Prüfungen nicht verändert.

Der native A2-Test auf einem **Raspberry Pi 5 / rpi5-64** ist ebenfalls
bestanden: HA OS 18.3, ATLAS 0.1.289, `aarch64` und Node `arm64`. Alle sechs
Plugins öffnen über Ingress; Terminal, File-Studio-Pfade und MDI-Katalog
funktionieren. Vor dem ATLAS-Neustart wurde ein lokales verschlüsseltes
HA-Backup erstellt. Danach stimmen Administrationseinstellungen,
Plugin-Metadaten und vollständiger Editor-Export weiterhin überein, abgesehen
vom Exportzeitpunkt. Der Editor verbindet sich mit 27 echten Entitäten.
Der vorhandene Arbeitsbereich war leer. Desktop-Chrome-Ansichten mit 390×844
und 844×390 passen über den echten Pi-Ingress ohne Seitenüberlauf. Physische
Mobilbrowser, größere gefüllte Projekte und Last-/Leistungsmessungen sind
damit nicht geprüft; ein ARM64-Supervisor-Update wurde hier nicht durchgeführt.

Ergänzend bestätigt der Benutzer auf einem **echten Android-Tablet**: Hub und
Administration funktionieren hoch und quer sowie in DE/EN/FR. Nach dem Wechsel
der HA-URL von `homeassistant.local:80` zur erreichbaren IP-Adresse funktioniert
auch die Verbindung; YAML-Dialog und „Problem melden“ wurden als OK gemeldet.
Dies ist eine Benutzerbestätigung, kein automatisierter Gerätetest.
[Verbindungshinweis für Mobilgeräte](./homeassistant#verbindung-auf-tablet-und-smartphone).
Touch-Drag/Resize, Bildschirmtastatur, native Datei-/Download-Dialoge und iOS
wurden damit nicht unabhängig auf allen Geräten geprüft. A2 ist dennoch mit
der Benutzerfreigabe abgeschlossen; diese Grenzen sind keine offenen A2-Aufgaben.

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

Die nächste Priorität ist A5: Produktionsreife mit größeren realen Projekten,
Live-Updates, Wiederverbindung und Plugin-Kompatibilität prüfen.
Der aktuelle Home-Assistant-App/Add-on-Stand ist `0.1.292`. Administration und
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

1. **A5 – Produktionsreife:** Renderer, Theme und Plugin-APIs mit größeren realen Projekten, Live-Updates, Wiederverbindung und Kompatibilität prüfen und ausbauen.
2. **A6 – Französische Doku:** Unvollständige FR-Seiten übersetzen und DE/EN/FR strukturell und fachlich abgleichen.
3. **A7 – Weitere Bereitstellung:** Linux-/systemd-Installer und native ATLAS-Integration in HA/HACS auf derselben Laufzeit vorbereiten.

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
