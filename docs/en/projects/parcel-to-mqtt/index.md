# Parcel to MQTT

<img src="/images/parcel-to-mqtt-icon.svg" alt="Parcel to MQTT icon" width="96">

Parcel to MQTT is a Home Assistant app that publishes parcel tracking data through MQTT Discovery.

The current version uses direct DHL and Hermes parcel tracking with manually configured tracking numbers. Notifications are intentionally handled through normal Home Assistant automations based on the generated entities.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

The shared status model is inspired by the MIT licensed Home Assistant parcel integrations [ha-parcel-integrations](https://github.com/ha-parcel-integrations).
:::

## Features

- direct DHL parcel tracking
- direct Hermes Germany parcel tracking
- multiple tracking numbers as comma-separated lists
- GLS configuration is prepared, but GLS Germany is not active yet because it needs a guest bearer session
- DPD and UPS are planned as next provider targets
- MQTT Discovery for Home Assistant
- counters for total, registered, in transit, out for delivery, pickup point, delivered, returning, exception and unknown
- JSON list of all parcels
- up to 20 parcel slots, 6 by default
- Mushroom example card
- notifications through Home Assistant automations

## Repository

[Open Parcel to MQTT on GitHub](https://github.com/rockbaer2007/parcel-to-mqtt)

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
