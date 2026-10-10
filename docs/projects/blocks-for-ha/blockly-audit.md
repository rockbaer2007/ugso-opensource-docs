---
title: Blockly-Abgleich, Farben und Funktionen
description: Abgleich aller Standardkategorien mit ioBroker und eigener Home-Assistant-Ausgabe.
---
# Blockly-Abgleich, Farben und Funktionen

Stand **0.1.15**, 10. Oktober 2026: **111 unterstützte Blocktypen**. Drei Farbberechnungen und drei originale Blockly-Typen für Wertfunktionen/Parameter sind neu. Eine Funktionsdefinition ist neben der Automation erlaubt; andere unverbundene Blocks verhindern weiterhin den Export.

## Quellen und Vorgehen

Verglichen wurden die bei uns installierten Standardblocks aus **Blockly 13.3.0**, die originale [Blockly-Blockbibliothek](https://github.com/raspberrypifoundation/blockly/tree/4195d60c610bec4b4b186aa22d58cb16beb42dfa/blocks) sowie die [ioBroker-Standardtoolbox](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/index.html) und deren [Blockly-Bridge](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/src/Components/blockly-plugins/bridge.ts). Die Links sind auf die geprüften Commits festgelegt.

**Registriert, im Menü angeboten und bei uns exportierbar sind unterschiedliche Dinge.** ioBroker lädt die Standardbibliothek vollständig. Ein dort registrierter Block muss nicht in seiner Standardtoolbox erscheinen. Die Bilder zeigen außerdem nicht zwangsläufig die aktuelle Toolbox. Textumkehr ist inzwischen im ioBroker-Menü enthalten; atan2 fehlt dort, ist aber durch den Bibliotheksimport grundsätzlich registriert. Das ist kein Nachweis, dass ioBroker atan2 nicht ausführen könnte.

## Alle Standardkategorien

| Kategorie / originale Typen | ioBroker-Standardmenü | UGSo / HA und offene Varianten |
| --- | --- | --- |
| Logik: `controls_if`, `controls_ifelse`, `logic_compare`, `logic_operation`, `logic_negate`, `logic_boolean`, `logic_null`, `logic_ternary` | Enthalten; weitere eigene UND/ODER-, Fall-, Bereichs- und Ersatzwertblocks | Vergleich, Gruppen, Falls/Sonst-wenn/Sonst, Wertauswahl, Bereich und Fallauswahl umgesetzt. Formvarianten werden durch eigene Blocks zusammengefasst. |
| Schleifen: `controls_repeat`, `controls_repeat_ext`, `controls_whileUntil`, `controls_for`, `controls_forEach` | Enthalten, hauptsächlich Value-Variante der Wiederholungszahl | Anzahl/solange/bis/für jeden sowie ganzzahlige feste Zählgrenzen umgesetzt. Dynamische oder gebrochene Zählgrenzen offen. |
| Schleifensteuerung: `controls_flow_statements` | break / continue | Lokales break/continue offen. „Lauf stoppen“ beendet den gesamten HA-Lauf und ist kein Ersatz. |
| Mathematik: `math_number`, `math_arithmetic`, `math_single`, `math_trig`, `math_constant`, `math_number_property`, `math_round`, `math_on_list`, `math_modulo`, `math_constrain`, `math_random_int`, `math_random_float`, `math_change` | Enthalten; zusätzliche feste Nachkommastellen | Eigene Rechen-, Statistik-, Rundungs-, Zufalls- und Variablenänderungsblocks. Offen: Primzahl, Standardabweichung, Modalwert mit allen Gleichständen und Unendlich. Keine vollständige Gleichheit aller Dropdown-Varianten behauptet. |
| Mathematik: `math_atan2` | Nicht angeboten, Bibliothek registriert | Vierquadranten-Winkel bereits umgesetzt. |
| Text: `text`, `text_join`, `text_append`, `text_length`, `text_isEmpty`, `text_indexOf`, `text_charAt`, `text_getSubstring`, `text_changeCase`, `text_trim`, `text_count`, `text_replace`, `text_reverse` | Enthalten; zusätzlich mehrzeiliger Text, Zeilenumbruch, enthält und Zahlenformatierung | Umgesetzt einschließlich Textumkehr. Teiltext hat derzeit Grenzen vom Anfang; weitere Positionsvarianten und ioBroker-Zahlenformatierung offen. |
| Text: `text_print`, `text_prompt`, `text_prompt_ext` | Nicht angeboten | Ausgabe über HA-Log-Aktion. Browser-Prompt wäre keine spätere HA-Eingabe und wird nicht als solche eingebaut. |
| Listen: `lists_create_empty`, `lists_create_with`, `lists_repeat`, `lists_length`, `lists_isEmpty`, `lists_indexOf`, `lists_getIndex`, `lists_setIndex`, `lists_getSublist`, `lists_split`, `lists_sort`, `lists_reverse` | Enthalten; leere Liste als Variante | Liste erstellen mit 0–100 Eingängen, Wiederholung, Suchen/Lesen/Setzen/Entfernen/Einfügen, Teilbereich, Teilen/Verbinden, Sortieren/Umkehren umgesetzt. Kombiniertes Lesen-und-Entfernen, weitere End-/Zufallspositionen offen. |
| Variablen: `variables_get`, `variables_set`, dynamische Typvarianten `variables_get_dynamic`, `variables_set_dynamic` | Dynamische Kategorie VARIABLE, keine VARIABLE_DYNAMIC-Kategorie | Erstellen, Lesen, Setzen, Erhöhen umgesetzt. Typauswahl/typed-variable-modal bleibt vorgemerkt. Originaler Getter zusätzlich für Funktionsparameter. |
| Funktionen: `procedures_defreturn`, `procedures_callreturn`, `procedures_defnoreturn`, `procedures_callnoreturn`, `procedures_ifreturn` | Dynamische Kategorie PROCEDURE | Neu: originale Wertdefinition/Aufruf mit Parametern und Rückgabewert. Aktionen ohne Rückgabewert über vorhandenen HA-Script-Aufruf; keine lokalen Aktionsfunktionen oder frühes return. |
| Farbe: picker/random/rgb/blend aus field-colour | Alle vier enthalten | Jetzt Farbwähler plus Zufall, RGB und Mischung in eigener Kategorie; eigene HA-Generatoren statt JavaScript. |

Interne Mutator-Hilfsblocks sind keine eigenständigen Anwenderblocks. Ältere Aliasformen werden über ihre entsprechende Funktion berücksichtigt. Bei ioBroker zusätzlich vorhandene Kategorien System, Aktionen, Sendto, Datum/Zeit, Konvertierung, Trigger, Timeouts und Objekt sind Erweiterungen der Script-Engine. Unsere bereits dokumentierten Gegenstücke stehen unter [Datum/Zeit](./time), [Konvertierung](./conversion), [Timeouts/Objekt/Logik](./flow) und [Sammlungen](./collections). Fremde Adapter und nachinstallierte Drittplugins sind nicht Bestandteil dieses Standardvergleichs. Sendto/JSONata und benannte JavaScript-Timer werden nicht als native HA-Funktionen ausgegeben.

## Farben verwenden

Unter **Farbe** stehen Farbauswahl, Zufallsfarbe, RGB-Prozentanteile und Mischung. Prozentwerte werden auf 0–100, der Mischanteil auf 0–1 begrenzt. Kanäle werden auf 0–255 umgerechnet und halbe positive Werte aufgerundet. Mischung 0 liefert Farbe 1, Mischung 1 Farbe 2; Rot/Blau mit 0,5 ergibt `[128, 0, 128]`. Keine Gamma-Korrektur.

Anders als die originalen JavaScript-Farbblocks liefern unsere berechneten Werte **RGB-Listen für HA**, keine Hextexte. Den Block an **Licht → Farbe** oder an eine Variablenzuweisung anschließen. Ein fester Farbwähler exportiert weiterhin eine native RGB-Liste; Berechnungen ein Template in `data.rgb_color`. Eine gespeicherte RGB-Variable kann ebenfalls angeschlossen werden. Es werden genau drei numerische Kanäle von 0–255 verlangt; Hextext zuerst bewusst umwandeln. Ungültige Werte führen zum Templatefehler.

Die Mischung wertet jeden direkt angeschlossenen Farbblock einmal aus. Veränderliche Zahlen-/Template-Eingänge, insbesondere der Mischanteil, vor Verwendung in einer Variablen speichern: generierte Typprüfungen oder mehrfach verwendete Funktionsparameter können Ausdrücke mehrfach auswerten. Zufall ist nicht kryptografisch. Die Generatoren nutzen die dokumentierten HA-Helfer [zip](https://www.home-assistant.io/template-functions/zip/), [multiply](https://www.home-assistant.io/template-functions/multiply/) und [add](https://www.home-assistant.io/template-functions/add/). Die Funktionsreferenz gilt für aktuelles HA; auf älteren Installationen Verfügbarkeit prüfen.

## Wertfunktionen verwenden

1. **Funktionen** öffnen und einen Definitionsblock auf die Arbeitsfläche ziehen.
2. Beispielsweise `doppelt` nennen; im originalen Zahnrad einen Parameter `x` hinzufügen.
3. Als Rückgabewert **Variable x × Zahl 2** anschließen. Parameter werden über Variablen-Getter gelesen.
4. Kategorie erneut öffnen: Der Aufruf `doppelt` mit Eingang `x` steht dynamisch bereit. Zahl 21 anschließen und den Aufruf beispielsweise einer Variablen zuweisen.

Beim Export entsteht der entsprechende Jinja-Ausdruck mit dem Argument 21, keine JavaScript-/Python-Funktion. Bis zu acht unterschiedliche Parameter; Namen aus ASCII-Buchstaben, Ziffern und Unterstrich, beginnend mit Buchstabe oder Unterstrich. Verschachtelte Aufrufe sind innerhalb der allgemeinen Ausdruckstiefengrenze möglich. Rekursion, fehlende Argumente/Rückgabewerte, doppelte Namen und Aktionskörper verhindern den Export. Innerhalb einer Wertfunktion haben Parameter Vorrang vor gleichnamigen Automationsvariablen. Außerhalb gelten normale HA-Variablen und deren Gültigkeit. Rückgabewerte werden zur Laufzeit nicht allein durch die Blockly-Anschlussfarbe typisiert; in Bedingungen muss das Ergebnis Boolean sein.

JSON-Projekte erhalten Definitionen, Parameter und Aufrufe. YAML speichert die expandierte Bedeutung und öffnet diese später als Template; daraus werden keine Funktionsdefinitionen rekonstruiert. Der vorgemerkte Developer-Tools-Import für freie Block-/Template-Pakete bleibt eine separate Roadmap-Aufgabe.

Verifiziert: Projekt-/YAML-Rundlauf, Farbgrenzen, Jinja-Auswertung mit immutable Sandbox und nachgebildeten HA-Helfern, originaler Funktionsmutator, dynamisches Menü und Browser-Neuladen. Eine Ausführung in einer echten Home-Assistant-Installation steht noch aus.

[Blockbilder und Einzelbeschreibungen](./blocks) · [Originales field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) · [Eigene Blockly-Blöcke](https://developers.google.com/blockly/guides/create-custom-blocks/overview)
