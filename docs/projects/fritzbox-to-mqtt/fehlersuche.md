# Fehlersuche

## MQTT meldet `Not authorized`

Die App nutzt den internen MQTT-Dienst von Home Assistant. Prüfe:

- Mosquitto-Broker-App installiert und gestartet
- MQTT-Integration eingerichtet
- App neu gestartet, nachdem Mosquitto verfügbar ist

## FRITZ!Box meldet `401 Unauthorized`

Prüfe Benutzername, Passwort und Berechtigungen des FRITZ!Box-Benutzers. Der Benutzer muss auf die benötigten FRITZ!Box-Daten zugreifen dürfen.

## Einzelne Werte bleiben `unknown`

Nicht jede FRITZ!Box liefert alle Werte über dieselben Schnittstellen. Die App probiert TR-064, Service-Discovery und Web-/Lua-Fallbacks. Wenn ein Wert fehlt, `log_value_details` aktivieren und die relevanten Logzeilen prüfen.

## Port `1012`

Port `1012` ist nur der Live-Anrufmonitor. Uploadrate, Downloadrate und Box-Status kommen nicht über Port `1012`.

## HACS findet das Projekt nicht

Das ist erwartet. Das Projekt ist eine Supervisor-App und wird über den Home-Assistant-App-Store als Repository installiert, nicht über HACS.
