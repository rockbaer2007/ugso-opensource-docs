---
layout: home

hero:
  name: Heizöl to MQTT
  text: Heizölpreise für Home Assistant
  tagline: Öffentliche Preisrechner von Esyoil und Heizöl24 abfragen und Bestpreise sowie Anbieter-Angebote per MQTT Discovery veröffentlichen.
  actions:
    - theme: brand
      text: Installation
      link: /projects/heizoel-to-mqtt/installation
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/heizoel-to-mqtt

features:
  - icon: 🛢️
    title: Heizölpreise
    details: Bestpreise für konfigurierte Postleitzahl, Menge und Lieferoptionen abrufen.

  - icon: 📍
    title: Deutschland und Österreich
    details: Preisabfragen für deutsche und österreichische Postleitzahlen.

  - icon: 🧾
    title: Anbieter-Angebote
    details: Bis zu sechs Anbieter-Angebote pro Quelle und Menge mit Preis pro Liter, Preis pro 100 Liter und Gesamtpreis.

  - icon: 🔎
    title: Esyoil und Heizöl24
    details: Öffentliche Preisrechner-Endpunkte werden abgefragt und normalisiert.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant legt Preis-, Anbieter- und Status-Entitäten automatisch an.

  - icon: 🧰
    title: Diagnose
    details: Optionales maskiertes Provider-Logging für Tests und Fehlersuche.
---

## Überblick

Heizöl to MQTT ist eine Home-Assistant-App, die Heizölpreise per MQTT Discovery in Home Assistant bereitstellt.

Die App fragt öffentliche Preisrechner-Endpunkte ab und normalisiert die besten Angebote pro Quelle und Liter-Menge. Sie ist nur für Deutschland und Österreich vorgesehen.

::: info Ursprung
Die Umsetzung ist adaptiert von und inspiriert durch den ioBroker-Adapter [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel).
:::

## Status

Die App ist in Home Assistant testbar und liefert Werte per MQTT Discovery. Unterstützt werden Bestpreis-Entitäten sowie bis zu sechs Anbieter-Angebote pro Quelle und Menge.

Die genutzten Preis-Endpunkte sind öffentliche Webseiten-Endpunkte und keine offiziell stabil dokumentierten APIs.

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
- [Beispiele](./beispiele)
