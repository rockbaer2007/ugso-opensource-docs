---
title: UGSo Special
description: Lignes SVG animées et nœuds de sommation pour ioBroker VIS 2.
---

# UGSo Special

**UGSo Special** permet de visualiser des flux de données dans VIS 2, par exemple la puissance de plusieurs appareils. Le pack contient deux widgets.

## Widgets

- **SVG-Line** relie des points par un tracé droit, à angle droit ou passant par des points intermédiaires. Les couleurs, les longueurs des tirets et les pointes de flèche sont réglables. Une valeur positive anime la ligne vers l’avant, une valeur négative inverse le sens et une valeur nulle arrête l’animation. La vitesse peut être fixe ou proportionnelle à la valeur absolue.
- **SVG LineBox** additionne jusqu’à quatre entrées et une valeur de correction facultative. Le total peut être transmis à deux lignes de sortie au maximum ou écrit, dans la vue d’exécution, dans un état numérique existant et modifiable sous `0_userdata.0`. Si une entrée sélectionnée est indisponible, le nœud attend sa valeur.

Dans l’éditeur, faites glisser une extrémité jaune pour l’aimanter à une autre ligne ou à une LineBox. Une extrémité munie d’une flèche ne peut pas s’aimanter. L’aimantation aligne le dessin ; le transfert des valeurs se configure séparément dans la LineBox.

## Installation

### Préparation du catalogue 0.1.34

Cette version comprend des notes de version dans les onze langues du catalogue, des dépendances corrigées, une analyse statique automatisée et les contrôles de paquet ioBroker. Les publications utilisent GitHub Actions avec une attestation de provenance npm. bluefox figure parmi les copropriétaires npm. L’admission au catalogue officiel reste en cours ; les fonctions des widgets et les projets existants sont conservés.

Le paquet s’appelle désormais `iobroker.vis-2-widgets-ugso-special`.
Exportez vos projets VIS 2 pour les sauvegarder, installez le nouveau paquet
et redémarrez VIS 2. Vérifiez les projets avant de supprimer l’ancien paquet.
Les identifiants des modèles de widgets et le nom interne de fédération sont conservés.

Une installation VIS 2 opérationnelle est nécessaire. Installez le pack via son URL GitHub dans ioBroker Admin (mode expert). Après une mise à jour, redémarrez VIS 2 pour charger la nouvelle version. Les deux widgets figurent dans la palette de l’éditeur sous **UGSo Special**.

- [GitHub](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special)
- [Releases](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special/releases)
- [npm](https://www.npmjs.com/package/iobroker.vis-2-widgets-ugso-special)
