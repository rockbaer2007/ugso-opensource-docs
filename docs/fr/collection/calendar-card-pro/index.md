---
title: Calendar Card Pro
description: Documentation non officielle en français pour Calendar Card Pro (Home Assistant).
---
<a id="orientation-actuelle"></a>

# Calendar Card Pro {#calendar-card-pro}

Calendar Card Pro est une carte de calendrier moderne et hautement personnalisable pour Home Assistant. Elle affiche les événements à venir de manière performante et claire. Elle prend en charge plusieurs calendriers, des vues compactes, une disposition en colonnes, la météo, des modèles (templates), des actions, des badges pour les événements sur toute la journée, des filtres par calendrier, ainsi qu'un éditeur visuel.

::: warning Documentation non officielle en français
Cette documentation est une traduction de travail non officielle en français, conçue pour une utilisation pratique. Le projet original Calendar Card Pro et sa documentation en anglais restent les références faisant foi.
:::

<img src="https://raw.githubusercontent.com/alexpfau/calendar-card-pro/main/.github/img/header.png" alt="Calendar Card Pro Vorschau" width="100%">

| Champ | Valeur |
| --- | --- |
| Projet original | [alexpfau/calendar-card-pro](https://github.com/alexpfau/calendar-card-pro) |
| Documentation originale | [calendar-card-pro.alexpfau.com](https://calendar-card-pro.alexpfau.com) |
| Commit vérifié | [`a3b01138daa44947f6673c33fe700e5ef4a08957`](https://github.com/alexpfau/calendar-card-pro/commit/a3b01138daa44947f6673c33fe700e5ef4a08957) |
| Version (Release) | [`v4.1.0`](https://github.com/alexpfau/calendar-card-pro/releases/tag/v4.1.0) |
| Licence | [MIT](https://github.com/alexpfau/calendar-card-pro/blob/main/LICENSE) |
| État | Documentation en français incluant l'installation, l'utilisation, les fonctionnalités, la référence, des exemples et le suivi des modifications |

## Sommaire {#inhalt}

- [Installation](/fr/collection/calendar-card-pro/installation)
- [Utilisation](/fr/collection/calendar-card-pro/nutzung)
- [Fonctionnalités](/fr/collection/calendar-card-pro/features)
- [Référence de configuration](/fr/collection/calendar-card-pro/konfiguration)
- [Exemples](/fr/collection/calendar-card-pro/beispiele)
- [Développement et contribution](/fr/collection/calendar-card-pro/entwicklung)
- [Licence et état des sources](/fr/collection/calendar-card-pro/lizenz-und-stand)

## À quoi sert cette carte ? {#wofur-ist-die-karte-gedacht}

Calendar Card Pro est conçue pour les tableaux de bord (dashboards) où les événements de calendrier doivent être affichés de manière lisible, compacte et esthétique. Cette carte est particulièrement intéressante lorsque plusieurs calendriers sont regroupés, que l'on souhaite distinguer les événements par couleur selon leur calendrier d'origine, ou qu'une vue hebdomadaire sous forme de colonnes est requise.

La carte nécessite au moins une entité Home Assistant de type `calendar.*`. Selon la documentation originale, elle a été testée notamment avec CalDAV et Google Calendar ; de manière générale, elle fonctionne avec toute intégration fournissant des entités de calendrier.
