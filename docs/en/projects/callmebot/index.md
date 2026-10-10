---
title: UGSo CallMeBot
description: WhatsApp text messages from Home Assistant with recipient profiles and Blockly.
---
# UGSo CallMeBot

Experimental **HA App 0.1.1** in the [same repository as Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot). Complete **DE/EN/FR** interface and blocks, system language and light/dark/system appearance. Inspired by [ioBroker.whatsapp-cmb](https://github.com/ioBroker/ioBroker.whatsapp-cmb); original UGSo implementation without ioBroker.

**Fix in 0.1.1:** Sending works without `crypto.randomUUID`, including HTTP Ingress. Restart the app and reload the page after updating. Request IDs use random bytes when available or a timestamp/counter fallback; they deduplicate requests and are not authentication tokens.

![English CallMeBot interface](/assets/callmebot/en.png)

## Installation and setup

1. Add `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` to the HA App Store.
2. Install **UGSo CallMeBot**, configure the MQTT broker and start the app.
3. Open the Ingress UI. Supervisor MQTT credentials take priority; app options are the fallback.
4. Activate your own recipient using the current bot number from the [official activation guide](https://www.callmebot.com/blog/free-api-whatsapp-messages/). Send exactly `I allow callmebot to send me messages`.
5. Save a profile ID, name, activated phone number **with + and country code**, and its matching API key. Select a default. Up to 16 profiles.
6. The test button really sends to the selected saved profile; an empty selection uses the default.

A blank key field preserves the stored key. Keys are never returned to the UI. They remain in `/data/profiles.json`, outside Blockly, MQTT messages, browser storage and logs. This backend file is not encrypted and is included in HA backups.

## CallMeBot Blockly block

Since **Blocks for HA 0.1.48**, under **Messages → WhatsApp · CallMeBot**.

![CallMeBot block](/assets/blocks-for-ha/blocks/en/ugso_callmebot_action.png)

Enter a profile ID or leave it empty for the default. Connect text, a variable or Jinja as the message. Logging: errors only, none or info. Exports native `mqtt.publish`, serializing JSON after template evaluation so quotes and newlines remain valid.

HA requires MQTT. JSON projects preserve the dedicated block. YAML imports back as a general HA/MQTT action.

## Alternative: existing WhatsApp integration

![WhatsApp integration block](/assets/blocks-for-ha/blocks/en/ugso_whatsapp_action.png)

The second block calls [FaserF’s WhatsApp integration](https://faserf.github.io/ha-whatsapp/services.html). Configure its app URL and **API token from the WhatsApp app** once in the HA setup dialog. The integration manages this token; the block does not need it.

Select `whatsapp.send_message · number` for the older format, `whatsapp.send_message · target` for the current documentation, or `notify.whatsapp` if configured. Recipient: **country code without +**. Message: text/Jinja. The optional account is exported for `whatsapp.send_message` only. Matching YAML imports as the dedicated block; extra options remain in the general HA action.

This alternative requires neither the CallMeBot app nor a CallMeBot key. The existing integration handles installation and WhatsApp connectivity.

## MQTT protocol and limits

- Send: `ugso/callmebot/send`, QoS 0, **retain false**.
- Payload: `{"profile":"default","message":"Hello from HA","loglevel":"errors"}`. Empty/omitted profile uses the default.
- Optional `request_id`: one-hour deduplication per profile, keeping up to 1000 IDs.
- Result: `ugso/callmebot/result`, non-retained profile, request ID, status and timestamp; no message or key.
- Availability: `ugso/callmebot/availability`, retained `online`/`offline` for the broker connection.
- Maximum 4000 characters, queue of 20, at least 10 seconds between attempts per profile. Faster commands are rejected, not delayed.
- No automatic provider retries or replay after restart. Retained send commands are rejected.
- One MQTT namespace/client ID: one app instance per broker. Restrict send-topic write permissions. This preview uses the internal broker; external TLS configuration is not included.

CallMeBot Free is for personal texts to your own activated numbers. No groups, media, replies or delivery confirmation. `accepted` confirms API acceptance only. Phone, key and text are transmitted over HTTPS to CallMeBot. Source: [CallMeBot activation and API](https://www.callmebot.com/blog/free-api-whatsapp-messages/).

## Verification

Docker build/start, mock-provider backend tests, MQTT protocol, DE/EN/FR UI, mobile layout and Blockly export were checked. Real WhatsApp delivery and HA Supervisor installation still require verification with your own setup. No real messages were sent.

[Source and local test commands](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot) · Apache-2.0 · Independent community project.
