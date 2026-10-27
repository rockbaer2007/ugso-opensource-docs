---
title: Configuration de Calendar Card Pro
description: Référence de configuration pour Calendar Card Pro.
---
<a id="calendar-card-pro-configuration"></a>
<a id="orientation-actuelle"></a>

# Référence de configuration {#konfigurationsreferenz}

Cette page reprend les groupes d'options de la documentation de référence originale. Pour des exemples détaillés, la documentation originale en anglais fait foi.

## Nouveautés dans la version 1.0 {#neu-in-v4-1-0}

La version `4.1.0` ajoute plusieurs contrôles liés au calendrier :

- `event_type` permet de distinguer les événements avec heure précise des événements sur toute la journée. - `filter_field` permet à `blocklist` et `allowlist` d'agir sur le titre, le lieu ou la description.
- `replace_field`, `replace_pattern` et `replace_with` modifient le texte affiché, sans pour autant altérer l'événement du calendrier lui-même.
- `allday_expires_at` permet de faire se terminer plus tôt dans la journée les événements d'une journée entière.
- `days_of_week` limite un calendrier aux jours ouvrables ou au week-end.
- `allday_badge`, `allday_badge_style` et `allday_badge_color` gèrent le nouvel affichage sous forme de badge pour les événements d'une journée entière.

## Paramètres de base {#grundeinstellungen}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `entities` | array | Obligatoire | Liste des entités de calendrier, avec possibilité de définir des paramètres spécifiques pour chaque calendrier. |
| `view` | string | `list` | Mise en page : `list` pour afficher les jours les uns en dessous des autres, `column` pour les afficher côte à côte. |
| `start_date` | string | aujourd'hui | Date de début, sous forme de `YYYY-MM-DD` ou d'expression relative telle que `today+7`, `start_of_week`, `monday+1w`. |
| `days_to_show` | number | `3` | Nombre de jours affichés. |
| `event_type` | string | `all` | Type d'événement : `all`, `timed` ou `all_day`. Peut être défini globalement ou par calendrier. |
| `compact_days_to_show` | number | - | Nombre de jours en mode compact. |
| `compact_events_to_show` | number | - | Nombre d'événements en mode compact. |
| `compact_events_complete_days` | boolean | `false` | Affiche tous les événements pour les jours où au moins un événement est visible. |
| `show_empty_days` | boolean | `false` | Affiche les jours sans événement. Dans la vue en colonnes, la valeur par défaut est `true`. |
| `hide_when_empty` | boolean | `false` | Masquer la carte s'il n'y a aucun événement à venir. |
| `empty_day_text` | string | valeur par défaut traduite | Texte personnalisé pour les jours sans événement ou les cartes entièrement vides. |
| `filter_duplicates` | boolean | `false` | Masquer les événements en double si le titre, le début, la fin et le lieu sont identiques. |
| `split_multiday_events` | boolean | `false` | Afficher les événements sur plusieurs jours pour chaque jour concerné. Dans la vue en colonnes, la valeur par défaut est `true`. |
| `language` | string | Système, repli sur `en` | Langue des textes de la carte, détectée automatiquement depuis Home Assistant. |
| `column` | object | hérite des valeurs de niveau supérieur | Options d'affichage spécifiques pour `view: column`. |

## Uniquement pour la vue en colonnes {#nur-fur-die-spaltenansicht}

| Option | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `column.day_header_gap` | string | `8px` | Espacement entre l'en-tête du jour et le premier événement. |
| `column.day_header_separator_width` | string | `0px` | Épaisseur de la ligne sous l'en-tête du jour. |
| `column.day_header_separator_color` | string | `var(--divider-color)` | Couleur de la ligne sous l'en-tête du jour. |
| `column.min_day_width` | number | `140` | Largeur minimale des colonnes en pixels. |
| `column.min_days_to_show` | number | `days_to_show` | Nombre minimal de colonnes visibles. |
| `column.min_days_fallback` | string | `list` | Comportement en cas d'espace insuffisant : `list` ou `cramp`. |

## Options sans effet dans la vue en colonnes {#optionen-ohne-wirkung-in-der-spaltenansicht}

Ces options restent pertinentes pour la vue en liste, mais n'ont pas d'effet direct dans la vue en colonnes :

`date_vertical_alignment`, `today_indicator_position`, `compact_events_to_show`, `compact_days_to_show`, `compact_events_complete_days`, ainsi que `split_multiday_events` (lié au calendrier).

## Options liées au calendrier {#kalenderbezogene-optionen}

Une entrée dans `entities` peut être soit un identifiant d'entité (Entity ID), soit un objet doté de ses propres paramètres.

| Option | Description |
| --- | --- |
| `entity` | Entité de calendrier, par exemple `calendar.family`. |
| `label` | Libellé personnalisé du calendrier. |
| `label_type` | Détermine la manière dont le libellé est lu. |
| `color` | Couleur du calendrier. |
| `accent_color` | Couleur d'accentuation pour la ligne et les arrière-plans facultatifs. |
| `label_icon_color` | Couleur du libellé/de l'icône. |
| `show_time` | Afficher l'heure pour ce calendrier. |
| `show_location` | Afficher le lieu pour ce calendrier. |
| `location_icon` | Icône pour les informations de lieu de ce calendrier, par exemple `mdi:office-building` ; peut remplacer la détection automatique de Teams. |
| `show_description` | Afficher la description pour ce calendrier. |
| `compact_events_to_show` | Limite compacte pour ce calendrier. |
| `blocklist` | Exclure des termes ou des modèles. |
| `allowlist` | Afficher uniquement les termes ou modèles correspondants. |
| `filter_field` | Champ pour `blocklist`/`allowlist` : `title`, `location` ou `description`. |
| `replace_field` | Champ pour le remplacement de texte : `title`, `location` ou `description`. |
| `replace_pattern` | Modèle d'expression régulière (regex) à remplacer ou à supprimer dans le champ sélectionné. |
| `replace_with` | Texte de remplacement ; en l'absence de `replace_pattern`, le champ entier est remplacé. |
| `split_multiday_events` | Scinder les événements s'étendant sur plusieurs jours pour ce calendrier. |
| `event_type` | Type d'événement lié au calendrier : `all`, `timed` ou `all_day`. |
| `allday_expires_at` | Heure (au format `HH:MM`) à partir de laquelle les événements sur toute la journée de ce calendrier sont considérés comme passés. |
| `days_of_week` | Limitation à `weekdays` ou `weekends`. |

## En-tête {#header}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `title` | chaîne | - | Titre de la carte ; peut contenir des modèles (templates) Home Assistant. |
| `title_font_size` | chaîne | `--calendar-card-font-size-title` | Taille de la police du titre. |
| `title_color` | chaîne | `--calendar-card-color-title` | Couleur du titre. |

## Mise en page et espacements {#layout-und-abstande}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `background_color` | chaîne | `--ha-card-background` | Couleur d'arrière-plan de la carte. |
| `accent_color` | chaîne | `#03a9f4` | Couleur d'accentuation de la ligne verticale et des badges optionnels (rendez-vous / journée entière). |
| `vertical_line_width` | string | `2px` | Épaisseur de la ligne verticale. |
| `day_spacing` | string | `10px` | Espacement entre les jours ou les colonnes. |
| `event_spacing` | string | `4px` | Espacement interne au sein d'un rendez-vous. |
| `additional_card_spacing` | string | `0px` | Espacement supplémentaire en haut et en bas de la carte. |
| `height` | string | `auto` | Hauteur fixe et précise de la carte. |
| `max_height` | string | `none` | Hauteur maximale de la carte en cas d'augmentation du contenu. |

## Numéros de semaine et lignes de séparation {#wochennummern-und-trennlinien}

| Option | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `show_week_numbers` | chaîne | `null` | Affichage des numéros de semaine : `iso`, `simple` ou désactivé. |
| `show_current_week_number` | booléen | `true` | Affichage du numéro de semaine pour la semaine en cours ou la première semaine. |
| `week_number_font_size` | chaîne | `12px` | Taille de police du numéro de semaine. |
| `week_number_color` | chaîne | `var(--primary-text-color)` | Couleur du texte du numéro de semaine. |
| `week_number_background_color` | chaîne | `#03a9f450` | Couleur d'arrière-plan du numéro de semaine. |
| `first_day_of_week` | chaîne | `system` | Début de la semaine : `monday`, `sunday` ou `system`. |
| `day_separator_width` | chaîne | `0px` | Ligne de séparation entre les jours. |
| `day_separator_color` | chaîne | `var(--secondary-text-color)` | Couleur de la ligne de séparation entre les jours. |
| `week_separator_width` | chaîne | `0px` | Ligne de séparation entre les semaines. |
| `week_separator_color` | chaîne | `#03a9f450` | Couleur de la ligne de séparation entre les semaines. |
| `month_separator_width` | chaîne | `0px` | Ligne de séparation entre les mois. |
| `month_separator_color` | chaîne | `var(--primary-text-color)` | Couleur de la ligne de séparation des mois. |

## Indicateur « Aujourd'hui » {#heute-markierung}

| Option | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `today_indicator` | booléen/chaîne | `false` | Indicateur « Aujourd'hui » : `true`, `dot`, `pulse`, `glow`, icône MDI, émoji ou chemin d'accès à une image. |
| `today_indicator_position` | chaîne | `15% 50%` | Position au format CSS. |
| `today_indicator_color` | chaîne | `#03a9f4` | Couleur de l'indicateur. |
| `today_indicator_size` | chaîne | `6px` | Taille de l'indicateur. |

## Colonne des dates {#datumsspalte}

| Option | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `date_vertical_alignment` | chaîne | `middle` | Alignement vertical : `top`, `middle`, `bottom`. |
| `weekday_font_size` | chaîne | `14px` | Taille de police du jour de la semaine. |
| `weekday_color` | chaîne | `--primary-text-color` | Couleur du jour de la semaine. |
| `day_font_size` | chaîne | `26px` | Taille de police du numéro du jour. |
| `day_color` | chaîne | `--primary-text-color` | Couleur du numéro du jour. |
| `show_month` | booléen | `true` | Affichage des noms des mois. |
| `month_font_size` | chaîne | `12px` | Taille de police du mois. |
| `month_color` | chaîne | `--primary-text-color` | Couleur du mois. |
| `weekend_weekday_color` | chaîne | hérite de `weekday_color` | Couleur du jour de la semaine pendant les week-ends. |
| `weekend_day_color` | chaîne | hérite de `day_color` | Couleur du numéro du jour pendant les week-ends. |
| `weekend_month_color` | chaîne | hérite de `month_color` | Couleur du mois pendant les week-ends. |
| `today_weekday_color` | chaîne | hérite de week-end/par défaut | Couleur du jour de la semaine pour aujourd'hui. |
| `today_day_color` | chaîne | hérite de week-end/par défaut | Couleur du numéro du jour pour aujourd'hui. |
| `today_month_color` | chaîne | hérite de week-end/par défaut | Couleur du mois pour aujourd'hui. |

## Colonne des rendez-vous {#terminspalte}

| Option | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `event_background_opacity` | nombre | `0` | Opacité de l'arrière-plan pour les rendez-vous avec une couleur d'accentuation, de 0 à 100. |
| `event_icon_vertical_alignment` | string | `top` | Alignement vertical de l'icône : `top`, `middle`, `bottom`. |
| `show_past_events` | boolean | `false` | Afficher les rendez-vous déjà terminés. |
| `show_countdown` | boolean | `false` | Afficher le compte à rebours jusqu'au rendez-vous. |
| `show_countdown_allday` | boolean | `true` | Afficher le compte à rebours également pour les rendez-vous sur toute la journée. |
| `show_multiday_allday_time` | boolean | `true` | Afficher une ligne temporelle pour les rendez-vous sur toute la journée s'étendant sur plusieurs jours ; elle indique la date de fin. |
| `allday_badge` | string | `off` | Position du badge « toute la journée » : `off`, `title` ou `time`. |
| `allday_badge_style` | string | `subtle` | Style du badge : `subtle`, `outline`, `tinted` ou `filled`. |
| `allday_badge_color` | string | `accent` | Couleur du badge : `accent`, `text` ou une couleur CSS. |
| `show_progress_bar` | booléen | `false` | Afficher la barre de progression pour les rendez-vous en cours. |
| `progress_bar_color` | chaîne | `var(--secondary-text-color)` | Couleur de la barre de progression. |
| `progress_bar_height` | chaîne | calculée | Hauteur de la barre de progression. |
| `progress_bar_width` | chaîne | selon la mise en page | Largeur de la barre de progression. |
| `empty_day_color` | chaîne | `--primary-text-color` | Couleur du texte pour les jours vides. |
| `event_font_size` | chaîne | `14px` | Taille de la police du titre du rendez-vous. |
| `title_max_lines` | nombre | `0` | Nombre maximal de lignes pour le titre du rendez-vous ; `0` = illimité. |
| `event_color` | chaîne | `--primary-text-color` | Couleur du titre du rendez-vous. |
| `show_time` | booléen | `true` | Afficher l'heure du rendez-vous. |
| `show_single_allday_time` | boolean | `true` | Afficher l'heure pour les événements individuels sur toute la journée. |
| `time_24h` | boolean | Système | Utiliser le format 24 heures. |
| `time_two_digit_hours` | boolean | `false` | Afficher les heures sur deux chiffres. |
| `show_end_time` | boolean | `true` | Afficher l'heure de fin. |
| `time_icon_size` | string | `14px` | Taille de l'icône d'horloge. |
| `time_font_size` | string | `12px` | Taille de la police de l'heure. |
| `time_color` | string | `--secondary-text-color` | Couleur de l'heure. |
| `time_max_lines` | number | `0` | Nombre maximal de lignes pour le texte de l'heure. |
| `show_location` | boolean | `true` | Afficher le lieu. |
| `show_location_allday` | boolean | `true` | Afficher le lieu même pour les événements sur toute la journée, si `show_location` est activé. |
| `remove_location_country` | boolean/string | `false` | Supprimer les noms de pays des lieux, éventuellement via une expression régulière (regex). |
| `location_icon_size` | string | `14px` | Taille de l'icône du lieu. |
| `location_font_size` | string | `12px` | Taille de la police du lieu. |
| `location_color` | string | `--secondary-text-color` | Couleur du lieu. |
| `location_max_lines` | number | `0` | Nombre maximal de lignes pour le lieu. |
| `show_description` | boolean | `false` | Afficher la description. |
| `show_description_allday` | boolean | `true` | Afficher les descriptions même pour les événements sur toute la journée, si `show_description` est activé. |
| `description_icon_size` | string | `14px` | Taille de l'icône de description. |
| `description_font_size` | string | `12px` | Taille de la police de la description. |
| `description_color` | string | `--secondary-text-color` | Couleur de la description. |
| `description_max_lines` | number | `0` | Nombre maximal de lignes pour la description. |

## Météo {#wetter}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `weather` | object | - | Configuration météo. |
| `weather.entity` | string | - | Entité météo pour les prévisions. |
| `weather.position` | string | `date` | Position : `none`, `date`, `event`, `both`. |
| `weather.date` | object | - | Affichage de la météo dans l'en-tête journalier. |
| `weather.event` | object | - | Affichage de la météo à côté des rendez-vous. |

`weather.date` accepte : `show_conditions`, `show_high_temp`, `show_low_temp`, `show_uv_index`, `uv_index_threshold`, `icon_size`, `font_size`, `color`.

`weather.event` accepte : `show_conditions`, `show_temp`, `show_uv_index`, `uv_index_threshold`, `daily_forecast_fallback`, `max_lines`, `icon_size`, `font_size`, `color`.

## Actions {#aktionen}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `tap_action` | object | `none` | Action lors d'un appui sur la carte. |
| `hold_action` | object | `none` | Action lors d'un appui prolongé sur la carte. |

Les paramètres d'action peuvent être, selon l'action :

`action`, `navigation_path`, `service`, `service_data`, `url_path`, `open_tab`.

## Cache et mise à jour {#cache-und-aktualisierung}

| Option | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `refresh_interval` | number | `30` | Minutes entre les mises à jour des données. |
| `refresh_on_navigate` | boolean | `true` | Recharger lors du passage d'une vue du tableau de bord à une autre. |
