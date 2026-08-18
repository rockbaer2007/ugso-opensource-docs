---
layout: home

hero:
  name: Heizöl to MQTT
  text: Heating-oil prices for Home Assistant
  tagline: Query public Esyoil and Heizöl24 price calculators and publish best prices plus provider offers through MQTT Discovery.
  actions:
    - theme: brand
      text: Installation
      link: /en/projects/heizoel-to-mqtt/installation
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/heizoel-to-mqtt

features:
  - icon: 🛢️
    title: Heating-oil prices
    details: Fetch best prices for configured postal code, amount and delivery options.

  - icon: 📍
    title: Germany and Austria
    details: Price lookups for German and Austrian postal codes.

  - icon: 🧾
    title: Provider offers
    details: Up to six provider offers per source and amount with price per liter, price per 100 liters and total price.

  - icon: 🔎
    title: Esyoil and Heizöl24
    details: Public price calculator endpoints are queried and normalized.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant creates price, provider and status entities automatically.

  - icon: 🧰
    title: Diagnostics
    details: Optional masked provider logging for testing and troubleshooting.
---

## Overview

Heizöl to MQTT is a Home Assistant app that publishes heating-oil prices through MQTT Discovery.

The app queries public price calculator endpoints and normalizes the best offer per source and amount. It is intended for Germany and Austria only.

::: info Origin
This implementation is adapted from and inspired by the ioBroker adapter [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel).
:::

## Status

The app is testable in Home Assistant and publishes values through MQTT Discovery. It supports best-price entities and up to six provider offers per source and amount.

The used price endpoints are public website endpoints and not officially documented stable APIs.

## Pages

- [Installation](./installation)
- [Configuration](./configuration)
- [Entities](./entities)
- [Examples](./examples)
