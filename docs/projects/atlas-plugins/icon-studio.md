---
title: ATLAS Icon Studio
description: Iconsets mit ATLAS Icon Studio verwalten, importieren, löschen und in Home Assistant speichern.
---
# ATLAS Icon Studio

ATLAS Icon Studio ist ein separat installiertes Plugin zum Erstellen und Verwalten von Home-Assistant-Iconsets mit dem Präfix `atlas:`. Version 0.1.15 unterstützt große Sammlungen ohne feste Icon-Anzahlgrenze; die Liste rendert jeweils nur 24 Einträge.

## Icons verwalten

Wähle ein Icon in der Sammlung aus und nutze **Icon löschen**, um es zu entfernen. Danach wird automatisch das nächste löschbare Icon ausgewählt. So lassen sich mehrere Icons hintereinander löschen, ohne nach jedem Schritt erneut ein Icon auswählen zu müssen. Das Referenz-Icon `atlas:home` ist geschützt und kann nicht gelöscht werden. Mindestens ein Icon bleibt in der Sammlung.

Suche, Tastaturnavigation und Export beziehen sich auf die gesamte Sammlung, auch wenn gerade nur ein kleiner Ausschnitt sichtbar ist. Sammlungen können als JSON gesichert und wieder eingelesen werden; Namenskonflikte lassen sich ersetzen, überspringen oder automatisch umbenennen.

## Home Assistant

Iconsets können lokal als `atlas-iconset.js` exportiert oder direkt über File Studio aus `/config/www/atlas-iconset.js` eingelesen werden. Beim Speichern kann die vorhandene Datei ersetzt werden; File Studio legt dabei eine Sicherung an. Alternativ erstellt Icon Studio eine neue nummerierte Datei und zeigt den `/local/...`-Ressourcenpfad an, der in Home Assistant registriert werden muss. Für direkten Zugriff muss `/config/www` in File Studio freigegeben sein.

Weitere Details zu Installation, Formaten und Dateipfaden stehen in der [Plugin-README](https://github.com/rockbaer2007/atlas-icon-studio-plugin#readme).
