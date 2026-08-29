---
title: Zendure HA Installation
description: Installation und Einrichtung der Zendure Home Assistant Integration.
---
# Installation

## Installation über HACS

1. Home Assistant öffnen.
2. `HACS` öffnen.
3. Zu `Integrationen` wechseln.
4. `+ Explore & Download Repos` öffnen.
5. Nach `Zendure` suchen.
6. `Zendure Home Assistant Integration` herunterladen.
7. Browser neu laden, falls Home Assistant die Integration noch nicht direkt anzeigt.
8. `Einstellungen -> Geräte & Dienste -> Integration hinzufügen` öffnen.
9. Nach `Zendure` suchen und die Einrichtung starten.

Direktlink:

[Zendure Integration in Home Assistant hinzufügen](https://my.home-assistant.io/redirect/config_flow_start/?domain=zendure_ha)

## Zendure-App-Token

Die Integration nutzt einen Token aus der Zendure-App. Dieser Token sollte aus dem Hauptkonto stammen, bei dem die Geräte registriert sind.

::: warning Upgrade von älteren Versionen
Bei älteren Installationen mit zweitem Konto oder alter Anmeldung muss die alte Konfiguration entfernt und neu eingerichtet werden. Die aktuelle Integration arbeitet tokenbasiert.
:::

In der Original-Wiki ist der Token-Dialog mit Screenshot dokumentiert:

[Token-Screenshot im Original-Wiki](https://github.com/Zendure/Zendure-HA/wiki/Installation)

## Optionen im Einrichtungsdialog

| Option | Bedeutung |
| --- | --- |
| `Zendure Token` | Token aus der Zendure-App |
| `P1 Sensor für Smart Matching` | Sensor für Hausverbrauch: positiv bei Verbrauch, negativ bei Einspeisung |
| `MQTT-Kommunikation loggen` | schreibt MQTT-Kommunikation in das HA-Log, wenn Debug-Logging aktiv ist |
| `Lokales MQTT verwenden` | öffnet einen zweiten Dialog für lokale MQTT-Daten |
| `MQTT-Benutzer automatisch verwalten` | versucht MQTT-Zugangsdaten automatisch zu verwalten |
| `WLAN SSID` | WLAN-Name für die Geräteumstellung |
| `Wifi Passwort` | WLAN-Passwort für die Geräteumstellung |

## Nach der Einrichtung

Nach erfolgreicher Einrichtung erscheinen Zendure-Geräte und ihre Entitäten in Home Assistant. Bei mehreren Geräten sollte danach die [Fuse Group](./fuse-group) korrekt gesetzt werden, damit Smart-Matching und Leistungsbegrenzungen sinnvoll arbeiten.

