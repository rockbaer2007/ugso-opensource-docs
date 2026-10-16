# ATLAS File Studio

ATLAS File Studio ist das zweite unabhängige ATLAS-Plugin. Es soll Dateien in freigegebenen Home-Assistant-Pfaden bearbeiten, ohne standardmäßig freien Root-Zugriff zu erlauben.

## Papierkorb und Historie über App-Updates

Ab ATLAS **0.1.312** liegen die vom ATLAS-Backend verwalteten Ablagen standardmäßig
unter `ATLAS_PLUGIN_DATA_ROOT/.file-studio/{trash,history}`. Docker muss die
Plugin-Datenablage als Volume behalten; in der HA-App liegt sie unter
`/data/atlas-plugins`. Vorhandene Linux-Installer-Pfade und die Overrides
`ATLAS_FILE_STUDIO_TRASH_ROOT` / `ATLAS_FILE_STUDIO_HISTORY_ROOT` bleiben gültig.
Bei eigenen Pfaden müssen auch diese dauerhaft eingebunden und gesichert werden.

**Erster Wechsel von einer älteren Container-Version:** Zuerst die alten
Papierkorb-/Historienordner und die persistenten Daten sichern. File-Studio-
Schreibaktionen bis zum Update pausieren. Den eigenständig ausführbaren Helfer
aus dem geprüften ATLAS-Release in den noch vorhandenen alten Container kopieren:

```sh
docker cp scripts/atlas-file-studio-retention.mjs ALTER_CONTAINER:/tmp/atlas-file-studio-retention.mjs
docker exec ALTER_CONTAINER node /tmp/atlas-file-studio-retention.mjs --app-root /app --plugin-root /data/atlas-plugins
```

Die Pfade gelten für das Standard-Image; bei eigenen Installationen prüfen.
Bei der HA-App denselben Helfer im bisherigen App-Terminal vor dem Update
ausführen. Er übernimmt erreichbare Altbestände einmalig, erhält Quellen und
Eintragskennungen und überschreibt keine abweichenden Zieldateien. Konflikte
zuerst anhand der Sicherung prüfen. Nach Erfolg auch die persistente Ablage
sichern, dann den Container ersetzen. Ein Übernahmemarker verhindert, dass
wiederhergestellte Einträge beim Neustart erneut importiert werden.

Bereits mit einem alten Container verlorene Dateien werden dadurch nicht
zurückgeholt; dafür ist eine vorhandene Sicherung nötig. Nach der isolierten
Prüfung wurde am 16.10.2026 auch der Wechsel von 0.1.311 auf 0.1.312 auf
Proxmox und Pi 5 geprüft: vorher frische HA-Backups, Übernahme im alten Container
und PC-Sicherung der alten sowie vorbereiteten Ablagen. Je Host bleiben beide
alten Papierkorbeinträge und alle zwölf Historien-Dateien erhalten, ebenso
Einstellungen, aktive Dateien, Projekte und Plugins. Dies ist kein Test einer
vollständigen HAOS-Backup-Wiederherstellung.

Ein separater vollständiger HAOS-Restore wurde anschließend mit eigenen Testdaten
geprüft: verschlüsseltes Vollbackup auf dem PC sichern, in eine frische Hyper-V-
HAOS-Instanz hochladen und über den Supervisor wiederherstellen. Einstellungen,
Projekt, sechs Plugins, Papierkorb und Historie sowie 154 geprüfte Dateien bleiben
erhalten. Die Testadresse wurde beibehalten; Pi 5 und Proxmox bleiben unverändert.
Ein zweiter frischer HAOS-Test wurde unter einer anderen IP-Adresse geprüft:
Alle 154 Dateien und die bisherigen Zugangsdaten bleiben erhalten. Gespeicherte
Adressen werden nicht automatisch umgeschrieben. Nach der Wiederherstellung in
der **Konfiguration der ATLAS-App** nur die Home-Assistant-URL ändern und die App
neu starten. Unter **Einstellungen → Geräte & Dienste → ATLAS Runtime →
Konfigurieren** die neue Runtime-Adresse einschließlich Port `4176` eintragen.
Der bestehende HA-Token muss in diesem geprüften vollständigen Restore nicht
ersetzt werden. Plugin-Links verwenden automatisch die neue ATLAS-Adresse.
Anschließend Verbindung, Projekte, Papierkorb und Historie prüfen.

Diese isolierten Prüfungen ersetzen keinen Wiederherstellungstest eines
produktiven Backups auf anderer Hardware; ARM64 und physische Geräte bleiben offen.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installationsseite: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository-Datei: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Aktueller Stand

File Studio ist als installierbares ATLAS-Plugin veröffentlicht und kann über das Demo-Repository in Administration und Hub getestet werden.

- aktueller Plugin-Stand: `0.1.52`
- französische Oberfläche: DE/EN/FR-Auswahl, Kopfzeile, zentrale Werkzeugleisten-Steuerelemente und Hinweise zur Upload-Grenze; Dialoge und weitere Ablaufmeldungen sind noch nicht vollständig übersetzt
- Upload-Hinweis: Dateien bis 64 MiB können direkt hochgeladen werden; bei größeren Dateien verweist File Studio auf die Samba-App
- dokumentierter Home-Assistant-App/Add-on-Stand: `0.1.312` (16.10.2026)
- Bildvorschau: SVG-, PNG-, JPG/JPEG- und WebP-Dateien direkt an das separat installierte ATLAS Icon Studio übergeben. Rasterdateien öffnen sich dort als Vorschau; einfache SVG-Pfaddateien werden in das monochrome Iconset importiert.
- Die Übergabe verwendet einen kurzlebigen Schlüssel im lokalen Browser und den freigegebenen File-Studio-Dateizugriff. Beide Plugins müssen auf demselben ATLAS-Server installiert sein; die Datei wird nicht hochgeladen oder dupliziert.
- Dateibaum für den freigegebenen `/config`-Bereich
- flexible Zwei-Spalten-Oberfläche mit begrenzbarer Maximalbreite und Maximalhöhe
- kompakte Werkzeugzeile unterhalb von `Dateibaum /config`, damit die Icons in
  schmaleren Ansichten nicht in die rechte Dateiliste rutschen
- Datei- und Ordneraktionen direkt am Pfad: Datei anlegen, Ordner anlegen, neu laden und alle Ordner einklappen
- Editorfläche mit lokaler CodeMirror-6-Bündelung
- große Dateien scrollen innerhalb der Editorfläche, damit die Statuszeile unten sichtbar bleibt
- direkte Links öffnen Dateien auch dann, wenn sie tiefer liegen als der zuerst
  geladene Dateibaum, zum Beispiel Automation-Exporter-Ausgaben
- Syntax Highlighting für YAML, JSON, JavaScript, TypeScript und Markdown
- YAML-Prüfung vor dem Speichern mit Home-Assistant-Hinweisen für häufige Dateien wie `configuration.yaml`, `automations.yaml`, `scripts.yaml` und Packages, inklusive typischer Root-Keys, Automations-/Script-Struktur und direkt eingetragener Secret-Werte
- Speichern der aktuell bearbeiteten Datei
- automatische Backups vor dem Speichern, Verlaufsliste der letzten Sicherungen,
  Vergleich mit dem aktuellen Stand und Wiederherstellen einer ausgewählten
  Sicherung
- lokal speichern, Drag-and-drop-Upload, Mehrfach-Upload und Download
- Uploads werden im aktuell ausgewählten Ordner gespeichert
- Nach dem Upload wird der Dateibaum aktualisiert, ohne die Datei automatisch zu öffnen
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
- Dateien bis 64 MiB direkt in einen freigegebenen Zielordner hochladen; der Transfer erfolgt als Binärdaten statt als Base64-JSON
- bei größeren Dateien den Upload direkt abbrechen und auf die [Home-Assistant-Samba-App](https://github.com/home-assistant/addons/tree/master/samba) verweisen
- ZIP-, TAR-, TAR.GZ- und TGZ-Inhaltsvorschau
- einzelne Dateien direkt aus der Archivvorschau extrahieren, ohne das ganze Archiv zu entpacken
- vollständige TAR-Archive mit Pfadprüfung sowie Grenzen für Dateigröße und Gesamtumfang entpacken
- `/config` als Standardwurzel
- zusätzliche Pfad-Freigaben für `www`, `custom_components`, `addons` und `parent-of-config`
- kompakter Freigabehinweis in normaler, kleinerer Schrift; jeder freigegebene Pfad ist zur besseren Unterscheidung farblich markiert
- Add-on-Verzeichnis nur nach Admin- oder Add-on-Freigabe
- kein freier Root-Zugriff standardmäßig

Die Editor-Bibliothek wird lokal mit dem Plugin ausgeliefert. Dadurch braucht File Studio für die Codeansicht kein CDN und bleibt auch im Home-Assistant-Add-on-Betrieb nachvollziehbar versioniert.

## Sicherheitsmodell

::: info Versionskonsistenz ab 0.1.52
Katalog, Manifest, Paket und eingebettetes Manifest nennen einheitlich **0.1.52**.
Der Paketgenerator synchronisiert nun auch den Katalog; eine lesende CI-Prüfung
erkennt veraltete Artefakte vor der Veröffentlichung. Die frühere Abweichung
Katalog 0.1.50 / Paket 0.1.51 ist behoben. Oberfläche und Datenformate bleiben
unverändert. Update, Paket-Wiederherstellung, erneutes Update und Neustart sind
isoliert mit erhaltenen Testeinstellungen, Dateien, Projekt, anderem Plugin,
Papierkorb und Historie geprüft. Pi 5 und Proxmox wurden dabei nicht verändert;
ein nativer Test von 0.1.52 ist damit nicht behauptet.
:::

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

Nach jedem sichtbaren ATLAS-Update wird die Home-Assistant-App/Add-on-Version angehoben. Home Assistant vergleicht die installierte Version (`old`) mit der Repository-Version (`target`). Für diesen dokumentierten Stand lautet die App-Version `0.1.312`. Wenn weiter eine alte Zielversion erscheint, im App/Add-on-Store die Repository-Informationen neu laden und anschließend ATLAS aktualisieren oder neu starten. Die unabhängig veröffentlichte HACS-Integration bleibt bei `0.1.306`.

Plugin und ATLAS-App haben getrennte Versionen. Dokumentationsänderungen
verändern keine Home-Assistant-Dateien.

## Nächste Ausbaustufen

- Home-Assistant-YAML-Hilfen weiter ausbauen, zum Beispiel mit echter Schema-/Service-Prüfung gegen eine verbundene Home-Assistant-Instanz
- optionale RAR-Unterstützung einschließlich RAR5, falls ein frei nutzbares
  Backend verfügbar ist
- Speichern von Icon-SVGs unter `/config/www/custom_local_icons/`, wenn die passende Home-Assistant-Integration genutzt wird
- Umschaltung zwischen `/config` und dem Automation-Export-Ordner anzeigen, wenn
  der ATLAS Automation Exporter / Editor installiert ist
