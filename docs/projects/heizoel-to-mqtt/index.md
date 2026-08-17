# Heizöl to MQTT

Heizöl to MQTT ist eine Home-Assistant-App, die Heizölpreise per MQTT Discovery in Home Assistant bereitstellt.

Die App fragt öffentliche Preisrechner-Endpunkte ab und normalisiert die besten Angebote pro Quelle und Liter-Menge.

::: info Ursprung
Die Umsetzung ist adaptiert von und inspiriert durch den ioBroker-Adapter [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel).
:::

## Quellen

- Esyoil
- Heizöl24 Deutschland
- Heizöl24 Österreich

## Status

Die App ist als testbares MVP gedacht. Die genutzten Preis-Endpunkte sind öffentliche Webseiten-Endpunkte und keine offiziell stabil dokumentierten APIs.

## Repository

[Heizöl to MQTT auf GitHub öffnen](https://github.com/rockbaer2007/heizoel-to-mqtt)

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
