# ATLAS File Studio

ATLAS File Studio ist das zweite unabhängige ATLAS-Plugin. Es soll Dateien in freigegebenen Home-Assistant-Pfaden bearbeiten, ohne standardmäßig freien Root-Zugriff zu erlauben.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Aktueller Stand

File Studio ist als installierbares ATLAS-Plugin veröffentlicht und kann über das Demo-Repository in Administration und Hub getestet werden.

- aktueller Plugin-Stand: `0.1.36`
- aktueller Home-Assistant-App/Add-on-Stand: `0.1.122`
- Dateibaum für den freigegebenen `/config`-Bereich
- flexible Zwei-Spalten-Oberfläche mit begrenzbarer Maximalbreite und Maximalhöhe
- kompakte Werkzeugzeile unterhalb von `Dateibaum /config`, damit die Icons in
  schmaleren Ansichten nicht in die rechte Dateiliste rutschen
- Datei- und Ordneraktionen direkt am Pfad: Datei anlegen, Ordner anlegen, neu laden und alle Ordner einklappen
- Editorfläche mit lokaler CodeMirror-6-Bündelung
- große Dateien scrollen innerhalb der Editorfläche, damit die Statuszeile unten sichtbar bleibt
- Syntax Highlighting für YAML, JSON, JavaScript, TypeScript und Markdown
- YAML-Prüfung vor dem Speichern mit Home-Assistant-Hinweisen für häufige Dateien wie `configuration.yaml`, `automations.yaml`, `scripts.yaml` und Packages, inklusive typischer Root-Keys, Automations-/Script-Struktur und direkt eingetragener Secret-Werte
- Speichern der aktuell bearbeiteten Datei
- automatische Backups vor dem Speichern, Verlaufsliste der letzten Sicherungen,
  Vergleich mit dem aktuellen Stand und Wiederherstellen einer ausgewählten
  Sicherung
- lokal speichern, Drag-and-drop-Upload, Mehrfach-Upload und Download
- Downloadnamen werden im Browser automatisch hochgezählt, zum Beispiel `configuration.yaml`, `configuration-1.yaml`, `configuration-2.yaml`
- Upload-Konflikte können im File-Studio-Dialog ersetzt, umbenannt oder abgebrochen werden
- Mehrfachauswahl für Löschen, Kopieren und Verschieben
- Papierkorb mit Wiederherstellen statt sofortigem endgültigem Löschen; das
  rechte Toolbar-Icon ist grau im leeren Zustand und rot, sobald Einträge
  vorhanden sind
- Favoritenleiste für häufig genutzte Dateien und Ordner
- farbige Dateityp-Icons mit kompakten Typ-Badges
- Suche mit Typfilter, optionaler Inhaltssuche, Trefferzeile und Inhaltsvorschau
- opt-in Problembericht im File-Studio-Dialog mit Vorschau und vorbereitetem GitHub-Issue-Link; der Bericht enthält keine Home-Assistant-Token, Provider-API-Keys oder Dateiinhalte
- ZIP-Inhaltsvorschau ohne Entpacken
- `/config` als Standardwurzel
- zusätzliche Pfad-Freigaben für `www`, `custom_components`, `addons` und `parent-of-config`
- Add-on-Verzeichnis nur nach Admin- oder Add-on-Freigabe
- kein freier Root-Zugriff standardmäßig

Die Editor-Bibliothek wird lokal mit dem Plugin ausgeliefert. Dadurch braucht File Studio für die Codeansicht kein CDN und bleibt auch im Home-Assistant-Add-on-Betrieb nachvollziehbar versioniert.

## Sicherheitsmodell

Der erste Plugin-Vertrag beschreibt eine feste Zugriffspolitik:

| Pfad | Standard | Freigabe |
|---|---|---|
| `/config` | aktiv | ohne zusätzliche Freigabe |
| `/config/www` | sichtbar als Fähigkeit | über Atlas Administration oder Add-on-Option |
| `/config/custom_components` | sichtbar als Fähigkeit | über Atlas Administration oder Add-on-Option |
| `/addons` | deaktiviert | über Atlas Administration oder Add-on-Option |
| `parent-of-config` | deaktiviert | nur bewusst als Admin-Freigabe |
| `/` | deaktiviert | nicht standardmäßig erlaubt |

`/config` ist der normale Home-Assistant-Konfigurationsbereich. Dort liegen zum Beispiel `configuration.yaml`, `automations.yaml`, Dashboards, Themes, Blueprints, Skripte und lokale Webdateien unter `www`.

`/addons` wird für lokale Home-Assistant-Add-ons genutzt. Dort können eigene Add-on-Ordner mit Dateien wie `config.yaml`, `Dockerfile`, Startskripten, Icons und Dokumentation liegen. Weil Änderungen dort direkt installierbare Add-ons beeinflussen können, bleibt dieser Bereich in File Studio standardmäßig gesperrt und wird nur nach bewusster Freigabe in der Atlas Administration sichtbar.

Im Home-Assistant-App/Add-on-Betrieb kommen diese Freigaben aus der Add-on-Konfiguration. In Docker- oder Linux-Installationen steuert Atlas Administration dieselben Datei-Fähigkeiten. Plugins erhalten dabei keine rohen Dauer-Secrets, sondern nur den freigegebenen Pfadkontext.

## Home-Assistant-Update-Hinweis

Nach jedem sichtbaren ATLAS-Update wird die Home-Assistant-App/Add-on-Version angehoben. Home Assistant vergleicht die installierte Version (`old`) mit der Repository-Version (`target`). Fuer diesen Stand sollte `target` mindestens `0.1.122` anzeigen. Wenn weiter eine alte Zielversion erscheint, im Add-on Store die Repository-Informationen neu laden und anschliessend ATLAS aktualisieren oder neu starten.

Damit kann der Installations- und Update-Fluss bereits getestet werden, bevor echter Dateizugriff in der Add-on-Runtime freigeschaltet wird.

## Nächste Ausbaustufen

- Home-Assistant-YAML-Hilfen weiter ausbauen, zum Beispiel mit echter Schema-/Service-Prüfung gegen eine verbundene Home-Assistant-Instanz
- Archiv-Unterstützung nach ZIP: `.rar` inklusive RAR5, `.tar`, `.tar.gz`,
  `.tgz`, `.gz` und `.gzip` lesen und extrahieren
- Archiv-Extraktion zuerst sicher als Inhaltsliste und gezieltes
  Einzeldatei-Extrahieren, später mit geschützter Alles-extrahieren-Aktion
- optionaler Icon-/Logo-Studio-Workflow mit SVG- und PNG-Ausgabe
- Speichern von Icon-SVGs unter `/config/www/custom_local_icons/`, wenn die passende Home-Assistant-Integration genutzt wird
