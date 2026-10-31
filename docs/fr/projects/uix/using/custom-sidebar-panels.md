---
title: Raccourcis personnalisés dans la barre latérale
description: Créer des entrées UIX dans la barre latérale de Home Assistant avec une redirection interne.
---
# Raccourcis personnalisés dans la barre latérale

::: info Disponible à partir de UIX 9.0.0-beta.6
Cette fonction appartient à l’aperçu sur `dev`, et non à la base stable 8.4.0. Comparaison effectuée le 31 octobre 2026 avec la [source anglaise](https://github.com/Lint-Free-Technology/uix/blob/e6fb84dd715ea4bac9a330357705897ea8d44690/docs/source/using/custom-sidebar-panels.md).
:::

UIX peut ajouter des entrées personnalisées à la barre latérale de Home Assistant pour accéder directement à une autre page de Home Assistant. Cela facilite l’accès aux pages souvent utilisées, normalement enfouies dans les paramètres ou dans un autre panneau.

Ouvrez **Paramètres → Appareils et services → UI eXtension → Configurer**, puis sélectionnez **Manage custom sidebar panels** (gérer les panneaux personnalisés de la barre latérale). Pour ajouter un panneau, choisissez son icône, saisissez son titre et sélectionnez sa destination avec le sélecteur de navigation.

Activez **Admin required** pour réserver l’accès au panneau aux comptes administrateurs.

Les destinations doivent être des chemins de navigation internes à la même instance Home Assistant. Ces panneaux ne redirigent pas vers des sites externes.

Chaque panneau possède une URL interne stable, gérée par UIX. Vous pouvez modifier son titre, son icône et sa destination sans le recréer. Sa suppression retire immédiatement l’entrée de la barre latérale.

::: tip Ordre de la barre latérale
Chaque utilisateur peut [réorganiser ou masquer les entrées de la barre latérale dans son profil Home Assistant](https://www.home-assistant.io/dashboards/dashboards/#reorganizing-items-in-the-sidebar).
:::

::: info Fonctionnement de la redirection
Un panneau personnalisé est une redirection, pas une copie de la page cible. Lorsqu’il est sélectionné, UIX remplace son URL par la destination configurée. L’historique du navigateur ne contient donc pas d’étape de redirection supplémentaire.
:::
