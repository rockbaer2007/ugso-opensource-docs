---
title: Aperçu des widgets
---

# Aperçu des widgets {#widget-ubersicht}

**Standard CSS à partir de Studio 0.1.271 :** Tous les widgets, à l'exception de la gamme « Industrial », intègrent désormais les groupes complets suivants : **CSS Général**, **CSS Police et Texte**, **CSS Arrière-plan**, **CSS Bordures** ainsi que **CSS Ombres et Espacement**. Cela s'applique également aux ensembles de widgets installés ultérieurement. Les paramètres existants sont conservés ; les nouveaux groupes optionnels ajoutés sont désactivés par défaut. La gamme « Industrial » continue d'utiliser ses propres paramètres de structure (boîtier).

Ensemble externe autonome : [Calendar +](/fr/projects/grafik-visual-studio/calendar-plus), disponible à partir de **Studio 0.1.266**. Détecte automatiquement tous les calendriers Home Assistant (activés par défaut). Chaque calendrier peut être affiché ou masqué individuellement et dispose de ses propres paramètres de couleur et de couleur d'arrière-plan. Liste des événements, regroupement par jour et fenêtre contextuelle détaillée ; détection automatique de la langue (allemand/anglais). Inspiré de [xBourner/calendar-card-plus](https://github.com/xBourner/calendar-card-plus).

**Sauvegarde automatique (Autosave) à partir du Studio 0.1.265 :** Le délai configuré (par ex. deux secondes) commence à courir après la dernière modification détectée. En cas d'échec de la sauvegarde, une nouvelle tentative est effectuée automatiquement après cinq secondes, même si aucune autre modification n'a été apportée entre-temps. Si une requête de sauvegarde reste bloquée, elle est interrompue après 15 secondes (délai d'expiration/timeout), ce qui évite tout blocage permanent des sauvegardes ultérieures. Les modifications effectuées pendant une requête en cours sont conservées pour la sauvegarde suivante. En cas de sauvegarde manuelle, le système attend, si nécessaire, la fin de la requête en cours.

À partir du **Studio 0.1.264**, les fonctions **Runtime** et **Nouvel onglet** enregistrent le projet en cours avant de s'ouvrir. Ainsi, la Runtime prend en compte les widgets qui viennent d'être déplacés, sans qu'il soit nécessaire de cliquer manuellement sur « Enregistrer ». Cela s'applique à tous les ensembles de widgets. Le système attend la fin des opérations de sauvegarde en cours ; en cas d'échec de la sauvegarde, l'éditeur reste ouvert. Les onglets Runtime déjà ouverts doivent être rechargés si des modifications sont apportées ultérieurement.

Ensemble externe autonome : [Printer](/fr/projects/grafik-visual-studio/printer) avec état de l'imprimante et **1 à 6 cartouches réparties automatiquement de manière uniforme**, à partir du Studio **0.1.261**. Inspiré de [ADNPolymerase/ha-printer-card](https://github.com/ADNPolymerase/ha-printer-card), avec un dessin SVG personnalisé et une intégration à Home Assistant (lecture seule).

Autre ensemble externe : [Technic](/fr/projects/grafik-visual-studio/technic) avec **Window – Wall** (Fenêtre – Mur), à partir du Studio 0.1.197. Inspiré des widgets « Technic » pour ioBroker créés par Sefina-DS ; inclut une intégration HA dédiée et est distribué sous licence MIT.

Ajout installable séparément : [Météo et chauffage](/fr/projects/grafik-visual-studio/weather-heating) comprenant un **graphique général** (à partir de 0.1.187), un **graphique en barres sur deux semaines** (à partir de 0.1.188), un **widget météo** (à partir de 0.1.189), un **aperçu des pièces chauffées** (à partir de 0.1.190), un **widget météo METEORED** (à partir de 0.1.191), un **aperçu de l'état des fenêtres** (à partir de 0.1.192), une fonction **« Informer mon propriétaire »** (à partir de 0.1.193) et les **paramètres généraux de chauffage** (à partir de 0.1.194). Ce paquet optionnel ne fait pas partie des 74 widgets intégrés et se voit automatiquement attribuer une couleur d'ensemble disponible.

Le catalogue de widgets actuel contient **74 éléments répartis en cinq groupes**. Les noms correspondent à ceux figurant dans la palette de l'éditeur. Les widgets liés à une entité lisent l'état actuel dans Home Assistant lors de l'exécution (runtime) ; en l'absence d'entité, ils utilisent des valeurs de prévisualisation ou des valeurs explicitement configurées. L'accès en écriture est limité aux widgets et types d'entités mentionnés ci-dessous. Les changements d'état externes sont interrogés toutes les cinq secondes. Les modifications apportées par l'utilisateur à un curseur (slider) sont immédiatement répercutées sur les éléments de type « Number » et « SVG-Line », pendant que la commande d'écriture est transmise à Home Assistant.

Les widgets de base inspirés de VIS2 conservent leurs noms en anglais. Les widgets interactifs, tels que les calendriers et les curseurs, utilisent des noms traduits dans la palette. Les anciens noms de la palette restent utilisables comme termes de recherche. Les noms personnalisés attribués aux widgets et déjà enregistrés demeurent inchangés.

**La fonction « HTML Logout » n'est pas reprise** et n'est pas prévue pour faire partie des futurs widgets du Studio.

À partir de la version Studio 0.1.135, le nom technique du widget reste visible dans l'interface de l'éditeur. Sur la zone de travail et lors de l'exécution, seules les étiquettes personnalisées s'affichent ; les nouveaux widgets sont créés sans titre prédéfini. Cette règle s'applique également aux futurs packs de widgets ainsi qu'au composant « LineBox ». Lors du chargement de projets plus anciens, les titres par défaut existants sont supprimés. Les étiquettes personnalisées sont conservées ; il est toutefois possible de saisir à nouveau manuellement un ancien texte par défaut si vous le souhaitez.

**Widgets permettant l'écriture :** Les widgets « Switch », « Icon Toggle Button », « Bool Checkbox », « Bool Select », « Bool SVG » et « Bool HTML (control) » agissent sur les entités `switch`, `light` ou `input_boolean` qui leur sont associées. Le widget « Bulb on/off » permet de commuter ces entités ou de définir un « helper » (assistant) `input_number` à sa valeur minimale ou maximale configurée. Les curseurs (« Slider ») et les curseurs radiaux (« Radial Slider ») écrivent uniquement dans `input_number` ; le widget « Input val » écrit dans `input_number` ou `input_text`. Le widget « Note » écrit, via une boîte de dialogue dédiée, dans un « helper » `input_text` (sans sélection d'attribut). Le widget « Universal Element », en mode interrupteur (« Switch »), transmet ses valeurs « false » ou « true » ; en mode bouton-poussoir (« Push Button »), il transmet la valeur configurée suivante à une entité commutable appropriée ou à un « helper » de type numérique ou texte. Si l'entité associée est inadaptée ou indisponible, l'interaction est désactivée. Les widgets « Checkbox » et « Switch » transmettent leurs paires de valeurs configurées à des interrupteurs ou à des « helpers » numériques/textuels compatibles. Le widget « Dropdown » permet de sélectionner des options dans `select`/`input_select` ou des valeurs personnalisées au sein de « helpers » numériques ou textuels. Les autres widgets ne modifient aucun état dans Home Assistant (HA).

## Graphismes HA – Base (46) {#ha-grafik-–-basis-46}

| Widget | Fonction actuelle |
| --- | --- |
| Tabs — Tabs (Onglets) | À partir de 0.1.116 : 1 à 20 onglets, disposés horizontalement ou verticalement ; en mode horizontal, ils peuvent être alignés par défaut, centrés ou occuper toute la largeur. Pour chaque onglet, il est possible de définir un titre, une icône ou une image, la taille et la couleur de l'icône, ainsi que le comportement en cas de dépassement (débordement) sur les axes X et Y. Le contenu peut être une zone de widgets dédiée ou une page existante du projet. Seul le contenu actif est intégré lors de l'exécution (runtime) ; La sélection reste enregistrée localement dans le navigateur. |

### Modifier les onglets {#tabs-bearbeiten}

À partir de la version Studio 0.1.122, le paramètre principal **Onglets** propose le curseur **Assombrir les onglets inactifs (%)**, réglable de 0 à 90. À 0, les couleurs restent inchangées ; à 90, il ne subsiste que 10 % de la luminosité. L'arrière-plan, le texte et l'icône des onglets inactifs sont assombris simultanément ; l'onglet actif et le contenu de l'onglet restent inchangés. Ce paramètre s'applique aux dispositions horizontales comme verticales et est enregistré dans le projet.

À partir de la version Studio 0.1.121, vous pouvez définir séparément la **Couleur du texte (actif)** et la **Couleur du texte (inactif)** dans le paramètre principal **Onglets**. Ces réglages s'appliquent aux libellés de tous les onglets, en fonction de la sélection actuelle. Si une valeur est laissée vide, la **Couleur de l'onglet** définie précédemment est utilisée. La couleur de l'icône de chaque onglet reste indépendante ; la couleur de l'onglet continue par ailleurs de déterminer le marquage de l'élément actif.

**Débordement X** et **Débordement Y** proposent, à partir du studio 0.1.120, les options `none`, `visible`, `hidden`, `scroll`, `auto`, `initial` et `inherit`. `none` supprime la définition CSS spécifique, `visible` laisse visible le contenu qui dépasse, `hidden` le masque (coupe), `scroll` active les barres de défilement et `auto` les affiche si nécessaire. `initial` utilise la valeur CSS initiale, tandis que `inherit` reprend la définition de l'élément parent. En l'absence de sélection enregistrée, `auto` est appliqué par défaut. Le CSS peut agir sur les deux axes simultanément, notamment lorsque `visible` est combiné avec un autre axe doté d'une barre de défilement.

À partir du studio 0.1.119, vous pouvez définir indépendamment la **couleur d'arrière-plan** de chaque **onglet [n]**. Cette couleur s'applique à l'onglet correspondant, que la disposition soit horizontale ou verticale ; l'indicateur de l'onglet actif reste visible.

Insérez des **onglets** depuis la palette et définissez la largeur et la hauteur au niveau du widget principal. Dans chaque onglet (**Onglet [1]**, **Onglet [2]**, etc.), vous pouvez choisir le type de contenu. L'option **Modifier la zone de l'onglet** permet d'accéder à l'espace dédié — via la palette de widgets habituelle — ou à la page de projet référencée. L'option **Retour au widget Onglets** permet de revenir au widget principal. La taille du contenu personnalisé est déterminée par le widget principal, diminuée de 44 px pour les onglets horizontaux, ou jusqu'à 120 px pour les onglets verticaux (dans la limite de la moitié de la largeur du widget). Ces zones personnalisées font partie intégrante du widget et n'apparaissent pas en tant que pages de projet distinctes. Les pages existantes demeurent des références partagées ; toute modification affecte toutes les instances intégrées.

À partir de la version Studio 0.1.124, le contenu des onglets actifs est affiché directement depuis le projet ouvert, sans recours à un iFrame ni rechargement lors du changement d'onglet. Un clic sur la zone de contenu permet d'accéder à son édition ; après le retour, les modifications (même non enregistrées) sont immédiatement visibles. Pensez toutefois à enregistrer vos travaux avant d'ouvrir une instance d'exécution (Runtime) séparée, surtout si la fonction de sauvegarde automatique (Auto-Save) est désactivée. L'instance d'exécution interroge également les valeurs des entités pour le contenu des onglets actifs. Les pages existantes de grande taille sont affichées sans mise à l'échelle automatique ; les paramètres de débordement (Overflow X/Y) contrôlent la possibilité de faire défiler le contenu. Si le nombre d'onglets est réduit, le contenu personnalisé masqué est conservé en mémoire et réapparaît si le nombre d'onglets est augmenté à nouveau. Les opérations de copie, de regroupement, ainsi que l'exportation et l'importation préservent le contenu personnalisé ; les copies se voient attribuer de nouveaux identifiants (ID) de widget et de groupe. L'imbrication cyclique de pages est empêchée. L'ajout d'autres widgets d'onglets au sein de zones d'onglets personnalisées n'est pas pris en charge pour le moment. Cette implémentation est autonome ; elle n'est pas liée à une fonction d'importation depuis VIS2.

### Autres widgets de base {#weitere-basis-widgets}

| Widget | Fonctionnalité actuelle |
| --- | --- |
| link | Contenu HTML formatable servant de lien vers une URL. |
| Note | Bloc-notes affichant la valeur d'une entité, un texte de test, un coin éventuellement masqué et une boîte de dialogue textuelle. |
| Screen Resolution — Résolution d'écran | Affiche la résolution actuelle de la fenêtre. |
| Red Number — Chiffre en couleur | Valeur numérique représentée sous forme de cercle coloré ou de punaise, avec un rayon personnalisable. |
| Bool SVG — SVG booléen | Affiche l'un des deux motifs SVG disponibles en fonction de l'état actuel ; peut piloter une entité commutable ou un « helper » (assistant) de type 0/1 approprié. |
| SVG shape | Dessine une forme géométrique SVG avec couleur, épaisseur du trait, rotation et mise à l’échelle. |
| Input val — Champ de saisie | Champ de saisie pour texte ou nombres (150 × 70). Mode numérique avec valeurs min/max optionnelles ; le mode « lecture seule » permet également d'afficher des capteurs. La touche « Entrée » valide systématiquement la saisie. L'option « Auto-set » (validation automatique) déclenche l'écriture après une pause configurable (1000 ms par défaut) ; elle fonctionne également avec « withEnter ». L'option « withEnter » ajoute un bouton de validation pour les saisies non encore envoyées. Si « Auto-set » est désactivé, quitter le champ ne déclenche aucune écriture. Les données sont écrites vers des « helpers » (assistants) de type `input_number` ou `input_text` ; en l'absence d'entité, la saisie reste locale. |
| View in widget — Vue dans un widget | Intègre une page de projet Studio (300 × 200 par défaut) ; l'imbrication récursive est empêchée. Pour les tableaux de bord Home Assistant (HA), un widget dédié est disponible dans la catégorie « Spécial ». |
| View in widget 8 — Vue dans un widget 8 | Sélectionne l'une des 50 pages disponibles en fonction de l'état d'un index. |
| iFrame | Intègre une URL, si la page cible l'autorise ; avec des options pour la bordure, le défilement et l'actualisation. |
| iFrame 8 | Sélectionne un cadre (frame) parmi [0] à [20] en fonction de l'état de l'index, avec un paramètre « sandbox » spécifique pour chaque URL. |
| Image 8 | Sélectionne une image, de [0] jusqu'à un maximum de [200], en fonction de l'état de l'index. |
| AckFlag HTML | Affiche deux états HTML configurables ; Home Assistant ne dispose pas d'un indicateur (flag) natif équivalent au `ack` d'ioBroker. |
| Icon Toggle Button — Bouton bascule avec icône | Bouton utilisant des images distinctes pour les états « activé » et « désactivé » ; permet de piloter une entité commutable. |
| Switch — Interrupteur (Switch) | Commutateur graphique marche/arrêt ; permet de piloter une entité commutable. |
| Bool Checkbox — Case à cocher booléenne | Sélection marche/arrêt ; permet de piloter une entité commutable. |
| Bulb on/off — Ampoule marche/arrêt | Icône d'ampoule avec des images distinctes pour les états « allumé » et « éteint » ; permet de piloter une entité commutable ou une entité auxiliaire numérique (helper). |
| Slider — Curseur (Slider) | Curseur avec minimum, maximum et pas d'incrémentation ; les étiquettes « min » et « max » peuvent être activées via une case à cocher. Les limites doivent correspondre à l'entité auxiliaire (*helper*) utilisée, par exemple de `-200` à `200`. Une entité auxiliaire `input_number` sélectionnée fournit la valeur actuelle ; lors du déplacement du curseur, les widgets dépendants (de type *Number* ou *SVG Line*) sont mis à jour instantanément, et la valeur est transmise à Home Assistant au moment du relâchement. En l'absence d'entité, la modification reste locale. À partir de la version 0.1.114, il est possible de configurer séparément les propriétés de la piste (couleur, couleur active, épaisseur, arrondi) et celles du curseur lui-même (couleur, taille, arrondi). Le type de piste peut être défini sur « Normal » (du minimum à la valeur actuelle), « Inversé » (de la valeur actuelle au maximum), ou désactivé. La piste et le curseur disposent chacun de leurs propres ombres, paramétrables via un décalage X/Y, un flou, une extension et une couleur (format CSS/RGBA). Arrondi : 0 % pour des angles vifs, 100 % pour une forme entièrement arrondie ; si toutes les valeurs de taille de l'ombre sont à 0, celle-ci est désactivée. Des graduations restent disponibles en haut ou en bas, avec l'option d'afficher des chiffres. |
| Number — Nombre (Number) | Affiche une valeur numérique formatée, avec application d'un multiplicateur et gestion des décimales ; en l'absence de valeur d'entité, la valeur `--` est utilisée. À partir de la version 0.1.125, les options **Ajouter du HTML avant** et **Ajouter du HTML après (Singulier/Pluriel)** sont visibles dans l'éditeur et lors de l'exécution, même lorsqu'une entité Home Assistant est liée ; elles sont conservées lors des mises à jour instantanées. Le singulier s'applique si la valeur calculée (après application du multiplicateur) est égale à 1 ; dans le cas contraire, c'est le pluriel qui est utilisé. Si aucun texte HTML n'est défini après la valeur, l'unité configurée est utilisée à la place. En l'absence d'entité, un titre de prévisualisation est affiché. Ce widget est distinct du widget graphique « Red Number ». |
| String | Valeur textuelle avec icône et code HTML optionnels, placés avant ou après la valeur. |
| String (unescaped) — String (non échappé) | Représente une valeur HTML avec des éléments ajoutés avant et après. |
| String img src | Affiche une image provenant d'une URL contenue dans l'état. |
| TimesValue | Formate une valeur temporelle issue de l'état. |
| Timestamp Value | Formate un horodatage (timestamp) issu de l'état. |
| Timestamp | Formate l'instant de la dernière mise à jour dans HA. |
| Last change Timestamp | Formate l'instant du dernier changement d'état dans HA. |
| ValueList Text | Affiche sous forme de texte un élément de liste sélectionné via un état d'index. |
| ValueList HTML | Affiche sous forme de code HTML un élément de liste sélectionné via un état d'index. |
| ValueList HTML Style | Affiche un élément de liste HTML associé à un style CSS. |
| Bool HTML | Affiche l'un des deux contenus HTML possibles selon l'état, avec du code HTML optionnel avant et après. |
| Bool Select | Sélecteur Marche/Arrêt avec libellés personnalisables ; permet de piloter une entité commutable. |
| Bool HTML (control) | Affichage HTML Marche/Arrêt cliquable ; permet de piloter une entité commutable. |
| HTML State | Bouton HTML qui écrit une valeur fixe à chaque clic et appelle éventuellement une URL. |
| Table | Tableau généré à partir de données JSON, avec sélection de lignes et option d'impression ; un état HA (Home Assistant) lié doit contenir des lignes au format JSON. |
| Full Screen | Bouton permettant de passer l'interface en mode plein écran. |
| Bar | Barre horizontale ou verticale représentant une valeur numérique. |
| HTML | Contenu HTML entièrement configurable. |
| HTML navigation | Bouton ou lien vers une page du projet, une URL ou un chemin HA. |
| filter - dropdown | Filtre les widgets d'exécution (runtime) en fonction du mot-clé défini dans la section « Général ». |
| Text | Champ de texte libre, sans liaison avec une entité. |
| Border | Cadre avec titre, position du titre, en-tête et couleurs. |
| Horizontal line | Ligne de séparation horizontale avec extrémités réglables et fonction d'alignement (magnétisme). |
| Vertical line | Ligne de séparation verticale avec extrémités réglables et fonction d'alignement (magnétisme). |
| Gauge | Indicateur de mesure simple avec unité. |
| Image | Source d'image, options d'étirement et rechargement contrôlé ; interactions natives du navigateur disponibles en option. Taille par défaut : 200 × 130 px. |

Les images suivantes proviennent de projets de test allemands. Les cases à cocher CSS antérieures sont indiquées dans les légendes des images ; seul le comportement actuel, décrit dans le texte, fait foi.

### Paramètres CSS {#css-vorgaben}

![CSS obligatoire (Général) et sections CSS facultatives](/images/grafik-visual-studio/html-navigation-css.png)

*La section « CSS Général » est cochée et verrouillée ; les autres groupes CSS sont facultatifs.*

À partir de la version **0.1.154**, le **CSS Général** reste obligatoirement actif pour tous les widgets, y compris pour les projets déjà enregistrés et les futurs packs de widgets. La position et la taille sont ainsi préservées lors de l'exportation. Les mentions antérieures relatives à des sections CSS désactivées ne s'appliquent, à partir de cette version, qu'aux autres groupes CSS.

### Input val / Valeur saisie {#input-val-eingegebener-wert}

À partir de la version **0.1.157**, le mode numérique propose des paramètres **min/max** facultatifs. La fonction **Auto-setzen** (définition automatique) applique la valeur après une pause définie (par défaut **1000 ms**), même lorsque l'option **withEnter** est activée. La touche « Entrée » permet toujours de confirmer. L'option **withEnter** ajoute un bouton de validation pour les modifications non encore transmises ; sans la fonction « Auto-setzen », le simple fait de quitter le champ ne déclenche aucune action. Les saisies manuelles sont conservées jusqu'à leur validation. Le mode « lecture seule » permet également d'afficher des valeurs provenant de capteurs ; pour la saisie de nombres ou de texte, des composants auxiliaires appropriés (`input_number`/`input_text`) sont nécessaires. Dans l'éditeur, aucune donnée n'est jamais écrite vers HA (Home Assistant).

![Détail des paramètres de saisie avec limites numériques et définition automatique](/images/grafik-visual-studio/input-value.png)

*Extrait des paramètres de saisie : min/max 0–1000, délai 1000 ms et mode « lecture seule » activé.*

Avec le style, l'option « HTML avant » correspond à l'étiquette du champ, tandis que « HTML après » correspond au texte d'aide situé sous le champ. L'option **Sans style** affiche, quant à elle, du code HTML nettoyé avant et après un champ de saisie simple. Les variantes disponibles sont : standard, *outlined* (contour) et *filled* (rempli). Les valeurs vides, invalides ou situées en dehors des limites min/max ne sont pas inscrites. Les nouveaux widgets activent uniquement le CSS général ; les messages destinés aux utilisateurs effectuant une transition peuvent être désactivés de manière centralisée.

### Chaîne de caractères (String) {#string-zeichenfolge}

![Aperçu d'une chaîne de caractères avec une icône en forme d'ampoule de 43 pixels et des textes formatés avant et après](/images/grafik-visual-studio/string.png)

*Exemple dans l'éditeur avec une icône de 43 px, un préfixe en gras et un suffixe en italique ; la valeur source reste du texte brut.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/string.png)

À partir de la version **0.1.156**, les champs « HTML avant », « HTML après » et « Texte de test » disposent d'un éditeur HTML. La valeur de l'entité et le texte de test sont toutefois affichés sous forme de texte brut : dans le texte de test, `<b>Test</b>` affiche les balises littéralement. Seuls les éléments placés avant et après sont formatés en tant que code HTML nettoyé. Un texte de test non vide remplace la source dans l'éditeur ; en revanche, c'est la source qui est utilisée lors de l'exécution (*runtime*). En l'absence d'entité, la valeur lors de l'exécution reste vide ; si une entité ou un attribut est manquant, le résultat est `--`.

Pour le point de données ioBroker `…attribute.friendly_name`, sélectionnez l'**entité Home Assistant** correspondante et saisissez `friendly_name` dans le champ **Attribut HA (vide : état)**. Si le champ d'attribut est laissé vide, c'est l'état qui s'affiche. Aucun « assistant » (helper) n'est requis ; la sélection s'effectue en mode lecture seule. Le point de départ optionnel transmet la valeur source telle quelle, sans préfixe, suffixe ni texte de test de l'éditeur.

L'option **Icône** utilise le sélecteur d'icônes/images existant. Le paramètre **Taille de l'icône (en pixels)** n'apparaît que lorsqu'une icône est sélectionnée ; il permet de choisir une valeur entre 5 et 200 px (la valeur par défaut est 24 px). La valeur d'exportation `43` génère une icône de 43 × 43 px. Les nouveaux widgets sont créés avec un contenu vide, des dimensions de 100 × 30 px et seule l'option « CSS général » activée ; pour des icônes plus grandes, ajustez la hauteur du widget en conséquence. Les conseils destinés aux utilisateurs effectuant une migration (concernant les attributs et le texte de test) peuvent être désactivés de manière centralisée.

### HTML {#html}

![Éditeur HTML avec intervalle de mise à jour](/images/grafik-visual-studio/html.png)

*Ancienne vue de test HTML avec un intervalle de 500 ms. Depuis 0.1.154, l'option « CSS général » doit obligatoirement rester activée.*

L'option **HTML** permet d'afficher un contenu HTML personnalisé via l'éditeur HTML intégré. `<b>Hallo</b><i> Susi</i>` génère le texte « **Hallo** » suivi de « *Susi* » en italique. Le paramètre **Délai de mise à jour (ms)** permet de régénérer ce contenu à l'intervalle défini ; si le champ est laissé vide ou contient `0` ou `null`, la mise à jour périodique est désactivée. La plage s'étend jusqu'à 180 000 ms, par incréments de 100 ms. Il ne s'agit pas d'un temps d'interrogation HA et cela ne nécessite aucun « helper ».

Studio nettoie le code HTML : les scripts intégrés et les gestionnaires d'événements (event handlers) ne sont pas exécutés. Ce comportement diffère de celui de la version originale de VIS2 ; une notification destinée aux utilisateurs effectuant la transition — et pouvant être désactivée — explique ce point. `{value}` n'est pas un espace réservé (placeholder). Les nouveaux widgets démarrent avec un code HTML vide, des dimensions de 200 × 130 px et seul le « CSS général » activé ; le contenu existant est conservé. Le point de départ optionnel reste disponible.

### Navigation HTML {#html-navigation}

Le champ **HTML** permet de définir une étiquette personnalisable ; **Vue de navigation** permet de sélectionner une page du projet. Un clic, ou l'appui sur les touches Entrée/Espace, déclenche la navigation uniquement en mode exécution (runtime), sans cible d'écriture HA (Home Assistant) ni « helper ». Si aucune cible n'est définie, l'étiquette reste visible. Les nouveaux widgets démarrent avec un code HTML vide, des dimensions de 200 × 130 px et seul le « CSS général » activé. Les cibles (URL ou chemins HA) et les étiquettes précédemment enregistrées restent utilisables.

La fonction **Sous-vue** (Unteransicht), issue de VIS2, est conçue pour des systèmes de navigation spécifiques tels que « Jaeger Design » ; elle n'est pas encore implémentée dans Studio, et le champ correspondant est donc désactivé. Cela ne fait pas référence à un onglet dans Studio. Des notifications, que l'utilisateur peut désactiver, expliquent cette limitation ainsi que le nettoyage du code HTML.

### Filtre – menu déroulant {#filter-dropdown}

![Éditeur de filtres avec couleurs HEX et sélection par défaut](/images/grafik-visual-studio/filter-editor.png)

*Deux entrées : la première comporte une icône et des couleurs HEX ; la seconde constitue la sélection par défaut.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/filter-editor.png)

À partir de **0.1.155**, la fonction **editor → Bearbeiten** (éditeur → modifier) permet de gérer les entrées en définissant leur valeur, titre, icône, image, couleur du texte, couleur active et sélection par défaut. Il est possible d'ajouter ou de supprimer des entrées, ainsi que de réorganiser leur ordre dans la boîte de dialogue à l'aide des touches fléchées. En mode de sélection unique, une seule entrée peut être définie par défaut ; en mode de sélection multiple, plusieurs entrées peuvent l'être. Le bouton **Appliquer** enregistre les modifications, tandis que **Annuler** les rejette.

Les couleurs sont enregistrées au format **HEX** : `rgba(120,112,160,1)` correspond à `#7870A0`, et `rgba(65,77,25,1)` à `#414D19`. Un canal alpha peut également être ajouté (voir `#RRGGBBAA`). Le champ de couleur peut être laissé vide. La **couleur active** correspond, pour les boutons, à la couleur du texte de l'entrée sélectionnée ; l'arrière-plan, quant à lui, dépend de la variante choisie. L'icône est prioritaire sur l'image.

Le paramètre **Type** propose un menu déroulant, ou des boutons disposés horizontalement ou verticalement. Les boutons peuvent être de type *outlined* (contour), *contained* (plein) ou *text* (texte) ; les menus déroulants peuvent être *standard*, *outlined* ou *filled* (rempli), avec des options supplémentaires comme le nom, l'autofocus et une taille réduite. La liste déroulante affiche les icônes/images et prend en charge la navigation au clavier. L'option **Aucun filtre** permet de masquer l'option de réinitialisation ; Pour le reste, le choix du texte est libre.

Les valeurs de filtrage correspondent au **mot-clé de filtre** des widgets présents sur la même page. L'utilisation d'une virgule ou d'un point-virgule au sein d'une valeur permet de cibler plusieurs mots-clés de filtre. Les widgets dépourvus de mot-clé de filtre restent visibles. Les sélections et filtrages par défaut s'appliquent lors de l'utilisation (en mode exécution) ; les widgets demeurent modifiables dans l'éditeur. Chaque page conserve sa propre sélection, indépendante des autres. Aucune entité « auxiliaire » (helper) de Home Assistant n'est requise. Les nouveaux filtres sont créés avec une liste d'entrées vide, des dimensions de 200 × 50 px, et seul le paramètre « CSS général » activé. Les listes simples existantes restent fonctionnelles.

### Barre {#bar}

![Barre bleue inversée avec paramètres de bordure et d'ombre](/images/grafik-visual-studio/bar.png)

*Aperçu du test précédent : la barre inversée s'étend depuis la droite. Le paramètre « CSS général » doit rester activé.*

[Ouvrir l'image en taille réelle](/images/grafik-visual-studio/bar.png)

Le widget **Barre** affiche une valeur numérique — comprise dans une plage définie par un **Minimum** et un **Maximum** — sous la forme d'une barre colorée. Pour une plage allant de 0 à 1000, une valeur de 300 correspond à un taux de remplissage de 30 %. Les valeurs situées en dehors de cette plage sont ramenées (tronquées) à l'échelle 0–100 % ; si le minimum et le maximum sont identiques, la barre reste vide. Une entité de type « capteur » (sensor) dans Home Assistant — par exemple, celle mesurant la production d'énergie solaire — est parfaitement adaptée ; le widget fonctionne en mode lecture seule et ne nécessite aucune entité « auxiliaire » (helper) supplémentaire.

En orientation horizontale, la barre s'étend depuis la gauche ; en orientation verticale, elle s'étend depuis le haut. L'activation de l'option **Inverser la valeur** déplace l'origine vers la droite ou vers le bas, selon le cas — bien qu'une valeur de 30 % continue de représenter 30 %. Le champ **Border** (Bordure) attend une syntaxe CSS, telle que `2px solid blue`. L'entrée individuelle `2` issue de l'exportation ne constitue pas une définition complète de bordure. Le paramètre **Transparency (Shadow/CSS)** (Transparence/Ombre/CSS) correspond au champ VIS2 `shadow` et attend une définition d'ombre CSS (par ex. `2px 2px 4px #0008`) plutôt qu'une simple valeur de transparence. Les valeurs d'opacité « Studio » enregistrées précédemment restent en vigueur.

Les nouvelles barres apparaissent initialement en bleu et en position horizontale, avec une plage de 0 à 100, des dimensions de 200 × 130 px, et seul le paramètre CSS « General » (Général) activé. Des « notes de transition » expliquent les différents champs ; elles peuvent être désactivées en sélectionnant **Hide transition notes** (Masquer les notes de transition). Le point de départ optionnel demeure disponible.

### État HTML {#html-state}

![État HTML avec une valeur fixe et des notes de transition](/images/grafik-visual-studio/html-state.png)

*Cet exemple affiche « Hallo » (Bonjour) et envoie une commande « off » (désactivation) ; les petites notes expliquent les cibles d'écriture et les appels d'URL dans le navigateur.*

**HTML** fait référence au contenu affiché. **Value** (Valeur) représente une valeur d'écriture fixe : chaque clic envoie la même valeur, quel que soit l'état actuel. Votre exemple, utilisant `Hallo` et `off`, affiche « Hallo » et envoie une commande « off » à une entité Home Assistant compatible (commutable) à chaque clic. Un capteur ne peut pas servir de cible d'écriture. Les valeurs numériques nécessitent un assistant (`helper`) correspondant de type `input_number`, tandis que les valeurs textuelles requièrent un assistant de type `input_text` ; les éléments `switch`, `light` et `input_boolean` prennent en charge les valeurs « on/off » (activation/désactivation) appropriées. Les cibles indisponibles ou inadaptées ne feront l’objet d’aucune écriture.

**Appeler une URL au clic** envoie, de manière facultative, une requête HTTP(S) de type GET depuis le navigateur. La vue reste ouverte. Cette requête fonctionne même sans cible d'écriture HA (Home Assistant) et n'est pas exécutée via un serveur ioBroker ; les règles du navigateur, le protocole HTTPS et les contraintes d'accès réseau restent en vigueur. Une réponse du navigateur, même opaque, ne garantit pas que l'action a bien été traitée par le système cible. Dans l'éditeur, aucune valeur n'est écrite et aucune URL n'est appelée. En mode exécution (runtime), l'action peut être déclenchée par un clic, la touche Entrée ou la barre d'espace.

Les nouveaux widgets présentent des champs vides, avec seule l'option « CSS général » activée. Le contenu existant est conservé ; l'ancienne valeur de prévisualisation est reprise en tant que valeur fixe, tant qu'aucune nouvelle **valeur** n'est définie. Le code HTML est affiché sous une forme nettoyée ; `{value}` ne sert pas ici d'espace réservé (placeholder). Les indications destinées aux utilisateurs en transition (affichées au niveau des entités et des URL) peuvent être désactivées de manière centralisée dans les paramètres.

### Indications pour les utilisateurs en transition {#umsteigerhinweise}

![Indication rouge (désactivable) sous une entité](/images/grafik-visual-studio/migration-hints.png)

*Exemple de « Bool-Select » avec une indication sous le sélecteur d'entité. Ces messages dans l'éditeur peuvent être désactivés de manière centralisée.*

Les indications peuvent être activées ou désactivées globalement via **Paramètres → Général → Afficher les indications pour les utilisateurs en transition**. Ce réglage est mémorisé par projet ; par défaut, ces indications sont actives. Elles s'affichent directement sous les champs concernés dans l'éditeur et fournissent des explications sur les cibles d'écriture HA ou les « helpers » (assistants) appropriés, les sources JSON/index, ainsi que sur les fonctions de contrôle supplémentaires non encore configurées. Un simple affichage ne nécessite aucun « helper » d'écriture additionnel. Le texte est en police de 10 px, non gras, et s'affiche en rouge clair sur fond sombre (ou en rouge foncé sur fond clair) dans l'éditeur. Ces indications n'apparaissent pas en mode exécution (runtime).

### Tableau {#table}

![Tableau avec les colonnes Title et Value](/images/grafik-visual-studio/table.png)

*Exemple de JSON statique : les métadonnées _Description n'apparaissent pas dans les deux colonnes visibles.*

Le **JSON statique (sans ID)** contient un tableau d'objets représentant des lignes. Une entité HA (Home Assistant) liée fournit, quant à elle, son état au format JSON lors de l'exécution. Dans l'exemple `[{"Title":"first","Value":1,"_Description":"Value1"},{"Title":"second","Value":2,"_Description":"Value2"}]`, les colonnes **Title** et **Value** s'affichent. Les attributs associés à `_` restent masqués en tant que métadonnées ; `_btn…` génère un bouton de confirmation. Les cellules peuvent contenir du code HTML, qui est nettoyé avant l'affichage.

Le paramètre **Nombre de colonnes** fait apparaître des options pour les titres des colonnes, la largeur CSS et l'affectation des attributs. Une affectation explicite des attributs permet également d'afficher des métadonnées. Les options **Pas d'en-tête**, **Afficher la barre de défilement** et **Nombre maximal de lignes** permettent de contrôler la présentation. Par défaut, les nouveaux tableaux n'ont que l'option « CSS général » activée. Un bouton d'impression n'apparaît que si un texte est saisi dans le champ **btn_print** ; le paramètre **view_for_print** permet, au choix, de définir la page destinée à l'impression.

**ID d'événement** lit des lignes JSON individuelles. L'état initial existant n'est pas pris en compte comme un nouvel événement. Les modifications viennent compléter la liste des événements ; les entrées partageant le même `_id` remplacent une ligne d'événement existante. L'option **Nouvel événement au début** s'applique à cette liste d'événements sans pour autant inverser le tableau de base. Les événements et la sélection sont valables pour la session d'exécution (runtime) en cours.

La sélection d'une ligne écrit l'objet correspondant au format JSON dans l'**ID de sélection** (`input_text`) et affiche `_detail` dans le **widget détaillé**. Les boutons de confirmation écrivent `_ack_id` ou l'objet de la ligne dans l'**ID de confirmation**. Les cibles HA (Home Assistant) doivent être des entités auxiliaires (helpers) de type nombre ou texte disponibles et compatibles ; leurs limites de type et de longueur restent en vigueur. Aucune valeur HA n'est écrite lors de l'utilisation de l'éditeur.

### Bool Select (Sélection booléenne) {#bool-select}

![Bool Select avec l'état « En cours » sélectionné](/images/grafik-visual-studio/bool-select.png)

*Exemple en exécution (runtime) avec un préfixe et le texte « En cours » sélectionné.*

Le champ de sélection comporte deux entrées définies par **Texte pour « false »** et **Texte pour « true »**. Il interprète les états booléens et numériques : `0` est considéré comme « false », tandis que toute autre valeur numérique est considérée comme « true ». Les états HA `off`/`on` sont mappés en conséquence. Les options **Ajouter du HTML avant**, **Ajouter du HTML après** et **Autofocus** sont disponibles ; l'autofocus ne s'applique qu'en mode exécution (runtime).

Une sélection écrit `0` ou `1` dans un élément auxiliaire (`input_number` ou `input_text`) approprié. Pour `switch`, `light` et `input_boolean`, une commande de commutation HA correspondante est envoyée. Les cibles inadaptées ou indisponibles sont désactivées. En l'absence d'entité, un aperçu local est possible lors de l'exécution (runtime) ; aucune donnée n'est écrite dans l'éditeur. Les nouveaux widgets démarrent avec des champs texte/HTML vides, l'autofocus désactivé et seul le paramètre CSS « Général » activé. Les libellés existants sont conservés.

### Bool SVG {#bool-svg}

![Bool SVG avec motif en étoile et mode « Affichage seul »](/images/grafik-visual-studio/bool-svg.png)

Sous **Général**, on trouve l'entité HA, l'option **Affichage seul**, les champs **SVG pour « false »** et **SVG pour « true »**, ainsi que la **transparence**. Les champs SVG peuvent être modifiés dans l'éditeur de code. Les nouveaux widgets ont une taille de 85 × 85 px et utilisent les deux motifs en étoile du modèle VIS2. Les coordonnées SVG et les valeurs personnalisées `transform` sont conservées ; la taille du widget n'entraîne pas de redimensionnement automatique du contenu.

`false`, `off` et la valeur numérique zéro sélectionnent le motif « false » ; les nombres différents de zéro sélectionnent le motif « true ». Lors de la commutation de valeurs numériques, le seuil VIS2 de 0,5 s'applique : en dessous, la valeur 1 est écrite ; à partir de 0,5, la valeur 0 est écrite. Les entités HA commutables disposent des états Marche/Arrêt ; Les valeurs numériques ou textuelles nécessitent un assistant `input_number` ou `input_text` approprié. L'option **Affichage uniquement** empêche toute écriture ; dans ce cas, des capteurs peuvent également servir de source. Aucune commutation n'est effectuée dans l'éditeur.

La transparence varie de 0 à 1. Dans l'éditeur, une visibilité d'au moins 20 % est maintenue afin que le widget reste modifiable ; en phase d'exécution (*runtime*), une transparence totale est possible. La section **CSS Général** est active pour la position et la taille, tandis que les autres groupes CSS sont désactivés par défaut pour les nouveaux widgets. Des notes facultatives, destinées aux utilisateurs effectuant une migration, expliquent les objectifs de configuration et le comportement de la transparence.

### Red Number {#red-number}

![Red Number avec texte HTML préliminaire et couleurs personnalisées](/images/grafik-visual-studio/red-number.png)

*Exemple d'affichage agrandi avec une valeur de prévisualisation locale de 125 ; la taille par défaut des nouveaux widgets est de 52 × 30 px.*

Les nouveaux widgets sont créés avec une taille de 52 × 30 px. La section **Général** permet de définir l'entité HA (Home Assistant) ; le paramètre **type** (cercle/épingle) est disponible, ainsi que trois champs HTML dotés d'un éditeur de code. Il est possible de configurer l'arrière-plan ; pour le type « cercle », on peut également définir la couleur de la bordure et le rayon des angles (0–100, valeur par défaut : 16). Le cercle utilise une bordure de 3 px, tandis que le type « épingle » affiche une forme de repère sans bordure circulaire. Les couleurs sont sélectionnées via un sélecteur hexadécimal ; les couleurs au format RGB(A) existantes restent prises en charge.

Le champ **HTML avant** permet d'ajouter du contenu HTML avant le nombre. Si la valeur est exactement égale à 1, le contenu défini dans **HTML après (singulier)** est affiché ; dans tous les autres cas, c'est le contenu de **HTML après (pluriel)** qui est utilisé. La valeur numérique est extraite de l'état de l'entité. En phase d'exécution, l'affichage est masqué si la valeur est 0, `false` ou si aucune valeur numérique valide n'est disponible. Dans l'éditeur, l'élément reste visible ; en l'absence de source, la mention `--` s'affiche. Les textes HTML longs nécessitent une surface de widget plus importante.

Le widget fonctionne uniquement en lecture et ne nécessite aucun « assistant » (helper) HA supplémentaire. Le point de départ existant demeure utilisable comme source de données, même si l'affichage du zéro est masqué. Le groupe **CSS Général** reste actif, tandis que les autres groupes CSS sont désactivés par défaut. Une note explicative (optionnelle) justifie le masquage de l'affichage.

### Forme SVG {#svg-shape}

![Forme SVG avec cercle et curseurs de mise à l'échelle distincts](/images/grafik-visual-studio/svg-shape.png)

La forme est générée directement au format SVG ; aucun fichier image, entité HA ou assistant supplémentaire n'est requis. Par défaut, les nouveaux widgets mesurent **100 × 100 px**. Dans la section **Général**, vous pouvez choisir parmi les formes suivantes : ligne, triangle, carré, pentagone, hexagone, octogone, cercle, étoile, flèche ou polygone personnalisé. Pour le polygone personnalisé, un paramètre **Nombre de points** (de 3 à 20) est disponible ; il permet de créer un polygone régulier (il n'est pas possible de saisir des coordonnées arbitraires).

La **couleur du trait** et la **couleur de remplissage** sont définies au format HEX. L'**épaisseur du trait** peut varier de 0 à 100 (valeur par défaut : 5), et la **rotation** de 0 à 360 degrés. L'**échelle en largeur** et l'**échelle en hauteur** sont réglables indépendamment, de 0 à 1 par incréments de 0,05. La rotation et la mise à l'échelle s'effectuent par rapport au centre de la forme ; dans le cas d'une ligne — conformément au modèle VIS2 — seule la rotation s'applique, l'épaisseur du trait restant fixe lors d'un agrandissement.

L'étoile utilise des arêtes qui se croisent ; la flèche pointe vers le haut sans aucune rotation. L'épaisseur du trait réduit le rayon disponible du cercle et des polygones. Des traits très épais peuvent remplir entièrement les petites formes ; les rayons négatifs sont évités. La section **CSS Général** reste active pour la position et la taille ; tous les autres groupes CSS sont désactivés par défaut pour les nouveaux widgets. L'éditeur et l'environnement d'exécution (runtime) affichent la même géométrie.

### Image {#image}

La section **Général** comprend la source, les options d'étirement, la durée de mise à jour (ms), la mise à jour lors du réveil, la mise à jour lors du changement de vue, l'option « Ne rien ajouter à l'URL » et `allowUserInteractions`. La section **CSS Général** reste active ; les autres groupes CSS sont désactivés par défaut.

- Sans l'option **Étirement**, l'image occupe toute la largeur du widget tout en conservant son rapport hauteur/largeur d'origine. La partie qui dépasse en hauteur est tronquée. Avec l'option **Étirement**, l'image remplit toute la largeur et la hauteur, même si cela modifie son rapport hauteur/largeur.
- Une **durée de mise à jour de 0** désactive le rechargement périodique. Par exemple, `51800` effectue une mise à jour toutes les 51,8 secondes. Les images inchangées ne sont pas rechargées lors d'autres changements d'état ; les minuteurs en cours conservent leur cadence. Les images invisibles ne sont pas mises à jour périodiquement.
- Les options **Mise à jour lors du réveil / changement de vue** déclenchent un rechargement lors de la réactivation de la page du navigateur ou lors de l'ouverture de la page du projet. L'option **Ne rien ajouter à l'URL** conserve l'URL telle quelle, ce qui permet au navigateur d'utiliser son cache. Si cette option n'est pas cochée, Studio ajoute un horodatage tout en préservant les paramètres d'URL et les ancres existants.
- **allowUserInteractions** autorise les actions habituelles du navigateur, telles que le glisser-déposer ou l'accès au menu contextuel de l'image dans l'environnement d'exécution. Si l'option n'est pas cochée, les actions du pointeur sont transmises à l'élément situé en dessous. Dans l'éditeur, le widget reste sélectionnable et déplaçable.

Sélectionnez une image via le sélecteur de fichiers du Studio ou via une URL. Les chemins VIS2, tels que `_PRJ_NAME/001_cheerful.png`, doivent être remplacés par le chemin de fichier correspondant dans le Studio. Aucun « helper » (assistant) HA n'est requis. Les projets existants utilisant une entité de type URL continueront d'être lus ; cela n'entraîne pas la connexion à une API de caméra HA. Les petits indicateurs rouges destinés aux utilisateurs en transition peuvent être activés ou désactivés via un paramètre central.

![Comparaison entre une image étirée et une image affichée proportionnellement](/images/grafik-visual-studio/image.png)

Référence fonctionnelle : [Image VIS2](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicImage.tsx).

### Image 8 {#image-8}

L'entité HA fournit l'index de l'image ; `false`/`off` correspond à 0, tandis que `true`/`on` correspond à 1. En l'absence d'entité ou si l'état est manquant, c'est l'**Image [0]** qui est utilisée. L'entité est lue uniquement (lecture seule), tant dans l'éditeur qu'en phase d'exécution ; aucun « helper » (assistant) HA supplémentaire n'est nécessaire.

Le paramètre **Nombre de valeurs jusqu'à** indique l'index maximal et est limité à **200** : 0 correspond à une entrée, tandis que 200 correspond à **201 entrées, de l'image [0] à l'image [200]**. Chaque groupe d'images dispose d'une source avec sélection de fichier et peut être copié, supprimé, déplacé ou désactivé. La dernière entrée est conservée ; à l'index 200, la fonction de copie est désactivée. Les index vides, désactivés ou invalides n'affichent aucune image ; les sources existantes ne sont pas renumérotées automatiquement. En cas de réduction de la limite, les sources masquées sont conservées jusqu'à ce qu'elles soient explicitement supprimées.

Les nouveaux widgets ont une taille de **200 × 130 px**. Les paramètres relatifs à l'étirement, au délai de mise à jour, au réveil, au changement de vue, à l'URL inchangée et aux actions de navigation standard fonctionnent de la même manière que pour le widget **Image**. Une image inchangée n'est pas rechargée lors d'autres changements d'état ; les minuteurs de rafraîchissement en cours conservent leur cadence. Le paramètre **CSS général** reste actif, tandis que les autres groupes CSS sont désactivés par défaut. Les petits indicateurs rouges de transition peuvent être activés ou désactivés de manière centralisée.

![Image 8 avec un index maximal de 200 et des paramètres de rafraîchissement](/images/grafik-visual-studio/image8.png)

Référence fonctionnelle : [VIS2 Image 8](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicImage8.tsx).

### iFrame {#iframe}

![iFrame avec site web UGSo intégré et options de mise à jour](/images/grafik-visual-studio/iframe.png)

Les nouveaux widgets ont une taille de **600 × 320 px**. Sous **Général**, on trouve : Source, Temps de mise à jour (ms), Pas de « bac à sable » (sandbox), Mise à jour au réveil, Mise à jour au changement de vue, Ne rien ajouter à l'URL, Défilement X/Y et Pas de bordure. **CSS Général** reste actif ; les autres groupes CSS sont désactivés par défaut. Dans l'éditeur, le widget peut être sélectionné et déplacé sans que la page intégrée ne capte les interactions à la souris.

Un **Temps de mise à jour** de 0 désactive le rechargement périodique. Des valeurs allant jusqu'à 180 000 ms définissent un intervalle de mise à jour. L'option **Mise à jour au réveil** déclenche un rechargement lors du retour à la fenêtre du navigateur ; **Mise à jour au changement de vue** s'applique lors de l'affichage de la page dans Studio. La modification d'autres paramètres du widget n'entraîne pas le rechargement du contenu intégré. Si l'option **Ne rien ajouter à l'URL** n'est pas cochée, une mise à jour ajoute le paramètre d'horodatage `_gvs` ; les paramètres d'URL et les ancres existants sont conservés. Si l'option est cochée, l'URL est rechargée telle quelle.

Par défaut, un « bac à sable » (sandbox) limite la page intégrée aux scripts et aux formulaires. L'option **Pas de « bac à sable »** supprime cette restriction. Les procédures de connexion, les cookies et les règles d'intégration propres à la page cible restent en vigueur ; une page peut également refuser son intégration via des politiques de navigateur. Les paramètres **Défilement X/Y** définissent les options de débordement souhaitées ; la présence effective de barres de défilement dépend toutefois du navigateur et du contenu de la page cible. Dans le cas de domaines tiers, Studio ne peut pas forcer leurs axes de défilement internes. L'option **Pas de bordure** supprime la bordure de l'iFrame.

Aucun état HA n'est écrit et aucun « helper » (assistant) HA n'est requis. Les notes facultatives destinées aux utilisateurs en transition expliquent les concepts de « sandbox » (bac à sable) et de mise à jour. Un iFrame conserve un lien vers sa source, même après une exportation ; le site externe n'est pas intégré sous forme de copie locale.

### iFrame 8 {#iframe-8}

![iFrame 8 avec URL et sandbox pour chaque entrée](/images/grafik-visual-studio/iframe8.png)

*Exemple dans l'éditeur avec une URL SVG locale pour le frame [0].*

La variante dépendante de l'état utilise l'entité HA comme index pour l'URL. `false`/`off` sélectionnent le frame [0], tandis que `true`/`on` sélectionnent le frame [1] ; les valeurs numériques permettent de choisir l'entrée correspondante. En l'absence d'entité, les nouveaux widgets démarrent sur le frame [0]. Les index invalides, négatifs ou trop élevés, ainsi que les entrées vides ou désactivées, n'affichent aucun frame. L'entité est uniquement lue ; aucun « helper » HA supplémentaire n'est nécessaire.

Le paramètre **Nombre de valeurs jusqu'à** correspond à l'index maximal, et non au nombre total d'éléments : la valeur par défaut 2 donne les index [0], [1] et [2] ; le maximum de 20 donne **21 entrées, de [0] à [20]**. Les groupes **frames [n]** contiennent les options **URL si valeur [n]** et **Pas de sandbox [n]**. Ces éléments peuvent être activés/désactivés, copiés, supprimés ou réorganisés. Si l'on réduit le nombre maximal, les entrées masquées sont conservées. Les numéros correspondent directement à la valeur de l'entité ; toute réorganisation modifie cette association.

La taille par défaut est de **600 × 320 px**. L'intervalle de mise à jour, le réveil, le changement de vue, l'URL inchangée, le défilement (Scroll) X/Y et la bordure fonctionnent comme pour un **iFrame**. La « Sandbox » (bac à sable) est définie pour chaque entrée. Si l'URL et la « Sandbox » restent identiques, l'élément n'est pas rechargé lors de modifications apportées à d'autres widgets. En revanche, si l'URL ou la « Sandbox » change, l'élément intégré est remplacé. La section **CSS Général** reste active, tandis que les autres groupes CSS sont désactivés par défaut. Des conseils optionnels destinés aux utilisateurs effectuant une migration expliquent les concepts d'index, de « Sandbox » et de mise à jour.

### Note {#note}

La section **Général** comprend les paramètres suivants : entité Home Assistant, attribut HA, ajout de HTML avant ou après le contenu, texte de test et masquage des coins. Le champ d'attribut supplémentaire remplace les points de données d'attribut ioBroker : pour `friendly_name`, sélectionnez l'entité HA correspondante et saisissez `friendly_name`. Si le champ d'attribut est laissé vide, c'est l'état (state) qui est lu.

Si le champ **Texte de test** n'est pas vide, il remplace la valeur de l'entité dans l'éditeur. Lors de l'exécution (runtime), seule la valeur de l'entité ou de l'attribut est affichée ; si cette valeur est absente, la zone de texte centrale reste vide. Les éléments ajoutés avant ou après le contenu restent visibles. Comme dans le code source de la note VIS2, les champs désignés comme « HTML » sont affichés sous forme de texte brut ; par exemple, `<b>` n'y générera pas de mise en forme en gras. Les sauts de ligne sont conservés.

L'option **Masquer le coin** agit uniquement sur le coin inférieur droit et ne constitue pas une protection en écriture. Si elle n'est pas cochée, la couleur de la bordure est affichée. Les nouvelles notes ont une taille de **100 × 70 px**, avec un rayon de coin de 5 px, une bordure grise de 1 px et un fond jaune `#FFFF69CC`. La taille et les couleurs restent personnalisables via CSS ; le groupe **CSS Général** est actif par défaut, tandis que les autres groupes CSS sont désactivés au démarrage.

Un clic en mode exécution (runtime) ouvre la boîte de dialogue de la note. Un « helper » (assistant) de type **input_text sans sélection d'attribut** permet de modifier, d'effacer et d'enregistrer le contenu ; la longueur maximale du texte est respectée. Seul le texte de la note est écrit, sans ajout de préfixe ni de suffixe. Les capteurs et les attributs restent lisibles, mais ne peuvent pas servir de cible d'écriture. En l'absence de cible d'écriture appropriée, le champ de texte dans la boîte de dialogue est en lecture seule et l'option d'enregistrement est désactivée. Les boutons « Annuler » ou la touche « Échap » ferment la boîte de dialogue sans enregistrer les modifications. Les petits indicateurs rouges peuvent être activés ou désactivés via l'option **Afficher les conseils pour les utilisateurs en transition**.

![Note avec un texte de test, illustrant la différence entre un coin masqué et un coin visible](/images/grafik-visual-studio/note.png)

Référence fonctionnelle : [Note VIS2](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicNote.tsx).

### Ligne horizontale / Ligne verticale {#horizontal-line-vertical-line}

Ces deux lignes de séparation servent uniquement à l'affichage et ne nécessitent aucun « helper » HA (Home Assistant). La ligne horizontale démarre avec des dimensions de **200 × 16 px**, et la ligne verticale avec **16 × 200 px**. Pour la **ligne de séparation CSS**, les paramètres suivants sont disponibles : épaisseur (1–100 px, valeur par défaut : 2), couleur HEX, couleur de bordure, largeur de bordure et forme des extrémités : **carrée** (par défaut), **arrondie** ou **pointue (en forme de flèche)** aux deux extrémités. Une augmentation de l'épaisseur accroît, si nécessaire, la dimension transversale du widget ; lors d'une réduction ultérieure, la surface du widget limite l'épaisseur visible.

À partir de la version **0.1.183**, les lignes de séparation ne disposent plus de **points d'ancrage** ni de **flux de données**. L'option **Activer la fonction d'accrochage** (sous « Ligne de séparation CSS ») permet d'activer l'alignement géométrique ; cette fonction est désactivée par défaut pour les nouvelles lignes. Les paramètres d'accrochage déjà activés sont conservés. Lors du déplacement individuel, du redimensionnement d'une extrémité ou de la modification de la géométrie, les extrémités se positionnent sur le centre d'une ligne de séparation orthogonale si elles se trouvent à moins de **8 pixels** de celle-ci. Cela fonctionne en tout point le long de l'autre ligne, y compris pour les jonctions en « T ». Les lignes parallèles ne s'accrochent pas entre elles. Le déplacement simultané de plusieurs widgets ne modifie pas leurs distances relatives. La définition manuelle de positions/tailles CSS ou l'application de transformations CSS désactivent la fonction d'accrochage.

Les coordonnées réelles et la configuration des lignes sont enregistrées, y compris lors de l'exportation de widgets ou de projets. La connexion n'est pas un lien permanent : si une ligne est déplacée ultérieurement, l'autre ne suit pas automatiquement. Les paramètres **CSS Général** et **CSS Ligne de séparation** restent actifs lors de l'enregistrement. L'indication facultative de correspondance (transfert) suit le paramètre central **Afficher les indications de correspondance**.

![Lignes de séparation avec jonction en T, extrémités en forme de flèche et paramètres CSS](/images/grafik-visual-studio/separator-lines.png)

![Fonction d'accrochage activée sans points d'ancrage ni flux de données dans l'éditeur de lignes de séparation](/images/grafik-visual-studio/separator-snap.png)

*La fonction d'accrochage permet une connexion en n'importe quel point de l'autre ligne de séparation. Les anciens paramètres d'ancrage et de flux de données sont supprimés lors du chargement et de l'enregistrement.*

### Bordure (Border) {#border}

L'élément « Bordure » (Border) dessine un cadre doté d'un titre et d'une zone d'en-tête facultative. Les nouveaux widgets ont une taille de **100 × 70 px**, avec une bordure grise (`#888888`) de 1 px et un débordement (overflow) visible. La section **Général** comprend six champs standard : titre, arrière-plan du titre, espacement supérieur du titre, espacement gauche du titre, hauteur de l'en-tête et couleur de l'en-tête. Les couleurs sont définies au format hexadécimal (HEX).

La position du titre est absolue par rapport au cadre : par défaut, **-10 px par rapport au haut et 20 px par rapport à la gauche**, sans décalage vertical supplémentaire. Le titre peut contenir des balises HTML simples (ex. : `<b>Titel</b>`) ; les scripts, les gestionnaires d'événements (event handlers) et les éléments intégrés actifs sont supprimés. La police et la bordure peuvent être configurées via les groupes CSS correspondants.

**Hauteur de l'en-tête : 0** masque la zone d'en-tête. En l'absence d'arrière-plan spécifique pour le titre, celui-ci s'affiche sur un fond noir (thème sombre) ou blanc (thème clair). Si la zone d'en-tête est visible, l'arrière-plan du titre reste transparent s'il n'a pas de couleur définie ; une couleur d'en-tête vide utilise également le noir ou le blanc, selon le thème. Dans l'exemple de gauche, seul l'arrière-plan du titre est défini ; à droite, une zone d'en-tête de 30 px de hauteur est ajoutée.

La bordure et le titre ne nécessitent ni entité Home Assistant ni « helper » (assistant). La section **CSS Général** reste active pour gérer la position et la taille ; les autres groupes CSS sont désactivés par défaut. Des petits indicateurs rouges (optionnels) peuvent être activés ou désactivés de manière centralisée.

![Bordure avec position du titre et zone d'en-tête optionnelle](/images/grafik-visual-studio/border.png)

Référence fonctionnelle : [VIS2 Border](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicFrame.tsx).

### Case à cocher booléenne (Bool Checkbox) {#bool-checkbox}

La case à cocher reflète l'état de l'entité Home Assistant associée. En mode exécution (runtime), elle permet de basculer les états `switch`, `light` et `input_boolean` ; si aucune entité appropriée n'est disponible, elle est verrouillée. Dans l'éditeur, elle sert uniquement de prévisualisation.

Les options **Prepend HTML** (HTML en préfixe) et **Append HTML** (HTML en suffixe) permettent d'ajouter du texte ou du code HTML à la case à cocher. L'option **Autofocus** ne s'applique qu'au moment de l'exécution. Les nouveaux widgets présentent des champs HTML vides, l'option « Autofocus » désactivée, et seule l'option « General CSS » activée. Les paramètres existants demeurent inchangés.

### Bool HTML {#bool-html}

![Bool HTML avec éditeurs pour « true » (vrai) et « false » (faux)](/images/grafik-visual-studio/bool-html.png)

*Aperçu d'un test précédent des quatre champs HTML. L'option « General CSS » demeure obligatoire.*

À partir de la version **0.1.146**, les options **Prepend HTML**, **Append HTML**, **HTML for 'false'** (HTML pour « faux ») et **HTML for 'true'** (HTML pour « vrai ») sont disponibles, chacune disposant de son propre éditeur HTML. Le contenu affiché est déterminé par l'état de l'entité ; en l'absence d'entité, le paramètre **Test State** (état de test) sert d'aperçu. Une valeur booléenne `true`, une valeur numérique `1`, ou les valeurs textuelles `true`, `on`, `ein`, `yes` et `1` déclencheront l'affichage du contenu correspondant à « true », tandis que tout autre état déclenchera le contenu correspondant à « false ». Le code HTML ajouté en préfixe ou en suffixe est affiché quel que soit l'état. Le processus de nettoyage (sanitization) HTML du Studio s'applique à ces quatre champs.

Les nouveaux widgets présentent des champs HTML vides, avec seule l'option « General CSS » activée. Le contenu configuré précédemment demeure inchangé. Le composant **Bool HTML** est destiné uniquement à l'affichage et ne permet pas de modifier l'état d'une entité ; pour cette fonctionnalité, utilisez **Bool HTML (control)**.

### ValueList HTML {#valuelist-html}

À partir de **0.1.144**, le paramètre **Valeur de test (éditeur uniquement)** vous permet de sélectionner un index parmi les entrées disponibles dans la liste. **Valeur réelle / État de prévisualisation** affiche l'état standard du widget, même au sein de l'éditeur. Une valeur de test ne modifie pas l'état de prévisualisation enregistré ni la valeur domotique (HA) ; l'environnement d'exécution utilise toujours l'état de l'entité liée ou, en l'absence de liaison, l'état de prévisualisation.

Séparez les entrées par des points-virgules ou des sauts de ligne : `Test;test2;test3` génère les index 0, 1 et 2. Les virgules sont considérées comme faisant partie du texte ; par exemple, `Test, test2, test3` constitue une entrée unique. Pour inclure un point-virgule dans une entrée HTML — par exemple dans un style CSS ou une entité HTML — utilisez `§§`. Les options **Ajouter du HTML au début** et **Ajouter du HTML à la fin** encadrent l'entrée sélectionnée ; le code HTML est assaini (nettoyé) conformément aux règles établies par Studio. Si un état est absent, invalide ou situé en dehors de la plage définie, aucune entrée de la liste ne sera affichée. Pour les nouveaux widgets ValueList HTML, seul le « CSS général » est activé par défaut ; les configurations existantes demeurent inchangées.

### Style ValueList HTML {#valuelist-html-style}

À partir de **0.1.145**, le widget propose des sections individuelles — de **Valeur [0]** à **Valeur [n]** — contenant chacune un contenu HTML et le style CSS associé. Le paramètre **Nombre de valeurs (maximum)** définit l'index maximal : `2` génère trois entrées, tandis que `0` n'en génère qu'une seule. Studio prend en charge un index maximal de 50. Les champs de liste existants, issus d'anciens projets, continueront de fonctionner en tant que solution de repli.

**Valeur de test (éditeur uniquement)** : sélectionne une entrée exclusivement pour la prévisualisation. L'environnement d'exécution (runtime) lit l'index à partir de l'entité liée ou de l'état de prévisualisation non lié ; `true` et `false` correspondent respectivement à 1 et 0. L'index ne définit pas une plage de valeurs : pour les entrées `10`, `20` et `30`, l'état `2` affiche le texte `30` ; l'état `30`, quant à lui, se situe au-delà de la liste (limitée à l'index 2) et n'affiche aucune entrée.

Le style s'applique également au code HTML ajouté avant ou après le contenu. Utilisez des déclarations CSS complètes, par exemple `font-weight: bold; color: #29c8b5; font-size: 20px;`. L'utilisation de `bold` seul est sans effet. Studio prend en charge les styles d'affichage prédéfinis sans nécessiter d'URL CSS externes. Pour les nouveaux widgets, seul le style « CSS général » est activé par défaut ; les styles spécifiques à chaque valeur restent toutefois utilisables indépendamment.

### Affichage dans le widget 8 {#view-in-widget-8}

À partir de **0.1.160**, ce widget intègre une **page de projet Studio** en fonction de l'état d'une entité HA (Home Assistant). Il s'agit d'un mode en lecture seule ; aucun « assistant » (helper) HA supplémentaire n'est requis. Les pages sélectionnables sont assignées sous **Page [0]**, **Page [1]**, etc. Le paramètre **Nombre de valeurs jusqu'à** correspond à l'index maximal : `1` génère deux entrées, tandis que `0` en génère exactement une ; Le Studio autorise un index maximal de 50.

`false`/`off` sélectionne l'index 0, `true`/`on` l'index 1. Les états de type entier sélectionnent l'index correspondant. Les valeurs vides, indisponibles, non entières ou situées en dehors de la liste ne sélectionnent aucune page. En l'absence d'entité, l'index 0 est appliqué par défaut aux nouveaux widgets. L'éditeur affiche la page sélectionnée sous forme d'aperçu textuel ; le runtime, quant à lui, l'intègre. Une cible inchangée n'est pas rechargée lors des mises à jour d'état. Les pages manquantes ainsi que les intégrations récursives sont empêchées.

Les nouveaux widgets démarrent avec des dimensions de **300 × 200 pixels** et seul le **CSS général** activé. Des indications destinées aux utilisateurs (désactivables de manière centralisée) expliquent le fonctionnement des index et la dépendance aux pages. L'exportation JSON du widget n'inclut pas les pages du projet référencées ; pour une exportation complète du projet, toutes les pages nécessaires doivent être jointes. Il convient de distinguer ce widget de la fonction « Dashboard in widget », qui permet d'ouvrir un tableau de bord HA (Home Assistant).

## Graphique HA – Interactif (11) {#ha-grafik-–-interaktiv-11}


| Widget | Fonctionnalité actuelle |
| --- | --- |
| Universal Element — Élément universel | État par défaut et jusqu'à 20 états conditionnels ; icône, image, texte ou HTML. Commutation, bouton-poussoir, affichage et navigation via des touches uniques ou séparées. |
| Calendar — Calendrier | Vue mensuelle avec sélection de date, marquage du jour actuel, blocage de jours et affichage des semaines calendaires. |
| Terminkalender — Agenda | Affichage des rendez-vous par mois, semaine, jour, année ou sous forme de liste ; sources multiples et règles de coloration. |
| Checkbox — Case à cocher | Valeurs « faux/vrai » personnalisées, textes d'état, quatre positions pour le texte et personnalisation de l'apparence de la case. |
| Schieberegler — Curseur | Curseur numérique horizontal ou vertical avec affichage de la valeur, repères de pas, et styles distincts pour la piste et le curseur (poignée). |
| Tabelle — Tableau | Tableau au format JSON avec gestion des formats de colonne, formules, tri, filtrage, pagination et coloration des lignes. |
| Lauftext — Texte défilant | Texte statique ou état HA (Home Assistant) affiché en défilement continu ; paramètres de direction, vitesse et pause au survol. |
| Werteliste — Liste de valeurs | Répartition d'un texte en entrées de liste distinctes ; choix parmi huit types de puces, numérotation, caractères personnalisés et espacements. |
| Schalten — Commutateur | Valeurs « faux/vrai » et textes d'état personnalisés ; styles distincts pour la piste et le curseur, avec possibilité d'héritage des styles. |
| Radialer Schieberegler — Curseur radial | Curseur numérique défini par des angles de début et de fin, incluant la valeur et une étiquette, avec styles personnalisés pour la piste et le curseur. |
| Dropdown — Menu déroulant | Options issues de HA ou personnalisées, avec titre, arrière-plan conditionnel et gestion séparée des ombres pour le menu et le widget. |

### Dropdown {#dropdown}

À partir de **0.1.182**, le composant **Dropdown** (menu déroulant), situé sous la rubrique **Interactif**, propose une sélection d'options avec un titre facultatif ; ses dimensions par défaut sont de **300 × 50 px**. Pour les variantes `select` et `input_select`, les options sont issues de l'attribut `options`. L'option **Utiliser des options personnalisées** permet de définir jusqu'à **200 paires valeur/texte** ; les valeurs en double ne sont affichées qu'une seule fois. Les deux cases à cocher d'affichage permettent de choisir entre la valeur, le texte ou une combinaison des deux ; les textes identiques ne sont pas répétés. Si aucune case n'est cochée, la valeur reste visible afin de garantir une sélection sans ambiguïté.

- **Écriture :** `select`/`input_select` utilisent exclusivement les options actuellement autorisées. Les valeurs numériques personnalisées s'écrivent dans `input_number`, et les textes (jusqu'à 255 caractères) dans `input_text`. Les options non valides sont bloquées. L'accès en écriture est désactivé pour les capteurs, les états manquants, les éléments protégés en écriture et au sein de l'éditeur ; en l'absence d'entité, une sélection locale reste possible.
- **Conditions de couleur d'arrière-plan :** jusqu'à **20 règles**, utilisant six opérateurs de comparaison. La première règle correspondant à la situation est appliquée. Si aucune entité d'arrière-plan spécifique n'est définie, la valeur sélectionnée est prise en compte ; dans le cas contraire, c'est l'état de cette entité qui est utilisé. Les états inconnus ou indisponibles ne déclenchent aucune règle de couleur.
- **CSS du menu déroulant :** permet de configurer la taille de la police, les couleurs (texte, arrière-plan, surbrillance, bordure), l'épaisseur et le rayon de la bordure, ainsi que la taille et la couleur du titre (avec quatre paramètres d'espacement). Le titre peut adopter la couleur définie par la condition active. L'**ombre du menu déroulant** s'applique à la sélection et au menu ouvert, tandis que l'**ombre du widget** englobe l'ensemble de l'élément, titre inclus. Ces deux options permettent de régler le décalage (X/Y), le flou, l'extension et la couleur.
- **Depuis un autre widget :** permet de reprendre l'apparence d'un autre menu déroulant, y compris le style du titre et les ombres. Le texte du titre, la liste des options, l'entité associée et les règles restent locaux. Les copies partagées conservent les références de style appropriées ; les cycles de référence sont détectés et bloqués.
- **Utilisation :** un clic ou l'utilisation des touches fléchées ouvre le menu. La navigation dans la liste s'effectue via les touches fléchées, « Début »/« Fin », « Entrée »/« Espace » et « Échap » ; la touche « Tab » permet de quitter le menu. Les entrées longues sont automatiquement renvoyées à la ligne, et les listes volumineuses peuvent être parcourues par défilement. En cas de protection en écriture, la valeur s'affiche sans la flèche de sélection.

L'ensemble des paramètres, options personnalisées, règles et références sont conservés lors de l'exportation de projets, de widgets ou de paquets. La liste des options constitue un menu spécifique au Studio, garantissant une cohérence visuelle des couleurs et des ombres.

![Menus déroulants avec arrière-plan conditionnel, protection en écriture, menu ouvert et style appliqué](/images/grafik-visual-studio/dropdown.png)

Référence des fonctionnalités : [Menu déroulant « inventwo » pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/dropdown-widget.md). L'intégration avec Home Assistant (HA) ainsi que l'affichage ont été développés de manière autonome.

### Curseur radial {#radialer-schieberegler}

À partir de la version **0.1.181**, le **curseur radial** est disponible dans la section **Interactif**. Les nouveaux widgets sont créés par défaut avec des dimensions de **200 × 200 px**, une plage de **0 à 100**, un pas de **1**, un angle de départ de **225°** et un angle de fin de **135°**. L'angle **0° se situe en haut** ; l'arc progresse dans le sens des aiguilles d'une montre, couvrant par défaut **270°**. Des angles identiques forment un cercle complet ; une plage de **270° à 90°** forme un demi-cercle supérieur.

- **Général :** Entité HA, minimum, maximum, pas, angles de début/fin, affichage de la valeur, affichage de l'étiquette, étiquette et protection en écriture. En l'absence d'entité, la valeur de prévisualisation sert de valeur initiale.
- **Curseur radial CSS – Piste :** Couleur de la piste, couleur active, largeur (**1–50 px**), ainsi que couleur de l'ombre, décalage X/Y et flou.
- **Curseur radial CSS – Curseur (poignée) :** Couleur, taille (**1–50 px**) et ombre personnalisée.
- **Curseur radial CSS – Valeur :** Taille de la valeur (**8–100 px**), couleur de la valeur, taille de l'étiquette (**8–50 px**) et couleur de l'étiquette. Les chiffres sont réduits en cas de manque d'espace ; les étiquettes longues sont tronquées. Le texte intégral est conservé en tant que nom accessible du curseur.
- **Depuis le widget :** La piste et le curseur peuvent être repris depuis un autre curseur radial. L'affichage de la valeur, l'étiquette et la plage de valeurs restent locaux. Les cycles sont détectés et gérés ; les copies partagées reçoivent de nouvelles références appropriées.
- **Utilisation :** Le glisser-déposer ou les touches fléchées modifient la valeur par un pas ; les touches Page précédente/suivante (Page Up/Down) effectuent un saut de dix pas ; les touches Début/Fin (Home/End) sélectionnent le minimum/maximum. Un clic dans l'espace vide de l'arc sélectionne la valeur limite la plus proche. Si une opération de glisser-déposer est annulée, la valeur initiale est rétablie et aucune donnée n'est écrite.
- **HA :** Seuls les « helpers » (assistants) `input_number` disponibles sont mis à jour, au moment du relâchement (fin du glisser) ou de l'appui sur une touche. Les limites et le pas doivent correspondre à ceux du « helper ». Les capteurs et la protection en écriture permettent uniquement l'affichage ; les valeurs manquantes sont représentées par un tiret. En l'absence d'entité, les modifications restent locales. Aucune donnée n'est écrite dans l'éditeur.

Tous les paramètres et références de style sont conservés lors de l'exportation de projets, de widgets ou de paquets.

![Curseur radial avec arc standard, valeur décimale, demi-cercle et cercle complet en lecture seule](/images/grafik-visual-studio/radial-slider.png)

Référence fonctionnelle : [Curseur radial inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/radial-slider-widget.md). Studio utilise sa propre implémentation.


### Commutation {#schalten}

À partir de la version **0.1.180**, la fonction **Commutation** (sous la catégorie **Interactivité**) vient compléter le composant **Switch** (interrupteur) de base existant. Les nouveaux widgets sont créés avec des dimensions de **70 × 40 px**, une position de texte définie sur **Fin**, une épaisseur de piste de **12 px** et un curseur (poignée) de **16 px**. Si les champs **Valeur false/true** sont laissés vides, des valeurs booléennes sont utilisées ; il est toutefois possible de définir des paires de valeurs personnalisées (nombres ou textes). Le **Texte faux/vrai** s'affiche à droite, à gauche, en haut ou en bas selon l'état actuel, et demeure du texte brut.

- **Commutation CSS – Piste :** couleurs distinctes pour les états *false* (faux) et *true* (vrai), largeur de piste de **1 à 50 px**, arrondi de **1 à 100 %**, ainsi que décalage X/Y, flou, extension et couleurs d'ombre spécifiques à chaque état.
- **Commutation CSS – Curseur (bouton) :** couleurs distinctes pour les états *false* et *true*, taille de **1 à 50 px**, arrondi de **1 à 100 %** et paramètres d'ombre personnalisés. Une valeur de 100 % donne une forme ronde.
- **Depuis un widget :** permet de reprendre la configuration de la piste et du curseur depuis un autre widget de commutation, indépendamment de celui-ci. La liaison des valeurs et les textes restent locaux ; les références cycliques sont gérées en toute sécurité. Lors d'une copie groupée, les références sont automatiquement réassignées aux widgets copiés.
- **Utilisation :** clic sur l'interrupteur ou le texte, ou utilisation de la barre d'espace. L'environnement d'exécution (runtime) écrit les valeurs appropriées dans les entités disponibles : `switch`, `light`, `input_boolean`, `input_number` ou `input_text`. Les capteurs, les paires de valeurs incompatibles, les états manquants ainsi que l'éditeur ne permettent pas l'écriture. En l'absence d'entité, la commutation reste possible localement.

La police et la couleur du texte sont définies via les groupes CSS habituels. Toutes les valeurs, les textes associés aux états, les paramètres de style et les références sont conservés au sein du projet ainsi que lors de l'exportation de widgets ou de paquets.

![Commutation avec quatre positions de texte, reprise indépendante de la piste et affichage du capteur désactivé](/images/grafik-visual-studio/styled-switch.png)

Référence des fonctionnalités : [inventwo Switch pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/switch-widget.md). Le Studio utilise une implémentation spécifique.

### Liste de valeurs {#werteliste}

À partir de la version **0.1.179**, le widget **Liste de valeurs** (Werteliste) vient enrichir la catégorie **Interactif**, complétant ainsi les widgets de base existants : **ValueList Text/HTML/HTML Style**. Les nouveaux widgets sont créés avec une taille par défaut de **200 × 150 px**. Ils utilisent la virgule comme séparateur, suppriment automatiquement les espaces extérieurs et ignorent les entrées vides. Si une entité HA (Home Assistant) est associée, l'état de celle-ci est utilisé ; dans le cas contraire, vous pouvez saisir du **Texte (manuel)**. La liste fonctionne en mode lecture seule et affiche le texte tel quel.

- **Séparateur :** Un caractère ou une chaîne de caractères ; utilisez `\\n` pour les sauts de ligne et `\\t` pour les tabulations. Si aucun séparateur n'est défini, le texte entier est considéré comme une entrée unique. Les sauts de ligne au format Windows sont pris en charge.
- **Suppression des espaces** et **Ignorer les entrées vides** : ces options fonctionnent indépendamment l'une de l'autre. Si le filtrage est désactivé, les lignes vides restent visibles ; la numérotation suit alors les entrées affichées.
- **Affichage :** Point, cercle, carré, tiret, flèche, numérotation, aucun symbole, ou un symbole/émoji personnalisé. La couleur du symbole est indépendante de celle du texte. Si aucun symbole n'est sélectionné, les paramètres de couleur et d'espacement du symbole disparaissent ; le champ dédié au symbole personnalisé n'apparaît que lorsque cette option est choisie.
- **Espacements :** Entre le symbole et le texte : **0–50 px** (par défaut : **8**) ; entre les lignes : **0–50 px** (par défaut : **4**) ; marge intérieure (padding) : **0–200 px** (par défaut : **4**). Les entrées longues passent automatiquement à la ligne ; les listes volumineuses peuvent être parcourues par défilement (scroll) à l'intérieur du widget.

La police, la couleur du texte et l'arrière-plan se règlent via les groupes CSS standard. Tous les paramètres sont conservés au sein du projet ainsi que lors de l'exportation de widgets ou de paquets.

![Listes d'éléments avec puces, numérotation, caractères personnalisés et retour à la ligne](/images/grafik-visual-studio/interactive-value-list.png)

Référence des fonctionnalités : [Liste d'éléments inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/value-list-widget.md). Le Studio utilise une implémentation spécifique.

### Texte défilant {#lauftext}

À partir de la version **0.1.178**, vous trouverez le **texte défilant** dans la section **Interactif**. Les nouveaux widgets sont créés par défaut avec des dimensions de **300 × 40 px**, une direction vers la **gauche**, une vitesse de **80 px/s**, **3 copies du texte** et un espacement de **50 px**. En l'absence d'entité, le mode **« Texte défilant (statique) »** s'applique ; si une entité est définie, l'état HA (Home Assistant) est prioritaire. Le contenu reste du texte brut et ne modifie pas les valeurs dans HA.

- **Direction :** Gauche ou droite ; vitesse réglable de **10 à 500 px/s**. La vitesse reste constante, quel que soit le nombre de copies.
- **Copies du texte :** De **1 à 200** ; les textes courts sont répétés autant de fois que nécessaire pour remplir l'espace. **Espacement entre les copies** : de **0 à 1000 px**.
- **Pause au survol (Hover) :** Interrompt l'animation lorsque le curseur de la souris survole l'élément, et la reprend dès que le curseur s'en éloigne. Si le texte reste inchangé, le défilement se poursuit sans redémarrage lors des mises à jour provenant de HA.
- **Apparence :** L'arrière-plan, la police, la couleur du texte, la taille et les espacements se gèrent via les paramètres CSS habituels. Dans l'éditeur, le texte reste immobile. L'option **« Réduire les mouvements »** est activée par défaut : avec ce paramètre système, l'interface d'exécution (runtime) reste statique ; cette option peut être désactivée individuellement pour chaque widget.

Tous les paramètres sont conservés au sein du projet ainsi que lors de l'exportation de widgets ou de paquets.

![Texte défilant affichant des informations sur l'énergie et la météo, complété par des textes courts ajoutés automatiquement](/images/grafik-visual-studio/marquee.png)

Référence des fonctionnalités : [Texte défilant « inventwo » pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/marquee-widget.md). Le Studio utilise sa propre implémentation.

### Tableau {#tabelle}

À partir de la version **0.1.177**, le widget **Tableau** (sous la catégorie **Interactif**) vient compléter le widget **Table** de base existant. Les nouveaux widgets sont créés avec des dimensions de **400 × 300 px**, des colonnes générées automatiquement, un en-tête visible et sans pagination. Les données se présentent sous la forme d'une liste d'objets JSON, par exemple :

```json
[{"raum":"Küche","temperatur":25.4,"leistung":120,"aktiv":true}]
```

L'interface d'exécution (runtime) lit l'entité HA (Home Assistant) liée ou l'**attribut HA** spécifiquement sélectionné. Pour les listes plus longues, il est recommandé d'utiliser un attribut. En l'absence d'entité, ou lors de l'utilisation dans l'éditeur, ce sont les données de test JSON qui sont prises en compte. Le tableau fonctionne en mode lecture seule : les opérations de tri, de filtrage ou de changement de page n'entraînent aucune écriture de valeurs dans HA.

- **Colonnes :** Le système détecte automatiquement les clés ; il est possible de configurer jusqu'à 50 colonnes. Les options disponibles incluent : masquage, définition de clé, titre, largeur, alignement, préfixe/suffixe et espace réservé (placeholder). Formats pris en charge : texte, nombre (avec séparateurs décimaux et de milliers), booléen (affiché sous forme de case à cocher verrouillée), date/heure (avec format personnalisé), image, URL et adresse IP. Le contenu est traité comme du texte ; les images et les liens nécessitent une URL valide.
- **Formules :** Permettent d'effectuer des calculs basés sur les champs numériques de la ligne, par exemple `leistung * 2`. Les opérateurs `+ - * / % **` ainsi que l'utilisation de parenthèses sont pris en charge. Aucun code JavaScript n'est exécuté ; en cas de formule invalide, l'espace réservé est affiché. Les formats de date personnalisés prennent en charge `YYYY`, `YY`, `MM`, `M`, `DD`, `D`, `hh`, `h`, `mm`, `ss`, `sss`, `WD`, `WDL`, `KW` et `K`.
- **Tri et filtres :** Tri par défaut basé sur la clé et le sens du tri ; il est possible de définir jusqu'à 20 critères de tri par défaut avec gestion des priorités. Un clic sur les en-têtes de colonne triables permet de basculer entre les modes : croissant, décroissant ou sans tri. Les colonnes générées automatiquement sont triables ; les colonnes configurées manuellement disposent de leurs propres options de tri et de filtrage. Les filtres permettent de sélectionner les valeurs de cellule autorisées. La limite du nombre de lignes s'applique après le filtrage et le tri, mais avant la pagination. Les en-têtes de colonne peuvent être figés lors du défilement. - **Conditions de ligne :** jusqu'à 20 règles basées sur une clé ou un index de colonne (à partir de 0), avec six opérateurs de comparaison. La première règle qui correspond définit l'arrière-plan et la couleur du texte pour toute la ligne et/ou pour la colonne soumise à la condition. L'option **Mettre en évidence la ligne de total** ajoute une double ligne au-dessus de la dernière ligne de résultats ; les totaux doivent déjà être présents dans les données.
- **Tableau CSS :** groupes de paramètres **Apparence**, **Rayon des bordures**, **Bordures** et **Ombre externe**, avec gestion des couleurs HEX, hauteurs des lignes/en-têtes, marges des lignes, ainsi que la possibilité de définir des coins et des côtés de bordure distincts. L'option **Depuis le widget** permet d'appliquer chaque groupe indépendamment des autres tableaux ; les widgets copiés simultanément conservent des références cohérentes. Le paramètre **CSS général** reste actif.

L'exportation JSON du widget inclut les colonnes, les règles, les styles et les liaisons aux sources de données. Les entités HA (Home Assistant) requises, les attributs et les widgets de style référencés doivent être présents dans l'instance cible. Les données JSON enregistrées restent exploitables même en l'absence de liaison aux entités. Les petits messages d'aide destinés aux utilisateurs effectuant une migration peuvent être désactivés de manière centralisée.

![Tableau interactif avec tri, conditions de ligne, calcul de performance et pagination](/images/grafik-visual-studio/interactive-table.png)

Référence des fonctionnalités : [Tableau inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/table-widget.md). Le Studio utilise une implémentation spécifique.

### Curseur (Slider) {#schieberegler}

À partir de **0.1.176**, un **curseur** (slider) dédié est disponible dans la section **Interactif**. Le **curseur** existant, situé dans la section « Base », est conservé. Les nouveaux widgets sont créés avec des dimensions de **150 × 40 px**, une plage de **0 à 100**, un pas de **1**, une orientation horizontale et des valeurs min./max. visibles.

- **Général :** titre optionnel avec espacement, unité, entité HA (Home Assistant), valeur minimale/maximale, pas et valeur de prévisualisation. Les curseurs verticaux progressent du bas vers le haut. L'étiquette de valeur peut s'afficher lors de l'interaction, en permanence ou jamais. Le titre et l'unité sont affichés sous forme de texte.
- **Marques de graduation :** générées automatiquement selon un intervalle défini, ou placées à des positions spécifiques indiquées par une liste séparée par des virgules (par exemple : `-20,0,20,50,80`). Ces marques sont indépendantes du pas de réglage et peuvent être positionnées à l'intérieur de la piste, ou au-dessus/en dessous (respectivement à gauche/droite). Si l'échelle est trop dense, le nombre de marques est limité à 201 ; les étiquettes numériques s'adaptent à la taille du widget.
- **CSS du curseur – Piste / Poignée :** paramètres incluant les couleurs (format HEX), la largeur de la piste, la taille de la poignée, l'arrondi (en pourcentage) et des ombres distinctes (avec décalage X/Y, flou et extension). Le type de piste peut être « Normal », « Inversé » ou « Aucune piste active ». Une taille de poignée de **0** permet de masquer celle-ci. L'option **« Depuis le widget »** permet à chaque groupe de paramètres d'être indépendant des autres curseurs ; si des widgets sont copiés ensemble, les références internes sont ajustées en conséquence. La section **« CSS Général »** reste active.
- **Interaction :** pour permettre l'écriture de valeurs, un « helper » (entité auxiliaire) de type `input_number` est requis. Les valeurs minimale, maximale et le pas doivent correspondre à ceux configurés dans cet auxiliaire. Les capteurs (sensors) ainsi que les entités non disponibles sont affichés en mode « lecture seule ». **Lecture seule** empêche toute modification. En l'absence d'entité, la valeur reste locale ; aucune donnée n'est écrite dans l'éditeur. Les commandes d'écriture vers Home Assistant (HA) sont envoyées une fois la modification terminée.

L'exportation JSON du widget inclut toutes les options du curseur, les styles et les liaisons aux entités. L'entité ainsi que les widgets sources des styles référencés doivent également être présents sur la cible. Il peut être judicieux d'utiliser un widget de plus grande taille pour afficher le titre, l'étiquette de valeur et l'échelle.

![Curseur horizontal et vertical, barre de progression et repères personnalisés](/images/grafik-visual-studio/styled-slider.png)

Référence des fonctionnalités : [Curseur inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/slider-widget.md). Studio utilise une implémentation spécifique.

### Case à cocher (Checkbox) {#checkbox}

À partir de la version **0.1.175**, le widget **Checkbox** (Case à cocher), situé dans la section **Interactif**, vient compléter la **Bool Checkbox** (Case à cocher booléenne) existante dans les composants de base. Les nouveaux widgets sont créés avec des dimensions de **70 × 40 px**, une taille de case de **24 px** et une position du texte définie sur **Fin**.

- **Général :** Entité HA, valeurs booléennes (faux/vrai), texte associé, position du texte et état du test. Les valeurs vides utilisent `false` et `true`. Les positions « Fin/Début/Haut/Bas » placent le texte respectivement à droite, à gauche, au-dessus ou en dessous de la case. Les textes sont affichés en tant que texte.
- **Style de la case à cocher CSS :** Couleurs (format HEX) configurables pour les états inactif et actif, taille de la case (de 0 à 50 px) et option « Depuis le widget » pour reprendre le style d'une autre case à cocher. Les références cycliques sont gérées en toute sécurité ; les widgets copiés simultanément conservent des références internes cohérentes. La police et la couleur du texte suivent les paramètres CSS généraux. La section **CSS Général** reste active.
- **Utilisation :** En l'absence d'entité, la commutation s'effectue localement. `switch`, `light` et `input_boolean` prennent en charge les valeurs booléennes (on/off, 0/1). Les paires numériques nécessitent `input_number`, et les paires textuelles `input_text`. Les capteurs, les entités indisponibles et les paires de valeurs incompatibles sont en lecture seule. Aucune donnée n'est écrite depuis l'éditeur. Les opérations d'écriture en cours vers HA verrouillent temporairement la case à cocher.

L'exportation JSON inclut les valeurs, les textes, le style et la liaison avec les entités. Les entités doivent exister dans l'environnement cible ; les widgets sources dont le style est référencé doivent également y être présents. Les petites indications en rouge s'affichent conformément à l'option **Afficher les conseils pour les utilisateurs en transition**.

![Case à cocher avec texte d'état et héritage de style](/images/grafik-visual-studio/checkbox.png)

Référence fonctionnelle : [Case à cocher inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/checkbox-widget.md). Studio utilise une implémentation spécifique.

### Calendrier {#calendar}

**Calendrier** est une vue mensuelle destinée à la sélection d'une date ; elle ne sert pas à afficher des rendez-vous. Les nouveaux widgets sont créés avec une taille de **320 × 350 px**, des cellules journalières de **36 px**, le lundi comme début de semaine, et la mise en évidence du jour actuel. La section **Général** permet de configurer l'entité HA, le format de la valeur, une date de test (pour l'éditeur uniquement), la protection en écriture, le blocage des dates passées ou futures, la navigation par mois/année, le début de la semaine, l'affichage des numéros de semaine et la taille des cellules (20–80 px).

- **Horodatage (nombre, ms) :** millisecondes depuis l'époque Unix (Epoch), destiné à être écrit dans un helper `input_number`. Veillez à ce que la plage de valeurs de ce helper soit suffisamment étendue. Le sélecteur de date inscrit la valeur correspondant à minuit, selon le fuseau horaire local du navigateur.
- **Date ISO :** `JJJJ-MM-TT`, destiné à être écrit dans un helper `input_text`. Un capteur peut fournir la date, mais il ne peut pas être utilisé comme cible d'écriture. Seuls les helpers disponibles et au format approprié permettent la sélection d'une date ; une protection en écriture bloque également la navigation.
- En l'absence d'entité, la sélection reste locale à l'exécution (runtime) et n'est pas enregistrée dans le projet. La **date de test** est utilisée exclusivement dans l'éditeur ; elle est ignorée lors de l'exécution. L'éditeur n'écrit aucune valeur de date et désactive l'utilisation du calendrier.
- Les jours passés et futurs sont bloqués par rapport à la date locale du jour. Le jour actuel reste sélectionnable. Le format **ISO-8601** prend en compte les semaines calendaires au passage à la nouvelle année ; le mode **Simple** définit la semaine 1 comme celle contenant le 1er janvier, en tenant compte du jour de début de semaine choisi.

Les six groupes neutres **Calendrier CSS – En-tête / Jours de la semaine / Jour / Jour sélectionné / Aujourd'hui / Semaine calendaire** permettent de définir des couleurs (code HEX), le rayon des jours et l'ombre portée du jour sélectionné. Si les couleurs de texte ne sont pas définies, les couleurs du thème du Studio sont utilisées. L'option **Depuis le widget** reprend uniquement la configuration correspondante d'un autre widget Calendrier ; les références cycliques ou invalides sont gérées sans provoquer de boucle infinie. En cas de copie groupée, les références internes sont ajustées ; lors d'une exportation, les calendriers référencés doivent également être inclus. La section **CSS Général** reste active et conserve les paramètres de position et de taille. Les petites indications en rouge sont soumises au paramètre **Afficher les conseils pour les utilisateurs existants**.

Le mois et l'année peuvent être sélectionnés directement. Si la navigation par mois/année est désactivée, les flèches permettant de passer au mois précédent ou suivant restent disponibles en mode exécution (runtime). En cas d'échec d'une opération d'écriture HA (Home Automation), une erreur s'affiche et une nouvelle tentative est possible.

![Calendrier avec sélection de date, indicateur « Aujourd'hui » et numéros de semaine](/images/grafik-visual-studio/calendar.png)

Référence des fonctionnalités : [Calendrier par inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/calendar-widget.md). Studio utilise une implémentation propre, sans dépendance vis-à-vis du paquet ioBroker.

### Calendrier d'événements {#terminkalender}

À partir de la version **0.1.174**, le **calendrier d'événements** affiche les rendez-vous en mode lecture seule. La taille par défaut est de **600 × 500 px**. Les vues disponibles incluent : mois, semaine (avec grille horaire), jour, année (sur douze mois), ainsi que des listes par jour, semaine, mois ou année. L'en-tête et la navigation peuvent être désactivés séparément. Il est possible de configurer le début de la semaine, le format des numéros de semaine (norme ISO ou standard) et l'affichage de la ligne indiquant l'heure actuelle. Le paramètre **Max. d'événements par jour** limite le nombre d'entrées visibles ; `0` permet de toutes les afficher. Les événements supplémentaires sont accessibles via la mention **+N autres**.

- **Événements (entité HA) :** `calendar.*` charge la plage temporelle visible via [calendar.get_events](https://www.home-assistant.io/integrations/calendar/). L'état standard d'un calendrier ne contient pas une liste complète des événements. D'autres entités HA peuvent fournir une liste au format JSON en guise d'état.
- **Événements (JSON, sans entité) :** Une liste JSON stockée directement sert de source locale. Les champs pris en charge incluent `title` / `summary` / `event`, `start` / `_date`, éventuellement `end` / `_end`, `allDay` / `_allDay`, ainsi que `color` / `_calColor`. Les valeurs de début et de fin peuvent être des dates au format ISO, des dates-heures au format ISO ou des horodatages (timestamps) en millisecondes. Une date sans heure est considérée comme un événement sur toute la journée ; sa valeur de fin est alors exclue. Si la valeur de fin est absente ou identique à la valeur de début, une durée par défaut est appliquée.
- **Calendriers supplémentaires :** Il est possible de définir jusqu'à 20 sources, chacune associée à une entité HA, une couleur de source (au format HEX, facultative) et une étiquette pour la légende. Lorsque le nombre de sources dépasse `0`, ces sources remplacent à la fois le champ d'entité unique et la liste JSON locale. Les sources vides ne fournissent aucun événement. La légende peut être désactivée.
- **Règles de couleur des événements :** Il est possible de définir jusqu'à 20 règles permettant de cibler une partie du titre d'un événement (sans distinction majuscules/minuscules). La première règle correspondant au titre détermine la couleur d'arrière-plan. La couleur de la source reste visible sous forme de bande sur le côté gauche ou de point dans les listes.

```json
[{"title":"Familienausflug","start":"2026-10-03","end":"2026-10-05","color":"#3686BD"}]
```

Les six groupes neutres — **Calendrier CSS – En-tête / Jours de la semaine / Jour / Aujourd'hui / Tuiles d'événement / Bordure** — permettent de configurer les couleurs (codes HEX), les tailles de police, les rayons de bordure, les bordures, ainsi que les couleurs au survol pour les boutons de navigation. L'option **« Depuis un widget »** permet à un calendrier d'hériter des paramètres d'une autre instance de calendrier ; les références circulaires sont gérées de manière sécurisée. La section **« CSS général »** reste active. Des remarques destinées aux utilisateurs effectuant une mise à jour depuis des versions précédentes sont disponibles après l'interrupteur principal. Les aperçus dans l'éditeur ne créent pas d'événements réels dans le calendrier ; ils peuvent être déplacés et redimensionnés.

Les calendriers Home Assistant (HA) sont mis à jour lorsque la plage temporelle change ou après un intervalle minimal de 60 secondes ; les états des entités JSON suivent l'intervalle d'interrogation (polling) standard de cinq secondes. Les erreurs s'affichent directement au sein du widget. Les fichiers `.ics` sont intégrés via l'intégration calendrier de Home Assistant. La création, la modification ou la suppression d'événements de calendrier ne sont pas prises en charge.

Lors de l'exportation d'un widget, la configuration et tout code JSON saisi manuellement sont inclus, contrairement aux événements Home Assistant récupérés en temps réel. Les entités utilisées doivent être disponibles à la destination ; tout widget source référencé contenant du CSS doit également être inclus.

![Calendrier avec règles de couleur et fenêtre contextuelle (pop-up) pour les événements](/images/grafik-visual-studio/event-calendar.png)

Référence des fonctionnalités : [Calendrier inventwo pour VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/event-calendar-widget.md). L'environnement de studio utilise sa propre connexion de données et inclut une instance locale de [FullCalendar 6.1.21](https://legacy.fullcalendar.io/v6/), sous licence MIT ; le paquet ioBroker n'est pas requis.

### Élément universel {#universal-element}

![Les libellés restent visibles après un clic dans les trois widgets concernés](/images/grafik-visual-studio/captions-after-click.png)

À partir de la version Studio **0.1.195**, si le texte d'état est vide, il reprend le texte de l'état par défaut, puis, à défaut, le titre facultatif. Ainsi, un élément tel que « Éclairage garage » reste visible lors d'une commutation, même en cas d'utilisation de touches séparées. Les textes d'état non vides continuent, quant à eux, de remplacer le texte par défaut. Pour les widgets de type **Case à cocher** (**Checkbox**) et **Commutation** (**Schalten**), un texte d'état vide reprend le texte de l'autre état, puis le titre. Pour un affichage sans libellé, tous les champs de texte ainsi que le titre restent vides. Le nom de l'éditeur n'est pas affiché.

L'ancienne appellation **State Element** demeure utilisable comme terme de recherche. Les projets existants continuent d'utiliser le même type de widget : `universal-button`.

- **Général :** Entité HA, commande, mode, valeurs « faux »/« vrai » et URL de navigation. En l'absence d'entité, l'élément fonctionne localement. Un capteur ne peut pas être une cible d'écriture ; les valeurs numériques et le texte nécessitent des « assistants » (helpers) HA appropriés (`input_number`/`input_text`). Les modes « Affichage seul » et « Navigation » n'entraînent aucune modification de l'état dans HA.
- **Retour visuel au clic :** Durée en millisecondes et six couleurs au choix ; `0` permet de désactiver ce retour. Il reste visible pendant le changement d'état. L'option « Laisser passer le clic » transmet les clics de souris aux éléments situés en dessous lors de l'exécution, tout en désactivant l'interaction propre à l'élément.
- **État par défaut / États et contenus :** Le premier état actif correspondant est appliqué ; en l'absence de correspondance, l'état par défaut s'affiche. Des règles comparent l'entité du widget (ou une autre entité HA) avec les valeurs définies dans `==`, `!=`, `>`, `>=`, `<` ou `<=`. Les états peuvent être copiés, supprimés, déplacés ou désactivés. Les entrées masquées sont conservées dans la liste. L'option « Désactiver le clic si actif » ne bloque que l'état actuellement actif. Du texte peut être affiché en complément d'une icône ou d'une image ; la valeur `0` pour l'intervalle de clignotement signifie que l'élément ne clignote pas.
- **Texte / Contenu / Alignement :** Décoration du texte, marges externes distinctes, taille, rotation et effet miroir du contenu ; disposition en ligne ou en colonne, répartition, alignement du texte et du contenu, ainsi qu'inversion de l'ordre. Un type de contenu spécifiquement défini dans la section « Contenu » s'applique à tous les états. La propriété d'état `0` utilise la taille du widget du contenu.
- **Transparence / Espacement :** L'arrière-plan et le contenu possèdent leurs propres niveaux d'opacité ; les quatre marges intérieures sont réglables indépendamment.
- **Coins / Bordures / Ombre portée / Ombre interne / Forme :** Quatre coins arrondis ou biseautés, des épaisseurs et styles de bordure distincts, ainsi que des ombres définies par leur décalage, flou, taille et couleur. Les formes vont du rectangle à l'étoile, en passant par des polygones personnalisés. Les points des polygones sont saisis sous forme de paires de pourcentages ; en cas de saisie invalide, la forme redevient un rectangle. La rotation et le rayon s'appliquent aux polygones, tandis que les paramètres de coins classiques s'appliquent aux rectangles.

L'option **« Depuis le widget »** (*Vom Widget*) permet de récupérer de manière permanente les paramètres d'une section spécifique depuis un autre « Universal Element ». Les modifications apportées au widget source sont répercutées immédiatement ; en cas de source manquante ou de références cycliques, le système bascule sur des paramètres locaux plutôt que de créer une boucle infinie. Les références de couleur reprennent les couleurs par défaut du widget source. La case à cocher « Couleur personnalisée » (*eigene Farbe*) active la saisie d'une valeur de couleur HEX ; si elle n'est pas cochée, la couleur est héritée. Lors d'une copie groupée, les références internes sont automatiquement ajustées ; lors d'une exportation, les widgets référencés doivent également être inclus. La section **« CSS Général »** reste active afin de conserver les informations de position et de taille. Les petits indicateurs rouges signalant une transition peuvent être masqués de manière centralisée.

![Universal Element avec des sections de paramètres neutres et plusieurs modes d'affichage](/images/grafik-visual-studio/universal-element.png)

Les fonctionnalités s'inspirent de la [documentation « Universal » pour VIS2 d'inventwo](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/universal/styling-and-shapes.md). Studio utilise sa propre implémentation et ne nécessite pas le paquet ioBroker.

## Graphiques HA – Jauges (10) {#ha-grafik-–-gauges-10}

À partir de la version **0.1.186**, un ensemble d'instruments dédié, caractérisé par un arrière-plan brun doré, est disponible. La référence fonctionnelle est basée sur le [code source actuel de `ioBroker.vis-2-widgets-gauges`](https://github.com/ioBroker/ioBroker.vis-2-widgets-gauges/tree/main/src-widgets/src), qui comprend dix types différents. Le fichier README du projet de référence n'en présente que les trois premiers. Studio génère lui-même les instruments au format SVG ; ioBroker n'est pas requis. Il s'agit de widgets propres à Studio, et non d'une importation directe de la configuration ioBroker.

| Widget | Fonctionnalité et paramètres spécifiques |
| --- | --- |
| Farbmesser — Indicateur en arc | Segments colorés, aiguille, angle de l'arc et étiquettes min./max. |
| Wasserstand — Niveau d'eau | Indicateur de niveau circulaire avec hauteur de vague réglable et animation en option. |
| Batterie | Batterie horizontale ou verticale, jusqu'à 20 cellules, entité d'état de charge et icône de charge. |
| Bogenmesser — Indicateur en arc (progressif) | Arc de progression, rotation, jusqu'à 100 segments, remplissage à partir de zéro et entité de valeur cible. |
| Kompass — Boussole | Degrés et points cardinaux, décalage du nord, inversion de direction, échelle rotative et entité de vitesse. |
| Linearmesser — Indicateur linéaire | Barre ou aiguille horizontale/verticale avec divisions principales et secondaires, et marqueur de cible. |
| Rundinstrument — Instrument circulaire | Instrument à aiguille avec bande colorée, échelle graduée, angle d'arc, rotation et cadre. |
| Ringe — Anneaux | Jusqu'à huit entités distinctes avec leurs propres plages, couleurs, libellés et unités ; légende positionnable en bas, sur le côté ou masquée. |
| Tank — Réservoir | Forme cylindrique, rectangulaire ou horizontale, avec échelle, niveau de remplissage, pourcentage (optionnel) et effet de vagues. |
| Thermometer — Thermomètre | Colonne et réservoir (bulbe) avec plage de valeurs dédiée ; échelle positionnable à gauche, à droite ou des deux côtés. |

Tous les instruments lisent les états HA (Home Assistant) sans jamais écrire de valeurs. En l'absence d'entité, la valeur de prévisualisation est utilisée ; si une entité liée est manquante ou indisponible, l'affichage indique **—**. Les valeurs situées hors plage restent visibles sous forme numérique, tandis que le remplissage est limité à la fourchette 0–100 %. Une plage de valeurs invalide entraîne également l'affichage de **—**. Les nombres, unités, décimales, libellés, couleurs actives, couleurs des échelles/segments/aiguilles/textes, ainsi que les dimensions, sont configurables. Jusqu'à dix paliers de couleur peuvent être définis ; ils sont triés selon leurs limites supérieures, le premier palier correspondant incluant sa propre limite. Tous les paramètres et les liaisons aux entités sont enregistrés dans le fichier JSON du projet et du widget.

Dans le cas des jauges circulaires (anneaux), l'entité principale est remplacée par des entités spécifiques à chaque anneau. L'état de chargement, la vitesse et les marqueurs de cible sont récupérés conjointement avec les valeurs principales. Les effets d'animation (ondes) ne sont actifs qu'en phase d'exécution (*runtime*) et respectent le paramètre de réduction des mouvements. L'affichage des valeurs minimale et maximale reste précis, même sans ces animations.

![Les dix types de jauges en tant qu'instruments autonomes dans Studio](/images/grafik-visual-studio/gauges.png)

## Graphiques HA – Flux de données (3) {#ha-grafik-–-datenfluss-3}

| Widget | Fonction actuelle |
| --- | --- |
| [Wert-Verbindung](./datenfluss) — [Liaison de valeur](/fr/projects/grafik-visual-studio/datenfluss) | Transfert interne orienté de valeurs ; représenté par une simple ligne dans l'éditeur, invisible en phase d'exécution. |
| [Wert-Konverter](./datenfluss) — [Convertisseur de valeur](/fr/projects/grafik-visual-studio/datenfluss) | Convertit des nombres, du texte, des états de commutation et des unités ; dispose d'une fenêtre de configuration dédiée avec prévisualisation du type ; invisible en phase d'exécution. |
| [Wert-Berechnung](./datenfluss) — [Calcul de valeur](/fr/projects/grafik-visual-studio/datenfluss) | Propose les mêmes quatre types de calcul que « SVG LineBox Math » ; invisible par défaut lors de l'exécution. |

## Graphiques HA – Spécial (4) {#ha-grafik-–-spezial-4}

| Widget | Fonctionnalité |
| --- | --- |
| Dashboard in widget | Intègre un tableau de bord HA (Home Assistant) lors de l'exécution. Dimensions : 32–800 × 32–640 pixels (par défaut : 300 × 200). L'éditeur affiche un aperçu sélectionnable. |
| [SVG-Line](./svg-line) — [SVG-Line](/fr/projects/grafik-visual-studio/svg-line) | Dessine et anime des connexions entre les widgets, avec des points d'ancrage, des tracés manuels à plusieurs points et une liaison ciblée via des points de regroupement. |
| [SVG LineBox Math](./svg-linebox-math) — [SVG LineBox Math](/fr/projects/grafik-visual-studio/svg-linebox-math) | Carré visible doté de 16 points de connexion (A–P). Permet d'appliquer une formule personnalisée ou de calculer la moyenne des entrées actives ; les entrées multiples sur un même point sont additionnées. Transmission interne des valeurs sans nécessiter d'entité HA supplémentaire. |
| [SVG LineBox](./svg-linebox) — [SVG LineBox](/fr/projects/grafik-visual-studio/svg-linebox) | Distributeur visible dans l'éditeur : additionne les valeurs numériques des lignes entrantes et les transmet aux lignes sortantes, avec la possibilité de les envoyer également vers une entité auxiliaire numérique (« helper ») dans HA. Un cercle paramétrable masque les extrémités des lignes connectées lors de l'exécution. |

### Dashboard in widget {#dashboard-in-widget}

::: warning Export vers un runtime externe
Destiné aux visualisations au sein de Home Assistant. Si un export vers un runtime externe est prévu, il est préférable de ne pas utiliser ce widget. Le tableau de bord intégré n'est pas inclus dans l'exportation ; il nécessite toujours Home Assistant ainsi qu'une connexion via un navigateur.

Depuis **0.1.159**, cet avertissement s'affiche en permanence dans les paramètres du widget, indépendamment de l'option « Afficher les conseils pour les utilisateurs en transition ». Il apparaît également lors de l'exportation JSON de widgets sélectionnés si un tableau de bord est inclus ; les zones d'onglets personnalisées sont également prises en compte. La boîte de dialogue indique les widgets concernés et propose les options **Exporter quand même** ou **Annuler**. Seule la liaison au tableau de bord est exportée. L'exportation complète du projet pour un runtime externe reste prévue.
:::

![Aperçu du tableau de bord HA dans l'éditeur pour la vue Lovelace 0](/images/grafik-visual-studio/dashboard-widget.png)

*Aperçu dans l'éditeur pour /lovelace/0. L'image de test locale ne montre pas de tableau de bord HA connecté.*

**Tableau de bord** permet d'accéder à la liste des tableaux de bord HA via le menu « … ». Il est également possible de saisir directement un chemin, tel que `/lovelace` ou `/dashboard-solar`. **Vue du tableau de bord** permet de sélectionner, au choix, un chemin de vue ou un identifiant numérique, par exemple `energie` ou `0`. Dans le cadre de HA Ingress, le champ **URL de base HA** reste vide. En cas d'accès direct à Studio, l'adresse de HA doit y être saisie, par exemple `https://ha.example.org`.

L'authentification utilise la session de navigateur HA habituelle. Le widget ne stocke aucun jeton (token) ; La sélection de tableaux de bord ne renvoie que les titres et les chemins d'accès. D'autres origines peuvent être bloquées par les règles du navigateur ou des paramètres d'intégration. Une reconnexion peut s'avérer nécessaire. Les mises à jour habituelles de l'état du Studio ne rechargent pas un tableau de bord déjà intégré. Les nouveaux widgets n'activent que le CSS général ; les notifications destinées aux utilisateurs effectuant une transition peuvent être désactivées de manière centralisée. La fonction « View in widget » reste dédiée aux pages du Studio.
