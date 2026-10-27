---
title: Client MQTT
description: Transmettre en temps réel des valeurs sélectionnées de Home Assistant via MQTT et les piloter de manière ciblée.
---

# Client MQTT 0.1.16 {#mqtt-client-0-1-16}

Le client MQTT transmet des appareils, des états et des attributs sélectionnés depuis Home Assistant vers un broker MQTT externe, comme par exemple l'adaptateur MQTT d'ioBroker. Au lieu de répliquer toutes les entités HA, vous sélectionnez vous-même les valeurs dont vous avez besoin. Le broker HA existant demeure en place. L'application lit les données directement depuis HA ; il ne s'agit pas d'un pont entre brokers (bridge).

[Code source et référence de configuration](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [Documentation en anglais](/fr/projects/mqtt-client/)

## Configuration et sélection {#einrichtung-und-auswahl}

1. Ajoutez `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` depuis l'App Store de Home Assistant. 2. Installer et lancer le **client MQTT** ; les architectures amd64 et aarch64 sont prises en charge.
3. Ouvrir l'interface web et enregistrer l'hôte, le port, l'utilisateur et le mot de passe du broker externe. En l'absence de TLS, le port par défaut est 1883.
4. Sélectionner un appareil sur la gauche. Dans la fenêtre qui s'affiche, ses entités sont regroupées par catégories : commandes, capteurs, configuration et diagnostic. La fonction de recherche permet également de trouver des entités au sein d'un appareil.
5. Sélectionner les valeurs et attributs souhaités. La case à cocher située à droite d'une ligne de valeur permet de transférer l'état ainsi que tous les attributs associés ; la sélection de l'appareil permet quant à elle d'inclure toutes les valeurs de celui-ci.

Les modifications sont appliquées immédiatement. Aucun jeton d'accès (access token) HA supplémentaire n'est requis : l'application utilise l'accès « Supervisor » pour interagir avec l'API HA Core. En cas d'utilisation de plusieurs instances, veillez à employer des identifiants client (client IDs) et des préfixes de sujet (topic prefixes) distincts.

## Transmission en temps réel et état {#live-ubertragung-und-status}

Après le chargement initial de l'état complet, l'application traite les changements d'état de HA en temps réel via WebSocket. Si la connexion à HA est rétablie, l'état initial est rechargé ; si la connexion MQTT est rétablie, toutes les valeurs sélectionnées sont retransmises.

En cas de défaillance de la connexion en temps réel, le mécanisme d'interrogation (polling) précédent prend le relais — configuré par défaut sur un intervalle de cinq secondes, mais ajustable via `poll_interval` (de 1 à 300 secondes). Les changements survenus pendant une interruption ou entre deux intervalles d'interrogation ne peuvent pas être reconstitués a posteriori. Une saturation de la file d'attente des événements est signalée et déclenche une resynchronisation.

L'état permet de distinguer la connexion MQTT de l'accessibilité de HA ; il affiche le mode actif (temps réel/interrogation), l'heure de la dernière synchronisation, la date de la dernière publication, le nombre total de publications, ainsi que tout type d'erreur ayant été résolu. Les identifiants d'accès et le contenu des messages (payloads) ne sont pas affichés.

| Sujet MQTT | Contenu |
| --- | --- |
| `<topic_prefix>/<device>/<value>/state` | État sous forme textuelle |
| `<topic_prefix>/<device>/<value>/attribute/<attribute>` | Attribut sélectionné |
| `<topic_prefix>/<device>/<value>/set` | Canal de retour pour les commandes de contrôle prises en charge |
| `<topic_prefix>/availability` | `online` en cas de synchronisation HA réussie ; sinon `offline` |

Le préfixe par défaut est `ha_external`. Les états et les attributs sont publiés avec un niveau de QoS 1 et le drapeau « retain » (conservation) ; aucune configuration de découverte MQTT (MQTT discovery) n'est générée. Lors de la connexion initiale, les états et les attributs sont envoyés avant les canaux de retour d'information `/set`, avec un intervalle par défaut de 50 ms entre chaque publication. Les messages `unknown` et `unavailable` sont transmis tels quels ; les entités inexistantes renvoient `unavailable`.

## Commandes de contrôle vers HA {#steuerbefehle-zuruck-an-ha}

Les canaux de retour d'information sont automatiquement activés pour les entités contrôlables sélectionnées. Les capteurs restent en mode « sortie uniquement ». Envoyez les commandes vers le sujet (`topic`) `/set` correspondant, **sans utiliser l'indicateur « retain »**.

| Entité | Données (Payload) |
| --- | --- |
| Entité commutable | `ON` ou `OFF` |
| `number`, `input_number` | Valeur numérique |
| `select`, `input_select` | Nom d'une option disponible |
| `text`, `input_text` | Texte |
| `button`, `input_button` | `PRESS` |
| `cover` | `OPEN`, `CLOSE`, `STOP` ou `{"position":45}` |
| `light` | `{"brightness_pct":75}` |
| `fan` | `{"percentage":50}` |

Les commandes JSON n'autorisent que le champ spécifié, accompagné d'une valeur numérique comprise entre 0 et 100. L'appareil HA (Home Assistant) doit prendre en charge cette fonctionnalité. Les anciens identifiants d'entité (Entity IDs), tels que `ha_external/switch.plug/set`, restent valides. Les messages avec l'indicateur « retain » (persistant), les commandes obsolètes et les contenus non valides sont ignorés ; l'exécution d'actions HA arbitraires n'est pas prévue.

## Suppression des « topics » persistants (retain topics) obsolètes {#veraltete-retain-topics-entfernen}

La fonction **Vérifier les « topics » persistants obsolètes** affiche les « topics » enregistrés qui ne sont plus utilisés en raison de modifications apportées à la sélection, aux préfixes ou aux noms des appareils. Sélectionnez les « topics » concernés et confirmez leur suppression ; un maximum de 100 éléments peut être traité par opération.

L'application supprime uniquement les publications qu'elle a elle-même effectuées et confirmées avec succès sur le broker actuellement configuré. Les « topics » actifs ainsi que ceux créés par d'autres sources restent intacts. L'inventaire est conservé de manière permanente sous `/data/mqtt-topics.json`. En cas d'échec de la suppression, l'élément est conservé pour une nouvelle tentative ultérieure. Il n'existe **pas de nettoyage automatique**. Les anciens « topics » non répertoriés, créés avant cette mise à jour, doivent être supprimés directement sur le broker.

## Sauvegarde et restauration des paramètres {#einstellungen-sichern-und-wiederherstellen}

La fonction **Sauvegarder les paramètres** permet de télécharger un fichier JSON contenant les paramètres du broker, l'identifiant client (Client ID), le préfixe des « topics », la sélection, l'intervalle d'interrogation, l'espacement des publications et l'autorité de certification (CA) personnalisée. La fonction **Ouvrir une sauvegarde** vérifie le contenu du fichier et demande une confirmation avant de procéder au remplacement des paramètres actuels.

Le fichier ne contient **ni mot de passe MQTT, ni certificat client, ni clé privée, ni jeton (token) HA**. Il n'est pas chiffré. Si vous utilisez le même broker, les identifiants et le certificat/la clé client stockés localement sont conservés. Si vous changez de broker, ces informations doivent être saisies à nouveau. Les messages « retained » (conservés) ne sont pas inclus ; cette procédure ne remplace pas une sauvegarde complète de l'application HA.

## TLS avec certificats personnalisés {#tls-mit-eigenen-zertifikaten}

Dans la section **Transmission et TLS**, vous pouvez charger des fichiers PEM (contenant une autorité de certification, un certificat client et une clé privée) ou coller leur contenu textuel. Le certificat et la clé doivent être fournis ensemble. Le port TLS dépend du broker utilisé ; il s'agit souvent du port 8883.

Le certificat du serveur et le nom d'hôte sont systématiquement vérifiés, soit via les autorités de confiance du système, soit via une autorité de certification (CA) personnalisée. Si les champs de données sensibles sont laissés vides, les valeurs précédemment enregistrées sont conservées. Pour les supprimer, cochez l'option spécifique **Supprimer les certificats et clés TLS enregistrés** et enregistrez vos modifications. Toute configuration TLS invalide sera rejetée lors de la tentative de modification des paramètres.

## Mise à jour et compatibilité {#update-und-kompatibilitat}

Les paramètres existants issus de 0.1.15 restent valides : les identifiants du broker, la sélection des appareils/attributs, l'ID client, le préfixe des sujets (topics), l'intervalle d'interrogation et l'intervalle de publication ne sont pas modifiés au démarrage. La configuration TLS est conservée ; les nouveaux champs relatifs aux certificats sont vides par défaut. Les données conservées (« retained data ») ne sont pas supprimées lors de la mise à jour.

La version 0.1.16 a été validée via des tests backend, un broker MQTT, un point de terminaison WebSocket, TLS avec certificat client, une interface web et un déploiement Docker. L'installation effective dans Home Assistant (HA) ainsi que les fonctionnalités prises en charge doivent être vérifiées dans votre propre environnement.
