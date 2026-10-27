---
title: Actions de `flex-table-card`
description: Actions sur les cellules, actions au toucher (*tap-actions*) et actions d'édition (*edit-actions*) de `flex-table-card`.
---
<a id="flex-table-card-actions"></a>
<a id="orientation-actuelle"></a>

# Actions {#aktionen}

Les colonnes peuvent déclencher des actions Home Assistant. Les actions Lovelace classiques sont prises en charge, telles que `more-info`, `toggle`, `perform-action`, `navigate`, `url`, `assist` ainsi que `fire-dom-event`.

## Affichage des détails (*more-info*) au toucher {#more-info-beim-tippen}

```yaml
type: custom:flex-table-card
title: Lichter
entities:
  include: light.*
columns:
  - name: Name
    data: name
    tap_action:
      action: more-info
  - name: Status
    data: state
```

## Action utilisant les valeurs des colonnes {#aktion-mit-spaltenwerten}

Au sein d'une ligne, il est possible de faire référence aux valeurs d'autres colonnes.

| Référence | Signification |
| --- | --- |
| `cell[n]` | Colonne visible avec l'index `n` |
| `col[n]` | Colonne avec l'index `n`, même si elle est masquée |

```yaml
type: custom:flex-table-card
title: Navigation
entities:
  include: sensor.room_*
columns:
  - name: Raum
    data: name
  - name: Pfad
    data: dashboard_path
    hidden: true
  - name: Oeffnen
    data: name
    tap_action:
      action: navigate
      navigation_path: col[1]
```

## Remarque concernant les anciennes terminologies {#hinweis-zu-alten-begriffen}

Home Assistant utilise désormais `action` et `perform-action`. Les anciennes terminologies, telles que `call-service`, `service` ou `service_data`, ne doivent plus être utilisées pour les actions sur les colonnes.
