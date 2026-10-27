---
title: Autres exemples intéressants
description: Exemples issus de la communauté et de sources tierces concernant Home Assistant, UIX et Lovelace.
---
<a id="weitere-interessante-exemples"></a>
<a id="orientation-actuelle"></a>

# Autres exemples intéressants {#weitere-interessante-beispiele}

Nous rassemblons ici des exemples concrets externes, des « Gists » de la communauté et des idées intéressantes qui ne font pas directement partie de la documentation d'un projet ou de sa traduction.

Cette page est volontairement séparée de la documentation spécifique à chaque projet. Cela permet aux traductions de rester fidèles à l'original, tout en rendant accessibles des idées complémentaires utiles.

## Collection de thèmes UIX par Mariusthvdb {#uix-theme-sammlung-von-mariusthvdb}

Un exemple concret et complet de thèmes UIX est maintenu par Mariusthvdb sous forme de « Gist » :

- [Thèmes UIX par Mariusthvdb](https://gist.github.com/Mariusthvdb/ecdd6ac6776d501b09e859888b01a9c6)

Ce « Gist » présente, entre autres :

- Variables globales du thème UIX
- `uix-macros-yaml` avec des macros réutilisables
- Règles relatives aux icônes et aux couleurs pour les entités
- Personnalisation de la barre latérale (sidebar), de l'en-tête (header), des badges et des vues
- Animations et couleurs d'état

::: warning Exemple de la communauté
Cet exemple ne fait pas partie de la documentation officielle d'UIX et est fortement adapté à l'installation Home Assistant propre à son auteur. Utilisez-le comme source d'inspiration et adaptez les entités, libellés, couleurs, macros et la version d'UIX à votre propre installation.
:::

De courts extraits peuvent servir de référence. Le code YAML complet doit être récupéré directement depuis le Gist et vérifié avant toute utilisation.

```yaml
theme-mods:
  uix-top-app-bar-fixed: |
    header.top-app-bar {
      background: var(--header-background);
      color: var(--text-color-off);
    }

  uix-macros-yaml: |
    power_color:
      template: >
        {% for entity in label_entities('power') %}
        --uix-icon-color-for-{{ entity.replace('.','_') }}:
        {{ 'var(--success-color)' if states(entity)|int(0) < 2500 else 'var(--alert-color)' }};
        {% endfor %}
```
