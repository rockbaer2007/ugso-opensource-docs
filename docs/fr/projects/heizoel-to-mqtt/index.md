---
layout: home
hero:
  name: Heizöl to MQTT
  text: Prix du fioul domestique pour Home Assistant
  tagline: Interroge les calculateurs de prix publics d'Esyoil et de Heizöl24, puis publie les meilleurs tarifs ainsi que les offres individuelles des fournisseurs
    via la découverte MQTT.
  actions:
  - theme: brand
    text: Installation
    link: /fr/projects/heizoel-to-mqtt/installation
  - theme: alt
    text: GitHub
    link: https://github.com/rockbaer2007/heizoel-to-mqtt
features:
- icon: 🛢️
  title: Prix du fioul domestique
  details: Récupère les meilleurs prix pour un code postal, une quantité et des options de livraison configurés.
- icon: 📍
  title: Allemagne et Autriche
  details: Consultation des prix pour des codes postaux en Allemagne et en Autriche.
- icon: 🧾
  title: Offres des fournisseurs
  details: Jusqu'à six offres de fournisseurs par source et par quantité, incluant le prix au litre, le prix pour 100 litres et le prix total.
- icon: 🔎
  title: Esyoil et Heizöl24
  details: Les points de terminaison (endpoints) des calculateurs de prix publics sont interrogés et normalisés.
- icon: 🏠
  title: Découverte MQTT (MQTT Discovery)
  details: Home Assistant crée automatiquement des entités pour les prix, les fournisseurs et l'état.
- icon: 🧰
  title: Diagnostics
  details: Journalisation (logs) facultative des fournisseurs, avec masquage des données, pour les tests et le dépannage.
---
<a id="index"></a>
<a id="statut"></a>


## Aperçu {#uberblick}

« Heizöl to MQTT » (Fioul domestique vers MQTT) est une application pour Home Assistant qui fournit les prix du fioul domestique dans Home Assistant via la découverte MQTT (MQTT Discovery).

L'application interroge les points de terminaison des calculateurs de prix publics et normalise les meilleures offres pour chaque source et chaque quantité (en litres). Elle est destinée exclusivement à l'Allemagne et à l'Autriche.

::: info Origine
Cette implémentation est adaptée et inspirée de l'adaptateur ioBroker [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel).
:::

## État {#status}

L'application peut être testée au sein de Home Assistant et fournit des valeurs via la découverte MQTT. Elle prend en charge des entités « meilleur prix » ainsi qu'un maximum de six offres de fournisseurs par source et par quantité.

Les points de terminaison de prix utilisés correspondent à ceux de sites web publics, et non à des API stables et officiellement documentées.

## Autres pages {#weitere-seiten}

- [Installation](/fr/projects/heizoel-to-mqtt/installation)
- [Configuration](/fr/projects/heizoel-to-mqtt/configuration)
- [Entités](/fr/projects/heizoel-to-mqtt/entities)
- [Exemples](/fr/projects/heizoel-to-mqtt/examples)
