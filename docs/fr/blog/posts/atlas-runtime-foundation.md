---
title: ATLAS – Runtime Foundation
description: L'état actuel du développement du framework modulaire ATLAS.
date: '2026-08-02'
author: UGSo Software
tags:
- ATLAS
- TypeScript
- Architektur
---
<a id="atlas-runtime-foundation"></a>
<a id="statut"></a>


# ATLAS – Runtime Foundation {#atlas-–-runtime-foundation}

**2 août 2026 · ATLAS**

ATLAS est un framework TypeScript modulaire destiné à des applications, des plugins et des outils liés à Home Assistant, conçus pour être réutilisables.

## État actuel {#aktueller-stand}

La structure fondamentale du dépôt (repository) et de la documentation est finalisée.

Les éléments suivants sont déjà implémentés :

- Monorepo avec des espaces de travail (workspaces) `pnpm`
- Documents de gouvernance et d'architecture
- Couche d'événements et de contrats
- Contrats d'événements publics
- Implémentation de référence `DefaultEventBus`
- Tests pour les composants de base

## Prochain sprint {#nachster-sprint}

La prochaine étape de développement consiste à :

```text
Sprint G2.5.3 – Runtime Foundation
```

L'accent est mis sur :

- Conteneurs de services
- Injection de dépendances
- Descriptions de services
- Résolution contrôlée des dépendances
- Contrats d'exécution (runtime) stables

## Objectif à long terme {#langfristiges-ziel}

ATLAS a pour vocation de constituer une base technique commune pour plusieurs projets UGSo.

La **Lovelace UV Card** reste prévue comme projet ultérieur, dédié à l'indice UV, au statut de protection et aux tableaux de bord visuels pour Home Assistant.

## En savoir plus {#mehr-erfahren}

[Ouvrir la page du projet ATLAS](/fr/projects/atlas/)
