---
title: En-têtes et pieds de page de la `flex-table-card`
description: En-têtes de colonnes, icônes et lignes de résumé dans la `flex-table-card`.
---
<a id="flex-table-card-en-tete-et-pied-de-page"></a>
<a id="orientation-actuelle"></a>

# En-têtes et pieds de page {#header-und-footer}

## En-têtes de colonnes {#spaltenuberschriften}

La carte détermine l'en-tête d'une colonne selon l'ordre suivant :

1. `name`
2. `id`
3. `data`

```yaml
columns:
  - name: Geraet
    data: name
  - id: battery
    data: state
  - data: area
```

Il est possible d'avoir un en-tête vide :

```yaml
columns:
  - name: ""
    data: icon
```

## Icônes dans l'en-tête {#icons-im-header}

```yaml
columns:
  - name: Batterie
    icon: mdi:battery
    data: state
    align: right
```

L'alignement des cellules influe également sur l'alignement de l'en-tête.

## Activer le pied de page {#footer-aktivieren}

```yaml
display_footer: true
```

Il est ensuite possible de définir, pour chaque colonne, ce qui doit être calculé ou affiché dans le pied de page.

| Valeur | Signification |
| --- | --- |
| `sum` | Somme |
| `average` | Moyenne |
| `count` | Nombre |
| `max` | Valeur maximale |
| `min` | Valeur minimale |
| `text` | Texte fixe |

## Exemple avec une ligne de totaux {#beispiel-mit-summenzeile}

```yaml
type: custom:flex-table-card
title: Werte nach Land
entities: []
display_footer: true
columns:
  - name: Land
    data: rows.country
    footer_type: text
    footer_text: "Gesamt:"
  - name: Wert
    data: rows.value
    fmt: number
    align: right
    footer_type: sum
    footer_modify: x.toFixed(0)
static_data:
  rows:
    - country: Deutschland
      value: 120
    - country: Frankreich
      value: 90
```

## Personnaliser le pied de page via CSS {#footer-per-css-gestalten}

```yaml
css:
  tfoot th: "text-align: right; font-weight: 700;"
  tfoot *: "border-style: solid none none none;"
```

Exemple visuel original : [FlexTableFooterExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/FlexTableFooterExample.png)
