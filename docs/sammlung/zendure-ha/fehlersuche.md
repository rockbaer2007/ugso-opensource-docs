---
title: Zendure HA Fehlersuche
description: Fehlersuche bei Verbindungsproblemen mit der Zendure Home Assistant Integration.
---
# Fehlersuche

## Grundcheck

1. Integration auf die aktuelle Version aktualisieren.
2. Home Assistant neu starten.
3. Prüfen, ob der Zendure-App-Token aus dem Hauptkonto stammt.
4. Prüfen, ob Geräte in der Zendure-App sichtbar sind.
5. Debug-Logging für die Zendure Integration aktivieren.
6. Bei lokalem MQTT: Broker-Adresse, Benutzer, Passwort, WLAN-SSID und WLAN-Passwort prüfen.

## Häufige Fehlermeldungen

| Meldung | Bedeutung / Maßnahme |
| --- | --- |
| Token ungültig | Token erneut aus der Zendure-App kopieren |
| Keine Geräte gefunden | falsches Zendure-Konto oder falsche Region prüfen |
| Kein MQTT-Server zurückgegeben | lokales oder Cloud-MQTT in der Zendure-App prüfen |
| Keine Sicherungsgruppe | Fuse Group setzen |
| HEMS | Gerät wird durch HEMS beeinflusst und kann vom Manager nicht frei geregelt werden |

## Hyper2000 / Legacy-Geräte

Bei Verbindungsproblemen empfiehlt die Original-Wiki:

1. Debug-Logging aktivieren.
2. Integrations-Eintrag löschen.
3. Gerät neu starten.
4. Integration aktualisieren.
5. Integration mit Zendure-App-Token neu hinzufügen.
6. MQTT-Logging aktivieren.
7. Lokales MQTT mit allen Feldern einrichten.
8. Zunächst `cloud` als Verbindungsmodus testen.
9. Fuse Group setzen.
10. Prüfen, ob das Gerät eine Bluetooth-MAC-Adresse hat.
11. Mindestens 10 Minuten warten, weil Updates über Bluetooth zeitverzögert sein können.

## Wenn das Gerät nicht reagiert

- Betriebsmodus `Manuelle Leistungsregelung` wählen.
- `Manuelle Leistung` testweise ändern, zum Beispiel 300 W und danach 400 W.
- Danach `Smarte Leistungsregelung` testen.
- Wenn keine Reaktion kommt, vollständiges Debug-Log sichern.

Original-Wiki:

- [Troubleshooting](https://github.com/Zendure/Zendure-HA/wiki/Troubleshooting)

