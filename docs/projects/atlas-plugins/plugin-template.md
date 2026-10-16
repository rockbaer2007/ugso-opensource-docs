---
title: ATLAS Plugin-Vorlage
description: Mit der offiziellen GitHub-Vorlage ein eigenes ATLAS-Plugin erstellen.
---
# ATLAS Plugin-Vorlage

Die [offizielle ATLAS Plugin-Vorlage auf GitHub](https://github.com/rockbaer2007/atlas-plugin-template) ist ein startfertiges Repository für ein einzelnes ATLAS-Plugin. GitHub erstellt daraus mit **Use this template** ein eigenes Repository.

## Plugin-Generator in der Administration

Die ATLAS-Administration bietet einen Plugin-Generator für ID, Name, Beschreibung, Version, Einstiegspfad und Fähigkeiten. Wähle ein MDI-Icon aus dem lokal gebündelten Katalog oder ein eigenes PNG bis 512 KiB; das Paket enthält die Grafik samt nötigen Lizenzhinweisen. Farben und Transparenz eigener PNGs bleiben erhalten. Erzeugt werden ein bearbeitbares HTML/CSS/JavaScript-Grundgerüst, Paket, `repository.json` und eine lokalisierte `README.md`, die auch einzeln heruntergeladen werden kann. Prüfe Inhalte und Pfade vor der Veröffentlichung. Der Generator erstellt kein GitHub-Repository und veröffentlicht nichts automatisch. Unterstützte manuell importierte Pakete werden nach der Kompatibilitätsprüfung auf dem App-Server installiert und unter `/plugin-assets/<slug>/` bereitgestellt. Die Oberfläche läuft erst beim Öffnen im Browser; Runtime-Hooks werden nicht automatisch registriert. Halte `entry` und Paketpfade konsistent.

Plugins mit eigener Sprachauswahl übernehmen die gespeicherte ATLAS-Sprachwahl beim Öffnen. Ein `language`-Parameter in der Plugin-URL hat Vorrang. Unterstützt ein Plugin die gewählte Sprache nicht, verwendet es seine konfigurierte Rückfallsprache.

## Schnellstart

1. Öffne das Vorlagen-Repository und wähle **Use this template** → **Create a new repository**.
2. Klone das neue Repository und bearbeite `plugins/atlas-plugin/atlas-plugin.json`. Vergib eine eindeutige Plugin-ID und trage Name, Version, Beschreibung sowie nur die tatsächlich benötigten Fähigkeiten ein.
3. Ersetze die Beispielanwendung unter `plugins/atlas-plugin/` sowie `icon.svg`, `logo.svg` und `preview.svg` durch deine Plugin-Inhalte.
4. Baue und prüfe das Paket lokal:

   ```sh
   npm run build
   npm run check
   ```

5. Passe `repository.json` und `install.html` an dein Repository an. Der Paketgenerator übernimmt ID, Name, Version, Beschreibungen und Asset-Pfade aus dem Manifest und hält den Katalog synchron.
6. Der Katalog ist nach dem Push ohne GitHub Pages unter `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json` erreichbar. Aktiviere GitHub Pages zusätzlich für die öffentliche `install.html`, falls gewünscht.
7. Füge die Katalog-URL in der ATLAS-Administration hinzu und installiere das Plugin zum Testen.

## Was enthalten ist

Die Vorlage enthält ein kleines Beispielplugin, Manifest, Repository-Katalog, Installationsseite, Paketgenerator, Validierung und einen GitHub-Actions-Workflow. Der Workflow führt Build und Prüfung bei Pushes und Pull Requests aus.

Erhöhe bei jeder Veröffentlichung die Plugin-Version und führe anschließend `npm run build` aus. Die Plugin-ID sollte nach der Veröffentlichung stabil bleiben. Prüfe vor dem Veröffentlichen insbesondere Berechtigungen und deklarierte Fähigkeiten.

## Aktueller Installationsumfang

Der App-Server installiert geprüfte Repository- und Importpakete im persistenten Plugin-Verzeichnis und stellt statische Webdateien unter `/plugin-assets/<slug>/` bereit. Beim Öffnen läuft deren JavaScript im Browser; beliebige Node-Module oder Runtime-Hooks werden nicht automatisch registriert. Die Installation ist keine Sandbox: Prüfe Paket und Browsercode vor dem Öffnen. Paketdateien enthalten Text oder ausdrücklich gekennzeichnete Base64-Assets; maximal 300 Dateien und 20 MB pro Paket. Größere Binärdateien separat bereitstellen.

Weitere Details zum Katalog und Paketformat stehen unter [Repository-Format](./repository-format). Die Vorlage: [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
