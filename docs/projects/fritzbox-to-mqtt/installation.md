# Installation

## Voraussetzungen

- Home Assistant mit Supervisor/Add-on Store.
- MQTT-Broker, zum Beispiel das Mosquitto-Broker-Add-on.
- Aktivierter MQTT-Integration in Home Assistant.
- FRITZ!Box-Benutzer mit passenden Rechten für Telefonie, Netzwerkstatus und Smart-Home-/Systemdaten.
- TR-064 in der FRITZ!Box aktiviert.

## Add-on-Repository hinzufügen

1. Home Assistant öffnen.
2. **Einstellungen > Add-ons > Add-on Store** öffnen.
3. Im Drei-Punkte-Menü **Repositories** öffnen.
4. Dieses Repository eintragen:

```text
https://github.com/rockbaer2007/fritzbox-to-mqtt
```

5. **FRITZ!Box to MQTT** installieren.
6. Konfiguration ausfüllen.
7. Add-on starten.

## HACS

HACS ist für dieses Projekt nicht der richtige Installationsweg. Das Add-on läuft als Docker-basierter Supervisor-Dienst und wird über den Home-Assistant-Add-on-Store installiert.
