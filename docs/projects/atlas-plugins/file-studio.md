# ATLAS File Studio

ATLAS File Studio ist das zweite unabhängige ATLAS-Plugin. Es soll Dateien in freigegebenen Home-Assistant-Pfaden bearbeiten, ohne standardmäßig freien Root-Zugriff zu erlauben.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Aktueller Stand

File Studio ist als installierbares ATLAS-Plugin veröffentlicht und kann über das Demo-Repository in Administration und Hub getestet werden.

- Dateibaum für den freigegebenen `/config`-Bereich
- flexible Zwei-Spalten-Oberfläche mit begrenzbarer Maximalbreite und Maximalhöhe
- Datei- und Ordneraktionen direkt am Pfad: Datei anlegen, Ordner anlegen, neu laden und alle Ordner einklappen
- Editorfläche mit lokaler CodeMirror-6-Bündelung
- Syntax Highlighting für YAML, JSON, JavaScript, TypeScript und Markdown
- YAML-Prüfung vor dem Speichern
- Speichern der aktuell bearbeiteten Datei
- lokal speichern, Upload und Download
- `/config` als Standardwurzel
- Add-on-Verzeichnis nur nach Admin-Freigabe
- kein freier Root-Zugriff standardmäßig

Die Editor-Bibliothek wird lokal mit dem Plugin ausgeliefert. Dadurch braucht File Studio für die Codeansicht kein CDN und bleibt auch im Home-Assistant-Add-on-Betrieb nachvollziehbar versioniert.

## Sicherheitsmodell

Der erste Plugin-Vertrag beschreibt eine feste Zugriffspolitik:

| Pfad | Standard | Freigabe |
|---|---|---|
| `/config` | aktiv | ohne zusätzliche Freigabe |
| `/addons` | deaktiviert | nur über Atlas Administration |
| `/` | deaktiviert | nicht standardmäßig erlaubt |

Damit kann der Installations- und Update-Fluss bereits getestet werden, bevor echter Dateizugriff in der Add-on-Runtime freigeschaltet wird.

## Nächste Ausbaustufen

- feinere Home-Assistant-YAML-Hilfen auf Basis bekannter HA-Strukturen
- bessere Dateityp-Icons nach dem Vorbild von VS Code Icons
- optionaler Icon-/Logo-Studio-Workflow mit SVG- und PNG-Ausgabe
- Speichern von Icon-SVGs unter `/config/www/custom_local_icons/`, wenn die passende Home-Assistant-Integration genutzt wird
