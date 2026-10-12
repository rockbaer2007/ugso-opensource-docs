---
title: MQTT-Client
description: Ausgewählte Home-Assistant-Werte live per MQTT übertragen und gezielt steuern.
---

# MQTT-Client 0.1.16

MQTT-Client überträgt ausgewählte Geräte, Zustände und Attribute aus Home Assistant an einen externen MQTT-Broker, beispielsweise den MQTT-Adapter von ioBroker. Statt sämtliche HA-Entitäten zu spiegeln, wählst du die benötigten Werte selbst aus. Der vorhandene HA-Broker bleibt bestehen. Die App liest direkt aus HA; sie ist keine Broker-Bridge.

[Quellcode und Konfigurationsreferenz](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [English documentation](/en/projects/mqtt-client/)

## Einrichtung und Auswahl

1. `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im Home-Assistant-App-Store hinzufügen.
2. **MQTT-Client** installieren und starten; unterstützt werden amd64 und aarch64.
3. Die Weboberfläche öffnen und Host, Port, Benutzer und Passwort des externen Brokers speichern. Ohne TLS ist der Standardport 1883.
4. Links ein Gerät auswählen. Im Dialog sind seine Entitäten nach Steuerung, Sensoren, Konfiguration und Diagnose gruppiert. Die Suche findet auch Entitäten innerhalb eines Geräts.
5. Die gewünschten Werte und Attribute auswählen. Das Kontrollkästchen rechts in einer Wertzeile überträgt den Zustand einschließlich aller Attribute; die Geräteauswahl kann sämtliche Werte des Geräts übernehmen.

Änderungen werden unmittelbar übernommen. Ein zusätzlicher HA-Zugriffstoken ist nicht nötig: Die App verwendet den Supervisor-Zugang zur HA-Core-API. Für mehrere Instanzen unterschiedliche Client-IDs und Themenpräfixe verwenden.

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
