---
title: UGSo Blocks for HA
description: Native Home-Assistant-Automationen mit visuellen Blocks erstellen.
---
# UGSo Blocks for HA

**Version 0.1.5 · experimentelle HA-App.** Mit visuellen Blocks entstehen native Home-Assistant-Automationen. Der Editor erzeugt YAML; Home Assistant übernimmt die Ausführung. Direkte Entitäts-/Aktionsauswahl aus HA ist noch geplant.

Die Blocks verwenden die klassischen Blockly-Puzzleformen (Geras) mit kompakter Schrift. Startansicht und Einpassen vergrößern kleine Automationen höchstens auf 80 Prozent. Über die Zoomsteuerung lässt sich die Ansicht weiter vergrößern. Referenz: [Original-Blockly-Beispiele](https://raspberrypifoundation.github.io/blockly-samples/).

## Im HA-App-Store installieren

Das gemeinsame Repository `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` hinzufügen beziehungsweise über die Repository-Aktualisierung neu laden. **UGSo Blocks for HA** installieren, starten und **Weboberfläche öffnen** wählen. Die App unterstützt amd64 und aarch64 und öffnet den Editor über HA-Ingress. Zum Öffnen ist keine zusätzliche Token-Eingabe nötig. Die App greift noch nicht auf HA-Entitäten zu und schreibt keine HA-Systemdateien.

## Start und Dateien

Der Code liegt neben Grafik Visual Studio im [gemeinsamen Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha). Im Ordner `blocks_for_ha` mit Node.js 22.12 oder neuer:

```sh
npm install
npm run dev
```

Editor: `http://127.0.0.1:4180/`. YAML kann angezeigt, kopiert, als Datei gespeichert und wieder als Blocks geöffnet werden. Unterstützt wird eine Automation als Objekt oder Liste mit einem Eintrag. Nicht unterstützte Strukturen werden zurückgewiesen. JSON-Projekte erhalten zusätzlich Blockpositionen; der Browser sichert den letzten Stand lokal.

## ioBroker / unsere Blocks: vorhandene Funktionen

14 Blocktypen einschließlich des Automationsrahmens:

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

Name, Beschreibung, ID und Ausführungsmodi `single`, `restart`, `queued`, `parallel` sind vorhanden. Für queued/parallel lässt sich die maximale Anzahl festlegen. Drei Beispiele zeigen Licht, Batterie und Abendlicht.

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
- **Shadow-Zahlen:** Grenzen und Wartezeiten haben editierbare Standardwerte. Ein herausgezogener Zahlenblock kann sie ersetzen. Wird dieser entfernt, erscheint der Standardwert wieder. Sensorwerte, Text- und Entitäts-Wertblocks sind noch nicht umgesetzt.
- **Kontextmenü:** Rechtsklick beziehungsweise langes Drücken bietet die Blockly-Funktionen, etwa Duplizieren, Kommentar, Einklappen, Deaktivieren, Löschen und Hilfe. Hilfe führt hierher. Kommentare bleiben im JSON-Projekt; sie werden noch nicht als YAML-Kommentare exportiert.
- **Deaktivieren:** Deaktivierte Aktionen und Auslöser werden beim Export übersprungen. Deaktivierte Bedingungen werden ausgelassen. Pflichtinhalte bleiben erforderlich; fehlende Auslöser, leere Falls-Bedingungen oder leere Aktionszweige verhindern den Export.
- **Papierkorb:** Blocks löschen, den Papierkorb öffnen und gelöschte Blocks zurück auf die Arbeitsfläche ziehen. Der Verlauf ist auf die aktuelle Sitzung begrenzt. Rückgängig/Wiederholen steht zusätzlich bereit.
- **Einfügemarkierung:** Blockly zeigt beim Ziehen die mögliche Andockposition an.

Projektdateien aus Version 0.1.4 und früher werden automatisch auf die neue Anschlussstruktur umgestellt. Alte Bedingungsketten werden als UND-Gruppen mit derselben YAML-Bedeutung erhalten. Die bestehenden YAML-Dateien bleiben importierbar.

## Blockly-Bibliothek und verbindlicher Entwicklungsstand

Wir verwenden bereits **Blockly 13.3.0**, die originale Bibliothek, statt eine eigene Block-Engine zu entwickeln. Blockly übernimmt Arbeitsfläche, Kategorie-Toolbox und Flyouts, Verbindungen mit Typprüfung, Shadow-Blocks, Mutatoren, Kontextmenü, Zoom, Papierkorb und Einfügemarkierungen. Unsere HA-Blocks, Strukturvalidierung, Projektmigration und der YAML-Generator sind eigener UGSo-Code. Es wird kein ioBroker-JavaScript ausgeführt.

Die [Originaldokumentation zur Arbeitsfläche und zu Blockteilen](https://docs.blockly.com/guides/get-started/workspace-anatomy/) und die [Blockly-Beispiele](https://raspberrypifoundation.github.io/blockly-samples/) dienen als Referenz für vertraute Bedienmuster. Bibliotheksupdates werden bewusst mit Verbindungs-, Import-/Export- und Browserprüfungen übernommen.

| Aufgabe | Stand in 0.1.5 / nächster Schritt |
| --- | --- |
| Anschlussgeometrie und Typprüfung | Boolean-Bedingungen und Number-Werte seitlich; Auslöser/Aktionen als getrennte Statement-Ketten umgesetzt |
| Erweiterbare Blocks | Falls und UND/ODER/NICHT umgesetzt; Aktionsdaten später als visuelle Felder |
| Standardwerte | Shadow-Zahlen umgesetzt; Text- und Entitäts-Wertblocks offen |
| Sensorwerte und Attribute | Offen; passende HA-Template-Ausgabe und Typumwandlung mitplanen |
| Editorbedienung | Kontextmenü, Hilfe, Deaktivieren, Papierkorb-Wiederherstellung, Zoom und Einfügemarkierung vorhanden |
| Kommentare | Im Projekt erhalten; YAML-Kommentare und eigener Kommentarblock offen |
| Menü und Blockfarben | Dunkles Kategorienmenü, helle Blockauswahl, getrennte Gruppenfarben umgesetzt |
| ioBroker-Kategorien | Schrittweise prüfen, zunächst System; Gegenüberstellung bei jeder Funktion aktualisieren |
| Veröffentlichung und Updates | Jede neue HA-App von Anfang an im gemeinsamen Repository mit installierbarem Paket; Paket- und Oberflächenversion gemeinsam anheben |
| HA-Verbindung, Katalog und Plugins | Offen; verwaltete Verbindung und deklarative Erweiterungen vorgesehen |

Diese Seite hält umgesetzte Funktionen und offene Aufgaben zusammen fest und wird mit jeder Erweiterung gepflegt.

## System: Stand und nächste Schritte

Steuern, Umschalten, Wartezeit und generische Aktionen sind vorhanden. Eigene Blocks für Kommentar, Debug, Entitätsauswahl, Zustand/Attribute als Werte, Existenz/Verfügbarkeit, Helfer und Script-Steuerung folgen schrittweise. ioBroker-`ack`, Adapterinstanzen und Datenpunkt-Erzeugung haben kein direktes HA-Gegenstück.

Die vollständige [Gegenüberstellung mit Umsetzungsstatus](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/blocks_for_ha/docs/iobroker-comparison.de.md) wird bei jeder Erweiterung aktualisiert. Katalog und deklarative Plugins sind geplant.

## Prüfung und Original

Der Editor prüft die unterstützte Struktur. Entitäts-IDs werden derzeit eingegeben; installierte Aktionen und echte HA-Ausführung sind damit nicht verifiziert. Vor Verwendung Beispiel-Entitäten ersetzen und Aktionen in HA prüfen. Der Editor schreibt keine HA-Systemdateien.

Built with [Blockly](https://www.blockly.com/). Eigene HA-Blocks, kein ioBroker-Fork. Eigener Code und Blockly: Apache-2.0; YAML-Bibliothek: ISC. Lizenztexte werden mitgeliefert.
