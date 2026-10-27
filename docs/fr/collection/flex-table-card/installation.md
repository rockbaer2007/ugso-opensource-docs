---
title: Installation de flex-table-card
description: Installation de flex-table-card via HACS ou manuellement.
---
<a id="flex-table-card-installation"></a>
<a id="orientation-actuelle"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

L'installation recommandée s'effectue via HACS.

1. Ouvrez Home Assistant.
2. Ouvrez HACS.
3. Recherchez `flex-table`.
4. Installez la carte.
5. Rechargez Home Assistant si HACS vous y invite.

Le type de carte sera alors disponible dans Lovelace en tant que carte personnalisée (Custom Card) :

```yaml
type: custom:flex-table-card
```

## Installation manuelle {#manuelle-installation}

L'installation manuelle est plutôt destinée aux développeurs ou aux cas particuliers.

1. Téléchargez le fichier `flex-table-card.js` depuis le dépôt d'origine.
2. Placez le fichier dans le dossier `www` de Home Assistant.
3. Ajoutez la ressource dans Lovelace.

```yaml
resources:
  - type: module
    url: /local/flex-table-card.js
```

Avec HACS, la ressource est généralement gérée automatiquement ou via la notification HACS.

## Test rapide {#schnelltest}

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
