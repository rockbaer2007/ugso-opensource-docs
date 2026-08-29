---
title: Calendar Card Pro
description: Inoffizielle deutsche Dokumentation zur Calendar Card Pro fuer Home Assistant.
---
# Calendar Card Pro

Calendar Card Pro ist eine moderne, stark anpassbare Kalenderkarte fuer Home Assistant. Sie zeigt kommende Termine performant und uebersichtlich an, unterstuetzt mehrere Kalender, kompakte Ansichten, Spaltenansicht, Wetter, Templates, Aktionen und einen visuellen Editor.

::: warning Inoffizielle deutsche Doku
Diese Dokumentation ist eine inoffizielle deutsche Arbeitsuebersetzung und Praxisdoku. Das originale Calendar-Card-Pro-Projekt und dessen englische Dokumentation bleiben massgeblich.
:::

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/header.png" alt="Calendar Card Pro Vorschau" width="100%">

| Feld | Wert |
| --- | --- |
| Originalprojekt | [alexpfau/calendar-card-pro](https://github.com/alexpfau/calendar-card-pro) |
| Originaldoku | [calendar-card-pro.alexpfau.com](https://calendar-card-pro.alexpfau.com) |
| Gepruefter Commit | [`f5226781fd64fb7b69257ba2f5b1f4af0d28ebf6`](https://github.com/alexpfau/calendar-card-pro/commit/f5226781fd64fb7b69257ba2f5b1f4af0d28ebf6) |
| Release | [`v4.0.0`](https://github.com/alexpfau/calendar-card-pro/releases/tag/v4.0.0) |
| Lizenz | [MIT](https://github.com/alexpfau/calendar-card-pro/blob/main/LICENSE) |
| Status | Deutsche Doku mit Installation, Nutzung, Features, Referenz, Beispielen und Aenderungspruefung |

## Inhalt

- [Installation](./installation)
- [Nutzung](./nutzung)
- [Features](./features)
- [Konfigurationsreferenz](./konfiguration)
- [Beispiele](./beispiele)
- [Entwicklung und Mitwirken](./entwicklung)
- [Lizenz und Quellenstand](./lizenz-und-stand)

## Wofuer ist die Karte gedacht?

Calendar Card Pro ist fuer Dashboards gedacht, auf denen Kalendertermine gut lesbar, kompakt und optisch sauber dargestellt werden sollen. Die Karte ist besonders interessant, wenn mehrere Kalender zusammengefuehrt werden, Termine nach Kalender farblich unterschieden werden sollen oder eine Wochenansicht als Spaltenlayout gebraucht wird.

Die Karte benoetigt mindestens eine Home-Assistant-Entitaet vom Typ `calendar.*`. Getestet sind laut Original besonders CalDAV und Google Calendar, grundsaetzlich funktioniert die Karte mit Integrationen, die Kalenderentitaeten bereitstellen.
