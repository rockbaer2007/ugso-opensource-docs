---
title: Logic Studio
description: HA Logic Studio Pro 0.1.72 · Skriptnachrichten mit Antwort
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.12 – öffentliches Testupdate, 8. November 2026.** Oberfläche und Dokumentation sind jetzt **DE/EN/FR**. Logic Studio ist eine eigene HA-App für grafische Funktionspläne, unabhängig von Grafik Visual Studio und Blocks for HA. Die React-Flow-Zeichenfläche mit eigenen Bausteinen, typgeprüften Verbindungen, Zoom und MiniMap bleibt erhalten; Bibliotheken und Lizenzen sind lokal enthalten.

::: warning Testversion
Zuerst auf einem Testsystem installieren und vorher ein vollständiges Backup erstellen. Native Detailoptionen werden zunächst als JSON bearbeitet. Die App schreibt keine Automationen oder Skripte in HA zurück und schaltet keine Geräte. Erzeugte Ausgaben immer prüfen und selbst in HA installieren.
:::

[GitHub-Testrelease und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.12) · [Quellcode im Sammel-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## HA Logic Studio Pro 0.1.72

Blocks JS übernimmt ioBroker-Skriptnachrichten mit Antwort und berechneten Zieladressen. Die Importvorschau zeigt am jeweiligen Block, welche Empfangsadresse und Antwortverarbeitung zu prüfen sind.

Auf dem Home-Assistant-Testsystem `.193` setzte ein laufendes Blocks-JS-Skript die Zieladresse aus zwei Textteilen zusammen. Das zweite Skript protokollierte den Empfang, und der Antwortblock im Sender wurde ausgeführt. Danach wurden beide Testprojekte gelöscht und die temporäre Freigabe für `logic_studio_script_message` wieder entfernt.

[HA Logic Studio Pro 0.1.72 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.72)

## HA Logic Studio Pro 0.1.71

Der Schalter „Expertenmodus“ im Projektmenü speichert die Auswahl pro Home-Assistant-Benutzer. Er blendet erweiterte Werkzeuge ein, darunter Quelltext und Skript-API in JavaScript, Import und Codeausgabe in Blocks JS sowie Diagnose und Ausführung im Funktionsplan. Speichern, Abbrechen, Testlauf und Play sind in den dafür vorgesehenen Editoren direkt erreichbar.

Nach einem Vollbackup auf `.193` wurden diese drei Editoren geprüft. Die Auswahl blieb nach dem Neuladen erhalten. Anschließend wurde die ursprüngliche Einstellung wiederhergestellt und nach erneutem Neuladen bestätigt.

[HA Logic Studio Pro 0.1.71 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.71)

## HA Logic Studio Pro 0.1.70

Benutzerdefinierte Ordner lassen sich über das Stiftsymbol im Projektbaum umbenennen. Auf dem Home-Assistant-Testsystem `.193` habe ich nach einem Vollbackup die Projektbaum-Exporte vor dem Umbenennen und nach dem Neuladen verglichen. Ordner-ID, Projektzuordnungen und Reihenfolge der beiden Projekte blieben erhalten. Danach habe ich den ursprünglichen Namen wiederhergestellt und nach erneutem Neuladen bestätigt.

[HA Logic Studio Pro 0.1.70 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.70)

## HA Logic Studio Pro 0.1.69

Der Rules-Assistent übernimmt einen Sprachwechsel im geöffneten Editor. Nach einem Vollbackup auf `.193` wurden im Chrome-Tabletformat (820 × 1180 px) beim Wechsel **DE → EN → FR → DE** Titel, Schritte und Auslöser in der jeweils gewählten Sprache angezeigt. Die Studio-Oberfläche und die App-Verwaltung in Home Assistant zeigten beide **0.1.69**. Der Server liest die angezeigte Version jetzt aus den Paketdaten.

[HA Logic Studio Pro 0.1.69 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.69)

## HA Logic Studio Pro 0.1.68

Der YAML-Export lädt die Datei direkt aus dem Editor herunter. Beim Doppeltest auf `.193` wurden zwei vollständige, bytegleiche YAML-Dateien erzeugt. Chrome meldete beim zweiten Export **Unsicherer Download blockiert**. Nach der manuellen Bestätigung mit **Behalten** lag auch die zweite Datei vollständig im Downloadordner.

[HA Logic Studio Pro 0.1.68 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.68)

## HA Logic Studio Pro 0.1.67

Aktuelles öffentliches Testupdate. Vor dem Update ein Vollbackup erstellen und zuerst auf einem Testsystem prüfen.

„Datenpunkt vorhanden?“ und „Objekt-ID“ behalten beim Import die ioBroker-ID. Ordne sie im jeweiligen Block ausdrücklich einer HA-Entität zu. Beim Import einer JavaScript-Datei erkennt Blocks JS eingebettete Blockly-Daten auch dann, wenn weitere Kommentare folgen.

Unter **Nötige Codeanpassungen** erklärt die Importvorschau, wie sich nicht unterstützte Blöcke wie `exec` ersetzen lassen. Auf `.193` wurden nach einem Vollbackup XML- und JavaScript-Testdateien importiert und die neuen Zuordnungsfelder im Editor geprüft.

### Wiederverbindung nach Core-Neustart

Auf dem Testsystem `.193` wurde vor dem Test ein Vollbackup erstellt. Nach dem Neustart von Home Assistant Core stellte die Runtime die Verbindung 31 Sekunden nach der Trennung wieder her. Derselbe JavaScript-Skriptlauf empfing anschließend den Wechsel des Testhelfers von `off` auf `on` und das benutzerdefinierte HA-Ereignis `logic_studio_runtime_test` samt Testdaten.

### Ordnerwechsel und Reihenfolge nach Neuladen

Auf dem Testsystem `.193` wurden nach einem Vollbackup zwei Testskripte per Drag-and-drop in einen anderen Ordner verschoben. Nach dem Speichern der Sortierung und dem Neuladen von Logic Studio Pro waren beide Skripte weiterhin im Zielordner und standen in der gespeicherten Reihenfolge.

[HA Logic Studio Pro 0.1.67 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.67)

## HA Logic Studio Pro 0.1.66

Aktiviere im Funktionsplan **Zähler und Merker speichern** und speichere das Projekt. CTU, CTD, CTUD, RS und SR können ihre Werte nach einem App-Neustart wiederherstellen.

Der Blocks-JS-Importbericht weist berechnete ioBroker-IDs separat aus. Ordne im importierten Block unter **ID-Zuordnung (JSON)** jede mögliche ioBroker-ID einer HA-Entität zu.

Auf `.193` behielten der CTU-Zähler und der RS-Merker nach einem App-Neustart die Werte `1` und `true`.

Im Live-Test auf `.193` berechnete das importierte Blocks-JS-Skript die ioBroker-ID `zigbee.0.sensor`. Über **ID-Zuordnung (JSON)** las es den HA-Testhelfer `input_boolean.logic_studio_runtime_test`. Zwei Starts über **Play** ergaben im Runtime-Protokoll `false` bei ausgeschaltetem und `true` bei eingeschaltetem Helfer.

[HA Logic Studio Pro 0.1.66 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.66)

## HA Logic Studio Pro 0.1.65

### Autostart, Simulation und ioBroker-Import

JavaScript, TypeScript und Funktionspläne können beim Start der App ausgeführt werden. Speichere dafür die Option **Beim Start der App ausführen** im Projekt. Die Simulation bietet Haltepunkte und Einzelschritt. Beim automatischen Anordnen bleiben angeheftete Bausteine stehen. Blocks JS zeigt beim ioBroker-Import nicht unterstützte Blöcke und feste IDs zur Zuordnung.

Auf `.193` startete das gespeicherte JavaScript-Testprojekt nach einem Neustart der App automatisch. Geprüft wurden außerdem ein Haltepunkt mit Einzelschritt sowie die ioBroker-Importvorschau mit einer festen ID.

[HA Logic Studio Pro 0.1.65 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.65)

## HA Logic Studio Pro 0.1.62


HA Logic Studio Pro ist eine eigenständige Home-Assistant-App im UGSo-Sammelrepository. Sie baut auf Logic Studio auf und greift Erfahrungen aus der Arbeit mit ioBroker auf.

**Verfügbare Funktionen**

- **Funktionsplan:** Bausteine verbinden, Signale an den Eingängen anzeigen und den Plan simulieren. Die Ausführung auf dem HA-Server kann auf Änderungen reagieren oder in einem festen Zyklus laufen.
- **Regeln und Blocks A:** Automationen visuell erstellen und als HA-YAML ausgeben.
- **Blocks JS, JavaScript und TypeScript:** Logik bearbeiten, mit simulierten Werten testen und auf dem HA-Server ausführen.
- **HA-YAML:** Automationen und Skripte bearbeiten, prüfen und exportieren.
- **Projektverwaltung:** Projekte und Ordner pro HA-Benutzer auf dem Server speichern.
- **Sprachwahl:** Die Editoren stehen auf Deutsch, Englisch und Französisch zur Verfügung.

**0.1.62** ergänzte die unten beschriebenen Rules-Funktionen.

### Erweiterte Rules und Live-Test auf .193

Zustandsauslöser unterstützen Von/Nach, ein Attribut und eine Mindestdauer. Bedingungen prüfen Zustände und Attribute sowie numerische Grenzen. DANN und SONST unterstützen einen HA-Aktionswähler mit JSON-Parametern und separate Verzögerungsschritte.

Der Editor und der Aktionswähler wurden lokal im Browser geprüft. Nach einem Vollbackup lief die erzeugte YAML direkt in Home Assistant auf `.193`. Ein kurzer Impuls löste nichts aus. Nach drei Sekunden Zustandsdauer lief DANN. Ein Wechsel des Anzeigenamens löste SONST aus. Beide Traces bestätigten zwei Sekunden Verzögerung und den erwarteten Textwert. Die Testautomation und beide Helfer wurden entfernt.

Die neuen Bausteine werden als HA-YAML ausgegeben. Rules → JS meldet, wenn ein Baustein die Konvertierung verhindert.

[HA Logic Studio Pro 0.1.62 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.62)

### YAML-Export und Live-Test auf .193

Der Rules-Export schützt Zustände wie `on` und `off` vor der Umwandlung in YAML-Wahrheitswerte. Die korrigierte Automation wurde direkt in Home Assistant auf `.193` mit Testhelfern ausgeführt.

| Auslöser | Bedingung | Ergebnis laut HA-Trace |
| --- | --- | --- |
| Zustandswechsel | ODER erfüllt | Beide DANN-Aktionen |
| Zustandswechsel | UND nicht erfüllt | Beide SONST-Aktionen |
| HA-Ereignis | NICHT erfüllt | Beide DANN-Aktionen |
| Uhrzeit 20:26 | NICHT nicht erfüllt | Beide SONST-Aktionen |

Vor dem Test wurde ein Vollbackup erstellt. Die Testautomation und alle drei Testhelfer wurden danach entfernt.

[HA Logic Studio Pro 0.1.61 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.61)

### Rules: kompakte Leiste und mehrere Auslöser

Links zeigt der Editor eine kompakte Liste mit Icons. Eine Regel kann Zustandswechsel, tägliche Uhrzeit und HA-Ereignisse kombinieren. Bedingungen unterstützen UND, ODER und NICHT. In DANN und SONST laufen mehrere Aktionen in der eingetragenen Reihenfolge.

Auf `.193` wurde eine bestehende Regel mit drei Auslösern, zwei Bedingungen und zwei Aktionen pro Zweig geprüft. Die YAML-Vorschau zeigte die erwartete Struktur. Im Studio-Testlauf führten alle drei simulierten Auslöser bei erfüllter ODER-Bedingung beide DANN-Aktionen aus. Bei nicht erfüllter UND-Bedingung liefen beide SONST-Aktionen in der festgelegten Reihenfolge. Es wurden keine echten Geräte geschaltet.

[HA Logic Studio Pro 0.1.60 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.60)

![Rules-Editor auf .193 mit kompakter Leiste und beiden Aktionszweigen](/images/logic-studio/0.1.60-rules-test-193.png)

### Regeln mit dem Assistenten erstellen

Wähle **Regeln → Assistent**. Der Dialog führt durch **Auslöser → Bedingungen → Aktionen → Übersicht**. Eine Regel kann auf einen Zustandswechsel, eine tägliche Uhrzeit in der HA-Zeitzone oder ein HA-Ereignis reagieren. Bedingungen und der SONST-Zweig sind optional. In der Übersicht siehst du die YAML-Vorschau. **Übernehmen** überträgt den Entwurf in den Editor; erst **Speichern** sichert ihn dauerhaft. Bestehende Regeln lassen sich weiterhin bearbeiten und als JavaScript oder HA-YAML öffnen.

[HA Logic Studio Pro 0.1.59 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.59)

Am 12. November 2026 wurden alle drei Auslöser direkt in Home Assistant auf dem Testsystem `.193` geprüft. Ein Zustandswechsel von Aus auf Ein, die tägliche Uhrzeit um 19:38 Uhr (HA-Ortszeit) und das Ereignis `rules_live_0159_event` schalteten den Testausgang jeweils auf Ein. Vor dem Test wurde ein Vollbackup erstellt. Anschließend wurden die drei Testautomationen und beide Testhelfer entfernt.

![Home Assistant zeigt die letzte Ausführung aller drei Rules-Testautomationen und den eingeschalteten Testausgang](/images/logic-studio/0.1.59-rules-live-test-193.png)

### Was seit 0.1.12 neu ist

- **Projektbaum und Editoren:** Projekte und Ordner werden pro HA-Benutzer serverseitig gespeichert. Vorhandene Browserprojekte können beim ersten Start aus dem bisherigen Browser übernommen werden. JavaScript und TypeScript haben Syntaxfarben, Zeilennummern und eigene Werkzeugleisten. Icons und Farben stimmen zwischen Projektauswahl, Baum und Filtern überein. Blocks A und Blocks JS haben getrennte Filter. Die automatisch bemessene Projektspalte bleibt per Anfasser verstellbar.
- **Blocks A und Blocks JS:** Blocks A nutzt den integrierten Katalog von Blocks for HA. Blocks JS hat eine eigene JavaScript-Palette. Blocks A exportiert HA-Automationen als YAML. Blocks JS erzeugt JavaScript für Testlauf und Runtime. Beim ioBroker-Import bleiben unbekannte Blöcke als Platzhalter sichtbar und verhindern die Codeausgabe, bis sie ersetzt sind. ioBroker-Objekt-IDs durch passende HA-Entitäts-IDs ersetzen.
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

### Skripte und Automationen steuern

Unter **Blocks JS → System** wählst du mit **Skript oder Automation auswählen** eine Home-Assistant-Entität aus und verbindest den Block mit **Steuern**. Skripte lassen sich starten oder stoppen. Automationen lassen sich aktivieren, deaktivieren oder einmal auslösen. Beim Auslösen ist **Bedingungen prüfen** standardmäßig aktiv. Wenn du die Option abwählst, überspringt Home Assistant die Bedingungen. Für die Live-Ausführung muss die Zielentität unter `runtime_write_entities` freigegeben sein.

[HA Logic Studio Pro 0.1.58 · GitHub und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.58)

### Funktionen und ioBroker-Import

Unter **Blocks JS → Funktionen** gibt es zwei JavaScript-Funktionsblöcke mit und ohne Rückgabewert. Über das Zahnrad legst du Parameter fest. Über **…** bearbeitest du den Code. Nach dem Anlegen einer Definition erscheint der passende Aufrufblock in der Palette.

Der ioBroker-Import übernimmt Definitionen, Aufrufe, Parameter und JavaScript-Code. Passe ioBroker-spezifische API-Aufrufe an die HA-Runtime an und ordne importierte Objekt-IDs explizit HA-Entitäten zu.

### Verlauf abfragen

Unter **Blocks JS → Sendto → Verlauf abfragen** liest du aufgezeichnete Zustände aus dem HA-Recorder. Ohne Zeitraum gilt der aktuelle Tag in der HA-Zeitzone. Der Ergebnisblock liefert Einträge mit Zeitstempel und Wert. Beim ioBroker-Import bleiben Zeitraum, Aggregation, Schrittweite und Anzahl erhalten.

[HA Logic Studio Pro 0.1.57 · GitHub und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.57)

### 0.1.29 · Manuelles Speichern und Blocks-Editoren

Alle Editoren übernehmen Änderungen erst mit **Speichern**. **Abbrechen** lädt den letzten gespeicherten Stand oder verwirft ein neues Projekt. Bei ungespeicherten Änderungen sind **Play** und **Neustart** gesperrt. Ein laufendes Skript lässt sich weiterhin stoppen. Blocks A öffnet die Entitätsauswahl direkt am Blockfeld. Blocks JS bietet eine an ioBroker orientierte Palette mit HA-Entitäten, HA-Aktionen und Auslösern ohne Jinja.

[Testupdate und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.29)

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
