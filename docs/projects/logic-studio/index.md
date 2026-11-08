---
title: Logic Studio
description: Logic Studio 0.1.7 mit typgeprüften Ziehverbindungen und navigierbarer Miniübersicht für Home Assistant.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.7 – öffentliches Testupdate, 8. November 2026.** Neu sind typgeprüfte Maus-Ziehverbindungen und eine Miniübersicht mit Navigation. Logic Studio ist eine eigene HA-App für grafische Funktionspläne, unabhängig von Grafik Visual Studio und Blocks for HA. Die Oberfläche ist derzeit **Deutsch**; diese Anleitung gibt es in **DE/EN/FR**.

::: warning Testversion
Zuerst auf einem Testsystem installieren und vorher ein vollständiges Backup erstellen. Native Detailoptionen werden zunächst als JSON bearbeitet. Die App schreibt keine Automationen oder Skripte in HA zurück und schaltet keine Geräte. Erzeugte Ausgaben immer prüfen und selbst in HA installieren.
:::

[GitHub-Testrelease und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.7) · [Quellcode im Sammel-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## Testinstallation aus GitHub

[![Repository in Home Assistant hinzufügen](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. In **Einstellungen → Apps → App-Store → Repositorys** die folgende Adresse eintragen. Ist „UGSo HA Apps“ schon eingerichtet, nur nach Updates suchen.
2. **UGSo Logic Studio** auswählen und installieren. Falls experimentelle Apps ausgeblendet sind, im HA-Profil den erweiterten Modus aktivieren.
3. Starten und die Benutzeroberfläche öffnen. Unterstützt werden **HA OS/Supervised**, **amd64 und aarch64**. Der erste Container-Build kann einige Minuten dauern. Dies ist kein HACS-/Marketplace-Frontend-Paket.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Vorhandene lokale Testinstallation erhalten:** GitHub- und lokale App haben verschiedene Repository-IDs und getrennte Daten. Den alten Plan über **Projekt** als JSON exportieren und in der GitHub-App über **Öffnen** importieren. Es gibt keine automatische Migration oder Deinstallation. Projekt und Paletteinstellungen der jeweiligen App bleiben unter `/data` gespeichert.

**Bestehende GitHub-App aktualisieren:** Vorher sichern, in der App-Verwaltung nach Updates suchen und **UGSo Logic Studio → Aktualisieren** wählen. Die App bleibt installiert; `/data`, Entity-IDs und bestehende Pläne werden nicht ersetzt. Nicht deinstallieren oder die App-ID wechseln. Auf .193 blieben Originalplan, Favoriten, zuletzt benutzte Bausteine und eingeklappte Bereiche nach dem Update erhalten.

## Zwei Arten von Plänen

| Plan | Zweck und Ausgabe |
| --- | --- |
| Wertplan | Typisierte Ein-/Ausgänge, Logik, Mathematik, Auswahl sowie Speicher, Flanken, Timer und Zähler. 33 implementierte Typen; weitere Referenztypen sind als Vorlagen gekennzeichnet. Ausgabe als HA-Automation, HA-Skript oder JavaScript-Funktion mit Host-Schnittstelle. |
| Nativer HA-Ablauf | Automationen, Skripte und Blueprints importieren und als verschachtelte Bausteine bearbeiten. 53 zusätzliche HA-Typen für Auslöser, Bedingungen, Zweige, Schleifen, Warteaktionen, Variablen und Blueprint-Eingaben. Ausgabe ausschließlich als native HA-YAML. |

Wertpläne können mit Demo-/Momentaufnahmewerten simuliert werden. Persistente Wertbausteine benötigen die dokumentierten HA-Texthelfer bzw. einen JavaScript-Speicher-Host. Native HA-Abläufe werden im Editor weder ausgeführt noch automatisch in JavaScript umgerechnet. Die JavaScript-Ausgabe ist kein ioBroker-Skript.

## Verbindungen ziehen und Miniübersicht

Am farbigen Anschluss die Maustaste gedrückt halten, zum passenden Gegenanschluss ziehen und loslassen. Der Cursor wird zum Kreuz; eine Leitungsvorschau folgt der Maus. Passende Ziele werden grün, unpassende oder belegte Eingänge rot markiert. Auch vom Eingang zurück zum Ausgang ziehen ist möglich. **Esc** oder Loslassen auf freier Fläche bricht ab; **Rückgängig** nimmt eine erstellte Leitung zurück.

**BOOL verbindet nur mit BOOL.** Gleiche Signaltypen passen zueinander; `INT → REAL` ist zusätzlich erlaubt. Explizite `ANY`-Anschlüsse sind universell. Zahlen und Texte werden nicht stillschweigend zu BOOL umgedeutet. Pro Eingang ist genau eine Leitung erlaubt; falsche Typen, gleiche Anschlussseiten, Selbstverbindungen und Rückkopplungen werden abgewiesen. Eine Fehlermeldung erklärt den Grund. Für die Tastatur Ausgang per Tab/Enter auswählen, anschließend Eingang und Enter.

![Auf .193 erfolgreich mit der Maus verbundene BOOL-Anschlüsse](/images/logic-studio/0.1.7-bool-verbunden.png)

![STRING nach BOOL wird mit verständlichem Typfehler abgewiesen](/images/logic-studio/0.1.7-typ-abgewiesen.png)

Rechts unten zeigt die **Übersicht** farbige Bausteinpositionen und den Rahmen des sichtbaren Ausschnitts. Ein Klick verschiebt den Ausschnitt. Mit fokussierter Übersicht navigieren auch Pfeiltasten, **Pos1** und **Ende**. Die Darstellung folgt Scrollen, Zoom und Positionsänderungen. **Referenz: React Flow** öffnet das Referenzprojekt in einem neuen Tab; die aktuelle Zeichenfläche ist eine eigene Umsetzung und verwendet React Flow nicht als Laufzeitbibliothek.

![Miniübersicht mit Bausteinpositionen und sichtbarem Ausschnitt auf .193](/images/logic-studio/0.1.7-miniuebersicht.png)

## Import und Bearbeitung

**HA importieren** öffnen, Automationen/Skripte/Blueprints auswählen und **Aus HA einlesen**, eine YAML-/JSON-Datei oder eingefügten Text verwenden. Eintrag und Vorschau prüfen, dann **Import übernehmen**. Vorher den eigenen Plan als JSON sichern; zusätzlich entstehen Projekt- und Quelldateisicherungen.

Der HA-Konfigurationsordner ist **schreibgeschützt** eingebunden. Gelesen werden `automations.yaml`, `scripts.yaml` und Blueprint-Dateien. Vor dem Parsen kopiert die App Quellen unter `/data/ha-source-backups/<Zeitstempel>/` mit ursprünglichem Namen. `secrets.yaml` wird nicht geöffnet; `!secret` und `!include` bleiben unaufgelöst. Bei ausgelagerten Include-Dateien die tatsächliche Datei selbst importieren.

Orange **FLOW**-Leitungen bilden Reihenfolge und Zweige ab: Zweigausgang → **DO**, anschließend **NEXT → DO**. Gelbe **VALUE/REF**-Leitungen zeigen Blueprint-Parameter und deren `!input`-Verwendung. Eigenschaften enthalten HA-Konfiguration und Zweigpfade als JSON. Parameter-/Feldschlüssel müssen eindeutig sein. Unbekannte Abschnitte bleiben als **YAML_ORIGINAL** erhalten; fehlende Verbindungen können den Export sperren.

![Importvorschau vorhandener HA-Blueprints](/images/logic-studio/blueprint-import.png)

Das **⋮-Menü** jedes Bausteins bietet **Eigenschaften, Duplizieren und Löschen**. Duplizieren übernimmt Eigenschaften ohne Leitungen. Löschen entfernt zugehörige Leitungen; **Rückgängig** stellt sie wieder her. Suche, Favoriten und zuletzt benutzte Bausteine erleichtern die Auswahl.

![Drei-Punkte-Menü im Funktionsplan](/images/logic-studio/block-menu.png)

## Prüfstand und Grenzen

Der Funktionsstand **0.1.5** wurde auf **.193 / HA Core 2026.10.4** geprüft: echter Blueprint-Import, Automation-/Skript-/Blueprint-Beispiele, inhaltlich gleiche YAML-Ausgabe und Menüaktionen. **0.1.6** ist dessen erste öffentliche Paketierung. 22 Node- und acht Python-Tests prüfen unter anderem Export, Persistenz, verschachtelte Abläufe und sicheren Quelldateiimport; die GitHub-Prüfung baut zusätzlich den Container.

**0.1.7 auf .193 / HA Core 2026.10.4:** Echter Maus-Ziehtest für BOOL → BOOL und die Gegenrichtung bestanden. STRING → BOOL und ein bereits belegter Eingang wurden abgewiesen. Miniübersicht, Klicknavigation und Pos1 geprüft. Nach dem Test wurde der Originalplan wiederhergestellt und mit der Sicherung verglichen: **fünf Bausteine, drei Leitungen und alle Paletteinstellungen erhalten**, einschließlich nach dem lokalen Update auf 0.1.7. Vorher vollständiges HA-Backup und separate Plan-/Einstellungssicherung; keine Geräte geschaltet. Aktuell bestehen **26 Node- und acht Python-Tests**. Bilder zeigen die deutsche Oberfläche.

Keine vollständige HA-Semantikprüfung im Editor: Ziele, Templates und Selektoren in HA kontrollieren. Kommentare, YAML-Anker und Formatierung werden nicht originalgetreu rekonstruiert. Importgrenzen: **1 MB, 200 Bausteine, 500 Leitungen**, begrenzte Verschachtelung und bis zu 250 Blueprint-Dateien in üblichen Ordnern. Regler, Kalender und eigene Unterpläne sind teilweise noch Vorlagen.

Für lokale Tests das Release-ZIP vollständig entpacken, Python 3.10+ und die Pakete aus `requirements.txt` installieren; unter Windows danach **Start-Demo.cmd** starten. `http://127.0.0.1:4180/` zeigt Demo-Entitäten ohne HA-Verbindung. Das ZIP enthält außerdem `addon/logic_studio/` für lokale App-Installationen.

Fehler bitte mit Versionen, Architektur und einem kleinen anonymisierten Beispiel [auf GitHub melden](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues). Keine Zugangsdaten, persönlichen Automationen oder Vollbackups veröffentlichen. Weitere Anleitungen und Prüfbericht liegen im Paket. Lizenz: MIT; Herkunft der übernommenen Block-Metadaten siehe `THIRD-PARTY.txt`.
