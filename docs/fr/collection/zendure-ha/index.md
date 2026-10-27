---
title: Intégration Zendure pour Home Assistant
description: Documentation non officielle en français concernant l'intégration de Zendure dans Home Assistant.
---
<a id="orientation-actuelle"></a>

# Intégration de Zendure dans Home Assistant {#zendure-home-assistant-integration}

L'intégration Zendure pour Home Assistant permet d'ajouter des appareils Zendure à Home Assistant. Elle expose les données transmises sous forme d'entités, permet de définir des paramètres de contrôle (tels que les limites de charge et de sortie) et propose, via le « Zendure Manager », une régulation de la puissance basée sur un capteur de consommation domestique (type P1).

::: warning Documentation non officielle en français
Cette documentation constitue une adaptation indépendante en français. Le projet original et le wiki d'origine font foi.
:::

## État du projet {#projektstand}

| Champ | Valeur |
| --- | --- |
| Projet original | [zendure/zendure-ha](https://github.com/zendure/zendure-ha) |
| Wiki original | [Wiki Zendure-HA](https://github.com/Zendure/Zendure-HA/wiki) |
| Version du dépôt documentée | `master`, vérifiée le 29.08.2026 |
| Derniers tags du dépôt | `1.4.4`, `1.4.4-pre1` |
| Version minimale (selon le README) | Home Assistant `2025.5+` |
| Version minimale (selon le fichier HACS) | Home Assistant `2025.4.0` |
| Licence | MIT |
| Domaine d'intégration | `zendure_ha` |

## Appareils pris en charge selon la documentation originale {#unterstutzte-gerate-laut-originaldoku}

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
- SuperBase V4600 : prise en charge limitée ou incomplète via jeton (token)

## Sommaire {#inhalt}

1. [Installation](/fr/collection/zendure-ha/installation)
2. [MQTT local](/fr/collection/zendure-ha/lokales-mqtt)
3. [Groupe de fusibles (Fuse Group)](/fr/collection/zendure-ha/fuse-group)
4. [Zendure Manager](/fr/collection/zendure-ha/manager)
5. [Entités](/fr/collection/zendure-ha/entitaeten)
6. [Dépannage](/fr/collection/zendure-ha/fehlersuche)

## Remarque importante {#wichtiger-hinweis}

Certaines pages du wiki original sont considérées par le projet lui-même comme étant partiellement obsolètes. Dans cette documentation en français, ces contenus sont repris à titre indicatif et pratique, mais ne doivent pas être considérés comme des spécifications techniques contraignantes.
