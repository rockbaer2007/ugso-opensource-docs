---
title: Zendure HA lokales MQTT
description: Lokales MQTT fuer Zendure Legacy-Geraete einrichten.
---
# Lokales MQTT

Lokales MQTT ist laut Original-Wiki vor allem für Zendure-Legacy-Geräte relevant:

- Hyper2000
- Hub2000
- Hub1200
- Ace1500

Neuere Geräte wie SolarFlow 800, SolarFlow 800 Pro und SolarFlow 2400 können über `zenSDK` kommunizieren und benötigen lokales MQTT normalerweise nicht.

## Voraussetzungen

- MQTT-Broker in Home Assistant, zum Beispiel Mosquitto
- Bluetooth-Integration in Home Assistant
- Zendure-Gerät muss per Bluetooth sichtbar sein
- WLAN-SSID und WLAN-Passwort
- MQTT-Benutzer und Passwort

::: warning MQTT-Adresse
Als MQTT-Serveradresse sollte eine echte Netzwerkadresse oder IP-Adresse genutzt werden. `core-mosquitto` ist laut Original-Wiki keine geeignete Netzwerkadresse für die Zendure-Geräte.
:::

## Einrichtungsdaten

| Feld | Beispiel / Hinweis |
| --- | --- |
| MQTT-Server | IP-Adresse oder Hostname des Brokers |
| MQTT-Port | meistens `1883` |
| MQTT-Benutzer | Benutzername am Broker |
| MQTT-Passwort | Passwort am Broker |
| WLAN SSID | WLAN, in das das Gerät eingebunden werden soll |
| WLAN-Passwort | Passwort dieses WLANs |

## Verbindungsart pro Gerät

Bei unterstützten Geräten kann pro Gerät die Verbindungsart gewählt werden:

- `cloud`
- `local`
- je nach Gerät auch `zenSDK`

Beim Wechsel der Verbindungsart versucht die Integration, den MQTT-Server per Bluetooth im Gerät zu setzen. Das Gerät kann dabei neu starten. Der Vorgang kann einige Sekunden dauern und erzeugt anschließend eine Home-Assistant-Benachrichtigung mit Erfolg oder Fehler.

## Reset Verbindung

Für Legacy-Geräte stellt die Integration einen Button `Reset Verbindung` bereit. Dieser kann genutzt werden, wenn die MQTT-Umstellung nicht sauber abgeschlossen wurde.

Original-Wiki:

- [Local MQTT (Legacy Devices)](https://github.com/Zendure/Zendure-HA/wiki/Local-Mqtt-(Legacy-Devices))

