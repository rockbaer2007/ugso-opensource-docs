---
layout: home

hero:
  name: FRITZ!Box to MQTT
  text: Home Assistant app for FRITZ!Box data
  tagline: Publish call lists, live calls, WLAN, WAN, phonebooks and FRITZ!Box status to Home Assistant through MQTT Discovery.
  actions:
    - theme: brand
      text: Installation
      link: /en/projects/fritzbox-to-mqtt/installation
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/ugso-ha-mqtt-addons

features:
  - icon: 📞
    title: Calls and answering machines
    details: Call lists, live call monitor and answering machines AB0 to AB4 as Home Assistant entities.

  - icon: 📶
    title: WLAN and network
    details: Switches for 2.4 GHz, 5 GHz and guest WLAN plus WAN connection data, IP addresses and link status.

  - icon: 📚
    title: Phonebooks
    details: Phonebooks with selectable display and optional exclusions for individual names.

  - icon: 🧭
    title: Multiple data sources
    details: TR-064, FRITZ!Box web/Lua fallbacks and the live call monitor are combined.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant creates sensors and switches automatically through MQTT Discovery.

  - icon: 🛠️
    title: Troubleshooting
    details: Dedicated troubleshooting page for login, TR-064, DNS over TLS, call monitor and MQTT.
---

## Overview

FRITZ!Box to MQTT is a Home Assistant app that publishes FRITZ!Box data to Home Assistant through MQTT Discovery.

The current published add-on state lives in the shared
`rockbaer2007/ugso-ha-mqtt-addons` repository. The older standalone
`rockbaer2007/fritzbox-to-mqtt` repository is archived.

The app combines several data sources because FRITZ!Box models and FRITZ!OS versions do not expose every value in the same place:

- TR-064 for many FRITZ!Box services
- FRITZ!Box web/Lua queries as fallbacks
- the live call monitor on port `1012`
- MQTT Discovery for automatic Home Assistant entity creation

::: info HACS
This project is a Home Assistant Supervisor app. HACS installs custom integrations and frontend cards, but not Docker-based Supervisor apps. Install it through the Home Assistant app repository flow.
:::

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
- [Troubleshooting](./troubleshooting)
