---
title: MQTT-Client
description: Ausgewählte Home-Assistant-Werte live per MQTT übertragen und gezielt steuern.
---

# MQTT-Client 0.1.30 {#mqtt-client-0-1-16}

Ausgewählte HA-Zustände und Attribute gezielt an einen externen MQTT-Broker übertragen. Version 0.1.30 priorisiert Schalt-Rückmeldungen und ergänzt einen Kontrollabgleich mit HA. Die Korrektur wird als HA-App installiert; Helfer 0.1.27 kann bleiben.

[Release 0.1.30](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.30)

## Neu in 0.1.30: Zugangsdaten einklappen

**Zugangsdaten** besitzt jetzt eine eigene Auf-/Zuklapp-Schaltfläche, auch per Tastatur bedienbar. Bei vorhandenem Broker bleiben IP, Port, Benutzername und Passwort nach Laden und Speichern eingeklappt. Fehlen Pflichtangaben, wird der Bereich zur Eingabe geöffnet. **Übertragung und TLS**, **Speichern und verbinden** und **Aktuell übertragene Werte** bleiben sichtbar. Einstellungen und Zugangsdaten werden nicht verändert. Die Priorisierung aus 0.1.29 und Helfer 0.1.27 bleiben erhalten. Der Nutzer hat die Schalt-Rückmeldung mit ungefähr einer halben Sekunde Verzögerung als erfolgreich bestätigt. Auch die Zigbee-Lampe wurde erfolgreich geprüft: Rückmeldung funktioniert, die Helligkeit folgt HA auf 100 %.

## Neu in 0.1.29: Schaltwerte vor Messwerten

**Die HA-MQTT-Client-App auf 0.1.29 aktualisieren; der ioBroker-Helfer 0.1.27 bleibt unverändert.** Schaltzustände, Kontakte und Befehlsrückmeldungen werden vor Messwerten behandelt. Ihre Veröffentlichung wartet nicht auf die Publish-Pause. Bereits laufende Übertragungen werden abgeschlossen; zwischen Nachrichten geben Messwert-/Attributpakete für dringende Zustände und Schaltbefehle nach. Wenn mindestens 32 Ereignisse warten, werden Sensor-Zwischenstände in begrenzten Paketen auf den jeweils letzten Zustand zusammengefasst. Normale Schaltfolgen bleiben erhalten. Zusätzlich liest der Kontrollabgleich auch bei bestehender Live-Verbindung den tatsächlichen HA-Zustand im vorhandenen `poll_interval` (Standard 5 Sekunden). Unveränderte Werte werden nicht erneut veröffentlicht. **Übertragung und TLS** sowie die **Publish-Pause für Messwerte und Attribute** sind direkt sichtbar; Zugangsdaten bleiben separat einklappbar. Die Statuszeile unterscheidet **Wartend**, **Zusammengefasst**, **HA-Eingang** und den fortlaufenden Zähler **Gesendet**. Bestehende Einstellungen und Werte bleiben erhalten. Für die Prüfung den Kontrollabgleich auf 5 Sekunden lassen und ein unkritisches Relais in HA schalten. Erst eine tatsächliche HA-Rückmeldung führt zu `ack: true`; die Broker-Übergabe allein genügt nicht. Lokal geprüft, Bestätigung der Verzögerung auf dem Nutzersystem steht noch aus.

Schalter werden über die Domain `switch.*` erkannt und benötigen weder Geräteklasse noch Einheit. Lampen verwenden `light.*`. Die aktivierte automatische Messwertauswahl bleibt auf dieselbe HA-Gerätezuordnung beschränkt. Für Sensoren gilt zuerst `device_class`; fehlt sie, werden eindeutige Einheiten aus `unit_of_measurement` wie W/kW/MW, V/mV/kV, A/mA und Wh/kWh/MWh verwendet. Vorhandene Klassen werden nicht überschrieben; ähnliche Namen oder ein mehrdeutiges Prozentzeichen genügen nicht. Unter **Zugehörige Messwerte prüfen** zeigt eine schreibgeschützte Prüfung die erkannten Sensoren und Ausschlussgründe, etwa fehlende Gerätezuordnung, deaktivierte Entität oder ungeeignete Klasse/Einheit. Messwerte dürfen hinter Schaltwerten warten. Einstellungen, Zugangsdaten und bestehende Werte bleiben erhalten.

## Neu in 0.1.28: HA-Live-Rückmeldungen ohne fremde Ereignisflut

Diese Korrektur betrifft die **MQTT-Client-App in Home Assistant**: auf 0.1.28 aktualisieren und die App neu starten. Der ioBroker-Helfer 0.1.27 kann unverändert bleiben; sein Austausch allein behebt den Empfang von HA-Ereignissen nicht. Bei aktiver Label-Auswahl werden nur noch Ereignisse tatsächlich ausgewählter Entitäten und ihrer aktivierten Gerätemesswerte eingereiht. Ereignisse des übrigen HA-Bestands können die Warteschlange nicht mehr füllen. Wenn Labels oder Gerätezuordnungen geändert werden, lädt der Client frische HA-Zustände. Ältere gepufferte Zustände mit überholtem `last_updated` werden nach einem Abgleich verworfen; normale zeitlich geordnete Änderungen bleiben erhalten. Der Überlastzähler zählt seit dem App-Start und meldet weiterhin echte Überläufe ausgewählter Ereignisse. Die eingestellte Publish-Pause und alle Zugangsdaten/Auswahlen bleiben erhalten; ein großer erster Abgleich kann weiterhin länger dauern. Nach abgeschlossenem Erstabgleich ein unkritisches Relais in HA schalten und prüfen, ob MQTT und der virtuelle ioBroker-Status zeitnah folgen. Live-Bestätigung auf dem Nutzersystem steht noch aus.

## Neu in 0.1.27: Rückkanal ohne Retain

Schaltbefehle werden jetzt gezielt über die ioBroker-MQTT-Schnittstelle `sendMessage2Client` mit **`retain: false`** veröffentlicht. Normale Schreibzugriffe auf MQTT-`set`-Datenpunkte können im Servermodus mit gesetztem Retain-Flag beim Client ankommen. Der HA-Client verwirft solche Befehle weiterhin, damit beim Verbinden keine alten Schaltaufträge ausgeführt werden. Globale Broker-Einstellungen und MQTT-Datenpunktwerte bleiben erhalten. Der Helfer prüft den Befehlstopic gegen den zugehörigen Statustopic und verwendet `native.topic`, nicht aus Objekt-IDs erratene Pfade. In VIS 2 weiterhin ausschließlich den virtuellen Datenpunkt unter `0_userdata.0.ugso_mqtt` mit `ack: false` bedienen und `mode: 'apply'` verwenden. Die Logzeile `Command handed to MQTT adapter (retain=false)` bestätigt nur die Übergabe; erst ein neuer HA-Status bestätigt den Vorgang. Der rohe MQTT-`set`-Wert muss dabei nicht wechseln. Keine automatischen Wiederholungen; Fehler oder fehlende HA-Bestätigung bleiben als unbestätigt erkennbar. Für diese Korrektur die vollständige Helferdatei ersetzen und eigene Einstellungen übernehmen.

## Neu in 0.1.26: automatische Basisanlage

Fehlende eigene Basisordner (`virtualRoot`, `aliasRoot`) und beide Sicherungsdatenpunkte (`virtualBackupId`, `backupId`) werden jetzt beim Start in **jedem Modus** automatisch angelegt, auch in `preview` und `restore`. Vorhandene Ordner, Sicherungen, Werte und manuelle Rollen werden nicht überschrieben. Neue Journale enthalten gültige leere Strukturen. Für die Basisanlage muss `setObject` in der JavaScript-Instanz auch in der Vorschau erlaubt sein. Fehlende Freigaben oder kollidierende Pfade werden als Fehler gemeldet. Die Vorschau legt keine steuerbaren VIS-2-Datenpunkte an und ändert keine MQTT-Rollen oder Gerätewerte; dafür nach Prüfung `mode: 'apply'` verwenden. Die ereignisgesteuerte Verarbeitung aus 0.1.25 bleibt erhalten.

## Automatische VIS-2-Datenpunkte ab 0.1.24

Der kombinierte ioBroker-Helfer erstellt virtuelle Datenpunkte mit Status und
Rückkanal in einem. Unterstützt werden Switches, Light-Werte und weitere freigegebene
Zahl-/Auswahl-/Textkanäle; Datum und Messwerte bleiben lesend. Die ursprünglichen
MQTT-Werte, Einstellungen und vorhandenen Aliase bleiben erhalten. Vorschau,
automatische Sicherung, Typ-/Grenzwertprüfung und Schutz vor Rückkopplungen sind
enthalten. Die Warnungen beim Lesen fehlender optionaler Datenpunkte sind korrigiert.
Für die APIs von JavaScript-Adapter **10.4.10** vorbereitet, noch kein neuer realer
Installationstest.

[Einrichtung und Zuordnungstabelle](./iobroker-roles.md#vis2) ·
[Release 0.1.24](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.24)

## ioBroker-Rollenzuordnung ab 0.1.23

Ein optionales JavaScript ordnet Datum, Zeitstempel und eindeutige Messwerte
passenden ioBroker-Rollen zu. Vorschau, Sicherung vor Änderungen und Wiederherstellung
sind enthalten. Vorhandene Werte, Zugangsdaten und manuelle Spezialrollen bleiben
erhalten. Schreibbare MQTT-Messwerte erhalten lesende Aliase. Das Skript lässt
abweichende Datentypen, Einheiten und mehrdeutige Klassen aus.

[Installation und vollständige Zuordnung HA → ioBroker](./iobroker-roles.md) ·
[Release 0.1.23](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.23)

## Neu in 0.1.22

Die Label-Auswahl aktiviert jetzt den Zustand, vorhandene Standardattribute und
passende Rückkanäle steuerbarer Entitäten. Schalter erhalten automatisch
`<base>/set` für `ON`/`OFF`; Zahlen, Selects und Taster verwenden ihre
unterstützten Befehle. Es werden beim Einrichten keine Schaltbefehle gesendet.
Retain-Befehle, leere Befehle und ungültige Werte werden verworfen.

Bei Lampen entstehen nur die von HA gemeldeten Kanäle:

| Kanal unter `<base>` | Wert und Rückkanal |
| --- | --- |
| `brightness/state`, `brightness/set` | Helligkeit 0–100 % |
| `rgb_color/state`, `rgb_color/set` | JSON `[255,128,0]`, Komponenten 0–255 |
| `effect/state`, `effect/set` | Effektname aus der gemeldeten Effektliste |
| `color_temp_kelvin/state`, `color_temp_kelvin/set` | Ganze Kelvinzahl innerhalb der gemeldeten Grenzen |

`<base>` ist das bestehende Topic ohne `/state`. Effektliste, unterstützte
Farbmodi und minimale/maximale Kelvinwerte werden als Attribute nur gelesen.
Manuell ausgewählte HA-Attribute behalten ihren Pfad und ihre Einheit:
`attribute/brightness` bleibt beispielsweise 0–255.

Unter **Übertragung und TLS** kann **Zugehörige Mess- und Batteriewerte desselben
Geräts automatisch einbeziehen** aktiviert werden. `label_device_readings` ist
standardmäßig `false`. Berücksichtigt werden Energie, Spannung, Strom, Leistung,
Temperatur, Feuchtigkeit und Batterie sowie ein vorhandener Batterie-leer-Sensor.
Die Zuordnung erfolgt ausschließlich über dieselbe HA-Geräte-ID. Es werden keine
Schwellwerte erfunden oder ähnlich benannte Geräte zusammengefasst. Diese
zusätzlichen Sensoren erhalten keine Rückkanäle.

Automatisch übertragen werden vorhandene Standardangaben wie Name, Geräteklasse,
Einheit und Zustandsklasse sowie notwendige Auswahl-/Grenzwerte. Andere Attribute
bleiben manuell auswählbar. `device_class` wird als Metadatum übertragen; die
ioBroker-Rolle, etwa `date`, wird dadurch nicht automatisch geändert.

Das Werte-Popup zeigt auch automatische Attribute, Light-Werte und aktive
Rückkanäle mit ihrer Herkunft. Nach Entfernen des Labels entfallen automatische
Werte und Rückkanäle beim nächsten Abgleich; wartende Befehle werden vor der
Ausführung erneut geprüft. Manuelle Auswahlen und Zugangsdaten bleiben erhalten.
Alte Retain-Werte werden erst über die bestätigte Topic-Bereinigung entfernt.

Lokal mit simuliertem HA und Broker geprüft; kein neuer Gerätetest auf HA.
[Release 0.1.22](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.22)

## Aktuell übertragene Werte

Ab **0.1.21** klappen nur die Zugangsdaten automatisch ein. **Übertragung und TLS**
ist davon getrennt erreichbar. **Speichern und verbinden** und **Aktuell übertragene
Werte** bleiben gleich groß in einer Reihe sichtbar.

Der zweite Button öffnet eine durchsuchbare, scrollbare Liste aller aktuell
ausgewählten States und Attribute, einschließlich der per HA-Label ausgewählten
States. Doppelte States werden zusammengeführt. Die Herkunft wird als beschriftetes
Badge gezeigt: **Label** blau, **Manuell** grün, **Beides** violett. Seit 0.1.22
werden auch automatische Standardattribute und Light-Werte angezeigt.

Jede Zeile zeigt Name, Entitäts-ID, gegebenenfalls Attribut, aktuellen Wert und
MQTT-Topic. Die letzte erfolgreiche Brokerbestätigung enthält Zeitpunkt und
gesendeten Wert; noch nicht bestätigte Werte sind gekennzeichnet und Fehler
separat rot markiert. Die Bestätigung belegt die Annahme durch den Broker,
nicht die Verarbeitung durch ioBroker oder ein Zielgerät. Im geöffneten Popup
erfolgt alle drei Sekunden eine Aktualisierung, zusätzlich über **Aktualisieren**.
Die Übersicht gilt für die laufende Verbindung und wird bei deren Neustart
zurückgesetzt. Zugangsdaten und Einstellungen werden weder geändert noch in
dieser Liste ausgegeben. Lokal mit manuellen/Label-Auswahlen, Attributen,
Bestätigungsfehlern und Mobilansicht geprüft.
[Release 0.1.21](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.21)

**0.1.20:** Die Verbindungseinstellungen sind unter **Zugangsdaten** einklappbar.
Zur Ersteinrichtung bleibt der Bereich offen. Mit gespeicherter Brokeradresse
klappt er nach dem Laden und erfolgreichen Speichern automatisch zu. Ein Klick
auf den Titel öffnet ihn wieder. Speicher- und Fehlermeldungen bleiben sichtbar;
Einstellungen und Zugangsdaten bleiben erhalten.
[Release 0.1.20](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.20)

**0.1.19** ergänzt die Zeilentrennung in der Übertragungsliste: Der Name steht
über der Zusammenfassung aus State, ausgewählten Attributen und Rückbefehl.
**Bearbeiten** bleibt rechts. Auch diese Ansicht wurde lokal bei 1300 und
390 Pixeln Breite geprüft. [Release 0.1.19](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.19)

MQTT-Client überträgt ausgewählte Geräte, Zustände und Attribute aus Home Assistant an einen externen MQTT-Broker, beispielsweise den MQTT-Adapter von ioBroker. Statt sämtliche HA-Entitäten zu spiegeln, wählst du die benötigten Werte selbst aus. Der vorhandene HA-Broker bleibt bestehen. Die App liest direkt aus HA; sie ist keine Broker-Bridge.

[Quellcode und Konfigurationsreferenz](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [English documentation](/en/projects/mqtt-client/)

## Einrichtung und Auswahl

Seit **0.1.18** sind die Angaben im Geräte-Popup klar getrennt: **Name** in der
ersten Zeile, **Entitäts-ID** in der zweiten und **Zieltyp mit Attributanzahl**
in der dritten. Lange Namen und IDs werden umgebrochen; der aktuelle State bleibt
rechts. Die Trennung bleibt auch nach einer Änderung der Auswahl erhalten.
Die Darstellung wurde lokal bei 1300 und 390 Pixeln Breite geprüft.
Einstellungen, Zugangsdaten und die Auswahl der übertragenen Werte bleiben beim
Update erhalten. [Release 0.1.18](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.18)

1. `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im Home-Assistant-App-Store hinzufügen.
2. **MQTT-Client** installieren und starten; unterstützt werden amd64 und aarch64.
3. Die Weboberfläche öffnen und Host, Port, Benutzer und Passwort des externen Brokers speichern. Ohne TLS ist der Standardport 1883.
4. Links ein Gerät auswählen. Im Dialog sind seine Entitäten nach Steuerung, Sensoren, Konfiguration und Diagnose gruppiert. Die Suche findet auch Entitäten innerhalb eines Geräts.
5. Die gewünschten Werte und Attribute auswählen. Das Kontrollkästchen rechts in einer Wertzeile überträgt den Zustand einschließlich aller Attribute; die Geräteauswahl kann sämtliche Werte des Geräts übernehmen.

Änderungen werden unmittelbar übernommen. Ein zusätzlicher HA-Zugriffstoken ist nicht nötig: Die App verwendet den Supervisor-Zugang zur HA-Core-API. Für mehrere Instanzen unterschiedliche Client-IDs und Themenpräfixe verwenden.

## Weiterleitung per Home-Assistant-Label {#weiterleitung-per-label}

![Home Assistant: Dialog zum Anlegen eines neuen Labels](/images/projects/mqtt-client/ha-label-erstellen.png)

*Beispiel in Home Assistant: Das Label heißt hier „zu mqtt client“. Verwende im MQTT-Client die ID des Labels, das du angelegt hast.*

1. **Label anlegen:** Gehe in Home Assistant zu **Einstellungen → Bereiche, Labels und Zonen → Labels**. Erstelle das Label **zu mqtt client** wie im Screenshot.
2. **Label-ID ablesen:** Öffne **Einstellungen → Werkzeuge → Vorlage** (bei älteren Versionen **Entwicklerwerkzeuge → Vorlage**). Gib die Vorlage unten ein und kopiere das Ergebnis, beispielsweise `zu_mqtt_client`.
3. **ID im MQTT-Client eintragen:** Öffne **MQTT-Client** in der Home-Assistant-Seitenleiste. Klappe **Übertragung und TLS** auf. Direkt unter **Topic-Präfix** findest du **HA-Label-ID für Zustandsweiterleitung**. Füge dort das Ergebnis aus Schritt 2 ein und klicke **Speichern und verbinden**.
4. **Label zuweisen:** Öffne **Einstellungen → Geräte & Dienste → Entitäten**, wähle die gewünschte Entität und öffne über das Zahnrad ihre Einstellungen. Wähle **Label hinzufügen → zu mqtt client** und klicke **Aktualisieren**.

```jinja
{{ label_id("zu mqtt client") }}
```

[Home Assistant · label_id](https://www.home-assistant.io/template-functions/label_id/)

Der Client prüft die Zuordnung im eingestellten Polling-Intervall. Das Label sendet Zustand und Standardattribute und aktiviert passende Rückkanäle. Weitere Attribute bleiben manuell auswählbar. Beim Entfernen des Labels endet die automatische Weiterleitung samt Rückkanälen; manuell ausgewählte Entitäten bleiben aktiv. Den letzten gespeicherten MQTT-Wert kannst du bei Bedarf über die Retain-Bereinigung entfernen.

Auf Home Assistant `.177` mit einem separaten MQTT-Broker geprüft: Nach dem Hinzufügen kamen `off` und `on` an. Nach dem Entfernen wurde die nächste Zustandsänderung nicht mehr gesendet. [Release 0.1.17](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.17)

## Live-Übertragung und Status

Nach dem vollständigen Anfangsstand verarbeitet die App HA-Zustandsänderungen live über WebSocket. Nach einer erneuten HA-Verbindung wird der Anfangsstand neu eingelesen; nach einer MQTT-Neuverbindung werden alle ausgewählten Werte erneut übertragen.

Bei ausgefallener Live-Verbindung bleibt die bisherige Abfrage als Fallback aktiv: **standardmäßig alle fünf Sekunden**, einstellbar über `poll_interval` von 1 bis 300 Sekunden. Während einer Unterbrechung oder zwischen Fallback-Abfragen verpasste Änderungen lassen sich nicht nachträglich rekonstruieren. Eine überlastete Ereigniswarteschlange wird angezeigt und löst eine erneute Synchronisierung aus.

Der Status unterscheidet MQTT-Verbindung und HA-Erreichbarkeit und zeigt Live-/Abfragemodus, letzte Synchronisierung, letzte Veröffentlichung, Anzahl der Veröffentlichungen und bereinigte Fehlertypen. Zugangsdaten und Nachrichteninhalte werden dort nicht ausgegeben.

| MQTT-Thema | Inhalt |
| --- | --- |
| `<topic_prefix>/<device>/<value>/state` | Zustand als Text |
| `<topic_prefix>/<device>/<value>/attribute/<attribute>` | Ausgewähltes Attribut |
| `<topic_prefix>/<device>/<value>/set` | Rückkanal für unterstützte Steuerbefehle |
| `<topic_prefix>/availability` | `online` nach erfolgreicher HA-Synchronisierung, sonst `offline` |

Standardpräfix ist `ha_external`. Zustände und Attribute werden mit QoS 1 und Retain veröffentlicht; MQTT-Discovery wird nicht erzeugt. Beim ersten Aufbau kommen Zustände und Attribute vor den `/set`-Rückkanälen, standardmäßig mit 50 ms Abstand zwischen Veröffentlichungen. `unknown` und `unavailable` werden weitergereicht; fehlende Entitäten liefern `unavailable`.

## Steuerbefehle zurück an HA

Für ausgewählte steuerbare Entitäten werden Rückkanäle automatisch aktiviert. Sensoren bleiben reine Ausgänge. Befehle an das passende `/set`-Thema **ohne Retain** senden.

| Entität | Nutzdaten |
| --- | --- |
| Schaltbare Entität | `ON` oder `OFF` |
| `number`, `input_number` | Zahlenwert |
| `select`, `input_select` | Name einer verfügbaren Option |
| `text`, `input_text` | Text |
| `button`, `input_button` | `PRESS` |
| `cover` | `OPEN`, `CLOSE`, `STOP` oder `{"position":45}` |
| `light` | `{"brightness_pct":75}` |
| `fan` | `{"percentage":50}` |

Die JSON-Befehle erlauben jeweils nur das genannte Feld und eine endliche Zahl von 0 bis 100. Das HA-Gerät muss die Funktion unterstützen. Alte Entitäts-ID-Themen wie `ha_external/switch.plug/set` bleiben gültig. Retained-Befehle, veraltete Befehle und ungültige Inhalte werden verworfen; beliebige HA-Aktionsaufrufe sind nicht vorgesehen.

## Veraltete Retain-Topics entfernen

**Veraltete Retain-Topics prüfen** zeigt aufgezeichnete Themen, die durch geänderte Auswahl, Präfixe oder Gerätenamen nicht mehr verwendet werden. Gewünschte Themen markieren und das Löschen bestätigen; höchstens 100 pro Vorgang.

Die App löscht ausschließlich eigene, erfolgreich bestätigte Veröffentlichungen auf dem aktuell konfigurierten Broker. Aktive und fremde Themen bleiben geschützt. Das Inventar liegt dauerhaft in `/data/mqtt-topics.json`. Fehlgeschlagene Löschungen bleiben für einen erneuten Versuch erhalten. Es gibt **keine automatische Bereinigung**. Nicht aufgezeichnete Alt-Themen aus der Zeit vor diesem Update müssen weiterhin direkt am Broker entfernt werden.

## Einstellungen sichern und wiederherstellen

**Einstellungen sichern** lädt eine JSON-Datei mit Broker-Einstellungen, Client-ID, Themenpräfix, Auswahl, Abfrageintervall, Veröffentlichungsabstand und eigener CA herunter. **Sicherung öffnen** prüft die Datei und fragt vor dem Ersetzen nach.

Die Datei enthält **kein MQTT-Passwort, kein Client-Zertifikat, keinen privaten Schlüssel und keinen HA-Token**. Sie ist nicht verschlüsselt. Bei gleichem Broker bleiben lokal gespeicherte Zugangsdaten und Client-Zertifikat/Schlüssel erhalten. Bei einem anderen Broker müssen diese neu eingegeben werden. Retained-Inhalte sind nicht enthalten; eine vollständige HA-App-Sicherung wird dadurch nicht ersetzt.

## TLS mit eigenen Zertifikaten

Unter **Übertragung und TLS** können eigene CA, Client-Zertifikat und privater Schlüssel als PEM-Dateien geladen oder als Text eingefügt werden. Zertifikat und Schlüssel müssen zusammen vorliegen. Der TLS-Port richtet sich nach dem Broker, häufig 8883.

Serverzertifikat und Hostname werden immer geprüft, mit Systemvertrauen oder eigener CA. Leere Geheimnisfelder behalten gespeicherte Werte. Zum Entfernen die ausdrückliche Option **Gespeicherte TLS-Zertifikate und Schlüssel entfernen** aktivieren und speichern. Ungültige TLS-Konfigurationen werden vor dem Ändern der Einstellungen abgewiesen.

## Update und Kompatibilität

Bestehende Einstellungen aus 0.1.15 bleiben gültig: Broker-Zugangsdaten, Geräte-/Attributauswahl, Client-ID, Themenpräfix, Abfrageintervall und Veröffentlichungsabstand werden beim Start nicht umgeschrieben. TLS bleibt in seiner bisherigen Einstellung; neue Zertifikatsfelder sind standardmäßig leer. Retained-Daten werden beim Update nicht gelöscht.

Version 0.1.16 wurde mit Backend-Tests, einem MQTT-Broker, einer WebSocket-Gegenstelle, TLS mit Client-Zertifikat, Weboberfläche und Docker-Start geprüft. Die tatsächliche HA-Installation und die unterstützten Gerätefunktionen müssen mit der eigenen Umgebung geprüft werden.
