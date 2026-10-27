---
title: Dépannage Zendure pour Home Assistant
description: Dépannage en cas de problèmes de connexion avec l'intégration Zendure pour Home Assistant.
---
<a id="zendure-ha-depannage"></a>
<a id="orientation-actuelle"></a>

# Dépannage {#fehlersuche}

## Vérifications de base {#grundcheck}

1. Mettre à jour l'intégration vers la dernière version.
2. Redémarrer Home Assistant.
3. Vérifier que le jeton (token) de l'application Zendure provient bien du compte principal.
4. Vérifier que les appareils sont visibles dans l'application Zendure.
5. Activer la journalisation de débogage (debug logging) pour l'intégration Zendure.
6. En cas d'utilisation de MQTT local : vérifier l'adresse du broker, l'identifiant, le mot de passe, ainsi que le SSID et le mot de passe du réseau Wi-Fi.

## Messages d'erreur fréquents {#haufige-fehlermeldungen}

| Message | Signification / Action |
| --- | --- |
| Jeton (Token) invalide | Copiez à nouveau le jeton depuis l'application Zendure |
| Aucun appareil trouvé | Vérifiez si le compte Zendure ou la région sont corrects |
| Aucun serveur MQTT renvoyé | Vérifiez la configuration MQTT (locale ou cloud) dans l'application Zendure |
| Aucun groupe de protection (Fuse Group) | Définissez un groupe de protection (Fuse Group) |
| HEMS | L'appareil est contrôlé par un système HEMS et ne peut pas être géré librement par le gestionnaire |

## Hyper2000 / Appareils d'ancienne génération (Legacy) {#hyper2000-legacy-gerate}

En cas de problèmes de connexion, le wiki officiel recommande :

1. Activer la journalisation de débogage (Debug-Logging).
2. Supprimer l'entrée de l'intégration.
3. Redémarrer l'appareil.
4. Mettre à jour l'intégration.
5. Ajouter à nouveau l'intégration à l'aide du jeton (token) de l'application Zendure.
6. Activer la journalisation MQTT.
7. Configurer le MQTT local en incluant tous les champs.
8. Tester d'abord `cloud` comme mode de connexion.
9. Définir le « Fuse Group » (groupe de protection).
10. Vérifier si l'appareil possède une adresse MAC Bluetooth.
11. Attendre au moins 10 minutes, car les mises à jour via Bluetooth peuvent être différées.

## Si l'appareil ne répond pas {#wenn-das-gerat-nicht-reagiert}

- Sélectionner le mode de fonctionnement `Manuelle Leistungsregelung`.
- Modifier `Manuelle Leistung` à titre de test (par exemple, régler sur 300 W, puis sur 400 W).
- Tester ensuite `Smarte Leistungsregelung`.
- En l'absence de réaction, sauvegarder le journal de débogage (debug log) complet.

Wiki original :

- [Dépannage](https://github.com/Zendure/Zendure-HA/wiki/Troubleshooting)
