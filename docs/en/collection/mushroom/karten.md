---
title: Mushroom cards
description: Complete overview of Mushroom Cards, Legacy Card and Badge.
---
<a id="mushroom-karten"></a>
<a id="current-focus"></a>

# Cards {#karten}

This list shows the cards and badges linked in the Mushroom README.

## Active cards {#aktive-karten}

| card | Purpose | Original |
| --- | --- | --- |
| Alarm control panel | View and control alarm system. | [alarm-control-panel](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/alarm-control-panel.md) |
| Chips | Display small status and action chips. | [chips](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/chips.md) |
| Climate | Control climate entities. | [climate](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/climate.md) |
| Cover | Control roller blinds, garage doors, curtains or other covers. | [cover](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/cover.md) |
| Entity | Show individual entity compactly. | [entity](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/entity.md) |
| Empty | Use empty space or spacers. | [empty](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/empty.md) |
| Fan | Control fan. | [fan](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/fan.md) |
| Humidifier | Control humidifier. | [humidifier](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/humidifier.md) |
| Light | Switch lights and control brightness. | [light](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/light.md) |
| Lock | View and control lock. | [lock](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/lock.md) |
| Media player | View and operate media players. | [media player](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/media-player.md) |
| Number | Show and set Number entities. | [number](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/number.md) |
| person | Show person status. | [person](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/person.md) |
| Select | Show select entities and select value. | [select](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/select.md) |
| Template | Display your own content using templates. | [template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/template.md) |
| Title | Show titles, subtitles and section headings. | [title](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/title.md) |
| Update | Show update entities and offer actions. | [update](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/update.md) |
| Vacuum | View and control vacuum cleaner robots. | [vacuum](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/vacuum.md) |

## Legacy card {#legacy-karte}

| card | Purpose | Original |
| --- | --- | --- |
| Legacy Template | Older template card, still usable, but not visible in the card picker. | [legacy-template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/legacy-template.md) |

## Badge {#badge}

| Badge | Purpose | Original |
| --- | --- | --- |
| Template Badge | Template-based badge for Home Assistant from 2024.8. | [template badge](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/badges/template.md) |

## Basic scheme {#grundschema}

Many mushroom cards follow this pattern:

```yaml
type: custom:mushroom-entity-card
entity: light.wohnzimmer
name: Wohnzimmer
icon: mdi:lightbulb
```

The specific `type` depends on the card, for example `custom:mushroom-light-card`, `custom:mushroom-climate-card` or `custom:mushroom-template-card`.
