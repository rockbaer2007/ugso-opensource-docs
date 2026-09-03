---
title: Calendar Card Pro
description: Inoffizielle deutsche Dokumentation zur Calendar Card Pro für Home Assistant.
---
# Calendar Card Pro

Calendar Card Pro ist eine moderne, stark anpassbare Kalenderkarte für Home Assistant. Sie zeigt kommende Termine performant und übersichtlich an, unterstützt mehrere Kalender, kompakte Ansichten, Spaltenansicht, Wetter, Templates, Aktionen, ganztägige Termin-Badges, kalenderbezogene Filter und einen visuellen Editor.

::: warning Inoffizielle deutsche Doku
Diese Dokumentation ist eine inoffizielle deutsche Arbeitsübersetzung und Praxisdoku. Das originale Calendar-Card-Pro-Projekt und dessen englische Dokumentation bleiben maßgeblich.
:::

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/header.png" alt="Calendar Card Pro Vorschau" width="100%">

| Feld | Wert |
| --- | --- |
| Originalprojekt | [alexpfau/calendar-card-pro](https://github.com/alexpfau/calendar-card-pro) |
| Originaldoku | [calendar-card-pro.alexpfau.com](https://calendar-card-pro.alexpfau.com) |
| Gepruefter Commit | [`a3b01138daa44947f6673c33fe700e5ef4a08957`](https://github.com/alexpfau/calendar-card-pro/commit/a3b01138daa44947f6673c33fe700e5ef4a08957) |
| Release | [`v4.1.0`](https://github.com/alexpfau/calendar-card-pro/releases/tag/v4.1.0) |
| Lizenz | [MIT](https://github.com/alexpfau/calendar-card-pro/blob/main/LICENSE) |
| Status | Deutsche Doku mit Installation, Nutzung, Features, Referenz, Beispielen und Änderungsprüfung |

## Inhalt

- [Installation](./installation)
- [Nutzung](./nutzung)
- [Features](./features)
- [Konfigurationsreferenz](./konfiguration)
- [Beispiele](./beispiele)
- [Entwicklung und Mitwirken](./entwicklung)
- [Lizenz und Quellenstand](./lizenz-und-stand)

## Wofür ist die Karte gedacht?

Calendar Card Pro ist für Dashboards gedacht, auf denen Kalendertermine gut lesbar, kompakt und optisch sauber dargestellt werden sollen. Die Karte ist besonders interessant, wenn mehrere Kalender zusammengeführt werden, Termine nach Kalender farblich unterschieden werden sollen oder eine Wochenansicht als Spaltenlayout gebraucht wird.

Die Karte benötigt mindestens eine Home-Assistant-Entität vom Typ `calendar.*`. Getestet sind laut Original besonders CalDAV und Google Calendar, grundsätzlich funktioniert die Karte mit Integrationen, die Kalenderentitäten bereitstellen.
