---
title: MQTT-Client
description: Transfer selected Home Assistant values live over MQTT and control supported entities.
---

# MQTT-Client 0.1.24 {#mqtt-client-0-1-16}

## Automatic VIS-2 states since 0.1.24

The combined ioBroker helper creates virtual states combining feedback and a return
channel. Supports switches, Light values and other enabled number/select/text
channels; dates and measurements remain read-only. Original MQTT values, settings
and existing aliases are preserved. Includes preview, automatic backup, type/limit
validation and feedback-loop protection. Warnings for missing optional states are
fixed. Prepared for JavaScript adapter **10.4.10** APIs; not yet newly tested in a
real installation.

[Setup and mapping table](./iobroker-roles.md#vis2) ·
[Release 0.1.24](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.24)

## ioBroker role mapping since 0.1.23

An optional JavaScript assigns dates, timestamps and unambiguous measurements to
matching ioBroker roles. Includes preview, backup before changes and guarded restore.
Existing values, credentials and manual specific roles are preserved. Writable
MQTT measurements use read-only aliases. Incompatible types, units and ambiguous
classes are skipped.

[Installation and complete HA → ioBroker mapping](./iobroker-roles.md) ·
[Release 0.1.23](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.23)

## New in 0.1.22

Label selection now includes the state, available standard metadata and return
channels for supported controllable entities. Switches automatically receive
`<base>/set` for `ON`/`OFF`; numbers, selects and buttons use their supported
commands. Setup sends no control commands. Retained, empty and invalid commands
are discarded.

Lights receive only channels supported by their HA capabilities:

| Channel below `<base>` | Value and return channel |
| --- | --- |
| `brightness/state`, `brightness/set` | Brightness 0–100% |
| `rgb_color/state`, `rgb_color/set` | JSON `[255,128,0]`, components 0–255 |
| `effect/state`, `effect/set` | Effect name from the reported effect list |
| `color_temp_kelvin/state`, `color_temp_kelvin/set` | Integer Kelvin within the reported limits |

`<base>` is the existing topic without `/state`. Effect lists, supported color
modes and minimum/maximum Kelvin values are read-only attributes. Manually selected
HA attributes retain their paths and units: `attribute/brightness` remains 0–255.

Under **Übertragung und TLS** (Transfer and TLS), enable **Zugehörige Mess- und
Batteriewerte desselben Geräts automatisch einbeziehen** to include related
measurements. `label_device_readings` defaults to `false`. Supported readings
are energy, voltage, current, power, temperature, humidity, battery and an existing
battery-low sensor. Matching uses the same HA device ID, never similar names.
No thresholds are invented. These additional sensors have no return channels.

Automatic metadata includes available names, device classes, units and state
classes, plus required choices and limits. Other attributes remain selectable
manually. `device_class` is transmitted as metadata; this does not automatically
change an ioBroker role such as `date`.

The transmission popup also shows automatic attributes, Light values and active
return topics with their origin. Removing a label revokes automatic values and
return channels at the next sync; queued commands are checked again before
execution. Manual selections and credentials are preserved. Old retained values
are removed only through confirmed topic cleanup.

Verified locally with simulated HA and broker; no new HA device test.
[Release 0.1.22](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.22)

## Current transmissions

Since **0.1.21**, only credentials collapse automatically. **Übertragung und TLS**
(Transmission and TLS) remains separately accessible. Equal-size **Save and connect**
and **Current transmissions** buttons remain visible in one row.

The second button opens a searchable, scrollable list of all currently selected
states and attributes, including HA-label-selected states. Duplicate states are
merged. Labelled origin badges distinguish blue **Label**, green **Manual** and
purple **Both**. Since 0.1.22, automatic standard attributes and Light values are included too.

Each row shows the name, entity ID, attribute where applicable, current value and
MQTT topic. The last successful broker acknowledgement includes the time and sent
value; unconfirmed values are marked and errors appear separately in red.
Acknowledgement proves broker acceptance, not processing by ioBroker or a target
device. The open popup refreshes every three seconds and via **Refresh**.
The overview covers the running connection and resets when it restarts. Credentials
and settings are neither changed nor displayed in this list. Tested locally with
manual/label selections, attributes, acknowledgement failures and mobile layout.
[Release 0.1.21](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.21)

**0.1.20:** Connection settings are collapsible under **Zugangsdaten** (Credentials).
The section stays open for initial setup. With a saved broker address, it
automatically collapses after loading and successfully saving. Click its title
to reopen it. Save and error messages remain visible; settings and credentials
are preserved.
[Release 0.1.20](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.20)

**0.1.19** also separates the lines in the transmission list: the name appears
above the state, selected-attribute and return-command summary. **Edit** remains
on the right. This view was also checked locally at widths of 1300 and 390 pixels.
[Release 0.1.19](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.19)

Since **0.1.18**, device popup rows separate the **name** on the first line,
**entity ID** on the second, and **target type with attribute count** on the third.
Long names and IDs wrap; the current state remains on the right. This separation
is preserved after selection changes. The layout was checked locally at widths
of 1300 and 390 pixels. Settings, credentials and selected transmissions are
preserved during the update. [Release 0.1.18](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.18)

MQTT-Client sends selected Home Assistant devices, states and attributes to an external MQTT broker, such as ioBroker's MQTT adapter. Choose the values you need instead of mirroring the entire HA inventory. The existing HA broker remains in place. The app reads HA directly; it is not a broker bridge.

[Source and configuration reference](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [Deutsche Dokumentation](/projects/mqtt-client/)

## Setup and selection

1. Add `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` to the Home Assistant app store.
2. Install and start **MQTT-Client**; amd64 and aarch64 are supported.
3. Open the web interface and save the external broker's host, port, username and password. The default port without TLS is 1883.
4. Select a device on the left. Its dialog groups entities into control, sensors, configuration and diagnostics. Search also finds entities inside devices.
5. Select the states and attributes to transfer. The checkbox on the right of a value row includes the state and all attributes; device-wide selection can include every value of that device.

Changes apply immediately. No additional HA access token is required: the app uses Supervisor access to the HA Core API. Use different client IDs and topic prefixes for multiple instances.

## Forward states using a Home Assistant label {#weiterleitung-per-label}

![Home Assistant dialog for creating a new label](/images/projects/mqtt-client/ha-label-erstellen.png)

*Home Assistant example: the label is named “zu mqtt client”. Enter the ID of the label you created in the MQTT Client.*

1. **Create the label:** In Home Assistant, go to **Settings → Areas, labels & zones → Labels** and create **zu mqtt client**, as shown.
2. **Look up the label ID:** Open **Settings → Tools → Template** (**Developer tools → Template** in older versions). Paste the template below and copy the result, for example `zu_mqtt_client`.
3. **Enter the ID in MQTT Client:** Open **MQTT-Client** from the Home Assistant sidebar. Expand **Übertragung und TLS** (Transfer and TLS). Paste the result into **HA-Label-ID für Zustandsweiterleitung**, directly below **Topic-Präfix**, and click **Speichern und verbinden** (Save and connect).
4. **Assign the label:** Open **Settings → Devices & services → Entities**, select the entity, and open its settings using the gear icon. Choose **Add label → zu mqtt client** and click **Update**.

```jinja
{{ label_id("zu mqtt client") }}
```

[Home Assistant · label_id](https://www.home-assistant.io/template-functions/label_id/)

The client checks assignments at the configured polling interval. The label forwards the state and standard metadata and enables supported return channels. Other attributes remain manually selectable. Removing the label stops automatic forwarding and revokes return channels, while manually selected entities remain active. Use retained topic cleanup to remove the last stored MQTT value if needed.

Tested on Home Assistant `.177` with a separate MQTT broker. After adding the label, the broker received `off` and `on`. After removing it, the next state change was no longer sent. [Release 0.1.17](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.17)

## Live transfer and status

After a complete initial snapshot, the app processes HA state changes live over WebSocket. Reconnecting to HA loads a fresh snapshot; reconnecting to MQTT republishes all selected values.

If the live connection fails, the existing polling mechanism remains the fallback: **every five seconds by default**, configurable using `poll_interval` from 1 to 300 seconds. Changes missed during an outage or between fallback polls cannot be reconstructed. Event queue overload is reported and requests a new synchronization.

Status separates MQTT connectivity and HA reachability and shows live/polling mode, last synchronization, last publication, publication count and sanitized error types. Credentials and message contents are not exposed there.

| MQTT topic | Contents |
| --- | --- |
| `<topic_prefix>/<device>/<value>/state` | State as text |
| `<topic_prefix>/<device>/<value>/attribute/<attribute>` | Selected attribute |
| `<topic_prefix>/<device>/<value>/set` | Return channel for supported commands |
| `<topic_prefix>/availability` | `online` after successful HA synchronization, otherwise `offline` |

The default prefix is `ha_external`. States and attributes use QoS 1 and Retain; no MQTT Discovery is generated. Initial setup publishes states and attributes before subscribing to `/set` return channels, with a default 50 ms delay between publications. `unknown` and `unavailable` pass through; missing entities produce `unavailable`.

## Commands back to HA

Return channels are enabled automatically for selected controllable entities. Sensors remain outgoing-only. Send commands to the corresponding `/set` topic **without Retain**.

| Entity | Payload |
| --- | --- |
| Toggle-like entity | `ON` or `OFF` |
| `number`, `input_number` | Numeric value |
| `select`, `input_select` | Available option name |
| `text`, `input_text` | Text |
| `button`, `input_button` | `PRESS` |
| `cover` | `OPEN`, `CLOSE`, `STOP` or `{"position":45}` |
| `light` | `{"brightness_pct":75}` |
| `fan` | `{"percentage":50}` |

Each JSON command permits only the named field and a finite number from 0 to 100. The HA device must support the function. Legacy entity-ID topics such as `ha_external/switch.plug/set` remain valid. Retained commands, stale commands and invalid contents are discarded; arbitrary HA action calls are unsupported.

## Remove obsolete retained topics

**Veraltete Retain-Topics prüfen** (review obsolete retained topics) lists recorded topics no longer used after selection, prefix or device name changes. Select topics and confirm removal; at most 100 per operation.

The app clears only its own acknowledged publications on the currently configured broker. Active and foreign topics are protected. The inventory persists in `/data/mqtt-topics.json`. Failed removals remain available for retry. There is **no automatic cleanup**. Unrecorded obsolete topics from before this update still require manual broker cleanup.

## Back up and restore settings

**Einstellungen sichern** (back up settings) downloads JSON containing broker settings, client ID, topic prefix, selection, polling interval, publication delay and custom CA. **Sicherung öffnen** (open backup) validates the file and asks before replacing settings.

The file contains **no MQTT password, client certificate, private key or HA token**. It is not encrypted. Locally stored credentials and client certificate/key are retained for the same broker. Enter them again when changing to another broker. Retained payloads are excluded; this does not replace a complete HA app backup.

## TLS with custom certificates

**Übertragung und TLS** (transfer and TLS) accepts a custom CA, client certificate and private key through PEM file upload or pasted text. Certificate and key must be provided together. Use the broker's TLS port, often 8883.

Server certificates and hostnames are always verified using system trust or a custom CA. Blank secret fields keep stored values. To remove them, enable the explicit option **Gespeicherte TLS-Zertifikate und Schlüssel entfernen** (remove stored TLS certificates and keys) and save. Invalid TLS configurations are rejected before changing settings.

## Updates and compatibility

Existing 0.1.15 settings remain valid: broker credentials, device/attribute selection, client ID, topic prefix, polling interval and publication delay are not rewritten at startup. TLS retains its previous setting; new certificate fields default to empty. Updating does not delete retained data.

Version 0.1.16 was checked with backend tests, an MQTT broker, a WebSocket counterpart, TLS client certificates, the web interface and Docker startup. Verify the actual HA installation and supported device functions in your own environment.
