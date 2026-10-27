---
layout: home
hero:
  name: FRITZ!Box to MQTT
  text: Application Home Assistant pour les données FRITZ!Box
  tagline: Intégration des journaux d'appels, des appels en temps réel, du Wi-Fi, du WAN, des répertoires téléphoniques et de l'état de la FRITZ!Box dans
    Home Assistant via la découverte MQTT (MQTT Discovery).
  actions:
  - theme: brand
    text: Installation
    link: /fr/projects/fritzbox-to-mqtt/installation
  - theme: alt
    text: GitHub
    link: https://github.com/rockbaer2007/ugso-ha-mqtt-addons
features:
- icon: 📞
  title: Appels et répondeurs
  details: Journaux d'appels, suivi des appels en temps réel et répondeurs (de AB0 à AB4) disponibles en tant qu'entités dans Home Assistant.
- icon: 📶
  title: Wi-Fi et réseau
  details: Contrôles pour les réseaux Wi-Fi 2,4 GHz, 5 GHz et invité, ainsi que les données de connexion WAN, les adresses IP et l'état des liaisons.
- icon: 📚
  title: Répertoires téléphoniques
  details: Répertoires téléphoniques avec affichage sélectionnable et possibilité d'exclure certains noms.
- icon: 🧭
  title: Sources de données multiples
  details: Combinaison de TR-064, des mécanismes de secours (fallbacks) via l'interface Web/Lua de la FRITZ!Box et du moniteur d'appels en temps réel.
- icon: 🏠
  title: Découverte MQTT (MQTT Discovery)
  details: Home Assistant crée automatiquement les capteurs et les interrupteurs grâce à la découverte MQTT.
- icon: 🛠️
  title: Dépannage
  details: Page dédiée au dépannage pour la connexion, TR-064, DNS over TLS, le moniteur d'appels et MQTT.
---
<a id="index"></a>
<a id="statut"></a>


## Aperçu {#uberblick}

« FRITZ!Box to MQTT » est une application pour Home Assistant qui intègre des données provenant d'une FRITZ!Box dans Home Assistant via la découverte MQTT.

La version actuelle de l'add-on est disponible dans le dépôt commun
`rockbaer2007/ugso-ha-mqtt-addons`. L'ancien dépôt dédié
`rockbaer2007/fritzbox-to-mqtt` est désormais archivé.

L'application utilise plusieurs sources, car les interfaces disponibles peuvent varier d'une FRITZ!Box à l'autre :

- TR-064 pour de nombreux services de la FRITZ!Box
- Requêtes via l'interface Web/Lua de la FRITZ!Box en guise de solution de secours (fallback)
- Le moniteur d'appels en temps réel sur le port `1012`
- La découverte MQTT pour la création automatique d'entités dans Home Assistant

::: info HACS
Ce projet est une application pour le « Supervisor » de Home Assistant. HACS permet d'installer des intégrations personnalisées et des cartes d'interface (frontend cards), mais ne prend pas en charge les applications basées sur Docker (Supervisor apps). L'installation doit donc s'effectuer via la fonctionnalité de dépôt d'applications de Home Assistant. :::

## Autres pages {#weitere-seiten}

- [Installation](/fr/projects/fritzbox-to-mqtt/installation)
- [Configuration](/fr/projects/fritzbox-to-mqtt/configuration)
- [Entités](/fr/projects/fritzbox-to-mqtt/entities)
- [Exemples](/fr/projects/fritzbox-to-mqtt/examples)
- [Dépannage](/fr/projects/fritzbox-to-mqtt/troubleshooting)
