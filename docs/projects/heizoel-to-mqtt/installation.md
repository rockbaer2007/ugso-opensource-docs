# Installation

Über den Button kann das Repository direkt in Home Assistant geöffnet werden:

[![Heizöl to MQTT in Home Assistant öffnen](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fheizoel-to-mqtt)

## App-Repository hinzufügen

1. Home Assistant öffnen.
2. **Einstellungen > Apps > App-Store** öffnen.
3. Im Drei-Punkte-Menü **Repositories** öffnen.
4. Dieses Repository eintragen:

```text
https://github.com/rockbaer2007/heizoel-to-mqtt
```

5. **Heizöl to MQTT** installieren.
6. PLZ, Mengen und Quellen konfigurieren.
7. App starten.

## MQTT

Die App nutzt den internen MQTT-Dienst von Home Assistant, wenn der Mosquitto-Broker als App verfügbar ist.
