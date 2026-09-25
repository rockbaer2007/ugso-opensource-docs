---
title: ATLAS Plugin-Vorlage
description: Mit der offiziellen GitHub-Vorlage ein eigenes ATLAS-Plugin erstellen.
---
# ATLAS Plugin-Vorlage

Die [offizielle ATLAS Plugin-Vorlage auf GitHub](https://github.com/rockbaer2007/atlas-plugin-template) ist ein startfertiges Repository für ein einzelnes ATLAS-Plugin. GitHub erstellt daraus mit **Use this template** ein eigenes Repository.

## Plugin-Generator in der Administration

Die ATLAS-Administration bietet einen Plugin-Generator. Neben ID, Name, Beschreibung, Version, Einstiegspfad und Fähigkeiten kannst du ein MDI-Icon suchen und per Klick auswählen. Die Suche nutzt eine lokal gebündelte Liste; das gewählte SVG und die zugehörigen Lizenzhinweise werden in das Installationspaket übernommen. Der Generator erstellt außerdem ein bearbeitbares HTML/CSS/JavaScript-Grundgerüst sowie eine `repository.json`-Katalogdatei. Prüfe die erzeugten Inhalte und Pfade und ergänze die Dateien in deinem Repository; der Generator legt kein GitHub-Repository an und veröffentlicht nichts automatisch. Manuell importierte Pakete erscheinen im Plugin Hub. Ihre Dateien werden derzeit jedoch nicht als Plugin-Seite bereitgestellt oder ausgeführt; dafür muss das Plugin über ein Repository beziehungsweise einen lokal bereitgestellten Plugin-Ordner verfügbar sein.

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
6. Aktiviere GitHub Pages für den Branch `main`. Der Katalog ist dann unter `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json` erreichbar.
7. Füge die Katalog-URL in der ATLAS-Administration hinzu und installiere das Plugin zum Testen.

## Was enthalten ist

Die Vorlage enthält ein kleines Beispielplugin, Manifest, Repository-Katalog, Installationsseite, Paketgenerator, Validierung und einen GitHub-Actions-Workflow. Der Workflow führt Build und Prüfung bei Pushes und Pull Requests aus.

Erhöhe bei jeder Veröffentlichung die Plugin-Version und führe anschließend `npm run build` aus. Die Plugin-ID sollte nach der Veröffentlichung stabil bleiben. Prüfe vor dem Veröffentlichen insbesondere Berechtigungen und deklarierte Fähigkeiten.

## Aktueller Installationsumfang

Der generische Repository-Installer speichert Paketdateien derzeit lokal. Er führt beliebigen heruntergeladenen Plugin-Code noch nicht automatisch aus. Das Paketformat speichert Plugin-Dateien als Text; größere Binärdateien sollten separat gehostet und per URL referenziert werden.

Weitere Details zum Katalog und Paketformat stehen unter [Repository-Format](./repository-format). Die Vorlage: [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
