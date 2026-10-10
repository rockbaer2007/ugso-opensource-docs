# UGSo HA Apps

The shared repository is the central publishing location for all UGSo Software Home Assistant apps: MQTT apps, Grafik Visual Studio, Blocks for HA and future projects. Each app has its own subdirectory, version and documentation. The existing repository URL is retained.

## UGSo HA Apps and other projects

| Project | Documentation |
| --- | --- |
| [UGSo CallMeBot](/en/projects/callmebot/) | Experimental HA App 0.1.0: recipient profiles, WhatsApp texts via MQTT, DE/EN/FR and matching Blockly blocks. |
| [UGSo Blocks for HA](/en/projects/blocks-for-ha/) | Experimental HA app 0.1.3: visual Blocks for native automations, YAML import/export and extensible branches; editor through HA ingress. |
| [Grafik Visual Studio](/en/projects/grafik-visual-studio/) | Graphical editor and runtime for HA visualizations. |

These projects live in the same repository as the MQTT apps below.

## Shared Add-on Repository

The MQTT projects are now primarily provided through a shared Home Assistant add-on repository. Home Assistant only needs one repository URL; after adding it, the individual projects appear separately in the add-on store.

Repository URL for Home Assistant:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Included add-ons:

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT (development discontinued)
- [MQTT-Client](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/mqtt_client/DOCS.en.md): selected Home Assistant to ioBroker transfer via MQTT. Instead of mirroring the full Home Assistant inventory through ioBroker's HASS adapter, you choose specific devices and values; they appear in ioBroker as a clear device tree. Controllable values such as switches, inputs, sliders, selects and buttons can use `/set` topics to switch, write or press back into Home Assistant. Version 0.1.14 publishes states and attributes first in small batches and subscribes `/set` return channels afterwards, so ioBroker can build the device tree more cleanly. The existing HA broker stays in place.

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

**Development discontinued:** Parcel Tracker is already much further along, so we are discontinuing development of our package. We recommend taking a look at [Parcel Tracker by SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker). Our existing documentation remains available as an archive.

A Home Assistant app that publishes parcel tracking data as MQTT Discovery entities. The current version uses DHL account parcel lists, optional DHL tracking numbers and Hermes parcel tracking.

- [Open the Parcel to MQTT documentation](/en/projects/parcel-to-mqtt/)
- [Open the package in the shared add-on repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt)
- [Open the archived single-project repository on GitHub](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adapted from: [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## More Project Areas

- [Open C# Projects](/en/projects/)
- [Open Misc Projects](/en/projects-diverse/)
- [Open ATLAS](/en/projects/atlas/)
