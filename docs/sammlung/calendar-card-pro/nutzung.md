---
title: Calendar Card Pro Nutzung
description: Calendar Card Pro im Home-Assistant-Dashboard verwenden.
---
# Nutzung

## Karte Per Editor Hinzufuegen

1. Dashboard oeffnen.
2. Dashboard bearbeiten.
3. Neue Karte hinzufuegen.
4. Nach `Calendar` suchen.
5. Calendar Card Pro auswaehlen.
6. Drei-Punkte-Menue der Karte oeffnen.
7. **Configure** waehlen, um den visuellen Editor zu oeffnen.

Ab Home Assistant `2026.6` kann die Karte laut Original auch im Tab **By entity** vorgeschlagen werden, wenn eine `calendar.*`-Entitaet gewaehlt wird.

## Schnellstart Per YAML

```yaml
type: custom:calendar-card-pro
entities:
  - calendar.family
days_to_show: 3
show_location: false
show_month: false
```

`calendar.family` muss durch eine eigene Kalenderentitaet ersetzt werden.

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

## Typische Einsatzfaelle

- Familienkalender im Dashboard
- Arbeits- und Privatkalender in einer Ansicht
- Wochenuebersicht in Spalten
- Termine mit Wettervorschau
- kompakte Kalenderkarte fuer Wandtablets
- dynamische Titel mit naechstem Termin oder Terminanzahl
