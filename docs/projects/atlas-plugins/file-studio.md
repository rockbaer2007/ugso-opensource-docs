# ATLAS File Studio

ATLAS File Studio ist das zweite unabhängige ATLAS-Plugin. Es soll Dateien in freigegebenen Home-Assistant-Pfaden bearbeiten, ohne standardmäßig freien Root-Zugriff zu erlauben.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Geplanter Funktionsumfang

- Dateibaum
- Editorfläche
- Syntax Highlighting
- YAML-Prüfung
- Upload und Download
- `/config` als Standardwurzel
- Add-on-Verzeichnis nur nach Admin-Freigabe
- kein freier Root-Zugriff standardmäßig

## Sicherheitsmodell

Der erste Plugin-Vertrag beschreibt eine feste Zugriffspolitik:

| Pfad | Standard | Freigabe |
|---|---|---|
| `/config` | aktiv | ohne zusätzliche Freigabe |
| `/addons` | deaktiviert | nur über Atlas Administration |
| `/` | deaktiviert | nicht standardmäßig erlaubt |

Damit kann der Installations- und Update-Fluss bereits getestet werden, bevor echter Dateizugriff in der Add-on-Runtime freigeschaltet wird.
