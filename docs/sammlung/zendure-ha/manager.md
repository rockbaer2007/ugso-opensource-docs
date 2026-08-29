---
title: Zendure Manager
description: Betriebsarten und Leistungsregelung des Zendure Managers.
---
# Zendure Manager

Der Zendure Manager versucht, über die Zendure-Geräte den P1-/Hausverbrauchssensor in Richtung `0 W` zu regeln. Dafür steuert er Lade- und Entladeleistung der Geräte.

::: warning HEMS und App-Programme
Wenn Zendure Manager und HEMS oder ein Energieprogramm in der Zendure-App gleichzeitig regeln, können sie gegeneinander arbeiten. Nutze nur eine aktive Regelstrategie.
:::

## P1-Sensor

Der P1-Sensor sollte den Hausverbrauch liefern:

- positiver Wert: Haus verbraucht Netzstrom
- negativer Wert: Haus speist ein

Dieser Sensor ist die Grundlage für Smart Matching.

## Betriebsarten

| Modus | Bedeutung |
| --- | --- |
| `Aus` | Manager steuert keine Geräte |
| `Manuelle Leistungsregelung` | fester Leistungswert über `Manuelle Leistung` |
| `Smarte Leistungsregelung` | versucht den P1-Sensor auf 0 W zu halten |
| `Smartes nur Entladen` | wie Smart Matching, aber ohne Laden |
| `Smartes nur Laden` | lädt nur, entlädt nicht |
| `Solar speichern` | speichert Solar-/Offgrid-Eingang bevorzugt in Batterien |

## Manuelle Leistung

Bei `Manuelle Leistungsregelung` bestimmt die Entität `Manuelle Leistung`, wie viel Leistung ein- oder ausgespeist werden soll.

- positiver Wert: Batterie entlädt in Richtung Haus/Grid
- negativer Wert: Batterie lädt, wenn das Gerät AC-Laden unterstützt

## Smart Matching

Bei Smart Matching verteilt der Manager Leistung auf die verfügbaren Geräte. Dabei spielen Fuse Group, Ladezustand, Mindest-SoC, Maximalleistung und Gerätestatus eine Rolle.

Die Original-Wiki beschreibt die Verteilungslogik als teilweise veraltet. Deshalb sollte diese Seite als Orientierung verstanden und bei Bedarf gegen den aktuellen Code geprüft werden.

Original-Wiki:

- [Function description](https://github.com/Zendure/Zendure-HA/wiki/Function-description)
- [Power distribution strategy](https://github.com/Zendure/Zendure-HA/wiki/Power-distribution-strategy)

