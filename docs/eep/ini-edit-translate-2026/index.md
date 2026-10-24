---
title: INI Edit Translate 2026
description: Funktionsbeschreibung des Windows-Editors für EEP-Modell-INI-Dateien und Installation.eep mit ChatGPT-Übersetzung.
---

# INI Edit Translate 2026

**Version 2.1.48.0 · Windows 11 · .NET Framework 4.8**

INI Edit Translate 2026 bearbeitet Modellbeschreibungen und Installationsdateien für
EEP. Die Anwendung wird von Uwe Grimm / UGSo Software entwickelt und unter der
MIT-Lizenz veröffentlicht.

[Quellcode und README auf GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Aktuelles Design von Version 2.1.37 mit Lime-Menüleiste, ohne private Inhalte](/eep/ini-edit-translate-2026/editor-v2-1-37-de.png)

## Version 2.1.48: Teilset-Namen wieder übersetzen

Die Namen und Beschreibungen der fünf Teilsets `Install_00` bis `Install_04`
werden wieder übersetzt. Geschützt bleiben ausschließlich die Modellnamen im
Modellbereich. Ausgangstexte bleiben erhalten; Deutsch und Französisch nutzen
weiterhin Englisch als Zwischensprache.

Alle fünf Übersetzungsbuttons und der automatische Import verwenden dieselbe
geprüfte Zuordnung. Der Button des zweiten Teilsets bearbeitet wieder dessen
eigene Felder. Ein Teilset wird erst nach vollständiger Übersetzung übernommen;
bei Fehler oder Abbruch bleiben seine Namen und Beschreibungen erhalten.

91 lokale Prüfungen bestanden. Ein eigener Installations-Test mit dem Namen
„Detailmodell Großdiesellokomotive V140 001 DRG“ wurde tatsächlich über MyMemory
übersetzt, gespeichert und erneut eingelesen; Modellnamen und ein zusätzliches
INI-Feld blieben erhalten. Die Datei auf dem entfernten Spielerechner wurde dabei
nicht verändert.

## Download

[Windows-ZIP v2.1.48 herunterladen](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/download/v2.1.48/INI-Edit-Translate-2026-v2.1.48-windows.zip) · [GitHub-Release und SHA-256](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/tag/v2.1.48)

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

## Übersetzungsanbieter

Unter **Optionen → Übersetzungseinstellungen** stehen OpenAI-API, ChatGPT-Abo
und **MyMemory** zur Wahl. MyMemory benötigt Internet, aber keinen Schlüssel und kein
Konto. Eine optionale E-Mail-Adresse wird mit jeder Anfrage an MyMemory gesendet:
laut Anbieter 5.000 Zeichen täglich anonym, bis zu 50.000 mit gültiger E-Mail.
Jede Zielsprache zählt separat; längere Texte werden in Abschnitte mit höchstens
500 UTF-8-Bytes zerlegt. Ein flüchtiger Cache vermeidet Wiederholungen innerhalb einer Aktion.

Deutsch ist die Voreinstellung. Die ausgewählte Oberfläche bestimmt die anfängliche
Ausgangssprache; die Quellwahl für Achsen/Signalfunktionen bleibt bedienbar.
Deutsch und Französisch werden zuerst nach Englisch übersetzt; weitere Zielsprachen
entstehen aus diesem englischen Zwischenstand. Die gewählte Ausgangssprache bleibt erhalten.
Das gilt für alle Anbieter. Modellnamen werden weiterhin nicht übersetzt.

MyMemory kann übermittelte Texte langfristig speichern. Die App ruft ausschließlich
die Übersetzungsabfrage auf und veröffentlicht keine zusätzlichen Wörterbucheinträge.
Es gibt keinen automatischen Anbieterwechsel. Bereits gespeicherte API-Schlüssel,
ChatGPT-Verbindungen, Modelle und Wörterbücher bleiben erhalten.
Polnische Sonderzeichen werden beim INI-Speichern über Unicode erhalten; wenn nötig
wird die gesicherte Ausgabedatei in UTF-16 mit BOM gespeichert. Die reale EEP-Verarbeitung
einer solchen Datei wurde hier nicht geprüft.

90 lokale Prüfungen sowie Einlesen, echte MyMemory-Übersetzung und Speichern einer
Kopie der bereitgestellten Beispiel-INI wurden geprüft. Die Originaldatei bleibt unverändert.
Maschinelle Fachübersetzungen vor Verwendung prüfen.

[MyMemory API](https://mymemory.translated.net/doc/spec.php) ·
[Kontingente](https://mymemory.translated.net/doc/usagelimits.php) ·
[Datennutzung](https://mymemory.translated.net/terms-and-conditions)

## Einrichtung und Bedienung

1. Die Windows-ZIP über den Downloadlink herunterladen und vollständig entpacken.
2. `INI Edit Translate 2026.exe` aus dem entpackten Ordner starten. DLLs und Sprachordner
   müssen bei der Anwendung bleiben.
3. Unter **Über → Einstellungen → Übersetzungseinstellungen** MyMemory, OpenAI-API oder ChatGPT-Abo wählen. Für MyMemory ist keine Anmeldung nötig; die E-Mail-Adresse ist optional.
4. Eine gesicherte eigene Datei zunächst im Modus **Nur einlesen** öffnen.
5. Für die Übersetzung **Einlesen und übersetzen** oder eine Übersetzungsschaltfläche
   verwenden. Bei Bewegungsachsen und Signalfunktionen die Ausgangssprache auswählen.
6. Vorschau und Modelltexte prüfen und anschließend ausdrücklich speichern.

Der Info-Dialog wählt die geprüfte Hilfe `Info.de.rtf`, `Info.en.rtf` oder `Info.fr.rtf` passend zur Oberflächensprache. Die historische `Info.rtf` bleibt unverändert als Original erhalten. Die aktuellen Hilfetexte beschreiben OpenAI und die wiederhergestellte Nachschlagehilfe.

## GitHub-Updates

Unter **Über → Nach Updates suchen** wird das neueste öffentliche GitHub-Release
abgefragt. Es gibt keine automatische Prüfung beim Programmstart. Nur eine neuere
stabile Version wird angeboten; Versionsnummer und Release-Notizen werden angezeigt.

**Herunterladen und installieren** lädt die Windows-ZIP samt SHA-256-Prüfsumme.
Download und Paketprüfung sind abbrechbar und erfolgen vor dem Schließen der Anwendung.
Vor der Installation müssen offene Dateien gespeichert und Info_trans geschlossen sein.
Die Installation startet erst nach Bestätigung. Ein separates Hilfsprogramm wartet auf
das Ende des Editors, sichert die bisherigen Dateien und installiert das Paket.

Einstellungen und der verschlüsselte OpenAI-Schlüssel bleiben erhalten. Vorhandene
IET2.FDB-, CSV-, DAT- und Konfigurationsdateien der Nachschlagehilfe sowie die ursprüngliche
Info.rtf werden gesichert und nicht ersetzt. Eigene Modelldateien bleiben unangetastet.
Bei einem Installationsfehler wird die Wiederherstellung der bereits ersetzten Dateien
versucht; ein Bericht nennt das Ergebnis. Sicherungen und Berichte liegen unter
`%LOCALAPPDATA%/UGSo/IET2026/updates/<Kennung>/`.

Der Updater benötigt keine Serverzugangsdaten. Prüfsummen dienen der Integritätsprüfung;
es ist keine zusätzliche digitale Paketsignatur implementiert.
36 isolierte Updateprüfungen decken Download, Abbruch, Paketpfade, Datenerhalt,
gesperrte Dateien und Rücknahme nach einem teilweisen Schreibfehler ab.

### Updater-Korrektur 2.1.48

Die Prozessübergabe verwendet jetzt einen stabilen Windows-Prozesshandle statt
Modulzugriffen auf den bereits schließenden Editor. Vier zusätzliche Prüfungen
decken x86/x64, bereits beendete Prozesse, falsche Identität und Zeitüberschreitungen ab.
Falls der alte 2.1.37-Helfer vor der Installation scheitert, das vollständige
2.1.48-ZIP zuerst in einen neuen Ordner entpacken. Eigene Daten vorher sichern
und vorhandene Datenbanken sowie Wörterbücher nicht durch Paketdateien ersetzen.

Der vollständige Ablauf von der veröffentlichten 2.1.37 zur 2.1.48 wurde an
einer gesicherten Testkopie erfolgreich geprüft: GitHub-Download, Installation
und automatischer Neustart. Alle 32 bisherigen Einstellungswerte, 17 geprüfte
Daten-/Modelldateien und 18 vorhandene Benutzerkonfigurationen blieben erhalten.
Ein synthetischer DPAPI-Testschlüssel blieb unverändert und entschlüsselbar;
anschließend wurde der ursprüngliche Zustand ohne Schlüssel wiederhergestellt.
Es erfolgte kein OpenAI-Aufruf. Der Neustart wurde über Prozess-ID, Dateiversionen,
Hashes und Konfiguration bestätigt; die Windows-Fenstersteuerung meldete danach
einen Erfassungsfehler. Der erneute lesende GitHub-Dialogtest erkannte 2.1.48 korrekt.

## Zweites Programm: Info_trans

Das Paket enthält auch `help/Info_trans.exe`. **Nachschlagehilfe** im Haupteditor
öffnet dieses separate Programm in der gewählten Sprache. Die echte `IET2.FDB`
und die zugehörige native Firebird-2.5.8-Laufzeit wurden aus dem Archiv von 2019
übernommen. Eine separate Firebird-Serverinstallation ist nicht nötig.

Die Datenbank enthält 5 Immobilien- und 2 Gütereinträge sowie 2 Updateeinträge.
Die Tabellen für Signale, Rollmaterial, Gleisobjekte und Landschaft sind im
Original leer. Zusätzlich sind 236 Iconeinträge, 369 technische Begriffe und
2.428 bereinigte Einträge im **Wörterbuch DE/EN/FR** enthalten. Englisch ist die
Referenz; bestätigte deutsche Korrekturen und französische Übersetzungen sind eingearbeitet.
Abgetrennte Zeilen wurden zusammengeführt und vermischte Begriffe getrennt.
Amerikanische und britische Fachbegriffe bleiben mit ihren Kennzeichnungen erhalten.
Alle Rückfragen zur Wörterbuchprüfung sind geklärt. Die ursprüngliche DE/EN-Datei
und die Quelldatenbank bleiben unverändert im vollständigen Paket erhalten.

![Info_trans 2.1.37 mit Lime-Registerkarten und geladener Originaldatenbank](/eep/ini-edit-translate-2026/info-trans-v2-1-37-de.png)

![Dreisprachiges Wörterbuch in Info_trans mit gut lesbaren DE-, EN- und FR-Spalten](/eep/ini-edit-translate-2026/dictionary-v2-1-37-de.png)

`Info_trans` wird passend zu den nativen DLLs für x86 gebaut. Die verwaltete DLL
FirebirdSql.Data.FirebirdClient 7.5.0.0 wurde mit der echten Firebird-2.5.8-Datenbank
geprüft. Tests lesen nur getrennte Datenbankkopien und vergleichen alle sieben
Tabellen mit der Anzeige in DE/EN/FR. Das Paket enthält die unveränderte Quelldatenbank.

Fehlende oder nicht ladbare Bestandteile werden angezeigt. SQL-Import bleibt dann
gesperrt; vor einem verfügbaren manuellen SQL-Import wird die Datenbank lokal gesichert.
Die automatische Programmaktualisierung bleibt deaktiviert.

## Daten und Datenschutz

Die neue Fassung importiert keine alten Registrierungen oder privaten Datenbanken.
Einstellungen werden getrennt pro Windows-Benutzer gespeichert. OpenAI-Konfiguration
und Dateisicherungen liegen unter `%LOCALAPPDATA%/UGSo/IET2026/`.

Der Schlüssel wird für das Windows-Konto mit DPAPI verschlüsselt. Nur ausdrücklich
übersetzte Texte werden an OpenAI gesendet; die API-Anfrage setzt `store: false`.
Internet und separate API-Abrechnung sind erforderlich. Ein ChatGPT-Abonnement
ersetzt die API-Abrechnung nicht.

## Updatefunktion und Prüfstand

**GitHub-Updates werden manuell gestartet und vor der Installation bestätigt.** Der alte Updateserver wird nicht verwendet.
Google, LEO, Linguee und DeepL werden nicht mehr angeboten.

41 lokale Prüfungen mit simulierten API-Antworten sowie Debug- und Release-Builds
prüfen Fehlerfälle, Abbruch, Wiederherstellung, Tabellenexport und die gerenderten
Oberflächen in DE/EN/FR. Die Tests senden keine Texte an OpenAI. Ein echter API-Aufruf
und die Qualität erzeugter Modellübersetzungen sind mit dem eigenen Zugang noch zu prüfen.
Nicht jedes denkbare INI-Schema wird unterstützt; die inhaltliche Prüfung bleibt notwendig.

Das vollständige lokale Release 2.1.37 wurde vor der Veröffentlichung vom Nutzer
kontrolliert und als funktionsfähig bestätigt. Das ZIP enthält beide Programme,
die native Firebird-Laufzeit, die Originaldatenbank und das korrigierte Wörterbuch.
ZIP-Integrität und SHA-256 wurden geprüft, alle sieben Datenbanktabellen wurden
auf getrennten Kopien mit der Anzeige in DE/EN/FR verglichen. Die Bilder zeigen
das aktuelle Design mit neutralen Daten und ohne private Einstellungen.
