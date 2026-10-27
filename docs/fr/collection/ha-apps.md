---
title: Applications et modules complémentaires (Add-ons) pour HA
description: Modules complémentaires, applications et ponts MQTT pour Home Assistant, issus de la collection open source UGSo.
---
<a id="orientation-actuelle"></a>

# Applications et modules complémentaires HA {#ha-apps-und-add-ons}

Cette section regroupe les modules complémentaires (add-ons) Home Assistant, les applications, les ponts MQTT et les services en cours d'exécution.

## Projets existants {#vorhandene-projekte}

| Projet | Description |
| --- | --- |
| <img class="package-icon" src="/images/packages/projects-blocks-for-ha.png" width="32" height="32" alt="" aria-hidden="true"> [Blocks for HA](/fr/projects/blocks-for-ha/) | Application expérimentale pour HA : création d'automatisations natives via des blocs visuels ; inclut la gestion des entrées (Ingress), l'export/import YAML et des embranchements extensibles. |
| <img class="package-icon" src="/images/packages/projects-fritzbox-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [FRITZ!Box to MQTT](/fr/projects/fritzbox-to-mqtt/) | Intégration des données FRITZ!Box dans Home Assistant via MQTT Discovery. |
| <img class="package-icon" src="/images/packages/projects-heizoel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [Heizöl to MQTT](/fr/projects/heizoel-to-mqtt/) | Intégration des prix du fioul domestique dans Home Assistant via MQTT Discovery. |
| <img class="package-icon" src="/images/packages/projects-parcel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [Parcel to MQTT](/fr/projects/parcel-to-mqtt/) | Développement arrêté. Alternative : [Parcel Tracker](https://github.com/SoerenKaiser99/parcel_tracker). Documentation conservée à titre d'archive. |
| <img class="package-icon" src="/images/packages/projects-mqtt-client.png" width="32" height="32" alt="" aria-hidden="true"> [MQTT-Client](/fr/projects/mqtt-client/) | Envoi en temps réel de valeurs sélectionnées depuis HA vers un broker externe, et pilotage des entités compatibles. Depuis la version 0.1.16, inclut la gestion des états, la suppression confirmée des messages persistants (retain), la sauvegarde des paramètres et la prise en charge de certificats TLS personnalisés ; les anciens paramètres restent valides. |

## Dépôt d'add-ons {#add-on-repository}

Les projets MQTT sont mis à disposition via un dépôt d'add-ons Home Assistant commun :

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

- [Ouvrir les projets MQTT](/fr/projects-mqtt/)
