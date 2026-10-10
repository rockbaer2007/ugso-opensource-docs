---
title: Liste der Blocks
description: Alle UGSo Blocks für HA mit Bild, Funktion und Originalplugins.
---

# Liste der Blocks

Entitätsfelder öffnen seit 0.1.17 einen Suchdialog. [Entitäten laden, auswählen und manuell eingeben](./entities). Der aktuelle Katalog enthält 163 Typen.

Stand **0.1.43**: 163 Blocktypen. Die Bilder zeigen die tatsächlichen UGSo-Blocks im Editor. Dropdown-Varianten zählen nicht als zusätzliche Blocktypen. Anleitungen und ioBroker-Gegenüberstellung: [Datum und Zeit](./time), [Konvertierung](./conversion).

Auslöser sind orange, Bedingungen violett, Werte grün und Aktionen blau. Seitliche Anschlüsse sind typisiert; Auslöser und Aktionen bilden getrennte vertikale Ketten. Entitäts-IDs werden gesucht oder manuell eingegeben.

## Farben und Wertfunktionen seit 0.1.15

[Bedienung, HA-Ausgabe und vollständiger Quellenvergleich](./blockly-audit).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Zufällige Farbe**<br><code>ugso_colour_random</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_random.png" alt="Zufällige Farbe" style="max-width:280px;max-height:180px"> | Drei zufällige RGB-Kanäle 0–255. Bei jeder Auswertung neu; nicht kryptografisch. |
| **Farbe aus RGB**<br><code>ugso_colour_rgb</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_rgb.png" alt="Farbe aus RGB" style="max-width:280px;max-height:180px"> | Prozentanteile auf 0–100 begrenzen und in RGB-Kanäle umrechnen. 100/50/0 ergibt [255,128,0]. |
| **Farben mischen**<br><code>ugso_colour_blend</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_blend.png" alt="Farben mischen" style="max-width:280px;max-height:180px"> | Lineare RGB-Mischung. Anteil Farbe 2 von 0–1. Rot/Blau bei 0,5 ergibt [128,0,128], ohne Gamma-Korrektur. |
| **Wertfunktion definieren**<br><code>procedures_defreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_defreturn.png" alt="Wertfunktion definieren" style="max-width:280px;max-height:180px"> | Originaler Blockly-Editor, Zahnrad für bis zu acht Parameter, Rückgabewert erforderlich. Keine Aktionen. Jinja-Expansion beim Export. |
| **Wertfunktion aufrufen**<br><code>procedures_callreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_callreturn.png" alt="Wertfunktion aufrufen" style="max-width:280px;max-height:180px"> | Erscheint dynamisch in Funktionen. Argumenteingänge folgen den Parametern. Ergebnis als Wert oder Boolean-Bedingung; keine Rekursion. |
| **Originaler Parameter-Getter**<br><code>variables_get</code> | <img src="/assets/blocks-for-ha/blocks/de/variables_get.png" alt="Originaler Parameter-Getter" style="max-width:280px;max-height:180px"> | Original-Blockly-Getter, etwa aus dem Kontextmenü der Definition. Liest im Funktionskörper den Parameter, sonst eine HA-Variable. Eigener Getter bleibt nutzbar. |

## Mathematik, Text, Listen und Zählschleifen seit 0.1.14

[Original-Blockly / ioBroker / HA: Zuordnung, Beispiele und Grenzen](./collections).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Arithmetik**<br><code>ugso_math_arithmetic</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_arithmetic.png" alt="Arithmetik" style="max-width:280px;max-height:180px"> | Rechnet mit Zahlen: Addition, Subtraktion, Multiplikation, Division oder Potenz. Keine automatische Text-/Boolean-Konvertierung. |
| **Einzelne Zahl berechnen**<br><code>ugso_math_single</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_single.png" alt="Einzelne Zahl berechnen" style="max-width:280px;max-height:180px"> | Wurzel, Betrag, Negation, Logarithmen und Exponentialfunktionen. Ungültige Werte erzeugen einen Templatefehler. |
| **Trigonometrie**<br><code>ugso_math_trig</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_trig.png" alt="Trigonometrie" style="max-width:280px;max-height:180px"> | Winkelfunktionen in Grad; inverse Funktionen liefern Grad. HA verwendet intern Radiant. |
| **Konstanten**<br><code>ugso_math_constant</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_constant.png" alt="Konstanten" style="max-width:280px;max-height:180px"> | Endliche mathematische Konstanten. Unendlich wird nicht als exportierbarer Zahlenwert angeboten. |
| **Zahleneigenschaften**<br><code>ugso_math_property</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_property.png" alt="Zahleneigenschaften" style="max-width:280px;max-height:180px"> | Zahleneigenschaften prüfen. Teiler erscheint nur bei teilbar durch; Nullteiler ist ungültig. |
| **Runden**<br><code>ugso_math_round</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_round.png" alt="Runden" style="max-width:280px;max-height:180px"> | Rundet auf 0–10 Nachkommastellen. HA/Jinja rundet halbe Werte zur geraden Zahl; Auf-/Abrunden folgen ceil/floor. |
| **Mathematik über Liste**<br><code>ugso_math_list</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_list.png" alt="Mathematik über Liste" style="max-width:280px;max-height:180px"> | Statistik über eine Zahlenliste; Zufallseintrag akzeptiert beliebige Listenelemente. Leere Summe ist 0, andere leere Ergebnisse sind null. |
| **Modulo**<br><code>ugso_math_modulo</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_modulo.png" alt="Modulo" style="max-width:280px;max-height:180px"> | Jinja-Modulo. Bei negativem Dividend folgt das Vorzeichen dem Teiler und kann von JavaScript abweichen. |
| **Begrenzen**<br><code>ugso_math_clamp</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_clamp.png" alt="Begrenzen" style="max-width:280px;max-height:180px"> | Begrenzt einen Zahlenwert. Vertauschte Grenzen werden zuerst sortiert. |
| **Ganzzahlige Zufallszahl**<br><code>ugso_math_random_int</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_random_int.png" alt="Ganzzahlige Zufallszahl" style="max-width:280px;max-height:180px"> | Inklusive beider ganzzahliger Grenzen. Höchstens 10000 mögliche Werte, vertauschte Grenzen sind erlaubt. |
| **Zufallsbruch**<br><code>ugso_math_random_fraction</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_random_fraction.png" alt="Zufallsbruch" style="max-width:280px;max-height:180px"> | Zufallswert in Schritten von 0,00001. Kein kryptografischer Zufall; bei jeder Auswertung neu. |
| **Winkel atan2**<br><code>ugso_math_atan2</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_atan2.png" alt="Winkel atan2" style="max-width:280px;max-height:180px"> | Vierquadranten-Winkelfunktion aus dem Blockly-Standard, zusätzlich zu den gezeigten Bildern. |
| **Zeilenumbruch**<br><code>ugso_text_newline</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_newline.png" alt="Zeilenumbruch" style="max-width:280px;max-height:180px"> | Liefert einen echten Zeilenumbruch für Textverknüpfung. |
| **Text verknüpfen**<br><code>ugso_text_join</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_join.png" alt="Text verknüpfen" style="max-width:280px;max-height:180px"> | Verknüpft 0–100 Werte als Text. Zahnrad und +/− ändern die Anzahl der Eingänge. |
| **Text anhängen**<br><code>ugso_text_append</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_append.png" alt="Text anhängen" style="max-width:280px;max-height:180px"> | Weist der vorher initialisierten Textvariable einen neuen Text zu. Kein Schreiben einer HA-Entität. |
| **Textlänge**<br><code>ugso_text_length</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_length.png" alt="Textlänge" style="max-width:280px;max-height:180px"> | Anzahl Unicode-Codepunkte, nicht JavaScript-UTF-16-Codeeinheiten. |
| **Text ist leer**<br><code>ugso_text_empty</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_empty.png" alt="Text ist leer" style="max-width:280px;max-height:180px"> | Prüft einen Text auf Länge 0. |
| **Text enthält**<br><code>ugso_text_contains</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_contains.png" alt="Text enthält" style="max-width:280px;max-height:180px"> | Prüft Teiltext, mit Groß-/Kleinschreibung. |
| **Text suchen**<br><code>ugso_text_index</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_index.png" alt="Text suchen" style="max-width:280px;max-height:180px"> | Position ab 1, nicht gefunden ergibt 0. Unicode-Codepunkte. |
| **Zeichen lesen**<br><code>ugso_text_char</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_char.png" alt="Zeichen lesen" style="max-width:280px;max-height:180px"> | Zeichen ab 1 vom Anfang/Ende, erstes/letztes oder zufälliges Zeichen. Außerhalb ergibt leeren Text. |
| **Teiltext**<br><code>ugso_text_slice</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_slice.png" alt="Teiltext" style="max-width:280px;max-height:180px"> | Inklusive Grenzen ab 1 vom Anfang. Ungültige/umgekehrte Grenzen ergeben leeren Text. |
| **Groß-/Klein-/Titelbuchstaben**<br><code>ugso_text_case</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_case.png" alt="Groß-/Klein-/Titelbuchstaben" style="max-width:280px;max-height:180px"> | Unicode-Text in Groß-, Klein- oder Titelbuchstaben umwandeln. |
| **Leerraum entfernen**<br><code>ugso_text_trim</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_trim.png" alt="Leerraum entfernen" style="max-width:280px;max-height:180px"> | Entfernt äußeren Leerraum einschließlich Tabs und Zeilenumbrüchen. |
| **Text zählen**<br><code>ugso_text_count</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_count.png" alt="Text zählen" style="max-width:280px;max-height:180px"> | Zählt nicht überlappende Treffer; leerer Suchtext ergibt 0. |
| **Text ersetzen**<br><code>ugso_text_replace</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_replace.png" alt="Text ersetzen" style="max-width:280px;max-height:180px"> | Ersetzt alle wörtlichen Treffer, ohne Regex. Leerer Suchtext lässt den Text unverändert. |
| **Text umkehren**<br><code>ugso_text_reverse</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_reverse.png" alt="Text umkehren" style="max-width:280px;max-height:180px"> | Zusätzlicher Blockly-Standardblock. Kehrt Unicode-Codepunkte um, nicht zusammengesetzte Grapheme. |
| **Listenelement wiederholen**<br><code>ugso_list_repeat</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_repeat.png" alt="Listenelement wiederholen" style="max-width:280px;max-height:180px"> | Neue Liste mit 0–10000 Wiederholungen eines Wertes. |
| **Listenelement suchen**<br><code>ugso_list_index</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_index.png" alt="Listenelement suchen" style="max-width:280px;max-height:180px"> | Position ab 1, nicht gefunden ergibt 0. HA/Python-Gleichheit statt JavaScript-Referenzgleichheit. |
| **Listenelement lesen**<br><code>ugso_list_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_get.png" alt="Listenelement lesen" style="max-width:280px;max-height:180px"> | Liest ab 1 vom Anfang/Ende, erstes/letztes oder zufälliges Element. Außerhalb/leere Liste ergibt null. |
| **Listenelement setzen/einfügen**<br><code>ugso_list_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_set.png" alt="Listenelement setzen/einfügen" style="max-width:280px;max-height:180px"> | Weist eine neue Liste mit ersetzt/eingefügtem Wert zu. Index ab 1; Einfügen erlaubt Länge+1. Ungültiger Index lässt die Liste unverändert. |
| **Listenelement entfernen**<br><code>ugso_list_remove</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_remove.png" alt="Listenelement entfernen" style="max-width:280px;max-height:180px"> | Weist eine neue Liste ohne dieses Element zu. Index ab 1, ungültiger Index lässt die Liste unverändert. |
| **Teilliste**<br><code>ugso_list_slice</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_slice.png" alt="Teilliste" style="max-width:280px;max-height:180px"> | Kopie eines Bereichs, inklusive Grenzen ab 1 vom Anfang. Umgekehrte/ungültige Grenzen ergeben eine leere Liste. |
| **Liste/Text teilen/verbinden**<br><code>ugso_list_split</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_split.png" alt="Liste/Text teilen/verbinden" style="max-width:280px;max-height:180px"> | Text anhand eines wörtlichen Trennzeichens teilen oder Liste verbinden. Leeres Trennzeichen teilt in Unicode-Zeichen. |
| **Liste sortieren**<br><code>ugso_list_sort</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_sort.png" alt="Liste sortieren" style="max-width:280px;max-height:180px"> | Neue sortierte Liste; Original bleibt erhalten. Numerischer Modus verlangt Zahlen, Textmodus wandelt Elemente in Text um. |
| **Liste umkehren**<br><code>ugso_list_reverse</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_reverse.png" alt="Liste umkehren" style="max-width:280px;max-height:180px"> | Neue Liste in umgekehrter Reihenfolge; Original bleibt erhalten. |
| **Zählschleife**<br><code>ugso_for_range</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_for_range.png" alt="Zählschleife" style="max-width:280px;max-height:180px"> | Feste ganze Grenzen, inklusive Ende wenn auf dem Schrittraster. Auf-/absteigend automatisch, Schrittbetrag >0, höchstens 10000 Durchläufe. HA repeat.for_each mit Variable pro Durchlauf. |
| **Für jeden Wert mit Variable**<br><code>ugso_foreach_variable</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_foreach_variable.png" alt="Für jeden Wert mit Variable" style="max-width:280px;max-height:180px"> | HA repeat.for_each mit benannter Variable, vor dem Körper aus repeat.item gesetzt. Wiederverwendung derselben Variable in verschachtelten Schleifen vermeiden. |

## Abläufe, Objekte und Listen seit 0.1.13

[ioBroker / Original-Blockly / native HA: Gegenüberstellung und Grenzen](./flow).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Pause**<br><code>ugso_pause</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_pause.png" alt="Pause" style="max-width:280px;max-height:180px"> | Dauer mit ms/Sekunden/Minuten/Stunden; konstante oder berechnete Zahl. Native HA-Wartezeit. |
| **Warte bis**<br><code>ugso_wait</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_wait.png" alt="Warte bis" style="max-width:280px;max-height:180px"> | Boolean-Bedingung mit Timeout und Haken zum Fortsetzen; ohne Haken endet der Lauf bei Timeout. |
| **Diesen Lauf stoppen**<br><code>ugso_stop</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_stop.png" alt="Diesen Lauf stoppen" style="max-width:280px;max-height:180px"> | Grund und optionaler Fehler-Haken. Beendet den gesamten Lauf, auch in Schleifen. |
| **Wiederhole Anzahl**<br><code>ugso_repeat</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_repeat.png" alt="Wiederhole Anzahl" style="max-width:280px;max-height:180px"> | C-Körper für HA-repeat.count; repeat.index ist der 1-basierte Index. |
| **Wiederhole solange/bis**<br><code>ugso_repeat_while</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_repeat_while.png" alt="Wiederhole solange/bis" style="max-width:280px;max-height:180px"> | Boolean-Eingang und Aktionskörper. Solange prüft vorher, bis danach. Pause im Körper verwenden. |
| **Für jeden Eintrag**<br><code>ugso_foreach</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_foreach.png" alt="Für jeden Eintrag" style="max-width:280px;max-height:180px"> | Liste durchlaufen; aktueller Wert über Template repeat.item, Index über repeat.index. |
| **Neues Objekt**<br><code>ugso_object_new</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_new.png" alt="Neues Objekt" style="max-width:280px;max-height:180px"> | 0–100 benannte Attribute mit Zahnrad/+−. Dictionary-Wert, keine HA-Entität. |
| **Attribut von Objekt**<br><code>ugso_object_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_get.png" alt="Attribut von Objekt" style="max-width:280px;max-height:180px"> | Schlüssel lesen; fehlender Schlüssel ergibt null. Dictionary erforderlich. |
| **Objekt hat Attribut**<br><code>ugso_object_has</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_has.png" alt="Objekt hat Attribut" style="max-width:280px;max-height:180px"> | Boolean-Test auf einen Dictionary-Schlüssel. |
| **Attribute des Objekts**<br><code>ugso_object_keys</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_keys.png" alt="Attribute des Objekts" style="max-width:280px;max-height:180px"> | Schlüsselliste für Listen- und Für-jeden-Eintrag-Blocks. |
| **Setze Attribut in Variable**<br><code>ugso_object_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_set.png" alt="Setze Attribut in Variable" style="max-width:280px;max-height:180px"> | Variablenauswahl und Wertanschluss; weist eine Dictionary-Kopie mit geändertem Schlüssel zu. Vorher als Objekt setzen. |
| **Entferne Attribut aus Variable**<br><code>ugso_object_remove</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_remove.png" alt="Entferne Attribut aus Variable" style="max-width:280px;max-height:180px"> | Neue Zuweisung ohne Schlüssel. Keine Mutation anderer Variablen oder Entity-Attribute. |
| **Bereichsvergleich**<br><code>ugso_logic_range</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_range.png" alt="Bereichsvergleich" style="max-width:280px;max-height:180px"> | Unabhängig &lt; oder ≤ für Unter- und Obergrenze; Zahl und Laufzeitzahl. |
| **Ersatzwert**<br><code>ugso_logic_default</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_default.png" alt="Ersatzwert" style="max-width:280px;max-height:180px"> | Auswahl null/nicht gesetzt oder leer/falsch/0; null-Modus erhält gültige 0 und falsch. |
| **Der Fall ist**<br><code>ugso_case</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_case.png" alt="Der Fall ist" style="max-width:280px;max-height:180px"> | 1–100 Fallwerte mit Zahnrad/+− und Aktionskörpern. Erste Übereinstimmung, sonst optionaler Standardkörper. |
| **Liste erstellen**<br><code>ugso_list_new</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_new.png" alt="Liste erstellen" style="max-width:280px;max-height:180px"> | 0–100 beliebige Einträge mit Zahnrad/+−, auch verschachtelte Werte. |
| **Listenlänge**<br><code>ugso_list_length</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_length.png" alt="Listenlänge" style="max-width:280px;max-height:180px"> | Länge einer Liste als Laufzeitzahl. Texte und Dictionaries sind keine Listen. |
| **Liste ist leer**<br><code>ugso_list_empty</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_empty.png" alt="Liste ist leer" style="max-width:280px;max-height:180px"> | Boolean-Prüfung auf eine Liste ohne Einträge. |

## Konvertierung seit 0.1.12

[Anleitung, ioBroker-Gegenüberstellung und vorgemerktes JSONata](./conversion).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Nach Zahl**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_number.png" alt="Nach Zahl" style="max-width:280px;max-height:180px"> | HA float ohne Ersatzwert; vollständige Zahl mit Dezimalpunkt. Laufzeitzahl für Variablen, Vergleiche und Zeitrechnung. |
| **Nach Logikwert**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_boolean.png" alt="Nach Logikwert" style="max-width:280px;max-height:180px"> | HA bool; erkannte Boolean-/Textwerte. Boolean-Ausgang für Bedingungen und Logik. |
| **Nach String**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_string.png" alt="Nach String" style="max-width:280px;max-height:180px"> | Jinja-Textdarstellung eines Werts; keine JSON-Serialisierung. |
| **Typ von**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_type.png" alt="Typ von" style="max-width:280px;max-height:180px"> | HA typeof liefert Python-Typnamen, z. B. str, float, bool, dict. Ab HA 2023.4. |
| **Nach Datum/Zeit**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_datetime.png" alt="Nach Datum/Zeit" style="max-width:280px;max-height:180px"> | ISO-Text oder Unix-Sekunden/-Millisekunden nach HA-Ortszeit. Typisierter Time-Ausgang. |
| **Datum/Zeit nach …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_date_format.png" alt="Datum/Zeit nach …" style="max-width:280px;max-height:180px"> | Datumswert, Format, Unix-Zahl oder Datumsbestandteil. Auswahl wechselt den Ausgangstyp; eigenes Format zeigt ein Textfeld. |
| **Zeitdifferenz formatieren**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_duration.png" alt="Zeitdifferenz formatieren" style="max-width:280px;max-height:180px"> | Dauer in Millisekunden oder Sekunden nach hh:mm:ss, hh:mm, mm:ss. Vorzeichen und große Stunden/Minuten bleiben erhalten. |
| **JSON nach Wert**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_from_json.png" alt="JSON nach Wert" style="max-width:280px;max-height:180px"> | JSON-Text nach Objekt, Liste oder Einzelwert. Ungültiges JSON erzeugt einen HA-Fehler. |
| **Wert nach JSON**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_to_json.png" alt="Wert nach JSON" style="max-width:280px;max-height:180px"> | JSON-Serialisierung mit Checkbox für Einrückung. Datumswerte vorher formatieren. |

## Datum und Zeit seit 0.1.11

Die violetten Zeit-Blocks verwenden einen eigenen typisierten Datumswert-Anschluss. [Bedienung, Grenzfälle und Gegenüberstellung](./time).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Uhrzeitvergleich**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_compare.png" alt="Uhrzeitvergleich" style="max-width:280px;max-height:180px"> | Feste Uhrzeit HH:mm/HH:mm:ss; kleiner, größer, gleich oder Zeitraum. Ende erscheint nur bei zwischen/nicht zwischen. |
| **Uhrzeitvergleich mit Eingängen**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_compare_input.png" alt="Uhrzeitvergleich mit Eingängen" style="max-width:280px;max-height:180px"> | Uhrzeitgrenzen als Text-Blocks. Haken aus: eigener Datumswert-Eingang erscheint. Zeiträume auch über Mitternacht. |
| **Aktuelle Zeit als Datumswert**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_now.png" alt="Aktuelle Zeit als Datumswert" style="max-width:280px;max-height:180px"> | HA-Ortszeit mit Datum und Zeitzone, Time-Ausgang für Berechnung oder Formatierung. |
| **Berechnete Zeit**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_boundary.png" alt="Berechnete Zeit" style="max-width:280px;max-height:180px"> | Beginn von Tag, nächstem Tag, Woche (Montag), Monat oder Jahr in HA-Ortszeit. |
| **Nächste Sonnenzeit**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_sun.png" alt="Nächste Sonnenzeit" style="max-width:280px;max-height:180px"> | Aufgang, Untergang, Dämmerung, Höchststand oder Sonnenmitternacht aus sun.sun. Minutenoffset; kann morgen sein. |
| **Zeit berechnen**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_shift.png" alt="Zeit berechnen" style="max-width:280px;max-height:180px"> | Datumswert plus/minus Zahl in Millisekunden, Sekunden, Minuten, Stunden oder Tagen. |
| **Zeit formatieren**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_format.png" alt="Zeit formatieren" style="max-width:280px;max-height:180px"> | Datumswert als Uhrzeit, Datum, Datum/Uhrzeit, ISO mit Zeitzone oder Unix-Sekunden. |

## Weitere Blocks

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Automation**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_automation.png" alt="Automation" style="max-width:280px;max-height:180px"> | Rahmen mit Auslösern, optionaler Bedingung und Aktionskette. Name, ID, Beschreibung und Modus stehen außerhalb des Blocks. |
| **Zustand erreicht**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_state_trigger.png" alt="Zustand erreicht" style="max-width:280px;max-height:180px"> | Startet, wenn die Entität den eingetragenen Zustand erreicht. Erzeugt `trigger: state` mit `to`. |
| **Zahl über/unter Grenze**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_numeric_trigger.png" alt="Zahl über/unter Grenze" style="max-width:280px;max-height:180px"> | Startet beim Grenzübertritt, nicht fortlaufend. Grenze als Number-Wert; `trigger: numeric_state`. |
| **Uhrzeit**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_trigger.png" alt="Uhrzeit" style="max-width:280px;max-height:180px"> | Täglicher Uhrzeit-Auslöser, HH:MM oder HH:MM:SS; `trigger: time`. |
| **Sonnenaufgang/-untergang**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_sun_trigger.png" alt="Sonnenaufgang/-untergang" style="max-width:280px;max-height:180px"> | Dropdown für Sonnenaufgang oder Sonnenuntergang; `trigger: sun`. |
| **HA startet**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_start_trigger.png" alt="HA startet" style="max-width:280px;max-height:180px"> | Startet beim Home-Assistant-Start; `trigger: homeassistant`. |
| **Zustand ist**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_state_condition.png" alt="Zustand ist" style="max-width:280px;max-height:180px"> | Boolean-Bedingung: Entität hat den angegebenen Zustand; `condition: state`. |
| **Zahlenvergleich**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_numeric_condition.png" alt="Zahlenvergleich" style="max-width:280px;max-height:180px"> | Boolean-Bedingung über/unter einer Grenze; `condition: numeric_state`. |
| **UND / ODER / NICHT**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_condition.png" alt="UND / ODER / NICHT" style="max-width:280px;max-height:180px"> | Verknüpft 1–100 Bedingungen. Plus/Minus ergänzt oder entfernt den letzten Eingang; Zahnrad ordnet um. `and`, `or`, `not`. |
| **Datum heute**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_date_condition.png" alt="Datum heute" style="max-width:280px;max-height:180px"> | Datumsauswahl mit ist/ab/bis einschließlich Jahr. HA-Template vergleicht das heutige Datum in der HA-Zeitzone. Kein eigener Auslöser. |
| **Zahl**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_number.png" alt="Zahl" style="max-width:280px;max-height:180px"> | Unbegrenzter Zahlen-Wertblock. Passt in Grenzen und Wartezeiten; deren eigene Validierung gilt weiterhin. |
| **Prozent**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_percent.png" alt="Prozent" style="max-width:280px;max-height:180px"> | Slider und genaue Eingabe für ganze Werte 0–100. Number-Output, beispielsweise für Ladezustand oder Helligkeit. |
| **Mehrzeiliger Text**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text.png" alt="Mehrzeiliger Text" style="max-width:280px;max-height:180px"> | String-Wert für Logmeldungen. Enter: neue Zeile; Shift+Enter: übernehmen. Drei sichtbare Zeilen, vollständiger Text bleibt gespeichert. |
| **Farbe**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour.png" alt="Farbe" style="max-width:280px;max-height:180px"> | Hex-Farbauswahl; als RGB-Liste für Licht, Variablen oder Farbberechnungen. Colour/Value-Ausgang, nicht an feste Zahlenanschlüsse. |
| **Ein / Aus / Umschalten**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_switch_action.png" alt="Ein / Aus / Umschalten" style="max-width:280px;max-height:180px"> | Aktion der Entitätsdomain: `turn_on`, `turn_off` oder `toggle`. Die Entität muss die Aktion unterstützen. |
| **Generische HA-Aktion**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_service_action.png" alt="Generische HA-Aktion" style="max-width:280px;max-height:180px"> | Aktionsname, optional eine Zielentität, Daten als JSON-Objekt. Für Parameter, die Komfortblocks noch nicht anbieten. |
| **Warte Sekunden**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_delay_action.png" alt="Warte Sekunden" style="max-width:280px;max-height:180px"> | Pause von 0–86400 ganzen Sekunden. Number-Eingang mit Shadow-Standardwert. |
| **Falls / sonst falls / sonst**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_if_action.png" alt="Falls / sonst falls / sonst" style="max-width:280px;max-height:180px"> | Plus/Minus ergänzt oder entfernt den letzten sonst-falls-Zweig; S schaltet Sonst um. Zahnrad zum Umordnen. `if` oder `choose`, erster passender Zweig. |
| **Log-Ausgabe**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_log_action.png" alt="Log-Ausgabe" style="max-width:280px;max-height:180px"> | Textmeldung und Schweregrad-Dropdown; `system_log.write`. Info/Debug können in HA gefiltert sein. |
| **HA-Script steuern**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_script_action.png" alt="HA-Script steuern" style="max-width:280px;max-height:180px"> | Starten ohne Warten, stoppen oder direkt aufrufen und warten. `script.turn_on`, `script.turn_off` oder `script.name`. |
| **Entität aktualisieren**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_update_action.png" alt="Entität aktualisieren" style="max-width:280px;max-height:180px"> | `homeassistant.update_entity` fordert ein Update an. Setzt keinen Zustand; Unterstützung hängt von der Integration ab. |
| **Helfer steuern**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_helper_action.png" alt="Helfer steuern" style="max-width:280px;max-height:180px"> | Typ-Dropdown Schalter/Zähler/Timer steuert das Aktions-Dropdown. Entitäts-ID muss zum Typ passen. Timer nutzt vorhandene Dauer; Parameter über generische Aktion. |
| **Licht mit Farbe**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_action.png" alt="Licht mit Farbe" style="max-width:280px;max-height:180px"> | Lichtentität, Colour-Eingang und Helligkeit 0–100. Erzeugt `light.turn_on` mit `rgb_color` und `brightness_pct`. Farbunterstützung des Geräts erforderlich. |

Bei Minus oder ausgeschaltetem Sonst werden angeschlossene Blocks abgelöst, nicht gelöscht. Wieder verbinden oder entfernen, bevor YAML exportiert wird. Rückgängig stellt Anschlüsse und Verbindungen wieder her. Shadow-Werte kehren zurück, wenn ein ersetzender Wertblock entfernt wird.

## Variablen- und Template-Blocks seit 0.1.8

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Variable setzen**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_set.png" alt="Variable setzen" style="max-width:280px;max-height:180px"> | Aktionsblock: ausgewählte Variable auf Zahl, Text/Template, Boolean oder null setzen. Erzeugt eine native HA-`variables`-Aktion. Vor späteren Lesezugriffen platzieren. |
| **Variable lesen**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_get.png" alt="Variable lesen" style="max-width:280px;max-height:180px"> | Seitlicher String-Anschluss; erzeugt <code v-pre>{{ name }}</code> für Log-Meldungen und weitere Variablenzuweisungen. Dropdown bietet Umbenennen/Löschen. |
| **Template-Wert**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_template.png" alt="Template-Wert" style="max-width:280px;max-height:180px"> | Mehrzeiliges Jinja-Template mit String-Anschluss für Log-Meldungen oder Variablenzuweisungen. HA wertet die Vorlage bei Ausführung aus; Blocks führt sie nicht aus. |
| **Template-Bedingung**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_template_condition.png" alt="Template-Bedingung" style="max-width:280px;max-height:180px"> | Boolean-Anschluss für Nur wenn, Falls und logische Gruppen. Erzeugt `condition: template` mit `value_template`. Ergebnis muss in HA wahr sein; kein eigener Auslöser. |

## Variablen und Templates verwenden

### Erhöhen und Verringern seit 0.1.10

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Erhöhe Variable um …**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_change.png" alt="Erhöhe Variable um" style="max-width:280px;max-height:180px"> | Dropdown für die Variable, Number-Eingang mit Standard-Schritt `1`. Addiert den Schritt zur zuvor gesetzten Zahlenvariable. Negative Schritte verringern; `0` und Dezimalschritte sind möglich. Native HA-Variablenzuweisung mit Jinja. |

Im Menü **Variablen** erscheinen für jede erstellte Variable **Setze**, **Erhöhe** und **Variable lesen**. Beispiel in der Aktionskette: **Setze test auf 10 → Erhöhe test um 1 → Log Info Meldung Variable test**. Die Meldung verwendet anschließend den Wert `11`. Mit Schritt `-2` würde aus `10` der Wert `8`.

Vor dem Erhöhen die Variable als Zahl setzen. Fehlende Variablen, Text (auch `"10"`), Boolean oder null werden nicht automatisch konvertiert oder mit `0` initialisiert; die Jinja-Auswertung in HA schlägt dann fehl. Erstellen allein weist keinen Wert zu. JSON erhält den Erhöhen-Block; unser genaues YAML-Ausgabeformat wird beim Import wieder als Erhöhen-Block erkannt. Andere Rechenvorlagen bleiben Template-Blocks. Der geplante Dialog für typisierte Variablen bleibt offen.

Im Menü **Variablen → Variable erstellen …** beispielsweise `leistung` anlegen. Namen verwenden Buchstaben, Ziffern und `_`, keine führende Ziffer. Den Setzen-Block in **Dann** platzieren und eine Zahl oder ein Template anschließen. Danach den Lesen-Block in eine Log-Meldung stecken. Erstellen allein weist noch keinen Wert zu. Variablen gelten für den HA-Automationslauf; sie ersetzen keine dauerhaft gespeicherten Helfer.

Beispiel: **Setze leistung auf Template** mit <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>, danach **Log Info Meldung Variable leistung**. HA liest den Sensor beim Setzen und verwendet den Wert im folgenden Schritt. Eine Template-Bedingung kann beispielsweise <code v-pre>{{ states('sensor.leistung') | float(0) > 100 }}</code> prüfen.

Umbenennen aktualisiert die verbundenen Variablen-Blocks. Namen in frei eingegebenen Jinja-Texten müssen manuell geändert werden. Aktionsvariablen stehen erst nach ihrer Zuweisung bereit, nicht in vorgelagerten Automationsbedingungen. Blocks prüft Struktur und YAML, keine Jinja-Syntax oder vorhandenen HA-Entitäten. Der Import unterstützt pro Variablenwert Text/Template, Zahl, Boolean oder null. Mehrere Einträge werden seit 0.1.34 im gemeinsamen JSON-Block unterstützt. Listen/Objekte als Werte und Variablen auf Automationsebene werden weiterhin abgelehnt. [Native HA-Variablen und Gültigkeit](https://www.home-assistant.io/docs/scripts/#define-variables).

## Logik-Blocks seit 0.1.9

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Vergleich**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_compare.png" alt="Vergleich" style="max-width:280px;max-height:180px"> | Vergleicht zwei Werte mit =, ≠, &lt;, ≤, &gt; oder ≥. Zahlen, Texte, Variablen und einzelne Template-Ausdrücke anschließen. Liefert Boolean; Ausgabe als HA-Template-Bedingung oder Variablenwert. |
| **UND / ODER kompakt**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_binary_logic.png" alt="UND ODER kompakt" style="max-width:280px;max-height:180px"> | Zwei Boolean-Eingänge. Als Bedingung native HA-`and`/`or`-Gruppe; als Variablenwert geklammerter Jinja-Ausdruck. Die erweiterbare Gruppe bleibt für mehr Eingänge verfügbar. |
| **NICHT**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_not.png" alt="NICHT" style="max-width:280px;max-height:180px"> | Negiert eine Boolean-Bedingung. Als Bedingung native HA-`not`-Gruppe, als Variablenwert Jinja-`not`. |
| **wahr / falsch**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_boolean.png" alt="wahr falsch" style="max-width:280px;max-height:180px"> | Boolean-Konstante mit Dropdown. Für Bedingungen und Variablen; die Zuweisung erzeugt echte YAML-Boolean-Werte. |
| **null**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_null.png" alt="null" style="max-width:280px;max-height:180px"> | Kein Wert. Variablen erhalten YAML `null`, Ausdrücke Jinja `none`. Weder `0` noch `falsch`; kein Boolean-Bedingungsblock. |
| **Wenn → dann Wert → sonst Wert**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ternary.png" alt="Bedingte Wertauswahl" style="max-width:280px;max-height:180px"> | Wählt anhand einer Boolean-Bedingung einen von zwei Werten. Für Variablen, Log-Meldungen und Vergleiche; erzeugt einen Jinja-Ausdruck und enthält keine Aktionskette. |

**Beispiel:** In der Aktionskette zuerst `leistung` setzen. Dann **Setze meldung auf Wenn**, mit **Vergleich Variable leistung &gt; Zahl 100** als Test, Text **Hohe Leistung** als Dann-Wert und Text **Geringe Leistung** als Sonst-Wert. Danach **Log Info Meldung Variable meldung** verwenden. HA entscheidet bei Ausführung.

Vergleiche konvertieren Typen nicht automatisch: Zahl `20` unterscheidet sich von Text `"20"`. Sensorzustände gegebenenfalls im Template mit `float` oder `int` umwandeln. In einem Ausdruckseingang ist nur eine einzelne Jinja-Ausgabe zulässig, beispielsweise <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>. Mehrzeilige Anweisungen und gemischter Text bleiben im eigenständigen Template-Wertblock nutzbar. Dynamische Wertauswahlen sind nicht als feste Zahlen-Grenzen oder Wartezeiten vorgesehen.

JSON-Projekte bewahren die Blockformen und Anschlüsse. YAML speichert die native Bedeutung: Beim Wiederöffnen erscheinen Vergleiche und Wertauswahlen als Template-Blocks, UND/ODER/NICHT als Bedingungsgruppen. [HA-Logikbedingungen](https://www.home-assistant.io/docs/scripts/conditions/#logical-conditions).

## Originalplugins und Einbindung

Die sechs bisherigen Originalplugins sind auf **13.2.0**, die vier Theme-/Zoom-Plugins und die Arbeitsbereichssuche auf **13.3.0** festgelegt und werden lokal mit Blockly **13.3.0** ausgeliefert. Lizenz: Apache-2.0. Die folgenden Links führen direkt zu den Original-Repositories. Unsere HA-Blocks, YAML-Adapter und Plus/Minus-Steuerung sind eigener UGSo-Code.

| Originalplugin | Nutzung / Stand |
| --- | --- |
| [workspace-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/workspace-search) | Findet platzierte Blocks im Arbeitsbereich; getrennt von der Toolboxsuche. Seit 0.1.21 verfügbar. |
| [toolbox-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) | Blocksuche am Menüende, deutsche Suchhinweise; Treffer behalten Dropdowns und Shadows. |
| [field-multilineinput](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) | Im Textblock; Zeilenumbrüche bleiben im Projekt und YAML erhalten. |
| [field-slider](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) | Im Prozentblock; 0–100 mit genauer Zahleneingabe. |
| [field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) | Im Farbblock; Hex wird für die Lichtaktion nach RGB umgewandelt. Zufall/RGB/Mischung seit 0.1.15 mit eigenen HA-Generatoren. |
| [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) | Dunkle Arbeitsfläche und Blockauswahl; Teil der gespeicherten Theme-Auswahl. |
| [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) | Originalpalette mit kräftigeren Rändern; eigene Blocks über Theme-Stile. |
| [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) | Originalpalette für Standardgruppen, passende UGSo-Erweiterungsfarben und adaptive Schriftkontraste. |
| [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) | Zusätzlicher Einpassen-Knopf neben den Zoom-Reglern; auch per Tastatur. |
| [field-date](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) | Im Datumsvergleich; UGSo-Unterklasse sichert den verzögerten Kalenderaufruf ab. |
| [field-dependent-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) | Im Helferblock; Helfertyp bestimmt Aktionen. Keine Live-HA-Auswahl. |
| [block-plus-minus](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-plus-minus) | Bedienprinzip in eigenen HA-Blocks umgesetzt; Originalplugin nicht installiert. Zahnrad bleibt verfügbar. |
| [block-dynamic-connection](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-dynamic-connection) | Noch nicht eingebunden. Automatisch wachsende Anschlüsse, Textverknüpfung und Listen sind geplant. |

Die Farbauswahl verwendet zusätzlich die indirekte Abhängigkeit [field-grid-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-grid-dropdown). HA-Ausgabe wird von uns erzeugt; die mitgelieferten JavaScript-Generatoren werden nicht verwendet.

[Zur Übersicht](/projects/blocks-for-ha/)

Benutzerdefinierte Blocks seit 0.1.18 ergänzen die 163 nativen Typen. [Editor](./custom-blocks) und [Paketkatalog](./catalog/).

## Trigger-IDs und mehrere Ziele

Seit **0.1.28**: Zustandslisten über **Zustände als JSON-Liste**, z. B. `["1_single","1_double"]`; optionale Trigger-IDs in allen Standardauslösern; **Ausgelöst durch ID** als native Trigger-Bedingung (einzelne ID oder JSON-Liste). Allgemeine HA-Aktionen unterstützen **Ziele als JSON-Liste**, optionale Metadaten und erhalten ausdrücklich leere Datenobjekte. Vierfach-Taster mit vier `choose`-Zweigen sind vollständig importierbar.

**Einzelne Automation · HA-Editor** gibt keine oberste `id` aus. Trigger-IDs bleiben erhalten. Projekt und **automations.yaml-Liste** behalten eine vorhandene Automations-ID.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Ausgelöst durch ID**<br><code>ugso_trigger_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_trigger_condition.png" alt="Ausgelöst durch ID" style="max-width:280px;max-height:180px"> | `condition: trigger` · `id` |

[Home Assistant: Trigger IDs](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Trigger condition](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

## Poolpumpen, Ereignisse und mehrere Uhrzeiten

Seit **0.1.30**: Ein Zeit-Auslöser akzeptiert über **Uhrzeiten als JSON-Liste** mehrere feste Uhrzeiten, z. B. `["10:00:00","13:00:00","19:00:00"]`. **Jede Änderung** im Zustandsauslöser lässt `to` weg; **Entitäten als JSON-Liste** überwacht mehrere Entitäten. Ohne `to` reagiert HA auch auf Attributänderungen. Der Ereignis-Auslöser unterstützt z. B. `timer.finished` und einen optionalen JSON-Datenfilter. Die native Zeitbedingung erhält `before`/`after` unverändert; feste Uhrzeiten, nach inklusive und vor exklusiv, auch über Mitternacht. Gleiche Grenzen entsprechen ganztägig. Zeithelfer, Zeit-Templates und Wochentagsfilter bleiben hier noch außerhalb des unterstützten Imports. Die vollständige Poolpumpen-Automation bleibt einschließlich mehrzeiligem Timer-Template und verschachteltem `choose` erhalten.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Ereignis-Auslöser**<br><code>ugso_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_event_trigger.png" alt="Ereignis-Auslöser" style="max-width:280px;max-height:180px"> | `trigger: event` · `event_type` · `event_data` |
| **Native HA-Zeitbedingung**<br><code>ugso_native_time_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_native_time_condition.png" alt="Native HA-Zeitbedingung" style="max-width:280px;max-height:180px"> | `condition: time` · `before` · `after` |

[Home Assistant: triggers](https://www.home-assistant.io/docs/automation/trigger/) · [Time condition](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

## Temperatur geändert

Seit **0.1.31** unterstützt der neue Block den nativen Auslöser temperature.changed. Ziel (JSON): entity_id als Text oder Liste. Schwelle (JSON): type any, above, below, between oder outside. any benötigt nur type; above/below benötigen value, between/outside value_min und value_max. Zahlen: number plus unit_of_measurement (°C/°F). Referenzen: entity (sensor, number oder input_number). Optional ist eine Trigger-ID. Seit 0.1.39 sind auch Bereich, Gerät, Etage und Label importierbar. MQTT-Topics, qos/retain/evaluate_payload und mehrzeilige JSON-/Jinja-Payloads bleiben erhalten.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Temperatur geändert**<br><code>ugso_temperature_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_temperature_trigger.png" alt="Temperatur geändert" style="max-width:280px;max-height:180px"> | temperature.changed |

[Home Assistant: temperature.changed](https://www.home-assistant.io/triggers/temperature.changed/)

## Kalender und Antwortvariablen

**0.1.32:** `calendar.event_started` / `calendar.event_ended`. Ziel: JSON-Objekt mit `entity_id` als Text oder Liste. Optionen sind optional: `offset` mit Tagen, Stunden, Minuten und Sekunden (kombinierbar) oder `HH:MM:SS`; `offset_type` ist `before` oder `after`. Null-Offset, ausgelassene Optionen und optionale Auslöser-ID bleiben erhalten.

Das Feld **Antwortvariable (optional)** im Block **HA-Aktion** erzeugt `response_variable`, zum Beispiel `termine` für `calendar.get_events`. Leer lässt das Feld im YAML weg. Die vollständige Feiertage-/Ferien-Automation erhält beide Kalender, den HA-Start, Variablen zeitpunkt/termin_aktiv, mehrzeilige Jinja-Templates, choose/default und queued. Home Assistant verarbeitet die Kalender und Templates.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Kalendertermin beginnt/endet**<br><code>ugso_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_calendar_trigger.png" alt="Kalendertermin beginnt/endet" style="max-width:280px;max-height:180px"> | calendar.event_started / calendar.event_ended |

[Home Assistant: calendar.event_started](https://www.home-assistant.io/triggers/calendar.event_started/) · [calendar.event_ended](https://www.home-assistant.io/triggers/calendar.event_ended/) · [calendar.get_events](https://www.home-assistant.io/actions/calendar.get_events/)

## Numerische Auslöser mit Haltezeit

Seit **0.1.33** unterstützt **Zahl über/unter Grenze** mehrere Entitäten: **Entitäten als JSON-Liste** einschalten und etwa `["sensor.temp_1","sensor.temp_2"]` eintragen. Ohne Haken bleibt die einzelne Entität aktiv. **Haltezeit (JSON)** mit **verwenden** erzeugt das optionale `for`: etwa `{"hours":0,"minutes":1,"seconds":0}`, `60` oder `"00:01:00"`. Kombinierte days/hours/minutes/seconds/milliseconds, Nulleinträge und HA-Ausgabetemplates bleiben erhalten. Ein deaktivierter Haken lässt `for` weg. Weiterhin genau eine feste Zahlen-Grenze (above oder below); Trigger-ID und choose-Zweige bleiben erhalten.

Home Assistant löst nach dem Grenzübertritt aus, sobald der Wert die gesamte Haltezeit auf dieser Seite der Grenze bleibt. Ein HA-Neustart oder Neuladen der Automationen setzt die laufende Haltezeit zurück. [Home Assistant: numeric_state](https://www.home-assistant.io/triggers/numeric_state/).

## Mehrere Variablen in einer Aktion

Seit **0.1.34** steht im Menü **Variablen** ein gemeinsamer Block **Variablen setzen (JSON)** bereit. Das JSON-Objekt enthält 1–100 Variablennamen mit Text, HA-Template, Zahl, Boolean oder null. Mehrere Einträge bleiben eine einzige native `variables`-Aktion, einschließlich ihrer Reihenfolge. Einzelne Zuweisungen verwenden weiterhin den bisherigen Setzen-Block. Seit 0.1.39 sind auch Listen/Objekte und Variablen auf Automationsebene unterstützt; siehe [HA erweitert und Jinja](./advanced). Namen und Templates im JSON müssen dort direkt bearbeitet werden; Umbenennen über den Blockly-Dialog ändert diesen freien JSON-Text nicht. Beim Import werden die Namen auch in Blockly registriert.

Das Timer-Beispiel erhält h/m, beide überwachten Entitäten, die Bedingung und den restart-Modus. Fehlende conditions werden als leere Liste ergänzt.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Variablen setzen (JSON)**<br><code>ugso_variables_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variables_action.png" alt="Variablen setzen (JSON)" style="max-width:280px;max-height:180px"> | Variablen mit einzelnen Wertfeldern; Listen und Objekte als JSON, neue Namen über zusätzliche Optionen. |

[Home Assistant: variables](https://www.home-assistant.io/docs/scripts/#variables)

## Wartezeit als Zeittext oder Template

Seit **0.1.35** importiert Blocks native `delay`-Zeittexte in den neuen Block unter **Timeouts**. Beispiele: `00:00:02`, `01:30` (eine Stunde und 30 Minuten), `00:00:00.250` oder ein HA-Ausgabetemplate. Der Zeittext bleibt ein Text im YAML und im gespeicherten Projekt. Eine Wartezeit verlängert den aktuellen HA-Lauf; nachfolgende Aktionen folgen danach. Bestehende Sekunden- und Einheiten-Blocks bleiben verfügbar. Diese Erweiterung betrifft `delay`, nicht den Timeout des Warte-bis-Blocks.

Das Timer-Reset-Beispiel schaltet zunächst timer_reset aus, wartet zwei Sekunden und schaltet anschließend beide Zielentitäten aus. Die Entitäts-ID input_boolean.timer_runing bleibt genau wie im Original erhalten.

| Block | Bild | Funktion |
| --- | --- | --- |
| **Warte Zeittext / Template**<br><code>ugso_delay_text</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_delay_text.png" alt="Warte Zeittext / Template" style="max-width:280px;max-height:180px"> | Nativer delay-Zeittext / HA-Template. |

[Home Assistant: delay](https://www.home-assistant.io/docs/scripts/#wait-for-time-to-pass-delay)

## Dynamische HA-Aktionsnamen

Seit **0.1.36** akzeptiert das erste Feld im Block **HA-Aktion** einen statischen Aktionsnamen oder eine Jinja-Vorlage. Das Feld lässt sich mehrzeilig bearbeiten. Beispiele: `input_boolean.turn_on`, `input_boolean.turn_` mit angehängtem Jinja-Ausdruck oder ein vollständiges if/else-Template. Ziel, Daten, Metadaten und Antwortvariable bleiben in ihren bisherigen Feldern. Die Vorlage und ihre Zeilenumbrüche bleiben bei Import, Projekt-Speicherung und YAML-Export erhalten.

Beim Shelly-Beispiel bleibt die zusammengesetzte Aktion `input_boolean.turn_` plus Zustandsabfrage erhalten, ebenso die verschachtelten choose-Zweige. Home Assistant wertet den Aktionsnamen erst beim Ausführen aus; er muss dann einen vorhandenen Dienstnamen ergeben. Blocks prüft statische Aktionsnamen und vorhandene Template-Klammern, keine Jinja-Syntax oder Laufzeitergebnisse. Zielentitäten müssen weiterhin feste IDs sein; Templates für ganze Datenobjekte sind nicht Teil dieser Erweiterung.

[Home Assistant: choosing the action with a template](https://www.home-assistant.io/docs/scripts/perform-actions/#choosing-the-action-with-a-template)


## Zeitmuster-Auslöser

Unter **Auslöser** steht seit **0.1.37** ein nativer `time_pattern`-Block. Das JSON-Feld enthält beispielsweise `{"seconds":"/30"}` für die Sekunden 0 und 30 jeder Minute. Optional sind `hours`, `minutes` und `seconds`; mindestens ein Feld ist erforderlich. Feste Werte: Stunden 0–23, Minuten/Sekunden 0–59, als Zahl oder Text ohne führende Nullen. `*` passt auf jeden Wert, `/n` auf durch n teilbare Werte (n > 0 innerhalb des Wertebereichs). Fehlende Einheiten und Zahl/Text-Typen bleiben unverändert; Home Assistant ergänzt seine Standardwerte zur Laufzeit. Optional ist eine Auslöser-ID.

Die LCD-Automation mit vier `input_text.set_value`-Aktionen und `mode: restart` wurde vollständig geprüft: Jinja, Formatierung, Textkürzung, Auffüllen und Zeilenumbrüche bleiben erhalten. Home Assistant führt die Templates und den Zeitplan aus.

| Block | Type |
| --- | --- |
| ![Zeitmuster (JSON)](/assets/blocks-for-ha/blocks/de/ugso_time_pattern_trigger.png) | `ugso_time_pattern_trigger` |

[Home Assistant: time_pattern](https://www.home-assistant.io/triggers/time_pattern/).


## Dynamische Zielentitäten

Seit **0.1.39** akzeptiert das Feld **Ziel** in der allgemeinen **HA-Aktion** eine feste Entitäts-ID oder ein HA-Template, zum Beispiel <code v-pre>{{ ziel_tv }}</code>. Der Entitätsdialog bietet dafür ein mehrzeiliges Eingabefeld. Auch die JSON-Zielliste darf feste IDs und Templates enthalten. Jinja bleibt unverändert erhalten und wird erst von Home Assistant ausgewertet. Dynamische Ziele werden beim Import in der allgemeinen HA-Aktion dargestellt; spezialisierte Schaltblöcke würden die Domain nicht zuverlässig bestimmen können.

Die Schlafzimmer-TV-Automation mit einer mehrzeiligen Sommerbetrieb-Variable, 21:30 und 00:30 Uhr und zwei choose-Zweigen ist geprüft. Zielvorlagen, Variableninhalt und Uhrzeitbedingungen bleiben beim Import, Projekt-Neuladen und Export erhalten. Auslöser- und Bedingungsfelder für Entitäts-IDs verlangen weiterhin feste IDs.

[Home Assistant: templates in action targets](https://www.home-assistant.io/docs/scripts/perform-actions/#setting-targets-and-options-with-a-template).


## HA erweitert und Jinja seit 0.1.39

[Anleitung / Guide](./advanced).

| Block | Bild | Funktion |
| --- | --- | --- |
| **HA state**<br><code>ugso_ha_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_state_trigger.png" alt="HA state" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA numeric_state**<br><code>ugso_ha_numeric_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_numeric_state_trigger.png" alt="HA numeric_state" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA time**<br><code>ugso_ha_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_time_trigger.png" alt="HA time" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA sun**<br><code>ugso_ha_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_sun_trigger.png" alt="HA sun" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA homeassistant**<br><code>ugso_ha_homeassistant_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_homeassistant_trigger.png" alt="HA homeassistant" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA mqtt**<br><code>ugso_ha_mqtt_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_mqtt_trigger.png" alt="HA mqtt" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA template**<br><code>ugso_ha_template_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_template_trigger.png" alt="HA template" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA webhook**<br><code>ugso_ha_webhook_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_webhook_trigger.png" alt="HA webhook" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA zone**<br><code>ugso_ha_zone_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_zone_trigger.png" alt="HA zone" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA device**<br><code>ugso_ha_device_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_device_trigger.png" alt="HA device" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA tag**<br><code>ugso_ha_tag_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_tag_trigger.png" alt="HA tag" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA conversation**<br><code>ugso_ha_conversation_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_conversation_trigger.png" alt="HA conversation" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA geo_location**<br><code>ugso_ha_geo_location_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_geo_location_trigger.png" alt="HA geo_location" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA calendar**<br><code>ugso_ha_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_calendar_trigger.png" alt="HA calendar" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA event**<br><code>ugso_ha_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_event_trigger.png" alt="HA event" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA-Auslöser (erweitert)**<br><code>ugso_ha_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_trigger.png" alt="HA-Auslöser (erweitert)" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA-Bedingung (erweitert)**<br><code>ugso_ha_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_condition.png" alt="HA-Bedingung (erweitert)" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA-Schritt (erweitert)**<br><code>ugso_ha_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_action.png" alt="HA-Schritt (erweitert)" style="max-width:280px;max-height:180px"> | Beschriftete HA-Eingaben und zusätzliche JSON-Optionen. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA-Aktion Zielart Ziel Daten Schrittoptionen**<br><code>ugso_target_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_target_action.png" alt="HA-Aktion Zielart Ziel Daten Schrittoptionen" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **HA-Integration Ziel Optionen verwenden**<br><code>ugso_integration_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_integration_trigger.png" alt="HA-Integration Ziel Optionen verwenden" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Aktionsgruppe**<br><code>ugso_sequence</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_sequence.png" alt="Aktionsgruppe" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Parallel Zweig 1 Zweig 2**<br><code>ugso_parallel</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_parallel.png" alt="Parallel Zweig 1 Zweig 2" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Warte auf Auslöser Optionen**<br><code>ugso_wait_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_wait_trigger.png" alt="Warte auf Auslöser Optionen" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Nur weiter wenn**<br><code>ugso_condition_step</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_condition_step.png" alt="Nur weiter wenn" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Ereignis auslösen Daten**<br><code>ugso_fire_event</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_fire_event.png" alt="Ereignis auslösen Daten" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Assist antwortet**<br><code>ugso_assist_response</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_assist_response.png" alt="Assist antwortet" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Szene aktivieren**<br><code>ugso_scene</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_scene.png" alt="Szene aktivieren" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Jinja (experimentell)**<br><code>ugso_jinja_value</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_value.png" alt="Jinja (experimentell)" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |
| **Jinja-Bedingung (experimentell)**<br><code>ugso_jinja_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_condition.png" alt="Jinja-Bedingung (experimentell)" style="max-width:280px;max-height:180px"> | Erweiterte HA-Felder oder Original-Jinja. Unterstützte Struktur wird geprüft; Integration und Ausführung in HA prüfen. |

## Jinja-Strukturen (experimentell)

15 neue Typen seit 0.1.41. Die äußeren Wert-/Bedingungsblocks verbinden die verschachtelten Teile mit HA. Jinja-Ausdrücke und Template-Teile haben eigene typisierte Anschlüsse. [Einlesen, Bearbeiten und Grenzen](./advanced#jinja-experimentell).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Jinja zusammengesetzt**<br><code>ugso_jinja_composed_value</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_composed_value.png" alt="Jinja zusammengesetzt" style="max-width:280px;max-height:180px"> | Äußerer Wertblock: zusammenhängendes Template; Original bleibt bis zur Bearbeitung erhalten. |
| **Jinja-Bedingung zusammengesetzt**<br><code>ugso_jinja_composed_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_composed_condition.png" alt="Jinja-Bedingung zusammengesetzt" style="max-width:280px;max-height:180px"> | Äußerer Boolean-Block für eine HA-Template-Bedingung. |
| **Entität Funktion**<br><code>ugso_jinja_entity</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_entity.png" alt="Entität Funktion" style="max-width:280px;max-height:180px"> | Entität suchen und states/state_attr/is_state/is_state_attr wählen; zusätzliche Argumente anschließen. |
| **Filter Argumente Wert**<br><code>ugso_jinja_filter</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_filter.png" alt="Filter Argumente Wert" style="max-width:280px;max-height:180px"> | Filter auswählen; 0–3 Positionsargumente und einen Jinja-Ausdruck anschließen. |
| **Literal (Jinja)**<br><code>ugso_jinja_literal</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_literal.png" alt="Literal (Jinja)" style="max-width:280px;max-height:180px"> | Zahl, String in Anführungszeichen, true/false oder none in Jinja-Schreibweise. |
| **Jinja-Variable**<br><code>ugso_jinja_variable</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_variable.png" alt="Jinja-Variable" style="max-width:280px;max-height:180px"> | Einfacher Jinja-Variablenname als Text; keine automatische Blockly-Umbenennung. |
| **Jetzt (Jinja)**<br><code>ugso_jinja_now</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_now.png" alt="Jetzt (Jinja)" style="max-width:280px;max-height:180px"> | now() erzeugen; Home Assistant liefert den Zeitpunkt bei der Auswertung. |
| **Ausdruck**<br><code>ugso_jinja_binary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_binary.png" alt="Ausdruck" style="max-width:280px;max-height:180px"> | Zwei Jinja-Ausdrücke berechnen, vergleichen oder mit and/or verbinden. |
| **Ausdruck**<br><code>ugso_jinja_unary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_unary.png" alt="Ausdruck" style="max-width:280px;max-height:180px"> | not, negatives oder positives Vorzeichen für einen Jinja-Ausdruck. |
| **Wert wenn sonst**<br><code>ugso_jinja_select</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_select.png" alt="Wert wenn sonst" style="max-width:280px;max-height:180px"> | Wert wählen: yes if test else no. Alle drei Ausdruckseingänge sind erforderlich. |
| **Ausgeben**<br><code>ugso_jinja_output</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_output.png" alt="Ausgeben" style="max-width:280px;max-height:180px"> | Einen Ausdruck als <code v-pre>{{ ... }}</code> innerhalb eines Templates ausgeben. |
| **Jinja-Text**<br><code>ugso_jinja_text</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_text.png" alt="Jinja-Text" style="max-width:280px;max-height:180px"> | Wörtlicher Text einschließlich Leerraum; Jinja-Steuerzeichen hier nicht einfügen. |
| **Template-Teile danach**<br><code>ugso_jinja_join</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_join.png" alt="Template-Teile danach" style="max-width:280px;max-height:180px"> | Zwei Template-Teile in der dargestellten Reihenfolge verbinden. |
| **Wenn Text sonst**<br><code>ugso_jinja_if</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_if.png" alt="Wenn Text sonst" style="max-width:280px;max-height:180px"> | if/else mit Bedingung und verschachtelten Text-/Ausgabeteilen. |
| **Für in Text wenn leer**<br><code>ugso_jinja_for</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_for.png" alt="Für in Text wenn leer" style="max-width:280px;max-height:180px"> | Einfache for-Schleife: Variable, Ausdruck, Template-Inhalt und optionaler Leerfall. |
