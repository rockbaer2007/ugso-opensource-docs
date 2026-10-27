---
title: Installation de Zendure pour HA
description: Installation et configuration de l'intégration Zendure pour Home Assistant.
---
<a id="zendure-ha-installation"></a>
<a id="orientation-actuelle"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

1. Ouvrir Home Assistant.
2. Ouvrir `HACS`.
3. Accéder à `Integrationen`. 4. Ouvrir `+ Explore & Download Repos`.
5. Rechercher `Zendure`.
6. Télécharger `Zendure Home Assistant Integration`.
7. Actualiser le navigateur si Home Assistant n'affiche pas encore directement l'intégration.
8. Ouvrir `Einstellungen -> Geräte & Dienste -> Integration hinzufügen`.
9. Rechercher `Zendure` et lancer la configuration.

Lien direct :

[Ajouter l'intégration Zendure dans Home Assistant](https://my.home-assistant.io/redirect/config_flow_start/?domain=zendure_ha)

## Jeton (token) de l'application Zendure {#zendure-app-token}

L'intégration utilise un jeton provenant de l'application Zendure. Ce jeton doit être issu du compte principal sur lequel les appareils sont enregistrés.

::: warning Mise à niveau depuis des versions antérieures
Pour les installations anciennes comportant un second compte ou utilisant une ancienne méthode de connexion, l'ancienne configuration doit être supprimée puis recréée. L'intégration actuelle repose sur un système de jetons (tokens).
:::

La fenêtre de saisie du jeton est documentée dans le wiki d'origine, capture d'écran à l'appui :

[Capture d'écran du jeton dans le wiki d'origine](https://github.com/Zendure/Zendure-HA/wiki/Installation)

## Options dans la fenêtre de configuration {#optionen-im-einrichtungsdialog}

| Option | Signification |
| --- | --- |
| `Zendure Token` | Jeton (token) provenant de l'application Zendure |
| `P1 Sensor für Smart Matching` | Capteur de consommation domestique : valeur positive en cas de consommation, négative en cas d'injection sur le réseau |
| `MQTT-Kommunikation loggen` | Enregistre les échanges MQTT dans les journaux (logs) de Home Assistant (si le mode débogage est activé) |
| `Lokales MQTT verwenden` | Ouvre une seconde fenêtre pour la saisie des données MQTT locales |
| `MQTT-Benutzer automatisch verwalten` | Tente de gérer automatiquement les identifiants d'accès MQTT |
| `WLAN SSID` | Nom du réseau Wi-Fi pour la reconfiguration des appareils |
| `Wifi Passwort` | Mot de passe du réseau Wi-Fi pour la reconfiguration des appareils |

## Après la configuration {#nach-der-einrichtung}

Une fois la configuration effectuée avec succès, les appareils Zendure et leurs entités apparaissent dans Home Assistant. Si vous possédez plusieurs appareils, il est recommandé de configurer correctement le [groupe de protection (Fuse Group)](/fr/collection/zendure-ha/fuse-group) afin que les fonctionnalités de « Smart-Matching » (correspondance intelligente) et de limitation de puissance fonctionnent de manière optimale.
