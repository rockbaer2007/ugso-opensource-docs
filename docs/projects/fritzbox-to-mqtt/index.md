# FRITZ!Box to MQTT

FRITZ!Box to MQTT ist eine Home-Assistant-App, die Daten aus einer FRITZ!Box per MQTT Discovery in Home Assistant bereitstellt.

Die App nutzt mehrere Quellen, weil nicht jede FRITZ!Box dieselben Schnittstellen gleich ausliefert:

- TR-064 für viele FRITZ!Box-Dienste
- FRITZ!Box-Web-/Lua-Abfragen als Fallback
- den Live-Anrufmonitor auf Port `1012`
- MQTT Discovery für die automatische Entitätserstellung in Home Assistant

::: info HACS
Dieses Projekt ist eine Home-Assistant-Supervisor-App. HACS installiert Custom Integrations und Frontend-Karten, aber keine Docker-basierten Supervisor-Apps. Die Installation erfolgt deshalb über die App-Repository-Funktion von Home Assistant.
:::

## Funktionen

- Anrufbeantworter `AB0` bis `AB4` mit neuen und alten Nachrichten, Status und Ein/Aus-Schalter.
- WLAN-Schalter für 2,4 GHz, 5 GHz und Gast-WLAN, sofern die FRITZ!Box sie bereitstellt.
- WAN-Verbindungsdaten, Uploadrate, Downloadrate und Linkstatus.
- Externe IPv4- und IPv6-Adresse, sofern verfügbar.
- Box-Status wie Mesh-Rolle, PPP-Verbindung, DECT-Basis und DNS over TLS.
- Anruflisten für alle, eingehende, ausgehende, verpasste, abgewiesene und gesperrte Anrufe.
- Live-Anrufmonitor mit `RING`, `CALL`, `CONNECT` und `DISCONNECT`.
- Telefonbücher mit auswählbarer Anzeige.
- Optionale DECT-Handset-Sensoren für interne Nummer und Geräte-ID.

## Repository

[FRITZ!Box to MQTT auf GitHub öffnen](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## Community

Discord-Kanal: `#fritzbox-to-mqtt`

## Weitere Seiten

- [Installation](./installation)
- [Konfiguration](./konfiguration)
- [Entitäten](./entitaeten)
- [Fehlersuche](./fehlersuche)
