# Parcel to MQTT

<img src="/images/parcel-to-mqtt-icon.svg" alt="Parcel to MQTT icon" width="96">

Parcel to MQTT is a Home Assistant app that publishes parcel tracking data through MQTT Discovery.

The first version uses the 17TRACK API and manually configured tracking numbers. Notifications are intentionally handled through normal Home Assistant automations based on the generated entities.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).
:::

## Features

- 17TRACK API lookup
- multiple tracking numbers as a comma-separated list
- MQTT Discovery for Home Assistant
- counters for total, in transit, out for delivery, delivered, exception and unknown
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
