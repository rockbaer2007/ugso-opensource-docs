---
title: ATLAS Icon Studio
description: Iconsets mit ATLAS Icon Studio verwalten, importieren, löschen und in Home Assistant speichern.
---
# ATLAS Icon Studio

ATLAS Icon Studio ist ein separat installiertes Plugin zum Erstellen und Verwalten von Home-Assistant-Iconsets mit dem Präfix `atlas:`. Version 0.1.15 unterstützt große Sammlungen ohne feste Icon-Anzahlgrenze; die Liste rendert jeweils nur 24 Einträge.

## Icons verwalten

Aktueller Plugin-Stand: **0.1.17**. Diese Version korrigiert den fehlenden
Validator-Import beim Anlegen von Zeichnungstext. Version 0.1.16 behob zuvor
einen Startfehler beim Exportformat-Selektor. Speicherformate bleiben unverändert.

Die Sammlung liegt im browserlokalen IndexedDB-Speicher. Ältere lokale Daten
werden übernommen; vor einem Browser-/Adresswechsel die Sammlung als JSON sichern.

## Zeichnen und Bildvorschau

Ein separater Zeichenbereich unterstützt farbige SVGs mit Formen, Freihand und
Text, Ebenenreihenfolge sowie bis zu zehn Rückgängig-/Wiederholen-Schritte.
„Speichern unter“ exportiert SVG, PNG oder WebP, optional mit transparentem
Hintergrund. Rasterbilder lassen sich anzeigen und optional vektorisieren;
sie werden nicht direkt zu `atlas:`-Icons. Das HA-Iconset benötigt SVG-Pfade.
File Studio kann unterstützte Bilder auf demselben ATLAS-Server direkt an Icon
Studio übergeben. Downloads werden nicht automatisch nach HA kopiert.

## Sammlung bearbeiten

Wähle ein Icon in der Sammlung aus und nutze **Icon löschen**, um es zu entfernen. Danach wird automatisch das nächste löschbare Icon ausgewählt. So lassen sich mehrere Icons hintereinander löschen, ohne nach jedem Schritt erneut ein Icon auswählen zu müssen. Das Referenz-Icon `atlas:home` ist geschützt und kann nicht gelöscht werden. Mindestens ein Icon bleibt in der Sammlung.

Suche, Tastaturnavigation und Export beziehen sich auf die gesamte Sammlung, auch wenn gerade nur ein kleiner Ausschnitt sichtbar ist. Sammlungen können als JSON gesichert und wieder eingelesen werden; Namenskonflikte lassen sich ersetzen, überspringen oder automatisch umbenennen.

## Home Assistant

Iconsets können lokal als `atlas-iconset.js` exportiert oder direkt über File Studio aus `/config/www/atlas-iconset.js` eingelesen werden. Beim Speichern kann die vorhandene Datei ersetzt werden; File Studio legt dabei eine Sicherung an. Alternativ erstellt Icon Studio eine neue nummerierte Datei und zeigt den `/local/...`-Ressourcenpfad an, der in Home Assistant registriert werden muss. Für direkten Zugriff muss `/config/www` in File Studio freigegeben sein.

Weitere Details zu Installation, Formaten und Dateipfaden stehen in der [Plugin-README](https://github.com/rockbaer2007/atlas-icon-studio-plugin#readme).

## Sichere Plugin-Wiederherstellung

Vorher die Sammlung als JSON sichern, das Iconset exportieren und Zeichnungen
separat als SVG speichern. In **Administration → Plugin-Manager → Icon Studio →
Wiederherstellen** eine Sicherung auswählen, Version und Kompatibilität prüfen
und **Sichern und übernehmen** ausführen. Die aktuelle Plugin-Version wird dabei
ebenfalls gesichert. **Abbrechen** lässt die Installation unverändert.

::: info Isoliert geprüft am 16.10.2026
Mit ATLAS 0.1.312 wurden der Wechsel **0.1.16 → 0.1.17** und die Wiederherstellung
**0.1.17 → 0.1.16 → gesicherte 0.1.17** einschließlich App-Neustart geprüft.
Alle zwölf Paketdateien waren versionsgenau. Die Sammlung mit 131 Icons und
eine Zeichnung mit zwei Textobjekten blieben bei gleicher Browseradresse und
gleichem Profil erhalten. JSON-, Iconset-JavaScript- und SVG-Exporte waren
danach bytegleich. Neue Texteingabe, Duplizieren und Rückgängig funktionierten.
Testdateien, bestehendes Iconset, Projekt, anderes Plugin, Papierkorb und Historie
blieben erhalten. Vorher wurden Repositories, Serverdaten und Browser-Exporte
gesichert. **Pi 5 und Proxmox wurden weder abgefragt noch verändert.**
Datenformat-Migrationen sind damit nicht geprüft.
:::

::: info Auf Pi 5 und Proxmox geprüft am 16.10.2026
Nach neuen lokalen HA-Sicherungen, PC-Dateikopien und Browser-Exporten wurde
**0.1.16 → 0.1.17 → ursprüngliche 0.1.16 → 0.1.17** über die Administration
geprüft. Alle zwölf Paketdateien stimmen; Einstellungen, vorhandene Dateien,
sechs aktive Plugins, Projekt, Papierkorb und Historie bleiben erhalten.
ATLAS 0.1.312 und HA 2026.10.1 benötigten keinen Neustart. Beide Systeme enden
mit Icon Studio 0.1.17. Bei einer abgewiesenen veralteten Update-Vorschau nach
Wiederherstellung die Administration neu laden und das Update erneut wählen.
Direkter Zugang und HA-Ingress wurden je Host geprüft: jeweils drei Referenzicons
und ein leerer Zeichnungsentwurf. Sammlungs-JSON bleibt bytegleich, der Entwurf
nach Neuladen unverändert. Text anlegen und rückgängig machen funktioniert.
Größere Sammlungen und gefüllte Zeichnungen wurden im isolierten Test geprüft.
:::

Die Paket-Wiederherstellung stellt keine gelöschten Browserdaten wieder her.
IndexedDB und lokaler Zeichnungsentwurf gehören zum Browserprofil und zum
Ursprung aus Protokoll, Host und Port. Eine HA-/Serversicherung enthält diese
Browserdaten nicht. Sammlungs-JSON und Iconset-JavaScript enthalten keine farbige
Zeichnung; eine exportierte SVG ist kein vollständiges Entwurfs-/Undo-Backup.
Formen und Dateiname des aktuellen Entwurfs bleiben lokal erhalten;
Werkzeugauswahl, Suche und Rückgängig-/Wiederholen-Verlauf sind sitzungsbezogen.
