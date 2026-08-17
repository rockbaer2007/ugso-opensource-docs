# Parcel to MQTT

<img src="/images/parcel-to-mqtt-icon.svg" alt="Parcel to MQTT icon" width="96">

Parcel to MQTT is a Home Assistant app that publishes parcel tracking data through MQTT Discovery.

The current version uses DHL account parcel lists, optional manual DHL tracking numbers and Hermes parcel tracking. Notifications are intentionally handled through normal Home Assistant automations based on the generated entities.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

The shared status model is inspired by the MIT licensed Home Assistant parcel integrations [ha-parcel-integrations](https://github.com/ha-parcel-integrations).
:::

## Features

- DHL account parcel list through the DHL browser login code
- optional direct DHL parcel tracking by manual tracking number
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

## Provider Roadmap

The ioBroker adapter settings are used as a reference for future provider login flows:

- DHL: active through `dhllogin://` browser login code plus optional manual tracking numbers
- Amazon: planned with e-mail, password, optional OTP token and cookie reset for login problems
- Hermes: currently active by manual tracking number; account login with app username and app password is planned
- UPS: planned with app username and app password
- GLS and DPD: planned after the stable login/session flow is mapped

## Repository

[Open Parcel to MQTT on GitHub](https://github.com/rockbaer2007/parcel-to-mqtt)

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
