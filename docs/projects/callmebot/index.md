---
title: UGSo CallMeBot
description: WhatsApp-Textnachrichten aus Home Assistant mit Empfängerprofilen und Blockly.
---
# UGSo CallMeBot

Experimentelle **HA-App 0.1.0** im [gemeinsamen Repository mit Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot). Oberfläche und Bausteine sind vollständig in **DE/EN/FR**, mit Systemsprache und Hell/Dunkel/System. Inspiration: [ioBroker.whatsapp-cmb](https://github.com/ioBroker/ioBroker.whatsapp-cmb); eigenständige UGSo-Implementierung ohne ioBroker.

![CallMeBot-Oberfläche auf Deutsch](/assets/callmebot/de.png)

## Installieren und einrichten

1. Das Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im HA-App-Store hinzufügen.
2. **UGSo CallMeBot** installieren, MQTT-Broker einrichten und App starten.
3. Oberfläche über HA-Ingress öffnen. Der interne MQTT-Dienst liefert bevorzugt die Broker-Zugangsdaten; die App-Optionen sind der Fallback.
4. Mit der aktuellen Bot-Nummer aus der [offiziellen Aktivierungsanleitung](https://www.callmebot.com/blog/free-api-whatsapp-messages/) den eigenen Empfänger aktivieren. Genau `I allow callmebot to send me messages` an den Bot senden.
5. Profil-ID, Name, eigene aktivierte Telefonnummer **mit + und Ländervorwahl** sowie passenden API-Schlüssel speichern. Standardprofil festlegen. Bis zu 16 Profile.
6. Die Testschaltfläche sendet wirklich an das ausgewählte gespeicherte Profil; bei leerer Auswahl an den Standardempfänger.

Ein leeres Schlüsselfeld beim Speichern behält den vorhandenen Schlüssel. Die Oberfläche erhält den Schlüssel niemals zurück. Er liegt in `/data/profiles.json`, nicht in Blockly, MQTT-Nachrichten, Browser-Speicher oder Protokollen. Die Backend-Datei ist nicht verschlüsselt und wird in HA-Sicherungen aufgenommen.

## Blockly: CallMeBot

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
