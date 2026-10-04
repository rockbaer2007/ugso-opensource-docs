---
layout: home

hero:
  name: Parcel to MQTT
  text: Development discontinued
  tagline: Parcel Tracker is already much further along. We are therefore discontinuing development of Parcel to MQTT. The existing documentation remains available as an archive.
  actions:
    - theme: brand
      text: View Parcel Tracker
      link: https://github.com/SoerenKaiser99/parcel_tracker
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt

features:
  - icon: 📦
    title: Parcel status
    details: Parcel status, last event, destination and tracking number as Home Assistant entities.

  - icon: 🚚
    title: DHL and Hermes active
    details: DHL account parcel list, manual DHL tracking numbers and Hermes parcel tracking.

  - icon: 🧩
    title: Provider sections
    details: Grouped settings for DHL, Hermes, GLS, DPD, UPS, Amazon Logistics, Deutsche Post letters and FedEx.

  - icon: 📊
    title: Counters and slots
    details: Counters for total, in transit, out for delivery, pickup point, delivered, returning, exception and unknown.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant creates parcel, status and counter entities automatically.

  - icon: 🔔
    title: Automations
    details: Notifications are built through normal Home Assistant automations based on the generated entities.
---

::: warning Development discontinued
Parcel Tracker is already much further along. We are therefore discontinuing development of Parcel to MQTT and recommend taking a look at [Parcel Tracker by SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker).

Source code and existing documentation remain available as an archive. The features and instructions below describe the final state of our package.
:::

## Overview

Parcel to MQTT is a Home Assistant app that publishes parcel tracking data through MQTT Discovery.

The current version uses DHL account parcel lists, optional manual DHL tracking numbers and Hermes parcel tracking. App settings are grouped by provider so the Home Assistant configuration stays compact as provider sections.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

The shared status model is inspired by the MIT licensed Home Assistant parcel integrations [ha-parcel-integrations](https://github.com/ha-parcel-integrations).
:::

## Former Provider Roadmap (Archive)

The following items describe the previous development state and earlier plans. This roadmap will no longer be implemented:

- DHL: active through `dhllogin://` browser login code plus optional manual tracking numbers
- Amazon: prepared with e-mail, password and optional OTP token
- Hermes: currently active by manual tracking number; account login with app username and app password is planned
- UPS: prepared with app username, app password and manual tracking numbers
- GLS: prepared with manual tracking numbers and delivery postal code; polling waits for a stable guest bearer session
- DPD: prepared with username, password and manual tracking numbers after the stable login/session flow is mapped
- Deutsche Post letters and FedEx: prepared with manual tracking numbers for later connectors

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
