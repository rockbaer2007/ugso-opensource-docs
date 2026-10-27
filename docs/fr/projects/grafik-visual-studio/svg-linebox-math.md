---
title: SVG LineBox Math
---

# SVG LineBox Math {#svg-linebox-math}

## Exemple pratique : Fusionner deux valeurs de puissance positives {#praxisbeispiel-zwei-positive-leistungswerte-zusammenfuhren}

Un onduleur peut fournir les puissances de charge et de décharge sous forme de **deux valeurs distinctes, toutes deux positives**. Pour obtenir un affichage de puissance unifié, il est nécessaire de générer une valeur unique dont le signe indique le sens du flux. **SVG LineBox Math** calcule cette différence directement dans le navigateur de l'écran d'affichage. Aucun capteur « template » (modèle) ni automatisation supplémentaire dans Home Assistant n'est requis : Home Assistant fournit les valeurs des capteurs, tandis que l'ordinateur de l'écran se charge des calculs. La connexion existante et le transfert de données continuent toutefois de générer une certaine charge.

### Éditeur : Acquisition et calcul des valeurs {#editor-werte-erfassen-und-berechnen}

![Éditeur avec des widgets numériques colorés, des liaisons de valeurs et une « MathBox » à côté de l'indicateur de batterie](/images/grafik-visual-studio/battery-math-editor.png)

*Les widgets auxiliaires colorés permettent de suivre le traitement des données au sein de l'éditeur. Les couleurs rouge et bleu distinguent les deux valeurs d'entrée positives, tandis que la « MathBox » grise affiche le résultat calculé. Les lettres aux points de connexion ainsi que les poignées sont des éléments d'aide propres à l'éditeur.*

| Widget | Rôle dans l'exemple |
| --- | --- |
| Deux **widgets « Number »** (numériques), rouge et bleu | Lire une valeur de capteur pour la charge et la décharge, respectivement, et la transmettre via le point de départ du flux de données activé. Les couleurs servent à les distinguer ; elles ne déterminent pas le signe. |
| **Connexions de valeurs** | Relier les sorties « Number » aux entrées **O** et **M** du bloc mathématique, et transmettre le résultat calculé depuis la sortie **A** vers l'indicateur de puissance. Ces liaisons sont invisibles lors de l'exécution (runtime). |
| **Bloc mathématique « SVG LineBox Math »** (gris) | Soustraire les deux valeurs d'entrée positives l'une de l'autre et fournir la puissance résultante, signe inclus, via la sortie **A**. |
| **Indicateur de batterie industriel** | Afficher la puissance calculée. La température et l'état de charge restent des mesures distinctes ; ils ne font pas partie de ce calcul de différence. |
| **Lignes SVG** | Visualiser le flux d'énergie entre les panneaux solaires et la batterie. Elles peuvent être animées ; leur sens doit correspondre à l'affectation départ/arrivée et à la convention de signe choisies. |
| **Affichages numériques sur les lignes solaires** | Indiquer la puissance solaire correspondante ; ces valeurs ne font pas partie des deux entrées utilisées pour le calcul de la différence au niveau de la batterie. |
| **Panneaux solaires industriels** | Représenter graphiquement les deux sources photovoltaïques (PV). |

Dans l'éditeur, les entrées **O = 1249** et **M = 0** sont connectées ; le bloc mathématique affiche **1249**. Pour cette configuration, la différence est **`O - M`**. Configurez **O** et **M** comme entrées, et **A** comme sortie. Activez la facture 1, sélectionnez **Formule personnalisée**, saisissez `O - M` et, sous **Sorties**, saisissez `A`. L'option **Transmettre le résultat en interne vers une entrée** doit rester désactivée. Activez le point de sortie sur les deux widgets numériques (« Number ») et effectuez la connexion à partir de ce point précis.

La signification du signe est déterminée par l'affectation des capteurs. Si **O correspond à la puissance de charge** et **M à la puissance de décharge**, alors :

| Puissance de charge O | Puissance de décharge M | Résultat O − M | Signification |
| --- | --- | --- | --- |
| 1249 W | 0 W | +1249 W | Charge |
| 0 W | 420 W | −420 W | Décharge |
| 0 W | 0 W | 0 W | Aucun flux net |

Si les capteurs sont raccordés à l'inverse, la signification du signe est inversée. Pour utiliser la convention opposée, employez `M - O`. Lorsque les valeurs sont simultanément positives, la différence indique le **flux net**, et non les deux puissances individuelles. Une valeur **0** réelle constitue une donnée d'entrée valide ; une valeur de capteur manquante ou invalide n'est pas automatiquement remplacée par zéro.

### Exécution (Runtime) : Affichage sans widgets auxiliaires {#runtime-anzeige-ohne-hilfswidgets}

![Exécution avec lignes solaires et affichage de la batterie ; les widgets auxiliaires colorés et la MathBox sont masqués](/images/grafik-visual-studio/battery-math-runtime.png)

*L'environnement d'exécution (Runtime) affiche la visualisation finale. La puissance de la batterie apparaît en bleu, la température en magenta et l'état de charge en vert. La flèche directionnelle aide à visualiser le flux d'énergie. Les captures d'écran ont été prises à des moments différents ; les valeurs mesurées ne correspondent donc pas nécessairement.*

À partir de la version **Studio 0.1.287**, cochez l'option **Masquer en exécution** (Hide in Runtime) pour les deux widgets auxiliaires de type « Number » ainsi que pour la « MathBox » (dans l'onglet **WIDGET** en haut), puis enregistrez le projet. Ces éléments restent visibles et modifiables dans l'éditeur, mais n'apparaissent pas sur l'affichage final. **Le transfert de leurs valeurs et les calculs associés continuent de fonctionner.** Les indicateurs de puissance, les éléments représentant la batterie et les lignes SVG restent, quant à eux, affichés.

Le calcul s'effectue localement dans le navigateur où l'affichage est ouvert. Grâce à ce transfert de valeurs en local, aucune entité HA (Home Assistant) supplémentaire n'est créée, et le résultat n'est pas automatiquement renvoyé vers Home Assistant. Si l'affichage — ou le navigateur correspondant — est fermé, le calcul s'arrête également.

## Configuration alternative : Batterie → Onduleur {#alternative-zuordnung-batterie-→-wechselrichter}

Un widget de type **Number** peut transmettre une valeur (issue d'une entité ou d'une prévisualisation) à un module de calcul (« Math »). Activez son **point de sortie** dans la section **Flux de données** (Data Flow) et reliez ce point précis à une entrée active du module de calcul. Pour créer des liaisons invisibles, utilisez des connexions de valeurs ou, à partir de la version **0.1.285**, des lignes SVG avec un **Z-index** défini explicitement à **-100 ou moins**. L'élément devient invisible lors de l'exécution, mais les valeurs restent actives.

Si la puissance **P** circule **vers la batterie** et que **O** (sortie) provient **de la batterie**, alors pour une ligne reliant la batterie à l'onduleur, les conditions suivantes s'appliquent :

| Paramètre | Valeur |
| --- | --- |
| O | Entrée ; `sensor.hyper_2000_eg_1_output_pack_power` |
| P | Entrée ; `sensor.hyper_2000_eg_1_pack_input_power` |
| A | Sortie |
| Calcul 1 | Activer ; Formule personnalisée |
| Formule | `O - P` |
| Sorties | `A` |
| Transfert interne | Désactivé |

Les deux capteurs peuvent fournir des valeurs positives : O = 0, P = 1252 donne **−1252 W** (charge) ; O = 150, P = 0 donne **+150 W** (décharge). Si des valeurs sont actives simultanément, le résultat correspond au flux net. Une valeur de **0 est valide**. Le message « Entrée O : Valeur manquante… » indique qu'aucune valeur valide n'est reçue via la connexion : activez la sortie, vérifiez le point de départ correspondant et affectez la cible de la ligne à l'entrée O. Les valeurs manquantes ne sont pas traitées comme des zéros.

À partir de **0.1.141**, l'option **Masquer à l'exécution** (dans la section « Calcul ») masque uniquement l'affichage ; tous les calculs et transferts de valeurs restent actifs. La variante **Calcul de valeur** dans [HA Graphique – Flux de données](/fr/projects/grafik-visual-studio/datenfluss) utilise la même logique et est activée par défaut avec cette option. Des convertisseurs de valeur et des connexions de valeur invisibles peuvent être placés en amont.

À partir de la version **0.1.138**, la boîte de dialogue agrandie intègre **quatre calculs distincts**. Chacun dispose de sa propre activation, de sa propre formule (ou calcul de moyenne), de sa propre liste de sorties et d'un aperçu des résultats. Pour les projets existants, le premier calcul reprend les paramètres et les sorties précédemment définis ; les calculs 2 à 4, ainsi que toutes les entrées internes, sont désactivés par défaut.

## Taille, icône et couleurs {#große-icon-und-farben}

À partir de la version **0.1.140**, l'onglet **WIDGET** propose les cinq mêmes sections CSS que celles disponibles pour les widgets de base : **CSS Général**, **CSS Police et Texte**, **CSS Arrière-plan**, **CSS Bordures** et **CSS Ombres et Espacement**. Ces options permettent de configurer la position, l'affichage, la transparence, la police, l'alignement du texte, l'image d'arrière-plan, les bordures, le **rayon des coins**, les ombres ainsi que les marges internes et externes. La taille de la police, l'alignement du texte, le rayon des coins et la marge interne s'appliquent également à « LineBox Math ». Les points d'ancrage conservent leurs coordonnées géométriques initiales même en cas d'arrondi des angles ; l'utilisation de rayons plus importants peut toutefois éloigner le bord visible de la bordure par rapport aux sommets. Le style CSS personnalisé reste prioritaire sur les paramètres définis dans les champs correspondants. L'onglet **CSS**, quant à lui, contient le code CSS global du projet.

À partir de la version **0.1.139**, la largeur et la hauteur peuvent être définies indépendamment, dans une plage allant de **32 à 2000 px**, soit via la boîte de dialogue de calcul, soit à l'aide des poignées de redimensionnement dans l'éditeur. Il est ainsi possible de créer des formes rectangulaires. Les 16 points d'ancrage conservent leur position relative, et les connexions continuent d'aboutir perpendiculairement. Pour les widgets de petite taille, les marqueurs de l'éditeur sont réduits afin d'éviter tout chevauchement. Il est conseillé d'utiliser une vue agrandie dans l'éditeur pour faciliter l'assignation des lettres ; En phase d'exécution (runtime), les marqueurs sont masqués.

Sous **Affichage**, vous pouvez choisir une icône (optionnelle), définir sa taille (8–512 px) et sa couleur, ainsi que les couleurs de l'arrière-plan, de la bordure et du texte du résultat. Les icônes sont ajustées à l'espace disponible. L'application d'une couleur nécessite une icône compatible ; les images matricielles (raster) multicolores conservent leurs couleurs d'origine. L'option **Afficher le résultat** peut être désactivée sans interrompre le calcul ni la transmission des données. Pour une taille de 32 × 32 px, il est judicieux d'utiliser une icône et de masquer le texte du résultat.

Le champ **Style CSS supplémentaire** permet d'ajouter des déclarations CSS en ligne (inline), par exemple `border-radius: 4px; opacity: 0.8;`. Ce style est appliqué après les paramètres de couleur et peut les remplacer. Les URL et les expressions exécutables ne sont pas autorisées.

![Petit élément « LineBox Math » avec une icône de calculatrice](/images/grafik-visual-studio/math-size-icon.png)

*Exemple simple dans l'éditeur, avec une icône et un texte de résultat masqué.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/math-size-icon.png)

![Élément « LineBox Math » avec coins arrondis via CSS](/images/grafik-visual-studio/math-css.png)

*Un rayon d'angle de 24 px est défini dans les bordures CSS. Les points de connexion visibles dans l'éditeur conservent leur position.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/math-css.png)

## Affichage en mode exécution (Runtime) {#darstellung-in-der-runtime}

![Carré « LineBox-Math » avec un résultat de 90 et des connexions à angle droit](/images/grafik-visual-studio/math-runtime.png)

*Scénario de test en mode exécution : le carré et le résultat restent visibles ; les lignes de connexion entrent et sortent à angle droit. Les lettres identifiant les connexions ainsi que les poignées de sélection de l'éditeur sont masquées. Le résultat est calculé selon la formule définie et la somme des valeurs présentes sur chaque entrée utilisée.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/math-runtime.png)

## Quatre calculs et affectation de sortie {#vier-rechnungen-und-ausgangszuordnung}

![Boîte de dialogue étendue « SVG LineBox Math » avec des calculs distincts et un transfert interne vers l'entrée C](/images/grafik-visual-studio/linebox-math-four-dialog.png)

La capture d'écran actuelle montre les calculs séparés ainsi que le transfert interne activé vers l'entrée C. Cela permet au « calcul 2 » de traiter directement le résultat issu du « calcul 1 ».

## Calcul sur l'ordinateur d'affichage {#berechnung-auf-dem-display-computer}

Les calculs sont effectués dans le navigateur de l'ordinateur d'affichage concerné. Home Assistant fournit les valeurs des entités ; « SVG LineBox Math » calcule les résultats à partir de ces données et les transmet à d'autres widgets au sein de la visualisation. Même dans le cas de calculs enchaînés impliquant plusieurs entrées et sorties, aucune entité ou automatisation supplémentaire dans Home Assistant n'est requise.

Ainsi, l'ordinateur associé à l'écran prend en charge les calculs et l'affichage. Chaque écran ouvert calcule sa propre visualisation. Home Assistant demeure responsable de la connexion et de l'échange des valeurs des entités ; cette communication génère toujours une certaine charge. Les résultats des calculs effectués localement ne sont pas automatiquement enregistrés dans Home Assistant via le mécanisme interne de transfert vers les points de connexion.

Les calculs ne sont disponibles que tant que la visualisation est ouverte et que le navigateur correspondant est en cours d'exécution. Pour les processus devant continuer à fonctionner de manière fiable même lorsque l'écran est éteint, il est nécessaire de recourir à un calcul côté serveur ou à une automatisation dans Home Assistant.

## Configuration des sorties {#ausgange-konfigurieren}

Définissez d'abord les rôles des connexions dans la partie supérieure. Ensuite, pour chaque calcul activé, saisissez les lettres souhaitées dans le champ **Sorties (par ex. E,F;H)**. Les virgules, points-virgules et espaces sont acceptés comme séparateurs ; les lettres minuscules sont également reconnues. `E,F;H` attribue le même résultat aux trois sorties E, F et H. Chacun de ces points doit être configuré comme une **sortie** active. Si une lettre est définie comme entrée, un avertissement s'affiche ; une attribution contradictoire ne peut pas être validée. Une sortie ne peut être associée qu'à un seul calcul. Une sortie sans attribution ne fournit aucune valeur.

## Traitement interne des résultats {#ergebnisse-intern-weiterverarbeiten}

Chaque calcul dispose d'une option, désactivée par défaut, intitulée **Transmettre le résultat en interne vers une entrée**. Une fois cette option activée, vous pouvez sélectionner une lettre d'entrée active spécifique sous la rubrique **Entrée interne**. D'autres calculs pourront ensuite utiliser cette lettre dans leurs propres formules. Dans ce cas de figure, la transmission interne se substitue aux valeurs provenant des lignes externes ; si l'option est désactivée, les lignes connectées reprennent leur rôle. Un seul résultat interne est autorisé par entrée. L'ordre des numéros de calcul n'a aucune incidence sur la résolution des dépendances.

Exemple avec A = 150 et B = 30 :

| Calcul | Formule | Sorties | Transmission interne | Résultat |
| --- | --- | --- | --- | --- |
| 1 | `A + B` | `E,F;H` | activée → Entrée C | 180 |
| 2 | `C * 2` | `G` | désactivée | 360 |
| 3 | `A - B` | `I` | désactivée | 120 |
| 4 | désactivé | — | désactivée | — |

Un calcul ne peut pas renvoyer son résultat vers une entrée dont il dépend lui-même. Les boucles de rétroaction (directes ou indirectes) ainsi que les doubles affectations sont signalées et rejetées avant toute validation. Dans le cas d'une **moyenne de toutes les entrées occupées**, les entrées internes activement affectées sont également prises en compte ; par conséquent, transmettre le résultat de ce calcul de moyenne vers sa propre zone d'entrée constituerait une boucle de rétroaction.

Une erreur de calcul, telle qu'une division par zéro, interrompt le calcul concerné ainsi que tous les calculs qui en dépendent. Les calculs indépendants continuent de fonctionner. Les valeurs manquantes ne sont pertinentes que si le calcul utilise l'entrée correspondante ; un calcul de moyenne, par exemple, nécessite des valeurs valides sur toutes les entrées occupées. La fenêtre de dialogue affiche des indications pour chaque calcul. Sur les petits écrans, le contenu devient défilant et les zones de calcul sont disposées les unes en dessous des autres.

## Principes de base et exemple d'un calcul individuel {#grundlagen-und-beispiel-einer-einzelrechnung}

L'image suivante montre la fenêtre de dialogue originale issue de Studio 0.1.137. Le calcul continue de fonctionner en tant que « Calcul 1 » dans la fenêtre de dialogue étendue.

![SVG LineBox Math : Fenêtre de dialogue de calcul avec connexions A–P, valeurs d'entrée et moyenne de 90](/images/grafik-visual-studio/linebox-math-dialog.png)

L’image montre la fenêtre de calcul avec la **moyenne de toutes les entrées connectées**. L’entrée **A** contient déjà la somme de ses deux lignes (100 + 50 = **150**), tandis que l’entrée **B** fournit **30**. Le résultat est donc **90**. **G** est configuré comme sortie et transmet ce résultat. Les lettres vertes A, B et G indiquent des points connectés ; les lettres orange correspondent à des points sans ligne. Une entrée non connectée affichant `—` n’est pas prise en compte dans la moyenne. Dans ce mode de calcul, le champ de formule est désactivé, mais la formule précédemment saisie est conservée.

À partir de la version Studio 0.1.137, l'élément **SVG LineBox Math** est disponible sous la rubrique **HA Grafik – Spezial**. Il apparaît sous forme de carré, tant dans l'éditeur qu'en mode exécution (Runtime). Ses 16 points de connexion sont désignés par les lettres A à P, dans le sens des aiguilles d'une montre, en commençant par le coin supérieur gauche : A–E en haut, E–I à droite, I–M en bas et M–A à gauche. Chaque côté comporte trois points supplémentaires situés entre les coins. Dans l'éditeur, les points connectés sont affichés en vert et les points libres en orange, avec des lettres très contrastées ; ces repères disparaissent en mode exécution. Les lignes se raccordent à angle droit. Les points A/E sont alimentés par le haut, les points I/M par le bas, et les points latéraux par le bord du côté correspondant.

Sélectionnez le widget et ouvrez l'option **Modifier le calcul**. Vous pouvez y définir la largeur et la hauteur (32–2000 px), attribuer les rôles **Désactivé**, **Entrée** ou **Sortie** à chaque lettre, et configurer le calcul. Par défaut, les nouveaux points de connexion sont désactivés ; l'attribution d'un rôle d'entrée ou de sortie dans la fenêtre active le point correspondant. Il est également possible d'activer tous les points simultanément via la section **Points de connexion**.

La fonction **Formule personnalisée** prend en charge les éléments `+`, `-`, `*`, `/`, les parenthèses, les nombres avec séparateur décimal ainsi que les lettres A à P. La multiplication et la division sont prioritaires sur l'addition et la soustraction. Exemple : `(A + B) / C`. Lorsque plusieurs lignes sont connectées à une même entrée, leurs valeurs sont additionnées en tenant compte de leur signe : A avec 100 et 50 donne 150 ; B avec 30 donne, dans le cas de `A - B`, une valeur de 120. L'option **Moyenne de toutes les entrées occupées** comptabilise chaque borne d'entrée occupée une seule fois (voir `(150 + 30) / 2 = 90`) ; les points non occupés ne sont pas pris en compte.

L'aperçu affiche les valeurs d'entrée ainsi que le résultat. Les sorties transmettent le résultat en interne vers des lignes SVG, d'autres « LineBoxes » et des widgets capables de récupérer des valeurs numériques via un point d'ancrage. Aucune entité HA (Home Assistant) supplémentaire n'est requise. L'absence de valeurs connectées, des valeurs invalides, des entrées de formule non occupées, une division par zéro ou des boucles de rétroaction interrompent la sortie. Le widget affiche alors `—` accompagné d'un message d'erreur ; les formules sont évaluées sans exécution de code JavaScript. Les modifications ne sont prises en compte qu'après avoir cliqué sur **Appliquer** ; la fonction « Annuler » est également disponible.
