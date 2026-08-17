# Installation

## Requirements

- Home Assistant with Supervisor/Add-on Store.
- MQTT broker, for example the Mosquitto broker add-on.
- MQTT integration enabled in Home Assistant.
- FRITZ!Box user with permissions for telephony, network status and system data.
- TR-064 enabled on the FRITZ!Box.

## Add The Repository

1. Open Home Assistant.
2. Open **Settings > Add-ons > Add-on Store**.
3. Open the three-dot menu and choose **Repositories**.
4. Add this repository:

```text
https://github.com/rockbaer2007/fritzbox-to-mqtt
```

5. Install **FRITZ!Box to MQTT**.
6. Fill in the configuration.
7. Start the add-on.

## HACS

HACS is not the right installation path for this project. The add-on runs as a Docker-based Supervisor service and is installed through the Home Assistant Add-on Store.
