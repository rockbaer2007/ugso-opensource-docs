# FRITZ!Box to MQTT

<img src="/images/fritzbox-to-mqtt-icon.svg" alt="FRITZ!Box to MQTT icon" width="96">

FRITZ!Box to MQTT is a Home Assistant app that publishes FRITZ!Box data to Home Assistant through MQTT Discovery.

The app combines several data sources because FRITZ!Box models and FRITZ!OS versions do not expose every value in the same place:

- TR-064 for many FRITZ!Box services
- FRITZ!Box web/Lua queries as fallbacks
- the live call monitor on port `1012`
- MQTT Discovery for automatic Home Assistant entity creation

::: info HACS
This project is a Home Assistant Supervisor app. HACS installs custom integrations and frontend cards, but not Docker-based Supervisor apps. Install it through the Home Assistant app repository flow.
:::

## Features

- Answering machines `AB0` to `AB4` with new and old messages, status and on/off switch.
- WLAN switches for 2.4 GHz, 5 GHz and guest WLAN where the FRITZ!Box exposes them.
- WAN connection data, upload rate, download rate and link status.
- External IPv4 and IPv6 address where available.
- Box status such as mesh role, PPP connection, DECT base and DNS over TLS.
- Call lists for all, incoming, outgoing, missed, rejected and blocked calls.
- Live call monitor with `RING`, `CALL`, `CONNECT` and `DISCONNECT`.
- Phonebooks with selectable display.
- Optional DECT handset sensors for internal number and device ID.

## Repository

[Open FRITZ!Box to MQTT on GitHub](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
- [Troubleshooting](./troubleshooting)
