---
title: MQTT-Client
description: Transfer selected Home Assistant values live over MQTT and control supported entities.
---

# MQTT-Client 0.1.16

MQTT-Client sends selected Home Assistant devices, states and attributes to an external MQTT broker, such as ioBroker's MQTT adapter. Choose the values you need instead of mirroring the entire HA inventory. The existing HA broker remains in place. The app reads HA directly; it is not a broker bridge.

[Source and configuration reference](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [Deutsche Dokumentation](/projects/mqtt-client/)

## Setup and selection

1. Add `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` to the Home Assistant app store.
2. Install and start **MQTT-Client**; amd64 and aarch64 are supported.
3. Open the web interface and save the external broker's host, port, username and password. The default port without TLS is 1883.
4. Select a device on the left. Its dialog groups entities into control, sensors, configuration and diagnostics. Search also finds entities inside devices.
5. Select the states and attributes to transfer. The checkbox on the right of a value row includes the state and all attributes; device-wide selection can include every value of that device.

Changes apply immediately. No additional HA access token is required: the app uses Supervisor access to the HA Core API. Use different client IDs and topic prefixes for multiple instances.

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
