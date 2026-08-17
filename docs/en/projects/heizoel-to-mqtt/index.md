# Heizöl to MQTT

Heizöl to MQTT is a Home Assistant app that publishes heating-oil prices through MQTT Discovery.

The app queries public price calculator endpoints and normalizes the best offer per source and amount. It is intended for Germany and Austria only.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel).
:::

## Sources

- Esyoil
- Heizöl24 Germany
- Heizöl24 Austria

The price lookups are valid for German and Austrian postal codes only.

## Status

The app is a testable MVP. The used price endpoints are public website endpoints and not officially documented stable APIs.

## Repository

[Open Heizöl to MQTT on GitHub](https://github.com/rockbaer2007/heizoel-to-mqtt)

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
