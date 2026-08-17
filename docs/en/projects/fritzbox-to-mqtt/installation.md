# Installation

## Requirements

- Home Assistant with Supervisor/App-Store.
- MQTT broker, for example the Mosquitto broker app.
- MQTT integration enabled in Home Assistant.
- FRITZ!Box user with permissions for telephony, network status and system data.
- TR-064 enabled on the FRITZ!Box.

## Add The Repository

1. Open Home Assistant.
2. Open **Settings > Apps > App-Store**.
3. Open the three-dot menu and choose **Repositories**.
4. Add this repository:

```text
https://github.com/rockbaer2007/fritzbox-to-mqtt
```

5. Install **FRITZ!Box to MQTT**.
6. Fill in the configuration.
7. Start the app.

## HACS

HACS is not the right installation path for this project. The app runs as a Docker-based Supervisor service and is installed through the Home Assistant App-Store.
