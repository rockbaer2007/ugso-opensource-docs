---
title: Zendure HA Fuse Group
description: Fuse Group and performance limits in the Zendure Home Assistant integration.
---
<a id="zendure-ha-fuse-group"></a>
<a id="current-focus"></a>

# FuseGroup {#fuse-group}

The Fuse Group is a security and tax group. It describes which Zendure devices are connected to the same fuse or circuit and what maximum power is permitted there.

::: danger responsibility
The correct selection of the Fuse Group is relevant to safety. Choose them to suit your electrical installation and local regulations.
:::

## Why it is important {#warum-sie-wichtig-ist}

Zendure Manager distributes power based on the fuse group setting. Devices in the same group together should not exceed the set limit.

Without a suitable fuse group, a device will not be used for smart functions.

## Typical options {#typische-optionen}

| option | Meaning |
| --- | --- |
| `Nicht verwendet` | Device has no fuse group and is not used for smart matching |
| `Eigener Stromkreis / eigene Phase` | Device depends on its own circuit |
| `Sicherungsgruppe max. 800 W` | Group with a maximum of 800 W |
| `Sicherungsgruppe max. 1200 W` | Group with a maximum of 1200 W |
| `Sicherungsgruppe max. 2000 W` | Group with a maximum of 2000 W |
| `Sicherungsgruppe max. 2400 W` | Group with a maximum of 2400 W |
| `Sicherungsgruppe max. 3600 W` | Group with a maximum of 3600 W |
| `Sicherungsgruppe max. 4000 W` | Group with a maximum of 4000 W |
| `Sicherungsgruppe max. 5000 W` | Group with a maximum of 5000 W |

## Connection status {#verbindungstatus}

The integration shows a connection status that helps with classification:

| Status | Meaning |
| --- | --- |
| `Unbekannt` | no clear connection status |
| `Kalibrierung` | Device calibrated |
| `HEMS` | Device is affected by HEMS |
| `Keine Sicherungsgruppe` | Fuse Group is missing |
| `Verbunden (Cloud)` | Connection via cloud |
| `Verbunden (Local)` | Connection via local MQTT |
| `Verbunden (zenSDK)` | Connection via zenSDK |

Original wiki:

- [Fuse Group](https://github.com/Zendure/Zendure-HA/wiki/Fuse-Group)
