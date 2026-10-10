---
title: UGSo Blocks for HA
description: Native Home-Assistant-Automationen mit visuellen Blocks erstellen.
---
# UGSo Blocks for HA

Neu in **0.1.18**: [Eigener Block-/Template-Editor](./custom-blocks) als 95%-Dialog, Kategorie Benutzerdefiniert, mehrere Blocks pro Paket, kopierbarer JSON-Code und ZIP-Import/Export. [Blockpaket-Katalog](./catalog/).

Neu in **0.1.17**: Entitäten aus HA laden und in vorhandenen Blockfeldern nach Name/ID suchen. Passende Licht-/Script-/Helferfilter, manuelle IDs ohne Verbindung und serverseitige Zugangsdaten. [Anleitung mit Bild und Grenzen](./entities).

Neu in **0.1.16**: Theme-Auswahl UGSo Standard/Dark/Modern/Tritanopia und Zoom-to-fit-Knopf. Auswahl wird lokal gespeichert; eigene Blocks folgen den Paletten. [Bedienung, Bilder und Originalquellen](./themes). Weiterhin 111 Blocktypen.

**Version 0.1.19 · experimentelle HA-App.** Mit visuellen Blocks entstehen native Home-Assistant-Automationen. Der Editor erzeugt YAML; Home Assistant übernimmt die Ausführung. Entitätsauswahl aus HA ist seit 0.1.17 vorhanden; Live-Aktionsauswahl bleibt geplant.

Die Blocks verwenden die klassischen Blockly-Puzzleformen (Geras) mit kompakter Schrift. Startansicht und Einpassen vergrößern kleine Automationen höchstens auf 80 Prozent. Über die Zoomsteuerung lässt sich die Ansicht weiter vergrößern. Referenz: [Original-Blockly-Beispiele](https://raspberrypifoundation.github.io/blockly-samples/).

## Liste der Blocks und Originalplugins

Neu in **0.1.13**: 18 Blocks für **Timeouts, Objekt, Logik, Schleifen und Listen**. Native HA-Pausen mit Einheiten/Laufzeitwerten, Warten bis mit Timeout, Lauf stoppen, Wiederholungen, Dictionary-Zugriffe und -Zuweisungen, Fallauswahl, Bereichsvergleich, Ersatzwert und Listen. [ioBroker / Original-Blockly / UGSo: Zuordnung und Grenzen](./flow).

Neu in **0.1.12**: **Konvertierung** mit neun Blocks für Zahl, Boolean, String, Typ, Datum/Zeit, Datumsformat/-bestandteile, Zeitdifferenz und JSON. Dynamische Formatauswahl und JSON-Formatierung per Checkbox. JSONata bleibt als Erweiterung vorgemerkt. [Anleitung und ioBroker-Gegenüberstellung](./conversion).

Neu in **0.1.11**: sieben Blocks für **Datum und Zeit**, mit Uhrzeitvergleichen, Zeiträumen über Mitternacht, Datumswerten, Kalenderbeginn, nächsten Sonnenereignissen, Zeitberechnung und Formatierung. [Anleitung und ioBroker-Gegenüberstellung](./time).

Neu in **0.1.10**: **Erhöhe Variable um …** im Variablen-Menü mit Schritt `1`, negativen und dezimalen Schritten. [Bild, Beispiel und Voraussetzungen](./blocks#erhohen-und-verringern-seit-0-1-10).

Neu in **0.1.9**: Kategorie **Logik** mit Vergleich, kompaktem UND/ODER, NICHT, wahr/falsch, null und bedingter Wertauswahl. Variablen unterstützen jetzt auch Boolean und null. [Alle sechs neuen Blocks mit Bildern und Beispiel](./blocks#logik-blocks-seit-0-1-9).

Die [Liste aller 111 Blocks](./blocks) zeigt jeden Block mit Bild und Funktionsbeschreibung. Die Tabelle der Originalplugins verlinkt direkt auf die jeweiligen Quellen.

Neu in **0.1.8**: **Variablen → Variable erstellen …**, Setzen-/Lesen-Blocks und die Kategorie **Templates** mit eigenen Wert- und Bedingungsblocks. Variablen erzeugen native HA-`variables`-Aktionen; Lesen erzeugt <code v-pre>{{ name }}</code>. Jinja wird erst in HA ausgewertet. [Anleitung, Beispiel und Importgrenzen](./blocks#variablen-und-templates-verwenden).

Neu in 0.1.7: **Suche am Menüende**, mehrzeilige Texte, Prozent-Slider, Farbe und Lichtaktion, Datum heute und abhängige Helfer-Dropdowns. Plus/Minus ergänzt oder entfernt den letzten Eingang beziehungsweise sonst-falls-Zweig; **S** schaltet Sonst um. Entfernte Eingänge lösen ihre Blocks ab, löschen sie nicht. Das Zahnrad bleibt zum Umordnen.

Der Datumsvergleich einschließlich Jahr wird in HA mit `now().strftime('%Y-%m-%d')` ausgewertet; er verwendet die HA-Zeitzone und ist eine Bedingung, kein Auslöser. Diese Form erhält beim Import den Datumsblock; andere Template-Bedingungen erhalten den allgemeinen Template-Block. Die Lichtaktion erzeugt RGB-Farbe und Helligkeit in Prozent. Timer nutzen ihre konfigurierte Dauer; zusätzliche Parameter bleiben in der generischen HA-Aktion. Die tatsächlichen Gerätefähigkeiten müssen in HA geprüft werden.

Das eigene UGSo-Icon verbindet Haus und Puzzle-Baustein und wird in Oberfläche, Browser und HA-App verwendet. Zehn Originalplugins werden lokal ausgeliefert. Farbmischung und Zufallsfarben sind seit 0.1.15 umgesetzt; automatisch wachsende Anschlüsse und Live-Aktionsauswahl bleiben offen. Textverknüpfung und Listenbearbeitung sind umgesetzt.

## Im HA-App-Store installieren

Das gemeinsame Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` hinzufügen beziehungsweise über die Repository-Aktualisierung neu laden. **UGSo Blocks for HA** installieren, starten und **Weboberfläche öffnen** wählen. Die App unterstützt amd64 und aarch64 und öffnet den Editor über HA-Ingress. Zum Öffnen ist keine zusätzliche Token-Eingabe nötig. Die App lädt Entitäten lesend über den Supervisor und schreibt keine HA-Systemdateien.

## Start und Dateien

Der Code liegt neben Grafik Visual Studio im [gemeinsamen Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha). Im Ordner `blocks_for_ha` mit Node.js 22.12 oder neuer:

```sh
npm install
npm run dev
```

Editor: `http://127.0.0.1:4180/`. YAML kann angezeigt, kopiert, als Datei gespeichert und wieder als Blocks geöffnet werden. Unterstützt wird eine Automation als Objekt oder Liste mit einem Eintrag. Nicht unterstützte Strukturen werden zurückgewiesen. JSON-Projekte erhalten zusätzlich Blockpositionen; der Browser sichert den letzten Stand lokal.

## ioBroker / unsere Blocks: vorhandene Funktionen

111 Blocktypen einschließlich des Automationsrahmens; Variablen, Templates, Datum/Zeit und Konvertierung sind im Katalog beschrieben:

| ioBroker-Konzept | UGSo Blocks für HA | HA-Ausgabe |
| --- | --- | --- |
| Script-Rahmen | Automation | `triggers`, `conditions`, `actions` |
| Zustandstrigger | Zustand erreicht | `trigger: state` |
| Zahlenprüfung als Trigger | Grenzübertritt über/unter | `trigger: numeric_state` |
| Zeitplan | Uhrzeit | `trigger: time` |
| Astro | Sonnenaufgang/-untergang | `trigger: sun` |
| Systemstart, anderer Lebenszyklus | HA startet | `trigger: homeassistant` |
| Zustandsvergleich | Zustand ist | `condition: state` |
| Zahlenvergleich | Zahl über/unter | `condition: numeric_state` |
| UND/ODER/NICHT | Alle/mindestens eine/keine Bedingungen | `and`, `or`, `not` |
| Steuere/umschalten | Ein/Aus/Umschalten | Passende Aktion der Entitätsdomain |
| Adapteraktion | Generische HA-Aktion | `action`, optional Entitätsziel und JSON-Daten |
| Pause | Warte Sekunden | `delay` |
| Falls/sonst falls/sonst | Erweiterbarer Falls-Block | `if` oder `choose` |
| Zahl | Zahlen-Wertblock, auch als Shadow-Standardwert | Konstante für Grenze oder Wartezeit |
| Text | Text-Wertblock mit Shadow | Logmeldung |
| Prozent | Slider-Wert 0–100 | Number-Konstante |
| Farbe | Farb-Wertblock | Colour-Wert |
| Lichtfarbe | Licht mit Farbe/Helligkeit | `rgb_color`, `brightness_pct` |
| Datum | Datum heute ist/ab/bis | HA-Template-Bedingung |
| Helfer steuern | Abhängige Aktionsauswahl | Schalter/Zähler/Timer |
| Debug-Ausgabe | Log mit Schweregrad | `system_log.write` |
| Script steuern | Starten/stoppen/aufrufen und warten | `script.turn_on`, `script.turn_off` oder direkter Aufruf |
| Aktualisiere State, andere Bedeutung | Entität aktualisieren | `homeassistant.update_entity` |

Name, Beschreibung, ID und Ausführungsmodi `single`, `restart`, `queued`, `parallel` sind vorhanden. Für queued/parallel lässt sich die maximale Anzahl festlegen. Drei Beispiele zeigen Licht, Batterie und Abendlicht.

## System-Blocks ab Version 0.1.6

Die Kategorie **System** enthält drei neue Aktionsblocks. Unter **Werte** steht zusätzlich ein grüner **Text**-Block bereit. Er besitzt einen String-Output und passt in den Meldungseingang des Log-Blocks; Zahlen und Bedingungen passen dort nicht hinein.

| ioBroker | Unser Block | Bedienung und HA-Verhalten |
| --- | --- | --- |
| Debug-Ausgabe | Log | Meldung als Text-Shadow oder eigener Textblock; Dropdown Info, Warnung, Fehler, Debug oder Kritisch. Erzeugt `system_log.write`. |
| Script steuern | HA-Script | Script-ID eingeben; starten ohne Warten, stoppen oder aufrufen und warten wählen. |
| Aktualisiere State | Entität aktualisieren | Fordert mit `homeassistant.update_entity` eine Aktualisierung an. Setzt keinen Zustand und besitzt keine ioBroker-`ack`-Semantik. |
| Text | Text-Wertblock | Editierbarer Text für Logmeldungen, im Projekt und YAML erhalten. |

**Starten ohne Warten** erzeugt `script.turn_on`; die Automation läuft anschließend weiter. **Stoppen** erzeugt `script.turn_off`. **Aufrufen und warten** erzeugt einen direkten `script.name`-Aufruf: Die Automation wartet auf dessen Abschluss; Fehler können an den Aufrufer weitergegeben werden. Script-Parameter werden weiterhin über die generische HA-Aktion eingegeben.

Beim YAML-Import werden genau passende Systemaktionen als eigene Blocks erkannt. Zusätzliche Daten, etwa ein eigener Logger oder Script-Variablen, bleiben in der generischen HA-Aktion erhalten. Die Aktualisierung wird von der jeweiligen Integration unterstützt oder begrenzt. Logmeldungen entstehen erst bei Ausführung in HA; Info und Debug können durch die HA-Logkonfiguration ausgefiltert werden.

Referenzen: [HA-Systemprotokoll](https://www.home-assistant.io/integrations/system_log/), [HA-Scripts](https://www.home-assistant.io/integrations/script/), [HA-Core-Aktionen](https://www.home-assistant.io/integrations/homeassistant/).

## Zahnrad: Falls erweitern

Wie beim vertrauten ioBroker-Editor öffnet das Zahnrad eine kleine Arbeitsfläche. Dort lassen sich **sonst falls**-Elemente an den Falls-Rahmen anhängen und ein optionaler **sonst**-Zweig ergänzen. Die jeweiligen Bedingungen und Aktionen werden anschließend im Hauptblock eingesteckt.

- Ein Falls-Zweig erzeugt `if`/`then`, optional `else`.
- Mehrere Zweige erzeugen `choose`, der Sonst-Zweig wird `default`.
- HA führt den ersten passenden Zweig aus. Weitere passende Zweige werden nicht ausgeführt.
- Entfernte Zweige lösen ihre verbundenen Blocks ab. Diese müssen wieder verbunden oder entfernt werden, bevor exportiert werden kann.
- YAML-Import und JSON-Projekte erhalten die Verzweigungen. Alte Projekte behalten ihre bisherigen Sonst-Aktionen.

UND/ODER/NICHT besitzt ein eigenes Zahnrad für 1–100 seitliche Bedingungseingänge. Auslöser und Aktionen lassen sich als Ketten erweitern. Sonnen-, Vergleichs- und Schaltvarianten werden direkt im Dropdown gewählt. Die generische HA-Aktion verwendet zunächst JSON-Daten; ein visueller Datenfeld-Mutator ist noch geplant.

## Andocken und Bedienung

Das Kategorienmenü ist dunkel, die aufgeklappte Blockauswahl hell. Werte sind grün, Auslöser orange, Bedingungen violett und Aktionen blau. Die Kategorienmarkierungen zeigen die jeweilige Blockgruppe; die ausgewählte Kategorie ist zusätzlich hervorgehoben.

- **Output links / Werteingang rechts:** Bedingungen liefern Boolean-Werte. Sie passen in „Nur wenn“, „Falls“, „sonst falls“ und UND/ODER/NICHT. Zahlen liefern Number-Werte und passen in Grenzen oder Wartezeiten. Die Typprüfung verhindert unpassende Verbindungen.
- **Previous oben / Next unten:** Auslöser und Aktionen bilden jeweils eigene Ketten; sie können nicht miteinander vertauscht werden.
- **Statement-Innenraum:** „mache“ und „sonst“ nehmen Aktionsfolgen auf. Bedingungen gehören an die seitlichen Werteingänge.
- **Shadow-Zahlen:** Grenzen und Wartezeiten haben editierbare Standardwerte. Ein herausgezogener Zahlenblock kann sie ersetzen. Wird dieser entfernt, erscheint der Standardwert wieder. Logmeldungen nutzen String-Textblocks mit editierbarem Shadow. Sensor- und Entitäts-Wertblocks sind noch nicht umgesetzt.
- **Kontextmenü:** Rechtsklick beziehungsweise langes Drücken bietet die Blockly-Funktionen, etwa Duplizieren, Kommentar, Einklappen, Deaktivieren, Löschen und Hilfe. Hilfe führt hierher. Kommentare bleiben im JSON-Projekt; sie werden noch nicht als YAML-Kommentare exportiert.
- **Deaktivieren:** Deaktivierte Aktionen und Auslöser werden beim Export übersprungen. Deaktivierte Bedingungen werden ausgelassen. Pflichtinhalte bleiben erforderlich; fehlende Auslöser, leere Falls-Bedingungen oder leere Aktionszweige verhindern den Export.
- **Papierkorb:** Blocks löschen, den Papierkorb öffnen und gelöschte Blocks zurück auf die Arbeitsfläche ziehen. Der Verlauf ist auf die aktuelle Sitzung begrenzt. Rückgängig/Wiederholen steht zusätzlich bereit.
- **Einfügemarkierung:** Blockly zeigt beim Ziehen die mögliche Andockposition an.

Projektdateien aus Version 0.1.4 und früher werden automatisch auf die neue Anschlussstruktur umgestellt. Alte Bedingungsketten werden als UND-Gruppen mit derselben YAML-Bedeutung erhalten. Die bestehenden YAML-Dateien bleiben importierbar.

## Blockly-Bibliothek und verbindlicher Entwicklungsstand

Wir verwenden bereits **Blockly 13.3.0**, die originale Bibliothek, statt eine eigene Block-Engine zu entwickeln. Blockly übernimmt Arbeitsfläche, Kategorie-Toolbox und Flyouts, Verbindungen mit Typprüfung, Shadow-Blocks, Mutatoren, Kontextmenü, Zoom, Papierkorb und Einfügemarkierungen. Unsere HA-Blocks, Strukturvalidierung, Projektmigration und der YAML-Generator sind eigener UGSo-Code. Es wird kein ioBroker-JavaScript ausgeführt.

Die [Originaldokumentation zur Arbeitsfläche und zu Blockteilen](https://docs.blockly.com/guides/get-started/workspace-anatomy/) und die [Blockly-Beispiele](https://raspberrypifoundation.github.io/blockly-samples/) dienen als Referenz für vertraute Bedienmuster. Bibliotheksupdates werden bewusst mit Verbindungs-, Import-/Export- und Browserprüfungen übernommen.

| Aufgabe | Stand in 0.1.16 / nächster Schritt |
| --- | --- |
| Anschlussgeometrie und Typprüfung | Boolean-Bedingungen und Number-Werte seitlich; Auslöser/Aktionen als getrennte Statement-Ketten umgesetzt |
| Erweiterbare Blocks | Falls, UND/ODER/NICHT, Fallauswahl, Objekte und Listen umgesetzt; Aktionsdaten später als visuelle Felder |
| Standardwerte | Shadow-Zahlen und Textblocks umgesetzt; Entitäts-Wertblocks offen |
| Sensorwerte und Attribute | Eigene Wert-Blocks offen; über Templates bereits nutzbar. Typumwandlung als Konvertierungs-Blocks vorhanden |
| Editorbedienung | Kontextmenü, Hilfe, Deaktivieren, Papierkorb-Wiederherstellung, Zoom und Einfügemarkierung vorhanden |
| Kommentare | Im Projekt erhalten; YAML-Kommentare und eigener Kommentarblock offen |
| Menü und Blockfarben | Dunkles Kategorienmenü, helle Blockauswahl, getrennte Gruppenfarben umgesetzt |
| ioBroker-Kategorien | System, Datum/Zeit, Konvertierung, Timeouts, Objekt und Logik geprüft; Unterschiede zur HA-Ausführung dokumentiert |
| JSONata | Vorgemerkt; native Objekt-/Listen-Zugriffe und optionalen HA-Runtimeadapter prüfen |
| Veröffentlichung und Updates | Jede neue HA-App von Anfang an im gemeinsamen Repository mit installierbarem Paket; Paket- und Oberflächenversion gemeinsam anheben |
| HA-Verbindung, Katalog und Plugins | Lesende Entitätsanbindung und deklarative Blockpakete vorhanden; Live-Aktionsauswahl und Paketupdates offen |

Diese Seite hält umgesetzte Funktionen und offene Aufgaben zusammen fest und wird mit jeder Erweiterung gepflegt.

## Eigene Blocks: umgesetzt und Roadmap

Seit 0.1.18 sind der eigene HA-Editor, Blockly-Vorschau, Wert/Bedingung/Aktion/Auslöser, typisierte Felder und Werteingänge, Paketimport/export und eingebettete Projektdefinitionen umgesetzt. [Bedienung und Grenzen](./custom-blocks).

Die Einbettung der originalen Blockly Developer Tools, Dropdowns, Bilder, Variablenfelder, Statement-Container, Mutatoren, dynamische Eingänge, Paketupdates und Deinstallation bleiben vorgemerkt.

## System: Stand und nächste Schritte

Steuern, Umschalten, Wartezeit, generische Aktionen, Log-Ausgabe, Script-Steuerung, Entität aktualisieren und Helfer steuern sind vorhanden. Entitätsauswahl ist seit 0.1.17 umgesetzt. Eigene Blocks für Kommentar, Zustand/Attribute als Werte, Existenz/Verfügbarkeit und Zahlen-/Texthelfer folgen schrittweise. ioBroker-`ack`, Adapterinstanzen und Datenpunkt-Erzeugung haben kein direktes HA-Gegenstück.

Die vollständige [Gegenüberstellung mit Umsetzungsstatus](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/blocks_for_ha/docs/iobroker-comparison.de.md) wird bei jeder Erweiterung aktualisiert. Deklarative Blockpakete und Beispielkatalog sind seit 0.1.18 vorhanden.

## Prüfung und Original

Der Editor prüft die unterstützte Struktur. Entitäts-IDs werden gesucht oder manuell eingegeben; installierte Aktionen und echte HA-Ausführung sind damit nicht verifiziert. Vor Verwendung Beispiel-Entitäten ersetzen und Aktionen in HA prüfen. Der Editor schreibt keine HA-Systemdateien.

Built with [Blockly](https://www.blockly.com/). Eigene HA-Blocks, kein ioBroker-Fork. Eigener Code und Blockly: Apache-2.0; YAML-Bibliothek: ISC. Lizenztexte werden mitgeliefert.

## Built with Blockly

Blockly ist eine Open-Source-Entwicklerbibliothek der Raspberry Pi Foundation, ursprünglich bei Google entwickelt. Seit **0.1.19** verwendet die App das unveränderte offizielle Badge mit 32 Pixel Höhe, Freiraum und Link zu Blockly. Beide SVG-Varianten werden lokal ausgeliefert. [Originalhinweise zur Attribution](https://docs.blockly.com/guides/app-integration/attribution/).

<a class="blockly-attribution" href="https://www.blockly.com/" target="_blank" rel="noopener noreferrer"><img class="badge-light" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-white.svg" alt="Built with Blockly" width="87" height="32"><img class="badge-dark" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-black.svg" alt="Built with Blockly" width="87" height="32"></a>
