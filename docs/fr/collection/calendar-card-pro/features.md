---
title: Fonctionnalités de Calendar Card Pro
description: Aperçu en français des principales fonctionnalités de Calendar Card Pro.
---
<a id="calendar-card-pro-fonctions"></a>
<a id="orientation-actuelle"></a>

# Fonctionnalités {#features}

## Éditeur visuel {#visueller-editor}

La carte dispose d'un éditeur visuel. Selon la documentation originale, celui-ci a été entièrement repensé dans la version `4.0.0` et structuré en plusieurs sections. Il propose des paramètres de recherche, des filtres pour des valeurs personnalisées, des réglages liés au calendrier ainsi que des exceptions pour l'affichage en colonnes. Depuis `4.1.0`, l'éditeur permet de dupliquer les blocs de calendrier, ce qui autorise l'utilisation d'un même calendrier à plusieurs reprises avec des filtres, des couleurs ou des types d'événements différents.

## Calendriers multiples {#mehrere-kalender}

Il est possible d'afficher plusieurs calendriers au sein d'une même carte. Chaque calendrier peut disposer de ses propres couleurs et options d'affichage.

Depuis `4.1.0`, un calendrier peut également être segmenté selon le type d'événement. Avec `event_type: timed`, seuls les événements dotés d'une heure précise sont affichés, tandis qu'avec `event_type: all_day`, seuls les événements sur toute la journée apparaissent. Cela permet d'intégrer deux fois le même calendrier tout en lui attribuant des coloris différents.

```yaml
entities:
  - entity: calendar.family
    label: Familie ganztägig
    event_type: all_day
    accent_color: "#ff9800"
  - entity: calendar.family
    label: Familie Termine
    event_type: timed
    accent_color: "#03a9f4"
```

## Affichage compact {#kompakte-ansicht}

Les paramètres `compact_events_to_show` et `compact_days_to_show` permettent de limiter le nombre d'événements ou de jours visibles directement. Avec `tap_action: expand`, il est possible de basculer entre un affichage compact et un affichage étendu.

## Affichage en colonnes {#spaltenansicht}

Avec `view: column`, les jours sont présentés côte à côte sous forme de colonnes. Cette disposition est particulièrement adaptée aux vues hebdomadaires sur des tableaux de bord larges.

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
view: column
days_to_show: 7
column:
  min_day_width: 150
  min_days_to_show: 3
  min_days_fallback: list
```

Si l'espace disponible est insuffisant, la carte peut réduire le nombre de colonnes ou basculer vers un affichage sous forme de liste.

## Date de début dynamique {#dynamisches-startdatum}

Le paramètre `start_date` peut correspondre à une date fixe ou à une expression relative.

Exemples :

| Valeur | Signification |
| --- | --- |
| `today` | Commencer aujourd'hui |
| `today+7` | Commencer dans sept jours |
| `start_of_week` | Commencer en début de semaine |
| `monday+1w` | Lundi de la semaine suivante |
| `saturday` | Commencer le samedi |

## Événements sur plusieurs jours {#mehrtagige-termine}

`split_multiday_events` permet d'afficher les événements s'étendant sur plusieurs jours pour chaque jour concerné. Dans la vue par colonnes, cela s'avère particulièrement utile, car chaque colonne représente une journée.

Il existe une option de contrôle supplémentaire pour les événements sur toute la journée : si `show_past_events` est désactivé, `allday_expires_at` permet aux événements sur toute la journée de disparaître à une heure précise lors de leur dernier jour. Cette fonctionnalité est pratique, par exemple, pour les calendriers de collecte des déchets ou les rappels.

```yaml
entities:
  - entity: calendar.waste
    label: Abfall
    allday_expires_at: "10:00"
```

## Jours de la semaine et week-ends {#wochentage-und-wochenenden}

`days_of_week` permet de restreindre l'affichage d'un calendrier aux jours ouvrés ou aux week-ends. Dans le cas d'événements sur plusieurs jours qui sont scindés, chaque jour affiché est évalué individuellement.

```yaml
entities:
  - entity: calendar.school
    days_of_week: weekdays
  - entity: calendar.family
    days_of_week: weekends
```

## Badges pour les événements sur toute la journée {#ganztags-badges}

`allday_badge` permet d'afficher les événements sur toute la journée sous forme de badge. `title` place le badge autour du titre, tandis que `time` remplace la ligne dédiée aux événements sur toute la journée, située à côté de l'icône en forme d'horloge. `allday_badge_style` contrôle la forme, `allday_badge_color` la couleur.

```yaml
allday_badge: title
allday_badge_style: subtle
allday_badge_color: accent
```

## Filtres et remplacement de texte {#filter-und-textersetzung}

Par défaut, `blocklist` et `allowlist` s'appliquent au titre. Grâce à `filter_field`, ils peuvent être appliqués à `location` ou `description` à la place.

`replace_field`, `replace_pattern` et `replace_with` modifient le texte affiché lors du rendu de la carte, sans altérer l'événement original dans le calendrier.

```yaml
entities:
  - entity: calendar.work
    filter_field: location
    allowlist: teams.microsoft.com
    replace_field: title
    replace_with: Besetzt
```

## Icône de lieu {#orts-icon}

Les événements Microsoft Teams peuvent s'afficher automatiquement avec une icône Teams au lieu d'un marqueur de carte classique. Pour chaque calendrier, `location_icon` permet de définir une icône personnalisée, tandis que `mdi:map-marker-outline` permet de forcer l'utilisation du marqueur standard.

## Intégration météo {#wetterintegration}

`weather` permet d'intégrer une entité météo de Home Assistant. Les données météorologiques peuvent apparaître dans l'en-tête de la journée, à côté des événements, ou aux deux endroits.

```yaml
weather:
  entity: weather.home
  position: both
  date:
    show_high_temp: true
    show_low_temp: true
  event:
    show_temp: true
    show_conditions: true
```

## Actions {#aktionen}

La carte prend en charge `tap_action` et `hold_action`. Ces paramètres permettent, par exemple, d'afficher des détails, d'agrandir la carte, de lancer une navigation ou d'appeler un service.

## Modèles (Templates) {#templates}

Le titre peut contenir des modèles (templates) Home Assistant. Il existe par ailleurs des espaces réservés, tels que le nombre d'événements ou le prochain événement, qui peuvent être utilisés pour créer des titres dynamiques.

## Thèmes {#theming}

Calendar Card Pro prend en charge les thèmes et peut être personnalisé via des options ainsi que des variables CSS. Pour une personnalisation plus poussée, il est possible d'utiliser `card-mod`.

## Performances {#performance}

Selon la version originale, la carte utilise une mise à jour intelligente et la mise en cache. La version `4.0.0` réduit le volume de téléchargement — car l'éditeur est chargé séparément — et évite les requêtes en double vers les calendriers.
