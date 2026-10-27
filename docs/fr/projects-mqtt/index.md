<a id="mqtt-projets"></a>
<a id="statut"></a>

# Applications HA UGSo {#ugso-ha-apps}

Ce dépôt commun constitue le point de publication central pour toutes les applications Home Assistant de UGSo Software : applications MQTT, Grafik Visual Studio, « Blocks for HA » et projets futurs. Chaque application dispose de son propre sous-répertoire, de sa propre version et de sa propre documentation. L'URL du dépôt existant reste inchangée.

## Applications HA UGSo et autres projets {#ugso-ha-apps-und-weitere-projekte}

| Projet | Documentation |
| --- | --- |
| [Gestion des utilisateurs du tableau de bord](/fr/projects/dashboard-user-manager/) | 0.1.4 : Utilisateurs présentés sous forme de colonnes avec cases à cocher, affectation groupée ou individuelle, interface disponible en DE/EN/FR et sauvegarde du tableau de bord avant l'enregistrement. |
| [CallMeBot WhatsApp](/fr/projects/callmebot/) | Application HA expérimentale 0.1.4 : Profils de destinataires, messages WhatsApp via MQTT, interface en DE/EN/FR et blocs Blockly dédiés. |
| [CallMeBot Signal](/fr/projects/callmebot-signal/) | Application HA expérimentale 0.1.0 : Messages Signal, profils basés sur un numéro de téléphone ou un UUID, espace de nommage MQTT dédié et intégration Blockly avec sélection de profils (DE/EN/FR). |
| [Blocks for HA](/fr/projects/blocks-for-ha/) | Application HA expérimentale 0.1.3 : Blocs visuels pour les automatisations natives, importation/exportation YAML et branches conditionnelles extensibles ; éditeur accessible via HA Ingress. |
| [Grafik Visual Studio](/fr/projects/grafik-visual-studio/) | Éditeur graphique et moteur d'exécution pour les visualisations dans Home Assistant. |

Ces projets se trouvent dans le même dépôt (repository) que les applications MQTT suivantes.

## Dépôt d'add-ons commun {#gemeinsames-add-on-repository}

Les projets MQTT sont désormais principalement distribués via un dépôt d'add-ons commun pour Home Assistant. Il suffit d'ajouter une seule URL de dépôt dans Home Assistant ; les différents projets apparaîtront ensuite individuellement dans la boutique d'add-ons (Add-on Store).

URL du dépôt pour Home Assistant :

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Modules complémentaires inclus :

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT (développement arrêté)
- [Client MQTT](/fr/projects/mqtt-client/) : permet de transmettre des appareils et des valeurs sélectionnés depuis Home Assistant vers ioBroker ou un broker MQTT externe. **0.1.16** ajoute la prise en charge des changements d'état en temps réel (avec un mécanisme de secours par interrogation), des statuts détaillés, un nettoyage confirmé des anciens sujets « retain » (persistants), des commandes de contrôle supplémentaires, la sauvegarde des paramètres au format JSON et la gestion de certificats TLS personnalisés. Les paramètres existants restent valides ; les données « retain » ne sont pas supprimées automatiquement. Le broker HA déjà en place demeure inchangé.

- [Ouvrir le dépôt commun de modules complémentaires sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons)

Les anciens dépôts individuels restent accessibles en tant qu'archives historiques et renvoient vers ce dépôt commun.

## FRITZ!Box to MQTT {#fritz-box-to-mqtt}

**FRITZ!Box to MQTT**

Une application pour Home Assistant qui expose les données de la FRITZ!Box sous forme d'entités via la découverte MQTT (MQTT Discovery). Elle combine le protocole TR-064, des requêtes sur l'interface web/Lua de la FRITZ!Box et la surveillance des appels en temps réel.

- [Ouvrir la documentation de FRITZ!Box-to-MQTT](/fr/projects/fritzbox-to-mqtt/)
- [Ouvrir le dépôt individuel archivé sur GitHub](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## Heizöl to MQTT {#heizol-to-mqtt}

**Heizöl to MQTT**

Une application pour Home Assistant qui met à disposition les prix du fioul domestique (provenant d'Esyoil et Heizöl24) sous forme d'entités via la découverte MQTT (MQTT Discovery). Actuellement, les meilleurs prix ainsi que jusqu'à six offres de fournisseurs par source et par quantité sont publiés.

- [Ouvrir la documentation de Heizöl-to-MQTT](/fr/projects/heizoel-to-mqtt/)
- [Ouvrir le dépôt archivé sur GitHub](https://github.com/rockbaer2007/heizoel-to-mqtt)
- Adapté de : [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel)

## Parcel to MQTT {#parcel-to-mqtt}

**Parcel to MQTT**

**Développement arrêté :** Parcel Tracker est un projet bien plus abouti. Par conséquent, nous cessons le développement de notre propre solution. Nous vous invitons à découvrir [Parcel Tracker, par SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker). La documentation existante est conservée à titre d'archive.

Une application pour Home Assistant qui intègre le suivi de colis sous forme d'entités via « MQTT Discovery ». La version actuelle prend en charge les listes de colis issues d'un compte DHL, les numéros de suivi DHL (optionnels) ainsi que le suivi des colis Hermes.

- [Ouvrir la documentation de Parcel-to-MQTT](/fr/projects/parcel-to-mqtt/)
- [Ouvrir le paquet dans le dépôt d'add-ons partagé](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt)
- [Ouvrir le dépôt archivé sur GitHub](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adapté de : [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## Autres domaines de projet {#weitere-projektbereiche}

- [Ouvrir les projets C#](/fr/projects/)
- [Ouvrir divers projets](/fr/projects-diverse/)
- [Ouvrir ATLAS](/fr/projects/atlas/)
