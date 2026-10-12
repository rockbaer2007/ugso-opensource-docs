---
title: CallMeBot Whatsapp
description: WhatsApp-Textnachrichten aus Home Assistant mit Empfängerprofilen und Blockly.
---
# CallMeBot Whatsapp

Seit 0.1.5 heißt die App **CallMeBot Whatsapp**. Bestehende Profile, MQTT-Themen und Entitäts-IDs bleiben erhalten. Die separate [CallMeBot Signal](../callmebot-signal/) verwendet eigene Profile und Schlüssel.

Beta **HA-App 0.1.6** im [gemeinsamen Repository mit Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot). Oberfläche und Bausteine sind vollständig in **DE/EN/FR**, mit Systemsprache und Hell/Dunkel/System. Inspiration: [ioBroker.whatsapp-cmb](https://github.com/ioBroker/ioBroker.whatsapp-cmb); eigenständige UGSo-Implementierung ohne ioBroker.

**Korrektur 0.1.1:** Der Versandbutton funktioniert auch ohne `crypto.randomUUID`, etwa bei HTTP-Ingress. Nach dem Update die App neu starten und die Seite neu laden. Anfrage-IDs verwenden verfügbare Zufallsbytes oder einen Zeitstempel mit Zähler; sie dienen der Dublettenprüfung, nicht der Anmeldung.

![CallMeBot-Oberfläche auf Deutsch](/assets/callmebot/de.png)

## Installieren und einrichten

1. Das Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im HA-App-Store hinzufügen.
2. **CallMeBot Whatsapp** installieren, MQTT-Broker einrichten und App starten.
3. Oberfläche über HA-Ingress öffnen. Der interne MQTT-Dienst liefert bevorzugt die Broker-Zugangsdaten; die App-Optionen sind der Fallback.
4. Mit der aktuellen Bot-Nummer aus der [offiziellen Aktivierungsanleitung](https://www.callmebot.com/blog/free-api-whatsapp-messages/) den eigenen Empfänger aktivieren. Genau `I allow callmebot to send me messages` an den Bot senden.
5. Profil-ID, Name, eigene aktivierte Telefonnummer **mit + und Ländervorwahl** sowie passenden API-Schlüssel speichern. Standardprofil festlegen. Bis zu 16 Profile.
6. Die Testschaltfläche sendet wirklich an das ausgewählte gespeicherte Profil; bei leerer Auswahl an den Standardempfänger.

Ein leeres Schlüsselfeld beim Speichern behält den vorhandenen Schlüssel. Die Oberfläche erhält den Schlüssel niemals zurück. Er liegt in `/data/profiles.json`, nicht in Blockly, MQTT-Nachrichten, Browser-Speicher oder Protokollen. Die Backend-Datei ist nicht verschlüsselt und wird in HA-Sicherungen aufgenommen.

## Blockly: CallMeBot

### Gespeicherte Profile auswählen

Ab **CallMeBot 0.1.2 und Blocks for HA 0.1.69** öffnet das Profilfeld eine durchsuchbare Auswahl mit Profilnamen, Profil-ID und Standardempfänger. **Neu laden** aktualisiert die Liste. Im Block steht der Profilname, im Projekt und YAML bleibt die unveränderte ID gespeichert. Eine leere ID verwendet den aktuellen Standardempfänger.

![CallMeBot-Profilauswahl auf Deutsch](/assets/callmebot/profiles-de.png)

Beide Apps aktualisieren und neu starten, dann die Blocks-Seite neu laden. HA muss mit dem MQTT-Broker verbunden sein und MQTT-Discovery mit dem Standardpräfix `homeassistant` erlauben. CallMeBot veröffentlicht einen Diagnose-Sensor, standardmäßig `sensor.ugso_callmebot_profiles`, über den Blocks den Katalog mit seiner vorhandenen HA-Verbindung liest. Eine Umbenennung des Sensors ist möglich; er wird anhand seiner Katalog-Kennung gefunden. Technische Grundlage: [HA MQTT-Sensoren und JSON-Attribute](https://www.home-assistant.io/integrations/sensor.mqtt/).

Der retained Katalog `ugso/callmebot/profiles` enthält nur IDs, Namen, Standardprofil, Anzahl und Kennung. Telefonnummern, Nachrichten und API-Schlüssel werden nicht veröffentlicht. Änderungen und MQTT-Neuverbindungen aktualisieren den Katalog. Profilnamen sind in MQTT und HA sichtbar.

Wenn App, MQTT, Discovery oder HA-Verbindung fehlen, bleiben manuelle Profil-ID und Standardempfänger nutzbar. Gelöschte IDs werden im Projekt nicht automatisch ersetzt; die App lehnt einen Versand an ein fehlendes Profil ab.

Seit **Blocks for HA 0.1.68** unter **Nachrichten → WhatsApp · CallMeBot**.

![CallMeBot-Block](/assets/blocks-for-ha/blocks/de/ugso_callmebot_action.png)

Profil-ID angeben oder leer lassen für das Standardprofil. Text, Variable oder Jinja als Nachricht anschließen. Protokollstufe: nur Fehler, keins oder Info. Der Block erzeugt eine native `mqtt.publish`-Aktion. JSON wird erst nach der Template-Auswertung serialisiert; Anführungszeichen und Zeilenumbrüche bleiben korrekt.

HA muss MQTT eingerichtet haben. JSON-Projekte erhalten den Komfortblock. Beim YAML-Import bleibt der Versand als allgemeine HA-/MQTT-Aktion erhalten.

## Alternative: vorhandene WhatsApp-Integration

![WhatsApp-Integrationsblock](/assets/blocks-for-ha/blocks/de/ugso_whatsapp_action.png)

Der zweite Block ruft die [WhatsApp-Integration von FaserF](https://faserf.github.io/ha-whatsapp/services.html) direkt auf. Deren App-URL und **API-Token aus der WhatsApp-App** einmal im HA-Einrichtungsdialog hinterlegen. Der Block benötigt diesen Token nicht; die Integration verwaltet ihn.

Auswahl: `whatsapp.send_message · number` für das ältere Format, `whatsapp.send_message · target` für die aktuelle Doku oder `notify.whatsapp`, wenn diese Aktion eingerichtet ist. Empfänger **mit Ländervorwahl ohne +**, Nachricht als Text/Jinja. Optionales Konto wird nur bei `whatsapp.send_message` ausgegeben. Passende YAML-Aktionen werden als Komfortblock importiert; zusätzliche Optionen bleiben in der allgemeinen HA-Aktion.

Diese Variante benötigt keine CallMeBot-App und keinen CallMeBot-Schlüssel. Installation und WhatsApp-Verbindung übernimmt die vorhandene Integration.

## MQTT-Protokoll und Grenzen

- Versand: `ugso/callmebot/send`, QoS 0, **retain false**.
- Nutzdaten: `{"profile":"default","message":"Hallo aus HA","loglevel":"errors"}`. Leeres/fehlendes Profil nutzt den Standardempfänger.
- Optional: `request_id` für eine Stunde Dublettenprüfung je Profil, maximal 1000 gespeicherte IDs.
- Ergebnis: `ugso/callmebot/result`, nicht retained, nur Profil, Anfrage-ID, Status und Zeit; keine Nachricht oder Schlüssel.
- Verfügbarkeit: `ugso/callmebot/availability`, retained `online`/`offline`, zeigt die Broker-Verbindung.
- Maximal 4000 Zeichen, Warteschlange 20, mindestens 10 Sekunden zwischen Versandversuchen je Profil. Schnellere Befehle werden abgelehnt, nicht verzögert.
- Keine automatischen Wiederholungen oder Wiedergabe nach Neustart. Retained-Versandbefehle werden abgelehnt.
- Ein MQTT-Namensraum und eine Client-ID: eine App-Instanz pro Broker. Schreibrechte für Versandbefehle im Broker beschränken. Der interne Broker bleibt Standard; externe MQTT-Verbindungen mit geprüftem TLS sind optional.

CallMeBot Free ist für persönliche Texte an eigene aktivierte Nummern gedacht. Keine Gruppen, Medien, Antworten oder Zustellbestätigung. `accepted` bestätigt nur die API-Annahme. Telefonnummer, Schlüssel und Text gehen per HTTPS an CallMeBot. Quelle: [CallMeBot-Aktivierung und API](https://www.callmebot.com/blog/free-api-whatsapp-messages/).

## Entwicklungsstand

Docker-Build und Start, Backend-Tests mit Mock-Anbieter, MQTT-Protokoll, DE/EN/FR-Oberfläche, mobile Ansicht und Blockly-Export sind geprüft. Echte WhatsApp-Zustellung und Installation unter HA-Supervisor müssen mit der eigenen Einrichtung geprüft werden. Es wurden keine realen Nachrichten verschickt.

[Quellcode und lokale Testbefehle](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot) · Apache-2.0 · Unabhängiges Community-Projekt.

## Beta: Historie, Profilsicherung und MQTT-TLS

Die Historie enthält bis zu 200 dauerhaft gespeicherte Einträge mit Zeitpunkt, Profil-ID, Quelle und Ergebnis. Filter nach Profil oder Fehlerstatus und bestätigtes Löschen sind verfügbar. Nachrichten, Telefonnummern, API-Schlüssel und Anfrage-IDs werden nicht in der Historie gespeichert. „Angenommen“ bestätigt weiterhin nur die Annahme durch CallMeBot, keine Zustellung. Bei Speicherfehlern wird der Versand nicht wiederholt.

Die Profilsicherung verschlüsselt Profile einschließlich Telefonnummern, API-Schlüsseln und Standardempfänger mit AES-GCM und einem aus dem Sicherungspasswort abgeleiteten Schlüssel (scrypt). Mindestens 12 Zeichen; Passwort separat aufbewahren. Es wird nicht gespeichert. Ohne Passwort ist keine Wiederherstellung möglich. Wiederherstellen ersetzt die Profile erst nach Bestätigung und erfolgreicher Prüfung; falsches Passwort, beschädigte Dateien oder Sicherungen der anderen CallMeBot-App ändern nichts. Bei wartenden Versandversuchen wird die Wiederherstellung abgewiesen. MQTT-Zugangsdaten und Historie sind nicht enthalten; für diese weiterhin die vollständige HA-App-Sicherung verwenden.

Unter MQTT-Verbindung bleibt „HA-Broker automatisch verwenden“ der bisherige Standard. Für einen externen Broker die Automatik deaktivieren und Host, Port, Benutzer und Passwort angeben. TLS prüft Zertifikat und Hostname; eigene CA und Client-Zertifikat/Schlüssel sind als PEM-Datei oder Text möglich. TLS-Port passend wählen, häufig 8883. Leere Geheimnisfelder behalten gespeicherte Werte. HA/Blocks müssen diesen Broker verwenden oder die Send-/Result-/Profil-/Discovery-Topics zwischen den Brokern weiterleiten; eine externe Verbindung allein ersetzt keine Broker-Bridge.

Bestehende profiles.json, Profile, Schlüssel, MQTT-Themen und Entitäts-IDs bleiben erhalten. Neue Historie: /data/history.json; ausdrücklich gespeicherte MQTT-Einstellungen: /data/mqtt.json. Die Konfiguration wird beim Update nicht automatisch umgeschrieben. Alle neuen Oberflächentexte sind DE/EN/FR.

Die Oberfläche und Beschreibung heißen Beta. Home Assistant unterstützt keinen nativen stage-Wert beta; der gültige technische Status experimental bleibt deshalb bestehen. [HA-Konfiguration](https://developers.home-assistant.io/docs/apps/configuration/).
