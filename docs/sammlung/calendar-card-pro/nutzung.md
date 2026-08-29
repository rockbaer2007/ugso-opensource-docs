---
title: Calendar Card Pro Nutzung
description: Calendar Card Pro im Home-Assistant-Dashboard verwenden.
---
# Nutzung

## Karte Per Editor Hinzufügen

1. Dashboard öffnen.
2. Dashboard bearbeiten.
3. Neue Karte hinzufügen.
4. Nach `Calendar` suchen.
5. Calendar Card Pro auswählen.
6. Drei-Punkte-Menü der Karte öffnen.
7. **Configure** wählen, um den visuellen Editor zu öffnen.

Ab Home Assistant `2026.6` kann die Karte laut Original auch im Tab **By entity** vorgeschlagen werden, wenn eine `calendar.*`-Entität gewählt wird.

## Schnellstart Per YAML

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
days_to_show: 3
show_location: false
show_month: false
```

`calendar.family` muss durch eine eigene Kalenderentität ersetzt werden.

## Mehrere Kalender

```yaml
type: custom:calendar-card-pro
title: Termine
entities:
  - entity: calendar.family
    color: '#ff6c92'
  - entity: calendar.work
    color: '#86ebda'
  - entity: calendar.personal
    color: '#c2ffb3'
days_to_show: 7
compact_events_to_show: 3
tap_action:
  action: expand
```

## Typische Einsatzfälle

- Familienkalender im Dashboard
- Arbeits- und Privatkalender in einer Ansicht
- Wochenübersicht in Spalten
- Termine mit Wettervorschau
- kompakte Kalenderkarte für Wandtablets
- dynamische Titel mit nächstem Termin oder Terminanzahl
