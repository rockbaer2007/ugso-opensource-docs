---
title: Zendure HA Fuse Group
description: Fuse Group und Leistungsgrenzen in der Zendure Home Assistant Integration.
---
# Fuse Group

Die Fuse Group ist eine Sicherheits- und Steuergruppierung. Sie beschreibt, welche Zendure-Geräte an derselben Sicherung beziehungsweise demselben Stromkreis hängen und welche maximale Leistung dort zulässig ist.

::: danger Verantwortung
Die korrekte Auswahl der Fuse Group ist sicherheitsrelevant. Wähle sie passend zu deiner Elektroinstallation und den lokalen Vorschriften.
:::

## Warum sie wichtig ist

Der Zendure Manager verteilt Leistung anhand der Fuse-Group-Einstellung. Geräte in derselben Gruppe sollen zusammen die gesetzte Grenze nicht überschreiten.

Ohne passende Fuse Group wird ein Gerät für Smart-Funktionen nicht verwendet.

## Typische Optionen

| Option | Bedeutung |
| --- | --- |
| `Nicht verwendet` | Gerät hat keine Fuse Group und wird nicht fürs Smart Matching genutzt |
| `Eigener Stromkreis / eigene Phase` | Gerät hängt allein an einem eigenen Stromkreis |
| `Sicherungsgruppe max. 800 W` | Gruppe mit maximal 800 W |
| `Sicherungsgruppe max. 1200 W` | Gruppe mit maximal 1200 W |
| `Sicherungsgruppe max. 2000 W` | Gruppe mit maximal 2000 W |
| `Sicherungsgruppe max. 2400 W` | Gruppe mit maximal 2400 W |
| `Sicherungsgruppe max. 3600 W` | Gruppe mit maximal 3600 W |
| `Sicherungsgruppe max. 4000 W` | Gruppe mit maximal 4000 W |
| `Sicherungsgruppe max. 5000 W` | Gruppe mit maximal 5000 W |

## Verbindungstatus

Die Integration zeigt einen Verbindungsstatus, der bei der Einordnung hilft:

| Status | Bedeutung |
| --- | --- |
| `Unbekannt` | kein klarer Verbindungszustand |
| `Kalibrierung` | Gerät kalibriert |
| `HEMS` | Gerät wird durch HEMS beeinflusst |
| `Keine Sicherungsgruppe` | Fuse Group fehlt |
| `Verbunden (Cloud)` | Verbindung über Cloud |
| `Verbunden (Local)` | Verbindung über lokales MQTT |
| `Verbunden (zenSDK)` | Verbindung über zenSDK |

Original-Wiki:

- [Fuse Group](https://github.com/Zendure/Zendure-HA/wiki/Fuse-Group)

