---
title: Erweiterte HA-Automationen und Jinja
description: Auslöser, Bedingungen, Ziele, Ablaufgruppen und experimentelle Jinja-Erkennung.
---

# Erweiterte HA-Automationen und Jinja

## HA-Optionen über das Zahnrad seit 0.1.61

Im Zahnrad-Popup eine Option von links in die Liste ziehen. Jede Option ergänzt eine eigene Zeile unter den Pflichtfeldern. Reihenfolge und bewusst ausgewählte leere Zeilen werden im Projekt gespeichert. Entfernen setzt den Wert zurück. Importierte Optionen einschließlich `false`, `0`, Listen und Templates erscheinen automatisch und bleiben beim Laden erhalten. Alle Beschriftungen sind in DE/EN/FR verfügbar.

![Kompakter HA-Schritt](/assets/blocks-for-ha/blocks/de/ugso_ha_action.png)

| Geprüfte HA-Blöcke | Pflichtfelder / Zahnrad-Optionen |
| --- | --- |
| Alle erweiterten Auslöser und allgemeiner HA-Auslöser | Typ und Kerneingaben bleiben. Weitere Grenzen, Zustandsfilter, Dauer, Attribute, Templates, Ereignisfilter, Gerätezuordnung, ID, Name, Aktiv und Variablen je nach Auslöser im Zahnrad. |
| Erweiterte HA-Bedingung | Typ und Kerneingaben; optionale Zeitgrenzen, Wochentage, Attribute, Dauer, Name und Aktiv. |
| Erweiterter HA-Schritt | Aktion und Entität; Gerät, Bereich, Etage, Label, Daten, Antwortvariable, Name, Aktiv, Fehlerbehandlung und Metadaten einzeln ergänzbar. |
| Zielaktion, allgemeine Aktion, Ereignis senden | Aktions-/Ereignisname und Ziel bleiben; Daten, Antwortvariable, Listen, Metadaten bzw. Schrittoptionen ergänzbar. |
| Warte-Auslöser, Zeitmuster | Auslöserkette bleibt; Zeitlimit, Verhalten bei Zeitlimit und Schrittoptionen. Zeitfelder einzeln auswählbar; mindestens eines muss für gültiges YAML gesetzt sein. |
| Kalender, Temperatur, Integrationsauslöser | Kerneingaben und erforderliche Schwellenwerte bleiben; weitere Zielarten, Optionen und ID ergänzbar. |
| Einfache Auslöser | ID, mehrere Entitäten/Zustände/Uhrzeiten, jede Änderung, Haltezeit, Sonnenversatz und Ereignisfilter je nach Block. |
| Einfache Aktionen/Werte, Variablen | Kein unnötiges Zahnrad für reine Kerneingaben. Variablennamen und Werte bleiben direkt bearbeitbar. |
| Falls, Auswahl, Parallel, Objekte, Listen und Funktionen | Vorhandene spezialisierte Zahnrad-Editoren bleiben erhalten. |

**und**, **oder** und **nicht** sind getrennte Menüblöcke. und/oder haben jeweils einen erweiterbaren Zahnrad-Editor ohne Operatorauswahl; nicht hat einen Eingang. Alte kombinierte Gruppen bleiben lesbar, auch mit mehreren Negationseingängen. YAML-Import verwendet die getrennten Varianten, soweit sie exakt gleichwertig sind.

![und](/assets/blocks-for-ha/blocks/de/ugso_and.png)

![oder](/assets/blocks-for-ha/blocks/de/ugso_or.png)

Geprüft wurden das Rendern sämtlicher Blockdefinitionen in DE/EN/FR, Projekt-/YAML-Kompatibilität und das Hinzufügen/Entfernen von Optionen. Entitäten, Integrationen und Laufzeitdaten sind weiterhin in HA zu prüfen.

Seit **0.1.43** bieten die erweiterten HA-Blöcke beschriftete Eingaben statt eines großen JSON-Objekts. Weiterhin 163 Blocktypen: die Kategorien **HA erweitert** und **Jinja (experimentell)** ergänzen die einfachen Blocks. Der Import prüft die unterstützte Struktur; Integration, Geräte-IDs, Templates und Ausführung anschließend in Home Assistant prüfen.

Alle 15 klassischen erweiterten Auslöser, allgemeine Bedingungen und Schritte sowie Integrationsziele/-optionen, Kalender, Temperaturgrenzen, Zeitmuster, Variablen und Warte-/Schrittoptionen sind umgestellt. **numeric_state** bietet etwa Entität, Über, Unter, Attribut, Template, Dauer und ID. Leere optionale Felder werden nicht ausgegeben; beide Zahlengrenzen sind unabhängig bearbeitbar. Entitätsfelder erlauben HA-Suche, manuelle IDs, JSON-Listen und Templates. Bei Typwechsel in allgemeinen Blöcken zusätzliche Felder gegebenenfalls über die Optionen ergänzen.

Listen und Objekte als JSON eingeben; `null` ist ein expliziter Nullwert, `"null"` der Text. Zustände und Payloads bleiben Text. Unveränderte Werte behalten ihre ursprünglichen Typen und den vollständigen Jinja-Text. **Weitere Optionen (JSON)** erhält zusätzliche Angaben. Komplexe Daten und verschachtelte Zweige bleiben in getrennten JSON-Feldern; sie werden nicht beliebig in anschließbare Zweige zerlegt. Alte JSON-Projekte laden die neuen Felder automatisch; YAML-Import/-Export und gespeicherte Projekte bleiben kompatibel.

![Numeric-state-Auslöser mit einzelnen Eingaben](/assets/blocks-for-ha/blocks/de/ugso_ha_numeric_state_trigger.png)

Originalspezifikation: [HA-Auslöser](https://www.home-assistant.io/docs/automation/trigger/), [HA-Bedingungen](https://www.home-assistant.io/docs/scripts/conditions/), [HA-Schritte](https://www.home-assistant.io/docs/scripts/).

## Auslöser und Bedingungen

| Bereich | Unterstützte Ergänzungen |
| --- | --- |
| Zustand | Mehrere Entitäten; `from`, `to`, `not_from`, `not_to`, Listen und `null`; Attribute und `for`. |
| Zahlen | Beide Grenzen, Zahlenhelfer als Grenzen, Attribute, `value_template`, Haltezeit und mehrere Entitäten. |
| Zeit | Uhrzeiten und Listen, Zeithelfer/Sensoren, Zeitquelle mit Offset, Wochentage und Zeitmuster. |
| Sonne und HA | Sonnenauf-/untergang mit Offset; Start und Shutdown. |
| Weitere Auslöser | MQTT, Template, Webhook, Zone, Geräteauslöser, Tag, Sprachbefehl, Geolocation, Ereignis und klassischer Kalender. |
| Integrationen | `calendar.event_started/ended`, `temperature.changed`, `power.changed`, `motion.detected`, `timer.finished`. Ziele auch über Gerät, Bereich, Etage und Label. |
| Bedingungen | Zeit/Wochentag, Zustand mit Listen/Attribut/Haltezeit/`match`, Zahlengrenzen, Sonne, Zone, Gerät, Auslöser-ID, Template und verschachtelte UND/ODER/NICHT. Template-Kurzform bleibt erhalten. |

Der Integrationsblock bietet ein Dropdown für Leistung, Bewegung und Timer. Ziel und Optionen werden separat eingegeben. Beim Wechsel werden unveränderte Beispielwerte passend ersetzt; eigene Werte bleiben erhalten. Im erweiterten JSON-Auslöser lassen sich `alias`, `enabled`, `id` und Auslöservariablen angeben. Unbekannte Typen und nicht unterstützte Felder werden mit einer Meldung abgelehnt.

## Ziele, Variablen und Optionen

**HA-Aktion mit Zielart** bietet `entity_id`, `device_id`, `area_id`, `floor_id` und `label_id`. Eine ID, JSON-Liste oder ein HA-Template ist möglich. Mehrere Zielarten gleichzeitig lassen sich im **HA-Schritt (erweitert)** eingeben. Aktionsdaten dürfen Objekte oder ein vollständiges HA-Template sein; der Import erhält beide Formen.

Variablen unterstützen zusätzlich Listen und verschachtelte Objekte. Vorhandene Variablen haben einzelne Wertfelder; neue Namen können über die zusätzlichen Optionen ergänzt werden. Gemeinsame Schrittoptionen `alias`, `enabled`, `continue_on_error`, Antwortvariablen und Metadaten haben eigene Eingaben. `enabled` akzeptiert Boolean oder HA-Template, `continue_on_error` einen Boolean.

Unter **Projekt & Beschreibung → HA-Optionen** bearbeiten: `variables`, `trigger_variables`, `initial_state`, `trace.stored_traces` und `max_exceeded`. **Anwenden** übernimmt nur gültige Optionen. Nicht mehr enthaltene Optionen werden entfernt; `{}` entfernt alle Optionen dieses Feldes. Name und Ausführungsmodus bleiben separat. Eine Automation ohne `alias` kann importiert werden; der Dateiname fällt auf `automation.yaml` zurück.

## Warten und Ablaufgruppen

- **Warte auf Auslöser** verbindet eine Auslöserkette und bietet `timeout` / `continue_on_timeout` im Optionsfeld.
- **Aktionsgruppe** erzeugt eine native `sequence` mit anschließbaren Schritten.
- **Parallel** startet native parallele Zweige. Mit dem **Zahnrad** sind 1–100 Zweige möglich. Beim Entfernen eines belegten Zweigs bleibt dessen Inhalt als unverbundener Block erhalten; anschließend verbinden oder löschen.
- **Nur weiter wenn** erzeugt eine Bedingung als Aktionsschritt. Ereignis, Assist-Antwort und Szene haben eigene Blocks.
- Wiederholungen unterstützen auch echte Listen/Objekte bei `for_each`; Pausen erlauben kombinierte Einheiten und Bruchteile. Erweiterte oder gemischte Zweigformen bleiben als JSON-Schritt erhalten.

Diese Blocks exportieren native HA-Abläufe. Es gibt keine lokale Ausführung und keine parallele JavaScript-Script-Engine.

## Jinja (experimentell)

Seit **0.1.41** kann **Jinja einlesen** Templates in bearbeitbare, verschachtelte Blocks zerlegen. Template einfügen, die Vorschau prüfen, **Als bearbeitbare Blocks zerlegen** aktiviert lassen und bei Bedarf **Als Bedingung** auswählen. **Block erstellen** legt die zusammenhängende Struktur neben der Automation an. Anschließend den äußeren Wertblock mit einer Variablenzuweisung oder einem Werteingang verbinden; den Bedingungsblock mit einem Boolean-Eingang verbinden. Ohne Zerlegung entsteht ein Originaltextblock.

![Zusammengesetzter Jinja-Wertblock](/assets/blocks-for-ha/blocks/de/ugso_jinja_composed_value.png)

Beispiel: <code v-pre>Wasser: {{ states('sensor.water') | float(0) | round(1) }} °C</code> wird zu Textteilen und einer Ausgabe mit Entitätsfunktion, `float`- und `round`-Block. Das Entitätsfeld öffnet die vorhandene Suche. Entität, Filter, Argumente und Rundungsstellen lassen sich einzeln ändern. Der YAML-Import zerlegt passende Template-Werte, beispielsweise in einer einzelnen Variablenzuweisung, und Template-Bedingungen. Vorhandene spezifischere Blockformen bleiben erhalten. Templates innerhalb von Aktionsdaten-/Options-JSON bleiben im JSON-Feld.

![Bearbeitbare Struktur des Beispiels](/assets/blocks-for-ha/jinja/de.png)

| Unterstützte Teile | Darstellung |
| --- | --- |
| `states`, `state_attr`, `is_state`, `is_state_attr` mit fester Entitäts-ID | Entitätsfunktion mit Suchfeld und Argumentanschlüssen |
| `now()`, einfache Variablennamen, Zahlen, Strings in Anführungszeichen, Boolean und `none` | Ausdrucksblocks; Jinja-Variablennamen sind Textfelder |
| `float`, `int`, `round`, `default`, `abs`, `lower`, `upper`, `trim`, `length`, `string`, `list`, `join`, `replace` | Verschachtelte Filter mit 0–3 Positionsargumenten |
| `+`, `-`, `*`, `/`, `//`, `%`, `~`, Vergleiche, `and`, `or`, `not` | Berechnungen/Vergleiche mit expliziter Klammerung |
| `wert if bedingung else anderer_wert` | Bedingte Wertauswahl |
| Text, <code v-pre>{{ ... }}</code>, einfache `{% if ... %}...{% else %}...{% endif %}` | Text-, Ausgabe-, Verbindungs- und Wenn-/Sonst-Blocks |
| `{% for item in items %}...{% else %}...{% endfor %}` | Einfache Schleife über einen Ausdruck, optionaler Leerfall und verschachtelte Teile |

**Original erhalten:** Unveränderte Strukturen behalten den genauen Originaltext einschließlich Leerraum, auch nach Projekt-Reload und Undo/Redo. Änderungen erzeugen neu formatiertes Jinja. Zurückgesetzte Felder stellen bei gleicher Struktur wieder das Original her. Blockly-Projekte sichern Struktur und Original; YAML sichert den Template-Text, der beim Import wieder analysiert wird.

::: warning Grenzen der Zerlegung
Dies ist ein eigener Parser für einen begrenzten Jinja-Umfang. Sobald ein Teil nicht unterstützt wird, bleibt das **gesamte Template** als editierbarer Originalblock erhalten. Dazu gehören etwa `set`, `namespace`, Objekt-/Listenzugriffe, Listen-/Objektliterale, Tests wie `is defined`, Vergleichsketten, `elif`, benannte Argumente, unbekannte Funktionen/Filter, Kommentare und Whitespace-Steuerzeichen. Keine teilweise Zerlegung, Syntaxgarantie oder lokale Ausführung. Der äußere Wertblock kann ganze Templates enthalten; innerhalb einer anderen Berechnung ist nur eine einzelne Jinja-Ausgabe möglich. Fehlende Anschlüsse oder ungültige Literale verhindern den Export. Grenzen: 10000 Zeichen, 100 Template-Teile und begrenzte Verschachtelung. Jinja-Variablennamen werden nicht automatisch mit anderen Blockly-Variablen umbenannt. Home Assistant übernimmt die Auswertung; dort testen.
:::

Blockly-Projekte sichern auch Blockformen und Anordnung. YAML-Import → Blockly → Export erhält die unterstützten Werte einschließlich ausgelassener Optionalfelder. Grenzen: höchstens 100 Ketteneinträge bzw. Zweige, 10 Ebenen Ablauf-/Bedingungsverschachtelung und begrenzte Daten-/Templategröße. Nicht jede integrationsabhängige Geräteoption wird bereits unterstützt; eine abgelehnte Option wird nicht stillschweigend entfernt.

## Originalquellen und Lizenzhinweise

Eigene UGSo-Implementierung auf Basis der öffentlichen Spezifikation, keine kopierte ioBroker-Ausführungsengine. Blockly und Plugin-Lizenzen stehen unter **Über & Lizenzen**; App-Lizenz Apache-2.0.

- [HA-Auslöser](https://www.home-assistant.io/docs/automation/trigger/), [Bedingungen](https://www.home-assistant.io/docs/scripts/conditions/), [Ablaufbausteine](https://www.home-assistant.io/docs/scripts/) und [Automations-YAML](https://www.home-assistant.io/docs/automation/yaml/).
- [Leistungsänderung](https://www.home-assistant.io/triggers/power.changed/), [Bewegung](https://www.home-assistant.io/triggers/motion.detected/), [Timer beendet](https://www.home-assistant.io/triggers/timer.finished/).
- [Jinja-Templates](https://jinja.palletsprojects.com/en/stable/templates/) und [HA-Templates](https://www.home-assistant.io/docs/configuration/templating/).
- [Blockly: eigene Blocks](https://docs.blockly.com/guides/create-custom-blocks/overview/) und [UGSo-Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha).
