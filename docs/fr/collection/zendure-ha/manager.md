---
title: Zendure Manager
description: Modes de fonctionnement et régulation de la puissance du Zendure Manager.
---
<a id="zendure-gestionnaire"></a>
<a id="orientation-actuelle"></a>

# Zendure Manager {#zendure-manager}

Le Zendure Manager tente, via les appareils Zendure, d'ajuster la consommation domestique (mesurée par le capteur P1) en direction de `0 W`. Pour ce faire, il pilote la puissance de charge et de décharge des appareils.

::: warning HEMS et programmes de l'application
Si le Zendure Manager et un système HEMS (ou un programme énergétique configuré dans l'application Zendure) effectuent des régulations simultanées, ils risquent d'entrer en conflit. N'utilisez qu'une seule stratégie de régulation active.
:::

## Capteur P1 {#p1-sensor}

Le capteur P1 doit fournir la consommation domestique :

- valeur positive : le domicile consomme de l'électricité provenant du réseau
- valeur négative : le domicile injecte de l'électricité sur le réseau

Ce capteur constitue la base de la fonction « Smart Matching ».

## Modes de fonctionnement {#betriebsarten}

| Mode | Signification |
| --- | --- |
| `Aus` | Le gestionnaire ne pilote aucun appareil |
| `Manuelle Leistungsregelung` | Valeur de puissance fixe via `Manuelle Leistung` |
| `Smarte Leistungsregelung` | Tente de maintenir le capteur P1 à 0 W |
| `Smartes nur Entladen` | Similaire au « Smart Matching », mais sans charge |
| `Smartes nur Laden` | Charge uniquement, pas de décharge |
| `Solar speichern` | Priorise le stockage de l'énergie solaire (ou provenant d'un réseau isolé/off-grid) dans les batteries |

## Puissance manuelle {#manuelle-leistung}

Avec `Manuelle Leistungsregelung`, l'entité `Manuelle Leistung` détermine la quantité de puissance à injecter ou à soutirer.

- Valeur positive : la batterie se décharge vers la maison ou le réseau.
- Valeur négative : la batterie se charge (si l'appareil prend en charge la charge en courant alternatif/AC).

## Smart Matching {#smart-matching}

Dans le mode « Smart Matching », le gestionnaire répartit la puissance entre les appareils disponibles. Cette répartition prend en compte le groupe de fusibles (*Fuse Group*), l'état de charge (SoC), le SoC minimal, la puissance maximale et l'état de l'appareil.

La documentation originale (Wiki) décrit une logique de répartition qui est en partie obsolète. Par conséquent, cette page doit être considérée comme une simple indication ; il est conseillé de vérifier les informations par rapport au code actuel si nécessaire.

Wiki original :

- [Description des fonctions](https://github.com/Zendure/Zendure-HA/wiki/Function-description)
- [Stratégie de répartition de la puissance](https://github.com/Zendure/Zendure-HA/wiki/Power-distribution-strategy)
