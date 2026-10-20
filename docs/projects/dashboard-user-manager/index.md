---
title: Dashboard-Benutzerverwaltung
description: Benutzer für alle HA-Ansichten oder einzeln per Checkbox zuordnen, mit Sicherung und DE/EN/FR.
---
# Dashboard-Benutzerverwaltung

**Version 0.1.11 · DE / EN / FR · MIT · stabil**

<img src="/images/dashboard-user-manager/icon.png" width="96" height="96" alt="App-Icon mit Dashboard-Matrix, Benutzern und Häkchen" />

Ab 0.1.7 ist das eigene PNG-Icon in der HA-App-Kachel, im Kopf der Oberfläche und als App-Favicon enthalten. Das freigegebene Motiv ist in ZIP und UGSo-Paket vollständig enthalten und benötigt keinen externen Bilddienst. Die HA-Seitenleiste behält ihr konfiguriertes MDI-Symbol. Einstellungen, gespeicherte Vorauswahl und Dashboard-Daten bleiben beim Icon-Update erhalten.

Eine eigenständige HA-App: Dashboards auswählen, Benutzer als Spalten und Ansichten als Zeilen anzeigen und die Zuordnung per Checkbox bearbeiten. Kein ATLAS erforderlich. Die breite Oberfläche nutzt 90 vw und 90 vh; die Checkbox-Tabelle hat eine eigene begrenzte Höhe und scrollt vertikal sowie bei Bedarf horizontal. Innerhalb der Tabelle wischen oder den Scrollbereich fokussieren und Pfeiltasten/Bild auf/Bild ab verwenden. Ansichtennamen und Benutzerköpfe bleiben fixiert; niedrige Displays verwenden kürzere Köpfe. Außerhalb der Tabelle scrollt die übrige Seite.

![Vertikale und horizontale Scrollfläche in 0.1.11 auf .177 bei 390 × 844 Pixeln](/images/dashboard-user-manager/ha-177-scroll-mobile-0.1.11.png)

![Stabile Dashboard-Benutzerverwaltung 0.1.10 nach Wiederherstellung auf .177](/images/dashboard-user-manager/ha-177-de-0.1.10.png)

Echte Aufnahme vom Testsystem .177, 20.10.2026, nach vollständiger Wiederherstellung und Update auf 0.1.10: deutsche Oberfläche, 18 Ansichten und vier Benutzer. Das vorhandene Dashboard wurde nicht geändert.

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

## Zeitlimit, Abbruch und Entwurf

Ab 0.1.9 endet das Warten beim Speichern spätestens nach 30 Sekunden. **Warten abbrechen** beendet es früher. Die Checkbox-Auswahl bleibt erhalten; **Entwurf sichern** lädt die geplanten Zuordnungen als lokale JSON-Datei herunter. Diese Datei ist ein Entwurfsnachweis, kein vollständiges Dashboard-Backup und kein automatisch rückimportierbares Projekt. Vor dem Schließen des Tabs sichern.

Wurde noch kein Schreibauftrag gesendet, kann nach Behebung der Ursache erneut gespeichert werden. Bei **Speicherergebnis unklar** bleibt Speichern gesperrt: **Serverstand prüfen** liest den tatsächlichen Stand und verhindert die spätere Ausführung eines noch unbenutzten Speicherplans. Bereits gespeicherter Entwurf, unveränderter Server und zwischenzeitliche Änderungen werden unterschieden; die Prüfung schreibt nicht erneut. Auch sie ist zeitlich begrenzt und abbrechbar. Bei einem Konflikt zuerst den Entwurf sichern und anschließend bewusst neu laden.

Abbrechen beendet nur das lokale Warten; ein bereits beim Server eingegangener Schreibauftrag kann noch fertig werden. Deshalb nicht blind wiederholen. Nach einem App-Neustart kann eine neue Sitzung nötig sein: Entwurf zuerst sichern, anschließend die Sitzung neu laden und die gewünschten Änderungen gezielt übernehmen. Der Entwurf wird nicht automatisch nachgespeichert und überlebt ein Schließen/Neuladen nicht ohne die heruntergeladene Datei.

## Automatische Sprache

**Automatisch (Home Assistant)** übernimmt die HA-Oberflächensprache. Ist der umgebende HA-Rahmen nicht lesbar, gilt die bevorzugte Browsersprache. Nicht unterstützte Sprachen verwenden Englisch. Oben lässt sich zusätzlich DE, EN oder FR auswählen; die Präferenz gilt nur für diesen Browser.

Die Übersetzung umfasst Beschriftungen, Hilfen, Dialoge, Status, Datumsanzeigen, Barrierefreiheit und Servermeldungen. Ungespeicherte Checkboxen bleiben beim Sprachwechsel erhalten. Eigene Namen und gespeicherte Dashboard-Daten werden nicht übersetzt. Keine Cloud-Übersetzung oder zusätzlichen Schlüssel erforderlich.

## Sicherungen und Konflikte

Vor jeder Änderung entsteht eine vollständige Dashboard-JSON unter `/data/backups/` im privaten App-Speicher. Über **JSON sichern** herunterladen. Die Dateien enthalten alle Kartenkonfigurationen und müssen vertraulich aufbewahrt werden. App-Updates erhalten diesen Speicher; vor einer Deinstallation herunterladen oder in einem HA-Backup sichern.

Die App vergleicht Dashboard und Benutzerliste mit dem geladenen Stand und prüft nach dem Schreiben das Ergebnis. Zwischenzeitliche Änderungen sperren das Speichern. HA bietet kein atomares Vergleich-und-Speichern: während der kurzen Speicherphase nicht parallel in einem anderen Editor bearbeiten.

Eine Wiederherstellung sichert zuvor erneut und wird gesperrt, wenn das Dashboard nach der betreffenden Änderung weiter bearbeitet wurde. Bei unbestätigtem Speichern nicht blind wiederholen, sondern aktuellen Stand und Sicherung prüfen.

## App oder vollständiges HA-Backup wiederherstellen

Ein HA-Vollbackup muss die **Dashboard-Benutzerverwaltung** unter Apps enthalten: Dort liegen die privaten Dashboard-Sicherungen. Die eigentlichen Dashboards gehören zum HA-Konfigurationsanteil. Vor dem Rücksetzen eine frische vollständige Sicherung erstellen und keine parallelen Änderungen vornehmen.

Unter **Einstellungen → System → Backups** die passende Sicherung öffnen. Nur **Dashboard-Benutzerverwaltung** auswählen, um die App einschließlich ihrer privaten Sicherungen zurückzusetzen; die aktuelle HA-Dashboard-Konfiguration bleibt dabei bestehen. Für eine vollständige Wiederherstellung **Home Assistant**, Einstellungen/Verlauf, vorhandene Ordner und alle benötigten Apps auswählen. Dabei wird der gesamte ausgewählte Umfang auf den Sicherungszeitpunkt zurückgesetzt, einschließlich später angelegter Testobjekte. HA ist während seines Neustarts nicht erreichbar.

Nach Abschluss die App erneut über die HA-Seitenleiste öffnen. Version, vorhandene Dashboard-Sicherungen, Dashboard-/Benutzerzahl und Browser-Vorauswahl kontrollieren. Erst bei bestätigtem Serverstand weiter bearbeiten. Vollbackups und private Dashboard-JSON vertraulich aufbewahren; eine Browser-Vorauswahl ersetzt keine Datensicherung.

## Lokale ZIP-Installation aktualisieren

Nach Vollbackup die vollständigen neuen Quelldateien nach `/addons/dashboard_user_manager/` kopieren und im HA-Terminal ausführen:

```sh
touch /addons/dashboard_user_manager/config.yaml
ha store reload
ha apps info local_dashboard_user_manager
```

Sobald `version_latest` die neue Version meldet, in HA aktualisieren. `touch` erneuert nur den Zeitstempel und hilft bei älteren ZIPs, deren erhaltene Zeitstempel Supervisor sonst nicht als Änderung erkennt. Nicht deinstallieren. Repository-Apps werden über ihr Repository aktualisiert.

## Prüfstand und Grenzen

**0.1.11 – Scrollkorrektur:** Nutzerbefund: fehlende vertikale Bedienbarkeit auf BV6200 Pro mit Android 14/DokeOS 4.0, Samsung Tablet A6 mit Android 11, Companion-App und Chrome. Die Tabelle hat nun eine ausdrücklich vertikal scrollbar begrenzte Höhe, eine horizontale Scrollrichtung bei Platzmangel, Touch-Gesten und getrenntes Scrollen gegenüber der umgebenden Seite. Die Beschriftung nennt beide Richtungen in DE/EN/FR.

Nach frischem Vollbackup auf .177 von 0.1.10 auf 0.1.11 aktualisiert. Chrome-Prüfung mit 390 × 844, 844 × 390, 768 × 1024 und 1024 × 768 Pixeln: vertikales Scrollen bis zur letzten Ansicht möglich, im schmalen Handyformat auch horizontal. Köpfe und erste Spalte bleiben fixiert; sämtliche Checkbox-Zustände, 18 Ansichten, vier Benutzer, Vorauswahl und 17 private Sicherungen erhalten. Kein Speichern von Zuordnungen ausgeführt. Alle 23 geprüften ursprünglichen HA-Dateien bytegleich; Projekte, Plugins und Papierkorb unverändert. 33 Python- und 19 Node-Prüfungen sowie Docker-Builds amd64/arm64 bestanden.

**Geräteprüfung durch den Nutzer am 20.10.2026 bestätigt:** Vertikales und horizontales Scrollen funktionieren mit 0.1.11 in der tatsächlichen Home-Assistant-Companion-App auf Handy und Tablet: BV6200 Pro mit Android 14/DokeOS 4.0 sowie Samsung Tablet A6 mit Android 11. Damit ist auch der zuvor ausstehende Finger-Scrolltest auf beiden Geräten erfolgreich abgeschlossen. Grundlage ist die ausdrückliche Nutzerrückmeldung; die oben dokumentierte Chrome-Prüfung bleibt als eigener Nachweis erhalten.

**0.1.10 – Serverausgänge „nicht gespeichert“ und „Konflikt“ auf .177 geprüft:** Nach frischem Vollbackup wurde ausschließlich für das eigene Testdashboard der erste und dritte Schreibauftrag vor dem Senden an HA durch einen echten Socket-Abbruch verhindert. Die unveränderte App behandelte beide Ausgänge zunächst als unklar; alle Checkboxen des Entwurfs blieben erhalten. Kein Eingriff in Bestandsdashboards oder Zugriffsrechte.

- **Nicht gespeichert:** HA-Datei vor und nach **Serverstand prüfen** exakt gleich zum Ausgangsstand. Meldung **Serverstand ist unverändert. Dein Entwurf ist erhalten und kann erneut gespeichert werden.** Speichern wird wieder freigegeben; der bewusst gestartete zweite Versuch speichert anschließend genau die beiden gewünschten Benutzerlisten und liest sie erfolgreich zurück.
- **Konflikt:** Nach dem dritten, ebenfalls verhinderten Schreibauftrag änderte eine zweite HA-Sitzung einen Karteninhalt im eigenen Dashboard. Die Serverprüfung erkannte die Abweichung, sperrte Speichern und erhielt den vollständigen Entwurf. **Entwurf sichern** lieferte eine geprüfte JSON mit beiden geplanten Zuordnungen ohne Zugangsdaten. Die Änderung der zweiten Sitzung blieb durch die Prüfung bytegleich erhalten; keine erneute HA-Schreiboperation.

Alle 14 vorherigen privaten Dashboard-Sicherungen erhalten; die zwei verhinderten Versuche und der bewusste erfolgreiche Versuch erzeugten jeweils eine neue Sicherung. Der Konfliktvergleich erzeugte keine zusätzliche. Entwurf vor der Bereinigung privat gesichert, ursprüngliche Vorauswahl und automatische Sprache wiederhergestellt, Instrumentierung entfernt und Original-App neu aufgebaut. Eigenes Dashboard entfernt, „Test für APP“ und alle Bestandsdaten erhalten; weiterhin 0.1.10 und drei HA-Vollbackups auf .177. Zusammen mit den vorherigen Prüfungen sind alle drei Serverausgänge real geprüft: **bereits gespeichert, nicht gespeichert, Konflikt**.

![Unveränderter HA-Stand erkannt, Entwurf erhalten und erneutes Speichern möglich](/images/dashboard-user-manager/ha-177-outcome-before-0.1.10.png)

![Konflikt erkannt, Entwurf erhalten und Überschreiben gesperrt](/images/dashboard-user-manager/ha-177-outcome-conflict-0.1.10.png)

**0.1.10 – Abbruch während der HA-Schreibbestätigung auf .177 geprüft:** Nach frischem Vollbackup wurde die echte WebSocket-Verbindung der App zu HA für genau einen Schreibauftrag des eigenen Testdashboards unmittelbar nach dem Senden und vor dem Empfang der Ergebnisnachricht abgebrochen. Kein erfolgreicher Schreibstatus wurde an die App zurückgegeben und kein anschließendes Rücklesen im Commit ausgeführt. HA hatte die beiden gewünschten Benutzerlisten dennoch gespeichert, wie der unabhängige Dateivergleich belegt.

Die App meldete **Speicherergebnis unklar**, behielt den Checkbox-Entwurf vollständig und sperrte erneutes Speichern. **Serverstand prüfen** stellte über eine neue Verbindung fest: **Bereits gespeichert; kein erneuter Schreibvorgang.** Genau eine zusätzliche private Dashboard-Sicherung, alle 13 bisherigen Sicherungen erhalten; die HA-Datei blieb durch die Serverprüfung bytegleich. Karten, Namen, Pfade und Unteransicht unverändert. Anschließend temporäre Instrumentierung entfernt, Original-App neu aufgebaut und Testdashboard bereinigt. Bestandsdaten einschließlich „Test für APP“ und die ursprüngliche Vorauswahl bleiben erhalten; Paketversion weiterhin 0.1.10.

![Entwurf nach Abbruch des HA-WebSocket vor der Schreibbestätigung erhalten](/images/dashboard-user-manager/ha-177-ws-ack-draft-0.1.10.png)

![Neue Serververbindung erkennt bereits gespeicherten Entwurf ohne doppeltes Schreiben](/images/dashboard-user-manager/ha-177-ws-ack-checked-0.1.10.png)

**0.1.10 – Bestätigungsabbruch auf .177 geprüft:** Nach frischem Vollbackup wurde eine einmalige, ausschließlich auf ein eigenes Testdashboard begrenzte Instrumentierung verwendet: Die App schrieb zwei Zuordnungen tatsächlich nach HA, las sie erfolgreich zurück und brach dann die echte HTTP-Antwortverbindung zum Ingress ab, bevor die Oberfläche die Bestätigung erhielt. Dies ist ein gezielter Rückkanalfehler mit realen HA-Daten, kein nur gemockter Test und kein physisches Ziehen eines Netzwerkkabels.

Die Oberfläche meldete **Speicherergebnis unklar**, behielt sämtliche Checkbox-Auswahlen und sperrte erneutes Speichern. **Serverstand prüfen** erkannte den bereits gespeicherten Entwurf ohne weiteren Schreibvorgang. Genau eine zusätzliche Dashboard-Sicherung; die HA-Datei blieb nach der Prüfung bytegleich. Karten, Namen, Pfade und Unteransicht unverändert. Anschließend Testinstrumentierung vollständig entfernt, Original-App neu aufgebaut und eigenes Dashboard gelöscht: alle 23 geprüften HA-Dateien einschließlich „Test für APP“ und alle 19 App-Quelldateien bytegleich zum Ausgangsstand; sieben ATLAS-Projekte, Plugins, Papierkorb, Vorauswahl und automatische Sprache erhalten. Version und veröffentlichte Paketdateien bleiben unverändert bei 0.1.10.

![Unklarer Ausgang nach unterbrochener HTTP-Bestätigung, Entwurf erhalten auf .177](/images/dashboard-user-manager/ha-177-lost-ack-draft-0.1.10.png)

![Serverprüfung erkennt bereits gespeicherten Entwurf ohne erneutes Schreiben](/images/dashboard-user-manager/ha-177-lost-ack-checked-0.1.10.png)

**0.1.10 – Wiederherstellung geprüft, „Experimentell“ entfernt:** Am 20.10.2026 auf .177 zunächst frisch vollständig gesichert. Reine App-Wiederherstellung aus diesem Backup: Die zwölf ursprünglichen privaten Dashboard-Sicherungen sind wieder vorhanden, der zusätzliche Prüfmarker ist entfernt und die aktuelle HA-Testkonfiguration bleibt unverändert. Anschließend vollständige Wiederherstellung von HA 2026.10.2 einschließlich Einstellungen/Verlauf, Share, Medien, SSL und sämtlichen Apps ausgeführt. HA und die App starten wieder; „Test für APP“ zeigt unverändert 18 Ansichten und vier Benutzer, automatische Sprache und Vorauswahl bleiben erhalten.

Nach dem Neustart sind 21 HA-Dateien einschließlich aller vorhandenen Lovelace-Dateien bytegleich. Die zwei übrigen geprüften Register behalten sämtliche 22 Geräte und 73 Entitäten samt Einstellungen; nur Laufzeit-Änderungszeitstempel und die von HA erfasste App-Version aktualisieren sich. Sieben ATLAS-Projekte, Pluginverwaltung und Papierkorbstand sind unverändert. Die bestehende ATLAS-HA-Verbindung funktioniert ohne erneute Zugangsdaten. Das erst nach dem Backup angelegte Testdashboard wird durch die Vollwiederherstellung entfernt. Es handelt sich um eine Rücksicherung auf der vorhandenen Testinstallation, keinen Neuaufbau auf leerer Hardware. 33 Python- und 19 Node-Tests sowie Docker-Builds amd64/aarch64 bestanden. 0.1.10 entfernt nur die experimentelle Paketkennzeichnung und aktualisiert Version/Nachweise; Speicherlogik und Berechtigungen bleiben unverändert. .68 und Produktivsysteme wurden nicht verwendet.

Die Prüfungen decken verhinderte Schreibaufträge, eine zwischenzeitliche Änderung aus zweiter Sitzung, HA-WebSocket-Abbruch vor Empfang der Schreibbestätigung und HTTP-Rückkanalabbruch nach erfolgreichem HA-Rücklesen ab. Alle drei Serverausgänge sind an eigenen Testdaten beobachtet, keine Garantie für jeden möglichen Abbruchzeitpunkt. Ein physischer LAN-/Stromausfall wurde nicht ausgelöst. Die Anleitung zu unklaren Schreibausgängen gilt weiterhin.

![App nach vollständiger HA-Wiederherstellung auf .177 mit erhaltenem Originaldashboard](/images/dashboard-user-manager/ha-177-full-restore-0.1.9.png)

### Frühere Prüfungen – damaliger Stand

**Konflikte und Verbindungsunterbrechung mit 0.1.8 auf .177 geprüft:** Nach frischem Vollbackup wurden zwei App-Tabs mit demselben eigenen Testdashboard geöffnet. Eine Änderung in Tab A wurde gespeichert; der veraltete Entwurf aus Tab B wurde mit Konflikthinweis abgelehnt. Seine Auswahl blieb sichtbar, der Serverstand aus Tab A blieb bytegleich. Nach bewusstem Zurücksetzen/Neuladen ließ sich die zweite Änderung speichern, ohne die erste zu überschreiben.

Beim kontrollierten Stoppen der App wurde ein noch laufender Speichervorgang vollständig abgeschlossen und bestätigt. Der anschließende Speicherversuch gegen die gestoppte App änderte keine Daten. Nach Wiederstart erschien die Fehlermeldung zur Erreichbarkeit/Sitzung, der ungespeicherte Entwurf blieb erhalten und es erfolgte kein automatisches Nachspeichern. Nach Serververgleich und erneutem Laden war gezieltes Speichern wieder möglich. Karten, Namen und Unteransicht blieben erhalten; das eigene Testdashboard wurde anschließend entfernt.

**0.1.9 – Timeout-/Abbruchbefund behoben:** Nach frischem Vollbackup auf .177 installiert. Bei vollständig gestoppter App greift das lokale 30-Sekunden-Limit; manueller Abbruch und Erreichbarkeitsfehler erhalten ebenfalls beide geänderten Zeilen. Kein Schreibauftrag, Serverdatei bytegleich. Der heruntergeladene Entwurf enthält beide geplanten Zuordnungen und keine Tokens. Nach App-Neustart und erneuerter Sitzung ist gezieltes Speichern erfolgreich; Karten, Namen, Pfade und Unteransicht bleiben erhalten. Eigenes Testdashboard entfernt, ursprüngliche Vorauswahl und automatische Sprache wiederhergestellt; die vier vorhandenen Lovelace-Dateien einschließlich „Test für APP“ sind bytegleich zur Sicherung.

33 Python- und 19 Node-Prüfungen bestehen, einschließlich Fetch-/Antwort-Timeout, später Antworten, Abbruch, unklarem Schreibausgang, Serververgleich ohne erneutes Schreiben, Konflikten und verloren gegangener Bestätigung nach erfolgtem HA-Schreiben. Docker-Builds amd64/aarch64 und UGSo-App-CI erfolgreich. Ein harter Netzabbruch exakt zwischen HA-Schreiben und Bestätigung bleibt real unbewiesen; dieser Pfad ist automatisiert geprüft. Die vollständige App-/HA-Backup-Wiederherstellung bleibt offen, der experimentelle Status erhalten. .68 und Produktivsysteme unverändert.

![Zeitlimit erreicht, Entwurf erhalten – echte Prüfung 0.1.9 auf .177](/images/dashboard-user-manager/ha-177-timeout-0.1.9.png)

![Veralteten Speicherstand abgelehnt, Entwurf erhalten – echte Prüfung auf .177](/images/dashboard-user-manager/ha-177-conflict-0.1.8.png)

**0.1.8 – Speichern-Erfolgsmeldung korrigiert:** Der vollständige Satz samt Ansichtenanzahl wird als eine Übersetzung in DE/EN/FR angezeigt, unabhängig von der Sprache der API-Antwort. Eine bereits angezeigte Erfolgsmeldung folgt auch nach dem Speichern der aktuellen Sprachwahl ohne Neuladen. Der Hinweis auf gemischte Sprache in 0.1.7 weiter unten ist damit behoben.

Auf .177 nach frischem Vollbackup aktualisiert und mit einem eigenen Dashboard aus zwei Ansichten geprüft: drei echte Speichervorgänge in DE/EN/FR und Sprachwechsel nach dem Speichern bestanden. Jeweils zwei Zuordnungen geändert, keine Karten oder Namen. Automatische Sprache und ursprüngliche Vorauswahl wiederhergestellt; vorhandene Sicherungen erhalten. 28 Python- und zwölf Node-Prüfungen einschließlich englischer API-Antwort, nachträglichem Sprachwechsel und unverändertem Ergebnis bestanden; Docker-Builds für amd64/aarch64 und UGSo-App-CI erfolgreich. .68 und Produktivsysteme unverändert. Der experimentelle Status bleibt bis zum Abschluss der offenen Wiederherstellungs-/Konfliktprüfungen erhalten.

![Vollständig deutsche Speichern-Erfolgsmeldung auf .177 mit 0.1.8](/images/dashboard-user-manager/ha-177-save-de-0.1.8.png)

**Speichern und Wiederherstellen mit 0.1.7 am 20.10.2026 auf .177 bestanden:** Nach frischem HA-Vollbackup wurde ein eigenes temporäres Dashboard mit sechs Ansichten geprüft. Sammelauswahl/-abwahl für webuser und eine Einzelkorrektur änderten genau drei Ansichten. Nach Speichern und erneutem Laden waren nur die vorgesehenen Benutzerlisten geändert. Unberührte Sichtbarkeitswerte (`true`, `false`, `[]`), Karten einschließlich verschachtelter Inhalte, Pfade, Unteransicht und Originalnamen mit äußeren Leerzeichen blieben erhalten.

Die heruntergeladene automatische Sicherung enthielt exakt die ursprüngliche vollständige Dashboard-Konfiguration. Wiederherstellen erzeugte zuerst eine Gegensicherung des geänderten Standes und stellte danach die ursprüngliche Storage-Datei bytegleich wieder her. Das temporäre Dashboard wurde entfernt, die ursprüngliche Vorauswahl wiederhergestellt und alle vier vorhandenen Lovelace-Dateien einschließlich „Test für APP“ und Dashboard-Katalog blieben bytegleich. Auf .177 bleiben drei Vollbackups; private Wiederherstellungsnachweise und PC-Sicherungen bleiben erhalten. .68 und Produktivsysteme wurden nicht verändert.

![Erfolgreiche Wiederherstellung des eigenen Testdashboards auf .177 mit 0.1.7](/images/dashboard-user-manager/ha-177-restore-0.1.7.png)

Offen bleiben die vollständige App-/HA-Backup-Wiederherstellung und die reale Konflikt-/Abbruchprüfung. Kleine bekannte Darstellungsabweichung in 0.1.7: Die Speichern-Erfolgsmeldung kann einen englischen Satzteil in der deutschen Oberfläche enthalten; die Wiederherstellungsmeldung erschien korrekt deutsch. Die funktionale Prüfung ist bestanden.

0.1.7 nach frischem Vollbackup auf .177 aktualisiert: Icon in der HA-App-Kachel und im App-Kopf sichtbar, Kopfbereich in DE/EN/FR geprüft und fotografiert. Vorauswahl, 18 Ansichten, vier Benutzer und bestehende private Dashboard-Sicherung erhalten. Keine Zuordnung gespeichert; alle vier Lovelace-Dateien zur Sicherung unverändert. 28 Python- und elf Node-Prüfungen, korrekte PNG-Auslieferung, ZIP-Iconvergleich und amd64-/aarch64-Docker-Builds bestanden. Die persönliche Sprachwahl ist wieder auf automatisch gesetzt.

**Nutzerbestätigung vom 20.10.2026 für 0.1.6:** Das Update auf der betroffenen Installation ist erfolgreich. „Übersicht aktuell“ wird nur noch einmal angezeigt; die zuvor gespeicherte Dashboard-Vorauswahl ist erhalten. Diese Rückmeldung bestätigt die Korrektur im ursprünglich gemeldeten Fall und ergänzt die automatisierten Alias-/Dublettenprüfungen sowie den Update-Test auf .177. Es wurde dafür kein zusätzlicher Zugriff durch den Agenten auf das Produktivsystem ausgeführt.

0.1.5 auf .177 nach frischem Vollbackup geprüft: leere Karte ausgeblendet, Fehler der nicht konfigurierten Übersicht getrennt angezeigt, Abbrechen und gespeicherte leere/erneut aktivierte Vorauswahl nach Neuladen bestätigt. Dialog in DE/EN/FR sichtbar geprüft. Keine Benutzerzuordnung gespeichert; die vier Lovelace-Dateien bleiben unverändert. 26 Python- und zehn Node-Prüfungen sowie amd64-/aarch64-Docker-Builds bestanden.

0.1.3 wurde vom Nutzer mit Sammel-/Einzelauswahl, Speichern und Neuladen erfolgreich geprüft. 0.1.4 wurde nach Vollbackup als lokale App auf .177 aktualisiert. Die automatische Sprachwahl folgt dort Deutsch → Englisch → Französisch → Deutsch ohne Neuladen der App. Namen und Zuordnungen bleiben erhalten; alle vier Lovelace-Dateien einschließlich „Test für APP“ sind nach der Prüfung SHA-256-identisch zur Sicherung. Ergänzend bestehen Offline-Frontend-, API-, Datenerhalt- und Konflikttests. Kein Produktivsystem wurde verändert. Die vollständige HA-Backup-Wiederherstellung der App ist noch offen. Eine nicht konfigurierte Standardübersicht kann `config_not_found` melden; ein vorhandenes manuelles Dashboard auswählen.

- [App-Quellcode und Paket auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/projects-mqtt/)
- [English](/en/projects/dashboard-user-manager/) · [Français](/fr/projects/dashboard-user-manager/)
