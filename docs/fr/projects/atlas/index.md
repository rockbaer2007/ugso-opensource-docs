---
layout: home
title: ATLAS
description: Présentation du framework ATLAS et de son application pour Home Assistant.

hero:
  name: ATLAS
  text: Framework d'applications modulaire
  tagline: Un framework TypeScript modulaire pour créer des applications réutilisables, des plugins et des outils liés à Home Assistant.
  actions:
    - theme: brand
      text: Architecture
      link: /fr/projects/atlas/overview
    - theme: alt
      text: État du développement
      link: /fr/projects/atlas/development-status
    - theme: alt
      text: Home Assistant
      link: /fr/projects/atlas/homeassistant
    - theme: alt
      text: Plugins ATLAS
      link: /fr/projects/atlas-plugins/

features:
  - icon: modules
    title: Architecture modulaire
    details: Séparation claire entre Core, Foundation, Runtime, Renderer, Home Assistant, Theme et Devtools.
  - icon: gear
    title: Fondations Runtime
    details: Services, injection de dépendances, événements et autres éléments essentiels de l'exécution.
  - icon: plugin
    title: Extensible par plugins
    details: ATLAS fournit la plateforme et une documentation dédiée aux auteurs de plugins.
  - icon: home
    title: Intégration Home Assistant
    details: Les panneaux d'état, la sélection d'entités, l'export de cartes et la vérification des ressources Lovelace évoluent progressivement.
  - icon: test
    title: Testable
    details: Des contrats clairs, des implémentations de référence et des tests automatisés en constituent la base.
  - icon: package
    title: Monorepo
    details: Les paquets sont gérés avec les espaces de travail pnpm et des responsabilités distinctes.
---

## État du projet

ATLAS est en cours de développement. L'effort porte actuellement sur
l'application ATLAS pour Home Assistant, qui comprend l'Administration, le Hub
des plugins, Card Editor et File Studio.

L'Administration et le Hub des plugins prennent en charge l'allemand, l'anglais
et le français. Le choix de langue est mémorisé et partagé entre les deux
interfaces, même lorsqu'elles utilisent des ports d'application différents. Un
paramètre de langue présent dans l'URL d'un plugin reste prioritaire.

::: warning Projet en développement
ATLAS n'est pas encore déclaré prêt pour un usage en production. Les API, les
structures de paquets et les contrats internes peuvent encore évoluer.
:::

## Objectif

ATLAS vise à fournir une base technique commune à plusieurs projets UGSo :

- services réutilisables, EventBus et injection de dépendances ;
- plugins modulaires et outils de diagnostic et de développement ;
- intégrations Home Assistant, Administration et Hub des plugins ;
- File Studio pour les chemins Home Assistant autorisés ;
- Card Editor avec un flux Expert direct ;
- structures communes de thèmes et de rendu.
