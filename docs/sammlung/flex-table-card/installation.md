---
title: flex-table-card Installation
description: Installation der flex-table-card ueber HACS oder manuell.
---
# Installation

## Installation ueber HACS

Die empfohlene Installation laeuft ueber HACS.

1. Home Assistant oeffnen.
2. HACS oeffnen.
3. Nach `flex-table` suchen.
4. Die Karte installieren.
5. Home Assistant neu laden, falls HACS dazu auffordert.

Danach steht der Kartentyp in Lovelace als Custom Card zur Verfuegung:

```yaml
type: custom:flex-table-card
```

## Manuelle Installation

Die manuelle Installation ist eher fuer Entwickler oder Sonderfaelle gedacht.

1. Datei `flex-table-card.js` aus dem Original-Repository laden.
2. Datei in den Home-Assistant-Ordner `www` legen.
3. Resource in Lovelace eintragen.

```yaml
resources:
  - type: module
    url: /local/flex-table-card.js
```

Bei HACS wird die Resource normalerweise automatisch oder ueber den HACS-Hinweis gepflegt.

## Schnelltest

```yaml
type: custom:flex-table-card
title: Sensoren
entities:
  include: sensor.*
max_rows: 10
columns:
  - name: Name
    data: name
  - name: Status
    data: state
```

