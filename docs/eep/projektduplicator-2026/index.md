---
title: Projektduplicator 2026
description: EEP-Modellprojekte duplizieren und bearbeiten, mit mehrsprachiger Oberfläche, ZIP-Snapshots und manuellen GitHub-Updates.
---

# Projektduplicator 2026

Projektduplicator 2026 ist das eigenständige Windows-Werkzeug von UGSo Software zum Duplizieren und Bearbeiten von EEP-Modellprojekten. Die Oberfläche unterstützt Deutsch, Englisch, Französisch und Niederländisch.

## Download und Start

- [Windows-ZIP 4.6.6.59 herunterladen](https://github.com/rockbaer2007/projektduplicator-2026/releases/download/v4.6.6.59/Projektduplicator-2026-v4.6.6.59-windows.zip)
- [Release, SHA-256-Prüfsumme und Quellcode](https://github.com/rockbaer2007/projektduplicator-2026/releases/tag/v4.6.6.59)
- [GitHub-Repository](https://github.com/rockbaer2007/projektduplicator-2026)

Das ZIP vollständig in einen beschreibbaren Ordner entpacken und `Projektduplicator_2017.exe` starten. Der technische Dateiname bleibt für die Kompatibilität vorhandener Einstellungen erhalten. Benötigt wird Windows mit .NET Framework 4.8; die Projektmappe lässt sich in Visual Studio 2026 bauen.

## Funktionen

- EEP-Modellprojekte duplizieren und Modellinformationen bearbeiten.
- Modellnamen und Beschreibungen mehrsprachig bearbeiten und über Google Translate übersetzen.
- Sprache der Oberfläche während der Nutzung wechseln.
- ZIP-Snapshots der Projekte im eingestellten Sicherungsordner erstellen.
- Über die vorhandenen Update-Schaltflächen manuell neue GitHub-Releases prüfen, herunterladen und nach Bestätigung installieren.

Die Google-Webübersetzung benötigt Internet und hängt vom Antwortformat der Google-Webseite ab. Sie verwendet keine offizielle Google-API. Bei einem Übersetzungsfehler bleiben die bisherigen Texte erhalten.

## Einstellungen und Updates

Vor Änderungen eigene Projekte sichern. Vor einem Update Editoren schließen und Änderungen an Pfad- und Spline-Listen speichern. Es gibt keine automatische Updateprüfung beim Start.

Der Updater prüft das Paket und seine SHA-256-Prüfsumme, sichert vorhandene Programmdateien und Einstellungen und startet nach erfolgreicher Installation neu. Vorhandene Projektdateien, Pfadlisten und eigene `info.txt`-Inhalte bleiben erhalten. Fehlt `info.txt`, wird die mitgelieferte Fassung installiert. Eine bestehende ältere `info.txt` wird absichtlich nicht automatisch ersetzt.

## Geprüfter Stand

Version 4.6.6.59 wurde vom Nutzer lokal freigegeben. Der Form1-Designer wurde in Visual Studio geprüft. Die Beschreibung und Danksagungen in `info.txt` sind in DE/EN/FR/NL überarbeitet. 49 lokale Prüfungen decken unter anderem Sprachfassungen, Feldzuordnung, Paketprüfung, Datenerhalt, Abbruch, Rollback und den Prozesswechsel des Updaters ab.

Ein echter Updateablauf vom öffentlichen GitHub-Release mit Installation und Neustart ist noch gesondert zu prüfen. Die bisherigen Tests verwenden simulierte GitHub-Antworten und temporäre Installationen.

## Quellcode und Hinweise

UGSo-Quellcode unter MIT; Abhängigkeiten behalten ihre jeweiligen Lizenzbedingungen und Copyright-Hinweise. Details stehen im Repository unter `LICENSE` und `THIRD-PARTY-NOTICES.md`. EEP und Google Translate sind Produkte ihrer jeweiligen Rechteinhaber.
