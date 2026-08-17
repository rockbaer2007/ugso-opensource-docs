# Entities

Entities are created through MQTT Discovery.

## Answering Machines

For detected answering machines, entities from `AB0` to `AB4` are created:

- new messages
- old messages
- status
- on/off switch

The FRITZ!Box answering machine name is exposed as an attribute and is not used for the entity names.

## WLAN

Depending on the FRITZ!Box, these entities are created:

- WLAN 2.4 GHz on/off
- WLAN 2.4 GHz status
- WLAN 5 GHz on/off
- WLAN 5 GHz status
- guest WLAN on/off
- guest WLAN status

The WLAN status sensors show `Ein` or `Aus`; the raw FRITZ!Box status is kept as an attribute.

## WAN And Box Status

- connection download
- connection upload
- download rate
- upload rate
- WAN link status
- box mesh role
- box PPP connection
- box PPP IPv4 external
- box IPv6 external
- box DECT
- box DNS over TLS

`WAN link status` also shows `Ein` or `Aus`.

Optional values that are not exposed by the FRITZ!Box are hidden or published as `unknown`.

## Call Lists And Live Monitor

Configurable call lists:

- all calls
- incoming calls
- outgoing calls
- missed calls
- rejected calls
- blocked calls

The live call monitor publishes events such as `RING`, `CALL`, `CONNECT` and `DISCONNECT`.

## Phonebooks

Phonebooks are shown with their detected FRITZ!Box names. Tellows block lists can be hidden through name filters or renamed through `phonebook_names`.

## DECT

Optionally, each detected DECT handset publishes:

- internal number
- device ID

`NoRingTime` is intentionally no longer published.
