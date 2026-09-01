# Plugin-Dokumentation

ATLAS soll langfristig als erweiterbare Plattform funktionieren. Die Plugin-Dokumentation beschreibt deshalb nicht nur eine einzelne API, sondern den gesamten Weg von der Idee bis zur verteilbaren Erweiterung.

::: warning Planungsstand
Die Plugin-Schnittstellen sind noch in Arbeit. Diese Seite hält den Zielrahmen fest und wird mit den stabilen Verträgen Schritt für Schritt konkretisiert.
:::

## Ziel

Plugins sollen ATLAS erweitern können, ohne Kernpakete oder bestehende Anwendungen direkt zu verändern.

Geplante Einsatzbereiche sind:

- Home-Assistant-nahe Werkzeuge wie Card-Editoren, Diagnoseflächen und Lovelace-Helfer
- eigenständige UGSo-Projekte wie die geplante Lovelace UV Card
- wiederverwendbare Provider, Renderer, Themes und Devtools-Erweiterungen
- optionale Community-Erweiterungen mit klaren Verträgen

## Plugin-Lebenszyklus

Ein Plugin soll später einen nachvollziehbaren Lebenszyklus besitzen:

1. Manifest lesen
2. Abhängigkeiten prüfen
3. Plugin registrieren
4. Services, Commands oder UI-Flächen bereitstellen
5. Aktivieren
6. Diagnose- und Statusdaten melden
7. Deaktivieren oder sauber entfernen

Die Dokumentation wird diese Schritte mit Beispielen begleiten, sobald die Verträge stabil sind.

## Aktueller technischer Anker

Der erste technische Schritt ist ein Runtime-Adapter. Ein `RuntimePlugin` kann mit `createRuntimeModuleFromPlugin()` in ein vorhandenes ATLAS Runtime-Modul übersetzt werden. Dadurch nutzt ein Plugin denselben Start-, Diagnose- und Shutdown-Weg wie andere Runtime-Module.

Der Adapter bewahrt Plugin-Metadaten, Extension Points und bereitgestellte Fähigkeiten. Optionale Plugin-Hooks wie `deactivate()` und `dispose()` werden über den Runtime-Shutdown ausgeführt.

Mit `RuntimePluginCatalog` gibt es außerdem eine erste Discovery-Fläche. Sie registriert Plugins nach ID, stellt beschreibende Metadaten bereit und kann Plugins nach Extension Point oder bereitgestellter Capability finden.

`createRuntimePluginAdministrationView()` bereitet die spätere Atlas Administration vor. Die Funktion erzeugt aus Plugin-Katalogdaten eine Verwaltungsansicht mit Statuswerten wie `available`, `active` und `disabled` sowie Aktionen wie `inspect`, `activate`, `deactivate` und `export-package`.

Mit `createRuntimePluginInstallPackage()` gibt es auch den ersten Paketvertrag. Er erzeugt eine Paketbeschreibung mit `atlas-plugin.json`, `README.md` und optionalen Zusatzdateien, die später von der Administration oder einem Archiv-Builder als installierbares Paket ausgegeben werden kann.

`parseRuntimePluginInstallPackage()` liest diese Paketbeschreibung wieder als validierten Descriptor ein. Dabei wird kein Plugin-Code ausgeführt. Die Administration kann importierte Pakete dadurch sicher anzeigen, prüfen, erneut exportieren und wieder aus der lokalen Importliste entfernen. Aktivierungszustände werden in der lokalen Demo-Administration gemerkt, damit Plugin-Listen einen Reload überstehen.

Zusätzlich gibt es eine erste ATLAS-Repository-Installation in der Administration. Eine hinzugefügte `repository.json` wird geladen, verfügbare Plugins werden angezeigt und Pakete können aus `package`- oder `manifest`-URLs in den lokalen Administrationsspeicher installiert werden. Pro Repository-Plugin wird die installierte Version mit der Repository-Version verglichen, sodass die Administration `Installieren`, `Aktualisieren` und `Entfernen` anbieten kann. Dieser erste Schritt installiert noch browser-/administrationsnah; ein späterer Host-Installer kann daraus echte Dateisystem- oder Add-on-Installationen ableiten.

## Erstes Referenz-Plugin

Der Home Assistant Card Editor wird als erstes offizielles ATLAS-Referenz-Plugin behandelt. Er ist damit nicht nur eine Demo, sondern der praktische Nachweis, dass Plugin-Lebenszyklus, Discovery, Administration, Import/Export und Paketbau zusammen funktionieren.

Im Atlas-Code stellt `createHomeAssistantCardEditorPlugin()` diesen Editor als `RuntimePlugin` bereit. Bei der Aktivierung registriert das Plugin einen Service mit Card Targets, Editor-Templates, Bubble-Button-Typen und Fähigkeiten, die später in der Atlas Administration angezeigt werden können.

Zusätzlich erzeugt `createHomeAssistantCardEditorPluginInstallPackage()` ein erstes Installpaket für dieses Referenz-Plugin. Es enthält ein Plugin-Manifest, eine README und ein Beispiel für eine Home-Assistant-Card-Konfiguration.

Als Referenz-Plugin nutzt der Editor folgende Extension Points:

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

Dadurch entsteht ein echtes Beispiel für weitere Plugins: sichtbar in der Atlas Administration, aktivierbar über den Plugin-Katalog und exportierbar als installierbares Paket.

## Geplante Extension-Flächen

Die ersten Extension-Flächen sollen sich an den bestehenden ATLAS-Paketen orientieren:

| Bereich | Geplante Erweiterung |
|---|---|
| Runtime | Services, Lifecycle-Hooks und Aktivierungsregeln |
| Home Assistant | Card-Targets, Entity-Auswahl, Ressourcenprüfung und Exportpfade |
| Renderer | Render-Adapter und Zielflächen |
| Theme | Tokens, Theme-Varianten und visuelle Presets |
| Devtools | Diagnosepanels, Inspektoren und Entwicklungshelfer |

## Struktur einer Plugin-Doku

Eine vollständige Plugin-Doku soll später folgende Kapitel enthalten:

- Plugin-Grundlagen
- Manifest und Metadaten
- Lebenszyklus und Aktivierung
- Service-Registrierung
- Extension APIs
- Home-Assistant-spezifische Erweiterungen
- Beispiele
- Tests
- Versionierung
- Veröffentlichung und HACS-/Paket-Hinweise

## Repository-Format und Demo-Vorlage

ATLAS nutzt ein eigenes Repository-Format für installierbare Plugins. Ein Repository ist bewusst kein Home-Assistant-Add-on-Repository: Es muss sich mit ATLAS-Metadaten ausweisen, damit die Administration nicht versehentlich beliebige Home-Assistant-Repositories als Plugin-Quelle akzeptiert.

Referenz-Repository:

- Demo-Repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installations-Zwischenseite: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

Empfohlene Struktur:

```text
repository.json
plugins/
  example-plugin/
    plugin.atlas-plugin.json
    icon.png
    preview.png
    README.md
```

Die `repository.json` enthält mindestens folgende Informationen:

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

Beispiel:

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

Das Demo-Repository ist gleichzeitig Testquelle und Vorlage. Später kann daraus ein Generator entstehen, der ein neues ATLAS-Plugin mit korrekter Ordnerstruktur, Manifest, Icon, optionalem Vorschaubild und README vorbereitet.

## Atlas Administration

Für die Verwaltung von Plugins ist eine eigene Atlas-Administration als Weboberfläche geplant. Sie soll nicht nur installierte Plugins anzeigen, sondern den gesamten Arbeitsfluss rund um Plugins unterstützen.

Der erste sichtbare Schritt ist eine eigene minimale Administration auf Port `4175`, getrennt vom Home-Assistant-Card-Editor auf Port `4174`. Sie liest den Runtime-Plugin-Katalog, zeigt den Home Assistant Card Editor als erstes Referenz-Plugin, stellt Status, Version, Extension Points und Fähigkeiten dar und bietet erste Aktionen wie Prüfen, Aktivieren, Deaktivieren, Paket exportieren und Paket importieren.

Die Administration ist außerdem der zentrale Ort für sensible Verbindungseinstellungen. Home-Assistant-Tokens sollen dort verwaltet und bei `Save settings` lokal gespeichert werden können. Der lokale Admin-Server stellt gespeicherte Verbindungseinstellungen dem Card Editor bereit, damit Reloads und direkte Editor-Aufrufe funktionieren. Der Card Editor erhält den Token nur als Übergabe an die aktive Browser-Sitzung und kann optional nach dieser Übergabe automatisch verbinden. Plugins bekommen später nur freigegebene Kontextdaten wie Home-Assistant-URL, WebSocket-Pfad, erlaubte Ressourcenpfade und deklarierte Fähigkeiten, aber keinen rohen Access Token.

Geplante Funktionen sind:

- installierte Plugins anzeigen, aktivieren und deaktivieren
- Plugin-Status, Versionen, Abhängigkeiten und Diagnosemeldungen prüfen
- neue Plugins über einen Wizard oder eine Vorlage erstellen
- Plugin-Manifeste und Extension Points bearbeiten
- Plugins importieren und exportieren
- installierbare Pakete erzeugen, zum Beispiel ZIP- oder HACS-nahe Bundles
- Demo-Daten, Beispielkonfigurationen und README-Dateien für Pakete mitliefern

Die Administration soll langfristig als zentrale Oberfläche für Plugin-Verwaltung, Paketbau und Qualitätsprüfung dienen.

## Beispielrichtung

Ein einfaches Plugin könnte später etwa:

- ein Manifest bereitstellen
- einen Service registrieren
- einen Home-Assistant-Card-Typ anbieten
- Ressourcenabhängigkeiten beschreiben
- Beispiel-Entities oder Demo-Daten mitliefern

So bleibt eine Erweiterung installierbar, testbar und nachvollziehbar.

## Veröffentlichungsregeln

Für veröffentlichbare Plugins sind geplant:

- eindeutige Paket- und Plugin-Namen
- klare Versionsangaben
- dokumentierte Abhängigkeiten
- sichere Demo- oder Fallback-Daten
- nachvollziehbare Build- und Export-Artefakte
- Hinweise für Home Assistant, HACS oder eigenständige ATLAS-Nutzung

## Nächste Schritte

Die nächsten Doku-Schritte sind:

1. Plugin-Verträge im Atlas-Repo stabilisieren
2. den Home Assistant Card Editor als erstes Referenz-Plugin modellieren
3. Manifest- und Lifecycle-Beispiele ergänzen
4. Home-Assistant-spezifische Plugin-Erweiterungen dokumentieren
5. Repository-Format mit Demo-Repository konkretisieren
6. Atlas-Administration für Plugin-Verwaltung und Paketbau beschreiben
7. Plugin-Vorlage und späteren Generator aus dem Demo-Repository ableiten
8. Publishing-Checkliste ausarbeiten
