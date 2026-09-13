# MQTT Projekte

Diese Seite sammelt die Home-Assistant-Apps von UGSo Software für MQTT Discovery und den Datenaustausch mit externen MQTT-Brokern.

## Gemeinsames Add-on-Repository

Die MQTT-Projekte werden jetzt primär über ein gemeinsames Home-Assistant-Add-on-Repository bereitgestellt. In Home Assistant muss nur eine Repository-URL eingetragen werden; danach erscheinen die einzelnen Projekte separat im Add-on Store.

Repository-URL für Home Assistant:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Enthaltene Add-ons:

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT
- [MQTT-Client](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client): ausgewählte HA-Zustände an ioBroker oder andere externe Broker senden, optional Schreibbefehle empfangen. Der bestehende HA-Broker bleibt erhalten. Version 0.1.6 gruppiert Entitäten nach Geräten, zeigt zusammengehörige Switches, Sensorwerte, Updates und States in einer Geräteansicht, ordnet `press` als `button` und `state_boolean` als `switch` ein und bietet Bidirektional für steuerbare Domains, Eingabewerte und Buttons.

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

Eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery als Entitäten bereitstellt. Die aktuelle Version nutzt DHL-Konto-Paketlisten, optionale DHL-Sendungsnummern und Hermes-Paketverfolgung.

- [Parcel-to-MQTT-Dokumentation öffnen](/projects/parcel-to-mqtt/)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adaptiert von: [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## Weitere Projektbereiche

- [C# Projekte öffnen](/projects/)
- [Diverse Projekte öffnen](/projects-diverse/)
- [ATLAS öffnen](/projects/atlas/)
