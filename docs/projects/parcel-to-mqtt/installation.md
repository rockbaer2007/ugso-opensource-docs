# Installation

::: warning Archiv: Entwicklung eingestellt
Diese Anleitung beschreibt das bisherige Paket. Parcel Tracker ist bereits deutlich weiter entwickelt; deshalb stellen wir die Weiterentwicklung von Parcel to MQTT ein. Siehe [Parcel Tracker von SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker) für die Alternative und deren Installation.
:::

Das bisherige Paket liegt im [Ordner `parcel_to_mqtt` des gemeinsamen Add-on-Repositories](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt). In Home Assistant wird die unten angegebene Repository-URL ohne `/tree/master/parcel_to_mqtt` eingetragen.

[![Parcel to MQTT in Home Assistant öffnen](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Home Assistant öffnen.
2. Zu **Einstellungen > Apps > App-Store** gehen.
3. Über das Drei-Punkte-Menü **Repositories** öffnen.
4. Dieses Repository hinzufügen:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

5. **Parcel to MQTT** installieren.
6. DHL-Sendungsnummern eintragen.
7. App starten.

MQTT Discovery muss in Home Assistant aktiv sein. Ein MQTT Broker wird benötigt.
