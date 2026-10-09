---
title: UGSo Blocks for HA
description: Native Home-Assistant-Automationen mit visuellen Blocks erstellen.
---
# UGSo Blocks for HA

**Version 0.1.2 · lokaler Prototyp.** Mit visuellen Blocks entstehen native Home-Assistant-Automationen. Der Editor erzeugt YAML; Home Assistant übernimmt die Ausführung. Eine Live-HA-Verbindung und ein installierbares HA-Add-on sind noch geplant.

## Start und Dateien

Der Code liegt neben Grafik Visual Studio im [gemeinsamen Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha). Im Ordner `blocks_for_ha` mit Node.js 22.12 oder neuer:

```sh
npm install
npm run dev
```

Editor: `http://127.0.0.1:4180/`. YAML kann angezeigt, kopiert, als Datei gespeichert und wieder als Blocks geöffnet werden. Unterstützt wird eine Automation als Objekt oder Liste mit einem Eintrag. Nicht unterstützte Strukturen werden zurückgewiesen. JSON-Projekte erhalten zusätzlich Blockpositionen; der Browser sichert den letzten Stand lokal.

## ioBroker / unsere Blocks: vorhandene Funktionen

13 Blocktypen einschließlich des Automationsrahmens:

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

Name, Beschreibung, ID und Ausführungsmodi `single`, `restart`, `queued`, `parallel` sind vorhanden. Für queued/parallel lässt sich die maximale Anzahl festlegen. Drei Beispiele zeigen Licht, Batterie und Abendlicht.

## Zahnrad: Falls erweitern

Wie beim vertrauten ioBroker-Editor öffnet das Zahnrad eine kleine Arbeitsfläche. Dort lassen sich **sonst falls**-Elemente an den Falls-Rahmen anhängen und ein optionaler **sonst**-Zweig ergänzen. Die jeweiligen Bedingungen und Aktionen werden anschließend im Hauptblock eingesteckt.

- Ein Falls-Zweig erzeugt `if`/`then`, optional `else`.
- Mehrere Zweige erzeugen `choose`, der Sonst-Zweig wird `default`.
- HA führt den ersten passenden Zweig aus. Weitere passende Zweige werden nicht ausgeführt.
- Entfernte Zweige lösen ihre verbundenen Blocks ab. Diese müssen wieder verbunden oder entfernt werden, bevor exportiert werden kann.
- YAML-Import und JSON-Projekte erhalten die Verzweigungen. Alte Projekte behalten ihre bisherigen Sonst-Aktionen.

UND/ODER/NICHT unterstützt bereits mehrere angehängte Bedingungen. Auslöser und Aktionen lassen sich ebenfalls als Ketten erweitern. Ein zusätzlicher Mutator ist dort nicht nötig. Zahlen-, Sonnen- und Schaltblocks bieten ihre Auswahl direkt im Dropdown. Die generische HA-Aktion verwendet zunächst JSON-Daten; ein visueller Datenfeld-Mutator ist noch geplant.

## System: Stand und nächste Schritte

Steuern, Umschalten, Wartezeit und generische Aktionen sind vorhanden. Eigene Blocks für Kommentar, Debug, Entitätsauswahl, Zustand/Attribute als Werte, Existenz/Verfügbarkeit, Helfer und Script-Steuerung folgen schrittweise. ioBroker-`ack`, Adapterinstanzen und Datenpunkt-Erzeugung haben kein direktes HA-Gegenstück.

Die vollständige [Gegenüberstellung mit Umsetzungsstatus](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/blocks_for_ha/docs/iobroker-comparison.de.md) wird bei jeder Erweiterung aktualisiert. Katalog und deklarative Plugins sind geplant.

## Prüfung und Original

Der Editor prüft die unterstützte Struktur. Entitäts-IDs werden derzeit eingegeben; installierte Aktionen und echte HA-Ausführung sind damit nicht verifiziert. Vor Verwendung Beispiel-Entitäten ersetzen und Aktionen in HA prüfen. Der Editor schreibt keine HA-Systemdateien.

Built with [Blockly](https://www.blockly.com/). Eigene HA-Blocks, kein ioBroker-Fork. Eigener Code und Blockly: Apache-2.0; YAML-Bibliothek: ISC. Lizenztexte werden mitgeliefert.
