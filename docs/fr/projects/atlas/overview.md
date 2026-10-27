---
title: Architecture
description: Packages, événements, services et principes de l’architecture modulaire ATLAS.
---

# Architecture

ATLAS est un monorepo TypeScript modulaire. Les contrats communs séparent les
services, la présentation et l’intégration avec l’environnement hôte.

## Packages

| Package | Rôle |
| --- | --- |
| `@atlas/core` | Contrats et types centraux. |
| `@atlas/foundation` | Infrastructure et composants communs. |
| `@atlas/runtime` | Services d’exécution et conteneur de services. |
| `@atlas/renderer` | Présentation et abstractions du moteur de rendu. |
| `@atlas/homeassistant` | Intégration et workflows Home Assistant. |
| `@atlas/theme` | Thèmes et conception visuelle partagés. |
| `@atlas/devtools` | Diagnostics et outils de développement. |
| `@atlas/kernel` | Contrats des modules, conteneur de services et infrastructure. |
| `@atlas/workspace` | Contrats de préparation des espaces de travail. |
| `@atlas/file-studio` | Contrats et adaptateur Runtime internes ; le plugin web installable reste externe. |
| `@atlas/notifyarchive` | Contrats internes des archives de notifications. |

## Principes d’architecture

- Séparer les contrats de leurs implémentations.
- Utiliser de petits modules remplaçables.
- Concevoir des composants testables.
- Définir explicitement les interfaces et les dépendances.
- Fournir des implémentations de référence.
- Préparer l’extension par des plugins à long terme.

## Événements

Les contrats comprennent `Event`, `EventBus`, `Handler`, `Subscription`,
`Filter`, `Publisher` et `Subscriber`. `DefaultEventBus` fournit
l’implémentation de référence.

## Services et injection de dépendances

Les descripteurs et l’enregistrement des services, l’injection de dépendances
et les conteneurs permettent de résoudre les services de manière contrôlée.

## Utilisation actuelle et perspectives {#utilisations-prevues}

L’administration et le plugin de référence Home Assistant Card Editor sont déjà disponibles. D’autres outils et diagnostics sont intégrés via des plugins.

ATLAS vise les outils Home Assistant, les composants de tableaux de bord,
les applications de diagnostic et les applications web ou de bureau basées
sur des plugins. La carte Lovelace UV reste un projet ultérieur.

Les contrats sont encore en développement : cette architecture ne constitue
pas une promesse d’API de plugin stable. Voir l’[état du développement](/fr/projects/atlas/development-status).
