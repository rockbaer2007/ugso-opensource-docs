---
layout: home

hero:
  name: FRITZ!Box to MQTT
  text: Home Assistant App für FRITZ!Box-Daten
  tagline: Anruflisten, Live-Anrufe, WLAN, WAN, Telefonbücher und FRITZ!Box-Status per MQTT Discovery in Home Assistant bereitstellen.
  actions:
    - theme: brand
      text: Installation
      link: /projects/fritzbox-to-mqtt/installation
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/fritzbox-to-mqtt

features:
  - icon: 📞
    title: Anrufe und Anrufbeantworter
    details: Anruflisten, Live-Anrufmonitor und Anrufbeantworter AB0 bis AB4 als Home-Assistant-Entitäten.

  - icon: 📶
    title: WLAN und Netzwerk
    details: Schalter für 2,4 GHz, 5 GHz und Gast-WLAN sowie WAN-Verbindungsdaten, IP-Adressen und Linkstatus.

  - icon: 📚
    title: Telefonbücher
    details: Telefonbücher mit auswählbarer Anzeige und optionalen Ausschlüssen für einzelne Namen.

  - icon: 🧭
    title: Mehrere Datenquellen
    details: TR-064, FRITZ!Box-Web-/Lua-Fallbacks und der Live-Anrufmonitor werden kombiniert.

  - icon: 🏠
    title: MQTT Discovery
    details: Home Assistant legt die Sensoren und Schalter automatisch über MQTT Discovery an.

  - icon: 🛠️
    title: Fehlersuche
    details: Eigene Troubleshooting-Seite für Login, TR-064, DNS over TLS, Call Monitor und MQTT.
---

## Überblick

FRITZ!Box to MQTT ist eine Home-Assistant-App, die Daten aus einer FRITZ!Box per MQTT Discovery in Home Assistant bereitstellt.

Die App nutzt mehrere Quellen, weil nicht jede FRITZ!Box dieselben Schnittstellen gleich ausliefert:

- TR-064 für viele FRITZ!Box-Dienste
- FRITZ!Box-Web-/Lua-Abfragen als Fallback
- den Live-Anrufmonitor auf Port `1012`
- MQTT Discovery für die automatische Entitätserstellung in Home Assistant

::: info HACS
Dieses Projekt ist eine Home-Assistant-Supervisor-App. HACS installiert Custom Integrations und Frontend-Karten, aber keine Docker-basierten Supervisor-Apps. Die Installation erfolgt deshalb über die App-Repository-Funktion von Home Assistant.
:::

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
- [Beispiele](./beispiele)
- [Fehlersuche](./fehlersuche)
