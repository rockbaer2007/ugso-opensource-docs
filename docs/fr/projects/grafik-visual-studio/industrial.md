---
title: Widgets industriels
description: Installation et configuration du pack industriel externe pour Grafik Visual Studio.
---

# Widgets industriels {#industrie-–-widgets}

Le pack de widgets externes **Industrie 0.11.6** contient seize widgets : **Jauge/Potentiomètre – 270°**, **Interrupteur à bascule – 1 à 4**, **Interrupteur à levier (type bascule) – 1 à 4**, **LCD – 20×4**, **LCD – 16×2**, **Jauge linéaire / Curseur** et **Compteur** (versions standard et étroite), **LED 7 segments**, **LED 16 segments**, **LCD 16 segments**, **Horloge industrielle – Nixie / LED / LCD**, **Météo industrielle – LCD / LED**, **Élément factice (cache)** ainsi que **Chauffage – Chaudière et réservoir de fioul**. Le style industriel inclut des boîtiers, des têtes de vis et des cadres. Le widget de chauffage, avec ses graphismes détaillés, nécessite **Studio 0.1.253 ou une version ultérieure**.

**Note sur la mise à jour :** La version 0.11.4 ne pouvait pas être installée par-dessus une installation existante en raison de modifications apportées aux libellés des widgets. Utilisez plutôt **0.11.5** (en tant que fichier local `.wg`) ; cela permet de préserver les contrats de widgets publiés ainsi que les liaisons avec les entités. Studio **0.1.259** affiche les paramètres de départ (température de départ) sous leur nouvelle dénomination, sans modifier les clés de groupe enregistrées.

## Images {#bilder}

| Potentiomètre avec échelle graduée | Jauge avec anneau coloré |
| --- | --- |
| ![Potentiomètre industriel avec échelle graduée et affichage de la valeur en bas](/images/grafik-visual-studio/industrial-poti.png) | ![Jauge industrielle avec anneau coloré et affichage de la production solaire au centre](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| Sans entrée : cadran rotatif virtuel avec une échelle commençant par une valeur négative et affichant **15 °C** sous le bouton. | Avec entrée : puissance solaire de **823 W** sur une échelle de 0 à 1000 W, avec des zones colorées et l'affichage de la valeur au centre. |

Les images illustrent l'exécution avec des données d'exemple ; il ne s'agit pas de mesures en temps réel.

## Installation {#installation}

Tous les champs d'entité de l'ensemble disposent d'un bouton « **…** » permettant d'ouvrir le **sélecteur d'entités de Home Assistant**. Recherchez l'entité souhaitée, sélectionnez-la, puis cliquez sur **Insérer** pour l'ajouter au champ actif. À partir de la version **Studio 0.1.250**, cela s'applique également aux champs **Entrée : Entité** et **Sortie : Entité** pour chaque canal de commutateur (interrupteur/bascule). La sélection est alors associée au canal correspondant. Pour les packs déjà installés, une simple mise à jour de Studio suffit.

[Téléchargez le fichier du pack](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) et installez-le via **Paramètres → Packs de widgets → Local**. Commencez par mettre à jour Studio vers la version **0.1.253 ou ultérieure**, puis installez le pack **0.11.3**. Pour bénéficier du graphique détaillé, une mise à jour de Studio suffit si vous possédez déjà le pack 0.11.1/0.11.2. Ensuite, actualisez votre navigateur en utilisant la combinaison de touches **Ctrl+F5**. Ce pack est facultatif ; il utilise l'API 0.2 et ne contient aucun code exécutable. Les seize définitions de widgets existantes sont conservées lors de la mise à jour.

[Code source et instructions du paquet sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## Chauffage – Chaudière et cuve à fioul {#heizung-–-kessel-und-oltank}

![Widget de chauffage détaillé avec températures dynamiques, deux pompes, brûleur, état de défaut et niveau de la cuve](/images/grafik-visual-studio/industrial-heating.png)

Ce modèle détaillé au format PNG transparent représente, côte à côte, une chaudière rouge foncé, deux pompes vertes, un brûleur bleu et un réservoir en cuivre. Les températures, les indicateurs d'état, le symbole d'avertissement, le niveau de remplissage du réservoir et les flèches sont des éléments SVG dynamiques. Le graphique et les indicateurs partagent le même système de coordonnées, basé sur les dimensions réelles de l'image (**1683×935**), et sont mis à l'échelle simultanément. Ainsi, les indicateurs restent positionnés sur le composant correspondant, même lors d'un déplacement ou d'un redimensionnement.

**Dimensions : 7:4 cases de grille** (largeur:hauteur), en tenant compte des espacements ajoutés autour du boîtier : avec un espacement de 1 px, les dimensions minimales sont de **460×262 px** ; la valeur par défaut est de **908×518 px**. Les widgets existants aux formats 4:6 et 6:4 sont convertis vers ce format lors de leur ouverture, tout en conservant la taille de leurs cellules de grille et leurs associations d'entités. Le graphique est fourni localement avec Studio. L'illustration présente des valeurs de test locales.

| Indicateur | Entité et paramètres |
| --- | --- |
| Température de départ | Entité numérique, masquable, couleur de texte personnalisée |
| Température de retour | Entité numérique, masquable, couleur de texte personnalisée ; affichage situé sous le tuyau orange |
| Températures (chaudière, eau chaude, eau froide) | Une entité numérique pour chaque élément, avec couleur de texte personnalisée |
| Pompe de circuit de chauffage, pompe de circulation, brûleur | Une entité booléenne pour chaque élément ; l'indicateur d'état peut être masqué séparément |
| Défaut | Entité booléenne ; symbole d'avertissement situé à côté de la température de la chaudière, masquable |
| Niveau du réservoir | Capteur numérique exprimé en pourcentage (**0–100 %**) ; indique le niveau de remplissage et la valeur chiffrée |

Les **dix entités** disposent de l'option de sélection Home Assistant. Les valeurs booléennes `on/off`, `true/false` et `1/0` sont reconnues ; l'étiquette affichée peut être configurée sur **EIN/AUS**, **ON/OFF** ou **1/0**. Les températures héritent de l'unité de l'entité et peuvent être colorées indépendamment. Les couleurs par défaut suivent le modèle : rouge pour les températures, orange pour le retour, bleu pour l'eau froide, vert pour l'état « activé », jaune pour un défaut et rose pour le niveau de remplissage.

À partir du modèle **Studio 0.1.260**, le raccord rouge situé à gauche est positionné plus haut. Le conduit de retour orange passe devant, avec une légère courbure, parallèlement au raccord de la chaudière ; sa flèche est placée à gauche et orientée vers la droite, en direction de la chaudière. Dans la section **Retour**, il est possible de configurer l'entité, l'affichage, la couleur du texte et la flèche de flux. Les widgets existants héritent de ces propriétés suite à la mise à jour du Studio ; le modèle **Industrial 0.11.6** complète la documentation tout en préservant les contrats de paquet. Les couleurs personnalisées définies pour le niveau de remplissage sont conservées ; l'ancienne couleur orange par défaut est remplacée, une seule fois, par du rose.

Les **indicateurs de flux** pour le départ, la circulation, l'eau chaude, l'eau froide, ainsi que la fine **conduite de fioul** (de couleur cuivre) menant au brûleur, peuvent être désactivés individuellement. La pompe située à droite se trouve sur une conduite verticale partant directement de la chaudière vers le haut. Les circuits d'eau chaude et d'eau froide restent distincts. Le capteur de réservoir doit fournir une valeur en pourcentage ; la conversion en litres n'est pas automatique. Les valeurs situées en dehors de la plage 0–100 % limitent uniquement l'affichage du niveau de remplissage, mais la valeur réelle reste visible sous forme numérique.

Les valeurs manquantes ou invalides sont représentées par un tiret ; un état de défaut inconnu est indiqué par un point d'interrogation. Aucune mesure n'est inventée en l'absence d'entités associées. Des **données d'exemple (sans entités réelles)** peuvent être affichées ; cette option est désactivée par défaut. Ce widget sert uniquement à l'affichage et ne transmet aucune commande. Il dispose uniquement de points d'ancrage liés au boîtier ; les options de style industriel, les vis, les cadres et les arrière-plans personnalisés sont disponibles, tout comme dans le reste de la collection.

## Élément neutre (factice) {#blindelement}

![Boîtier industriel vide surmonté d'une zone de saisie](/images/grafik-visual-studio/industrial-blank-panel.png)

Widget d'arrière-plan universel servant de boîtier ou de surface personnalisable pour accueillir des widgets issus de **n'importe quelle collection**. Il permet d'y intégrer, par exemple, des champs de saisie, des interrupteurs, des indicateurs ou d'autres éléments de commande. Dans la section **Taille**, les paramètres **Sections** (horizontal) et **Sections verticales** peuvent être réglés de **1 à 12**, formant une grille maximale de **12×12 cases**. Chaque cellule de la grille mesure au minimum 64×64 px. La largeur et la hauteur totales incluent les espacements entre les widgets individuels : avec un **espacement de 1 px tout autour**, les dimensions résultantes sont de **64 / 130 / 196 / 262 px** dans chaque direction. La saisie et le glissement permettent de redimensionner simultanément les deux directions ; la modification du nombre de segments ajuste la taille des cellules de la grille.

Seuls les quatre **points d'ancrage du boîtier** (activables individuellement) sont présents. Il n'y a aucune entité, aucun affichage de valeur ni aucune entrée/sortie de données. Le style industriel, les vis, la couleur du cadre, la largeur du cadre (ajustable en option), le rayon des angles et le CSS sont disponibles, tout comme pour les autres éléments de style industriel. La valeur par défaut **CSS z-index -1** place cet élément « aveugle » (invisible/neutre) en arrière-plan, sous les widgets classiques. Les éléments superposés restent manipulables et déplaçables indépendamment ; cet élément ne les regroupe pas automatiquement. Pour utiliser des arrière-plans personnalisés, il est possible de désactiver le style industriel et d'utiliser du CSS. L'image présente un exemple local.

## Météo (style industriel) : LCD / LED {#industrie-wetter-lcd-led}

| LCD | LED |
| --- | --- |
| ![Météo style industriel (LCD) affichant 18,6 degrés et une icône en pixels](/images/grafik-visual-studio/industrial-weather-lcd.png) | ![Météo style industriel avec affichage LED à pixels lumineux bleus](/images/grafik-visual-studio/industrial-weather-led.png) |

Les images présentent des exemples de données issus d'une entité météo simulée. L'**entité météo** intègre une entité Home Assistant (`weather.*`) : l'état est représenté par une icône dédiée (en pixels) et du texte ; la température s'affiche en grand, avec l'humidité et le vent en dessous. Les icônes couvrent les conditions suivantes : soleil, nuit claire, nuages, pluie, neige/neige fondue, grêle, orage, brouillard, vent et conditions météorologiques exceptionnelles. Les unités de température et de vent proviennent de Home Assistant et sont affichées telles quelles, sans conversion ; la casse (majuscules/minuscules) des unités est préservée.

Les options **Afficher la probabilité de pluie** et **Afficher les minimums/maximums journaliers** complètent la ligne inférieure : la probabilité de pluie s'affiche à gauche, et les valeurs minimale et maximale à droite. Ces informations sont issues des prévisions quotidiennes pour la journée en cours, basées sur l'heure locale du navigateur. Les prévisions sont chargées via l'interface HA existante et mises en cache pendant cinq minutes. Dans Home Assistant, les mesures actuelles et les prévisions sont distinctes ; voir [Entité météo HA et prévisions](https://developers.home-assistant.io/docs/core/entity/weather/). Si l'intégration ne prend pas en charge les prévisions quotidiennes, des tirets s'affichent à la place de ces valeurs supplémentaires, tandis que les données actuelles restent visibles.

Dans la section **Capteurs supplémentaires**, chaque valeur peut être remplacée par une entité spécifique : température, humidité, vitesse du vent, probabilité de pluie, ainsi que les minimums et maximums journaliers. Si un capteur est défini pour une valeur donnée, il devient prioritaire, même s'il n'est pas disponible (aucune autre valeur ne viendra alors se substituer à lui). En l'absence de capteur, ce sont les données de l'entité météo ou des prévisions journalières qui sont utilisées. Les valeurs manquantes sont indiquées par **--**, tandis qu'un état inconnu est représenté par un point d'interrogation. L'option **Exemples de données sans entité météo** peut être activée explicitement ; elle affiche alors la mention **DEMO**. En cas d'entité météorologique liée, le système ne bascule jamais automatiquement sur des données d'exemple.

**Type d'affichage → LCD / LED** : LCD avec couleur de segment/fond, LED avec couleur d'éclairage au choix. Le cadre noir de l'écran et les caractéristiques du boîtier sont identiques à ceux des autres afficheurs industriels. **Grille 2:4**, avec par défaut **262×130 px** et un **espacement de 1 px tout autour** : hauteur = 2 × cellule de grille + 2 × espacement, largeur = 4 × cellule de grille + 6 × espacement. La cellule de grille conserve une taille minimale de 64 px. Les opérations de saisie, de déplacement et de modification des espacements maintiennent une disposition en deux rangées, chacune composée de quatre widgets individuels. Les contenus trop longs sont tronqués ; le texte complet est accessible via une info-bulle.

La mise en marche/arrêt s'effectue via l'entité **Affichage Marche/Arrêt** ou un **point de connexion supérieur** (`display-power`) activable individuellement, qui est prioritaire. En l'absence de liaison, l'état par défaut (prévisualisation) s'applique ; si les valeurs Marche/Arrêt sont manquantes ou inconnues, l'écran reste éteint. Les connexions de type interrupteur (à bascule), visibles ou invisibles, sont prises en charge. Il n'y a pas d'entrée de mesure, de sortie ou de commande d'écriture ; les paramètres relatifs aux quatre coins du boîtier, à l'espacement, aux vis, à la couleur du cadre, ainsi qu'à la largeur du cadre et au rayon des coins (optionnels), restent disponibles.

## Horloge industrielle : Nixie / LED / LCD {#industrie-uhr-nixie-led-lcd}

![Horloge industrielle avec six tubes Nixie affichant l'heure 12:34:58 en orange lumineux](/images/grafik-visual-studio/industrial-clock-nixie.png)

| LED | LCD |
| --- | --- |
| ![Horloge industrielle avec éclairage LED bleu](/images/grafik-visual-studio/industrial-clock-led.png) | ![Horloge industrielle avec segments LCD sombres sur fond vert](/images/grafik-visual-studio/industrial-clock-lcd.png) |

Un widget proposant le paramètre **Type d'affichage → Tube Nixie / LED / LCD**. Le mode Nixie imite des tubes en verre dotés d'une grille de protection et de chiffres formés par des filaments superposés, émettant une lueur orange. Le mode LED affiche des chiffres à sept segments lumineux, avec une **couleur d'éclairage LED** au choix. Le mode LCD permet de définir la **couleur des segments LCD** ainsi que la **couleur de fond LCD**. Les images présentent un exemple d'heure figée.

L'option **Afficher les secondes** permet de basculer entre les formats **HH:MM:SS** et **HH:MM** (format 24 heures). L'option **Clignotement des deux-points** fait clignoter les séparateurs au rythme d'une fois par seconde ; cette fonction peut être désactivée pour un affichage plus calme. Le paramètre **Fuseau horaire** propose l'heure locale du navigateur, l'UTC ou « Europe/Berlin », avec gestion automatique du passage à l'heure d'été/hiver. La source temporelle est l'horloge du navigateur. Aucune entité temporelle n'est requise et aucune sortie de données n'est prévue. Un signal de synchronisation commun met à jour uniquement le contenu de l'horloge ; la sélection et le focus de saisie dans l'éditeur restent inchangés.

| Affichage | HH:MM:SS | HH:MM | Hauteur minimale |
| --- | --- | --- | --- |
| Nixie | 518×128 px | 388×128 px | 64 px |
| LED / LCD | 262×64 px | 196×64 px | 32 px |

Les dimensions standard s'appliquent avec un **espacement de 1 px tout autour**. La largeur correspond respectivement à quatre ou trois unités de grille, espaces intermédiaires inclus : Largeur = Hauteur × unités de grille + 2 × espacement × (unités de grille − 1). Les proportions sont conservées lors de la saisie ou du redimensionnement par glissement. Le passage au mode Nixie double la hauteur, tandis qu'un retour au mode LED/LCD la réduit de moitié ; tout agrandissement spécifique est maintenu de manière relative. La largeur s'ajuste automatiquement en fonction des modifications apportées aux secondes et aux espacements.

Le boîtier, les vis, la couleur du cadre, la largeur du cadre (optionnelle), le rayon des angles ainsi que quatre points d'ancrage actifs sur le boîtier restent disponibles. L'affichage de l'heure est contrôlé soit par une **entité « Affichage Marche/Arrêt »**, soit par un **point de couplage « Marche/Arrêt » supérieur** (`display-power`) pouvant être activé individuellement ; ce dernier est prioritaire. En l'absence de liaison, l'affichage est considéré comme **« allumé sans entrée »**. Si les valeurs « Marche/Arrêt » sont inconnues ou manquantes, l'affichage s'éteint, mais l'heure et le boîtier demeurent visibles. Les connexions de type interrupteur à bascule peuvent être rendues visibles ou invisibles. Les graphismes des tubes Nixie sont des dessins SVG originaux ; le modèle OmniGraffle fourni n'est pas distribué.

## Affichages à segments : LED et LCD {#segmentanzeigen-led-und-lcd}

| LED à 7 segments | LED à 16 segments | LCD à 16 segments |
| --- | --- | --- |
| ![LED rouge à 7 segments affichant 647,25 Watts](/images/grafik-visual-studio/industrial-segment-0.png) | ![LED bleue à 16 segments avec valeur d'entrée 56,78 et indication en Ampères](/images/grafik-visual-studio/industrial-segment-1.png) | ![LCD verte à 16 segments avec mention « SOLAR » (12.3) et indication en Volts](/images/grafik-visual-studio/industrial-segment-2.png) |

Les images utilisent des données d'exemple. Les trois types d'affichage disposent de **1 à 10 positions fixes**. Le signe moins occupe une position, tandis que le point décimal est rattaché à la position précédente. L'affichage LED à 7 segments présente des nombres avec un nombre réglable de décimales et, en option, des zéros non significatifs (zéros de tête). L'arrondi est effectué avant la vérification du nombre de positions ; en cas de dépassement de capacité (débordement) ou de valeurs manquantes, des tirets s'affichent. Les afficheurs à 16 segments présentent des chiffres et du texte en majuscules. Les textes trop longs sont tronqués ; le contenu intégral est consultable dans une info-bulle. Les caractères non pris en charge s'affichent sous forme de points d'interrogation. Les caractères pris en charge sont : A–Z, 0–9, espace, point, signe moins, tiret bas, point d'interrogation, signe plus, barres obliques, deux-points, signe égal et symbole degré.

L'entité **Contenu** fournit la valeur mesurée ou le texte à afficher. En l'absence de connexion, c'est la **Valeur / Texte de prévisualisation** qui est utilisée. Alternativement, le point de connexion d'entrée de valeur situé à gauche (`value-input`) peut être activé individuellement ; il est prioritaire sur l'entité. Un second point de connexion, activable indépendamment et situé en haut (`display-power`), ou l'entité **Affichage Marche/Arrêt**, contrôle l'état de l'affichage. Le point de connexion Marche/Arrêt est prioritaire ; en l'absence de connexion, l'affichage est considéré comme « activé sans entrée ». Si les valeurs Marche/Arrêt sont manquantes ou inconnues, l'afficheur reste éteint. Les connexions de valeur, qu'elles soient visibles ou invisibles (par exemple depuis un interrupteur à bascule), sont fonctionnelles. Ces afficheurs ne disposent ni de sorties ni de commandes d'écriture.

À droite, les mentions **W, A et V** sont disposées les unes en dessous des autres. Pour la section **LED d'unité**, les choix se limitent à **Éteint / W / A / V** : une seule étiquette peut être allumée à la fois. Les autres restent visibles mais éteintes. La **couleur des segments et de l'unité** s'applique indifféremment aux chiffres, au texte et à l'unité sélectionnée. Les modes LED simulent des segments lumineux avec un léger halo, tandis que le mode LCD utilise des segments contrastés sur un arrière-plan réglable. L'unité est choisie manuellement et n'est pas déduite automatiquement des attributs de l'entité.

La taille standard est de **262×64 px** selon une **grille 1:4**, ou alternativement **196×64 px** selon une **grille 1:3**, avec dans les deux cas un **espacement de 1 px tout autour**. Comme pour les interrupteurs et les indicateurs linéaires, la formule est la suivante : Largeur = Hauteur × unités de grille + 2 × espacement × (unités de grille − 1). Les opérations de saisie et de redimensionnement par glissement respectent ce ratio. Le format 1:4 est recommandé pour afficher dix caractères bien lisibles ; si nécessaire, le widget peut être agrandi dans son ensemble. Les options concernant le boîtier, les vis, la couleur du cadre, l'épaisseur du cadre (facultative), l'activation individuelle des quatre coins du boîtier ainsi que l'espacement restent disponibles.

La géométrie des segments repose sur un dessin SVG dédié et ne nécessite aucune police de caractères installée sur le système. Le fichier **16Segments Basic.otf** fourni est, selon la licence intégrée, réservé à un usage privé ; il n'est donc pas inclus dans le paquet distribué au public.

## Compteur / Odomètre {#zahlwerk-odometer}

Le compteur est un afficheur industriel autonome, dédié uniquement à la lecture, doté de rouleaux chiffrés mécaniques. Une valeur numérique provient d'une **entité** ou via le **point de connexion d'entrée situé à gauche** (`value-input`), qui peut être activé individuellement. Le point de connexion activé est prioritaire ; en l'absence de liaison, la valeur de prévisualisation s'affiche. Les liaisons de valeurs, qu'elles soient visibles ou invisibles, sont prises en charge. Il n'y a ni sortie ni commande d'écriture.

| Normal 1:3 | Normal 1:4 |
| --- | --- |
| ![Compteur avec cinq chiffres entiers, deux décimales et kWh](/images/grafik-visual-studio/industrial-odo-normal-3.png) | ![Compteur large avec entrée via une liaison de valeur](/images/grafik-visual-studio/industrial-odo-normal-4.png) |

| Étroit 0,5:3 | Étroit 0,5:4 |
| --- | --- |
| ![Compteur étroit avec hauteur de chiffre réduite de moitié](/images/grafik-visual-studio/industrial-odo-slim-3.png) | ![Compteur large et étroit](/images/grafik-visual-studio/industrial-odo-slim-4.png) |

Les illustrations utilisent des données d'exemple. Avec un **espacement de 1 px tout autour**, les dimensions sont de **196×64 / 262×64 px** pour les widgets normaux, et de **196×32 / 262×32 px** pour les widgets étroits. La largeur inclut les espaces entre les trois ou quatre widgets individuels, comme c'est le cas pour les affichages linéaires. La **largeur en unités de grille**, la saisie, le déplacement (glisser-déposer) et les modifications de l'espacement tiennent compte de cette disposition.

La **hauteur de la fenêtre d'affichage des chiffres** est fixée à 62,5 % de la hauteur du widget : **40 px** pour un widget de 64 px, et **20 px** pour un widget de 32 px. Les formats avec un rapport hauteur/largeur de 1:3 et 1:4 utilisent la même hauteur, tandis que les formats étroits utilisent exactement la moitié de cette hauteur. L'augmentation du nombre de chiffres influe sur la largeur des chiffres et leur espacement, mais pas sur la hauteur.

Le nombre de **chiffres avant la virgule** peut être défini entre 1 et 12, et le nombre de **décimales** entre 0 et 6. Un léger espace est prévu autour du séparateur décimal (virgule ou point). Par exemple, cinq chiffres avant la virgule et deux décimales donnent un format de type `00123,45`. Si l'option des **zéros non significatifs** (zéros en début de nombre) est désactivée, ces emplacements restent vides. L'option « **espace pour un signe moins** » réserve en permanence un emplacement avant les chiffres ; les valeurs négatives pour lesquelles cet espace n'est pas réservé sont traitées comme un dépassement de capacité (débordement).

Une **unité** saisie est prioritaire sur `unit_of_measurement` de l’entité ou sur l’unité de la connexion de valeur. L’unité reste à droite de la fenêtre des chiffres. La **couleur de la police** et la **taille de la police de l’unité** sont réglables ; les unités trop longues sont tronquées. Le style industriel, les vis activées par défaut, la couleur du cadre, sa largeur optionnelle, les quatre coins du boîtier activables individuellement et l’espacement restent disponibles.

Lors de l'exécution, les chiffres s'animent en « défilant » pendant 350 ms lorsqu'ils changent — cela inclut le passage de 09 à 10. Cette animation est désactivée si le paramètre « réduire les animations » (ou « mouvement réduit ») du navigateur est activé. Les valeurs manquantes ou indisponibles sont représentées par des **tirets**, tandis qu'une valeur dépassant le nombre de chiffres configuré est affichée sous la forme **#**. L'arrondi est effectué avant la vérification du dépassement de capacité ; Par exemple, avec cinq chiffres avant la virgule et deux décimales, `99999,999` est signalé comme un dépassement de capacité (overflow). La largeur demeure constante.

## Jauge linéaire / Curseur {#linear-gauge-schieberegler}

À partir de **Studio 0.1.241**, la sélection d'une entité met immédiatement à jour le mode d'affichage : sous **Échelle → Apparence → Barre de couleurs**, une échelle colorimétrique et des plages de couleurs sont disponibles. Si aucune donnée d'entrée n'est fournie, seule une échelle graduée s'affiche. Le composant 0.6.0 peut continuer à être utilisé.

Lorsqu'une **entité d'entrée** ou une **donnée d'entrée issue d'un flux** est fournie, le widget fonctionne comme un affichage : un **triangle** indique la valeur actuelle. Les utilisateurs peuvent choisir entre une **échelle graduée** ou une **barre de couleurs** avec des plages de couleurs personnalisées. En l'absence de donnée d'entrée, il se transforme en **curseur doté d'un curseur rectangulaire et d'une simple échelle graduée**. Même si une configuration de barre de couleurs a été enregistrée précédemment, celle-ci n'apparaîtra pas lorsque le widget est en mode curseur.

| Curseur avec échelle graduée | Jauge linéaire avec barre de couleurs |
| --- | --- |
| ![Curseur linéaire avec un élément rectangulaire et une échelle graduée](/images/grafik-visual-studio/industrial-linear-slider.png) | ![Jauge linéaire avec un triangle et des plages de couleurs configurées](/images/grafik-visual-studio/industrial-linear-gauge.png) |

| Curseur étroit | Jauge linéaire étroite |
| --- | --- |
| ![Contrôle linéaire étroit avec une échelle graduée](/images/grafik-visual-studio/industrial-linear-slim.png) | ![Affichage linéaire étroit avec un triangle](/images/grafik-visual-studio/industrial-linear-slim-gauge.png) |

Les images utilisent des données d'exemple. Sous **Taille → Largeur en unités de grille**, les options 2, 3 et 4 sont disponibles :

| Version | Hauteur/Largeur | Tailles minimales (Largeur × Hauteur) |
| --- | --- | --- |
| Normale | 1:2 / 1:3 / 1:4 | 130×64 / 196×64 / 262×64 px |
| Étroite | 0,5:2 / 0,5:3 / 0,5:4 | 130×32 / 196×32 / 262×32 px |

Le tableau s'applique avec un **espacement de 1 px tout autour**. La largeur totale prend en compte les espaces entre les widgets individuels : **Largeur de grille × Unités + 2 × Espacement × (Unités − 1)**. La « largeur de grille » correspond à la hauteur ; pour la version étroite, elle équivaut au double de la hauteur. Sans espacement, on obtient 128/192/256 px. Ainsi, les bords extérieurs s'alignent avec deux, trois ou quatre widgets individuels ; toute modification de l'espacement ajuste automatiquement la largeur.

Lors de la saisie ou du redimensionnement par glissement, les deux dimensions sont mises à l'échelle en conservant le rapport choisi. Les paramètres **Minimum**, **Maximum**, **Graduation** et **Pas de réglage** sont configurables séparément ; des valeurs négatives sont autorisées, et la valeur zéro est mise en évidence. L'option **Afficher les valeurs de l'échelle** ajoute les valeurs extrêmes ainsi que le zéro (si l'espace le permet). Pour la barre colorée, les mêmes règles s'appliquent que pour les jauges ou potentiomètres, avec la possibilité de définir jusqu'à huit plages de couleurs. Les plages non valides n'affichent pas de couleurs arbitraires ; en l'absence de valeur d'entrée, aucun indicateur (aiguille) n'est affiché.

L'affichage de la valeur reprend l'unité et la mise en forme de la police, à l'instar des jauges ou des potentiomètres. L'option **Centre** place l'affichage au-dessus de l'échelle linéaire, tandis que l'option **Bas** le place en dessous. Les paramètres relatifs au style industriel, aux vis, à la couleur du cadre, à la largeur du cadre (optionnelle), aux quatre coins du boîtier (activables individuellement), à l'espacement et aux couleurs des points de connexion centraux s'appliquent également.

En mode exécution (*runtime*), le curseur peut être déplacé à l'aide de la souris, d'un écran tactile ou du clavier. Les touches fléchées permettent un déplacement par pas unitaire, les touches « Page précédente » / « Page suivante » par pas de dix, et les touches « Début » / « Fin » permettent de sauter directement au minimum ou au maximum. La valeur est transmise **au moment du relâchement** ou **pendant le déplacement**. Une entité `number`/`input_number` ou un point de départ (avec liaison de valeur visible ou invisible) récupère cette valeur. L'éditeur ne transmet aucune commande de manipulation. Une entrée de flux de données activée est prioritaire sur l'entité d'entrée ; elle demeure en mode affichage même en l'absence de valeur.

## Écrans LCD – 20×4 et 16×2 {#lcd-–-20×4-und-16×2}

Ces écrans simulent une police à **matrice de points 5×8** avec un bord d'écran noir. La police est générée dynamiquement à partir de pixels et fait partie intégrante de Studio ; aucune installation de police externe n'est requise. Sont inclus : les lettres majuscules et minuscules, les chiffres, la ponctuation, les caractères spéciaux allemands (Umlauts), le « ß », les symboles €, °, µ, Ω, ainsi que des flèches et le signe ✓. Les caractères non pris en charge s'affichent sous la forme `?`.

| 20×4 Jaune/Blanc | 20×4 Bleu/Blanc |
| --- | --- |
| ![Écran LCD avec fond jaune et caractères blancs en matrice de points](/images/grafik-visual-studio/industrial-lcd-yellow.png) | ![Écran LCD avec fond bleu et caractères blancs en matrice de points](/images/grafik-visual-studio/industrial-lcd-blue.png) |

| 16×2 Bleu/Blanc | Écran éteint |
| --- | --- |
| ![Écran LCD avec 16 caractères par ligne et deux lignes](/images/grafik-visual-studio/industrial-lcd-small.png) | ![Écran LCD éteint avec boîtier industriel visible](/images/grafik-visual-studio/industrial-lcd-off.png) |

Les images présentent des exemples de données. **Les deux formats sont disponibles en versions Jaune/Blanc et Bleu/Blanc.** À partir du **Studio 0.1.242**, l'écran 16×2 adopte une taille standard de **192×64 px** ; l'écran 20×4 est deux fois plus large et plus haut, avec **384×128 px**. Les deux conservent un rapport hauteur/largeur de **1:3** lors de l'insertion ou du redimensionnement. Les écrans enregistrés avec des dimensions plus petites sont mis à l'échelle pour atteindre ces tailles minimales lors du chargement. Pour les affichages plus grands, l'écran et les caractères sont mis à l'échelle simultanément. Les fonds bleus et jaunes sont plus sombres, et les pixels blancs sont plus intenses. Le paquet 0.6.0 reste inchangé ; une simple mise à jour du Studio suffit.

### Lignes et entités {#zeilen-und-entitaten}

Chacune des quatre (ou deux) lignes dispose de **sa propre entité**, avec une option de sélection associée. Le champ **Texte / Préfixe** précède la valeur de l'entité ; en l'absence d'entité, ce champ constitue l'intégralité du contenu fixe de la ligne. Exemple : `Temp: ` + valeur du capteur `-20.24` + unité automatique `°C` donne, avec une décimale, `Temp: -20.2 °C`.

**Unité issue de l'entité** : récupère `unit_of_measurement` depuis Home Assistant. Une unité définie manuellement est prioritaire. **Décimales** : prend en charge `auto` ou une valeur comprise entre 0 et 6 pour les nombres ; les états textuels restent du texte. Les valeurs d'entité manquantes ou indisponibles s'affichent sous la forme `?`. Les textes longs sont tronqués après 20 ou 16 caractères ; l'infobulle affiche le texte intégral. Il n'y a pas de saut de ligne ni de points de connexion de données dédiés pour les lignes.

### Activation/désactivation de l'écran et boîtier {#display-ein-aus-und-gehause}

En l'absence de liaison, le comportement par défaut est **activé sans entrée**. **Activation/désactivation de l'écran : Entité** peut, par exemple, être une entité de type `switch` ou `input_boolean`. Autre option : **Activer le point de connexion Marche/Arrêt** ; une entrée unique située en haut au centre (`display-power`) prend en charge `on/off`, `true/false` ou `1/0`. Reliez la sortie d'un interrupteur à bascule ou d'un bouton-poussoir à cette entrée via une connexion de valeur (visible ou invisible).

Le point de connexion activé est prioritaire sur l'entité. En l'absence d'entrée valide, l'écran reste éteint ; un écran désactivé n'affiche aucun texte, mais le boîtier demeure visible. L'écran LCD lit les états et n'envoie aucune commande de commutation. Il ne dispose d'**aucune sortie**.

Dans la section **Boîtier et couleurs**, vous trouverez des options pour le style industriel, des vis actives par défaut, la couleur du cadre et une largeur de cadre optionnelle. Les quatre **points d'ancrage du boîtier situés aux angles** peuvent être activés individuellement. L'espacement périphérique ainsi que les couleurs centrales des points d'entrée et du boîtier suivent les mêmes règles que pour les autres widgets de style industriel. La taille de la police est régie par une grille fixe ; la couleur du texte reste blanche, quel que soit le mode colorimétrique choisi.

## Interrupteurs à bascule – 1 à 4 {#wippschalter-–-1-bis-4}

À partir de la version **Studio 0.1.237**, la formule suivante s'applique aux interrupteurs à bascule : **Largeur = Hauteur × Nombre d'interrupteurs + 2 × Espacement périphérique × (Nombre d'interrupteurs − 1)**. Pour une hauteur de 64 px et un espacement de 1 px, les largeurs sont de **64 / 130 / 196 / 262 px**. Le centre des interrupteurs et les points de connexion (E/S) sont alignés avec ceux des widgets ancrés individuellement. Les interactions (saisie et glisser-déposer) tiennent compte de l'espacement. Une simple mise à jour du Studio suffit ; le paquet 0.3.0 demeure inchangé.

À partir du paquet **0.3.0** et du Studio **0.1.235**, l'interrupteur à bascule est une variante de l'interrupteur à levier utilisant des graphismes PNG transparents. Dans les sections **Interrupteur 1** à **Interrupteur 4 → Couleur de l'interrupteur**, vous pouvez choisir entre **Blanc/Gris**, **Rouge**, **Noir** ou **Vert** pour chaque canal. Un même widget peut combiner différentes couleurs ; le graphisme change en fonction de l'état (activé/désactivé).

![Quatre interrupteurs à bascule avec des couleurs choisies indépendamment](/images/grafik-visual-studio/industrial-rockers.png)

Toutes les propriétés des interrupteurs à bascule s'appliquent également ici : étiquetage, plaques supplémentaires (ON/OFF, 1/0, EIN/AUS ou personnalisées), couleurs des LED, entités, E1–E4/A1–A4, six points d'ancrage sur le boîtier, vis, cadre et espacement. Le marquage O/I imprimé fait partie intégrante du graphisme. Échelle de 1:1 à 4:1, avec un minimum de 64 px par canal. L'utilisation n'est possible qu'en mode exécution (runtime).

## Indicateur/Potentiomètre : Données et utilisation {#gauge-poti-daten-und-bedienung}

À partir de **Studio 0.1.282**, la sortie active du flux de données contrôle également la vitesse et la direction d'une ligne SVG connectée. Aucune entité de sortie supplémentaire liée à Home Assistant n'est nécessaire pour cela : le champ **Sortie : entité number/input_number** reste vide dans le cas de connexions purement locales ; une valeur initiale (comme `0`) doit être saisie dans le champ de valeur de prévisualisation. En revanche, pour effectuer des actions d'écriture vers Home Assistant, sélectionnez une entité disponible (`number.*` ou `input_number.*`).

Pour obtenir une vitesse qui varie visiblement en fonction de la valeur : activez l'animation, réglez le paramètre **Diviseur Potentiomètre / SVG LineBox** (par exemple sur **10**) et désactivez l'ajustement automatique de ce diviseur. Une valeur de 10 donne 1 cycle/s, 20 donne 2 cycles/s ; 0 correspond à l'arrêt, et les valeurs négatives entraînent un mouvement en sens inverse. Avec un diviseur réglé sur 1, toute valeur égale ou supérieure à 20 atteint la vitesse maximale. Plus de détails sont disponibles sous [SVG-Line](/fr/projects/grafik-visual-studio/svg-line) ; [Image de l'éditeur et animation](/fr/projects/grafik-visual-studio/bildergalerie) illustrent la structure.

Les sections suivantes, consacrées à l'échelle et à l'affichage des valeurs, décrivent l'indicateur (Gauge) et le potentiomètre. L'interrupteur à bascule fait l'objet d'une section dédiée à la fin de la page.

- **Sans entrée :** Utilisation du potentiomètre en mode exécution (*runtime*) via la souris, un écran tactile ou le clavier. La valeur de départ et le pas de réglage sont configurables.
- **Avec entité d'entrée ou point de couplage :** Affichage sous forme de jauge. Un point de couplage activé est prioritaire sur l'entité. L'absence d'entrée est signalée comme une valeur de mesure manquante.
- **Sortie :** `number.*` ou `input_number.*`, déclenchée au relâchement ou pendant le déplacement (glisser). Les modifications apportées aux valeurs de la jauge sont également transmises. L'entité doit être disponible et accessible en écriture ; les entités d'entrée et de sortie ne peuvent pas être identiques.
- **Lignes de valeur (*Value Lines*) :** Des connexions, visibles ou invisibles, exploitent le flux de données existant.

Dans l'éditeur, les fonctions de commande et d'écriture sont désactivées ; pour effectuer des réglages, veuillez ouvrir le mode exécution (*runtime*).

## Échelle et plages de couleurs {#skala-und-farbbereiche}

Il est possible de choisir entre une **échelle graduée** (avec un zéro mis en évidence) et un **anneau coloré**. Le minimum, le maximum, la graduation et le pas de réglage (indépendant de la graduation) sont configurables ; des limites négatives sont autorisées.

Les plages de couleurs sont définies par des **valeurs de seuil supérieur** croissantes au sein de l'échelle. La dernière couleur s'étend jusqu'au maximum. Pour une puissance solaire allant de 0 à 1000 W, on peut par exemple définir quatre plages se terminant respectivement à **250 / 500 / 750 / 1000**. Si les limites de l'échelle sont modifiées, les seuils de couleur doivent être ajustés en conséquence. Des limites invalides n'entraînent pas la suppression d'une valeur de mesure chargée ; un avertissement reste toutefois visible dans l'infobulle (*tooltip*).

## Affichage de la valeur {#wertanzeige}

La section de propriétés dédiée à l'**affichage de la valeur** comprend :

| Paramètre | Effet |
| --- | --- |
| Afficher la valeur | Affiche la valeur mesurée et l’unité dans l’instrument. |
| Unité | Unité personnalisée, par exemple W. Si le champ est vide, reprend `unit_of_measurement` de l’entité d’entrée Home Assistant. |
| Position de la valeur | **Centre** ou **Bas** ; la position basse se trouve sous le bouton du potentiomètre. |
| Taille de la police (px) | 12 px par défaut ; reste constante lorsque la taille du widget change. |
| Couleur de la police | Couleur réglable, claire par défaut. |

L'affichage de la valeur et de l'unité a été ajouté via Studio 0.1.227, et les paramètres d'affichage spécifiques via 0.1.228.

## Boîtier et couleurs {#gehause-und-farben}

À partir de la version **Studio 0.1.248**, **tous les widgets industriels** proposent une case à cocher **Adapter l'arrière-plan** associée à une **couleur d'arrière-plan du boîtier**. Si la case n'est pas cochée, le dégradé standard habituel (du gris foncé à l'anthracite) est conservé. Si elle est cochée, une couleur personnalisée uniforme est appliquée ; la valeur par défaut est **#263238**. Le sélecteur de couleur n'est accessible que lorsque la case est cochée. Si l'option est désactivée, l'arrière-plan par défaut est rétabli, mais la couleur choisie reste mémorisée pour une utilisation ultérieure. Cela s'applique aussi bien à l'éditeur qu'à l'exécution (Runtime), même si le style industriel est désactivé. Les couleurs des écrans, afficheurs LCD, segments, LED et échelles continuent d'être configurées séparément. La mise à jour du Studio suffit, même si une version antérieure du pack industriel est installée ; le pack 0.10.3 met à jour la documentation.

À partir de la version Studio **0.1.231**, une case à cocher **Activer les vis** est disponible juste en dessous de l'option **Style industriel**. Les vis sont affichées par défaut ; elles peuvent être désactivées séparément lorsque le style industriel est actif. La réactivation du style industriel réactive également les vis. Si le style industriel n'est pas utilisé, les vis ne sont pas visibles et la case à cocher est désactivée.

Le **style industriel** ajoute quatre têtes de vis, l'arrière-plan du boîtier et un cadre. Les couleurs de l'échelle et de l'aiguille peuvent être réglées séparément. Le paramètre **CSS Général → Rayon des coins (px)** permet de contrôler l'arrondi du cadre.

À partir de la version Studio 0.1.230, les règles suivantes s'appliquent à l'option **Adapter la largeur du cadre** :

- **Case non cochée :** largeur de cadre par défaut de 2 px.
- **Case cochée :** possibilité de définir une **largeur de cadre (px)** personnalisée, comprise entre 1 et 16 px. - La valeur définie est conservée après la désactivation ; le cadre reste visible.

La **couleur du cadre** peut être choisie séparément. Si le style industriel (« Industriestyle ») est désactivé, aucun cadre de boîtier n'est affiché.

## Taille {#große}

La taille minimale du widget est de **64 × 64 px**. L'option **Ratio 1:1** (activée par défaut depuis la version Studio 0.1.226) permet de conserver un rapport identique entre la largeur et la hauteur lors de la saisie ou du redimensionnement par glissement. Si cette option est désactivée, les dimensions peuvent être définies indépendamment (avec un minimum de 64 px chacune). Si l'option est réactivée, la plus grande des deux dimensions est appliquée aux deux côtés.

## Points d'ancrage du boîtier {#gehause-snappunkte}

Depuis la version Studio 0.1.224, la fonctionnalité **Points d'ancrage du boîtier** permet d'activer individuellement quatre coins et de définir un espacement commun pour tous les côtés. Avec une valeur de 1 px de chaque côté, un espace de 2 px est créé ; les widgets s'alignent automatiquement (« s'aimantent ») lorsqu'ils sont déplacés.

La couleur se règle via **Paramètres → Général → Éditeur et points d'ancrage → Couleur des points d'ancrage du boîtier**. Les connexions de signaux restent distinctes. Le routage automatique des connexions vers les côtés libres du boîtier sera implémenté ultérieurement.

## Interrupteurs à bascule – 1 à 4 {#kippschalter-–-1-bis-4}

À partir de la version **Studio 0.1.249**, une option **Étiquetage → Personnalisé** est disponible pour chaque interrupteur, permettant de définir un **texte pour l'état ARRÊT** et un **texte pour l'état MARCHE**. Par exemple : intitulé « Pompe », texte pour ARRÊT « 1 », texte pour MARCHE « 2 », ou encore « Froid/Chaud ». Les quatre canaux disposent de textes indépendants ; si aucun texte personnalisé n'est saisi, le champ reste vide. Les textes longs sont tronqués, mais une info-bulle affiche le texte complet correspondant à l'état actuel. Cela s'applique également à l'interrupteur à bascule ; les symboles O/I imprimés sur celui-ci demeurent visibles dans la représentation graphique. **Seul l'étiquetage est modifié :** les actions sur les entités et les points de connexion E/S restent de type booléen (`false`/`true`) ; les textes « 1 »/« 2 » ne sont pas interprétés comme des valeurs numériques et ne déclenchent pas la sélection automatique de deux entités distinctes. Les variantes d'étiquetage existantes restent disponibles. Une simple mise à jour du Studio suffit, en conservant les packs industriels actuels.

À partir de la version **Studio 0.1.236**, l'espacement intermédiaire est désormais pris en compte dans le calcul de la largeur totale du bloc pour l'interrupteur à levier : **Hauteur × Nombre d'interrupteurs + 2 × Espacement périphérique × (Nombre d'interrupteurs − 1)**. Avec une hauteur de 64 px et un espacement périphérique de 1 px, les largeurs obtenues sont respectivement de **64 / 130 / 196 / 262 px**. Ainsi, les centres des interrupteurs et les points de connexion E/S s'alignent parfaitement avec les widgets individuels situés en dessous. Les opérations de saisie et de glisser-déposer tiennent compte de cet ajout. Cette modification ne concerne pour l'instant que l'interrupteur à levier ; les interrupteurs à bascule restent inchangés. Une mise à jour du Studio suffit ; le pack 0.3.0 demeure inchangé.

À partir du pack **0.2.0** et du Studio **0.1.232**, il est possible de disposer côte à côte d'un à quatre interrupteurs fonctionnant indépendamment. Le paramètre **Nombre d'interrupteurs** définit le rapport largeur/hauteur, allant de **1:1 à 4:1**. Les dimensions minimales sont de 64 px de hauteur et 64 px de largeur par canal ; les proportions sont conservées lors de la saisie des dimensions ou du redimensionnement par glissement.

![Quatre interrupteurs à bascule industriels avec petites LED et trois variantes d'étiquettes](/images/grafik-visual-studio/industrial-switches.png)

*Exécution (Runtime) avec exemples : étiquettes personnalisées, LED vertes et plaques « ON/OFF », « 1/0 » ou « EIN/AUS ». À partir du Studio 0.1.233, le levier métallique provient d'un fichier PNG transparent fourni par rockbaer2007 ; il reste entièrement visible dans les deux positions. La LED, quant à elle, est générée en CSS. Une mise à jour du Studio suffit ; il n'est pas nécessaire de réinstaller le pack 0.2.0.*

Chaque section, de **Interrupteur 1** à **Interrupteur 4**, comprend une **étiquette** fixe, une inscription sur plaque (choix entre **ON/OFF**, **1/0**, **EIN/AUS** ou **Personnalisé**), un état initial, ainsi que des couleurs de LED spécifiques pour les états « allumé » et « éteint ». La LED est située au-dessus de l'étiquette ; les textes sur les plaques ne sont pas modifiés par les entités. La taille et la couleur de la police se règlent sous la rubrique **Étiquette**.

| Connexion par canal | Comportement |
| --- | --- |
| Entrée : Entité | État pour le levier et la LED. En l'absence d'entrée, une entité de sortie configurée est utilisée comme retour d'état. |
| Point de connexion d'entrée | Situé en haut de la colonne de l'interrupteur correspondant ; activable individuellement ; prioritaire sur l'entité. |
| Sortie : Entité | Commande `switch.*`, `light.*` ou `input_boolean.*`. Si aucune sortie distincte n'est définie, une entité d'entrée appropriée est commandée. |
| Point de connexion de sortie | Situé en bas de la colonne de l'interrupteur correspondant ; activable individuellement. Fournit la dernière commande effectuée sous forme de valeur booléenne ; avant la première action, il renvoie l'état actuel. |

En l'absence de liaison, l'interrupteur fonctionne localement. L'absence de retour d'état bloque toute commande. Aucune commande n'est envoyée dans l'éditeur. Les paramètres relatifs au boîtier, aux vis, au cadre et aux points d'ancrage du boîtier s'appliquent également à ce widget. Pour le nouvel interrupteur à bascule, mettez à jour le paquet local vers **0.2.0** ; les définitions existantes pour les jauges/potentiomètres sont conservées.

### Connexions E1–E4 et A1–A4 {#anschlusse-e1–e4-und-a1–a4}

À partir de **Studio 0.1.234**, les points de signal dans l'éditeur sont désignés par **E1–E4** (entrée située au-dessus de chaque interrupteur) et **A1–A4** (sortie située en dessous). Si le nombre d'interrupteurs est inférieur, seules les connexions correspondantes s'affichent. Ces points peuvent être activés individuellement pour chaque interrupteur ; les couleurs des entrées et des sorties sont déterminées par les paramètres centraux de l'éditeur. Les connexions existantes sont conservées.

Dans la catégorie **Points d'ancrage du boîtier**, l'interrupteur à bascule dispose de six points distincts pouvant être activés individuellement : les quatre coins, ainsi que les points **milieu gauche** et **milieu droit**. En incluant les points de connexion des signaux, on obtient un total de **8 / 10 / 12 / 14 points** disponibles pour un à quatre interrupteurs. Les points du boîtier servent à l'enclenchement selon un espacement défini et utilisent la couleur dédiée aux points d'ancrage du boîtier ; ils ne transmettent aucune valeur de commutation. Les points et les étiquettes des connexions ne sont visibles que dans l'éditeur. Une mise à jour du Studio suffit ; le paquet **0.2.0** demeure inchangé.
