# ATLAS File Studio

ATLAS File Studio ist das zweite unabhängige ATLAS-Plugin. Es soll Dateien in freigegebenen Home-Assistant-Pfaden bearbeiten, ohne standardmäßig freien Root-Zugriff zu erlauben.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Aktueller Stand

File Studio ist als installierbares ATLAS-Plugin veröffentlicht und kann über das Demo-Repository in Administration und Hub getestet werden.

- aktueller Plugin-Stand: `0.1.29`
- aktueller Home-Assistant-App/Add-on-Stand: `0.1.91`
- Dateibaum für den freigegebenen `/config`-Bereich
- flexible Zwei-Spalten-Oberfläche mit begrenzbarer Maximalbreite und Maximalhöhe
- Datei- und Ordneraktionen direkt am Pfad: Datei anlegen, Ordner anlegen, neu laden und alle Ordner einklappen
- Editorfläche mit lokaler CodeMirror-6-Bündelung
- Syntax Highlighting für YAML, JSON, JavaScript, TypeScript und Markdown
- YAML-Prüfung vor dem Speichern mit Home-Assistant-Hinweisen für häufige Dateien wie `configuration.yaml`, `automations.yaml`, `scripts.yaml` und Packages
- Speichern der aktuell bearbeiteten Datei
- automatische Backups vor dem Speichern und einfache Verlaufsliste der letzten Sicherungen
- lokal speichern, Upload und Download
- Downloadnamen werden im Browser automatisch hochgezählt, zum Beispiel `configuration.yaml`, `configuration-1.yaml`, `configuration-2.yaml`
- Upload-Konflikte können ersetzt, umbenannt oder abgebrochen werden
- Suche mit Trefferzeile und Inhaltsvorschau
- opt-in Problembericht mit Vorschau; der Bericht enthält keine Home-Assistant-Token, Provider-API-Keys oder Dateiinhalte
- ZIP-Inhaltsvorschau ohne Entpacken
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

`/config` ist der normale Home-Assistant-Konfigurationsbereich. Dort liegen zum Beispiel `configuration.yaml`, `automations.yaml`, Dashboards, Themes, Blueprints, Skripte und lokale Webdateien unter `www`.

`/addons` wird für lokale Home-Assistant-Add-ons genutzt. Dort können eigene Add-on-Ordner mit Dateien wie `config.yaml`, `Dockerfile`, Startskripten, Icons und Dokumentation liegen. Weil Änderungen dort direkt installierbare Add-ons beeinflussen können, bleibt dieser Bereich in File Studio standardmäßig gesperrt und wird nur nach bewusster Freigabe in der Atlas Administration sichtbar.

Damit kann der Installations- und Update-Fluss bereits getestet werden, bevor echter Dateizugriff in der Add-on-Runtime freigeschaltet wird.

## Nächste Ausbaustufen

- Home-Assistant-YAML-Hilfen weiter ausbauen, zum Beispiel für Includes, Pakete, Automationen und Skripte
- Wiederherstellen aus der Verlaufsliste direkt in der Oberfläche
- Problembericht später mit GitHub-Issue-Link vorbereiten
- bessere Dateityp-Icons nach dem Vorbild von VS Code Icons
- Archiv-Unterstützung nach ZIP: `.rar` inklusive RAR5, `.tar`, `.tar.gz`,
  `.tgz`, `.gz` und `.gzip` lesen und extrahieren
- Archiv-Extraktion zuerst sicher als Inhaltsliste und gezieltes
  Einzeldatei-Extrahieren, später mit geschützter Alles-extrahieren-Aktion
- optionaler Icon-/Logo-Studio-Workflow mit SVG- und PNG-Ausgabe
- Speichern von Icon-SVGs unter `/config/www/custom_local_icons/`, wenn die passende Home-Assistant-Integration genutzt wird
