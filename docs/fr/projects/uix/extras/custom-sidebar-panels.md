---
title: Raccourcis personnalisés de barre latérale
description: Créer des liens UIX vers des pages Home Assistant et des sites web.
---
# Raccourcis personnalisés de barre latérale

::: info UIX 9.0.0
Les raccourcis internes et externes font partie de la version stable **9.0.0** et nécessitent **Home Assistant 2026.11.0 ou ultérieur**. La nouvelle restriction aux navigateurs de bureau décrite ci-dessous provient de l’aperçu **9.1.0-beta.1** sur `dev`.
:::

UIX peut ajouter des entrées à la barre latérale de Home Assistant pour ouvrir une autre page Home Assistant ou un site web. Cela facilite l’accès aux pages fréquemment utilisées sous les paramètres et aux services web associés.

Ouvrez **Paramètres → Appareils et services → UI eXtension → Configurer**, puis sélectionnez **Manage custom sidebar panels**. Choisissez l’icône et saisissez le titre et la destination.

Activez **Admin required** pour réserver l’entrée aux comptes administrateurs.

La destination peut être un chemin Home Assistant commençant par `/`, comme `/config/dashboard`, ou une URL absolue `http` ou `https`. Les autres schémas d’URL ne sont pas acceptés.

Activez **Open in new tab (desktop only)** pour ouvrir un chemin interne Home Assistant dans un nouvel onglet d’un navigateur de bureau. L’onglet Home Assistant courant revient à la page précédemment affichée. Dans l’application Companion, UIX navigue plutôt vers le chemin HA à l’intérieur de l’application. Cette option ne s’applique pas aux URL de sites web externes, qui ne peuvent pas s’ouvrir à l’intérieur de l’application Companion.

::: info Nouvel onglet et blocage des fenêtres surgissantes
L’ouverture d’un chemin interne HA dans un nouvel onglet dépend de la politique du navigateur de bureau concernant les fenêtres surgissantes. UIX tente de l’ouvrir lors de la sélection du panneau, sans pouvoir le garantir. En cas de blocage, le chemin HA s’ouvre dans l’onglet courant.
:::

Chaque panneau possède une URL interne stable gérée par UIX. Vous pouvez donc modifier son titre, son icône et sa destination sans le recréer. Sa suppression retire immédiatement l’entrée de la barre latérale.

::: tip Ordre de la barre latérale
Chaque utilisateur peut [réorganiser et masquer les entrées](https://www.home-assistant.io/dashboards/dashboards/#reorganizing-items-in-the-sidebar) depuis son profil.
:::

::: info Redirection
Un panneau personnalisé est une redirection, pas une copie de la page ni un iframe. Pour une destination interne, UIX remplace l’URL du panneau par la destination configurée afin de ne pas ajouter d’étape de redirection à l’historique du navigateur.
:::

Source : [documentation originale anglaise UIX](https://uix.lf.technology/extras/custom-sidebar-panels/), Lint-Free-Technology/uix, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Revue complémentaire des sources du 7 novembre 2026 : [`dev e7b5bdd`](https://github.com/Lint-Free-Technology/uix/commit/e7b5bdd811a53960e9559c53a354c7855c537286), incluant [`1d53592`](https://github.com/Lint-Free-Technology/uix/commit/1d53592b241ec8666b34d67056671bb37d1c2a1f). L’indication d’aperçu ne constitue pas une publication stable.
