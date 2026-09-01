# Repository-Format

ATLAS nutzt ein eigenes Repository-Format für installierbare Plugins. Ein Repository ist bewusst kein Home-Assistant-Add-on-Repository: Es muss sich mit ATLAS-Metadaten ausweisen, damit die Administration nicht versehentlich beliebige Home-Assistant-Repositories als Plugin-Quelle akzeptiert.

## Referenz

- Demo-Repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installations-Zwischenseite: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

## Struktur

```text
repository.json
plugins/
  example-plugin/
    plugin.atlas-plugin.json
    icon.png
    preview.png
    README.md
```

## Felder

| Feld | Zweck |
|---|---|
| `kind` | Muss `atlas.plugin.repository` sein. |
| `atlas.type` | Muss `plugin-repository` sein. |
| `atlas.schemaVersion` | Schema-Version der ATLAS-Repository-Datei. |
| `name` | Anzeigename des Repositorys. |
| `version` | Version des Repository-Katalogs. |
| `homepage` | Optionale Projekt- oder GitHub-Seite. |
| `installPage` | Optionale ATLAS-Zwischenseite zum Kopieren der Repository-URL. |
| `plugins[]` | Liste installierbarer Plugins. |
| `plugins[].id` | Eindeutige Plugin-ID. |
| `plugins[].atlas.type` | Muss `plugin` sein. |
| `plugins[].atlas.schemaVersion` | Schema-Version des Plugin-Eintrags. |
| `plugins[].name` | Anzeigename des Plugins. |
| `plugins[].version` | Veröffentlichte Plugin-Version. |
| `plugins[].description` | Fallback-Kurzbeschreibung. |
| `plugins[].descriptions` | Optionale lokalisierte Beschreibungen, zum Beispiel `de` und `en`. |
| `plugins[].icon` | Pfad oder URL zum Plugin-Icon. Ein Icon reicht für Hub und Administration. |
| `plugins[].preview` | Optionaler Pfad oder URL zu einem Vorschaubild. |
| `plugins[].package` | Pfad oder URL zum installierbaren Paket. |
| `plugins[].manifest` | Fallback-Pfad oder URL zum Manifest. |
| `plugins[].capabilities` | Deklarierte Fähigkeiten. |
| `plugins[].compatibility` | ATLAS-/Host-Kompatibilität. |

Relative Pfade werden relativ zur geladenen `repository.json` aufgelöst. `package` zeigt auf das installierbare Plugin-Paket, `manifest` bleibt als lesbarer Fallback für Vorschau, Diagnose und manuelle Prüfung erhalten.

## Beispiel

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
      "description": "Referenz-Plugin für Home-Assistant-Cards.",
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
