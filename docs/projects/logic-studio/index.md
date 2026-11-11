---
title: Logic Studio
description: HA Logic Studio Pro 0.1.28 mit serverseitiger Funktionsplan-Ausführung und Editoren in DE, EN und FR.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.12 – öffentliches Testupdate, 8. November 2026.** Oberfläche und Dokumentation sind jetzt **DE/EN/FR**. Logic Studio ist eine eigene HA-App für grafische Funktionspläne, unabhängig von Grafik Visual Studio und Blocks for HA. Die React-Flow-Zeichenfläche mit eigenen Bausteinen, typgeprüften Verbindungen, Zoom und MiniMap bleibt erhalten; Bibliotheken und Lizenzen sind lokal enthalten.

::: warning Testversion
Zuerst auf einem Testsystem installieren und vorher ein vollständiges Backup erstellen. Native Detailoptionen werden zunächst als JSON bearbeitet. Die App schreibt keine Automationen oder Skripte in HA zurück und schaltet keine Geräte. Erzeugte Ausgaben immer prüfen und selbst in HA installieren.
:::

[GitHub-Testrelease und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.12) · [Quellcode im Sammel-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## HA Logic Studio Pro 0.1.28

HA Logic Studio Pro ist eine separate Home-Assistant-App im UGSo-Sammelrepo. **0.1.28** ist das aktuelle öffentliche Testupdate. Vor einem Update ein Vollbackup erstellen und zuerst auf einem Testsystem prüfen.

### Was seit 0.1.12 neu ist

- **Projektbaum und Editoren:** Projekte und Ordner werden pro HA-Benutzer serverseitig gespeichert. Vorhandene Browserprojekte können beim ersten Start aus dem bisherigen Browser übernommen werden. JavaScript und TypeScript haben Syntaxfarben, Zeilennummern und eigene Werkzeugleisten. Icons und Farben stimmen zwischen Projektauswahl, Baum und Filtern überein. Blocks A und Blocks JS haben getrennte Filter. Die automatisch bemessene Projektspalte bleibt per Anfasser verstellbar.
- **Blocks A und Blocks JS:** Beide nutzen den integrierten Katalog von Blocks for HA. Blocks A exportiert HA-Automationen als YAML. Blocks JS erzeugt JavaScript für Testlauf und Runtime. Beim ioBroker-Import bleiben unbekannte Blöcke als Platzhalter sichtbar und verhindern die Codeausgabe, bis sie ersetzt sind. ioBroker-Objekt-IDs durch passende HA-Entitäts-IDs ersetzen.
- **Funktionsplan:** Simulation, Zeitschritt von einer Sekunde und Zurücksetzen liegen als Icons in der oberen Leiste. Ausgabeformat und Vorschau sind rechts angeordnet. Verbindungen lassen sich am Zieleingang umhängen, Signalwerte erscheinen direkt am Eingang.
- **Server-Runtime:** Play startet JavaScript, transpiliertes TypeScript oder Blocks JS auf dem HA-Server. Stopp und Neustart sind im Editor verfügbar. Status und Runtime-Protokoll bleiben beim Browserwechsel abrufbar. Der separate **Testlauf** verwendet simulierte Zustände und Ereignisse. HA-YAML-Skripte und -Automationen werden exportiert und anschließend in Home Assistant ausgeführt.

### Live-Runtime einrichten

In **Einstellungen → Apps → HA Logic Studio Pro → Konfiguration** die benötigten Einträge setzen, speichern und die App neu starten. Die Listen sind anfangs leer. Beispiel für einen eigens angelegten Testhelfer:

```yaml
runtime_read_entities: []
runtime_write_entities:
  - input_boolean.logic_studio_runtime_test
runtime_events:
  - logic_studio_runtime_test
```

Eine Schreibfreigabe erlaubt auch das Lesen. `ha.readState` und `ha.readAttribute` liefern die zuletzt von HA bestätigten Werte. `ha.onState`, `ha.onAttribute` und `ha.onEvent` reagieren auf freigegebene Änderungen und Ereignisse. `ha.callAction` unterstützt Schaltaktionen, Werte für Zahlen-, Text- und Auswahlhelfer sowie Taster mit genau einem freigegebenen Ziel. `ha.schedule` verarbeitet Zeitmuster und feste Uhrzeiten mit optionalen Wochentagen in der HA-Zeitzone.

Nach einem App-Neustart müssen Skripte erneut gestartet werden. Bei einer Verbindungsunterbrechung oder abgelehnten Aktion hält die Runtime das Skript an und protokolliert den Fehler. Astro-Auslöser und automatische Wiederverbindung sind offen.

**Geprüft auf .193 mit HA 2026.11.1:** Live-Zustand und Attribut gelesen, Testhelfer per Zeitplan eingeschaltet und per echtem HA-Ereignis ausgeschaltet. Beide Zustandswechsel wurden gemeldet. Ein importierter Blocks-JS-Zeitplan lief alle zwei Sekunden. Zuvor wurden Start, Stopp, Neustart und der Weiterlauf nach Verlassen der Studio-Seite mit JavaScript und TypeScript geprüft.

### 0.1.28 · Übersetzungen in den Editoren

Version **0.1.28** ergänzt die Übersetzungen für Regeln, Blocks A, Blocks JS, JavaScript, TypeScript und HA-YAML. Die Sprachwahl gilt auch für den Funktionsplan. [Testupdate und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.28)

Auf .193 wurden die Werkzeugleisten von Funktionsplan, Regeln, Blocks A, Blocks JS, JavaScript, TypeScript, HA-Automation und HA-Skript im Browser in allen drei Sprachen geprüft. Zusätzlich wurde der französische Dialog für Codebeispiele geprüft.

Für die Installation im App-Store des UGSo-Sammelrepositories **HA Logic Studio Pro** auswählen. Bei einer bestehenden GitHub-Installation nach Updates suchen und **HA Logic Studio Pro → Aktualisieren** wählen. Mit **DE**, **EN** und **FR** oben in der Projektleiste wechselt die Sprache der Editoren.

### 0.1.26 · FBD Runtime

Funktionsplan direkt über **Play** auf dem HA-Server starten. **Automatisch** reagiert auf Änderungen der freigegebenen Zustände und Attribute; **Fester Zyklus** wertet den Plan alle 100 bis 60.000 ms aus. Simulation und YAML-Ausgabe bleiben separat. **Speichern** übernimmt den Entwurf, **Abbrechen** lädt den letzten gespeicherten Stand. Die Werkzeugleiste ist in DE/EN/FR verfügbar.

Auf .193 schaltete der Automatikstart den Testhelfer ein; der 200-ms-Zyklus schaltete ihn wieder aus. Stopp und das Verwerfen einer ungespeicherten Änderung wurden ebenfalls geprüft. Die Reaktion auf Eingangsänderungen wurde zusätzlich lokal für beide Betriebsarten getestet.

[GitHub-Testupdate und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.26) · [App im Sammelrepository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_logic_studio_pro)

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

## Sprache, Werkzeugleiste und Dokumentation

Oben **Sprache → Deutsch / English / Français** wählen. Menüs, Bausteinbeschreibungen, Entitätsauswahl sowie Import-/Exportdialoge wechseln ohne Neuladen. Die Auswahl wird mit den Browser-/App-Einstellungen gespeichert. **Eigene Namen, Entitäts-IDs, Werte, Anschlussbezeichnungen und erzeugter YAML-/JavaScript-Code werden nicht übersetzt.**

**Dokumentation** rechts zeigt die tatsächlich unterstützten Tastenkürzel und bei ausgewähltem Baustein dessen Beschreibung sowie Ein-/Ausgänge. **Strg+Z / Strg+Y**: Rückgängig/Wiederholen; **Entf**: Auswahl löschen; **Esc**: Verbindung abbrechen/Menü schließen. Anschlüsse lassen sich mit Tab und Enter/Leertaste auswählen und verbinden. Debugger-Befehle des ioBroker-Referenzeditors werden nicht als verfügbare Funktionen dargestellt.

Die Werkzeugleiste gruppiert **Rückgängig/Wiederholen → Projekt → Simulation → Ausgabe**. Die drei Simulationsbuttons sind gleich groß und einzeln erkennbar. Das Projektmenü enthält zusätzlich **Neues Projekt** und **Beispiel laden**. Die Entitätsauswahl öffnet über das Icon **neben HA-Entity-ID** in den Eigenschaften von STATE_IN/STATE_OUT; der bisherige obere Auswahlbutton entfällt.

![Deutsche Dokumentationsansicht auf .193 mit unverändertem Plan](/images/logic-studio/0.1.12-193-de-documentation.png)

![Englische Dokumentationsansicht desselben Plans auf .193](/images/logic-studio/0.1.12-193-en-documentation.png)

![Französische Dokumentationsansicht desselben Plans auf .193](/images/logic-studio/0.1.12-193-fr-documentation.png)

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

Rechts unten zeigt die **MiniMap** farbige Bausteinpositionen und den sichtbaren Ausschnitt. In der MiniMap ziehen zum Navigieren und das Mausrad zum Zoomen verwenden. Auf der freien Zeichenfläche ziehen verschiebt den Ausschnitt; **+/−** ändern den Zoom, **Alles anzeigen** passt alle Bausteine ein. Bausteine am Kopf verschieben. Der Herkunftslink **React Flow** bleibt unten rechts sichtbar. Seit 0.1.8 läuft die Bibliothek tatsächlich im Editor; Fachlogik, Typprüfung und Exporte bleiben eigenständige Logic-Studio-Funktionen.

![React-Flow-Zeichenfläche mit erhaltenem Originalplan und MiniMap auf .193](/images/logic-studio/0.1.8-react-flow-193.jpg)

![Lokaler React-Flow-Test mit typisierten Bausteinen](/images/logic-studio/0.1.8-react-flow-local.jpg)

Die folgenden Bilder dokumentieren zusätzlich die vorherigen Tests mit 0.1.7.

![Miniübersicht mit Bausteinpositionen und sichtbarem Ausschnitt auf .193](/images/logic-studio/0.1.7-miniuebersicht.png)

## Import und Bearbeitung

**HA importieren** öffnen, Automationen/Skripte/Blueprints auswählen und **Aus HA einlesen**, eine YAML-/JSON-Datei oder eingefügten Text verwenden. Eintrag und Vorschau prüfen, dann **Import übernehmen**. Vorher den eigenen Plan als JSON sichern; zusätzlich entstehen Projekt- und Quelldateisicherungen.

Der HA-Konfigurationsordner ist **schreibgeschützt** eingebunden. Gelesen werden `automations.yaml`, `scripts.yaml` und Blueprint-Dateien. Vor dem Parsen kopiert die App Quellen unter `/data/ha-source-backups/<Zeitstempel>/` mit ursprünglichem Namen. `secrets.yaml` wird nicht geöffnet; `!secret` und `!include` bleiben unaufgelöst. Bei ausgelagerten Include-Dateien die tatsächliche Datei selbst importieren.

Orange **FLOW**-Leitungen bilden Reihenfolge und Zweige ab: Zweigausgang → **DO**, anschließend **NEXT → DO**. Gelbe **VALUE/REF**-Leitungen zeigen Blueprint-Parameter und deren `!input`-Verwendung. Eigenschaften enthalten HA-Konfiguration und Zweigpfade als JSON. Parameter-/Feldschlüssel müssen eindeutig sein. Unbekannte Abschnitte bleiben als **YAML_ORIGINAL** erhalten; fehlende Verbindungen können den Export sperren.

![Importvorschau vorhandener HA-Blueprints](/images/logic-studio/blueprint-import.png)

Das **⋮-Menü** jedes Bausteins bietet **Eigenschaften, Duplizieren und Löschen**. Duplizieren übernimmt Eigenschaften ohne Leitungen. Löschen entfernt zugehörige Leitungen; **Rückgängig** stellt sie wieder her. Suche, Favoriten und zuletzt benutzte Bausteine erleichtern die Auswahl.

![Drei-Punkte-Menü im Funktionsplan](/images/logic-studio/block-menu.png)

## Prüfstand und Grenzen

**0.1.12 auf .193 / HA Core 2026.10.4:** Nach Vollbackup die lokale App von 0.1.8 aktualisiert. DE/EN/FR, Dokumentationsansicht und reale Entitätsauswahl erfolgreich geprüft. Französisch blieb nach Browser-Neuladen, App-Neustart und erneutem Laden des gespeicherten App-Projekts erhalten; abschließend wieder Deutsch eingestellt. Der Vergleich der Projektdateien zeigt **nur die neue Versionsnummer**, alle fünf Bausteine, drei Verbindungen, Namen, Werte und Positionen sind identisch. Der erzeugte YAML-Code ist in EN und FR identisch. Keine Geräte geschaltet. **31 Node- und neun Python-Tests** bestanden. Die folgenden älteren Berichte bleiben als Historie erhalten.

![Deutsch nach erfolgreichem App-Neustart auf .193](/images/logic-studio/0.1.12-193-neustart-de.png)

**0.1.8 auf .193 / HA Core 2026.10.4:** Bestehende lokale App nach Vollbackup aktualisiert. BOOL-Verbindungen per Maus, STRING→BOOL-Abweisung, belegte Eingänge, Verschieben/Rückgängig, Duplizieren, Zoom und MiniMap bestanden. Die Entitätsauswahl liest HA-Entitäten; ein verschachteltes Skript mit If/Then/Else, Delay und Stop wurde importiert und strukturerhaltend ausgegeben. Danach Originalplan wiederhergestellt und nach Neuladen verglichen: **alle IDs, Positionen, Parameter und drei Leitungen unverändert**, ebenso Favoriten, zuletzt benutzt und eingeklappte Kategorien. Keine Geräte geschaltet. Docker-Build und Container-HTTP-Test erfolgreich; **29 Node- und acht Python-Tests** bestanden. Bilder zeigen die deutsche Oberfläche. Hell-/Dunkel-Wechsel wurde in diesem Schritt nicht erneut manuell geprüft.

Der Funktionsstand **0.1.5** wurde auf **.193 / HA Core 2026.10.4** geprüft: echter Blueprint-Import, Automation-/Skript-/Blueprint-Beispiele, inhaltlich gleiche YAML-Ausgabe und Menüaktionen. **0.1.6** ist dessen erste öffentliche Paketierung. 22 Node- und acht Python-Tests prüfen unter anderem Export, Persistenz, verschachtelte Abläufe und sicheren Quelldateiimport; die GitHub-Prüfung baut zusätzlich den Container.

**0.1.7 auf .193 / HA Core 2026.10.4:** Echter Maus-Ziehtest für BOOL → BOOL und die Gegenrichtung bestanden. STRING → BOOL und ein bereits belegter Eingang wurden abgewiesen. Miniübersicht, Klicknavigation und Pos1 geprüft. Nach dem Test wurde der Originalplan wiederhergestellt und mit der Sicherung verglichen: **fünf Bausteine, drei Leitungen und alle Paletteinstellungen erhalten**, einschließlich nach dem lokalen Update auf 0.1.7. Vorher vollständiges HA-Backup und separate Plan-/Einstellungssicherung; keine Geräte geschaltet. Aktuell bestehen **26 Node- und acht Python-Tests**. Bilder zeigen die deutsche Oberfläche.

Keine vollständige HA-Semantikprüfung im Editor: Ziele, Templates und Selektoren in HA kontrollieren. Kommentare, YAML-Anker und Formatierung werden nicht originalgetreu rekonstruiert. Importgrenzen: **1 MB, 200 Bausteine, 500 Leitungen**, begrenzte Verschachtelung und bis zu 250 Blueprint-Dateien in üblichen Ordnern. Regler, Kalender und eigene Unterpläne sind teilweise noch Vorlagen.

Für lokale Tests das Release-ZIP vollständig entpacken, Python 3.10+ und die Pakete aus `requirements.txt` installieren; unter Windows danach **Start-Demo.cmd** starten. `http://127.0.0.1:4180/` zeigt Demo-Entitäten ohne HA-Verbindung. Das ZIP enthält außerdem `addon/logic_studio/` für lokale App-Installationen.

Fehler bitte mit Versionen, Architektur und einem kleinen anonymisierten Beispiel [auf GitHub melden](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues). Keine Zugangsdaten, persönlichen Automationen oder Vollbackups veröffentlichen. Weitere Anleitungen und Prüfbericht liegen im Paket. Lizenz: MIT; Herkunft der übernommenen Block-Metadaten siehe `THIRD-PARTY.txt`.
