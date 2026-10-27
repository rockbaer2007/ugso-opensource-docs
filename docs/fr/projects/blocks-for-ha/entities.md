---
title: Entités Home Assistant
---

# Entités Home Assistant

Depuis **0.1.44**, les champs appropriés des blocs simples et avancés ouvrent une sélection avec recherche. Une petite flèche les signale. **HA-Auswahl laden** et **Neu laden** actualisent les catalogues en lecture seule. Les actions viennent de HA ; les cibles suivent `entity_id`, `device_id`, `area_id`, `floor_id` ou `label_id` : entités, appareils, zones, étages ou étiquettes. Les quatre derniers catalogues ne sont pas filtrés par action.

**Mehrere Ziele auswählen** permet plusieurs cibles dans les champs prenant en charge les listes. IDs manuels, listes JSON et modèles Jinja pris en charge restent disponibles, y compris le texte multiligne intégral. Changer le type de cible ne réécrit pas les IDs existants. Sans catalogue d’actions, les exemples courants sont explicitement signalés ; les catalogues indisponibles permettent la saisie manuelle. Les menus spécialisés sont conservés. Noms de variables, IDs de déclencheurs, attributs, texte libre et données complexes ne reçoivent pas de sélection HA générique.

Installer **0.1.44** puis redémarrer l’application. Le serveur lit les entités et actions via l’[API REST](https://developers.home-assistant.io/docs/api/rest/) et les registres de cibles via l’[API WebSocket](https://developers.home-assistant.io/docs/api/websocket/). Les permissions manquantes affectent seulement la liste concernée. Aucun jeton HA n’est envoyé au navigateur. La connexion et le nombre d’entités apparaissent dans la barre des réglages.

Cliquer sur un champ d’entité d’un bloc ouvre le sélecteur. Chercher par nom ou ID puis choisir une ligne. Les noms affichés viennent de votre installation et ne sont pas traduits. Les mots de recherche peuvent correspondre au nom ou à l’ID. Le choix remplit le champ actuellement modifié.

Le filtre suit le type du bloc : une lampe pour une action de couleur, un script pour un appel de script, le domaine approprié pour un assistant. Les actions génériques peuvent avoir une cible vide si leur service le permet. Les autres IDs doivent respecter `domaine.identifiant`.

La saisie manuelle reste possible, y compris hors HA. En cas de connexion indisponible, aucun état d’entité simulé n’est présenté comme une connexion réelle. Le chargement est une lecture : il n’exécute pas l’automatisation et n’écrit pas dans HA.

Les blocs standard avec sélecteur d’entité et les paquets personnalisés déclarant un champ `entity` utilisent ce mécanisme. La liste contient uniquement les informations publiques utiles à l’éditeur, sans attributs arbitraires ou jetons. Ne pas coller de secrets dans les champs de données ou projets.

Installer une fois la dépendance avec `python -m pip install --require-hashes -r requirements.txt`, puis lancer le service local avec `npm run entities`. Docker installe automatiquement la dépendance. Les 163 types de blocs, filtres, cinq types de cibles, listes et Jinja sont vérifiés automatiquement. Les tests serveur utilisent des réponses HA simulées ; vérifier ensuite l’exécution dans Home Assistant.

[Catalogue des blocs](./blocks) · [Documentation Ingress HA](https://developers.home-assistant.io/docs/add-ons/presentation/#ingress).

:::: details Référence détaillée issue de la documentation allemande

## Sélectionner des entités {#entitaten-auswahlen}

Depuis la version **0.1.44**, les champs d'action et de cible appropriés, présents dans les blocs simples et avancés, ouvrent une interface de sélection avec fonction de recherche. Une petite flèche indique ces champs. Les options **Charger la sélection HA** (dans la barre d'outils) et **Recharger** (dans la boîte de dialogue) permettent de mettre à jour les catalogues disponibles.

![Sélection d'entités avec résultat de recherche](/assets/blocks-for-ha/entity-picker.png)

L'image utilise des entités de test simulées et l'interface en allemand. Depuis la version 0.1.46, l'interface s'adapte à la langue choisie pour l'application (DE/EN/FR). Les noms des entités sont repris tels quels depuis votre installation HA.

### Utilisation {#bedienung}

1. Cliquez sur l'identifiant (ID) de l'entité au sein du bloc.
2. Effectuez une recherche par nom ou par identifiant. Si vous utilisez plusieurs termes de recherche, ils doivent tous correspondre. Les 150 premiers résultats sont affichés ; affinez votre recherche si la liste est trop longue.
3. Sélectionnez un résultat et cliquez sur **Appliquer**. Le bloc ne sera mis à jour qu'après cette action. Si vous cliquez sur **Annuler** ou appuyez sur la touche Échap, le bloc restera inchangé.
4. Vous pouvez également saisir directement un identifiant (par exemple `light.wohnzimmer`). Cette méthode fonctionne même hors ligne ou pour des entités qui n'ont pas encore été chargées.

La liste affiche le nom, l'identifiant et l'état actuel (y compris l'unité de mesure). Ces états constituent un **instantané** ; ils ne permettent pas un suivi en continu et ne servent pas de blocs de valeurs de capteurs pour des scénarios d'automatisation.

| Bloc | Sélection |
| --- | --- |
| Déclencheurs et conditions basés sur un état ou une valeur numérique | Toutes les entités chargées |
| Éclairages (avec couleur/luminosité) | Uniquement `light` |
| Script HA (Home Assistant) | Uniquement `script` |
| Assistants (Helpers) | Selon le type sélectionné : `input_boolean`, `counter` ou `timer` |
| Activer/désactiver/basculer, mettre à jour une entité, action HA générique | Toutes les entités chargées ; veuillez vérifier si l'action spécifique est prise en charge par HA |

Les champs d'action affichent les actions signalées par Home Assistant (HA). Les entités cibles sont filtrées en fonction des domaines spécifiés dans la description ou le nom de l'action. La sélection de la cible suit les catégories `entity_id`, `device_id`, `area_id`, `floor_id` ou `label_id` : entités, appareils, zones, étages ou étiquettes. Les quatre derniers catalogues ne sont pas filtrés en fonction de l'action. La **sélection de plusieurs cibles** permet d'obtenir des listes dans les champs compatibles. Les identifiants personnalisés, les listes JSON et les modèles Jinja pris en charge restent disponibles ; le texte Jinja multiligne est conservé dans son intégralité. La modification du type de cible n'entraîne pas la réécriture des identifiants existants.

Les scènes et les assistants (« helpers ») proposent des domaines d'entités pertinents ; les limites numériques étendues incluent également les capteurs et les assistants numériques, tandis que les champs liés au temps englobent les assistants temporels et les capteurs. La saisie manuelle de nombres ou de durées reste possible. Les menus déroulants spécialisés sont conservés. Les noms de variables, les identifiants de déclenchement (« trigger IDs »), les attributs, les champs de texte libre et les données complexes ne sont pas soumis aux menus de sélection génériques de Home Assistant (HA). La modification d'un identifiant ne met pas à jour les références présentes dans les données Jinja ou JSON saisies manuellement. En l'absence de catalogue d'actions, des exemples courants — explicitement identifiés comme tels — sont affichés ; si aucun catalogue de cibles n'est disponible, la saisie manuelle d'identifiants est autorisée.

### Application et données HA {#ha-app-und-daten}

Mettez à jour le dépôt dans le HA App Store, installez la **version 0.1.44** et redémarrez l'application. L'application nécessite `homeassistant_api: true` et utilise `SUPERVISOR_TOKEN` côté serveur. Les entités et les actions sont récupérées via l' [API REST](https://developers.home-assistant.io/docs/api/rest/), tandis que les enregistrements de cibles sont accessibles via l' [API WebSocket](https://developers.home-assistant.io/docs/api/websocket/). L'absence d'autorisations dans le registre n'affecte que la liste spécifique concernée. Aucune saisie de jeton (« token ») n'est requise dans l'éditeur.

Le navigateur ne reçoit que des métadonnées sélectives : ID, nom d'affichage, domaines et, pour les entités, l'état et l'unité. Aucun autre attribut ni identifiant d'accès n'est transmis. Les points de terminaison se limitent à la lecture des catalogues et n'exécutent aucune action HA (Home Assistant). Le serveur ne suit pas les redirections impliquant des identifiants d'accès.

La liste est issue de la liste des états de HA, et non de l'ensemble du registre des entités. Les entités désactivées ou celles qui ne sont pas encore disponibles (et n'ont donc pas d'état) peuvent être absentes. `unknown`/`unavailable` sont affichés s'ils sont présents dans la liste. En cas d'erreur de chargement, la liste précédente est écartée ; les ID de bloc existants sont toutefois conservés.

Les valeurs de champ sélectionnées sont stockées dans le projet JSON et dans le fichier YAML. Le catalogue, les noms, l'aperçu des états et les identifiants d'accès ne sont ni enregistrés ni exportés. L'ensemble des 163 types de blocs est conservé. Avant toute mise à jour, téléchargez votre projet local via l'option **Sauvegarder le projet** ; une sauvegarde du code source ne contient pas la session du navigateur.

### Développement local {#lokale-entwicklung}

La dépendance Python doit être installée une fois via `python -m pip install --require-hashes -r requirements.txt`. Avec Docker, cette installation est automatique.

`npm run dev` fonctionne seul avec des ID définis manuellement. Pour établir une connexion, lancez également Python 3 : `npm run entities`. Définissez les variables d'environnement `BLOCKS_HA_URL` (adresse de base sans `/api`, par exemple `http://homeassistant.local:8123`) et `BLOCKS_HA_TOKEN` uniquement au niveau du processus serveur. Le serveur Vite, situé sur `127.0.0.1:4180`, transmet la requête au pont local (bridge) sur `127.0.0.1:9001`. Ne saisissez jamais d'identifiants d'accès dans le code source ou dans les fichiers du projet.

La version Docker lance simultanément le pont (bridge) et l'interface web. En dehors de HA, si des identifiants sont définis, il convient de restreindre l'accès à une liaison locale uniquement ou d'utiliser une interface intermédiaire authentifiée ; un système de connexion utilisateur autonome n'est pas encore implémenté. Au sein de HA, l'accès est protégé par Ingress.

### Tests {#prufung}

La compatibilité avec les projets/fichiers YAML, les fonctions de recherche et de filtrage, l'annulation, la saisie manuelle, la gestion des erreurs, l'affichage sur mobile ainsi que l'ensemble de la chaîne Docker ont été vérifiés face à un serveur HA simulé. Un test pratique dans une installation HA réelle reste à effectuer. La sélection d'une entité ne garantit pas que l'appareil choisi prend effectivement en charge l'action sélectionnée.

::::
