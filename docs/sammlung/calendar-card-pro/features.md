---
title: Calendar Card Pro Features
description: Deutsche Uebersicht der wichtigsten Calendar-Card-Pro-Funktionen.
---
# Features

## Visueller Editor

Die Karte besitzt einen visuellen Editor. Laut Original wurde dieser in Version `4.0.0` neu aufgebaut und in mehrere Bereiche gegliedert. Er bietet Suche nach Einstellungen, Filter fuer angepasste Werte, kalenderbezogene Einstellungen und Ausnahmen fuer die Spaltenansicht.

## Mehrere Kalender

Mehrere Kalender koennen in einer Karte angezeigt werden. Jeder Kalender kann eigene Farben und Anzeigeoptionen erhalten.

## Kompakte Ansicht

Mit `compact_events_to_show` und `compact_days_to_show` kann begrenzt werden, wie viele Termine oder Tage direkt sichtbar sind. Mit `tap_action: expand` kann zwischen kompakter und erweiterter Ansicht gewechselt werden.

## Spaltenansicht

Mit `view: column` werden Tage nebeneinander als Spalten angezeigt. Das eignet sich besonders fuer Wochenuebersichten auf breiten Dashboards.

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

Wenn nicht genug Breite vorhanden ist, kann die Karte Spalten reduzieren oder in die Listenansicht zurueckfallen.

## Dynamisches Startdatum

`start_date` kann ein festes Datum oder ein relativer Ausdruck sein.

Beispiele:

| Wert | Bedeutung |
| --- | --- |
| `today` | Heute starten |
| `today+7` | In sieben Tagen starten |
| `start_of_week` | Am Wochenanfang starten |
| `monday+1w` | Montag der naechsten Woche |
| `saturday` | Am Samstag starten |

## Mehrtaegige Termine

Mit `split_multiday_events` koennen mehrtaegige Termine auf jedem betroffenen Tag angezeigt werden. In der Spaltenansicht ist das besonders sinnvoll, weil jede Spalte einen Tag darstellt.

## Wetterintegration

Mit `weather` kann eine Home-Assistant-Wetterentitaet eingebunden werden. Wetterdaten koennen im Tageskopf, neben Terminen oder an beiden Stellen erscheinen.

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

Die Karte unterstuetzt `tap_action` und `hold_action`. Damit koennen zum Beispiel Details geoeffnet, die Karte erweitert, eine Navigation ausgefuehrt oder ein Dienst aufgerufen werden.

## Templates

Der Titel kann Home-Assistant-Templates enthalten. Zusaetzlich gibt es Platzhalter wie Terminanzahl oder naechster Termin, die fuer dynamische Titel genutzt werden koennen.

## Theming

Calendar Card Pro ist theme-aware und kann ueber Optionen sowie CSS-Variablen angepasst werden. Fuer tieferes Styling kann `card-mod` eingesetzt werden.

## Performance

Die Karte nutzt laut Original intelligente Aktualisierung und Caching. Version `4.0.0` reduziert den Download, weil der Editor separat geladen wird, und vermeidet doppelte Kalenderabfragen.
