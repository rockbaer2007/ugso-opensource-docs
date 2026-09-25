---
title: Bauen, prüfen und veröffentlichen
description: ATLAS-Pluginpakete und Repository-Kataloge vorbereiten und prüfen.
---
# Bauen, prüfen und veröffentlichen

Die [Plugin-Vorlage](../plugin-template) automatisiert die wiederholbaren Schritte für ein eigenes GitHub-Repository.

## Paket und Katalog bauen

```sh
npm run build
npm run check
```

Der Build erzeugt aus dem Manifest das installierbare Paket und synchronisiert den passenden Plugin-Eintrag im `repository.json`. Die Prüfung kontrolliert unter anderem IDs, Paketpfad und die Metadaten im erzeugten Paket. Ein GitHub-Actions-Workflow führt Build und Prüfung bei Pushes und Pull Requests aus.

## Veröffentlichungsschritte

1. Erhöhe `version` im Manifest bei jeder funktionalen oder sichtbaren Veröffentlichung.
2. Führe `npm run build` und `npm run check` aus.
3. Prüfe, ob Manifest, Katalog und erzeugtes Paket dieselbe ID und Version enthalten.
4. Kontrolliere Paketdateien, Asset-Pfade, externe Anfragen und deklarierte Fähigkeiten.
5. Aktiviere GitHub Pages für `main`, wenn dein Katalog über GitHub Pages erreichbar sein soll. Die Rohdatei ist dann unter `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json` verfügbar.
6. Füge die Katalog-URL in ATLAS Administration hinzu und teste Vorschau und Paketinstallation.

Halte die Plugin-ID nach der ersten Veröffentlichung stabil. Größere Binärdateien gehören nicht in das textbasierte Paketformat; hoste sie separat und referenziere sie über eine URL.

## Installationsstatus

Der generische ATLAS-Repository-Installer speichert heruntergeladene Paketdateien derzeit lokal. Er führt den enthaltenen beliebigen Plugin-Code noch nicht automatisch aus. Ein erfolgreicher Paketbuild bestätigt deshalb die Paketstruktur, aber keine ausführbare Installation oder Sicherheitsprüfung des Plugin-Codes.
