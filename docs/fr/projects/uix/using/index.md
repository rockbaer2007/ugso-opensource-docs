---
title: Utiliser UIX
description: Découvrez comment utiliser UI eXtension pour styliser les éléments de votre interface Home Assistant.
---
# Utiliser UIX Styling pour Home Assistant

- :bar_chart: [Styliser les cartes](./cards.md)
- :bulb: [Styliser les entités, badges, éléments et marqueurs d'entité](entities.md)
- :red_circle: [Styliser les icônes](./icons.md)
- :adult: [Styliser les images d'entité](./images.md)
- :white_square_button: [Arrière-plans de sections](./section-backgrounds.md)
- :film_frames: [Arrière-plans de vues : caméra, vidéo et image](./view-backgrounds.md)
- :abacus: [Styliser les panneaux personnalisés](./custom-panels.md)
- [Raccourcis personnalisés dans la barre latérale (à partir de 9.0.0-beta.6)](./custom-sidebar-panels)
- :material-application-cog: [Styliser les panneaux d'applications et d'Ingress](./apps.md)
- :clipboard: [Modèles](./templates.md)
- :art: [Thèmes](./themes.md)
- :hammer_and_pick: [Autres options](other.md)

## Exemples complémentaires de la référence allemande {#german-reference-examples}

:::: details Afficher les configurations complémentaires
Ces configurations complètent la référence traduite ci-dessus. Elles reprennent les exemples techniques de la [page allemande](/projects/uix/using/index). Les clés, expressions, valeurs et textes de démonstration sont conservés tels quels ; remplacez les entités par les vôtres. Les limites de version indiquées dans la référence restent applicables.

### 1. Principe de base {#reference-example-1}

```yaml
uix:
  style: |
    ha-card {
      border-radius: 12px;
    }
```

::::
