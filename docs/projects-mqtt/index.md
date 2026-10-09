# UGSo HA Apps

Das gemeinsame Repository ist die zentrale Veröffentlichung für alle Home-Assistant-Apps von UGSo Software: MQTT-Apps, Grafik Visual Studio, Blocks for HA und zukünftige Projekte. Jede App hat ein eigenes Unterverzeichnis, eine eigene Version und Dokumentation. Die bestehende Repository-URL bleibt erhalten.

## UGSo HA Apps und weitere Projekte

| Projekt | Dokumentation |
| --- | --- |
| [UGSo Blocks for HA](/projects/blocks-for-ha/) | Experimentelle HA-App 0.1.3: visuelle Blocks für native Automationen, YAML-Import/-Export und erweiterbare Falls-Zweige; Editor über HA-Ingress. |
| [Grafik Visual Studio](/projects/grafik-visual-studio/) | Grafischer Editor und Runtime für HA-Visualisierungen. |

Beide Projekte liegen im selben Repository wie die folgenden MQTT-Apps.

## Gemeinsames Add-on-Repository

Die MQTT-Projekte werden jetzt primär über ein gemeinsames Home-Assistant-Add-on-Repository bereitgestellt. In Home Assistant muss nur eine Repository-URL eingetragen werden; danach erscheinen die einzelnen Projekte separat im Add-on Store.

Repository-URL für Home Assistant:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Enthaltene Add-ons:

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT (Entwicklung eingestellt)
- [MQTT-Client](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client): gezielte Home-Assistant-zu-ioBroker-Übertragung per MQTT. Statt mit dem ioBroker-HASS-Adapter pauschal alle Home-Assistant-Entitäten zu spiegeln, wählst du einzelne Geräte und Werte aus; diese erscheinen in ioBroker als übersichtlicher Gerätebaum. Steuerbare Werte wie Switches, Eingaben, Slider, Selects und Taster können über `/set` wieder zurück nach Home Assistant geschaltet oder gedrückt werden. Version 0.1.14 sendet States und Attribute zuerst in kleinen Häppchen und legt die `/set`-Rückkanäle danach an, damit ioBroker den Gerätebaum sauberer aufbaut. Der bestehende HA-Broker bleibt erhalten.

- [Gemeinsames Add-on-Repository auf GitHub öffnen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons)

Die früheren Einzel-Repositories bleiben als archivierte Historie sichtbar und verweisen auf dieses gemeinsame Repository.

## FRITZ!Box to MQTT

**FRITZ!Box to MQTT**

Eine Home-Assistant-App, die FRITZ!Box-Daten per MQTT Discovery als Entitäten bereitstellt. Sie kombiniert TR-064, FRITZ!Box-Web-/Lua-Abfragen und den Live-Anrufmonitor.

- [FRITZ!Box-to-MQTT-Dokumentation öffnen](/projects/fritzbox-to-mqtt/)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## Heizöl to MQTT

**Heizöl to MQTT**

Eine Home-Assistant-App, die Heizölpreise von Esyoil und Heizöl24 per MQTT Discovery als Entitäten bereitstellt. Aktuell werden Bestpreise und bis zu sechs Anbieter-Angebote pro Quelle und Menge veröffentlicht.

- [Heizöl-to-MQTT-Dokumentation öffnen](/projects/heizoel-to-mqtt/)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/heizoel-to-mqtt)
- Adaptiert von: [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel)

## Parcel to MQTT

**Parcel to MQTT**

**Entwicklung eingestellt:** Parcel Tracker ist bereits deutlich weiter entwickelt. Deshalb stellen wir die Weiterentwicklung unseres Pakets ein. Wir empfehlen einen Blick auf [Parcel Tracker von SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker). Unsere bisherige Dokumentation bleibt als Archiv erhalten.

Eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery als Entitäten bereitstellt. Die aktuelle Version nutzt DHL-Konto-Paketlisten, optionale DHL-Sendungsnummern und Hermes-Paketverfolgung.

- [Parcel-to-MQTT-Dokumentation öffnen](/projects/parcel-to-mqtt/)
- [Paket im gemeinsamen Add-on-Repository öffnen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adaptiert von: [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## Weitere Projektbereiche

- [C# Projekte öffnen](/projects/)
- [Diverse Projekte öffnen](/projects-diverse/)
- [ATLAS öffnen](/projects/atlas/)
