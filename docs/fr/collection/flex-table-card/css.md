---
title: CSS pour flex-table-card
description: Personnalisez la mise en page et les couleurs du composant flex-table-card à l'aide de CSS.
---
<a id="flex-table-card-css"></a>
<a id="orientation-actuelle"></a>

# CSS {#css}

Le composant flex-table-card peut être stylisé directement via la section `css`. Le sélecteur CSS sert de clé, et le contenu CSS de valeur.

```yaml
type: custom:flex-table-card
title: Tabelle
entities:
  include: sensor.*
columns:
  - name: Name
    data: name
  - name: Wert
    data: state
css:
  table: "border-collapse: collapse; width: 100%;"
  thead th: "font-weight: 700; font-size: 13px;"
  tbody tr td: "font-size: 12px; padding: 6px 8px;"
  "tbody tr:nth-child(odd)": "background-color: rgba(255,255,255,0.04);"
  "tbody tr:nth-child(even)": "background-color: rgba(255,255,255,0.08);"
```

## Remplacement ou extension {#ersetzen-oder-erweitern}

Sans `+`, le style existant pour le sélecteur est remplacé.

```yaml
css:
  table: "border: 0;"
```

Avec `+`, le style est étendu.

```yaml
css:
  table+: "border: 0;"
```

## Ciblage de colonnes spécifiques {#spalten-gezielt-ansprechen}

```yaml
css:
  "thead th:nth-child(1)": "width: 120px;"
  "tbody tr td:nth-child(1)": "font-weight: 600;"
  "tbody tr td:nth-child(3)": "text-align: right;"
```

## Taille de police dans les lignes du tableau {#schriftgroße-in-tabellenzeilen}

```yaml
css:
  "tbody tr td": "font-size: 12px; line-height: 1.25;"
```

## Autoriser la sélection de texte {#auswahl-von-text-erlauben}

```yaml
css:
  "tbody tr+": "user-select: text;"
```
