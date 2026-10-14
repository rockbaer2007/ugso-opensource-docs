# Entwicklungsstand

## Getestete Hardwarevarianten

| Variante | Testumgebung |
| --- | --- |
| amd64 | Home Assistant in einer virtuellen Maschine unter Proxmox |
| ARM64 | Home Assistant auf einem echten Raspberry Pi 5 mit 8 GB RAM |

Diese Angaben beschreiben die getesteten Installationen; der Umfang und die
noch offenen Prüfungen sind im folgenden Entwicklungsstand dokumentiert.

## Aktueller Stand

**Expert-Bundle-Korrektur in 0.1.297:** Generierte Kartenscripte und HACS-Bundles übernehmen jetzt das strukturierte Expert-Layout statt lediglich eine Entitätsliste anzuzeigen. Home-Assistant-Kartenhelfer erzeugen die enthaltenen Core-/Community-Karten; konfigurierte Entitäten werden ersetzt und laufende Zustandsänderungen weitergegeben, ohne die Karten neu aufzubauen. Bestehende Projekte und ältere Scriptexporte bleiben kompatibel. Die Veröffentlichung als HACS-Repository mit Release-Verteilung bleibt ein separater Schritt.

**Native HA-/HACS-Prüfung vom 14.10.2026:** Pi 5 und Proxmox laufen nach Updates mit aktivierter HA-Sicherung auf ATLAS 0.1.296. Nach der HACS-/Bubble-/Mushroom-Installation auf dem Pi werden unveränderte ATLAS-YAML-Exporte mit Core/Bubble/Mushroom auf beiden Systemen in der echten, ungespeicherten HA-Kartenvorschau ohne Konfigurationsfehler ausgeführt. Eine zusätzliche Mushroom-Jinja-Vorschau auf dem Pi wertet den echten HA-Zustand aus. Originalprojekte und Administrationsexporte sind anschließend bis auf die Exportzeitstempel identisch; alle sechs Plugins bleiben aktiv. Testdashboards wurden nach Bestätigung entfernt. Die Vorschauen prüfen keine vollständige Bundle-Installation, Geräte-Schaltaktionen oder Leistung unter Last.

**Renderer/Themes in 0.1.296:** Fehler- und Wartestatus bleiben im Dunkelmodus rot beziehungsweise gelb; die Expert-Feldliste und Löschknöpfe sind in beiden Themes lesbar. Eine isolierte Chrome-Prüfung mit 36 vorbereiteten Entity-/Button-/Sensor-/Thermostat-/Bubble-/Mushroom-Vorschauen bestätigt DE/EN/FR, Hell/Dunkel/Auto, Neuladen sowie vier Bildschirmgrößen ohne Überlappung oder seitlichen Seitenüberlauf. Feldobjekte und Flächengröße bleiben unverändert. Automatische Systemwechsel wurden simuliert; echte HA/HACS-Ausführung und vielfältige Nutzerprojekte bleiben getrennte A5-Prüfungen.

Die nachgeholten Docker-Prüfungen vom 14.10.2026 bestehen für Standalone und HA-Paket auf Linux amd64: Build, echte Administration-/Editor-Laufzeit, Health-Checks, Container-Neustart und Plugin-Update/-Wiederherstellung mit getrennten Testdaten. Neun Backend-/Origin-Regressionsprüfungen bestehen zusätzlich im Linux-Image. Das ersetzt keine echte Supervisor-/Ingress-, ARM64- oder Browserprüfung; bestehende HA-Installationen wurden nicht verändert.

**A5-Fortsetzung vom 14.10.2026:** 0.1.295 berücksichtigt den im Browser gespeicherten Administrationsstatus auch bei direkten Plugin-Startlinks. Deaktivierte oder noch nicht aktivierte Plugins werden über diesen Weg nicht gestartet. Das ist eine Bedienpräferenz, keine Zugriffssperre für Plugin-Dateien. Isolierte Prüfungen des echten App-Servers bestätigen Installation, abgewiesene Updates, Austausch, Neustart, Deinstallation und Paket-Wiederherstellung; andere Plugin-Einträge und Testdaten bleiben erhalten. Die Testumgebung ersetzt keine echte HA-Installation. A5 bleibt für Renderer/Themes, vielfältige Projekte, native Last und geschlossene Verbindungen offen.

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

A5 ist gestartet: **0.1.293** korrigiert die Reihenfolge von Snapshots und
Live-Ereignissen sowie den Fehlerstatus beim Socket-Wechsel. Eine isolierte
PC-Prüfung mit HA-Mock bestätigt 100 dargestellte Test-Cards, 2.001 Entitäten,
drei Wiederverbindungen, 150 Live-Updates, Theme-Wechsel und Projekt-Roundtrips
in DE/EN/FR. 162 HA-Tests sind bestanden. Diese Messungen sind synthetisch.

Die native A5-Folgeprüfung lädt auf Pi 5 und Proxmox jeweils 100 kompakte und
24 größere Entitäts-Cards ohne Überlappungen. Theme-Wechsel, Neuladen und
DE/EN/FR erhalten die Felder. Auf dem Pi kommen echte Backup-Statuswechsel
live an; auf Proxmox werden zunächst 3.711 Entitäten und 143 Lovelace-Ressourcen
geladen. Der beobachtete VM-CPU-Wert bleibt konstant, eine Wertänderung ist dort
damit nicht nachgewiesen. Vorher wurden lokale verschlüsselte HA-Backups erstellt.
Die ursprünglichen Editor- und Admin-Konfigurationen sind anschließend exakt
wiederhergestellt, abgesehen vom Exportzeitpunkt; alle sechs Plugins bleiben
aktiv. Nach einem vom Benutzer ausgeführten Proxmox-Neustart verbindet sich der
Editor erneut und das Originalprojekt bleibt unverändert.

Getestet wurden vorbereitete Entitäts-Layouts im Desktop-Browser. Vielfältige
Nutzerprojekte, native Backend-Lastmessungen, Wiederverbindung nach geschlossenem Transport und
breitere Plugin-Lebenszyklusprüfungen bleiben in A5 offen. Desktop-Rendering
ist kein Pi-Leistungsbenchmark; native Neustartprüfung und simulierte
Socket-Abbrüche sind getrennte Nachweise.

**0.1.294** behebt die Wiederverbindung nach längeren Netzwerkausfällen: Der
Editor versucht es nach den bisherigen drei Versuchen weiter, mit höchstens
30 Sekunden Abstand. Authentifizierungs- und Protokollfehler stoppen die
automatischen Versuche, bis die Verbindung korrigiert wird. Ein isolierter
Test mit acht Sekunden nicht erreichbarem Endpunkt bestätigt die Erholung
ohne Neuladen und mit unverändertem Projekt. Beim echten LAN-Test wurde das
Pi-Kabel für etwa zwölf Sekunden getrennt. Alle 100 Testfelder blieben erhalten;
anschließend kamen Live-Daten ohne Neuladen wieder an. Die beobachtete
WebSocket-Verbindung blieb verbunden; eine neu aufgebaute native Verbindung
ist damit nicht nachgewiesen. Beide Systeme laufen mit 0.1.294. Der abschließende
Exportvergleich bestätigt unveränderte Admin-Einstellungen, Verschlüsselungsdaten,
aktive Plugin-IDs und Originalprojekte. Nur das bewusst aktualisierte externe
Icon Studio hat eine neue Version. Ein isolierter Docker-Build und /health
bestätigen außerdem die gemeinsame Administration-/Editor-Laufzeit.
Der Nutzer bestätigt außerdem die Funktion in einer macOS-Ventura-VM direkt auf Proxmox, meldet
aber sehr träges Verhalten. Das ist ein Funktionstest mit Leistungseinschränkung;
die Ursache wurde noch nicht gemessen oder geklärt.

Stand **13.10.2026**: Framework **0.2.0-alpha.88**, HA-App **0.1.294**. Die vier
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
Der aktuelle Home-Assistant-App/Add-on-Stand ist `0.1.297`. Administration und
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
