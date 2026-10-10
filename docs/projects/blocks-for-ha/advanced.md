---
title: Erweiterte HA-Automationen und Jinja
description: Auslöser, Bedingungen, Ziele, Ablaufgruppen und experimentelle Jinja-Erkennung.
---

# Erweiterte HA-Automationen und Jinja

Seit **0.1.39** gibt es 148 Blocktypen. Die Kategorien **HA erweitert** und **Jinja (experimentell)** ergänzen die einfachen Blocks. Einfache importierte Schritte behalten ihre bisherigen Formen. Zusätzliche Felder erscheinen in erweiterten Blocks als bearbeitbares JSON. Der Import prüft die unterstützte Struktur; Integration, Geräte-IDs, Templates und Ausführung müssen anschließend in Home Assistant geprüft werden.

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

Variablen unterstützen zusätzlich Listen und verschachtelte Objekte. Gemeinsame Schrittoptionen `alias`, `enabled` und `continue_on_error` werden erhalten, ebenso Antwortvariablen und Metadaten. Erweiterte Blocks bieten dafür JSON-Felder. `enabled` akzeptiert Boolean oder HA-Template, `continue_on_error` einen Boolean.

Unter **Projekt & Beschreibung → HA-Optionen** bearbeiten: `variables`, `trigger_variables`, `initial_state`, `trace.stored_traces` und `max_exceeded`. **Anwenden** übernimmt nur gültige Optionen. Nicht mehr enthaltene Optionen werden entfernt; `{}` entfernt alle Optionen dieses Feldes. Name und Ausführungsmodus bleiben separat. Eine Automation ohne `alias` kann importiert werden; der Dateiname fällt auf `automation.yaml` zurück.

## Warten und Ablaufgruppen

- **Warte auf Auslöser** verbindet eine Auslöserkette und bietet `timeout` / `continue_on_timeout` im Optionsfeld.
- **Aktionsgruppe** erzeugt eine native `sequence` mit anschließbaren Schritten.
- **Parallel** startet native parallele Zweige. Mit **+ / −** sind 1–100 Zweige möglich. Beim Entfernen eines belegten Zweigs bleibt dessen Inhalt als unverbundener Block erhalten; anschließend verbinden oder löschen.
- **Nur weiter wenn** erzeugt eine Bedingung als Aktionsschritt. Ereignis, Assist-Antwort und Szene haben eigene Blocks.
- Wiederholungen unterstützen auch echte Listen/Objekte bei `for_each`; Pausen erlauben kombinierte Einheiten und Bruchteile. Erweiterte oder gemischte Zweigformen bleiben als JSON-Schritt erhalten.

Diese Blocks exportieren native HA-Abläufe. Es gibt keine lokale Ausführung und keine parallele JavaScript-Script-Engine.

## Jinja (experimentell)

**Jinja einlesen** über dem Arbeitsbereich öffnet einen Dialog. Template einfügen, die Vorschau prüfen, optional **Als Bedingung** auswählen und **Block erstellen** klicken. Der neue Block wird neben der Automation angelegt und muss anschließend verbunden werden. Alternativ die Wert-/Bedingungsblocks aus der Kategorie ziehen. Importierte Template-Werte und Template-Bedingungen werden ebenfalls als Jinja-Blocks dargestellt, soweit keine spezifischere einfache Form passt.

![Experimenteller Jinja-Wertblock](/assets/blocks-for-ha/blocks/de/ugso_jinja_value.png)

Die Analyse erkennt häufige Muster: Entitätszustände und Attribute, Datum/Zeit, Variablen, Filterketten sowie `if/else` und `for`. Sie zeigt die erkannten Entitäten und Filter im Block an. Kommentare, Stringliterale und `raw`-Abschnitte werden bei der Referenzsuche übersprungen. Unvollständige Kontrollstrukturen werden in der Vorschau markiert.

::: warning Grenzen der Erkennung
Dies ist eine konservative Musteranalyse, kein vollständiger Jinja-Parser, keine automatische Zerlegung in ausführbare Teilblocks und keine Syntaxgarantie. Unbekannte Funktionen und komplexe Templates bleiben als editierbarer Originaltext erhalten. Der Text wird weder umgeschrieben noch lokal ausgeführt. In HA testen. Innerhalb eines zusammengesetzten Ausdrucks ist nur ein einzelner Jinja-Ausdruck möglich; ganze `if/for`-Templates gehören in den eigenständigen Wertblock.
:::

Blockly-Projekte sichern auch Blockformen und Anordnung. YAML-Import → Blockly → Export erhält die unterstützten Werte einschließlich ausgelassener Optionalfelder. Grenzen: höchstens 100 Ketteneinträge bzw. Zweige, 10 Ebenen Ablauf-/Bedingungsverschachtelung und begrenzte Daten-/Templategröße. Nicht jede integrationsabhängige Geräteoption wird bereits unterstützt; eine abgelehnte Option wird nicht stillschweigend entfernt.

## Originalquellen und Lizenzhinweise

Eigene UGSo-Implementierung auf Basis der öffentlichen Spezifikation, keine kopierte ioBroker-Ausführungsengine. Blockly und Plugin-Lizenzen stehen unter **Über & Lizenzen**; App-Lizenz Apache-2.0.

- [HA-Auslöser](https://www.home-assistant.io/docs/automation/trigger/), [Bedingungen](https://www.home-assistant.io/docs/scripts/conditions/), [Ablaufbausteine](https://www.home-assistant.io/docs/scripts/) und [Automations-YAML](https://www.home-assistant.io/docs/automation/yaml/).
- [Leistungsänderung](https://www.home-assistant.io/triggers/power.changed/), [Bewegung](https://www.home-assistant.io/triggers/motion.detected/), [Timer beendet](https://www.home-assistant.io/triggers/timer.finished/).
- [Jinja-Templates](https://jinja.palletsprojects.com/en/stable/templates/) und [HA-Templates](https://www.home-assistant.io/docs/configuration/templating/).
- [Blockly: eigene Blocks](https://docs.blockly.com/guides/create-custom-blocks/overview/) und [UGSo-Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha).
