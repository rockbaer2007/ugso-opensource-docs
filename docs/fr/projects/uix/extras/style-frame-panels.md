---
title: Styliser les panneaux intégrés dans un frame (expérimental)
description: Activer le style UIX dans les frames pris en charge des applications et des panneaux personnalisés.
---
# Styliser les panneaux intégrés dans un frame (expérimental)

Par défaut, UIX n'injecte pas de styles dans le contenu des frames. Activez ce réglage expérimental pour exécuter le moteur interne de UIX dans les frames de même origine des applications et des panneaux personnalisés pris en charge. Le style de l'élément hôte avec `uix-app` et `uix-panel-custom` n'est pas affecté par cette option.

::: warning Compatibilité avec les frameworks
Le moteur des frames a été largement testé avec le frontend de Home Assistant basé sur Lit. Les applications et panneaux personnalisés intégrés dans une iframe et développés avec d'autres frameworks peuvent avoir un cycle de vie ou un comportement DOM fantôme différent. Les panneaux dotés d'une racine DOM légère classique et sans limites de DOM fantôme fonctionnent généralement bien. Ceux qui gèrent leur DOM de façon réactive ou utilisent un DOM fantôme complexe doivent être validés pour chaque application. Inspectez la frame, testez chaque sélecteur et signalez les problèmes de compatibilité.

Dans les frames qui n'utilisent pas Lit, UIX applique une feuille de style de secours au lieu d'insérer un `uix-node` dans le DOM de l'application. Cette solution prend en charge le CSS direct, y compris les modèles, mais pas les chemins de sélecteurs YAML de UIX. Utilisez des sélecteurs CSS classiques dans le bloc de style direct.
:::

## Réglage dans l'interface de l'intégration

Cette option est **désactivée par défaut**. Pour l'activer :

1. Dans Home Assistant, ouvrez **Paramètres → Appareils et services → UI eXtension → Configurer**.
2. Choisissez **Réglages expérimentaux** dans le menu.
3. Activez **Styliser les panneaux intégrés dans un frame**.
4. Enregistrez.

Le réglage est immédiatement disponible dans toutes les sessions de navigateur connectées. Il peut être nécessaire de recharger la page pour l'appliquer à un panneau déjà affiché.

## Comportement lorsque l'option est activée

Lorsque cette option est activée :

- UIX installe son moteur interne, indépendant du type de panneau, dans les frames de même origine prises en charge pour les applications et les panneaux personnalisés.
- Pour les frames de panneaux personnalisés, le nom du panneau sert de cible de thème. Pour les applications, UIX essaie d'abord le slug complet du module complémentaire, puis son slug indépendant du dépôt.
- UIX n'ajoute un nœud de style que si le thème actif définit une cible `uix-<target>` correspondante. Les frames sans section `uix-<target>` correspondante restent inchangées.
- Si UIX détecte qu'aucun thème n'est appliqué, UIX Styling utilise le thème actuellement chargé dans le frontend de Home Assistant. Certains panneaux personnalisés, comme HACS, appliquent eux-mêmes le thème ; UIX Styling l'hérite alors.

::: tip
Le moyen le plus simple de trouver la cible `uix-<target>` consiste à consulter la console développeur du navigateur. L'information de chargement UIX générée par `uixFrame.js` ressemble à ceci :

<span style="background:#CE3226;color:white;padding:2px 5px;font-weight:bold;border-radius:5px;">💡 UIX 8.4.0 IS INSTALLED 💡 for hacs-frontend</span>

La dernière partie du message indique la cible, ici `hacs-frontend`.
:::
