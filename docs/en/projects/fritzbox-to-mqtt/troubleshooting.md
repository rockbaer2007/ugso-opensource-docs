# Troubleshooting

## MQTT Reports `Not authorized`

The app uses the internal MQTT service from Home Assistant. Check:

- Mosquitto broker app installed and started
- MQTT integration configured
- app restarted after Mosquitto became available

## FRITZ!Box Reports `401 Unauthorized`

Check the FRITZ!Box username, password and permissions. The user must be allowed to access the required FRITZ!Box data.

## Some Values Stay `unknown`

Not every FRITZ!Box exposes every value through the same interfaces. The app tries TR-064, service discovery and web/Lua fallbacks. If a value is missing, enable `log_value_details` and inspect the relevant log lines.

## Port `1012`

Port `1012` is only the live call monitor. Upload rate, download rate and box status do not come from port `1012`.

## HACS Does Not Find The Project

This is expected. The project is a Supervisor app and is installed through the Home Assistant App-Store as a repository, not through HACS.
