---
title: Calendar Card Pro Features
description: Deutsche Übersicht der wichtigsten Calendar-Card-Pro-Funktionen.
---
# Features

## Visueller Editor

Die Karte besitzt einen visuellen Editor. Laut Original wurde dieser in Version `4.0.0` neu aufgebaut und in mehrere Bereiche gegliedert. Er bietet Suche nach Einstellungen, Filter für angepasste Werte, kalenderbezogene Einstellungen und Ausnahmen für die Spaltenansicht.

## Mehrere Kalender

Mehrere Kalender können in einer Karte angezeigt werden. Jeder Kalender kann eigene Farben und Anzeigeoptionen erhalten.

## Kompakte Ansicht

Mit `compact_events_to_show` und `compact_days_to_show` kann begrenzt werden, wie viele Termine oder Tage direkt sichtbar sind. Mit `tap_action: expand` kann zwischen kompakter und erweiterter Ansicht gewechselt werden.

## Spaltenansicht

Mit `view: column` werden Tage nebeneinander als Spalten angezeigt. Das eignet sich besonders für Wochenübersichten auf breiten Dashboards.

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
view: column
days_to_show: 7
column:
  min_day_width: 150
  min_days_to_show: 3
  min_days_fallback: list
```

Wenn nicht genug Breite vorhanden ist, kann die Karte Spalten reduzieren oder in die Listenansicht zurückfallen.

## Dynamisches Startdatum

`start_date` kann ein festes Datum oder ein relativer Ausdruck sein.

Beispiele:

| Wert | Bedeutung |
| --- | --- |
| `today` | Heute starten |
| `today+7` | In sieben Tagen starten |
| `start_of_week` | Am Wochenanfang starten |
| `monday+1w` | Montag der nächsten Woche |
| `saturday` | Am Samstag starten |

## Mehrtägige Termine

Mit `split_multiday_events` können mehrtägige Termine auf jedem betroffenen Tag angezeigt werden. In der Spaltenansicht ist das besonders sinnvoll, weil jede Spalte einen Tag darstellt.

## Wetterintegration

Mit `weather` kann eine Home-Assistant-Wetterentität eingebunden werden. Wetterdaten können im Tageskopf, neben Terminen oder an beiden Stellen erscheinen.

```yaml
weather:
  entity: weather.home
  position: both
  date:
    show_high_temp: true
    show_low_temp: true
  event:
    show_temp: true
    show_conditions: true
```

## Aktionen

Die Karte unterstuetzt `tap_action` und `hold_action`. Damit können zum Beispiel Details geöffnet, die Karte erweitert, eine Navigation ausgeführt oder ein Dienst aufgerufen werden.

## Templates

Der Titel kann Home-Assistant-Templates enthalten. Zusätzlich gibt es Platzhalter wie Terminanzahl oder nächster Termin, die für dynamische Titel genutzt werden können.

## Theming

Calendar Card Pro ist theme-aware und kann über Optionen sowie CSS-Variablen angepasst werden. Für tieferes Styling kann `card-mod` eingesetzt werden.

## Performance

Die Karte nutzt laut Original intelligente Aktualisierung und Caching. Version `4.0.0` reduziert den Download, weil der Editor separat geladen wird, und vermeidet doppelte Kalenderabfragen.
