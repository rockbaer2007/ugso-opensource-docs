---
title: Zendure HA installation
description: Installing and setting up the Zendure Home Assistant integration.
---
<a id="zendure-ha-installation"></a>
<a id="current-focus"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

1. Open Home Assistant.
2. Open `HACS`.
3. Go to `Integrationen`.
4. Open `+ Explore & Download Repos`.
5. Search for `Zendure`.
6. Download `Zendure Home Assistant Integration`.
7. Reload the browser if Home Assistant does not yet display the integration directly.
8. Open `Einstellungen -> Geräte & Dienste -> Integration hinzufügen`.
9. Search for `Zendure` and start the setup.

Direct link:

[Add Zendure integration to Home Assistant](https://my.home-assistant.io/redirect/config_flow_start/?domain=zendure_ha)

## Zendure app token {#zendure-app-token}

The integration uses a token from the Zendure app. This token should come from the main account that the devices are registered to.

::: warning Upgrade from older versions
For older installations with a second account or old login, the old configuration must be removed and set up again. The current integration is token-based.
:::

The token dialog is documented with a screenshot in the original wiki:

[Token screenshot in original wiki](https://github.com/Zendure/Zendure-HA/wiki/Installation)

## Options in the setup dialog {#optionen-im-einrichtungsdialog}

| option | Meaning |
| --- | --- |
| `Zendure Token` | Tokens from the Zendure app |
| `P1 Sensor für Smart Matching` | Sensor for house consumption: positive for consumption, negative for feed-in |
| `MQTT-Kommunikation loggen` | writes MQTT communication to the HA log when debug logging is active |
| `Lokales MQTT verwenden` | opens a second dialog for local MQTT data |
| `MQTT-Benutzer automatisch verwalten` | tries to manage MQTT credentials automatically |
| `WLAN SSID` | WLAN name for the device change |
| `Wifi Passwort` | WiFi password for device switching |

## After setup {#nach-der-einrichtung}

After successful setup, Zendure devices and their entities appear in Home Assistant. If there are several devices, the [Fuse Group](/en/collection/zendure-ha/fuse-group) should then be set correctly so that smart matching and power limitations work sensibly.
