# Parcel to MQTT

<img src="/images/parcel-to-mqtt-icon.svg" alt="Parcel to MQTT Icon" width="96">

Parcel to MQTT ist eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery in Home Assistant bereitstellt.

Die aktuelle Version nutzt direkte DHL- und Hermes-Paketverfolgung mit manuell konfigurierten Sendungsnummern. Benachrichtigungen werden bewusst nicht in der App selbst verschickt, sondern über normale Home-Assistant-Automationen auf Basis der erzeugten Entitäten gebaut.

::: info Ursprung
Die Umsetzung ist adaptiert von und inspiriert durch den ioBroker-Adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

Das gemeinsame Statusmodell ist inspiriert durch die MIT-lizenzierten Home-Assistant-Paketintegrationen [ha-parcel-integrations](https://github.com/ha-parcel-integrations).
:::

## Funktionen

- direkte DHL-Paketverfolgung
- direkte Hermes-Deutschland-Paketverfolgung
- mehrere Sendungsnummern als kommagetrennte Listen
- GLS-Konfiguration ist vorbereitet, GLS Deutschland ist aber noch nicht aktiv, da dafür eine Guest-Bearer-Session benötigt wird
- DPD und UPS sind als nächste Provider-Ziele vorgesehen
- MQTT Discovery für Home Assistant
- Zähler für Gesamt, angemeldet, unterwegs, in Zustellung, Abholstelle, zugestellt, Rücksendung, Problem und unbekannt
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
