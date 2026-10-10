---
title: Konvertierung
description: Werte umwandeln, Datum und JSON mit ioBroker-Gegenüberstellung.
---
# Konvertierung

Seit **0.1.12** bietet die Kategorie neun neue Blocks. [Alle Konvertierungs-Blocks mit Bildern](./blocks#konvertierung-seit-0-1-12). Grundlage der Bedienung sind die [ioBroker-Konvertierungsblocks](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_convert.ts). Die Blocks verwenden die originale Blockly-Library mit einer eigenen UGSo-Übersetzung in HA-Jinja. Die Umwandlung findet erst bei Ausführung in Home Assistant statt.

## ioBroker / UGSo Blocks für HA

| ioBroker | Unser Block | Verhalten / Unterschied |
| --- | --- | --- |
| nach Zahl | **Nach Zahl** | HA `float`: konvertiert einen vollständigen Zahlenwert. `21.5` funktioniert; `21W` und Dezimalkomma nicht. Anders als `parseFloat` wird kein Zahlenpräfix herausgelöst. |
| nach Logikwert | **Nach Logikwert** | HA `bool`: Boolean oder erkannte Werte wie true/false, on/off, yes/no und 1/0. Unbekannte Texte sind kein automatisch wahrer Wert. |
| nach String | **Nach String** | Jinja-Textdarstellung. Boolean ergibt beispielsweise `True`/`False`; Objekte erhalten keine garantierte JSON-Darstellung. |
| Typ von | **Typ von** | HA `typeof`, ab HA 2023.4. Liefert Python-Typnamen wie str, int, float, bool, dict, list und NoneType statt JavaScript-Typnamen. |
| nach Datum/Zeit | **Nach Datum/Zeit** | ISO-Text oder ausdrücklich gewählte Unix-Sekunden/-Millisekunden → Datumswert in HA-Ortszeit. ISO mit Z oder Offset verwenden. |
| Datum/Zeit nach … | **Datum/Zeit nach …** | Datumswert, ISO/Uhrzeit/Datum, Unix-Zahl, Jahr/Monat/Tag/Stunde/Minute/Sekunde/Millisekunde, Wochentag, Kalenderwoche oder Zeit seit Mitternacht. Eigenes Format blendet ein zusätzliches Textfeld ein. |
| Zeitdifferenz formatieren | **Zeitdifferenz formatieren** | Numerische Dauer in Millisekunden (Standard) oder Sekunden. Formate hh:mm:ss, hh:mm, mm:ss. Negative Dauer behält das Vorzeichen; große Stunden/Minuten laufen nicht bei 24/60 über. |
| JSON nach Objekt | **JSON nach Wert** | `from_json`, auch Listen und Einzelwerte. Ungültiges JSON erzeugt einen Template-Fehler; kein stilles leeres Ersatzobjekt. |
| Objekt nach JSON, formatieren | **Wert nach JSON, formatieren** | `to_json`, mit Checkbox für Einrückung. Nur JSON-serialisierbare Werte; Datumswerte vorher in ISO oder Unix-Zahl umwandeln. |
| JSONata Ausdruck anwenden auf | **Noch offen** | Kein JSONata-Laufzeitadapter im Editor. Eigene HA-Templates können bereits Jinja-Zugriffe auf Objekt-/Listenwerte enthalten. Eine echte JSONata-Integration muss auch bei späterer HA-Ausführung vorhanden sein. |

Referenzen für die HA-Regeln: [float](https://www.home-assistant.io/template-functions/float/), [bool](https://www.home-assistant.io/template-functions/bool/), [typeof](https://www.home-assistant.io/template-functions/typeof/), [from_json](https://www.home-assistant.io/template-functions/from_json/), [to_json](https://www.home-assistant.io/template-functions/to_json/).

## Anschlüsse und Formatfelder

Boolean passt in Bedingungen und Logik. Konvertierte Zahlen sind **Laufzeitzahlen**: Sie passen in Wertvergleiche, Variablen, Dauerformatierung sowie Betrag/Offset der Zeit-Blocks. Feste numeric-state-Grenzen, Wartezeiten und Erhöhen-Schritte verlangen weiterhin konstante Number-Blocks. Dort lassen sich Laufzeitzahlen nicht versehentlich andocken. Dynamische HA-Konfiguration für diese Felder ist noch nicht implementiert.

Datumswerte verwenden den Time-Anschluss. Beim Block **Datum/Zeit nach …** bestimmt die Auswahl den Ausgang: Datumswert, Laufzeitzahl oder Text. Das eigene Format verwendet Python-`strftime` mit `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`. ioBroker-Formatcodes wie `YYYY` sind nicht austauschbar. Sprachabhängige Monats-/Wochentagsnamen, weitere Dauerformate und eine eigene Dauermaske sind noch nicht übernommen. Wochentag zählt Montag=1 bis Sonntag=7; die Kalenderwoche folgt ISO. Sekundenbruchteile einer Dauer werden abgeschnitten, nicht gerundet.

## Beispiele

Sensor-Text in Zahl wandeln und mit 20 vergleichen: Template-Wert mit Sensorzustand → Nach Zahl → Vergleich. Die HA-Ausgabe enthält:

```jinja
{{ (float((states('sensor.temperatur'))) > 20) }}
```

JSON-Text → JSON nach Wert → Wert nach JSON (formatieren):

```jinja
{{ (('{"wert":21.5}' | from_json) | to_json(pretty_print=true)) }}
```

Eine Zeitdifferenz von `3661000` Millisekunden wird zu `01:01:01`; `-3661000` zu `-01:01:01`. Millisekunden und Sekunden ausdrücklich unterscheiden. Der Block formatiert eine bereits vorliegende Dauer; er berechnet nicht automatisch die Differenz zweier Datumswerte.

## Fehler, Speichern und offene Erweiterung

Die Blocks vergeben keine stillen Standardwerte bei ungültiger Zahl, Boolean oder JSON. Wer einen Ersatzwert benötigt, kann ihn bewusst im allgemeinen HA-Template festlegen. HA-Variablen können Template-Ergebnisse als native Werte interpretieren; ein String-Anschluss ist eine Editor-Typinformation, keine Garantie gegen HA-eigene Typinterpretation beim Speichern eines Ergebnisses.

JSON-Projekte erhalten Blockformen, Checkboxen und das eigene Format. Beim YAML-Öffnen werden diese Ausdrücke als allgemeine Template-Blocks erhalten. Konvertierungen in einer Variablen-Aktion können zur Laufzeit Objekte/Listen erzeugen; direkt als YAML gespeicherte Objekt-/Listen-Variablen sind weiterhin nicht importierbar. Die allgemeine HA-Aktion erwartet derzeit statische JSON-Aktionsdaten; Konvertierungs-Blocks lassen sich dort noch nicht direkt einstecken.

**Vorgemerkt:** Objekt-/Listen-Zugriffe erweitern und danach optionalen JSONata-Runtimeadapter prüfen. Eine reine Browser-Auswertung würde das Verhalten einer später in HA laufenden Automation nicht abbilden.

Geprüft sind Blockly-/YAML-Rundläufe, Anschlusschecks und Jinja-Auswertung mit nachgebildeten HA-Helferfunktionen. Eine Ausführung auf einem echten HA-System ist noch nicht verifiziert.
