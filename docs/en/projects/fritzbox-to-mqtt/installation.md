# Installation

## Requirements

- Home Assistant with Supervisor/App-Store.
- MQTT broker, for example the Mosquitto broker app.
- MQTT integration enabled in Home Assistant.
- FRITZ!Box user with permissions for telephony, network status and system data.
- TR-064 enabled on the FRITZ!Box.

## Add The Repository

Use this button to open the repository directly in Home Assistant:

[![Open FRITZ!Box to MQTT in Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Open Home Assistant.
2. Open **Settings > Apps > App-Store**.
3. Open the three-dot menu and choose **Repositories**.
4. Add this repository:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

5. Install **FRITZ!Box to MQTT**.
6. Fill in the configuration.
7. Start the app.

## Local Development

To test the current local state in Home Assistant, copy the add-on folder from
the shared repository into Home Assistant's `addons` folder:

```text
C:\Users\rockb\source\repos\ugso-ha-mqtt-addons\fritzbox_tr064_tam
```

Target in Home Assistant:

```text
/addons/fritzbox_tr064_tam
```

Then reload repositories in the Home Assistant App-Store, update or install the
add-on and restart it.

## HACS

HACS is not the right installation path for this project. The app runs as a Docker-based Supervisor service and is installed through the Home Assistant App-Store.
