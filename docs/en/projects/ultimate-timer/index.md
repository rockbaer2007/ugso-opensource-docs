---
layout: home

hero:
  name: Ultimate Timer
  text: Home Assistant Blueprint V3.2.4
  tagline: Powerful hybrid timer with stable STOP logic, persistent DONE status, multi-instance support and MQTT.
  actions:
    - theme: brand
      text: Import into Home Assistant
      link: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/rockbaer2007/ha-ultimate-timer-blueprint/main/blueprints/automation/ultimate_timer_v3_2_4.yaml
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/ha-ultimate-timer-blueprint

features:
  - icon: timer
    title: Flexible Duration
    details: Timer duration in hh:mm:ss format.

  - icon: stop
    title: Reliable STOP
    details: The timer can be stopped cleanly at any time.

  - icon: target
    title: Persistent DONE Status
    details: DONE remains active until the daily reset runs.

  - icon: repeat
    title: Multi-Instance
    details: Multiple independent timers can run in parallel.

  - icon: shuffle
    title: Helper or MQTT
    details: State management through Home Assistant helpers or MQTT.

  - icon: shield
    title: Stable Flow
    details: Revised RUNNING and STOP logic without overwriting each other.
---

## Overview

**Ultimate Timer V3.2.4 FINAL CLEAN** is a Home Assistant automation blueprint
for reusable timers.

Typical use cases:

- pool and pond pumps
- irrigation
- watchdogs
- delayed workflows
- time-controlled devices
- reusable dashboard timers

[Go directly to installation](./installation)

## Preview

![Blueprint configuration](/images/ultimate-timer/preview_blueprint.png)
