---
title: Zendure Home Assistant Integration
description: German Zendure Home Assistant Integration documentation entry.
---
# Zendure Home Assistant Integration

This is the collection entry for the German Zendure Home Assistant Integration documentation.

The German documentation is maintained as an unofficial user guide. The original project and wiki remain authoritative.

| Field | Value |
| --- | --- |
| German documentation | [Zendure HA German docs](/sammlung/zendure-ha/) |
| Original project | [zendure/zendure-ha](https://github.com/zendure/zendure-ha) |
| Original wiki | [Zendure-HA Wiki](https://github.com/Zendure/Zendure-HA/wiki) |
| Documented repository state | `master`, checked on 2026-08-29 |
| Recent tags | `1.4.4`, `1.4.4-pre1` |
| License | MIT |

:::: details Detailed reference from the German documentation

## Zendure Home Assistant integration {#reference-zendure-home-assistant-integration}

The Zendure Home Assistant Integration integrates Zendure devices into Home Assistant. It provides reported values as entities, enables control values such as charging and output limits and offers power control using the Zendure Manager using a P1/house consumption sensor.

::: warning Unofficial English documentation
This documentation is an independent English guide based on the German documentation. The original project and the original wiki remain authoritative.
:::

### Project status {#projektstand}

| field | Value |
| --- | --- |
| Original project | [zendure/zendure-ha](https://github.com/zendure/zendure-ha) |
| Original Wiki | [Zendure-HA Wiki](https://github.com/Zendure/Zendure-HA/wiki) |
| Documented repo status | `master`, tested on 29.08.2026 |
| Last tags in repo | `1.4.4`, `1.4.4-pre1` |
| Minimum version according to README | Home Assistant `2025.5+` |
| Minimum version according to HACS file | Home Assistant `2025.4.0` |
| License | WITH |
| Integration domain | `zendure_ha` |

### Supported devices according to the original documentation {#unterstutzte-gerate-laut-originaldoku}

- Ace1500
- Aio2400
- Hyper2000
- Hub1200
- Hub2000
- SolarFlow 800 / 800 Pro / 800 Plus
- SolarFlow 1600 AC+
- SolarFlow 2400 AC / AC+ / Pro
- SolarFlow 4000 AC+
- SuperBase V6400
- SuperBase V4600 limited or not fully supported via tokens

### Content {#inhalt}

1. [Installation](/en/collection/zendure-ha/installation)
2. [Local MQTT](/en/collection/zendure-ha/lokales-mqtt)
3. [Fuse Group](/en/collection/zendure-ha/fuse-group)
4. [Zendure Manager](/en/collection/zendure-ha/manager)
5. [Entities](/en/collection/zendure-ha/entitaeten)
6. [Troubleshooting](/en/collection/zendure-ha/fehlersuche)

### Important note {#wichtiger-hinweis}

Some pages of the original wiki are marked as partially outdated by the project itself. In this English documentation, such content is adopted as a practical and orientation aid, but is not treated as a binding technical specification.

::::
