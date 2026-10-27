<a id="misc-projets"></a>
<a id="statut"></a>

# Projets divers {#diverse-projekte}

Cette page rassemble d'autres projets open source UGSo qui ne font pas directement partie des outils C# ou des applications MQTT.

## <img class="package-icon" src="/images/packages/projects-ultimate-timer.png" width="32" height="32" alt="" aria-hidden="true"> Ultimate Timer {#ultimate-timer}

**Ultimate Timer**

Un « blueprint » d'automatisation pour Home Assistant permettant de créer des minuteurs réutilisables, dotés d'une logique d'arrêt (STOP) robuste, d'un état « terminé » (DONE) persistant, d'une prise en charge multi-instance et d'une option de fonctionnement via MQTT.

- <img class="package-icon" src="/images/packages/projects-ultimate-timer.png" width="32" height="32" alt="" aria-hidden="true"> [Ouvrir la documentation d'Ultimate-Timer](/fr/projects/ultimate-timer/)
- [Ouvrir le Blueprint sur GitHub](https://github.com/rockbaer2007/ha-ultimate-timer-blueprint)

## Blueprints Home Assistant {#home-assistant-blueprints}

**Blueprints Home Assistant**

Une petite collection de Blueprints Home Assistant personnalisés, conçus pour la gestion des associations, des groupes de cibles et des fonctions d'arrêt d'urgence. Elle comprend des Blueprints pour relier une source à un maximum de six cibles, une source à un groupe de cibles personnalisable, ainsi qu'une automatisation d'arrêt d'urgence qui désactive des cibles sélectionnées lors du passage de `on` à `off`.

- Association 1 vers 6 : une source permet d'activer et de désactiver simultanément jusqu'à six cibles.
- Association source vers groupe de cibles : une source permet de contrôler des entités, des appareils ou des zones choisis librement.
- Arrêt d'urgence (source désactivée vers cibles désactivées) : lors du passage de la source de `on` à `off`, les cibles sélectionnées sont désactivées.
- Le fichier README sur GitHub contient des boutons d'importation directe vers Home Assistant pour tous les Blueprints inclus.

- [Ouvrir les Blueprints sur GitHub](https://github.com/rockbaer2007/homeassistant-blueprints)

## Autres domaines de projet {#weitere-projektbereiche}

- [Ouvrir les projets C#](/fr/projects/)
- [Ouvrir les projets MQTT](/fr/projects-mqtt/)
- <img class="package-icon" src="/images/packages/projects-atlas.png" width="32" height="32" alt="" aria-hidden="true"> [Ouvrir ATLAS](/fr/projects/atlas/)
