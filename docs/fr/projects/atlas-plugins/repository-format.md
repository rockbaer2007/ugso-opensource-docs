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

Le serveur App installe les paquets validés dans le stockage persistant et sert
leurs fichiers web. JavaScript s’exécute à l’ouverture dans le navigateur ;
modules Node et hooks Runtime ne sont pas enregistrés automatiquement. Ce n’est
pas une sandbox ; voir le [contrat Runtime](./developers/runtime).

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
      "id": "atlas.plugin.example",
      "atlas": {
        "type": "plugin",
        "schemaVersion": 1
      },
      "name": "Example Plugin",
      "version": "0.1.0",
      "description": "Example static ATLAS web plugin.",
      "descriptions": {
        "de": "Statisches ATLAS-Beispielplugin.",
        "en": "Static ATLAS example plugin."
      },
      "icon": "plugins/example/icon.svg",
      "preview": "plugins/example/preview.png",
      "package": "plugins/example/package.atlas-plugin.json",
      "manifest": "plugins/example/atlas-plugin.json",
      "capabilities": ["atlas.example"],
      "compatibility": {
        "atlas": ">=0.1.312 <0.2.0",
        "host": ["docker", "linux", "homeassistant"]
      }
    }
  ]
}
```
