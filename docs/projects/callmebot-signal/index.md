---
title: UGSo CallMeBot Signal
description: Signal-Textnachrichten aus Home Assistant mit Empfängerprofilen und Blockly.
---
# UGSo CallMeBot Signal

Experimentelle **HA-App 0.1.0** im [gemeinsamen Repository mit Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal). Vollständig **DE/EN/FR**, Systemsprache und Hell/Dunkel/System. Eigenständige UGSo-Implementierung, inspiriert von [ioBroker.signal-cmb](https://github.com/derAlff/ioBroker.signal-cmb).

![Signal-Oberfläche auf Deutsch](/assets/callmebot-signal/de.png)

## Einrichtung

1. Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` im HA-App-Store hinzufügen und **UGSo CallMeBot Signal** installieren.
2. MQTT in HA einrichten, App starten und Oberfläche über Ingress öffnen. Der interne MQTT-Dienst liefert bevorzugt die Zugangsdaten; App-Optionen dienen als Fallback.
3. Den aktuellen Bot-Kontakt aus der [offiziellen Signal-Aktivierungsanleitung](https://www.callmebot.com/blog/free-api-signal-send-messages/) verwenden. In **Signal** die dort angegebene Freischaltnachricht senden und den **Signal-API-Schlüssel** abwarten.
4. Profil-ID, Anzeigename, eigene internationale Telefonnummer **mit +** oder **Signal-UUID** sowie den passenden Schlüssel speichern. Bei verborgener Telefonnummer kann der Bot eine UUID liefern. Den Wert aus dem Aktivierungslink unverändert übernehmen.
5. Standardprofil wählen. „Nachricht senden“ sendet wirklich an das ausgewählte gespeicherte Profil.

WhatsApp-Schlüssel gelten nicht für Signal. Beide Apps können gleichzeitig laufen: getrennte Profile, MQTT-Themen, Client-IDs und Diagnose-Entitäten. Die [WhatsApp-App](../callmebot/) behält ihre bisherigen technischen IDs.

## Blockly und Profilauswahl

Seit **Blocks for HA 0.1.50**: **Nachrichten → Signal · CallMeBot**.

![Signal-Block](/assets/blocks-for-ha/blocks/de/ugso_callmebot_signal_action.png)

Profilfeld anklicken, nach Name/ID suchen und auswählen. Leer bedeutet Standardempfänger. Sichtbar ist der Name; gespeichert wird die Profil-ID. Text, Variable oder Jinja als Nachricht anschließen. Protokoll: nur Fehler, keins oder Info. Der Block erzeugt natives `mqtt.publish`; JSON wird nach der Template-Auswertung serialisiert.

Die App veröffentlicht einen Katalog auf `ugso/callmebot_signal/profiles` und per MQTT-Discovery die Diagnose-Entität **`sensor.ugso_callmebot_signal_profiles`**. Zustand: Profilanzahl. Attribute: IDs, Namen, Standardprofil und Quellenmarker, **keine Telefonnummer, Nachricht oder Schlüssel**. Blocks erkennt den Quellenmarker auch nach Umbenennung der Entität. Standard-Discovery-Präfix: `homeassistant`.

Bei fehlender Verbindung Profil-ID manuell eingeben oder leer lassen. Ungültige/gelöschte IDs werden nicht automatisch ersetzt. JSON-Projekte erhalten den Komfortblock; YAML-Import stellt den Versand als allgemeine HA-/MQTT-Aktion dar.

## Protokoll und Grenzen

- Versand: `ugso/callmebot_signal/send`, QoS 0, **retain false**.
- Beispiel: `{"profile":"default","message":"Hallo aus HA","loglevel":"errors"}`. Leeres Profil verwendet den Standardempfänger.
- Ergebnis: `ugso/callmebot_signal/result`, nicht retained, nur Profil, Anfrage-ID, Status und Zeit.
- Katalog und Verfügbarkeit: `ugso/callmebot_signal/profiles` und `ugso/callmebot_signal/availability`, retained. Verfügbarkeit zeigt die Broker-Verbindung.
- Maximal 16 Profile, 4000 Zeichen, Warteschlange 20, mindestens 10 Sekunden zwischen Versandversuchen je Profil. Schnellere Befehle werden abgelehnt.
- Optionale `request_id`: eine Stunde Dublettenprüfung, maximal 1000 IDs. Keine automatischen Wiederholungen oder Wiedergabe nach Neustart; retained Befehle werden abgelehnt.
- Eine Signal-App-Instanz pro Broker. Schreibrechte auf Versandthemen beschränken. Externe MQTT-TLS-Konfiguration ist nicht enthalten.

Diese App sendet **Textnachrichten an eigene aktivierte Empfänger**. Bilder, Gruppen und Antworten sind nicht implementiert. `accepted` bestätigt nur die API-Annahme. Empfänger, Schlüssel und Nachricht gehen per HTTPS an `https://signal.callmebot.com/signal/send.php`.

Schlüssel bleiben in der privaten Backend-Datei `/data/profiles.json`, werden nicht an Browser/MQTT/Blockly ausgegeben und nicht protokolliert. Die Datei ist nicht verschlüsselt und in HA-Backups enthalten; Backups entsprechend schützen.

## Prüfstand

Backend, UUID-/Nummernvalidierung, MQTT-Protokoll, Blockly/Jinja-Export, DE/EN/FR und mobile Ansicht sind mit Testdaten geprüft. Echte Signal-Zustellung und Installation unter HA-Supervisor sind mit der eigenen Einrichtung zu prüfen. Automatisierte Tests senden keine echten Nachrichten.

[Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal) · Apache-2.0 · Unabhängiges Community-Projekt.
