---
title: INI Edit Translate 2026
description: Funktionsbeschreibung des Windows-Editors für EEP-Modell-INI-Dateien und Installation.eep mit ChatGPT-Übersetzung.
---

# INI Edit Translate 2026

**Version 2.1.35.0 · Windows 11 · .NET Framework 4.8**

INI Edit Translate 2026 bearbeitet Modellbeschreibungen und Installationsdateien für
EEP. Die Anwendung wird von Uwe Grimm / UGSo Software entwickelt und unter der
MIT-Lizenz veröffentlicht.

[Quellcode und README auf GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Geprüfte deutsche Programmoberfläche ohne private Inhalte](/eep/ini-edit-translate-2026/editor-de.png)

## Download

[Windows-ZIP v2.1.35 herunterladen](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/download/v2.1.35/INI-Edit-Translate-2026-v2.1.35-windows.zip) · [GitHub-Release und SHA-256](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/tag/v2.1.35)

ZIP vollständig entpacken und `INI Edit Translate 2026.exe` starten. Windows 11 und
.NET Framework 4.8 werden benötigt. DLLs und Sprachordner zusammen lassen.
Visual Studio ist nur zum Bauen der Quellen nötig. Kein Installer erforderlich.

## Funktionen

| Bereich | Möglichkeiten |
| --- | --- |
| Modelltexte | Namen und Beschreibungen in EN/DE/FR/PL bearbeiten |
| Modellmetadaten | PDF-Verweise, Generation, Einsatzzeitraum, Land und Symbol bearbeiten |
| Bewegungsachsen und Signalfunktionen | Sprachabhängige Einträge anzeigen, bearbeiten und übersetzen |
| Installation.eep | Namen und Beschreibungen der unterstützten Installationsabschnitte bearbeiten |
| Vorschau | Originaldatei und erzeugte Dateivorschau vergleichen |
| Tabellenexport | Vollständige Tabellen als tabulatorgetrennte UTF-8-Dateien mit BOM exportieren |
| Sicherungen | Vor dem Überschreiben vorhandener INI-Dateien eine Kopie mit Originaldateinamen anlegen |

## ChatGPT-Übersetzung

Die Anwendung verwendet ausschließlich die OpenAI Responses API. Pro Originaltext
werden die drei anderen Zielsprachen gemeinsam angefordert. Es gibt keine
Zwischenübersetzung über Englisch. Wiederholte Texte innerhalb derselben Aktion
verwenden einen flüchtigen Cache.

Ein Fortschrittsdialog bietet **Abbrechen**. Das Anfragezeitlimit beträgt 60 Sekunden;
maximal 24.000 Zeichen werden je Text akzeptiert. Unvollständige Antworten, fehlende
Zielsprachen und veränderte Platzhalter wie `{0}`, `%s` oder `[e]` werden abgelehnt.
Bei einem Fehler bleiben die vor der Übersetzung vorhandenen Texte und Tabellen erhalten.

Die Oberfläche wurde in DE/EN/FR auf beschädigte Zeichen, falsche Sprachzuordnungen
und Sprachmischungen geprüft. Technische INI-Schlüssel wie `Name_GER` bleiben erhalten.

## Einrichtung und Bedienung

1. Die Windows-ZIP über den Downloadlink herunterladen und vollständig entpacken.
2. `INI Edit Translate 2026.exe` aus dem entpackten Ordner starten. DLLs und Sprachordner
   müssen bei der Anwendung bleiben.
3. Unter **Über → Einstellungen → OpenAI-Übersetzung** den eigenen API-Schlüssel
   und das Modell eintragen. Voreinstellung ist `gpt-4.1-mini`.
4. Eine gesicherte eigene Datei zunächst im Modus **Nur einlesen** öffnen.
5. Für die Übersetzung **Einlesen und übersetzen** oder eine Übersetzungsschaltfläche
   verwenden. Bei Bewegungsachsen und Signalfunktionen die Ausgangssprache auswählen.
6. Vorschau und Modelltexte prüfen und anschließend ausdrücklich speichern.

## Daten und Datenschutz

Die neue Fassung importiert keine alten Registrierungen oder privaten Datenbanken.
Einstellungen werden getrennt pro Windows-Benutzer gespeichert. OpenAI-Konfiguration
und Dateisicherungen liegen unter `%LOCALAPPDATA%/UGSo/IET2026/`.

Der Schlüssel wird für das Windows-Konto mit DPAPI verschlüsselt. Nur ausdrücklich
übersetzte Texte werden an OpenAI gesendet; die API-Anfrage setzt `store: false`.
Internet und separate API-Abrechnung sind erforderlich. Ein ChatGPT-Abonnement
ersetzt die API-Abrechnung nicht.

## Updatefunktion und Prüfstand

**Die Updatefunktion ist vorerst vollständig deaktiviert.** Weder eine automatische
Verbindung zum bisherigen Updateserver noch ein Update-Menüpunkt ist enthalten.
Google, LEO, Linguee und DeepL werden nicht mehr angeboten.

30 lokale Prüfungen mit simulierten API-Antworten sowie Debug- und Release-Builds
prüfen Fehlerfälle, Abbruch, Wiederherstellung, Tabellenexport und die gerenderten
Oberflächen in DE/EN/FR. Die Tests senden keine Texte an OpenAI. Ein echter API-Aufruf
und die Qualität erzeugter Modellübersetzungen sind mit dem eigenen Zugang noch zu prüfen.
Nicht jedes denkbare INI-Schema wird unterstützt; die inhaltliche Prüfung bleibt notwendig.
