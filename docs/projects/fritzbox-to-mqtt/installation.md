# Installation

## Voraussetzungen

- Home Assistant mit Supervisor/App-Store.
- MQTT-Broker, zum Beispiel die Mosquitto-Broker-App.
- Aktivierter MQTT-Integration in Home Assistant.
- FRITZ!Box-Benutzer mit passenden Rechten für Telefonie, Netzwerkstatus und Smart-Home-/Systemdaten.
- TR-064 in der FRITZ!Box aktiviert.

## App-Repository hinzufügen

1. Home Assistant öffnen.
2. **Einstellungen > Apps > App-Store** öffnen.
3. Im Drei-Punkte-Menü **Repositories** öffnen.
4. Dieses Repository eintragen:

```text
https://github.com/rockbaer2007/fritzbox-to-mqtt
```

5. **FRITZ!Box to MQTT** installieren.
6. Konfiguration ausfüllen.
7. App starten.

## HACS

HACS ist für dieses Projekt nicht der richtige Installationsweg. Die App läuft als Docker-basierter Supervisor-Dienst und wird über den Home-Assistant-App-Store installiert.
