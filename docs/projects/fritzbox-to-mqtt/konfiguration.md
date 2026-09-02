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

## Wichtige Optionen

`ip` ist die feste Adresse der FRITZ!Box. Das ist besser als `fritz.box`, wenn mehrere FRITZ!Boxen im Netz vorhanden sind.

`port` ist der TR-064-Port. Standard ist `49000`.

`call_monitor_port` ist der Port des Live-Anrufmonitors. Standard ist `1012`.

Die FRITZ!Box-Abfragen sind in Gruppen aufgeteilt, damit die Box weniger belastet wird:

- `poll_interval`: WLAN, WAN und allgemeiner Box-Status, Standard `120` Sekunden
- `call_list_poll_interval`: Anruflisten, Standard `600` Sekunden
- `tam_poll_interval`: Anrufbeantworter, Standard `600` Sekunden
- `dect_poll_interval`: DECT-Status und optionale DECT-Leitungen, Standard `600` Sekunden
- `phonebook_poll_interval`: Telefonbücher, Standard `3600` Sekunden

Der Live-Anrufmonitor bleibt unabhängig davon dauerhaft aktiv und meldet Ereignisse direkt über Port `1012`.

Wenn WAN/DSL als offline erkannt wird, pausiert die App Anruflisten-,
Anrufbeantworter-, DECT- und Telefonbuchabfragen. Aktiv bleiben nur WLAN-, WAN-
und allgemeine Verbindungsstatusabfragen, damit die App erkennt, wann die
Verbindung zurück ist. Sobald WAN/DSL wieder online ist, werden die pausierten
Gruppen sofort einmal nachgezogen.
Die Diagnose-Sensoren `Abfrage Modus` und `Abfrage Hinweis` zeigen dabei an, ob
alle Abfragen laufen (`full`) oder Detailabfragen pausiert sind, während die
FRITZ!Box die Verbindung wieder aufbaut (`limited`).

## Abfragestatus in Home Assistant

Die App veröffentlicht zwei Diagnose-Sensoren für Dashboards und Automationen:

- `Abfrage Modus`: technischer Status für Automationen
- `Abfrage Hinweis`: lesbarer Hinweistext für Dashboard-Karten

MQTT-Topics:

- `fritzbox/polling/mode`
- `fritzbox/polling/message`
- `fritzbox/polling/attributes`

Mögliche Werte für `Abfrage Modus`:

- `full`: WAN/DSL ist online, alle Gruppen werden normal abgefragt
- `limited`: WAN/DSL ist offline, Detailabfragen sind pausiert
- `unknown`: der Verbindungsstatus wird gerade ermittelt

Beispiel für eine Home-Assistant-Automation:

```yaml
alias: FRITZBox Detailabfragen pausiert
trigger:
  - platform: state
    entity_id: sensor.abfrage_modus
    to: "limited"
action:
  - service: persistent_notification.create
    data:
      title: "FRITZ!Box baut Verbindung auf"
      message: "Detailabfragen sind pausiert. Sobald WAN/DSL wieder online ist, werden alle Gruppen nachgezogen."
```

Passe `entity_id` an den tatsächlichen Entity-Namen in deiner Home-Assistant-Installation an.

`phonebooks` steuert die beim Start angezeigten Telefonbücher. Nach dem ersten erfolgreichen Scan kann die Anzeige über die Home-Assistant-Select-Entität geändert werden.

`phonebook_names` überschreibt generische Telefonbuchnamen.

`include_dect_lines` aktiviert optionale DECT-Handset-Sensoren.

`log_value_details` schreibt Rohwerte und normalisierte Werte ins App-Protokoll. Für normale Nutzung kann es nach der Fehlersuche deaktiviert werden.

## MQTT

Wenn der Home-Assistant-MQTT-Dienst verfügbar ist, liest die App Broker, Port und interne Zugangsdaten automatisch aus.
