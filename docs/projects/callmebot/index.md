---
title: UGSo CallMeBot Whatsapp
description: WhatsApp-Textnachrichten aus Home Assistant mit Empfängerprofilen und Blockly.
---
# UGSo CallMeBot Whatsapp

Seit 0.1.4 heißt die App **UGSo CallMeBot Whatsapp**. Bestehende Profile, MQTT-Themen und Entitäts-IDs bleiben erhalten. Die separate [UGSo CallMeBot Signal](../callmebot-signal/) verwendet eigene Profile und Schlüssel.

Experimentelle **HA-App 0.1.4** im [gemeinsamen Repository mit Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot). Oberfläche und Bausteine sind vollständig in **DE/EN/FR**, mit Systemsprache und Hell/Dunkel/System. Inspiration: [ioBroker.whatsapp-cmb](https://github.com/ioBroker/ioBroker.whatsapp-cmb); eigenständige UGSo-Implementierung ohne ioBroker.

**Korrektur 0.1.1:** Der Versandbutton funktioniert auch ohne `crypto.randomUUID`, etwa bei HTTP-Ingress. Nach dem Update die App neu starten und die Seite neu laden. Anfrage-IDs verwenden verfügbare Zufallsbytes oder einen Zeitstempel mit Zähler; sie dienen der Dublettenprüfung, nicht der Anmeldung.

![CallMeBot-Oberfläche auf Deutsch](/assets/callmebot/de.png)

## Installieren und einrichten

1. Das Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im HA-App-Store hinzufügen.
2. **UGSo CallMeBot Whatsapp** installieren, MQTT-Broker einrichten und App starten.
3. Oberfläche über HA-Ingress öffnen. Der interne MQTT-Dienst liefert bevorzugt die Broker-Zugangsdaten; die App-Optionen sind der Fallback.
4. Mit der aktuellen Bot-Nummer aus der [offiziellen Aktivierungsanleitung](https://www.callmebot.com/blog/free-api-whatsapp-messages/) den eigenen Empfänger aktivieren. Genau `I allow callmebot to send me messages` an den Bot senden.
5. Profil-ID, Name, eigene aktivierte Telefonnummer **mit + und Ländervorwahl** sowie passenden API-Schlüssel speichern. Standardprofil festlegen. Bis zu 16 Profile.
6. Die Testschaltfläche sendet wirklich an das ausgewählte gespeicherte Profil; bei leerer Auswahl an den Standardempfänger.

Ein leeres Schlüsselfeld beim Speichern behält den vorhandenen Schlüssel. Die Oberfläche erhält den Schlüssel niemals zurück. Er liegt in `/data/profiles.json`, nicht in Blockly, MQTT-Nachrichten, Browser-Speicher oder Protokollen. Die Backend-Datei ist nicht verschlüsselt und wird in HA-Sicherungen aufgenommen.

## Blockly: CallMeBot

### Gespeicherte Profile auswählen

Ab **CallMeBot 0.1.2 und Blocks for HA 0.1.49** öffnet das Profilfeld eine durchsuchbare Auswahl mit Profilnamen, Profil-ID und Standardempfänger. **Neu laden** aktualisiert die Liste. Im Block steht der Profilname, im Projekt und YAML bleibt die unveränderte ID gespeichert. Eine leere ID verwendet den aktuellen Standardempfänger.

![CallMeBot-Profilauswahl auf Deutsch](/assets/callmebot/profiles-de.png)

Beide Apps aktualisieren und neu starten, dann die Blocks-Seite neu laden. HA muss mit dem MQTT-Broker verbunden sein und MQTT-Discovery mit dem Standardpräfix `homeassistant` erlauben. CallMeBot veröffentlicht einen Diagnose-Sensor, standardmäßig `sensor.ugso_callmebot_profiles`, über den Blocks den Katalog mit seiner vorhandenen HA-Verbindung liest. Eine Umbenennung des Sensors ist möglich; er wird anhand seiner Katalog-Kennung gefunden. Technische Grundlage: [HA MQTT-Sensoren und JSON-Attribute](https://www.home-assistant.io/integrations/sensor.mqtt/).

Der retained Katalog `ugso/callmebot/profiles` enthält nur IDs, Namen, Standardprofil, Anzahl und Kennung. Telefonnummern, Nachrichten und API-Schlüssel werden nicht veröffentlicht. Änderungen und MQTT-Neuverbindungen aktualisieren den Katalog. Profilnamen sind in MQTT und HA sichtbar.

Wenn App, MQTT, Discovery oder HA-Verbindung fehlen, bleiben manuelle Profil-ID und Standardempfänger nutzbar. Gelöschte IDs werden im Projekt nicht automatisch ersetzt; die App lehnt einen Versand an ein fehlendes Profil ab.

Seit **Blocks for HA 0.1.48** unter **Nachrichten → WhatsApp · CallMeBot**.

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
- Ein MQTT-Namensraum und eine Client-ID: eine App-Instanz pro Broker. Schreibrechte für Versandbefehle im Broker beschränken. Diese Vorschau verwendet den internen Broker; externe TLS-Konfiguration ist nicht enthalten.

CallMeBot Free ist für persönliche Texte an eigene aktivierte Nummern gedacht. Keine Gruppen, Medien, Antworten oder Zustellbestätigung. `accepted` bestätigt nur die API-Annahme. Telefonnummer, Schlüssel und Text gehen per HTTPS an CallMeBot. Quelle: [CallMeBot-Aktivierung und API](https://www.callmebot.com/blog/free-api-whatsapp-messages/).

## Entwicklungsstand

Docker-Build und Start, Backend-Tests mit Mock-Anbieter, MQTT-Protokoll, DE/EN/FR-Oberfläche, mobile Ansicht und Blockly-Export sind geprüft. Echte WhatsApp-Zustellung und Installation unter HA-Supervisor müssen mit der eigenen Einrichtung geprüft werden. Es wurden keine realen Nachrichten verschickt.

[Quellcode und lokale Testbefehle](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot) · Apache-2.0 · Unabhängiges Community-Projekt.
