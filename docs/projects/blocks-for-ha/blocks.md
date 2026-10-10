---
title: Liste der Blocks
description: Alle UGSo Blocks für HA mit Bild, Funktion und Originalplugins.
---
# Liste der Blocks

Stand **0.1.12**: 50 Blocktypen. Die Bilder zeigen die tatsächlichen UGSo-Blocks im Editor. Dropdown-Varianten zählen nicht als zusätzliche Blocktypen. Anleitungen und ioBroker-Gegenüberstellung: [Datum und Zeit](./time), [Konvertierung](./conversion).

Auslöser sind orange, Bedingungen violett, Werte grün und Aktionen blau. Seitliche Anschlüsse sind typisiert; Auslöser und Aktionen bilden getrennte vertikale Ketten. Entitäts-IDs werden derzeit manuell eingegeben.

## Konvertierung seit 0.1.12

[Anleitung, ioBroker-Gegenüberstellung und vorgemerktes JSONata](./conversion).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Nach Zahl**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_number.png" alt="Nach Zahl" style="max-width:280px;max-height:180px"> | HA float ohne Ersatzwert; vollständige Zahl mit Dezimalpunkt. Laufzeitzahl für Variablen, Vergleiche und Zeitrechnung. |
| **Nach Logikwert**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_boolean.png" alt="Nach Logikwert" style="max-width:280px;max-height:180px"> | HA bool; erkannte Boolean-/Textwerte. Boolean-Ausgang für Bedingungen und Logik. |
| **Nach String**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_string.png" alt="Nach String" style="max-width:280px;max-height:180px"> | Jinja-Textdarstellung eines Werts; keine JSON-Serialisierung. |
| **Typ von**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_type.png" alt="Typ von" style="max-width:280px;max-height:180px"> | HA typeof liefert Python-Typnamen, z. B. str, float, bool, dict. Ab HA 2023.4. |
| **Nach Datum/Zeit**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_datetime.png" alt="Nach Datum/Zeit" style="max-width:280px;max-height:180px"> | ISO-Text oder Unix-Sekunden/-Millisekunden nach HA-Ortszeit. Typisierter Time-Ausgang. |
| **Datum/Zeit nach …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_date_format.png" alt="Datum/Zeit nach …" style="max-width:280px;max-height:180px"> | Datumswert, Format, Unix-Zahl oder Datumsbestandteil. Auswahl wechselt den Ausgangstyp; eigenes Format zeigt ein Textfeld. |
| **Zeitdifferenz formatieren**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_duration.png" alt="Zeitdifferenz formatieren" style="max-width:280px;max-height:180px"> | Dauer in Millisekunden oder Sekunden nach hh:mm:ss, hh:mm, mm:ss. Vorzeichen und große Stunden/Minuten bleiben erhalten. |
| **JSON nach Wert**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_from_json.png" alt="JSON nach Wert" style="max-width:280px;max-height:180px"> | JSON-Text nach Objekt, Liste oder Einzelwert. Ungültiges JSON erzeugt einen HA-Fehler. |
| **Wert nach JSON**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/ugso_convert_to_json.png" alt="Wert nach JSON" style="max-width:280px;max-height:180px"> | JSON-Serialisierung mit Checkbox für Einrückung. Datumswerte vorher formatieren. |

## Datum und Zeit seit 0.1.11

Die violetten Zeit-Blocks verwenden einen eigenen typisierten Datumswert-Anschluss. [Bedienung, Grenzfälle und Gegenüberstellung](./time).

| Block | Bild | Funktion |
| --- | --- | --- |
| **Uhrzeitvergleich**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_compare.png" alt="Uhrzeitvergleich" style="max-width:280px;max-height:180px"> | Feste Uhrzeit HH:mm/HH:mm:ss; kleiner, größer, gleich oder Zeitraum. Ende erscheint nur bei zwischen/nicht zwischen. |
| **Uhrzeitvergleich mit Eingängen**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_compare_input.png" alt="Uhrzeitvergleich mit Eingängen" style="max-width:280px;max-height:180px"> | Uhrzeitgrenzen als Text-Blocks. Haken aus: eigener Datumswert-Eingang erscheint. Zeiträume auch über Mitternacht. |
| **Aktuelle Zeit als Datumswert**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_now.png" alt="Aktuelle Zeit als Datumswert" style="max-width:280px;max-height:180px"> | HA-Ortszeit mit Datum und Zeitzone, Time-Ausgang für Berechnung oder Formatierung. |
| **Berechnete Zeit**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_boundary.png" alt="Berechnete Zeit" style="max-width:280px;max-height:180px"> | Beginn von Tag, nächstem Tag, Woche (Montag), Monat oder Jahr in HA-Ortszeit. |
| **Nächste Sonnenzeit**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_sun.png" alt="Nächste Sonnenzeit" style="max-width:280px;max-height:180px"> | Aufgang, Untergang, Dämmerung, Höchststand oder Sonnenmitternacht aus sun.sun. Minutenoffset; kann morgen sein. |
| **Zeit berechnen**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_shift.png" alt="Zeit berechnen" style="max-width:280px;max-height:180px"> | Datumswert plus/minus Zahl in Millisekunden, Sekunden, Minuten, Stunden oder Tagen. |
| **Zeit formatieren**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_format.png" alt="Zeit formatieren" style="max-width:280px;max-height:180px"> | Datumswert als Uhrzeit, Datum, Datum/Uhrzeit, ISO mit Zeitzone oder Unix-Sekunden. |

## Weitere Blocks

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Automation**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/ugso_automation.png" alt="Automation" style="max-width:280px;max-height:180px"> | Rahmen mit Auslösern, optionaler Bedingung und Aktionskette. Name, ID, Beschreibung und Modus stehen außerhalb des Blocks. |
| **Zustand erreicht**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_state_trigger.png" alt="Zustand erreicht" style="max-width:280px;max-height:180px"> | Startet, wenn die Entität den eingetragenen Zustand erreicht. Erzeugt `trigger: state` mit `to`. |
| **Zahl über/unter Grenze**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_numeric_trigger.png" alt="Zahl über/unter Grenze" style="max-width:280px;max-height:180px"> | Startet beim Grenzübertritt, nicht fortlaufend. Grenze als Number-Wert; `trigger: numeric_state`. |
| **Uhrzeit**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_time_trigger.png" alt="Uhrzeit" style="max-width:280px;max-height:180px"> | Täglicher Uhrzeit-Auslöser, HH:MM oder HH:MM:SS; `trigger: time`. |
| **Sonnenaufgang/-untergang**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_sun_trigger.png" alt="Sonnenaufgang/-untergang" style="max-width:280px;max-height:180px"> | Dropdown für Sonnenaufgang oder Sonnenuntergang; `trigger: sun`. |
| **HA startet**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/ugso_start_trigger.png" alt="HA startet" style="max-width:280px;max-height:180px"> | Startet beim Home-Assistant-Start; `trigger: homeassistant`. |
| **Zustand ist**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_state_condition.png" alt="Zustand ist" style="max-width:280px;max-height:180px"> | Boolean-Bedingung: Entität hat den angegebenen Zustand; `condition: state`. |
| **Zahlenvergleich**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_numeric_condition.png" alt="Zahlenvergleich" style="max-width:280px;max-height:180px"> | Boolean-Bedingung über/unter einer Grenze; `condition: numeric_state`. |
| **UND / ODER / NICHT**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_logic_condition.png" alt="UND / ODER / NICHT" style="max-width:280px;max-height:180px"> | Verknüpft 1–100 Bedingungen. Plus/Minus ergänzt oder entfernt den letzten Eingang; Zahnrad ordnet um. `and`, `or`, `not`. |
| **Datum heute**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_date_condition.png" alt="Datum heute" style="max-width:280px;max-height:180px"> | Datumsauswahl mit ist/ab/bis einschließlich Jahr. HA-Template vergleicht das heutige Datum in der HA-Zeitzone. Kein eigener Auslöser. |
| **Zahl**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/ugso_number.png" alt="Zahl" style="max-width:280px;max-height:180px"> | Unbegrenzter Zahlen-Wertblock. Passt in Grenzen und Wartezeiten; deren eigene Validierung gilt weiterhin. |
| **Prozent**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/ugso_percent.png" alt="Prozent" style="max-width:280px;max-height:180px"> | Slider und genaue Eingabe für ganze Werte 0–100. Number-Output, beispielsweise für Ladezustand oder Helligkeit. |
| **Mehrzeiliger Text**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/ugso_text.png" alt="Mehrzeiliger Text" style="max-width:280px;max-height:180px"> | String-Wert für Logmeldungen. Enter: neue Zeile; Shift+Enter: übernehmen. Drei sichtbare Zeilen, vollständiger Text bleibt gespeichert. |
| **Farbe**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/ugso_colour.png" alt="Farbe" style="max-width:280px;max-height:180px"> | Farbfeld mit Hexwert und Colour-Output für die Lichtaktion. Eigener Anschluss schützt vor Verwechslung mit Text oder Zahlen. |
| **Ein / Aus / Umschalten**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_switch_action.png" alt="Ein / Aus / Umschalten" style="max-width:280px;max-height:180px"> | Aktion der Entitätsdomain: `turn_on`, `turn_off` oder `toggle`. Die Entität muss die Aktion unterstützen. |
| **Generische HA-Aktion**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_service_action.png" alt="Generische HA-Aktion" style="max-width:280px;max-height:180px"> | Aktionsname, optional eine Zielentität, Daten als JSON-Objekt. Für Parameter, die Komfortblocks noch nicht anbieten. |
| **Warte Sekunden**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_delay_action.png" alt="Warte Sekunden" style="max-width:280px;max-height:180px"> | Pause von 0–86400 ganzen Sekunden. Number-Eingang mit Shadow-Standardwert. |
| **Falls / sonst falls / sonst**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_if_action.png" alt="Falls / sonst falls / sonst" style="max-width:280px;max-height:180px"> | Plus/Minus ergänzt oder entfernt den letzten sonst-falls-Zweig; S schaltet Sonst um. Zahnrad zum Umordnen. `if` oder `choose`, erster passender Zweig. |
| **Log-Ausgabe**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_log_action.png" alt="Log-Ausgabe" style="max-width:280px;max-height:180px"> | Textmeldung und Schweregrad-Dropdown; `system_log.write`. Info/Debug können in HA gefiltert sein. |
| **HA-Script steuern**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_script_action.png" alt="HA-Script steuern" style="max-width:280px;max-height:180px"> | Starten ohne Warten, stoppen oder direkt aufrufen und warten. `script.turn_on`, `script.turn_off` oder `script.name`. |
| **Entität aktualisieren**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_update_action.png" alt="Entität aktualisieren" style="max-width:280px;max-height:180px"> | `homeassistant.update_entity` fordert ein Update an. Setzt keinen Zustand; Unterstützung hängt von der Integration ab. |
| **Helfer steuern**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_helper_action.png" alt="Helfer steuern" style="max-width:280px;max-height:180px"> | Typ-Dropdown Schalter/Zähler/Timer steuert das Aktions-Dropdown. Entitäts-ID muss zum Typ passen. Timer nutzt vorhandene Dauer; Parameter über generische Aktion. |
| **Licht mit Farbe**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/ugso_colour_action.png" alt="Licht mit Farbe" style="max-width:280px;max-height:180px"> | Lichtentität, Colour-Eingang und Helligkeit 0–100. Erzeugt `light.turn_on` mit `rgb_color` und `brightness_pct`. Farbunterstützung des Geräts erforderlich. |

Bei Minus oder ausgeschaltetem Sonst werden angeschlossene Blocks abgelöst, nicht gelöscht. Wieder verbinden oder entfernen, bevor YAML exportiert wird. Rückgängig stellt Anschlüsse und Verbindungen wieder her. Shadow-Werte kehren zurück, wenn ein ersetzender Wertblock entfernt wird.

## Variablen- und Template-Blocks seit 0.1.8

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Variable setzen**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_set.png" alt="Variable setzen" style="max-width:280px;max-height:180px"> | Aktionsblock: ausgewählte Variable auf Zahl, Text/Template, Boolean oder null setzen. Erzeugt eine native HA-`variables`-Aktion. Vor späteren Lesezugriffen platzieren. |
| **Variable lesen**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_get.png" alt="Variable lesen" style="max-width:280px;max-height:180px"> | Seitlicher String-Anschluss; erzeugt <code v-pre>{{ name }}</code> für Log-Meldungen und weitere Variablenzuweisungen. Dropdown bietet Umbenennen/Löschen. |
| **Template-Wert**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/ugso_template.png" alt="Template-Wert" style="max-width:280px;max-height:180px"> | Mehrzeiliges Jinja-Template mit String-Anschluss für Log-Meldungen oder Variablenzuweisungen. HA wertet die Vorlage bei Ausführung aus; Blocks führt sie nicht aus. |
| **Template-Bedingung**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/ugso_template_condition.png" alt="Template-Bedingung" style="max-width:280px;max-height:180px"> | Boolean-Anschluss für Nur wenn, Falls und logische Gruppen. Erzeugt `condition: template` mit `value_template`. Ergebnis muss in HA wahr sein; kein eigener Auslöser. |

## Variablen und Templates verwenden

### Erhöhen und Verringern seit 0.1.10

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Erhöhe Variable um …**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/ugso_variable_change.png" alt="Erhöhe Variable um" style="max-width:280px;max-height:180px"> | Dropdown für die Variable, Number-Eingang mit Standard-Schritt `1`. Addiert den Schritt zur zuvor gesetzten Zahlenvariable. Negative Schritte verringern; `0` und Dezimalschritte sind möglich. Native HA-Variablenzuweisung mit Jinja. |

Im Menü **Variablen** erscheinen für jede erstellte Variable **Setze**, **Erhöhe** und **Variable lesen**. Beispiel in der Aktionskette: **Setze test auf 10 → Erhöhe test um 1 → Log Info Meldung Variable test**. Die Meldung verwendet anschließend den Wert `11`. Mit Schritt `-2` würde aus `10` der Wert `8`.

Vor dem Erhöhen die Variable als Zahl setzen. Fehlende Variablen, Text (auch `"10"`), Boolean oder null werden nicht automatisch konvertiert oder mit `0` initialisiert; die Jinja-Auswertung in HA schlägt dann fehl. Erstellen allein weist keinen Wert zu. JSON erhält den Erhöhen-Block; unser genaues YAML-Ausgabeformat wird beim Import wieder als Erhöhen-Block erkannt. Andere Rechenvorlagen bleiben Template-Blocks. Der geplante Dialog für typisierte Variablen bleibt offen.

Im Menü **Variablen → Variable erstellen …** beispielsweise `leistung` anlegen. Namen verwenden Buchstaben, Ziffern und `_`, keine führende Ziffer. Den Setzen-Block in **Dann** platzieren und eine Zahl oder ein Template anschließen. Danach den Lesen-Block in eine Log-Meldung stecken. Erstellen allein weist noch keinen Wert zu. Variablen gelten für den HA-Automationslauf; sie ersetzen keine dauerhaft gespeicherten Helfer.

Beispiel: **Setze leistung auf Template** mit <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>, danach **Log Info Meldung Variable leistung**. HA liest den Sensor beim Setzen und verwendet den Wert im folgenden Schritt. Eine Template-Bedingung kann beispielsweise <code v-pre>{{ states('sensor.leistung') | float(0) > 100 }}</code> prüfen.

Umbenennen aktualisiert die verbundenen Variablen-Blocks. Namen in frei eingegebenen Jinja-Texten müssen manuell geändert werden. Aktionsvariablen stehen erst nach ihrer Zuweisung bereit, nicht in vorgelagerten Automationsbedingungen. Blocks prüft Struktur und YAML, keine Jinja-Syntax oder vorhandenen HA-Entitäten. Der Import unterstützt pro Variablen-Aktion einen Text/Template, eine Zahl, Boolean oder null. Mehrere Einträge, Listen/Objekte sowie Variablen auf Automationsebene sind noch nicht unterstützt und werden beim Import abgelehnt. [Native HA-Variablen und Gültigkeit](https://www.home-assistant.io/docs/scripts/#define-variables).

## Logik-Blocks seit 0.1.9

| Block | Bild im Editor | Funktionsbeschreibung |
| --- | --- | --- |
| **Vergleich**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/ugso_compare.png" alt="Vergleich" style="max-width:280px;max-height:180px"> | Vergleicht zwei Werte mit =, ≠, &lt;, ≤, &gt; oder ≥. Zahlen, Texte, Variablen und einzelne Template-Ausdrücke anschließen. Liefert Boolean; Ausgabe als HA-Template-Bedingung oder Variablenwert. |
| **UND / ODER kompakt**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/ugso_binary_logic.png" alt="UND ODER kompakt" style="max-width:280px;max-height:180px"> | Zwei Boolean-Eingänge. Als Bedingung native HA-`and`/`or`-Gruppe; als Variablenwert geklammerter Jinja-Ausdruck. Die erweiterbare Gruppe bleibt für mehr Eingänge verfügbar. |
| **NICHT**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/ugso_not.png" alt="NICHT" style="max-width:280px;max-height:180px"> | Negiert eine Boolean-Bedingung. Als Bedingung native HA-`not`-Gruppe, als Variablenwert Jinja-`not`. |
| **wahr / falsch**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/ugso_boolean.png" alt="wahr falsch" style="max-width:280px;max-height:180px"> | Boolean-Konstante mit Dropdown. Für Bedingungen und Variablen; die Zuweisung erzeugt echte YAML-Boolean-Werte. |
| **null**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/ugso_null.png" alt="null" style="max-width:280px;max-height:180px"> | Kein Wert. Variablen erhalten YAML `null`, Ausdrücke Jinja `none`. Weder `0` noch `falsch`; kein Boolean-Bedingungsblock. |
| **Wenn → dann Wert → sonst Wert**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/ugso_ternary.png" alt="Bedingte Wertauswahl" style="max-width:280px;max-height:180px"> | Wählt anhand einer Boolean-Bedingung einen von zwei Werten. Für Variablen, Log-Meldungen und Vergleiche; erzeugt einen Jinja-Ausdruck und enthält keine Aktionskette. |

**Beispiel:** In der Aktionskette zuerst `leistung` setzen. Dann **Setze meldung auf Wenn**, mit **Vergleich Variable leistung &gt; Zahl 100** als Test, Text **Hohe Leistung** als Dann-Wert und Text **Geringe Leistung** als Sonst-Wert. Danach **Log Info Meldung Variable meldung** verwenden. HA entscheidet bei Ausführung.

Vergleiche konvertieren Typen nicht automatisch: Zahl `20` unterscheidet sich von Text `"20"`. Sensorzustände gegebenenfalls im Template mit `float` oder `int` umwandeln. In einem Ausdruckseingang ist nur eine einzelne Jinja-Ausgabe zulässig, beispielsweise <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>. Mehrzeilige Anweisungen und gemischter Text bleiben im eigenständigen Template-Wertblock nutzbar. Dynamische Wertauswahlen sind nicht als feste Zahlen-Grenzen oder Wartezeiten vorgesehen.

JSON-Projekte bewahren die Blockformen und Anschlüsse. YAML speichert die native Bedeutung: Beim Wiederöffnen erscheinen Vergleiche und Wertauswahlen als Template-Blocks, UND/ODER/NICHT als Bedingungsgruppen. [HA-Logikbedingungen](https://www.home-assistant.io/docs/scripts/conditions/#logical-conditions).

## Originalplugins und Einbindung

Alle sechs eingebundenen Originalplugins sind auf **13.2.0** festgelegt und werden lokal mit Blockly **13.3.0** ausgeliefert. Lizenz: Apache-2.0. Die folgenden Links führen direkt zu den Original-Repositories. Unsere HA-Blocks, YAML-Adapter und Plus/Minus-Steuerung sind eigener UGSo-Code.

| Originalplugin | Nutzung / Stand |
| --- | --- |
| [toolbox-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) | Blocksuche am Menüende, deutsche Suchhinweise; Treffer behalten Dropdowns und Shadows. |
| [field-multilineinput](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) | Im Textblock; Zeilenumbrüche bleiben im Projekt und YAML erhalten. |
| [field-slider](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) | Im Prozentblock; 0–100 mit genauer Zahleneingabe. |
| [field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) | Im Farbblock; Hex wird für die Lichtaktion nach RGB umgewandelt. Mischen/Zufall noch offen. |
| [field-date](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) | Im Datumsvergleich; UGSo-Unterklasse sichert den verzögerten Kalenderaufruf ab. |
| [field-dependent-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) | Im Helferblock; Helfertyp bestimmt Aktionen. Keine Live-HA-Auswahl. |
| [block-plus-minus](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-plus-minus) | Bedienprinzip in eigenen HA-Blocks umgesetzt; Originalplugin nicht installiert. Zahnrad bleibt verfügbar. |
| [block-dynamic-connection](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-dynamic-connection) | Noch nicht eingebunden. Automatisch wachsende Anschlüsse, Textverknüpfung und Listen sind geplant. |

Die Farbauswahl verwendet zusätzlich die indirekte Abhängigkeit [field-grid-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-grid-dropdown). HA-Ausgabe wird von uns erzeugt; die mitgelieferten JavaScript-Generatoren werden nicht verwendet.

[Zur Übersicht](/projects/blocks-for-ha/)
