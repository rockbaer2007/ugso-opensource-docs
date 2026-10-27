---
title: Utilisation de Calendar Card Pro
description: Utiliser Calendar Card Pro dans le tableau de bord (dashboard) de Home Assistant.
---
<a id="calendar-card-pro-utilisation"></a>
<a id="orientation-actuelle"></a>

# Utilisation {#nutzung}

## Ajouter la carte via l'éditeur {#karte-per-editor-hinzufugen}

1. Ouvrir le tableau de bord.
2. Modifier le tableau de bord.
3. Ajouter une nouvelle carte.
4. Rechercher `Calendar`.
5. Sélectionner Calendar Card Pro.
6. Ouvrir le menu (trois points) de la carte.
7. Choisir **Configure** pour ouvrir l'éditeur visuel.

À partir de la version `2026.6` de Home Assistant, la carte peut également être suggérée dans l'onglet **By entity** (Par entité) si une entité de type `calendar.*` est sélectionnée.

## Démarrage rapide via YAML {#schnellstart-per-yaml}

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
days_to_show: 3
show_location: false
show_month: false
```

`calendar.family` doit être remplacé par votre propre entité de calendrier.

## Calendriers multiples {#mehrere-kalender}

```yaml
type: custom:calendar-card-pro
title: Termine
entities:
  - entity: calendar.family
    color: '#ff6c92'
  - entity: calendar.work
    color: '#86ebda'
  - entity: calendar.personal
    color: '#c2ffb3'
days_to_show: 7
compact_events_to_show: 3
tap_action:
  action: expand
```

## Cas d'utilisation typiques {#typische-einsatzfalle}

- Calendrier familial sur le tableau de bord
- Calendriers professionnel et personnel dans une seule vue
- Vue hebdomadaire en colonnes
- Événements avec prévisions météorologiques
- Carte de calendrier compacte pour tablettes murales
- Titres dynamiques affichant le prochain événement ou le nombre d'événements
