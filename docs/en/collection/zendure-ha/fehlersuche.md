---
title: Zendure HA troubleshooting
description: Troubleshooting connection issues with the Zendure Home Assistant integration.
---
<a id="zendure-ha-troubleshooting"></a>
<a id="current-focus"></a>

# Troubleshooting {#fehlersuche}

## Basic check {#grundcheck}

1. Update integration to the current version.
2. Restart Home Assistant.
3. Check if the Zendure app token comes from the main account.
4. Check if devices are visible in the Zendure app.
5. Enable debug logging for Zendure integration.
6. For local MQTT: Check broker address, user, password, WiFi SSID and WiFi password.

## Common error messages {#haufige-fehlermeldungen}

| Message | Meaning/Measure |
| --- | --- |
| Token invalid | Copy tokens again from Zendure app |
| No devices found | Check wrong Zendure account or region |
| No MQTT server returned | Check local or cloud MQTT in Zendure app |
| No backup group | Set Fuse Group |
| HEMS | Device is influenced by HEMS and cannot be freely controlled by the manager |

## Hyper2000/Legacy devices {#hyper2000-legacy-gerate}

If you have connection problems, the original wiki recommends:

1. Enable debug logging.
2. Delete integration entry.
3. Restart device.
4. Update integration.
5. Add new integration with Zendure app token.
6. Enable MQTT logging.
7. Set up local MQTT with all fields.
8. First test `cloud` as the connection mode.
9. Set Fuse Group.
10. Check whether the device has a Bluetooth MAC address.
11. Wait at least 10 minutes because updates via Bluetooth can be delayed.

## If the device is not responding {#wenn-das-gerat-nicht-reagiert}

- Select operating mode `Manuelle Leistungsregelung`.
- Change `Manuelle Leistung` as a test, for example 300 W and then 400 W.
- Then test `Smarte Leistungsregelung`.
- If there is no response, save the complete debug log.

Original wiki:

- [Troubleshooting](https://github.com/Zendure/Zendure-HA/wiki/Troubleshooting)
