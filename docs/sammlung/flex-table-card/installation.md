---
title: flex-table-card Installation
description: Installation der flex-table-card über HACS oder manuell.
---
# Installation

## Installation über HACS

Die empfohlene Installation läuft über HACS.

1. Home Assistant öffnen.
2. HACS öffnen.
3. Nach `flex-table` suchen.
4. Die Karte installieren.
5. Home Assistant neu laden, falls HACS dazu auffordert.

Danach steht der Kartentyp in Lovelace als Custom Card zur Verfügung:

```yaml
type: custom:flex-table-card
```

## Manuelle Installation

Die manuelle Installation ist eher für Entwickler oder Sonderfälle gedacht.

1. Datei `flex-table-card.js` aus dem Original-Repository laden.
2. Datei in den Home-Assistant-Ordner `www` legen.
3. Resource in Lovelace eintragen.

```yaml
resources:
  - type: module
    url: /local/flex-table-card.js
```

Bei HACS wird die Resource normalerweise automatisch oder über den HACS-Hinweis gepflegt.

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

