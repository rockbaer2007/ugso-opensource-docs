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

`phonebooks` controls the phonebooks shown at startup. After the first successful scan, the display can be changed through the Home Assistant select entity.

`phonebook_names` overrides generic phonebook names.

`include_dect_lines` enables optional DECT handset sensors.

`log_value_details` writes raw values and normalized values to the app log. Disable it after troubleshooting for quieter logs.

## MQTT

When the Home Assistant MQTT service is available, the app reads broker, port and internal credentials automatically.
