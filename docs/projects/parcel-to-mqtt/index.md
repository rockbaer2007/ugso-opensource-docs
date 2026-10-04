---
layout: home

hero:
  name: Parcel to MQTT
  text: Entwicklung eingestellt
  tagline: Parcel Tracker ist bereits deutlich weiter entwickelt. Deshalb stellen wir die Weiterentwicklung von Parcel to MQTT ein. Die bisherige Dokumentation bleibt als Archiv erhalten.
  actions:
    - theme: brand
      text: Parcel Tracker ansehen
      link: https://github.com/SoerenKaiser99/parcel_tracker
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt

features:
  - icon: 📦
    title: Paketstatus
    details: Paketstatus, letztes Ereignis, Ziel und Sendungsnummer als Home-Assistant-Entitäten.

  - icon: 🚚
    title: DHL und Hermes aktiv
    details: DHL-Kontoliste, manuelle DHL-Sendungsnummern und Hermes-Sendungsverfolgung.

  - icon: 🧩
    title: Anbieterbereiche
    details: Gruppierte Einstellungen für DHL, Hermes, GLS, DPD, UPS, Amazon Logistics, Deutsche Post Briefe und FedEx.

  - icon: 📊
    title: Zähler und Slots
    details: Zähler für Gesamt, unterwegs, in Zustellung, Abholstelle, zugestellt, Rücksendung, Problem und unbekannt.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant legt Paket-, Status- und Zähler-Entitäten automatisch an.

  - icon: 🔔
    title: Automationen
    details: Benachrichtigungen werden über normale Home-Assistant-Automationen auf Basis der erzeugten Entitäten gebaut.
---

::: warning Entwicklung eingestellt
Parcel Tracker ist bereits deutlich weiter entwickelt. Deshalb stellen wir die Weiterentwicklung von Parcel to MQTT ein und empfehlen Interessierten einen Blick auf [Parcel Tracker von SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker).

Quellcode und bisherige Dokumentation bleiben als Archiv erhalten. Die folgenden Funktionen und Anleitungen beschreiben den letzten Stand unseres Pakets.
:::

## Überblick

Parcel to MQTT ist eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery in Home Assistant bereitstellt.

Die aktuelle Version nutzt DHL-Konto-Paketlisten, optionale manuelle DHL-Sendungsnummern und Hermes-Paketverfolgung. Die App-Einstellungen sind nach Dienstleistern gruppiert, damit die Home-Assistant-Konfiguration kompakt als Anbieterbereiche erscheint.

::: info Ursprung
Die Umsetzung ist adaptiert von und inspiriert durch den ioBroker-Adapter [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

Das gemeinsame Statusmodell ist inspiriert durch die MIT-lizenzierten Home-Assistant-Paketintegrationen [ha-parcel-integrations](https://github.com/ha-parcel-integrations).
:::

## Frühere Provider-Roadmap (Archiv)

Die folgenden Punkte beschreiben den bisherigen Entwicklungsstand und frühere Pläne. Diese Roadmap wird nicht mehr umgesetzt:

- DHL: aktiv über `dhllogin://` Browser-Login-Code plus optionale manuelle Sendungsnummern
- Amazon: vorbereitet mit E-Mail, Passwort und optionalem OTP-Token
- Hermes: aktuell per manueller Sendungsnummer aktiv; Konto-Login mit App-Username und App-Passwort ist geplant
- UPS: vorbereitet mit App-Username, App-Passwort und manuellen Sendungsnummern
- GLS: vorbereitet mit manuellen Sendungsnummern und Liefer-Postleitzahl; Polling wartet auf eine stabile Guest-Bearer-Session
- DPD: vorbereitet mit Username, Passwort und manuellen Sendungsnummern, sobald der stabile Login-/Session-Ablauf sauber abgebildet ist
- Deutsche Post Briefe und FedEx: vorbereitet mit manuellen Sendungsnummern für spätere Connectoren

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
- [Beispiele](./beispiele)
