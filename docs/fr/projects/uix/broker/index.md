---
title: UIX Broker
description: Créez des interactions déclaratives d'événements frontend pour Home Assistant avec UIX Broker.
---
# UIX Broker

UIX Broker transforme les événements du navigateur, les raccourcis clavier et les événements de bus d'événements Home Assistant en interactions déclaratives. Une interaction sélectionne un élément du navigateur, vérifie les règles facultatives, puis exécute les directives dans leur ordre configuré. La directive `block` constitue une exception : elle bloque l'événement déclencheur de manière synchrone avant les autres directives.

```text
Realm → Listen → Interaction anchor → Rules (Optional anchors) → Directives (Optional anchors)
```

Utilisez UIX Broker lorsqu'un comportement d'interface peut être configuré. Broker peut réagir aux clics, modifier un événement avant de le redistribuer, donner le focus à un élément, mettre à jour une propriété et appeler une méthode d'élément sûre. Il peut ajouter des boutons, badges, textes, icônes de tuile, info-bulles et demandes de déverrouillage ; associer ou exécuter des actions Home Assistant ; rendre des modèles ; évaluer du JavaScript et marquer des pauses.

```yaml
uix_broker:
  - realm: browser
    listen: click
    anchor: target
    rules:
      - ".action-button"
    directives:
      - type: block
      - type: event
        name: another-action
        data:
          source: action-button
```

## Guides du courtier UIX

- [Broker](./broker.md) — structure d'interaction, sources de configuration, cycle de vie et débogage.
- [Domaines](./realms.md) — événements de navigateur, raccourcis clavier et événements de bus d'événements Home Assistant.
- [Ancres d'interaction](./interaction-anchors.md) — sélection du chemin d'événement composé et de l'élément `select_tree`.
- [Règles](./rules) — éléments hôtes, données capturées, identité du navigateur, utilisateurs, statut administrateur, fragments d'URL, paramètres de recherche et panneaux.
- [Directives](./directives) — `block`, `property`, `event`, `call`, `button`, `badge`, `text-content`, `tile-icon`, `tooltip`, `lock`, `action-handler`, `action`, `template`, `javascript`, `wait`.
- [Exemples](./examples.md) — exemples. Voir également [UIX Guides](https://uix-guides.lf.technology), où des exemples plus détaillés peuvent être publiés.

::: note
Pour la correspondance de l'identité du navigateur, [Browser Mod](https://github.com/thomasloven/hass-browser_mod) est requis.

:::
