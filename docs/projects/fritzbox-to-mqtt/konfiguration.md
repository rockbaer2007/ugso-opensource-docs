# Konfiguration

Beispiel:

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

## Wichtige Optionen

`ip` ist die feste Adresse der FRITZ!Box. Das ist besser als `fritz.box`, wenn mehrere FRITZ!Boxen im Netz vorhanden sind.

`port` ist der TR-064-Port. Standard ist `49000`.

`call_monitor_port` ist der Port des Live-Anrufmonitors. Standard ist `1012`.

`phonebooks` steuert die beim Start angezeigten Telefonbücher. Nach dem ersten erfolgreichen Scan kann die Anzeige über die Home-Assistant-Select-Entität geändert werden.

`phonebook_names` überschreibt generische Telefonbuchnamen.

`include_dect_lines` aktiviert optionale DECT-Handset-Sensoren.

`log_value_details` schreibt Rohwerte und normalisierte Werte ins Add-on-Protokoll. Für normale Nutzung kann es nach der Fehlersuche deaktiviert werden.

## MQTT

Wenn der Home-Assistant-MQTT-Dienst verfügbar ist, liest das Add-on Broker, Port und interne Zugangsdaten automatisch aus.
