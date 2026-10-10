---
title: UGSo CallMeBot Signal
description: Messages texte Signal depuis Home Assistant avec profils et Blockly.
---
# UGSo CallMeBot Signal

**Application HA 0.1.0 expérimentale** dans le [dépôt commun de Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal). Entièrement **DE/EN/FR**, langue système et apparence claire/sombre/système. Implémentation UGSo originale inspirée de [ioBroker.signal-cmb](https://github.com/derAlff/ioBroker.signal-cmb).

![Interface Signal en français](/assets/callmebot-signal/fr.png)

## Configuration

1. Ajouter `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` au magasin HA et installer **UGSo CallMeBot Signal**.
2. Configurer MQTT dans HA, démarrer l’application et ouvrir son interface Ingress. Les identifiants MQTT du Supervisor sont prioritaires ; les options servent de secours.
3. Utiliser le contact actuel du bot indiqué dans le [guide officiel Signal](https://www.callmebot.com/blog/free-api-signal-send-messages/). Envoyer la phrase d’activation dans **Signal** et attendre la **clé API Signal**.
4. Enregistrer l’ID du profil, son nom, votre numéro international **avec +** ou **UUID Signal**, et la clé correspondante. Si le numéro est masqué, le bot peut fournir un UUID. Copier le destinataire du lien d’activation sans le modifier.
5. Choisir le profil par défaut. « Envoyer le message » envoie réellement au profil enregistré sélectionné.

Les clés WhatsApp ne fonctionnent pas pour Signal. Les deux applications peuvent fonctionner ensemble : profils, sujets MQTT, identifiants clients et entités de diagnostic séparés. L’[application WhatsApp](../callmebot/) conserve ses identifiants techniques.

## Blockly et sélection du profil

Depuis **Blocks for HA 0.1.50** : **Messages → Signal · CallMeBot**.

![Bloc Signal](/assets/blocks-for-ha/blocks/fr/ugso_callmebot_signal_action.png)

Cliquer sur le champ du profil, rechercher par nom/ID et sélectionner. Vide utilise le destinataire par défaut. Le nom est affiché, l’ID est enregistré. Connecter du texte, une variable ou Jinja. Journal : erreurs seules, aucun ou info. Le bloc produit une action native `mqtt.publish` ; le JSON est sérialisé après l’évaluation du modèle.

L’application publie le catalogue sur `ugso/callmebot_signal/profiles` et l’entité de diagnostic MQTT **`sensor.ugso_callmebot_signal_profiles`**. État : nombre de profils. Attributs : IDs, noms, profil par défaut et marqueur source, **sans destinataire, message ni clé**. Blocks utilise le marqueur même si l’entité est renommée. Préfixe de découverte standard : `homeassistant`.

Sans connexion, saisir l’ID manuellement ou le laisser vide. Les IDs invalides/supprimés ne sont jamais remplacés automatiquement. Les projets JSON conservent le bloc dédié ; l’import YAML représente l’envoi par une action HA/MQTT générale.

## Protocole et limites

- Envoi : `ugso/callmebot_signal/send`, QoS 0, **retain false**.
- Exemple : `{"profile":"default","message":"Bonjour depuis HA","loglevel":"errors"}`. Un profil vide utilise le destinataire par défaut.
- Résultat : `ugso/callmebot_signal/result`, non retenu, uniquement profil, ID de requête, état et heure.
- Catalogue et disponibilité : `ugso/callmebot_signal/profiles` et `ugso/callmebot_signal/availability`, retenus. La disponibilité reflète la connexion au courtier.
- Maximum 16 profils, 4000 caractères, file de 20 et 10 secondes entre tentatives par profil. Les commandes plus rapides sont refusées.
- `request_id` facultatif : déduplication pendant une heure, maximum 1000 IDs. Sans réessai automatique ni répétition après redémarrage ; commandes retenues refusées.
- Une instance Signal par courtier. Limiter les droits d’écriture sur les commandes. La configuration MQTT TLS externe n’est pas incluse.

Cette application envoie des **textes à vos propres destinataires activés**. Images, groupes et réponses ne sont pas implémentés. `accepted` confirme uniquement l’acceptation API. Destinataire, clé et message sont transmis par HTTPS à `https://signal.callmebot.com/signal/send.php`.

Les clés restent dans le fichier privé `/data/profiles.json`, ne sont jamais renvoyées au navigateur/MQTT/Blockly et ne sont pas journalisées. Ce fichier n’est pas chiffré et figure dans les sauvegardes HA ; protéger les sauvegardes.

## Vérification

Backend, validation UUID/numéro, protocole MQTT, export Blockly/Jinja, DE/EN/FR et affichage mobile sont vérifiés avec des données de test. Livraison Signal réelle et installation HA Supervisor nécessitent votre propre configuration. Les tests automatisés n’envoient aucun message réel.

[Code source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot_signal) · Apache-2.0 · Projet communautaire indépendant.
