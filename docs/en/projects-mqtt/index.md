# MQTT Projects

This page collects UGSo Software Home Assistant apps for MQTT Discovery and data exchange with external MQTT brokers.

## Shared Add-on Repository

The MQTT projects are now primarily provided through a shared Home Assistant add-on repository. Home Assistant only needs one repository URL; after adding it, the individual projects appear separately in the add-on store.

Repository URL for Home Assistant:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Included add-ons:

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT
- [MQTT-Client](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/mqtt_client/DOCS.en.md): export selected HA states to ioBroker or other external brokers, with optional write commands. The existing HA broker stays in place. Version 0.1.4 shows friendly names first, keeps sensor-like values outgoing-only and offers bidirectional commands for controllable domains and value inputs such as `input_number`, `number`, `input_select`, `select`, `input_text` and `text`.

- [Open the shared add-on repository on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons)

The former single-project repositories remain visible as archived history and point to this shared repository.

## FRITZ!Box to MQTT

**FRITZ!Box to MQTT**

A Home Assistant app that publishes FRITZ!Box data as MQTT Discovery entities. It combines TR-064, FRITZ!Box web/Lua queries and the live call monitor.

- [Open the FRITZ!Box to MQTT documentation](/en/projects/fritzbox-to-mqtt/)
- [Open the archived single-project repository on GitHub](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## Heizöl to MQTT

**Heizöl to MQTT**

A Home Assistant app that publishes heating-oil prices from Esyoil and Heizöl24 as MQTT Discovery entities. It currently publishes best prices and up to six provider offers per source and amount.

- [Open the Heizöl to MQTT documentation](/en/projects/heizoel-to-mqtt/)
- [Open the archived single-project repository on GitHub](https://github.com/rockbaer2007/heizoel-to-mqtt)
- Adapted from: [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel)

## Parcel to MQTT

**Parcel to MQTT**

A Home Assistant app that publishes parcel tracking data as MQTT Discovery entities. The current version uses DHL account parcel lists, optional DHL tracking numbers and Hermes parcel tracking.

- [Open the Parcel to MQTT documentation](/en/projects/parcel-to-mqtt/)
- [Open the archived single-project repository on GitHub](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adapted from: [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## More Project Areas

- [Open C# Projects](/en/projects/)
- [Open Misc Projects](/en/projects-diverse/)
- [Open ATLAS](/en/projects/atlas/)
