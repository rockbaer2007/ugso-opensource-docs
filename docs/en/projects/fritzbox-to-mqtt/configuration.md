# Configuration

Example:

```yaml
ip: 192.168.178.1
port: 49000
user: homeassistant
password: secret
call_lists: all,incoming,outgoing,missed,rejected,blocked
phonebooks: all
phonebook_names: 3:tellows Sperrliste 7,4:tellows Sperrliste 8-9
phonebook_name_excludes: ""
poll_interval: 120
call_list_poll_interval: 600
tam_poll_interval: 600
dect_poll_interval: 600
phonebook_poll_interval: 3600
call_monitor_enabled: true
call_monitor_port: 1012
max_calls: 20
max_live_events: 20
include_dect_lines: false
max_dect_lines: 6
dns_over_tls_enabled: true
log_value_details: true
```

## Important Options

`ip` is the fixed FRITZ!Box address. This is more reliable than `fritz.box` when several FRITZ!Box devices exist in the network.

`port` is the TR-064 port. The default is `49000`.

`call_monitor_port` is the live call monitor port. The default is `1012`.

FRITZ!Box polling is split into groups to reduce load on the box:

- `poll_interval`: WLAN, WAN and general box status, default `120` seconds
- `call_list_poll_interval`: call lists, default `600` seconds
- `tam_poll_interval`: answering machines, default `600` seconds
- `dect_poll_interval`: DECT status and optional DECT lines, default `600` seconds
- `phonebook_poll_interval`: phonebooks, default `3600` seconds

The live call monitor stays active independently and reports events directly through port `1012`.

When WAN/DSL appears offline, the app pauses call list, answering machine, DECT
and phonebook polling. Only WLAN, WAN and general connection status polling
remain active so the app can detect when the connection returns. Once WAN/DSL is
online again, the paused groups are refreshed immediately.
The diagnostic sensors `Abfrage Modus` and `Abfrage Hinweis` show whether all
polling is active (`full`) or detail polling is paused while the FRITZ!Box
reconnects (`limited`).

`phonebooks` controls the phonebooks shown at startup. After the first successful scan, the display can be changed through the Home Assistant select entity.

`phonebook_names` overrides generic phonebook names.

`include_dect_lines` enables optional DECT handset sensors.

`log_value_details` writes raw values and normalized values to the app log. Disable it after troubleshooting for quieter logs.

## MQTT

When the Home Assistant MQTT service is available, the app reads broker, port and internal credentials automatically.
