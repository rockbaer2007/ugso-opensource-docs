---
title: Dashboard-Benutzerverwaltung
description: Benutzer für alle HA-Ansichten oder einzeln per Checkbox zuordnen, mit Sicherung und DE/EN/FR.
---
# Dashboard-Benutzerverwaltung

**Version 0.1.4 · DE / EN / FR · MIT · experimentell**

Eine eigenständige HA-App: Dashboards auswählen, Benutzer als Spalten und Ansichten als Zeilen anzeigen und die Zuordnung per Checkbox bearbeiten. Kein ATLAS erforderlich. Die breite Oberfläche nutzt 90 vw und 90 vh; Namen stehen hochkant, Benutzerspalten sind schmal und bei Bedarf horizontal scrollbar.

## Installation über UGSo HA Apps

Zuerst ein vollständiges HA-Backup erstellen. Unter **Einstellungen → Apps → App-Store → Repositorys** hinzufügen:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Die **Dashboard-Benutzerverwaltung** installieren, starten und über HA Ingress öffnen. Die Oberfläche ist ausschließlich für aktive HA-Administratoren zugänglich. Kein zusätzlicher LAN-Port, kein manuell einzutragender Token. Benötigt Home Assistant mit Supervisor und ein manuell verwaltetes Dashboard. YAML- und automatisch erzeugte Dashboards sind nur lesbar.

Eine vorhandene **lokale App** bleibt beim Hinzufügen des Repositorys unverändert. Lokale und Repository-App besitzen verschiedene Kennungen und getrennte private App-Daten. Vor einem bewussten Quellenwechsel Vollbackup einschließlich der bisherigen App und deren JSON-Sicherungen herunterladen. Die lokale App nicht ungeprüft deinstallieren; nur eine App gleichzeitig zum Bearbeiten verwenden.

## Benutzer zuordnen

1. Dashboard wählen. Alle Ansichten einschließlich Unteransichten werden aufgelistet.
2. Im Spaltenkopf beispielsweise **webuser** auswählen: Der Benutzer wird für alle bearbeitbaren Ansichten angehakt. Abwählen entfernt ihn aus diesen Ansichten.
3. Einzelne Checkboxen pro Ansicht korrigieren. Ein Strich im Spaltenkopf bedeutet teilweise ausgewählt.
4. **Änderungen speichern**. Erst jetzt werden Dashboard-Sicherung und Schreibvorgang ausgeführt. **Auswahl zurücksetzen** verwirft ausschließlich ungespeicherte Änderungen.

**Grünes U = Benutzer, rotes A = Administrator.** Die Rollen selbst werden nicht geändert. Eigene Dashboard-, Ansichts- und Benutzernamen, Karten, Layouts, Pfade und nicht bearbeitete Ansichten bleiben erhalten. Frühere Benutzer-IDs werden nicht stillschweigend gelöscht. Bearbeitete Ansichten erhalten feste Listen; neu angelegte Benutzer werden dort später nicht automatisch ergänzt.

::: warning Sichtbarkeit ist keine Zugriffssperre
Die App steuert die Sichtbarkeit der Ansichts-Tabs. Direkte URLs bleiben erreichbar; das ersetzt keine HA-Zugriffsrechte. Siehe [offizielle HA-Dokumentation](https://www.home-assistant.io/dashboards/views/#visible).
:::

## Automatische Sprache

**Automatisch (Home Assistant)** übernimmt die HA-Oberflächensprache. Ist der umgebende HA-Rahmen nicht lesbar, gilt die bevorzugte Browsersprache. Nicht unterstützte Sprachen verwenden Englisch. Oben lässt sich zusätzlich DE, EN oder FR auswählen; die Präferenz gilt nur für diesen Browser.

Die Übersetzung umfasst Beschriftungen, Hilfen, Dialoge, Status, Datumsanzeigen, Barrierefreiheit und Servermeldungen. Ungespeicherte Checkboxen bleiben beim Sprachwechsel erhalten. Eigene Namen und gespeicherte Dashboard-Daten werden nicht übersetzt. Keine Cloud-Übersetzung oder zusätzlichen Schlüssel erforderlich.

## Sicherungen und Konflikte

Vor jeder Änderung entsteht eine vollständige Dashboard-JSON unter `/data/backups/` im privaten App-Speicher. Über **JSON sichern** herunterladen. Die Dateien enthalten alle Kartenkonfigurationen und müssen vertraulich aufbewahrt werden. App-Updates erhalten diesen Speicher; vor einer Deinstallation herunterladen oder in einem HA-Backup sichern.

Die App vergleicht Dashboard und Benutzerliste mit dem geladenen Stand und prüft nach dem Schreiben das Ergebnis. Zwischenzeitliche Änderungen sperren das Speichern. HA bietet kein atomares Vergleich-und-Speichern: während der kurzen Speicherphase nicht parallel in einem anderen Editor bearbeiten.

Eine Wiederherstellung sichert zuvor erneut und wird gesperrt, wenn das Dashboard nach der betreffenden Änderung weiter bearbeitet wurde. Bei unbestätigtem Speichern nicht blind wiederholen, sondern aktuellen Stand und Sicherung prüfen.

## Lokale ZIP-Installation aktualisieren

Nach Vollbackup die vollständigen neuen Quelldateien nach `/addons/dashboard_user_manager/` kopieren und im HA-Terminal ausführen:

```sh
touch /addons/dashboard_user_manager/config.yaml
ha store reload
ha apps info local_dashboard_user_manager
```

Sobald `version_latest` die neue Version meldet, in HA aktualisieren. `touch` erneuert nur den Zeitstempel und hilft bei älteren ZIPs, deren erhaltene Zeitstempel Supervisor sonst nicht als Änderung erkennt. Nicht deinstallieren. Repository-Apps werden über ihr Repository aktualisiert.

## Prüfstand und Grenzen

0.1.3 wurde vom Nutzer mit Sammel-/Einzelauswahl, Speichern und Neuladen erfolgreich geprüft. 0.1.4 ergänzt offline geprüfte Sprachkataloge, echte Frontend-Skripte in DE/EN/FR sowie API-, Datenerhalt- und Konflikttests. Kein Produktivsystem wurde für die Sprachänderung verändert. Die vollständige HA-Backup-Wiederherstellung der App ist noch offen. Eine nicht konfigurierte Standardübersicht kann `config_not_found` melden; ein vorhandenes manuelles Dashboard auswählen.

- [App-Quellcode und Paket auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/projects-mqtt/)
- [English](/en/projects/dashboard-user-manager/) · [Français](/fr/projects/dashboard-user-manager/)
