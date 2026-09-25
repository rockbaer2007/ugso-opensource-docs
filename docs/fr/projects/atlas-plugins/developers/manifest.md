---
title: Manifeste et capacités
description: Identifiants, versions, métadonnées et capacités d'un plugin ATLAS.
---
# Manifeste et capacités

Le manifeste décrit l'identité du plugin, ses informations d'affichage et son point d'entrée. Dans le [modèle officiel](../plugin-template), l'exemple se trouve dans `plugins/atlas-plugin/atlas-plugin.json`.

## Exemple

```json
{
  "id": "atlas.plugin.lights",
  "name": "Light Controls",
  "nameI18n": { "de": "Lichtsteuerung", "en": "Light Controls" },
  "version": "1.0.0",
  "description": "Controls selected lights.",
  "status": "active",
  "order": 100,
  "entry": "/plugin-assets/atlas-plugin/index.html",
  "icon": "icon.svg",
  "logo": "logo.svg",
  "preview": "preview.svg",
  "capabilities": ["homeassistant.entities.read"]
}
```

## Champs

- `id` : identifiant de plugin unique. Gardez-le stable après publication ; le modèle utilise des identifiants en minuscules séparés par des points.
- `name` et `nameI18n` : nom par défaut et noms éventuellement traduits.
- `version` : version publiée. Incrémentez-la à chaque modification publiée.
- `description` et `descriptionI18n` : descriptions brèves par défaut et traduites.
- `status` et `order` : indications d'état et de tri pour le catalogue et l'interface.
- `entry` : URL relative du point d'entrée. Dans Atlas, un plugin local contenant `index.html` peut recevoir une URL de lancement automatique si `entry` est omis.
- `icon`, `logo`, `preview` : chemins relatifs des ressources utilisées dans le catalogue et l'Administration.
- `capabilities` : liste des fonctions nécessaires au plugin. Ne déclarez que celles qui sont utilisées.

Le manifeste du paquet est distinct de `repository.json` : le catalogue comprend aussi, pour chaque plugin, l'URL du paquet, le manifeste de secours, la compatibilité et les descriptions du catalogue. Consultez [Format du dépôt](../repository-format).

## Limiter les capacités

Chaque capacité doit être précise et justifiée. N'ajoutez ni valeur provisoire ni autorisation générale d'administrateur. L'installation actuelle n'exécute pas le code téléchargé ; une capacité ne constitue donc pas une limite d'accès ni une sandbox.
