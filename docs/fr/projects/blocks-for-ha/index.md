---
title: UGSo Blocks for HA
description: Créer visuellement des automatisations Home Assistant avec Blockly, YAML et Jinja.
---

# UGSo Blocks for HA

UGSo Blocks for HA assemble des automatisations Home Assistant avec des blocs visuels. Les déclencheurs, conditions et actions produisent du YAML natif ; les expressions utilisent Jinja dans Home Assistant. Blockly fournit l’éditeur, pas le moteur d’exécution de HA.

**Version 0.1.37 · 119 types de blocs · code source Apache-2.0**

[Code source sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha) · [Documentation DE](/projects/blocks-for-ha/) · [Documentation EN](/en/projects/blocks-for-ha/)

## Langue des blocs

Le sélecteur **Langue des blocs** propose **Langue du système**, **Deutsch (DE)**, **English (EN)** et **Français (FR)**. Le mode système utilise les langues préférées du navigateur, y compris les variantes comme `fr-CA` ou `de-CH`. Si aucune langue prise en charge n’est trouvée, l’anglais est utilisé.

Ce choix concerne les libellés, menus déroulants, infobulles, catégories, recherche de blocs et dialogues natifs de Blockly, notamment la création de variables. Les autres commandes de l’application et ses diagnostics restent actuellement en allemand. La préférence est locale à ce navigateur et indépendante des thèmes.

Un changement sauvegarde le projet puis recharge l’éditeur. Terminer les blocs incomplets avant de changer de langue. Si le stockage du navigateur est indisponible, l’éditeur conserve les blocs et refuse le rechargement. Les IDs d’entités, noms de variables, textes saisis, modèles, paramètres et YAML ne sont pas traduits. Les blocs des paquets personnalisés conservent la langue définie par leur auteur.

Les captures du [catalogue des blocs](./blocks) sont générées avec les véritables blocs français. Les pages DE et EN utilisent leurs propres images.

## Installation et connexion

L’application est distribuée dans le [dépôt des applications HA UGSo](https://github.com/rockbaer2007/ugso-ha-mqtt-addons). Elle peut aussi être lancée localement depuis `blocks_for_ha` avec `npm install` puis `npm run dev` sur `http://127.0.0.1:4180/`. Pour compiler : `npm run build`.

Dans HA, ouvrir l’application via Ingress. La connexion aux entités utilise le service serveur supervisé, sans transmettre de jeton HA au navigateur. Hors HA, l’éditeur fonctionne avec saisie manuelle des IDs. Voir [Entités](./entities).

## Construire une automatisation

1. Donner un nom à l’automatisation et choisir son mode : `single`, `restart`, `queued` ou `parallel`. Les deux derniers proposent une limite maximale.
2. Placer les déclencheurs orange dans **Quand**, les conditions violettes dans **Seulement si**, puis les actions bleues dans **Alors**.
3. Rechercher ou saisir les IDs des entités. Remplacer les IDs d’exemple par ceux de son installation.
4. Vérifier le YAML et les diagnostics. Un indicateur valide vérifie la structure ; il ne confirme pas la disponibilité des services ou entités dans HA.
5. Copier le format **Einzelne Automation · HA-Editor** dans l’éditeur d’automatisation HA, via **Modifier en YAML**. Enregistrer et vérifier dans HA.

Les connexions sont typées : un déclencheur ne peut pas rejoindre une chaîne d’actions. Les valeurs numériques fixes et celles calculées à l’exécution ont des usages différents. Les blocs isolés ou incomplets peuvent empêcher l’export au lieu d’être ignorés.

## Importer et sauvegarder

**Kopieren** copie le YAML ; **Speichern** télécharge un fichier YAML nommé d’après l’automatisation. **Öffnen** lit un fichier pris en charge. Le format liste contient une seule automatisation. L’import ne convertit pas arbitrairement tout le YAML Home Assistant : les éléments non représentables sont refusés.

Pour coller du YAML, choisir **YAML → Code importieren**. Le panneau de sortie devient une zone de saisie ; **Importieren** remplace le bouton de sauvegarde. Taille maximale : **1 Mo en UTF-8**.

- Sans coche, l’import ajoute les déclencheurs, conditions et actions au projet valide actuel. Les conditions sont combinées avec ET ; les déclencheurs ajoutés peuvent entraîner davantage d’exécutions. Nom et réglages actuels sont conservés.
- Avec **Aktuelle Automation vollständig ersetzen**, une confirmation demande de remplacer tous les blocs. Après acceptation, les métadonnées et blocs importés remplacent le projet. Annulation ou erreur : état précédent conservé.

**Projekt sichern** télécharge le projet JSON complet, avec disposition et définitions des paquets utilisés. **Projekt öffnen** restaure ce projet. Le dernier état est également enregistré localement dans le navigateur. Cette sauvegarde locale ne remplace pas un fichier de sauvegarde.

## Espace de travail

Les commandes permettent d’annuler/rétablir, d’ajuster la vue et de chercher les blocs déjà placés. La recherche de la boîte à outils, en bas du menu, cherche les blocs disponibles. `Ctrl+F` ou `Cmd+F` dans Blockly ouvre la recherche de l’espace de travail ; Entrée/Maj+Entrée parcourt les résultats, Échap ferme la recherche. Le bouton **?** affiche les raccourcis de navigation.

Le panneau YAML peut être replié vers la droite ; l’éditeur récupère sa largeur. Le réglage est enregistré localement. Sur petit écran, le panneau replié forme une barre sous l’éditeur. Aucun changement du projet ou du YAML.

Le thème de l’application **Hell / Dunkel / System** est indépendant des palettes Blockly **UGSo Standard / Dark / Modern / Tritanopia**. Voir [Thèmes et zoom](./themes).

## Guides

| Sujet | Guide |
| --- | --- |
| Tous les types, images et fonctions | [Catalogue des blocs](./blocks) |
| Dates, comparaisons d’heure, soleil | [Date et heure](./time) |
| Nombres, booléens, dates, JSON | [Conversion](./conversion) |
| Délais, objets, conditions et choix | [Délais, objets et logique](./flow) |
| Calculs, textes, listes et boucles | [Mathématiques, textes, listes et boucles](./collections) |
| Différences Blockly/ioBroker/HA | [Comparaison et fonctions](./blockly-audit) |
| Connexion en lecture aux entités | [Entités](./entities) |
| Éditeur de paquets JSON/ZIP | [Blocs personnalisés](./custom-blocks) |
| Code copiable et téléchargements | [Catalogue des paquets](./catalog/) |

## Limites et direction

Les scripts ioBroker ne sont pas exécutés dans HA. Les intervalles nommés, `sendTo`, objets ioBroker et JSONata nécessiteraient une adaptation réelle. Le navigateur ne simule pas ces capacités. Les actions sont exécutées uniquement après utilisation du YAML dans Home Assistant.

Les prochaines possibilités comprennent la sélection des services et appareils HA, les variables typées, davantage de formes dans l’éditeur de blocs personnalisés et la gestion des versions de paquets. Le Block Factory original reste une référence ; ses définitions JSON seules ne contiennent pas un générateur HA complet.

## Licences

Projet communautaire indépendant, sans affiliation officielle à Home Assistant ou Blockly. Blockly est une bibliothèque de la Raspberry Pi Foundation, initialement développée chez Google. Les dépendances sont intégrées localement ; aucune bibliothèque Blockly n’est chargée depuis un CDN. Blockly et ses plugins : Apache-2.0 ; YAML : ISC ; fflate : MIT. Les notices sont incluses dans l’application.

<a class="blockly-attribution" href="https://www.blockly.com/" target="_blank" rel="noopener noreferrer"><img class="badge-light" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-white.svg" alt="Built with Blockly" width="87" height="32"><img class="badge-dark" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-black.svg" alt="Built with Blockly" width="87" height="32"></a>

Depuis **0.1.28** : **États en liste JSON**, par exemple `["1_single","1_double"]` ; IDs facultatifs dans tous les déclencheurs standard ; **Déclenché par ID** comme condition native (ID individuel ou liste JSON). Les actions HA génériques acceptent **Cibles en liste JSON**, des métadonnées facultatives et conservent explicitement les données vides. Les automatisations à quatre boutons et quatre branches `choose` sont entièrement importables.

La sortie **Automatisation individuelle · Éditeur HA** omet l’`id` principal. Les IDs des déclencheurs restent présents. Les projets et la sortie **liste automations.yaml** conservent l’ID existant de l’automatisation.

[Home Assistant: Trigger IDs](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Trigger condition](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

Depuis **0.1.29**, l’espace Blockly occupe toute la hauteur du panneau jusqu’à la légende. Un panneau YAML plus haut agrandit aussi l’espace de travail ; la sortie reste repliable.

Depuis **0.1.30** : activer **Heures en liste JSON** pour plusieurs heures fixes, par exemple `["10:00:00","13:00:00","19:00:00"]`. **Tout changement** omet `to` ; **Entités en liste JSON** surveille plusieurs entités. Sans `to`, HA réagit aussi aux changements d’attributs. Les événements acceptent par exemple `timer.finished` avec un filtre de données JSON facultatif. Les conditions horaires natives conservent `before`/`after` : heures fixes, après inclusif et avant exclusif, même à travers minuit. Des bornes identiques couvrent toute la journée. Assistants horaires, modèles horaires et filtres de jours restent hors de l’import pris en charge. L’automatisation complète conserve le modèle multiligne du minuteur et les branches `choose` imbriquées.

[Home Assistant: triggers](https://www.home-assistant.io/docs/automation/trigger/) · [Time condition](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

Depuis **0.1.31**, le nouveau bloc prend en charge temperature.changed natif. Cible (JSON) : entity_id texte ou liste. Seuil (JSON) : type any, above, below, between ou outside. any exige seulement type ; above/below exigent value, between/outside value_min et value_max. Nombres : number et unit_of_measurement (°C/°F). Références : entity (sensor, number ou input_number). ID facultatif. Autres cibles (zone/appareil/étiquette) non prises en charge. Les topics MQTT, qos/retain/evaluate_payload et contenus JSON/Jinja multilignes restent présents.

[Home Assistant: temperature.changed](https://www.home-assistant.io/triggers/temperature.changed/)

**0.1.32:** Calendriers et variables de réponse. [→](./blocks)

**0.1.33:** Déclencheurs numériques avec durée de maintien. [→](./blocks)

**0.1.34:** Plusieurs variables dans une action. [→](./blocks)

**0.1.35:** Délai en texte ou modèle. [→](./blocks)

**0.1.36:** Noms d’action HA dynamiques. [→](./blocks)


**0.1.37:** [Déclencheur de motif horaire](./blocks).
