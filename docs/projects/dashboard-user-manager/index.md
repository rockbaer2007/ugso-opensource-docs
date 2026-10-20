---
title: Dashboard-Benutzerverwaltung
description: Benutzer für alle HA-Ansichten oder einzeln per Checkbox zuordnen, mit Sicherung und DE/EN/FR.
---
# Dashboard-Benutzerverwaltung

**Version 0.1.6 · DE / EN / FR · MIT · experimentell**

Eine eigenständige HA-App: Dashboards auswählen, Benutzer als Spalten und Ansichten als Zeilen anzeigen und die Zuordnung per Checkbox bearbeiten. Kein ATLAS erforderlich. Die breite Oberfläche nutzt 90 vw und 90 vh; Namen stehen hochkant, Benutzerspalten sind schmal und bei Bedarf horizontal scrollbar.

![Dashboard-Benutzerverwaltung 0.1.4 auf dem HA-Testsystem .177 mit automatischer deutscher Sprache](/images/dashboard-user-manager/ha-177-de-0.1.4.png)

Echte Aufnahme vom Testsystem .177, 20.10.2026: automatische HA-Sprache, 18 Ansichten und vier Benutzer. Das vorhandene Dashboard wurde für die Aufnahme nicht geändert.

## Installation über UGSo HA Apps

Zuerst ein vollständiges HA-Backup erstellen. Unter **Einstellungen → Apps → App-Store → Repositorys** hinzufügen:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Die **Dashboard-Benutzerverwaltung** installieren, starten und über HA Ingress öffnen. Die Oberfläche ist ausschließlich für aktive HA-Administratoren zugänglich. Kein zusätzlicher LAN-Port, kein manuell einzutragender Token. Benötigt Home Assistant mit Supervisor und ein manuell verwaltetes Dashboard. YAML- und automatisch erzeugte Dashboards sind nur lesbar.

Eine vorhandene **lokale App** bleibt beim Hinzufügen des Repositorys unverändert. Lokale und Repository-App besitzen verschiedene Kennungen und getrennte private App-Daten. Vor einem bewussten Quellenwechsel Vollbackup einschließlich der bisherigen App und deren JSON-Sicherungen herunterladen. Die lokale App nicht ungeprüft deinstallieren; nur eine App gleichzeitig zum Bearbeiten verwenden.

## Dashboards filtern und vorauswählen

Ab 0.1.6 erscheint eine von HA migrierte Übersicht nur einmal: Der Eintrag `lovelace` und sein alter Standardzugang werden zusammengeführt. Eine zuvor über einen der beiden Einträge gespeicherte Vorauswahl bleibt erhalten. Gleichnamige Dashboards mit verschiedenen tatsächlichen Pfaden bleiben getrennt; Titel allein sind kein Dublettenkriterium. Ältere Dashboard-Sicherungen bleiben verwendbar. Grundlage ist die [HA-Zuordnung des Standardzugangs](https://github.com/home-assistant/core/blob/2026.10.2/homeassistant/components/lovelace/websocket.py).

![Dashboard-Vorauswahl 0.1.5 mit Checkboxen auf .177](/images/dashboard-user-manager/selection-177-de-0.1.5.png)

Die Dropdownliste enthält nur erfolgreich geladene Dashboards mit mindestens einer Ansicht. Bestätigte leere Einträge und App-Seiten ohne Ansichten werden ausgeblendet. Ladefehler erscheinen getrennt mit Dashboard-Namen und gelten nicht als leer; über **Neu laden** erneut prüfen. YAML- oder generierte Dashboards mit Ansichten bleiben als **nur lesbar** gekennzeichnet.

**Dashboard-Vorauswahl** öffnet ein Fenster mit einer Checkbox je verfügbarem Dashboard, **Alle auswählen**, **Alle abwählen**, **Abbrechen** und **Vorauswahl übernehmen**. Nur angehakte Einträge erscheinen anschließend im Dropdown. Die Auswahl wird pro Browser und HA-Adresse gespeichert; sie ändert keine Dashboards oder Benutzerzuordnungen. Auch eine leere Auswahl ist erlaubt. Nach einer gespeicherten Vorauswahl neue Dashboards bei Bedarf dort ergänzen. Bei Ladefehlern bleiben frühere Auswahlpräferenzen erhalten.

Bleibt das aktuelle Dashboard ausgewählt, bleiben auch ungespeicherte Zuordnungen erhalten. Wird es abgewählt, fragt die App vor dem Verwerfen ungespeicherter Änderungen nach. Bei gesperrtem Browser-Speicher zeigt sie einen Fehler und übernimmt die Vorauswahl nicht scheinbar erfolgreich.

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

0.1.5 auf .177 nach frischem Vollbackup geprüft: leere Karte ausgeblendet, Fehler der nicht konfigurierten Übersicht getrennt angezeigt, Abbrechen und gespeicherte leere/erneut aktivierte Vorauswahl nach Neuladen bestätigt. Dialog in DE/EN/FR sichtbar geprüft. Keine Benutzerzuordnung gespeichert; die vier Lovelace-Dateien bleiben unverändert. 26 Python- und zehn Node-Prüfungen sowie amd64-/aarch64-Docker-Builds bestanden.

0.1.3 wurde vom Nutzer mit Sammel-/Einzelauswahl, Speichern und Neuladen erfolgreich geprüft. 0.1.4 wurde nach Vollbackup als lokale App auf .177 aktualisiert. Die automatische Sprachwahl folgt dort Deutsch → Englisch → Französisch → Deutsch ohne Neuladen der App. Namen und Zuordnungen bleiben erhalten; alle vier Lovelace-Dateien einschließlich „Test für APP“ sind nach der Prüfung SHA-256-identisch zur Sicherung. Ergänzend bestehen Offline-Frontend-, API-, Datenerhalt- und Konflikttests. Kein Produktivsystem wurde verändert. Die vollständige HA-Backup-Wiederherstellung der App ist noch offen. Eine nicht konfigurierte Standardübersicht kann `config_not_found` melden; ein vorhandenes manuelles Dashboard auswählen.

- [App-Quellcode und Paket auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/projects-mqtt/)
- [English](/en/projects/dashboard-user-manager/) · [Français](/fr/projects/dashboard-user-manager/)
