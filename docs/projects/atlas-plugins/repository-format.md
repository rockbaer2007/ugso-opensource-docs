# Repository-Format

ATLAS nutzt ein eigenes Repository-Format für installierbare Plugins. Ein Repository ist bewusst kein Home-Assistant-Add-on-Repository: Es muss sich mit ATLAS-Metadaten ausweisen, damit die Administration nicht versehentlich beliebige Home-Assistant-Repositories als Plugin-Quelle akzeptiert.

## Referenz

- Demo-Repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installations-Zwischenseite: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`
- Offizielle Plugin-Vorlage: [atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template) (GitHub-Funktion „Use this template“)

Die Vorlage enthält ein funktionsfähiges Beispiel-Plugin, Manifest, Katalog,
Grafiken, Paketgenerator und Validierung. Nach Änderungen am Manifest erzeugt
`npm run build` das installierbare Paket und synchronisiert die Katalogdaten;
`npm run check` prüft die Konsistenz. GitHub Actions führt beide Prüfungen aus.

Der App-Server installiert geprüfte Pakete persistent und stellt ihre statischen
Webdateien bereit. JavaScript läuft beim Öffnen im Browser; Node-Module und
Runtime-Hooks werden dadurch nicht automatisch registriert. Die Installation
ist keine Sandbox; siehe [Runtime-Vertrag](./developers/runtime).

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

Schema-Beispiel für ein eigenes Plugin, keine aktuelle Version des integrierten
Card Editors. Die ID muss nach Veröffentlichung stabil bleiben.

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
