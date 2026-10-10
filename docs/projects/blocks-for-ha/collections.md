---
title: Mathematik, Text, Listen und Schleifen
description: Vergleich der Blockly- und ioBroker-Blocks mit der nativen HA-Ausgabe von UGSo.
---
# Mathematik, Text, Listen und Schleifen

**Seit 0.1.14:** 37 zusätzliche Blocktypen, insgesamt **105**. [Alle Blocks mit echten Editorbildern](./blocks). Die beiden Textbilder der Vorlage zeigen dieselbe Kategorie und werden einmal berücksichtigt. Es entstehen eigene HA-YAML-/Jinja-Ausgaben; ioBroker-JavaScript wird nicht ausgeführt.

## Abgleich mit den Originalen

Referenzen: originaler Blockly-Quellumfang für [Schleifen](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts), [Mathematik](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/math.ts), [Text](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/text.ts) und [Listen](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). Die ioBroker-Ergänzungen für [Nachkommastellen](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_number.ts) und [Text](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_text.ts) wurden ebenfalls geprüft. Grundlage der Zielausgabe sind die [HA-Templatefunktionen](https://www.home-assistant.io/template-functions/) und [HA-Scriptaktionen](https://www.home-assistant.io/docs/scripts/).

| Bereich / Original | UGSo-Umsetzung | Unterschiede / offene Varianten |
| --- | --- | --- |
| Wiederholen, solange/bis | Vorhandene native HA-repeat-Blocks | Solange prüft vorher, bis nachher. |
| Zählen von/bis/Schritt | Neuer Zählschleifenblock | Feste ganze Grenzen, Schrittbetrag, inklusive Ende auf dem Raster, automatisch auf-/absteigend, höchstens 10000 Werte. Dynamische oder gebrochene Grenzen bleiben offen. |
| Für jeden Wert aus Liste | Zusätzlich mit benannter Variable | Vor jedem Aktionskörper wird die Variable aus repeat.item gesetzt. |
| break / continue | Noch offen | HA Stop beendet den gesamten Lauf. Eine korrekte lokale Umsetzung braucht zusätzliches Kontrollflussmodell und Tests verschachtelter Schleifen. |
| Zahl, Variable erhöhen | Bereits vorhanden | Variablen erst initialisieren; Erhöhen verlangt Zahl. |
| Arithmetik, Einzelfunktionen, Trigonometrie, Konstanten | Neue Mathematik-Kategorie | Wurzel, Betrag, Negation, ln/log10, Potenzen; Winkel in Grad. Unendlich wird nicht angeboten. |
| Zahleneigenschaften | Gerade, ungerade, ganzzahlig, positiv, negativ, teilbar | Primzahlprüfung bleibt offen. |
| Runden / ioBroker-Nachkommastellen | Ein gemeinsamer Block, normal/auf/ab, 0–10 Stellen | HA/Jinja-Rundung statt JavaScript Math.round. |
| Mathematik über Liste | Summe, min/max, Mittelwert, Median, Zufallseintrag | Blockly-Modalwert als Liste aller häufigsten Werte und Standardabweichung bleiben offen; HA statistical_mode allein wäre nicht dieselbe Funktion. |
| Modulo, Begrenzen, Zufall | Neue Wertblocks | Modulo bei negativen Zahlen folgt Jinja. Ganzzahliger Zufall hat inklusive Grenzen; maximal 10000 Möglichkeiten. Zufallsbruch hat Raster 0,00001. |
| atan2 | Zusätzlich aus Original-Blockly übernommen | In den gelieferten Mathematikbildern nicht sichtbar; nicht als ioBroker-Defizit gewertet. |
| Ein-/mehrzeiliger Text | Vorhandener Textblock | Originales Multiline-Feld. |
| Zeilenumbruch, Zusammenfügen, Anhängen | Neue Textblocks | LF/CRLF/CR; Zusammenfügen mit Zahnrad/+−; Anhängen weist eine neue Textvariable zu. |
| Textlänge/leer/enthält/suchen/Zeichen/Teiltext | Neue Textblocks | Indizes ab 1, Suchergebnis 0 bei nicht gefunden. Bereichsgrenzen von Anfang einschließlich Ende; Teiltext vom Ende bleibt offen. |
| Groß-/Klein-/Titelbuchstaben, trim, zählen, ersetzen, umkehren | Neue Textblocks | Literal statt Regex; Unicode-/Python-Regeln. Textumkehr ist zusätzlich im originalen Blockly-Umfang. |
| print / prompt | Log-Aktion vorhanden; prompt offen | Ein Dialog im Browser wäre kein Eingabedialog für die später ausgeführte HA-Automation. |
| Leere Liste / Liste mit Einträgen | Vorhandener Listenblock mit 0–100 Eingängen | Zahnrad/+− verändert Einträge. |
| Liste wiederholen, Länge/leer, Index, lesen, Teilliste | Vorhandene und neue Listenblocks | Lesen vom Anfang/Ende/erstes/letztes/zufällig. Teilliste einschließlich Ende vom Anfang. |
| Liste ändern / einfügen / entfernen | Neue Aktionsblocks | Neue Liste in ausgewählter Variable; keine Mutation anderer Variablen. Lesen-und-Entfernen als kombinierter Wertblock, Änderung vom Ende und zufälliges Entfernen bleiben offen. |
| Split/join, sortieren, umkehren | Neue Listenblocks | Numerisch/Text/Text ohne Groß-/Kleinschreibung; Original bleibt erhalten. |

## Bedienung und Laufzeitwerte

Menü, heller Flyout und farbige Blocks bleiben klar getrennt; **Suchen steht ganz am Ende**. Mathematik ist blauviolett, Text dunkelgrün, Listen violett und Schleifen grün. Werte lassen sich in Variablen, Vergleiche, Templates und Laufzeitpausen stecken. Feste numerische Trigger-Grenzen akzeptieren weiterhin nur Zahlenblöcke, keine berechneten Templates.

Textverknüpfung besitzt 0–100 Eingänge. Variable erstellen bleibt in der Variablen-Kategorie; Text- und Listenänderungen wählen diese Variable aus. Vor Anhängen/Ändern muss sie den passenden Typ enthalten. Eine aus HA gelesene Zustandszeichenfolge bei Bedarf ausdrücklich mit dem Konvertierungsblock in eine Zahl wandeln. Ungültige Typen oder Indizes mit Nachkommastellen erzeugen Templatefehler statt stiller Konvertierung.

Index **1** bezeichnet das erste Element. Vom Ende zählt 1 das letzte. Beim Lesen liefert ein Index außerhalb des Bereichs leeren Text beziehungsweise null; bei Listenänderungen bleibt die Liste unverändert. Einfügen an Länge+1 hängt an. Bei Teilbereichen ergibt Start größer als Ende oder Start kleiner als 1 einen leeren Wert. Eine Endgrenze jenseits der Länge wird abgeschnitten.

Beispiel: Zähle `i` von 1 bis 5 in Schritten von 2, protokolliere im Körper einen Template-Wert mit `i`:

```yaml
actions:
  - repeat:
      for_each: '{{ range(1, 6, 2) | list }}'
      sequence:
        - variables:
            i: '{{ repeat.item }}'
        - action: system_log.write
          data:
            level: info
            message: '{{ i }}'
```

Das ergibt 1, 3, 5. Verschachtelte Schleifen sollten unterschiedliche Variablennamen verwenden; repeat.item bezeichnet jeweils den innersten Durchlauf. Wiederholte Zufalls-/zeitabhängige Ausdrücke zuerst in eine Variable speichern, wenn derselbe Wert an mehreren Stellen gebraucht wird: verschachtelte Templates können Eingänge mehrfach auswerten.

## Unterschiede zu JavaScript und Speicherung

- Bei 0 Nachkommastellen wird 2,5 zu 2 und 3,5 zu 4; JavaScript Math.round verhält sich anders. Auf-/Abrunden verwendet ceil/floor.
- Negatives Modulo: −9 modulo 2 ergibt 1. Winkel werden zwischen Grad und HA-Radiant umgerechnet.
- Textoperationen verwenden Unicode-Codepunkte. Ein Emoji kann in JavaScript zwei UTF-16-Einheiten haben; kombinierte Zeichen/Grapheme sind weiterhin mehrere Codepunkte. Titelbuchstaben und trim folgen Python/Jinja.
- Leerer Suchtext wird bei Zählen/Ersetzen ausdrücklich als 0/unveränderter Text behandelt. Treffer überlappen nicht. Suche ist wörtlich und unterscheidet Groß-/Kleinschreibung.
- Leere Liste: Summe 0, andere Mathematik-Aggregate und Zufallseintrag null. Numerische Aggregation/Sortierung verlangt echte Zahlen, keine Boolean- oder Textwerte. Python-Gleichheit kann beim Suchen 1 und wahr als gleich behandeln und unterscheidet sich von JavaScript-Referenzgleichheit.
- Listenänderungen erzeugen Kopien durch Slices und neue HA-Variablenzuweisung. Keine list.append-/pop-Mutation in der unveränderlichen HA-Sandbox.

Projekt-JSON behält Blockformen, Felder, Dropdowns, Reihenfolge und verknüpfte Einträge. YAML-Import erhält die Bedeutung, öffnet komplexe Wertausdrücke als allgemeine Templates und Zählschleifen als native Für-jeden-Schleife mit Variablenzuweisung. YAML enthält keine Informationen, aus denen sich die ursprünglichen Blockly-Formen eindeutig rekonstruieren lassen.

Geprüft: alle 37 neuen Blocktypen durch JSON/YAML, Grenzfälle, unveränderliche Jinja-Sandbox mit HA-Mathematik-Helfern, Kategorien und Text-Plus-Button im Browser, App-/Dokumentationsbuild und Docker-Vorschau. Die Ausführung in einer echten Home-Assistant-Instanz steht noch aus.
