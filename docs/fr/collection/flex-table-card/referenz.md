---
title: Référence pour `flex-table-card`
description: Référence de configuration concise en français pour flex-table-card.
---
<a id="flex-table-card-reference"></a>
<a id="orientation-actuelle"></a>

# Référence {#referenz}

## Niveau supérieur {#top-level}

| Option | Obligatoire | Description |
| --- | --- | --- |
| `type` | oui | Toujours `custom:flex-table-card` |
| `title` | non | Titre de la carte |
| `entities` | oui | Entités ou filtres pour la source de données |
| `columns` | oui | Définitions des colonnes |
| `strict` | non | Masquer les lignes sans résultat |
| `sort_by` | non | Trier par colonne, par exemple `state+` |
| `disable_header_sort` | non | Désactiver le tri manuel via l'en-tête |
| `max_rows` | non | Nombre maximal de lignes visibles |
| `clickable` | non | Ouvrir la boîte de dialogue de l'entité au clic |
| `selectable` | non | Autoriser la sélection de texte |
| `enable_search` | non | Afficher le champ de recherche au-dessus du tableau |
| `auto_format` | non | Utiliser le formatage de Home Assistant pour les valeurs |
| `display_footer` | non | Afficher la ligne de résumé |
| `css` | non | Règles CSS pour ce tableau |
| `action` | non | Action/script comme source de données |
| `action_data` | non | Données pour l'action |
| `static_data` | non | Données statiques au sein de la carte |

## Entités {#entities}

| Option | Obligatoire | Description |
| --- | --- | --- |
| `include` | oui | Regex ou liste d'expressions régulières pour les entités |
| `exclude` | non | Regex ou liste d'exclusion |

Pour `static_data`, la valeur `entities: []` est définie.

## Colonnes {#columns}

| Option | Obligatoire | Description |
| --- | --- | --- |
| `name` | non | En-tête de colonne |
| `id` | non | ID de colonne stable, important pour `sort_by` |
| `data` | oui | Sélecteur de données |
| `hidden` | non | Masquer la colonne |
| `icon` | non | Icône dans l'en-tête |
| `modify` | non | Expression JavaScript pour la valeur de la cellule |
| `align` | non | `left`, `center` ou `right` |
| `prefix` | non | Texte avant la valeur de la cellule |
| `suffix` | non | Texte après la valeur de la cellule |
| `no_auto_format` | non | Désactiver le formatage automatique pour la colonne |
| `multi_delimiter` | non | Séparateur pour plusieurs valeurs de données |
| `fmt` | non | Formatteur intégré |
| `sort_unmodified` | non | Trier selon la valeur d'origine |
| `footer_type` | non | `sum`, `average`, `count`, `max`, `min` ou `text` |
| `footer_text` | non | Texte dans la ligne de pied de page |
| `footer_colspan` | non | Texte de pied de page sur plusieurs colonnes |
| `footer_modify` | non | JavaScript pour la valeur du pied de page |
| `tap_action` | non | Action lors d'un appui simple |
| `hold_action` | non | Action lors d'un appui prolongé |
| `double_tap_action` | non | Action lors d'un double appui |
| `edit_action` | non | Modification et enregistrement depuis la cellule |

## Référence originale {#originalreferenz}

La référence technique complète se trouve dans le dépôt d'origine :

- [Configuration Reference](https://github.com/custom-cards/flex-table-card/blob/master/docs/config-ref.md)
