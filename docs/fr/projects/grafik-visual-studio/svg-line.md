---
title: SVG-Line – Dessiner et animer des lignes de connexion
---

# SVG-Line {#svg-line}

## Modifications jusqu'à la version Studio 0.1.285 {#anderungen-bis-studio-0-1-285}

- La **position de départ verticale**, située sous la rubrique **Ligne**, s'applique aussi bien aux *SVG-Line* qu'aux connexions de valeurs. Si l'option n'est pas cochée, une ligne libre débute horizontalement. Dans le cas d'un tracé automatiquement orthogonal, une ligne verticale monte ou descend d'abord, puis bifurque vers la droite ou la gauche à la hauteur de la cible. Ce comportement s'applique également aux lignes ancrées ; les points intermédiaires définis manuellement restent prioritaires.
- Le déplacement des points ne s'amorce qu'après un mouvement de souris d'au moins **6 pixels**. Les poignées individuelles ne déclenchent pas de déplacement groupé et ne sautent pas vers la position de la souris. L'autre point de connexion reste fixé. **Ctrl + Glisser** détache spécifiquement une extrémité ancrée ; **Alt + Glisser sur la ligne** déplace une ligne ancrée dans son intégralité et détache ses deux extrémités.
- Un **index Z (Z-index) de -100 ou moins** masque une ligne SVG uniquement lors de l'exécution (runtime). Elle reste modifiable dans l'éditeur et continue de transmettre des valeurs (par exemple, d'un composant « Number » vers « Math »), indépendamment de son ordre d'affichage dans l'éditeur.
- À partir de la version **0.1.282**, une sortie active de type « Gauge/Potentiomètre » ou « Linear » fournit directement la vitesse et la direction de la ligne SVG connectée, sans nécessiter d'entité numérique intermédiaire. Utilisez le paramètre **« Poti / SVG LineBox-Teiler » (diviseur)** : une valeur de 10 avec un diviseur de 10 donne 1 cycle/s ; une valeur de 20 avec un diviseur de 10 donne 2 cycles/s. Une valeur de zéro arrête l'animation, tandis que des valeurs négatives l'inversent. Avec un diviseur de 1, toute valeur égale ou supérieure à 20 atteint la vitesse maximale de 20 cycles/s. Pour obtenir une vitesse dépendante de la valeur, désactivez l'ajustement automatique du diviseur ; lorsqu'il est activé, ce mécanisme maintient volontairement la vitesse cible constante. Les connexions de valeurs en elles-mêmes ne comportent pas d'animation.

Vous trouverez la structure ainsi qu'une démonstration animée en cours d'exécution dans la [Galerie](/fr/projects/grafik-visual-studio/bildergalerie).

À partir de la version Studio 0.1.136, une fonction d'**ajustement automatique du diviseur** est disponible pour les entités numériques et les sorties « LineBox ». Elle permet de maintenir une vitesse d'animation constante, même lorsque les valeurs (puissances) varient. La configuration et le calcul sont expliqués ci-dessous, dans la section **Ajustement automatique du diviseur : comment et pourquoi**.

Vous trouverez **SVG-Line** sous la rubrique **HA Grafik – Spezial**. Ce widget permet de relier visuellement d'autres widgets, de faire passer des lignes par des angles et d'animer un flux de données. Une ligne peut commencer et se terminer au niveau des points d'ancrage d'un widget, sur un point de regroupement (« Sammelpunkt ») explicitement activé d'une autre SVG-Line, ou à des coordonnées libres. Il ne s'agit pas, en soi, d'une entité Home Assistant ; une entité optionnelle permet de piloter son animation.

## Connexion et points d'ancrage {#verbindung-und-andockpunkte}

1. Ajoutez un élément SVG-Line. Sélectionnez-le dans l'éditeur ; le début et la fin apparaissent sous forme de cercles déplaçables.
2. Sur le widget cible, activez les **points d'ancrage** et sélectionnez les positions souhaitées. Sur les nouveaux widgets, ces douze points sont désactivés par défaut : à gauche et à droite (en haut, au milieu et en bas) ; en haut et en bas (à 1/4, au milieu et aux 3/4). L'option **Tous les points** permet de les activer ou désactiver simultanément. Plusieurs lignes peuvent occuper le même point.
3. Faites glisser une extrémité de la ligne vers un point d'ancrage actif. Vous pouvez également définir le widget et le point d'ancrage correspondants dans les sections **Début** et **Fin**. L'option **Ou point de regroupement actif** permet de sélectionner un point de regroupement appartenant à une autre SVG-Line, tandis que **X/Y libre** permet de positionner une extrémité sans contrainte de rattachement.

| Manipulation | Effet |
| --- | --- |
| Déplacer une extrémité libre | Modifie le début ou la fin de la ligne. Les touches fléchées permettent de déplacer un point sélectionné de 1 pixel ; l'utilisation de `Umschalt` permet un déplacement de 10 pixels. |
| Déplacer une extrémité ancrée avec `Strg` | Rompt la connexion et déplace le point. L'utilisation de `Strg` combinée à une touche fléchée permet également cette opération. |
| Déplacer un point intermédiaire | Modifie le tracé d'une ligne composée de plusieurs segments. |
| Déplacer la ligne entière | Déplacement direct pour une ligne libre ; utilisation de `Alt` pour une ligne ancrée. Déplace la ligne dans son intégralité, en supprimant les ancrages existants au niveau du point de départ ou d'arrivée. |
| Cliquer sur la ligne (sans la faire glisser) | Ouvre un menu permettant de choisir entre **Point intermédiaire**, **Point de regroupement** ou **Point de couplage de valeur** ; le point est inséré après validation par **OK**. |

## Tracé et points de regroupement {#pfad-und-sammelpunkte}

### Point de couplage de valeur pour un affichage libre {#wert-koppelpunkt-fur-eine-freie-anzeige}

À partir de la version **0.1.275**, un troisième type de point est disponible : le **point de couplage de valeur**. Il restitue la valeur associée à la ligne SVG, telle que la valeur numérique de son entité d'animation ou la valeur provenant de sa source connectée. Dans l'éditeur, il est représenté par un octogone ; sa couleur se règle via **Paramètres → Point de couplage de valeur**. Il s'agit exclusivement d'un point de sortie ; il ne peut donc pas servir de destination pour une ligne.

À partir de la version **0.1.281**, le point de couplage de valeur ne peut être déplacé que **le long du tracé visible de la ligne**. Lors du déplacement, il reste calé sur le point le plus proche de la ligne, y compris sur les courbes et les angles arrondis. Il ne modifie ni le tracé de la ligne ni le type de chemin sélectionné ; seuls les points intermédiaires et les points de regroupement définissent le chemin. Une fois déplacé, la connexion d'affichage sortante s'ajuste automatiquement à la nouvelle position. Les points existants situés à côté de la ligne, ainsi que les positions saisies manuellement, sont replacés sur le chemin.

1. Sélectionnez la ligne SVG, cliquez à nouveau à l'endroit souhaité et insérez un **point de couplage de valeur**.
2. Placez un widget **Number** (Nombre) librement à côté, au-dessus ou en dessous de la ligne. Dans la section **Flux de données**, activez son **point d'entrée** et définissez son côté.
3. Créez une connexion. Sous **Début → Point de regroupement ou de couplage de valeur**, sélectionnez le nouveau point (ou faites glisser l'extrémité de la connexion sur celui-ci). Reliez ensuite la destination à l'entrée du widget Number.

Le point et la connexion sortante sont automatiquement invisibles lors de l'exécution (runtime), mais le transfert de valeur reste actif. La ligne SVG d'origine demeure visible. Le widget **String** (Chaîne de caractères) peut être utilisé de la même manière pour afficher une valeur textuelle issue du flux de données. Les **points de ligne** permettent de modifier ultérieurement le nom, la position et le type de point. Les valeurs inconnues ne sont pas remplacées par une valeur nulle arbitraire.

Sous **Tracé et points de jonction**, on trouve quatre **types de tracé** : **Ligne droite**, **Angle droit automatique**, **Courbe** et **Tracé manuel en zigzag/à points multiples**. Le **rayon d'angle** permet d'arrondir les angles du tracé. La section **Points intermédiaires et points de jonction** permet de nommer, placer et modifier des points. L'ajout d'un point intermédiaire ou d'un point de jonction par un simple clic fait passer la ligne en mode manuel à points multiples.

Un **point intermédiaire** se contente de créer un coude dans le tracé. Un **point de jonction**, lorsqu'il est activé, sert de point de connexion potentiel pour d'autres lignes SVG. Pour effectuer la connexion, faites glisser l'extrémité libre de la ligne vers le point de jonction visible, ou sélectionnez ce dernier dans les propriétés. Plusieurs lignes peuvent utiliser le même point de jonction. Un simple croisement ou contact ne crée pas de liaison entre les lignes. Un point de jonction désactivé n'accepte aucune nouvelle connexion.

## Ligne et pointes de flèche {#linie-und-pfeilspitzen}

| Groupe | Options de configuration |
| --- | --- |
| **Ligne** | **Couleur de base**, **couleur d'animation**, **épaisseur** (1–40 px), **opacité**, **type de ligne** (continue, en pointillés, en tirets), **longueur des tirets**, **espacement** entre les tirets/points et **extrémités de ligne** (arrondies, plates, carrées). |
| **Pointes de flèche** | **Au début** et **à la fin** (indépendantes) : aucune, flèche pleine, flèche ouverte ou cercle. La **taille** et la **couleur** s'appliquent aux marqueurs. Si le sens du flux est inversé, les marqueurs affichés changent de côté. |

## Animation et source de direction {#animation-und-richtungsquelle}

Activez l'option **Activer l'animation** et choisissez un **type d'animation** : flux bicolore, tirets en mouvement, pulsation ou point lumineux. Sous **Source de direction**, une seule variante est active à la fois :

| Source | Direction et vitesse |
| --- | --- |
| **Manuel** | **Direction** : du début vers la fin ou de la fin vers le début ; **durée** : de 0,2 à 20 secondes par cycle. En cas de connexion à un point de convergence, le flux manuel s'oriente vers ce point. |
| **Entité numérique** | Les valeurs positives génèrent un mouvement du début vers la fin, les valeurs négatives dans le sens inverse ; la valeur `0` arrête le flux. La valeur absolue divisée par le **diviseur** (par défaut : `1`) donne le nombre de cycles par seconde (limite : 0,05 à 20). Exemple : `1000 W ÷ 100 = 10` cycles/s. |
| **Entité booléenne** | `on`/`true`/`1` s'exécute vers l'avant, `off`/`false`/`0` vers l'arrière. L'option **Inverser la direction (booléen)** échange cette affectation. La **durée** définie détermine la cadence. |

Des états d'entité manquants ou invalides interrompent l'animation. L'entité sélectionnée est mise à jour dans l'éditeur et lors de l'exécution (runtime). La **SVG LineBox** peut transmettre le signe et la valeur absolue de sa valeur calculée à la ligne, via un point d'ancrage configuré comme sortie. Cette transmission est prioritaire sur la source de direction choisie. La ligne de sortie nécessite toujours l'activation de l'option **Activer l'animation** ; en présence de `0` ou en l'absence d'entrée valide, elle reste immobile. Le paramètre **Diviseur SVG LineBox (lors de la transmission)** détermine alors sa cadence, tandis que ses propres couleurs et son type de ligne sont conservés. [Explication détaillée de la SVG LineBox](/fr/projects/grafik-visual-studio/svg-linebox).

## Ajustement automatique du diviseur : comment et pourquoi {#automatische-teileranpassung-wie-und-warum}

Avec un diviseur fixe, la vitesse augmente proportionnellement à la valeur d'entrée. Si l'on utilise le diviseur `100`, par exemple, `10 W` ne produit que `0,1` cycles/s, alors que `1500 W` en produit déjà `15` cycles/s. Un diviseur plus élevé permet de modérer les puissances élevées (comme celles d'un système de chauffage ou d'une plaque de cuisson), mais rend les petites valeurs très lentes. À l'inverse, un diviseur plus faible accélère les petites valeurs, mais peut rendre les grandes valeurs difficiles à distinguer lors de l'animation.

Le mode automatique ajuste donc le diviseur en fonction de la **vitesse cible** choisie, à chaque modification de la valeur. Il n'utilise pas de paliers de puissance fixes et fonctionne également au-delà de 15.000. La relation est la suivante :

```text
Automatischer Teiler = Betrag des Eingangswerts / Zielgeschwindigkeit
Animationsgeschwindigkeit = Betrag des Eingangswerts / automatischer Teiler
```

Pour **1 cycle/s**, on obtient les valeurs suivantes :

| Valeur d'entrée | Diviseur automatique | Vitesse |
| --- | --- | --- |
| 10 | 10 | 1 cycle/s |
| 100 | 100 | 1 cycle/s |
| 1500 | 1500 | 1 cycle/s |
| 15.000 | 15.000 | 1 cycle/s |

Ainsi, le flux reste tout aussi bien perceptible, qu'il s'agisse de faibles ou de fortes puissances. Lorsque le mode automatique est activé, la vitesse affichée correspond à la vitesse cible choisie ; il n'est donc plus possible de déduire le niveau de puissance à partir de cette seule information. Le signe continue de déterminer la direction. La valeur `0`, l'absence de valeur ou des états invalides entraînent l'arrêt de l'animation.

### Configuration {#einrichten}

1. Sélectionnez la ligne SVG et, sous la rubrique **Animation**, cochez **Activer l'animation**.
2. Si vous utilisez une source numérique (Home Assistant), sélectionnez **Source de direction → Entité numérique**, saisissez l'entité concernée et activez l'option **Ajuster automatiquement le diviseur (entité numérique)**.
3. Si vous utilisez une sortie connectée provenant de **SVG LineBox** ou de [**SVG LineBox Math**](/fr/projects/grafik-visual-studio/svg-linebox-math), activez plutôt l'option **Ajuster automatiquement le diviseur (SVG LineBox)**. Ce mode de transmission de valeur est prioritaire sur la source de direction choisie. 4. Réglez la **vitesse cible** correspondante. La valeur par défaut est de **1 cycle/s** ; les valeurs autorisées sont comprises entre **0,05 et 5 cycles/s**. Avec `0,5`, un cycle dure deux secondes ; avec `2`, il dure une demi-seconde. Commencez avec `1` et ajustez la valeur en fonction du type de ligne et de l'espacement des traits.

Les deux modes automatiques sont indépendants et désactivés par défaut. Le **diviseur** manuel correspondant est mémorisé ; il est réutilisé lorsque le mode automatique est désactivé. Les modes **Manuel** et **Entité booléenne** continuent d'utiliser leur durée définie. Une animation de ligne principale héritée reste appliquée aux lignes secondaires normales ; une valeur LineBox transmise activement détermine elle-même le rythme de la ligne de sortie concernée.

Le nombre de cycles par seconde correspond aux répétitions de l'animation, et non à une vitesse en pixels. Le type de ligne, le type d'animation et l'espacement des traits influencent le résultat visuel. Le mode automatique assure un rythme stable ; la vitesse cible appropriée peut donc être réglée individuellement pour chaque ligne.

## Ligne principale, intersections et niveaux {#hauptlinie-kreuzungen-und-ebenen}

La fonction **Ligne principale / Groupe de flux** permet d'associer une ligne à une autre. L'option **Reprendre le rythme d'animation de la ligne principale (conserver ses propres couleurs)** applique le rythme et le type d'animation de la ligne principale, tout en permettant à la ligne secondaire de conserver sa propre couleur pendant l'animation du flux. La **Synchronisation** propose les modes **Même rythme** et **Arrivée synchronisée au point de convergence**. En cas de connexion directe à un point de convergence situé sur une ligne principale non animée, la ligne secondaire s'arrête également et affiche sa couleur de base, pointes de flèches incluses. Une fois la connexion supprimée, les paramètres propres à la ligne sont rétablis.

Les paramètres **Croisement et z-index** permettent de gérer l'affichage des intersections via les options **Superposition**, **Lacune** ou **Pont / Arche**, ainsi que de définir l'empilement (z-index) via les modes **Automatique**, **Au-dessus**, **En dessous** ou **Manuel**. Un élément doté d'un z-index plus élevé s'affiche visuellement devant un élément ayant un z-index plus faible. L'option **Laisser passer les clics** influe sur l'interactivité lors de l'exécution (runtime). La gestion des croisements et le z-index ne créent pas de connexion physique entre les lignes ; pour cela, il est nécessaire d'utiliser un point de convergence ou le composant [SVG LineBox](/fr/projects/grafik-visual-studio/svg-linebox).

La fonctionnalité SVG-Line est encore au stade expérimental ; le rendu des croisements et des animations synchronisées peut varier en fonction du tracé et du navigateur utilisé.
