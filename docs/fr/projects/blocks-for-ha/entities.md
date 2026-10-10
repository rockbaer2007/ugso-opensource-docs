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
