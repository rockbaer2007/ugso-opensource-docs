---
title: Entités Home Assistant
---

# Entités Home Assistant

Dans l’installation supervisée HA, **Entitäten laden** charge les entités depuis la connexion Ingress. Le serveur fournit ID, nom, domaine, état et unité via une API en lecture ; aucun jeton HA n’est envoyé au navigateur. La connexion et le nombre d’entités apparaissent dans la barre des réglages.

Cliquer sur un champ d’entité d’un bloc ouvre le sélecteur. Chercher par nom ou ID puis choisir une ligne. Les noms affichés viennent de votre installation et ne sont pas traduits. Les mots de recherche peuvent correspondre au nom ou à l’ID. Le choix remplit le champ actuellement modifié.

Le filtre suit le type du bloc : une lampe pour une action de couleur, un script pour un appel de script, le domaine approprié pour un assistant. Les actions génériques peuvent avoir une cible vide si leur service le permet. Les autres IDs doivent respecter `domaine.identifiant`.

La saisie manuelle reste possible, y compris hors HA. En cas de connexion indisponible, aucun état d’entité simulé n’est présenté comme une connexion réelle. Le chargement est une lecture : il n’exécute pas l’automatisation et n’écrit pas dans HA.

Les blocs standard avec sélecteur d’entité et les paquets personnalisés déclarant un champ `entity` utilisent ce mécanisme. La liste contient uniquement les informations publiques utiles à l’éditeur, sans attributs arbitraires ou jetons. Ne pas coller de secrets dans les champs de données ou projets.

Le service local peut être lancé avec `npm run entities`. Les tests vérifient le filtrage par domaine, la recherche, les IDs invalides, la saisie manuelle et l’absence d’interprétation HTML des noms d’entités.

[Catalogue des blocs](./blocks) · [Documentation Ingress HA](https://developers.home-assistant.io/docs/add-ons/presentation/#ingress).
