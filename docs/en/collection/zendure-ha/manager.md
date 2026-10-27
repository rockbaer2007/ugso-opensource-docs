---
title: Zendure Manager
description: Operating modes and performance control of the Zendure Manager.
---
<a id="current-focus"></a>

# Zendure Manager {#zendure-manager}

The Zendure Manager tries to regulate the P1/house consumption sensor towards `0 W` via the Zendure devices. To do this, it controls the charging and discharging performance of the devices.

::: warning HEMS and app programs
If Zendure Manager and HEMS or a power program in the Zendure app are controlling at the same time, they can work against each other. Only use an active control strategy.
:::

## P1 sensor {#p1-sensor}

The P1 sensor should provide home consumption:

- positive value: house consumes mains electricity
- negative value: house feeds in

This sensor is the basis for Smart Matching.

## Operating modes {#betriebsarten}

| Mode | Meaning |
| --- | --- |
| `Aus` | Manager does not control devices |
| `Manuelle Leistungsregelung` | fixed power value via `Manuelle Leistung` |
| `Smarte Leistungsregelung` | tries to keep the P1 sensor at 0W |
| `Smartes nur Entladen` | like Smart Matching, but without loading |
| `Smartes nur Laden` | only charges, does not discharge |
| `Solar speichern` | stores solar/offgrid input preferably in batteries |

## Manual performance {#manuelle-leistung}

For `Manuelle Leistungsregelung`, the entity `Manuelle Leistung` determines how much power should be fed in or out.

- positive value: battery discharges towards house/grid
- negative value: Battery charges if the device supports AC charging

## Smart matching {#smart-matching}

With Smart Matching, the manager distributes power to the available devices. Fuse group, charge level, minimum SoC, maximum performance and device status all play a role.

The original wiki describes the distribution logic as partially outdated. Therefore, this page should be seen as a guide and checked against the current code if necessary.

Original wiki:

- [Function description](https://github.com/Zendure/Zendure-HA/wiki/Function-description)
- [Power distribution strategy](https://github.com/Zendure/Zendure-HA/wiki/Power-distribution-strategy)
