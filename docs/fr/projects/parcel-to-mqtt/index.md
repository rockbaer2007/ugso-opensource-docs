---
layout: home
hero:
  name: Parcel to MQTT
  text: Développement arrêté
  tagline: Parcel Tracker est un projet bien plus abouti. C'est pourquoi nous mettons fin au développement de Parcel to MQTT. La documentation existante
    est conservée à titre d'archive.
  actions:
  - theme: brand
    text: Voir Parcel Tracker
    link: https://github.com/SoerenKaiser99/parcel_tracker
  - theme: alt
    text: GitHub
    link: https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt
features:
- icon: 📦
  title: Statut du colis
  details: Statut du colis, dernier événement, destination et numéro d'envoi sous forme d'entités Home Assistant.
- icon: 🚚
  title: DHL et Hermes pris en charge
  details: Gestion des comptes DHL, saisie manuelle de numéros d'envoi DHL et suivi des colis Hermes.
- icon: 🧩
  title: Sections par transporteur
  details: Paramètres regroupés pour DHL, Hermes, GLS, DPD, UPS, Amazon Logistics, Deutsche Post (courriers) et FedEx.
- icon: 📊
  title: Compteurs et emplacements
  details: 'Compteurs pour : total, en transit, en cours de livraison, en point relais, livré, retourné, problème rencontré et état inconnu.'
- icon: 🏠
  title: Découverte MQTT (MQTT Discovery)
  details: Home Assistant crée automatiquement les entités relatives aux colis, à leurs statuts et aux compteurs.
- icon: 🔔
  title: Automatisations
  details: Les notifications peuvent être configurées via les automatisations standard de Home Assistant, en se basant sur les entités générées.
---
<a id="index"></a>
<a id="statut"></a>


::: warning Développement arrêté
Parcel Tracker est un projet bien plus abouti. C'est pourquoi nous mettons fin au développement de Parcel to MQTT ; nous invitons les personnes intéressées à consulter [Parcel Tracker par SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker).

Le code source et la documentation précédente sont conservés sous forme d'archive. Les fonctionnalités et instructions suivantes décrivent l'état actuel de notre paquet.
:::

## Aperçu {#uberblick}

« Parcel to MQTT » est une application pour Home Assistant qui permet le suivi de colis via la fonctionnalité « MQTT Discovery » de Home Assistant.

La version actuelle prend en charge les listes de colis issues d'un compte DHL, l'ajout manuel de numéros de suivi DHL, ainsi que le suivi des colis Hermes. Les paramètres de l'application sont regroupés par prestataire, ce qui permet à la configuration dans Home Assistant de rester concise, organisée par fournisseur.

::: info Origine
Cette implémentation est adaptée de — et inspirée par — l'adaptateur ioBroker [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel).

Le modèle d'état commun s'inspire des intégrations de suivi de colis pour Home Assistant [ha-parcel-integrations](https://github.com/ha-parcel-integrations), distribuées sous licence MIT.
:::

## Feuille de route précédente (Archives) {#fruhere-provider-roadmap-archiv}

Les points suivants décrivent l'état d'avancement antérieur et les plans initiaux. Cette feuille de route n'est plus suivie :

- DHL : actif via un code de connexion par navigateur (`dhllogin://`) et ajout manuel de numéros de suivi ;
- Amazon : préparé pour une utilisation avec e-mail, mot de passe et jeton OTP optionnel ;
- Hermes : actuellement actif via la saisie manuelle de numéros de suivi ; La connexion au compte via le nom d'utilisateur et le mot de passe de l'application est prévue.
- UPS : prêt à l'emploi avec nom d'utilisateur, mot de passe et numéros de suivi saisis manuellement.
- GLS : prêt à l'emploi avec numéros de suivi saisis manuellement et code postal de livraison ; le mécanisme de récupération des données (*polling*) attend l'établissement d'une session « Guest-Bearer » stable.
- DPD : prêt à l'emploi avec nom d'utilisateur, mot de passe et numéros de suivi saisis manuellement, dès que le processus de connexion/session sera parfaitement stabilisé.
- Deutsche Post (lettres) et FedEx : préparation effectuée pour une intégration ultérieure via des connecteurs dédiés, avec saisie manuelle des numéros de suivi.

## Autres pages {#weitere-seiten}

- [Installation](/fr/projects/parcel-to-mqtt/installation)
- [Configuration](/fr/projects/parcel-to-mqtt/configuration)
- [Entités](/fr/projects/parcel-to-mqtt/entities)
- [Exemples](/fr/projects/parcel-to-mqtt/examples)
