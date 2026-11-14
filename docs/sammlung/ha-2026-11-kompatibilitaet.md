---
title: HA 2026.11 – Kompatibilitätsprüfung
description: Bestätigte Prüfungen, lokale Tests und offene Befunde der UGSo-Erweiterungen unter Home Assistant 2026.11.
---
# HA 2026.11 – Kompatibilitätsprüfung

**Stand: 05.11.2026 · Core 2026.11.0 · Frontend 20261028.4 · Testsystem ARM (Pi 5) (Port 80).**

Die folgende Übersicht unterscheidet Live-Prüfungen, Anwenderbestätigungen und lokale Tests. Sie ist keine pauschale Freigabe aller Funktionen oder Hardwarevarianten. Die ursprüngliche Prüfung änderte keine Softwareversionen; die anschließende Sidebar-Korrektur ist unten gesondert dokumentiert.

## ATLAS und Plugins

| Paket | Ergebnis und Prüfumfang |
| --- | --- |
| ATLAS App **0.1.334**, Card Editor **0.2.0-alpha.115** | Live: Ingress, Hub mit sechs aktiven Plugins, Editor, HA-Verbindung mit 35 Live-Entitäten und vorhandene Projektliste geladen. 431 Tests des HA-Pakets, 74 App-/Frontend-Tests und TypeScript-Prüfung aller elf Workspace-Pakete bestanden. |
| File Studio **0.1.52** | Live: Dateibaum, Editoroberfläche und freigegebene Pfade laden. Vier Pakettests und Katalogprüfung bestanden. Vorhandene Dateien wurden nicht bearbeitet. |
| Automation Exporter / Editor **0.1.28** | Live: Systemautomation nach eigener Sicherung gelesen; keine bestehenden Automationen vorhanden. Neun lokale Tests bestanden. Kein Schreiben in HA-Systemdateien. |
| Terminal **0.1.10** | Oberfläche live geprüft. **Der Anwender bestätigt am 05.11.2026: ATLAS Terminal funktioniert.** Dies ergänzt die zunächst nur geprüfte Oberfläche; keine gesonderte Bestätigung aller SSH-Ziele oder Oh-My-Posh-Themes. |
| Icon Bibliothek **0.1.9** | Live: 7.447 MDI-Icons (7.4.47) laden, Suche reagiert. Zehn Tests und Paketprüfung bestanden. |
| Icon Studio **0.1.17** | Live: Sammlung, SVG-Vorschau und Zeichenoberfläche laden. 15 Tests und Paketprüfung bestanden; bestehende Sammlung nicht verändert. |

Das ATLAS-App-Paket besteht zusätzlich die schreibfreie Prüfung von 523 Paketdateien. Der isolierte Python-Vertragstest der HA-Integration konnte lokal mangels importierbarem Home Assistant nicht ausgeführt werden; Docker war nicht gestartet. Ein vollständiger neuer Projekt-Schreib-/Wiederherstellungs-/HACS-Rundlauf ist nicht Bestandteil dieser Prüfung.

## Weitere HA-Erweiterungen

| Paket | Ergebnis und Grenze |
| --- | --- |
| [Dashboard Layout Card V2 **0.1.181**](/sammlung/dashboard-layout-card-v2/) | Separater Live-Test bestanden: Cards im zweiten Abschnitt hinzufügen/bearbeiten, schwebender Hinzufügen-Button, Kopf-/Fußzeilen und vollständiges Neuladen. |
| [Automation Status Card **0.1.3**](/projects/automation-status-card/) | Live bestanden: Rendern, Ein/Aus mit Zustandsbestätigung, laufender Durchlauf, Trace-Abfrage, normaler Abschluss, Checkboxen, Alle auswählen/abwählen und Neuladen. Bubble-/Mushroom-Einzelvorlagen dargestellt. 21 lokale Tests bestanden. Fehlerfälle und Laufzeitwarnung wurden unter 2026.11 nicht erneut gezielt provoziert. |
| [Sidebar Manager **0.1.9**](/projects/sidebar-manager/) | Auf dem Testsystem ARM (Pi 5) von 0.1.7 auf **0.1.9** aktualisiert. Live bestanden: Text-/Iconfarben der Einträge und Gruppen im nativen Bearbeitungsdialog, Transparenz, Abbrechen, Speichern, Theme-Rücksetzung und vollständiges Neuladen. 72 lokale Tests bestanden. Eigene Testobjekte bereinigt; exportiertes Layout entspricht der ursprünglichen Sicherung. |
| [Sidebar Colors **0.1.1**](/projects/sidebar-colors/) | **0.1.1** korrigiert denselben Zeilenselektor. 27 lokale Tests bestanden, einschließlich DOM-Regressionen für die alten/neuen HA-Elemente und Speichern/Abbrechen. Nicht zusätzlich parallel auf dem Testsystem ARM (Pi 5) installiert. |
| [Dashboard-Benutzerverwaltung **0.1.11**](/projects/dashboard-user-manager/) | Live: 19 Ansichten und vier Benutzer geladen, keine Änderungen gespeichert. **Offen: zusätzlicher Ladehinweis für das alte `lovelace`-Dashboard.** Ursache nicht abschließend geklärt. 33 Python- und 19 Node-Tests der App bestanden. |
| [HA Grafik Visual Studio **0.1.296**](/projects/grafik-visual-studio/) | 109 Python- und 388 Node-Tests bestanden. Kein eigener Live-Test auf dem Testsystem ARM (Pi 5); App dort nicht installiert. |
| [Blocks for HA **0.1.66**](/projects/blocks-for-ha/) | Zehn Python- und 172 Node-Tests bestanden; sieben optionale Tests übersprungen. Kein Live-Test auf dem Testsystem ARM (Pi 5). |
| [MQTT-Client **0.1.17**](/projects/mqtt-client/) | 36 Python-Tests bestanden; zwei Tests mit separatem MQTT-Broker übersprungen. Keine neue Live-Prüfung gegen einen externen Broker. |
| [CallMeBot Whatsapp **0.1.6**](/projects/callmebot/) / [Signal **0.1.2**](/projects/callmebot-signal/) | 17/18 Python-Tests und jeweils drei Request-ID-Tests bestanden. Keine Nachrichten an echte Empfänger gesendet. |
| Tabbed Card V2 / Editor **0.1.7**, HA-Integration **0.1.3** | JavaScript-/Python-Syntax geprüft; keine Live-Freigabe der nicht installierten Erweiterung. |
| [FRITZ!Box to MQTT **0.1.41**](/projects/fritzbox-to-mqtt/) / [Heizöl to MQTT **0.1.15**](/projects/heizoel-to-mqtt/) | Python-Syntax geprüft; Geräte, Datenquelle und MQTT Discovery nicht live getestet. |
| Materialdesign-Widgetpaket / [Ultimate Timer Blueprint](/projects/ultimate-timer/) | Im Bestand erfasst; keine neue vollständige Live-Funktionsprüfung. |

## Bekannte Befunde und nächste Prüfungen

**Behoben in Sidebar Manager 0.1.9 und Sidebar Colors 0.1.1:** Die Farbanwendung unterstützt jetzt das alte `ha-md-list-item` und das neue `ha-list-item-button`. Manager auf dem Testsystem ARM (Pi 5) live geprüft: Text-/Iconfarben der Einträge und Gruppen, Transparenz, Abbrechen, Speichern, Theme-Rücksetzung und vollständiges Neuladen. 72 Manager- und 27 Colors-Tests bestehen. Colors wurde separat lokal geprüft, nicht parallel auf dem Testsystem ARM (Pi 5) geladen. Keine Migration der gespeicherten Farbeinstellungen nötig.

Der `lovelace`-Ladehinweis der Benutzerverwaltung ist separat zu untersuchen. Ein fehlgeschlagenes Lesen darf weiterhin nicht als leeres Dashboard gelten. Der Hinweis ist noch nicht eindeutig als durch 2026.11 verursachte Regression eingeordnet.

Für nicht installierte Apps und bisher nicht ausgeführte Schreib-, Restore-, Geräte- oder Brokerabläufe bleiben ergänzende Live-Tests nötig. Fremdprojekte wie UIX, Calendar Card Pro, Zendure und Frosted Glass wurden hier nicht vollständig auditiert.

## Sicherung und Bereinigung

Vor der Prüfung wurde ein frisches Vollbackup angelegt. Die eigene Testautomation führte nur eine Verzögerung aus, ohne automatische Auslöser oder Geräteaktionen. Testautomation und Testdashboard sind entfernt; vorhandene Einstellungen, Projekte, Plugins und „Test für APP“ blieben erhalten. Nach ausdrücklich freigegebener Löschung der ältesten Sicherung bleiben genau drei Vollbackups; App-Update- und PC-Sicherungen sind erhalten.

## Referenzen

- [Offizielle Änderungen in HA 2026.11](https://www.home-assistant.io/blog/2026/11/04/release-202611/)
- [Frontend-Komponenten in 2026.11](https://contributors.home-assistant.io/blog/2026/10/28/frontend-component-updates-2026.11/)
- [Config-entry-Rückgaben: Boolean bleibt für Custom Integrations unterstützt](https://contributors.home-assistant.io/blog/2026/10/23/config-entry-methods-return-none/)
- [Originaler Anzeigeeditor 20261028.4](https://github.com/home-assistant/frontend/blob/20261028.4/src/components/ha-items-display-editor.ts)
