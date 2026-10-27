---
title: « Fuse Group » (Groupe de protection) pour Zendure HA
description: « Fuse Group » et limites de puissance dans l'intégration Zendure pour Home Assistant.
---
<a id="zendure-ha-fuse-group"></a>
<a id="orientation-actuelle"></a>

# Fuse Group {#fuse-group}

Le « Fuse Group » est un regroupement lié à la sécurité et au contrôle. Il indique quels appareils Zendure sont raccordés au même fusible (ou au même circuit électrique) et définit la puissance maximale autorisée sur ce circuit.

::: danger Responsabilité
Le choix correct du « Fuse Group » est crucial pour la sécurité. Choisissez-la en fonction de votre installation électrique et des réglementations locales.
:::

## Pourquoi est-ce important ? {#warum-sie-wichtig-ist}

Le Zendure Manager répartit la puissance en se basant sur le paramètre « Fuse Group » (groupe de protection). La somme des puissances des appareils appartenant à un même groupe ne doit pas dépasser la limite définie.

Si aucun « Fuse Group » approprié n'est défini, l'appareil ne sera pas pris en compte pour les fonctionnalités intelligentes.

## Options courantes {#typische-optionen}

| Option | Signification |
| --- | --- |
| `Nicht verwendet` | L'appareil n'est associé à aucun « Fuse Group » et n'est pas utilisé pour la gestion intelligente |
| `Eigener Stromkreis / eigene Phase` | L'appareil est seul sur son propre circuit électrique |
| `Sicherungsgruppe max. 800 W` | Groupe avec une limite maximale de 800 W |
| `Sicherungsgruppe max. 1200 W` | Groupe avec une limite maximale de 1200 W |
| `Sicherungsgruppe max. 2000 W` | Groupe avec une limite maximale de 2000 W |
| `Sicherungsgruppe max. 2400 W` | Groupe avec une limite maximale de 2400 W |
| `Sicherungsgruppe max. 3600 W` | Groupe avec une limite maximale de 3600 W |
| `Sicherungsgruppe max. 4000 W` | Groupe avec une limite maximale de 4000 W |
| `Sicherungsgruppe max. 5000 W` | Groupe avec une limite maximale de 5000 W |

## État de la connexion {#verbindungstatus}

L'intégration affiche un état de connexion qui aide à situer la situation :

| État | Signification |
| --- | --- |
| `Unbekannt` | Aucun état de connexion défini |
| `Kalibrierung` | Appareil calibré |
| `HEMS` | Appareil contrôlé par le HEMS |
| `Keine Sicherungsgruppe` | Groupe de fusibles (Fuse Group) manquant |
| `Verbunden (Cloud)` | Connexion via le cloud |
| `Verbunden (Local)` | Connexion via MQTT local |
| `Verbunden (zenSDK)` | Connexion via zenSDK |

Wiki original :

- [Groupe de fusibles (Fuse Group)](https://github.com/Zendure/Zendure-HA/wiki/Fuse-Group)
