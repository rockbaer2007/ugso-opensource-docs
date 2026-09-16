---
title: Dashboard Layout Card V2
description: Dashboard Layout Card V2 pour Home Assistant avec menu latéral, sous-menus, Sections V2, options kiosk, export de sauvegarde et éditeur multilingue.
---
# Dashboard Layout Card V2

**Dashboard Layout Card V2** est un fork installable en parallèle de la célèbre Lovelace `layout-card`. Elle ne remplace pas la carte originale. Elle ajoute ses propres types de layout `*-v2`, un menu latéral, des sous-menus, des options kiosk et un éditeur étendu pour les tableaux de bord Home Assistant.

| Champ | Valeur |
| --- | --- |
| Dépôt | [rockbaer2007/lovelace-layout-card-v2](https://github.com/rockbaer2007/lovelace-layout-card-v2) |
| Statut | expérimental, utilisable |
| Installation | HACS comme dépôt frontend personnalisé |
| Catégorie | HA Dashboard -> Extensions de tableau de bord |

## Vue d'ensemble

Cette extension est moins une simple carte Lovelace qu'une extension de vue/tableau de bord. L'objectif est de créer un tableau de bord Home Assistant flexible avec un menu latéral, des sous-pages et une présentation compacte pour tablettes ou écrans kiosk.

Fonctions principales :

- types de layout V2 dédiés : `sections-layout-v2`, `masonry-layout-v2`, `horizontal-layout-v2`, `vertical-layout-v2`, `grid-layout-v2`
- menu latéral à gauche ou à droite
- mode icônes uniquement pour mobile, tablette et kiosk
- colonne de sous-menu par entrée principale
- entrée Home et sous-vues
- nouvelles sous-vues en Sections V2 par défaut
- héritage du thème depuis la vue Home
- horloge numérique ou analogique, date et jour de la semaine
- popup de notification et valeurs d'état
- styles globaux, couleurs individuelles par bouton et favoris de couleurs
- réglages d'opacité pour menu, carte/contenu, notification, valeurs d'état et séparateurs
- export YAML de sauvegarde dans l'éditeur
- sélection de langue Debug pour les captures d'écran
- masquage optionnel de l'en-tête et de la barre latérale Home Assistant

![Vue Dashboard Layout Card V2](/images/dashboard-layout-card-v2/view.png)

Les layouts V2 apparaissent dans le sélecteur normal de layout de vue Home Assistant.

![Sélection du layout Dashboard Layout Card V2](/images/dashboard-layout-card-v2/view-layout-selection.png)

Les vues Sections V2 se comportent en mode édition de manière proche de la vue Sections native de Home Assistant. Les sections peuvent être déplacées avec la poignée à trois lignes, et le nouvel ordre est enregistré dans la vue.

<video controls src="/images/dashboard-layout-card-v2/demo.mp4" style="width: 100%; border-radius: 8px;"></video>

## Installation via HACS

Ajoutez le dépôt comme dépôt frontend personnalisé :

```text
https://github.com/rockbaer2007/lovelace-layout-card-v2
```

Home Assistant doit ensuite charger cette ressource :

```text
/hacsfiles/lovelace-layout-card-v2/dashboard-layout-card-v2.js
```

Si une ancienne version apparaît encore après une mise à jour :

- actualiser les dépôts HACS
- vider le cache du navigateur
- recharger fortement le tableau de bord

## Helpers nécessaires

Seules les fonctions activées ont besoin de helpers. Créez-les dans Home Assistant sous **Paramètres > Appareils et services > Helpers**.

| Entité | Type de helper | Utilisation | Obligatoire ? |
| --- | --- | --- | --- |
| `input_text.dashboard_notification` | Texte | Texte de notification optionnel. Vide, `unknown` et `unavailable` masquent la notification. | Seulement si `menu.notify.enabled` est utilisé. |
| `input_boolean.dashboard_holiday` | Interrupteur | Symbole du jour optionnel pour les jours fériés. | Seulement si le symbole doit réagir aux jours fériés. |
| `input_boolean.dashboard_birthday` | Interrupteur | Symbole du jour optionnel pour les anniversaires. | Seulement si le symbole doit réagir aux anniversaires. |
| `input_boolean.dashboard_christmas` | Interrupteur | Symbole du jour optionnel pour Avent/Noël. | Seulement si le symbole doit réagir à Avent/Noël. |

Les valeurs d'état n'ont pas besoin de helpers spéciaux. Elles peuvent utiliser toute entité Home Assistant lisible, par exemple des capteurs, binary sensors ou template sensors.

![Indication helper manquant Dashboard Layout Card V2](/images/dashboard-layout-card-v2/notify-helper-missing.png)

## Notification et valeurs d'état

La boîte de notification optionnelle apparaît au-dessus des valeurs d'état dans le menu latéral. Un helper texte comme `input_text.dashboard_notification` est recommandé. Tant que l'entité est absente, vide, `unknown` ou `unavailable`, la boîte reste masquée. Si le helper n'existe pas encore, l'éditeur affiche une courte indication pour le créer.

Dès que le helper contient du texte, le message apparaît dans le menu, par exemple pour des pannes, des notes de maintenance ou de courts messages globaux. Jusqu'à quatre valeurs d'état peuvent être affichées en dessous. Les valeurs numériques sont formatées de manière compacte avec au maximum une décimale.

En mode icônes uniquement, l'horloge, la date et les valeurs d'état sont masquées ; les notifications restent disponibles via un bouton compact avec popup.

![Notification et valeurs d'état Dashboard Layout Card V2](/images/dashboard-layout-card-v2/notify-and-status.png)

## Menu, sous-menus et couleurs

Jusqu'à 600 pixels de largeur d'écran, les boutons du menu affichent automatiquement uniquement les icônes. Le mode icônes uniquement peut aussi être activé manuellement, par exemple pour les tablettes kiosk ou les écrans muraux.

Les entrées du menu peuvent avoir des sous-menus. Le sous-menu est rendu comme une colonne d'icônes séparée à côté du menu principal et n'affiche que les sous-pages de l'entrée principale actuellement sélectionnée. Le premier bouton du sous-menu peut servir de page de départ pour l'entrée principale, ou être désactivé afin que l'entrée principale ouvre directement la première sous-page.

Les entrées Home, menu principal et sous-menu peuvent définir leurs propres couleurs : couleur d'icône, couleur d'icône active, arrière-plan d'icône, arrière-plan d'icône actif, couleur du bouton et couleur du bouton actif. Les champs vides continuent d'utiliser le style global du menu.

Les champs YAML correspondants sont `icon_color`, `icon_active_color`, `icon_background_color`, `icon_background_active_color`, `tab_color` et `active_tab_color`. Un bouton de réinitialisation peut effacer uniquement ces couleurs pour l'entrée sélectionnée ; page, chemin, icône, sous-menu et couleurs globales restent inchangés.

## Onglets de l'éditeur

La fenêtre de l'éditeur s'ouvre par défaut plus largement, avec 80 % de la largeur de la fenêtre, et peut être agrandie à 95 % par double-clic sur la barre supérieure.

| Onglet | Options |
| --- | --- |
| Menu | Position du menu (`left`, `none`, `right`), titre du menu et mode icônes uniquement global. |
| Home page | Entrée Home, titre, chemin, icône, couleurs Home, colonnes Sections V2 et héritage du thème. |
| Display | Horloge, date, jour de la semaine, couleurs de l'horloge et helpers pour le symbole du jour. |
| Pages | Pages principales, espaces, séparateurs, layouts, couleurs par entrée et comportement du premier bouton de sous-menu. |
| Submenu | Sous-pages de la page principale sélectionnée avec couleurs et layout. |
| Messages | Notification, bordures, opacité et jusqu'à quatre valeurs d'état. |
| Styles Global | Couleurs globales, tailles, formes d'icônes, arrière-plans, opacités et effets 3D. |
| Colors | Jusqu'à 20 couleurs favorites réutilisables. |
| Backup | Export YAML du tableau de bord actuel vers l'ordinateur local. |
| Advanced | Réglages Home Assistant chrome, utilisateurs visibles, Debug et JSON avancé. |

## Export YAML

L'onglet **Backup** peut exporter l'état actuel du tableau de bord comme fichier YAML sur l'ordinateur local. L'export ne modifie pas Home Assistant et sert de sauvegarde avant de grands tests ou changements de design.

## Sélecteur de langue Debug

Pour les captures d'écran de documentation ou les tests de langue, la langue affichée peut être forcée dans l'éditeur sous **Advanced > Special options / edit JSON > Debug** ou directement en YAML.

```yaml
debug:
  language: fr # vide/default, de, en ou fr
```

Avec une valeur vide, Dashboard Layout Card V2 utilise automatiquement la langue Home Assistant ou navigateur et revient à l'anglais si nécessaire.

## Images d'arrière-plan

Les images verticales fonctionnent le mieux pour les arrière-plans de menu. Un rapport pratique est environ `1:2,5` largeur:hauteur. D'autres formats sont possibles, mais `cover` peut les recadrer selon la hauteur visible du menu.

Les images doivent être placées dans le dossier `www` de Home Assistant, par exemple :

```text
/config/www/image/back2.jpg
```

Dans l'éditeur, utilisez ensuite :

```text
/local/image/back2.jpg
```

Veuillez utiliser uniquement vos propres images ou des images avec une licence libre/open-source compatible.

## Exemple

```yaml
views:
  - type: custom:sections-layout-v2
    path: home
    title: Home
    icon: mdi:home
    debug:
      language:
    layout:
      dashboard_layout_v2:
        inherit_theme: true
        menu:
          position: left
          title: Maison
          show_home: true
          icon_only: false
          home:
            title: Home
            path: home
            icon: mdi:home
          clock: analog
          analog_hour_marks: false
          analog_seconds: false
          date: true
          weekday: long
          style:
            icon_color: "#fbff00"
            icon_background_color: "#ffffff"
            icon_shape: circle
            icon_size: 28px
            active_tab_color: "#333aff"
            inactive_tab_color: "#191c3e"
            tab_border_color: "#fdf9d3"
            card_border_color: "transparent"
            background_mode: image
            background_image: /local/image/back2.jpg
        pages:
          - title: Sous-sol
            path: sous-sol
            icon: mdi:home-floor-negative-1
            layout_type: custom:sections-layout-v2
            max_columns: 3
          - type: divider
            color: "#ffffff"
            divider_opacity: 100
          - title: Jardin
            path: jardin
            icon: mdi:flower
            layout_type: custom:sections-layout-v2
            max_columns: 4
    sections:
      - type: grid
        cards: []
```
