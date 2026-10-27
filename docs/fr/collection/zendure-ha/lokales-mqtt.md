---
title: MQTT local pour Zendure dans Home Assistant
description: Configurer le MQTT local pour les anciens appareils Zendure.
---
<a id="zendure-ha-lokales-mqtt"></a>
<a id="orientation-actuelle"></a>

# MQTT local {#lokales-mqtt}

Selon le wiki original, le MQTT local concerne principalement les anciens appareils Zendure :

- Hyper2000
- Hub2000
- Hub1200
- Ace1500

Les appareils plus récents, tels que le SolarFlow 800, le SolarFlow 800 Pro et le SolarFlow 2400, peuvent communiquer via `zenSDK` et ne nécessitent généralement pas de MQTT local.

## Exigences {#voraussetzungen}

- Courtier (broker) MQTT dans Home Assistant, par exemple Mosquitto
- Intégration Bluetooth dans Home Assistant
- L'appareil Zendure doit être visible via Bluetooth
- SSID du réseau Wi-Fi et mot de passe Wi-Fi
- Nom d'utilisateur et mot de passe MQTT

::: warning Adresse MQTT
Une adresse réseau réelle ou une adresse IP doit être utilisée comme adresse du serveur MQTT. Selon le wiki original, `core-mosquitto` ne constitue pas une adresse réseau valide pour les appareils Zendure.
:::

## Données de configuration {#einrichtungsdaten}

| Champ | Exemple / Remarque |
| --- | --- |
| Serveur MQTT | Adresse IP ou nom d'hôte du courtier (broker) |
| Port MQTT | Généralement `1883` |
| Utilisateur MQTT | Nom d'utilisateur sur le courtier |
| Mot de passe MQTT | Mot de passe sur le courtier |
| SSID Wi-Fi | Réseau Wi-Fi auquel l'appareil doit être connecté |
| Mot de passe Wi-Fi | Mot de passe de ce réseau Wi-Fi |

## Type de connexion par appareil {#verbindungsart-pro-gerat}

Pour les appareils pris en charge, il est possible de choisir le type de connexion pour chaque appareil :

- `cloud`
- `local`
- selon l'appareil, également `zenSDK`

Lors du changement de type de connexion, l'intégration tente de configurer le serveur MQTT sur l'appareil via Bluetooth. L'appareil peut redémarrer au cours de cette opération. Le processus peut prendre quelques secondes et génère ensuite une notification dans Home Assistant indiquant la réussite ou l'échec de l'opération.

## Réinitialisation de la connexion {#reset-verbindung}

Pour les appareils de l'ancienne génération (« legacy »), l'intégration met à disposition un bouton `Reset Verbindung`. Celui-ci peut être utilisé si la transition vers MQTT ne s'est pas effectuée correctement.

Wiki original :

- [MQTT local (appareils de l'ancienne génération)](https://github.com/Zendure/Zendure-HA/wiki/Local-Mqtt-(Legacy-Devices))
