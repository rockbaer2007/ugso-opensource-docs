# Parcel to MQTT

<img src="/images/parcel-to-mqtt-icon.svg" alt="Parcel to MQTT Icon" width="96">

Parcel to MQTT ist eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery in Home Assistant bereitstellt.

Die erste Version nutzt direkte DHL-Paketverfolgung mit manuell konfigurierten DHL-Sendungsnummern. Benachrichtigungen werden bewusst nicht in der App selbst verschickt, sondern über normale Home-Assistant-Automationen auf Basis der erzeugten Entitäten gebaut.

::: info Ursprung
Die Umsetzung ist adaptiert von und inspiriert durch den ioBroker-Adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).
:::

## Funktionen

- direkte DHL-Paketverfolgung
- mehrere DHL-Sendungsnummern als kommagetrennte Liste
- MQTT Discovery für Home Assistant
- Zähler für Gesamt, unterwegs, in Zustellung, zugestellt, Problem und unbekannt
- JSON-Liste aller Sendungen
- bis zu 20 Paket-Slots, standardmäßig 6
- Beispiel-Mushroom-Card
- Benachrichtigungen über Home Assistant Automationen

## Repository

[Parcel to MQTT auf GitHub öffnen](https://github.com/rockbaer2007/parcel-to-mqtt)

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
- [Beispiele](./beispiele)
