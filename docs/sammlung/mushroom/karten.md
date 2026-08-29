---
title: Mushroom Karten
description: Vollstaendige Uebersicht der Mushroom Cards, Legacy Card und Badge.
---
# Karten

Diese Liste bildet die im Mushroom-README verlinkten Karten und Badges ab.

## Aktive Karten

| Karte | Zweck | Original |
| --- | --- | --- |
| Alarm control panel | Alarmanlage anzeigen und steuern. | [alarm-control-panel](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/alarm-control-panel.md) |
| Chips | Kleine Status- und Aktions-Chips anzeigen. | [chips](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/chips.md) |
| Climate | Klima-Entitaeten steuern. | [climate](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/climate.md) |
| Cover | Rollos, Garagentore, Vorhaenge oder andere Cover steuern. | [cover](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/cover.md) |
| Entity | Einzelne Entitaet kompakt anzeigen. | [entity](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/entity.md) |
| Empty | Leere Flaeche oder Abstandhalter verwenden. | [empty](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/empty.md) |
| Fan | Ventilator steuern. | [fan](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/fan.md) |
| Humidifier | Luftbefeuchter steuern. | [humidifier](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/humidifier.md) |
| Light | Licht schalten und Helligkeit steuern. | [light](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/light.md) |
| Lock | Schloss anzeigen und steuern. | [lock](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/lock.md) |
| Media player | Medienplayer anzeigen und bedienen. | [media-player](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/media-player.md) |
| Number | Number-Entitaeten anzeigen und setzen. | [number](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/number.md) |
| Person | Personenstatus anzeigen. | [person](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/person.md) |
| Select | Select-Entitaeten anzeigen und Wert auswaehlen. | [select](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/select.md) |
| Template | Eigene Inhalte ueber Templates darstellen. | [template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/template.md) |
| Title | Titel, Untertitel und Abschnittsueberschriften anzeigen. | [title](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/title.md) |
| Update | Update-Entitaeten anzeigen und Aktionen anbieten. | [update](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/update.md) |
| Vacuum | Staubsaugerroboter anzeigen und steuern. | [vacuum](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/vacuum.md) |

## Legacy-Karte

| Karte | Zweck | Original |
| --- | --- | --- |
| Legacy Template | Aeltere Template Card, weiterhin nutzbar, aber nicht im Card Picker sichtbar. | [legacy-template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/legacy-template.md) |

## Badge

| Badge | Zweck | Original |
| --- | --- | --- |
| Template Badge | Template-basiertes Badge fuer Home Assistant ab 2024.8. | [template badge](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/badges/template.md) |

## Grundschema

Viele Mushroom Cards folgen diesem Muster:

```yaml
type: custom:mushroom-entity-card
entity: light.wohnzimmer
name: Wohnzimmer
icon: mdi:lightbulb
```

Der konkrete `type` haengt von der Karte ab, zum Beispiel `custom:mushroom-light-card`, `custom:mushroom-climate-card` oder `custom:mushroom-template-card`.
