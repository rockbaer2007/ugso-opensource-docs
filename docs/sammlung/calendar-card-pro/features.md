---
title: Calendar Card Pro Features
description: Deutsche Übersicht der wichtigsten Calendar-Card-Pro-Funktionen.
---
# Features

## Visueller Editor

Die Karte besitzt einen visuellen Editor. Laut Original wurde dieser in Version `4.0.0` neu aufgebaut und in mehrere Bereiche gegliedert. Er bietet Suche nach Einstellungen, Filter für angepasste Werte, kalenderbezogene Einstellungen und Ausnahmen für die Spaltenansicht. Seit `4.1.0` kann der Editor Kalenderblöcke duplizieren, damit ein Kalender mehrfach mit unterschiedlichen Filtern, Farben oder Event-Typen genutzt werden kann.

## Mehrere Kalender

Mehrere Kalender können in einer Karte angezeigt werden. Jeder Kalender kann eigene Farben und Anzeigeoptionen erhalten.

Seit `4.1.0` lässt sich ein Kalender auch nach Terminart aufteilen. Mit `event_type: timed` werden nur Termine mit Uhrzeit angezeigt, mit `event_type: all_day` nur ganztägige Termine. Dadurch kann derselbe Kalender zweimal eingebunden und unterschiedlich eingefärbt werden.

```yaml
entities:
  - entity: calendar.family
    label: Familie ganztägig
    event_type: all_day
    accent_color: "#ff9800"
  - entity: calendar.family
    label: Familie Termine
    event_type: timed
    accent_color: "#03a9f4"
```

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

Für ganztägige Termine gibt es zusätzliche Steuerung: `allday_expires_at` lässt ganztägige Termine eines Kalenders schon zu einer Uhrzeit am letzten Tag verschwinden, wenn `show_past_events` deaktiviert ist. Das ist zum Beispiel für Müllabfuhr- oder Erinnerungs-Kalender sinnvoll.

```yaml
entities:
  - entity: calendar.waste
    label: Abfall
    allday_expires_at: "10:00"
```

## Wochentage Und Wochenenden

Mit `days_of_week` kann ein Kalender auf Werktage oder Wochenenden eingeschränkt werden. Bei gesplitteten mehrtägigen Terminen wird jeder angezeigte Tag einzeln bewertet.

```yaml
entities:
  - entity: calendar.school
    days_of_week: weekdays
  - entity: calendar.family
    days_of_week: weekends
```

## Ganztags-Badges

Mit `allday_badge` können ganztägige Termine als Badge dargestellt werden. `title` legt das Badge um den Titel, `time` ersetzt die Ganztags-Zeile neben dem Uhr-Icon. `allday_badge_style` steuert die Form, `allday_badge_color` die Farbe.

```yaml
allday_badge: title
allday_badge_style: subtle
allday_badge_color: accent
```

## Filter Und Textersetzung

`blocklist` und `allowlist` lesen standardmäßig den Titel. Mit `filter_field` können sie stattdessen auf `location` oder `description` angewendet werden.

`replace_field`, `replace_pattern` und `replace_with` ändern den angezeigten Text beim Rendern der Karte, ohne den Originaltermin im Kalender zu verändern.

```yaml
entities:
  - entity: calendar.work
    filter_field: location
    allowlist: teams.microsoft.com
    replace_field: title
    replace_with: Besetzt
```

## Orts-Icon

Microsoft-Teams-Termine können automatisch mit Teams-Icon statt Karten-Pin erscheinen. Pro Kalender kann `location_icon` ein eigenes Icon setzen oder mit `mdi:map-marker-outline` wieder den normalen Marker erzwingen.

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
