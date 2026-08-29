---
title: Zendure Home Assistant Integration
description: Inoffizielle deutsche Dokumentation zur Zendure Home Assistant Integration.
---
# Zendure Home Assistant Integration

Die Zendure Home Assistant Integration bindet Zendure-Geraete in Home Assistant ein. Sie stellt gemeldete Werte als Entitaeten bereit, ermoeglicht Steuerwerte wie Lade- und Ausgangsgrenzen und bietet mit dem Zendure Manager eine Leistungsregelung anhand eines P1-/Hausverbrauchssensors.

::: warning Inoffizielle deutsche Dokumentation
Diese Dokumentation ist eine unabhaengige deutsche Aufbereitung. Massgeblich bleiben das Originalprojekt und die Original-Wiki.
:::

## Projektstand

| Feld | Wert |
| --- | --- |
| Originalprojekt | [zendure/zendure-ha](https://github.com/zendure/zendure-ha) |
| Original-Wiki | [Zendure-HA Wiki](https://github.com/Zendure/Zendure-HA/wiki) |
| Dokumentierter Repo-Stand | `master`, geprüft am 29.08.2026 |
| Letzte Tags im Repo | `1.4.4`, `1.4.4-pre1` |
| Mindestversion laut README | Home Assistant `2025.5+` |
| Mindestversion laut HACS-Datei | Home Assistant `2025.4.0` |
| Lizenz | MIT |
| Integration-Domain | `zendure_ha` |

## Unterstützte Geräte laut Originaldoku

- Ace1500
- Aio2400
- Hyper2000
- Hub1200
- Hub2000
- SolarFlow 800 / 800 Pro / 800 Plus
- SolarFlow 1600 AC+
- SolarFlow 2400 AC / AC+ / Pro
- SolarFlow 4000 AC+
- SuperBase V6400
- SuperBase V4600 eingeschränkt beziehungsweise nicht vollständig über Token unterstützt

## Inhalt

1. [Installation](./installation)
2. [Lokales MQTT](./lokales-mqtt)
3. [Fuse Group](./fuse-group)
4. [Zendure Manager](./manager)
5. [Entitäten](./entitaeten)
6. [Fehlersuche](./fehlersuche)

## Wichtiger Hinweis

Einige Seiten der Original-Wiki sind vom Projekt selbst als teilweise veraltet gekennzeichnet. In dieser deutschen Doku werden solche Inhalte als Praxis- und Orientierungshilfe übernommen, aber nicht als verbindliche technische Spezifikation behandelt.

