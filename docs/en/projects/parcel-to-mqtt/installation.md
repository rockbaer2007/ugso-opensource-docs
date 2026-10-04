# Installation

::: warning Archive: development discontinued
These instructions describe the existing package. Parcel Tracker is already much further along, so we are discontinuing development of Parcel to MQTT. See [Parcel Tracker by SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker) for the alternative and its installation instructions.
:::

The existing package is in the [`parcel_to_mqtt` folder of the shared add-on repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt). In Home Assistant, add the repository URL below without `/tree/master/parcel_to_mqtt`.

[![Open Parcel to MQTT in Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Open Home Assistant.
2. Go to **Settings > Apps > App-Store**.
3. Open the three-dot menu and choose **Repositories**.
4. Add this repository URL:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

5. Install **Parcel to MQTT**.
6. Configure the DHL tracking numbers.
7. Start the app.

MQTT Discovery must be enabled in Home Assistant. An MQTT broker is required.
