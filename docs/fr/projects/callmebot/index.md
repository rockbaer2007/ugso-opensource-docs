---
title: UGSo CallMeBot Whatsapp
description: Messages texte WhatsApp depuis Home Assistant avec profils de destinataire et Blockly.
---
# UGSo CallMeBot Whatsapp

Depuis 0.1.4, l’application s’appelle **UGSo CallMeBot Whatsapp**. Profils, sujets MQTT et IDs existants sont conservés. [UGSo CallMeBot Signal](../callmebot-signal/) utilise ses propres profils et clés.

**Application HA expérimentale 0.1.4** dans le [même dépôt que Blocks for HA](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot). Interface et blocs complets en **DE/EN/FR**, langue système et apparence claire/sombre/système. Inspiré de [ioBroker.whatsapp-cmb](https://github.com/ioBroker/ioBroker.whatsapp-cmb) ; implémentation UGSo originale sans ioBroker.

**Correction 0.1.1 :** L’envoi fonctionne sans `crypto.randomUUID`, notamment avec Ingress en HTTP. Redémarrer l’application et recharger la page après la mise à jour. Les identifiants utilisent des octets aléatoires disponibles ou un horodatage avec compteur ; ils détectent les doublons et ne servent pas à l’authentification.

![Interface CallMeBot en français](/assets/callmebot/fr.png)

## Installation et configuration

1. Ajouter `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` au magasin d’applications HA.
2. Installer **UGSo CallMeBot Whatsapp**, configurer le courtier MQTT et démarrer l’application.
3. Ouvrir l’interface Ingress. Les identifiants MQTT du Supervisor sont prioritaires ; les options de l’application servent de secours.
4. Activer son propre destinataire avec le numéro actuel du bot dans le [guide officiel](https://www.callmebot.com/blog/free-api-whatsapp-messages/). Envoyer exactement `I allow callmebot to send me messages`.
5. Enregistrer l’ID du profil, son nom, le numéro activé **avec + et indicatif international**, ainsi que sa clé API. Choisir un profil par défaut. Maximum 16 profils.
6. Le bouton de test envoie réellement au profil enregistré sélectionné ; une sélection vide utilise le profil par défaut.

Un champ de clé vide conserve la clé enregistrée. Les clés ne sont jamais renvoyées à l’interface. Elles restent dans `/data/profiles.json`, hors Blockly, messages MQTT, stockage du navigateur et journaux. Ce fichier n’est pas chiffré et figure dans les sauvegardes HA.

## Bloc Blockly CallMeBot

### Choisir les profils enregistrés

Avec **CallMeBot 0.1.2 et Blocks for HA 0.1.49**, le champ de profil ouvre une liste consultable des noms, identifiants et du destinataire par défaut. **Actualiser** recharge la liste. Le bloc affiche le nom ; projets et YAML conservent l’ID original. Un ID vide utilise le destinataire par défaut actuel.

![Sélecteur de profil CallMeBot en français](/assets/callmebot/profiles-fr.png)

Mettre à jour et redémarrer les deux applications, puis recharger Blocks. HA doit être connecté au courtier et activer la découverte MQTT avec le préfixe standard `homeassistant`. CallMeBot découvre un capteur de diagnostic, normalement `sensor.ugso_callmebot_profiles` ; Blocks lit son catalogue via sa connexion HA existante. Le capteur peut être renommé, car son marqueur identifie le catalogue. Base technique : [capteurs MQTT HA et attributs JSON](https://www.home-assistant.io/integrations/sensor.mqtt/).

Le catalogue retenu `ugso/callmebot/profiles` contient uniquement IDs, noms, profil par défaut, nombre et marqueur. Aucun numéro, message ou clé API n’est publié. Modifications et reconnexions MQTT actualisent le catalogue. Les noms sont visibles dans MQTT et HA.

Si l’application, MQTT, la découverte ou la connexion HA est indisponible, la saisie manuelle et le destinataire par défaut restent utilisables. Les IDs supprimés ne sont jamais remplacés automatiquement ; l’application refuse l’envoi vers un profil absent.

Depuis **Blocks for HA 0.1.48**, dans **Messages → WhatsApp · CallMeBot**.

![Bloc CallMeBot](/assets/blocks-for-ha/blocks/fr/ugso_callmebot_action.png)

Indiquer l’ID du profil ou laisser vide pour le profil par défaut. Connecter texte, variable ou Jinja comme message. Journal : erreurs seulement, aucun ou info. Exporte `mqtt.publish` et sérialise le JSON après évaluation du modèle pour conserver correctement guillemets et sauts de ligne.

MQTT doit être configuré dans HA. Les projets JSON conservent le bloc dédié. Le YAML est réimporté comme action HA/MQTT générale.

## Alternative : intégration WhatsApp existante

![Bloc de l’intégration WhatsApp](/assets/blocks-for-ha/blocks/fr/ugso_whatsapp_action.png)

Le deuxième bloc appelle [l’intégration WhatsApp de FaserF](https://faserf.github.io/ha-whatsapp/services.html). Configurer une fois l’URL de son application et le **jeton API fourni par l’application WhatsApp** dans HA. L’intégration gère ce jeton ; le bloc n’en a pas besoin.

Choisir `whatsapp.send_message · number` pour l’ancien format, `whatsapp.send_message · target` selon la documentation actuelle ou `notify.whatsapp` si configuré. Destinataire : **indicatif international sans +**. Message : texte/Jinja. Le compte facultatif est exporté uniquement avec `whatsapp.send_message`. Le YAML compatible est importé comme bloc dédié ; les options supplémentaires restent dans l’action HA générale.

Cette alternative ne nécessite ni application CallMeBot ni clé CallMeBot. L’intégration existante assure l’installation et la connexion WhatsApp.

## Protocole MQTT et limites

- Envoi : `ugso/callmebot/send`, QoS 0, **retain false**.
- Données : `{"profile":"default","message":"Bonjour depuis HA","loglevel":"errors"}`. Profil vide/absent : destinataire par défaut.
- `request_id` facultatif : détection des doublons pendant une heure par profil, maximum 1000 identifiants.
- Résultat : `ugso/callmebot/result`, non retenu, profil, ID de requête, état et horodatage ; sans message ni clé.
- Disponibilité : `ugso/callmebot/availability`, `online`/`offline` retenu pour la connexion au courtier.
- Maximum 4000 caractères, file de 20 commandes, au moins 10 secondes entre les tentatives par profil. Les commandes trop rapides sont refusées, sans délai.
- Sans répétition automatique ni reprise après redémarrage. Les commandes d’envoi retenues sont refusées.
- Un espace MQTT et un ID client : une instance par courtier. Limiter les droits d’écriture sur le sujet d’envoi. Cette version utilise le courtier interne ; configuration TLS externe non incluse.

CallMeBot Free est destiné aux textes personnels vers ses propres numéros activés. Sans groupes, médias, réponses ni confirmation de livraison. `accepted` confirme seulement l’acceptation API. Numéro, clé et texte sont transmis par HTTPS à CallMeBot. Source : [activation et API CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/).

## Vérification

Build et démarrage Docker, backend avec fournisseur simulé, protocole MQTT, interface DE/EN/FR, affichage mobile et export Blockly vérifiés. Livraison WhatsApp réelle et installation sous HA Supervisor restent à vérifier avec sa propre configuration. Aucun message réel n’a été envoyé.

[Code source et commandes de test](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/callmebot) · Apache-2.0 · Projet communautaire indépendant.
