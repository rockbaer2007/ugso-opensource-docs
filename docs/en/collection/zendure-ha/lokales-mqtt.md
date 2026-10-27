---
title: Zendure HA local MQTT
description: Set up local MQTT for Zendure legacy devices.
---
<a id="zendure-ha-lokales-mqtt"></a>
<a id="current-focus"></a>

# Local MQTT {#lokales-mqtt}

According to the original wiki, local MQTT is particularly relevant for Zendure legacy devices:

- Hyper2000
- Hub2000
- Hub1200
- Ace1500

Newer devices such as SolarFlow 800, SolarFlow 800 Pro and SolarFlow 2400 can communicate via `zenSDK` and typically do not require local MQTT.

## Requirements {#voraussetzungen}

- MQTT broker in Home Assistant, for example Mosquitto
- Bluetooth integration in Home Assistant
- Zendure device must be visible via Bluetooth
- WiFi SSID and WiFi password
- MQTT user and password

::: warning MQTT address
A real network address or IP address should be used as the MQTT server address. According to the original wiki, `core-mosquitto` is not a suitable network address for the Zendure devices.
:::

## Setup data {#einrichtungsdaten}

| field | Example/Note |
| --- | --- |
| MQTT server | IP address or hostname of the broker |
| MQTT port | mostly `1883` |
| MQTT user | Username on the broker |
| MQTT password | Password on the broker |
| WiFi SSID | WLAN into which the device should be integrated |
| WiFi password | Password of this WLAN |

## Connection type per device {#verbindungsart-pro-gerat}

For supported devices, the connection type can be selected for each device:

- `cloud`
- `local`
- depending on the device also `zenSDK`

When changing the connection type, the integration tries to set the MQTT server in the device via Bluetooth. The device can restart. The process may take a few seconds and will then generate a Home Assistant notification with success or failure.

## Reset connection {#reset-verbindung}

For legacy devices, the integration provides a button `Reset Verbindung`. This can be used if the MQTT conversion was not completed properly.

Original wiki:

- [Local MQTT (Legacy Devices)](https://github.com/Zendure/Zendure-HA/wiki/Local-Mqtt-(Legacy-Devices))
