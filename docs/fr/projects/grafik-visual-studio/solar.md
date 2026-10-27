---
title: Solaire – Onduleurs et batteries empilables
description: Modules SVG neutres dotés de points de connexion affleurants, d'affichages textuels et de ports de flux de données librement assignables.
---

# Solaire {#solar}

**Solar 0.1.3** nécessite **Studio 0.1.280 ou une version ultérieure**. Cet ensemble de widgets autonome comprend quatre modules indépendants de toute marque, dotés de graphismes SVG transparents. Mettez d'abord à jour Studio, puis importez le [fichier de paquet ugso.solar.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/solar/ugso.solar.wg) via les paramètres des paquets.

| Widget | Taille standard | Points de connexion | Points de ligne |
| --- | --- | --- | --- |
| Élément supérieur (pile) | 256 × 64 px | En bas, au centre | À gauche/droite, ainsi que deux entrées pour panneaux solaires de chaque côté du boîtier |
| Module batterie | 256 × 169 px | En haut et en bas, au centre | À gauche, à droite |
| Onduleur Solo | 144 × 103,3 px | Aucune | À gauche/droite/en haut au centre, ainsi que sept points en bas, coins inclus |
| Panneau solaire avec pied | 320 × 288 px | Aucune | Une sortie : au niveau du mât ou sur le bord gauche/droite du widget |

Le graphique de l'élément principal est positionné au centre, sur le bord inférieur du widget. La batterie s'aligne parfaitement avec le graphique, en haut comme en bas. La batterie et l'onduleur Solo conservent leurs proportions lors d'un agrandissement ou d'une réduction. Le boîtier visible de l'onduleur Solo est environ un tiers plus étroit que l'élément principal.

![Système solaire dans l'éditeur : empilement de batteries, onduleur Solo et les deux orientations possibles pour le panneau solaire](/images/grafik-visual-studio/solar-overview.png)

Exemple avec des valeurs de prévisualisation et les points de connexion affichés. Les cercles jaunes représentent les entrées, les cercles bleus les sorties, et les carrés violets les points de couplage entre boîtiers. Ces points disparaissent lors de l'exécution (runtime).

## Panneau solaire avec mât et pied {#solarpanel-mit-standrohr-und-fuß}

Sous **Module solaire → Orientation**, vous pouvez choisir **Comme le modèle** ou **Miroir**. Le graphique SVG est alors inversé horizontalement ; le texte et l'affichage des valeurs restent lisibles. Les proportions sont préservées lors du redimensionnement.

![Panneau solaire avec mât et pied : à gauche identique au modèle, à droite en miroir ; sortie située sur le mât dans les deux cas](/images/grafik-visual-studio/solar-panel-variants.png)

Sélectionnez une entité Home Assistant sous **Puissance → Entité d'entrée (Puissance)**. Les valeurs exprimées en kW sont converties en W. L'option **Afficher la valeur** masque uniquement le texte (sans cadre) ; la sortie continue toutefois de transmettre des données. En l'absence d'entité, la valeur de prévisualisation est utilisée ; si l'entité est inconnue, un tiret s'affiche.

Sous **Connexion de ligne → Position du point de départ**, trois options sont disponibles : **Sur le tube vertical au-dessus du pied**, **Bord gauche du widget** et **Bord droit du widget**. Les positions sur les bords se situent à la même hauteur que le point sur le tube. Il n'y a qu'une seule sortie ; les lignes SVG déjà connectées s'ajustent automatiquement en cas de modification. L'option **Point de départ actif** permet d'activer ou de désactiver ce point. En mode exécution (runtime), le point est invisible, tandis que la ligne SVG reste visible. Le panneau solaire ne dispose pas de points de connexion sur son boîtier.

## Assembler une pile {#einen-stapel-zusammensetzen}

Ajoutez **un élément supérieur** (en-tête) ainsi que, selon votre installation, **1 à 6 instances du même widget de batterie**. Chaque batterie possède ses propres paramètres et entités. Les points de connexion centraux du boîtier sont activés par défaut, avec un espacement de **0 px**. Faites glisser une batterie en reliant son point supérieur au point inférieur de l'élément supérieur ou d'une autre batterie. Les éléments s'alignent automatiquement de manière centrée et jointive.

Sous **Points d'accrochage du boîtier**, vous pouvez configurer l'accrochage (snapping), les points individuels, l'espacement et l'affichage permanent dans l'éditeur. Les points de connexion du boîtier servent uniquement au positionnement ; ils ne transmettent aucune valeur. Ces points sont invisibles en mode exécution (runtime).

## Valeurs affichées sous forme de texte sur le boîtier {#werte-als-text-auf-dem-gehause}

Pour la **puissance**, la **température** et l'**état de charge (SoC)**, une sélection d'entité Home Assistant ainsi qu'une valeur de prévisualisation sont disponibles pour chaque paramètre. Les unités utilisées sont le **W**, le **°C** et le **%**. La puissance issue d'une entité exprimée en kW est convertie en W. La valeur de prévisualisation ne s'affiche que tant qu'aucune entité n'est renseignée. Les états manquants ou inconnus sont représentés par **—**.

L'option **Afficher la valeur** permet de désactiver uniquement l'affichage textuel correspondant. L'entité continue d'être mise à jour et les sorties continuent de transmettre leur valeur. Dans le cas de la batterie, les indicateurs actifs s'affichent juste en dessous de la ligne de séparation située après le premier tiers ; ils sont disposés automatiquement les uns en dessous des autres, sans espaces vides pour les éléments masqués. Il n'y a ni cadre ni encadré d'affichage. L'ordre est le suivant : puissance, température, SoC. La couleur et la taille maximale de la police sont réglables ; si l'espace est restreint, la taille de la police est réduite.

Par défaut, la batterie affiche les trois valeurs, tandis que le modèle « Solo » n'affiche que la puissance. L'en-tête n'affiche aucune valeur et ne propose pas de regroupement pour la puissance, la température, le SoC ou le sens du flux de puissance. Ces paramètres sont conservés pour l'onduleur « Solo ».

Pour la batterie, il est possible de définir séparément la **couleur de la police** des valeurs affichées pour la **puissance**, la **température** et l'**état de charge (SoC)**. Si aucune couleur spécifique n'est définie, la couleur de police générale s'applique. La couleur est conservée même lorsque l'affichage est masqué puis réaffiché.

![En-tête empilable avec quatre entrées pour panneaux solaires et une batterie affichant des valeurs en couleur, ainsi que des points de connexion latéraux sur le bord inférieur](/images/grafik-visual-studio/solar-stack-ports.png)

Dans la section **Sens de la puissance**, vous pouvez activer un symbole directionnel. Définissez si une puissance positive correspond à un **flux d'énergie entrant** ou **sortant**, et choisissez les symboles correspondants via des champs de saisie de texte libre. En cas de puissance nulle ou de valeur inconnue, aucun symbole directionnel n'est affiché. Le signe de la valeur numérique est conservé.

## Entrées et sorties pour les lignes SVG {#ein-und-ausgange-fur-svg-linien}

L'**onduleur « Solo »** dispose, sur son bord inférieur, de sept points de connexion répartis uniformément : les deux coins, le point central (existant précédemment) et deux points supplémentaires de chaque côté de celui-ci. En incluant les points situés au centre des côtés gauche, droit et supérieur, on obtient un total de dix points de connexion. Dans la section **Connexions de lignes**, vous pouvez définir, pour chaque point, s'il s'agit d'une **entrée** ou d'une **sortie** (ou s'il est **désactivé**), et spécifier la valeur associée. Les six nouveaux points situés en bas sont désactivés par défaut ; les connexions et liaisons déjà existantes restent inchangées.

![Onduleur « Solo » avec sept points de connexion sur le bord inférieur et trois points supplémentaires situés à gauche, à droite et en haut](/images/grafik-visual-studio/solar-solo-ports.png)

Dans cet exemple, les dix points sont configurés comme sorties ; dans votre propre projet, vous pouvez choisir le rôle de chaque point individuellement.

Pour la batterie, une **position** supplémentaire est disponible à gauche et à droite : **bord central du widget** ou **bord du boîtier au niveau de la jointure inférieure**. Les deux côtés peuvent être configurés indépendamment. Les connexions existantes sont conservées ; le rôle (entrée/sortie) et l'affectation des valeurs restent inchangés. Les points de connexion centraux du boîtier (en haut et en bas), utilisés pour l'empilement, ne sont pas affectés par ce changement.

L'élément supérieur (tête) dispose de quatre connecteurs visuels pour panneaux solaires : en haut et en bas, à gauche comme à droite. Ces quatre entrées sont actives par défaut et peuvent être désactivées individuellement dans la section **Connexions de lignes**. Elles suivent le tracé graphique aligné sur la partie inférieure, quelle que soit la hauteur du widget. Reliez la ligne SVG d'un panneau solaire à l'un de ces connecteurs. Les entrées constituent des cibles de ligne distinctes ; les valeurs ne sont pas additionnées automatiquement. L'ancien point de connexion supérieur est supprimé, tandis que les points de connexion situés à gauche et à droite restent disponibles.

Dans la section **Connexions de lignes**, chaque côté disponible propose deux réglages :

- **Rôle :** Désactivé, Entrée ou Sortie. Par défaut, les points de connexion sont désactivés.
- **Valeur :** Puissance, Température ou État de charge (SoC).

Une **sortie** transmet la valeur sélectionnée, accompagnée de son unité, par exemple vers un élément *Number* ou une ligne SVG. Une **entrée** récupère cette valeur depuis une source unique connectée et remplace l'entité pour ce canal. N'utilisez qu'une seule entrée par valeur. Une autre sortie peut relayer la valeur ainsi récupérée ; les boucles de rétroaction sont gérées (interceptées). Aucune entité Home Assistant n'est modifiée.

Les points de ligne sont indépendants des points de connexion du boîtier. Les sorties actives utilisent la couleur définie pour les points de sortie dans les paramètres du Studio. En mode exécution (*runtime*), ces points disparaissent ; les lignes SVG classiques restent visibles, tandis que les connexions de valeurs demeurent invisibles.

Tous les groupes CSS standard sont disponibles ; les sections optionnelles sont désactivées par défaut. L'ajout de marges internes (*padding*) ou de bordures peut altérer l'alignement affleurant.

Les éléments SVG sont des graphismes UGSo spécifiques, dépourvus de logo de fabricant. [Code source, instructions de montage et licence MIT](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/solar).
