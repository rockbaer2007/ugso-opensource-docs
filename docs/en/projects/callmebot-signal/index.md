---
title: UGSo CallMeBot Signal
description: Signal text messages from Home Assistant with recipient profiles and Blockly.
---
# UGSo CallMeBot Signal

Experimental **HA app 0.1.0** in the [shared Blocks for HA repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal). Complete **DE/EN/FR**, system language and light/dark/system appearance. Original UGSo implementation inspired by [ioBroker.signal-cmb](https://github.com/derAlff/ioBroker.signal-cmb).

![Signal interface in English](/assets/callmebot-signal/en.png)

## Setup

1. Add `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` to the HA app store and install **UGSo CallMeBot Signal**.
2. Configure HA MQTT, start the app and open its Ingress UI. Supervisor MQTT credentials take priority; app options are the fallback.
3. Use the current bot contact from the [official Signal activation guide](https://www.callmebot.com/blog/free-api-signal-send-messages/). Send its activation phrase in **Signal** and wait for your **Signal API key**.
4. Save a profile ID, display name, your international phone number **with +** or **Signal UUID**, and matching key. When your number is hidden, the bot may provide a UUID. Copy the recipient value from the activation link unchanged.
5. Choose a default profile. “Send message” really sends to the selected saved profile.

WhatsApp keys do not work for Signal. Both apps can run together with isolated profiles, MQTT topics, client IDs and diagnostic entities. The [WhatsApp app](../callmebot/) retains its existing technical IDs.

## Blockly and profile selection

Since **Blocks for HA 0.1.50**: **Messages → Signal · CallMeBot**.

![Signal block](/assets/blocks-for-ha/blocks/en/ugso_callmebot_signal_action.png)

Click the profile field, search by name/ID and select. Empty uses the default recipient. The display name is shown; the profile ID is stored. Connect text, a variable or Jinja as the message. Logging: errors only, none or info. The block generates native `mqtt.publish`; JSON is serialized after template evaluation.

The app publishes a catalog on `ugso/callmebot_signal/profiles` and the MQTT discovery diagnostic entity **`sensor.ugso_callmebot_signal_profiles`**. State: profile count. Attributes: IDs, names, default and source marker, **no recipient, message or key**. Blocks uses the source marker even if the entity is renamed. Standard discovery prefix: `homeassistant`.

Without a connection, enter the profile ID manually or leave it empty. Invalid/deleted IDs are never replaced automatically. JSON projects retain the dedicated block; YAML import displays the send as a general HA/MQTT action.

## Protocol and limits

- Send: `ugso/callmebot_signal/send`, QoS 0, **retain false**.
- Example: `{"profile":"default","message":"Hello from HA","loglevel":"errors"}`. Empty profile uses the default recipient.
- Result: `ugso/callmebot_signal/result`, not retained, profile, request ID, status and time only.
- Catalog and availability: `ugso/callmebot_signal/profiles` and `ugso/callmebot_signal/availability`, retained. Availability reflects the broker connection.
- Up to 16 profiles, 4000 characters, queue of 20, at least 10 seconds between attempts per profile. Faster commands are rejected.
- Optional `request_id`: one-hour deduplication, up to 1000 IDs. No automatic retries/replay after restart; retained commands are rejected.
- One Signal app instance per broker. Restrict write access to command topics. External MQTT TLS configuration is not included.

This app sends **text messages to your own activated recipients**. Images, groups and replies are not implemented. `accepted` confirms API acceptance only. Recipient, key and message are sent over HTTPS to `https://signal.callmebot.com/signal/send.php`.

Keys stay in the private backend file `/data/profiles.json`, are never returned to browsers/MQTT/Blockly and are not logged. The file is not encrypted and is included in HA backups; protect backups accordingly.

## Verification

Backend, UUID/number validation, MQTT protocol, Blockly/Jinja export, DE/EN/FR and mobile layout are verified with test data. Real Signal delivery and HA Supervisor installation require your own setup. Automated tests never send real messages.

[Source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal) · Apache-2.0 · Independent community project.
