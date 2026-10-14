# Format des dépôts

ATLAS utilise son propre format pour les plugins installables. Un dépôt de
plugins n’est pas un dépôt d’extensions Home Assistant : ses métadonnées ATLAS
permettent à l’Administration de rejeter les autres formats de dépôt.

## Références

- Dépôt de démonstration : `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Catalogue : `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Page de transition : `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`
- Modèle officiel : [atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template), avec **Use this template** sur GitHub.

Le modèle contient un plugin fonctionnel, son manifeste, son catalogue, ses
illustrations, le constructeur de package et la validation. Après modification
du manifeste, `npm run build` génère le package et synchronise le catalogue ;
`npm run check` vérifie leur cohérence. GitHub Actions exécute les deux contrôles.

L’installateur générique enregistre les fichiers du package localement.
Il n’exécute pas arbitrairement le code téléchargé depuis un dépôt.

## Structure

```text
repository.json
plugins/
  example-plugin/
    plugin.atlas-plugin.json
    icon.png
    preview.png
    README.md
```

## Champs

| Champ | Rôle |
| --- | --- |
| `kind` | Doit être `atlas.plugin.repository`. |
| `atlas.type` | Doit être `plugin-repository`. |
| `atlas.schemaVersion` | Version du schéma du catalogue ATLAS. |
| `name` | Nom affiché du dépôt. |
| `version` | Version du catalogue. |
| `homepage` | Page du projet ou GitHub, facultative. |
| `installPage` | Page de transition ATLAS pour copier l’URL, facultative. |
| `plugins[]` | Liste des plugins installables. |
| `plugins[].id` | Identifiant unique du plugin. |
| `plugins[].atlas.type` | Doit être `plugin`. |
| `plugins[].atlas.schemaVersion` | Version du schéma de l’entrée. |
| `plugins[].name` | Nom affiché du plugin. |
| `plugins[].version` | Version publiée du plugin. |
| `plugins[].description` | Description courte de repli. |
| `plugins[].descriptions` | Descriptions localisées facultatives, par exemple `de`, `en` et `fr`. |
| `plugins[].icon` | Chemin ou URL de l’icône ; une seule suffit pour le Hub et l’Administration. |
| `plugins[].preview` | Chemin ou URL d’un aperçu, facultatif. |
| `plugins[].package` | Chemin ou URL du package installable. |
| `plugins[].manifest` | Chemin ou URL du manifeste de repli. |
| `plugins[].capabilities` | Capacités déclarées. |
| `plugins[].compatibility` | Compatibilité ATLAS et hôte. |

Les chemins relatifs sont résolus par rapport au `repository.json` chargé.
`package` désigne le package installable ; `manifest` reste disponible pour
l’aperçu, les diagnostics et la vérification manuelle.

## Exemple

Cet exemple illustre le schéma ; ses numéros de version ne désignent pas
la version actuelle d’ATLAS.

```json
{
  "kind": "atlas.plugin.repository",
  "atlas": {
    "type": "plugin-repository",
    "schemaVersion": 1
  },
  "name": "ATLAS Plugin Demo Repository",
  "version": "0.1.0",
  "plugins": [
    {
      "id": "atlas-homeassistant-card-editor",
      "atlas": {
        "type": "plugin",
        "schemaVersion": 1
      },
      "name": "Home Assistant Card Editor",
      "version": "0.1.54",
      "description": "Reference plugin for Home Assistant cards.",
      "descriptions": {
        "de": "Referenz-Plugin für Home-Assistant-Cards.",
        "en": "Reference plugin for Home Assistant cards."
      },
      "icon": "plugins/card-editor/icon.svg",
      "preview": "plugins/card-editor/preview.png",
      "package": "plugins/card-editor/atlas-plugin.json",
      "manifest": "plugins/card-editor/plugin.atlas-plugin.json",
      "capabilities": ["homeassistant.card-editor"],
      "compatibility": {
        "atlas": ">=0.1.54",
        "host": ["administration", "hub", "homeassistant-addon"]
      }
    }
  ]
}
```
