---
layout: home

hero:
  name: Ultimate Timer
  text: Home Assistant Blueprint V3.2.4
  tagline: Leistungsstarker Hybrid-Timer mit stabiler STOP-Logik, dauerhaftem DONE-Status, Multi-Instance-Unterstützung und MQTT.
  actions:
    - theme: brand
      text: In Home Assistant importieren
      link: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/rockbaer2007/ha-ultimate-timer-blueprint/main/blueprints/automation/ultimate_timer_v3_2_4.yaml
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/ha-ultimate-timer-blueprint

features:
  - icon: ⏱️
    title: Flexible Dauer
    details: Timerdauer im Format hh:mm:ss.

  - icon: ⏹️
    title: Zuverlässiger STOP
    details: Der Timer lässt sich jederzeit sauber beenden.

  - icon: 🎯
    title: Dauerhafter DONE-Status
    details: DONE bleibt aktiv, bis der tägliche Reset ausgeführt wird.

  - icon: 🔁
    title: Multi-Instance
    details: Mehrere unabhängige Timer können parallel genutzt werden.

  - icon: 🔀
    title: Helper oder MQTT
    details: Statusverwaltung über Home-Assistant-Helper oder MQTT.

  - icon: 🛡️
    title: Stabiler Ablauf
    details: Überarbeitete RUNNING- und STOP-Logik ohne gegenseitiges Überschreiben.
---

## Übersicht

Der **Ultimate Timer V3.2.4 FINAL CLEAN** ist ein Home-Assistant-Automations-Blueprint für wiederverwendbare Timer.

Typische Einsatzbereiche:

- Pool- und Teichpumpen
- Bewässerung
- Watchdogs
- verzögerte Abläufe
- zeitgesteuerte Geräte
- wiederverwendbare Dashboard-Timer

[Direkt zur Installation](./installation)

## Vorschau

![Blueprint-Konfiguration](/images/ultimate-timer/preview_blueprint.png)
