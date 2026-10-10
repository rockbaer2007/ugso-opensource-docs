---
title: Timeouts, Objekt, Logik und Schleifen
description: ioBroker, Original-Blockly und native HA-Abläufe gegenübergestellt.
---
# Timeouts, Objekt, Logik und Schleifen

Diese Seite beschreibt die 18 Ergänzungen von 0.1.13 (damals 68 Blocktypen). Aktuell sind es **105** mit den weiteren [Mathematik-, Text-, Listen- und Schleifenblocks aus 0.1.14](./collections).

Seit **0.1.13** ergänzen 18 neue Blocks den Editor, insgesamt **68 Blocktypen**. [Bilder und Funktionen aller Blocks](./blocks#ablaufe-objekte-und-listen-seit-0-1-13). Grundlage sind die tatsächlichen [Timeout-](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_timeout.ts), [Objekt-](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_object.ts), [Logik-](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_logic.ts) und [Switch-Blocks](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_switch.ts) des ioBroker-JavaScript-Adapters. Die folgende Zuordnung erklärt Ähnlichkeiten und Grenzen; ioBroker-JavaScript wird nicht importiert.

## Timeouts

| ioBroker | UGSo Blocks für HA | Unterschied |
| --- | --- | --- |
| Pause, Einheit ms/sec/min | **Pause** mit ms/Sekunden/Minuten/Stunden und andockbarem Wert | Native HA-delay. Der aktuelle Ablauf wartet; keine Blockierung des Browsers. |
| Ausführen timeout in …, feste/variable Dauer | **Pause**, anschließend Aktionen | HA führt die folgenden Schritte nacheinander aus. Kein unabhängig laufender Callback und kein benannter Timeout-Handle. |
| Stop timeout | **HA-Script stoppen** für ein separat gestartetes Script; **Diesen Lauf stoppen** für den aktuellen Lauf | Stop beendet den gesamten aktuellen Lauf. Keine selektive Löschung eines ioBroker-Timeouts. |
| Verzögerung als Handle | Kein Handle-Block | HA-Scripts oder Timer-Helfer über System/Aktionen verwenden. Ein Timer-Helfer startet keinen eingebetteten Callback. |
| Ausführen Intervall alle … | **Wiederhole solange/bis** und **Pause** im Körper | Sequentielle Wiederholung: Aktionsdauer plus Pause bestimmt den Abstand. Kein setInterval und keine parallelen überlappenden Ticks. |
| Stop zyklische Ausführung | Schleifenbedingung ändern oder separates HA-Script stoppen | **Diesen Lauf stoppen** stoppt auch äußere Schleifen; entspricht keinem lokalen break. |
| Intervall als Handle | Kein Handle-Block | Separat gestartete Scripts können über script.turn_off beendet werden. |
| Zusätzlich in UGSo | **Warte bis**, begrenzte Wiederholung, Für jeden Eintrag | Native HA-Steuerung einschließlich Timeout-Haken und Laufabbruch als Fehler. |

**Warte bis** verwendet HA wait_template und einen verpflichtenden Timeout. Ohne „bei Timeout weiter“ endet der Lauf, sobald die Frist abläuft. Mit Haken folgen die nächsten Aktionen auch bei nicht erfüllter Bedingung. Entitätsabhängige Bedingungen verwenden: reine Zeit-/now()-Templates werden während wait_template nicht kontinuierlich neu ausgewertet. HA stellt danach wait.completed bereit, nutzbar im Template-Block. [HA-Warten und Wiederholungen](https://www.home-assistant.io/docs/scripts/).

**Solange** prüft vor jedem Durchlauf; **bis** prüft danach und führt den Körper mindestens einmal aus. Eine Pause im Körper verhindert eine enge Dauerschleife. Millisekunden sind Mindestverzögerungen, keine Echtzeitgarantie. Ein HA-Neustart beendet laufende delays/waits; für persistente Zeitplanung separate Timer-/Auslöser-Strategien einsetzen. [Timer-Helfer](https://www.home-assistant.io/integrations/timer/).

Konstante Dauer: 0–86400 Sekunden mit expliziter Einheit. Konstante Wiederholungsanzahl: 1–10000 ganze Durchläufe. Andockbare Variablen und Templates müssen gültige Laufzeitzahlen liefern; Prüfung und mögliche Fehler erfolgen in HA. Die Grenzen für Konstanten sind Editorgrenzen, keine garantierten Laufzeitlimits für Templates.

## Objekt

| ioBroker | UGSo Block | Verhalten |
| --- | --- | --- |
| Neues Objekt mit Zahnrad | **Neues Objekt** mit Zahnrad und +/− | 0–100 Attribute, eindeutige frei benannte Schlüssel, beliebige Werte einschließlich verschachtelter Objekte/Listen. |
| Setze Attribut des Objekts auf Wert | **Setze Attribut in Variable auf** | Neue HA-Variablenzuweisung an eine vorher gesetzte Objektvariable. Andere Variablenkopien bleiben unverändert. |
| Entferne Attribut | **Entferne Attribut aus Variable** | Neues Dictionary ohne den Schlüssel; fehlt er, bleibt der Inhalt gleich. |
| Objekt hat Attribut | **Objekt hat Attribut** | Boolean-Test auf einen eigenen Dictionary-Schlüssel. |
| Attribute des Objekts | **Attribute des Objekts** | Liste der Schlüssel, für die Für-jeden-Eintrag-Schleife verwendbar. |
| Attribut lesen, in ioBroker unter System | **Attribut von Objekt** | Schlüsselzugriff statt unsicherem Punktzugriff; fehlender Schlüssel ergibt null. Auch Namen wie keys/items funktionieren. |

Diese Objekte sind lokale Werte eines Automationslaufs. Sie erzeugen keine Entitäten, verändern keine HA-Entity-Attribute und entsprechen nicht ioBroker-Datenpunktdefinitionen. Der Setter verwendet eine Variablenauswahl, damit die neue Zuweisung ein eindeutiges Ziel hat. Die Variable zuvor auf **Neues Objekt**, einen Dictionary-Templatewert oder **JSON nach Objekt** setzen. Ein anderer Typ erzeugt einen HA-Templatefehler.

Die [unveränderliche Jinja-Sandbox](https://jinja.palletsprojects.com/en/stable/sandbox/) erlaubt keine direkte Mutation über update/pop. UGSo erzeugt deshalb Dictionary-Kopien und weist diese neu zu. Keine JavaScript-Objektmutation und kein HA-Systemzugriff.

## Logik und Original-Blockly

Die originalen [Blockly-Logikdefinitionen](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/logic.ts) umfassen Falls/sonst-falls/sonst, feste Falls/sonst-Variante, Vergleich, UND/ODER, NICHT, Boolean, null und bedingte Wertauswahl. Diese Grundfunktionen sind bei UGSo bereits vorhanden: **Falls** unter Aktionen, die Werte unter **Logik**, die erweiterbaren UND/ODER/NICHT-Gruppen unter Bedingungen und zusätzlich Logik. Auswahl und Verbindungsformen stammen von der originalen Blockly-Library; HA-YAML/Jinja wird von UGSo erzeugt.

| ioBroker-Erweiterung | UGSo | Semantik |
| --- | --- | --- |
| UND/ODER mit Zahnrad | Bestehende erweiterbare Gruppe, auch unter Logik | 1–100 Boolean-Eingänge; +/− und Zahnrad zum Umordnen. |
| der Fall ist / im Falle von / machen | **Der Fall ist** | 1–100 Fälle mit +/− und Zahnrad, optional belegter sonst-Körper. Erste Übereinstimmung gewinnt; kein JavaScript-Fallthrough. |
| min ≤ wert ≤ max | **Bereichsvergleich** | Beide Grenzen separat strikt oder einschließlich. Keine automatische Text-in-Zahl-Konvertierung; **Nach Zahl** bei Sensor-/Templatewerten einsetzen. |
| wenn leer … dann … | **Ersatzwert** mit Modusauswahl | Standard null/nicht gesetzt erhält 0/falsch/leeren Text. „leer/falsch/0“ ersetzt auch leere Listen und Dictionaries. |

ioBroker verwendet beim Ersatzwert JavaScript-ODER: leere Arrays/Objekte sind dort wahr. Jinja/Python behandelt diese als falsch. Der zusätzliche Null-Modus verhindert, dass gültige Zahlen/Boolean versehentlich ersetzt werden. Nicht verfügbare Sensorzustände wie unknown/unavailable sind Texte; sie sind keine null-Werte und werden nicht automatisch ersetzt.

Fallvergleiche verwenden HA/Jinja-Gleichheit; Boolean und Zahlen können sich anders verhalten als beim JavaScript-switch. Der Testausdruck wird pro geprüftem HA-Zweig ausgewertet. Wechselnde Werte vorher in einer Variablen speichern und diese als Fallwert einsetzen, wenn alle Fälle denselben Schnappschuss vergleichen sollen.

## Schleifen und Listen

Aus dem originalen [Blockly-Schleifenumfang](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts) sind jetzt **Wiederhole Anzahl**, **solange/bis** und **Für jeden Eintrag** übertragen. **Liste erstellen**, **Listenlänge** und **Liste ist leer** orientieren sich an den [originalen Listenblocks](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). Diese Funktionen gibt es auch in ioBroker-Kategorien außerhalb der drei gezeigten Menüs; sie werden nicht als ausschließliches ioBroker-Defizit dargestellt.

Liste erstellen unterstützt 0–100 beliebige Einträge mit Zahnrad/+−. Für jeden Eintrag erwartet eine Liste; aktueller Wert und 1-basierter Index stehen als HA repeat.item und repeat.index im Template-Block zur Verfügung. Länge/Leer prüfen echte Listen statt Text oder Dictionaries. Jinja kann daraus Laufzeitfehler melden, wenn der Eingang einen anderen Typ liefert.

```yaml
actions:
  - variables:
      daten: '{{ {"attribute1": "alt"} }}'
  - variables:
      daten: '{{ dict((daten if daten is mapping else none), **{"attribute1": "neu"}) }}'
  - repeat:
      count: 3
      sequence:
        - delay:
            milliseconds: 1000
        - action: system_log.write
          data:
            message: '{{ repeat.index }}'
            level: info
```

## Speicherung und offene Funktionen

Projekt-JSON bewahrt Blockformen, Reihenfolge und Attributnamen. YAML öffnet Pausen, waits, Stop und Wiederholungen direkt als entsprechende Blocks. Fallauswahl öffnet als bestehender Falls/choose-Block; komplexe Objekt-/Listen-/Logikwerte öffnen als allgemeine Templates. Das YAML-Verhalten bleibt erhalten, die ursprüngliche Form lässt sich daraus nicht eindeutig rekonstruieren. Gemischte Dauermappings, rohe for_each-Listen und zusätzliche HA-Optionsfelder sind noch nicht unterstützt und werden beim Import abgelehnt, statt still entfernt zu werden.

Vorgemerkt: benannte persistente Timer mit timer.finished-Auslöser, periodische HA-Auslöser, parallele Zweige und lokale break/continue-Semantik. Feste ganzzahlige Zählschleifen und Listenbearbeitung sind seit [0.1.14](./collections) ergänzt. **Diesen Lauf stoppen** wird ausdrücklich nicht als break/continue ausgegeben. Eigene Entitätszustands-/Attribut-Wertblocks bleiben getrennte Aufgaben. Der Original-Blockly-Grundumfang enthält selbst keine ioBroker-Timeout-Engine und keine entsprechenden ioBroker-Objektblocks; das sind Erweiterungen des Adapters.

Verifiziert: Modell-/YAML-/Projekt-Rundläufe, Eingabefehler, unveränderliche Jinja-Sandbox mit Laufzeitwerten sowie Browserbedienung, Mutator und Undo. Ein Test gegen eine echte HA-Instanz ist noch offen.
