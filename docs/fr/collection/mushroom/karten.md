---
title: Cartes Mushroom
description: Aperçu complet des cartes Mushroom, de la carte « Legacy » et des badges.
---
<a id="mushroom-karten"></a>
<a id="orientation-actuelle"></a>

# Cartes {#karten}

Cette liste reprend les cartes et badges mentionnés dans le fichier README de Mushroom.

## Cartes actives {#aktive-karten}

| Carte | Utilité | Original |
| --- | --- | --- |
| Alarm control panel | Afficher et contrôler le système d'alarme. | [alarm-control-panel](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/alarm-control-panel.md) |
| Chips | Afficher de petits éléments (chips) d'état ou d'action. | [chips](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/chips.md) |
| Climate | Contrôler les entités de climatisation/chauffage. | [climate](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/climate.md) |
| Cover | Contrôler des volets, portes de garage, rideaux ou autres dispositifs d'ouverture/fermeture. | [cover](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/cover.md) |
| Entity | Afficher une entité unique de manière compacte. | [entity](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/entity.md) |
| Empty | Créer un espace vide ou un espacement. | [empty](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/empty.md) |
| Fan | Contrôler un ventilateur. | [fan](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/fan.md) |
| Humidifier | Contrôler un humidificateur. | [humidifier](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/humidifier.md) |
| Light | Allumer/éteindre une lumière et en régler la luminosité. | [light](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/light.md) |
| Lock | Afficher et contrôler une serrure. | [lock](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/lock.md) |
| Media player | Afficher et piloter un lecteur multimédia. | [media-player](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/media-player.md) |
| Number | Afficher et définir des entités de type « nombre » (number). | [number](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/number.md) |
| Person | Afficher le statut d'une personne. | [person](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/person.md) |
| Select | Afficher des entités de type « sélection » (select) et choisir une valeur. | [select](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/select.md) |
| Template | Afficher du contenu personnalisé via des modèles (templates). | [template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/template.md) |
| Title | Afficher des titres, sous-titres et en-têtes de section. | [title](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/title.md) |
| Update | Afficher des entités de type « mise à jour » (update) et proposer des actions. | [update](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/update.md) |
| Vacuum | Afficher et contrôler un aspirateur robot. | [vacuum](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/vacuum.md) |

## Carte héritée (Legacy) {#legacy-karte}

| Carte | Usage | Original |
| --- | --- | --- |
| Modèle hérité (Legacy Template) | Carte basée sur un modèle ancien ; toujours utilisable, mais n'apparaît pas dans le sélecteur de cartes. | [legacy-template](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/legacy-template.md) |

## Badge {#badge}

| Badge | Usage | Original |
| --- | --- | --- |
| Badge basé sur un modèle (Template Badge) | Badge pour Home Assistant basé sur un modèle, à partir de 2024.8. | [template badge](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/badges/template.md) |

## Structure de base {#grundschema}

De nombreuses cartes Mushroom suivent ce modèle :

```yaml
type: custom:mushroom-entity-card
entity: light.wohnzimmer
name: Wohnzimmer
icon: mdi:lightbulb
```

La valeur spécifique `type` dépend de la carte ; il peut s'agir, par exemple, de `custom:mushroom-light-card`, `custom:mushroom-climate-card` ou `custom:mushroom-template-card`.
