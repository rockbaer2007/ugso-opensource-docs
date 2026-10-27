---
title: Éditeur et raccourcis clavier
---

# Éditeur et raccourcis clavier {#editor-und-tastenkombinationen}

À partir de **0.1.296**, une langue (DE/EN/FR) peut être définie pour le projet ou le widget, s'appliquant aux paquets et affichages restants, ainsi qu'aux éléments optionnels tels que les [sources HA, les unités et les commandes de climatisation](/fr/projects/grafik-visual-studio/ha-quellen-climate). L'interface générale du Studio reste disponible en DE/EN ; les anciens paramètres demeurent valides.

À partir du **Studio 0.1.295**, des fonctionnalités supplémentaires sont disponibles, notamment des [fonctions universelles, des dégradés de couleurs radiaux et des icônes « Material » de plus grande taille](/fr/projects/grafik-visual-studio/interaktiv). Les paramètres et le comportement des boutons existants sont conservés ; les nouvelles options peuvent être activées au choix.

À partir de la version **Studio 0.1.294**, les aperçus des onze **widgets interactifs** occupent tout l'espace disponible dans la barre latérale et le sélecteur de widgets, en s'adaptant aux thèmes clair et sombre. Les paramètres et le comportement à l'exécution (runtime) sont conservés. La [comparaison du code source avec Inventwo VIS-2 1.10.0](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/inventwo-interactive-audit-2026-10-12.md) détaille les différences : il manque notamment des actions et contenus supplémentaires pour le widget « Universal », ainsi que des dégradés de couleurs pour le curseur radial. Une équivalence parfaite (1:1) n'est donc pas encore atteinte.

À partir de la version **Studio 0.1.293**, les [compléments « Basic » issus de la comparaison avec VIS-2](/fr/projects/grafik-visual-studio/basic) sont disponibles, incluant des propriétés sélectionnables séparément pour les langues DE, EN et FR. Les paramètres des widgets existants sont conservés.

À partir de la version **Studio 0.1.291**, les raccourcis **Ctrl+C** (copier), **Ctrl+X** (couper) et **Ctrl+V** (coller) sont fonctionnels pour un ou plusieurs widgets sélectionnés. Sur macOS, la touche **Cmd** est utilisée en lieu et place de Ctrl. Ces opérations utilisent le même presse-papiers interne que la barre d'outils et le menu contextuel ; les widgets collés se voient attribuer de nouveaux identifiants (ID), tandis que leurs valeurs sont préservées. Les actions « couper » et « coller » peuvent être annulées. Dans les champs de texte, les raccourcis clavier textuels habituels restent actifs ; les boîtes de dialogue ouvertes ainsi que l'exécution en mode « runtime » ne déclenchent aucune action liée aux widgets.

À partir de la version **Studio 0.1.290**, l'utilisation de la touche **Suppr** (ou **Entf**) sur des widgets sélectionnés ouvre la même boîte de dialogue de suppression que celle utilisée pour la corbeille. Cela s'applique également en cas de sélection multiple. L'annulation ou l'utilisation de la touche **Échap** permet de conserver les widgets ; si la suppression est confirmée, il est possible de la rétablir via la fonction « Annuler ». L'option permettant de désactiver temporairement les demandes de confirmation (pour une durée de cinq minutes) s'applique aussi à la touche **Suppr**. Dans les champs de texte, les boîtes de dialogue ouvertes et lors de l'exécution (Runtime), cette touche ne supprime aucun widget ; maintenir la touche enfoncée ne déclenche pas de demandes supplémentaires.

## Masquer des widgets uniquement lors de l'exécution (Runtime) {#widgets-nur-in-der-runtime-ausblenden}

À partir de la version **Studio 0.1.287**, une case à cocher intitulée **Masquer lors de l'exécution** (ou « In Runtime verstecken ») est disponible pour **tous les widgets**, tout en haut de l'onglet **WIDGET**. Cochez cette case et enregistrez le projet : le widget reste visible dans l'éditeur, mais est masqué lors de l'exécution (Runtime). Les calculs et les transferts de valeurs restent actifs (par exemple, depuis un widget de type « Nombre » masqué vers un bloc de calcul). Cette option fonctionne indépendamment de l'indice Z (Z-index). Si la case est décochée, la visibilité normale est rétablie ; les widgets spécifiques liés au flux de données restent, quant à eux, toujours masqués. Les éléments de contrôle masqués ne peuvent pas être cliqués lors de l'exécution.

À partir de la version **Studio 0.1.286**, l'attribution d'un **indice Z (Z-index) de -100 ou moins** permet de masquer n'importe quel type de widget lors de l'exécution (Runtime). Dans l'éditeur, le widget reste visible et modifiable. Les calculs et le flux de données demeurent actifs ; il est ainsi possible d'utiliser des widgets de type « Nombre », des blocs de calcul (« MathBox ») et leurs connexions comme une chaîne de traitement invisible. Cette règle de masquage spécifique ne s'applique pas si l'indice Z est supérieur ou égal à -99. Un élément de contrôle masqué ne peut pas être cliqué lors de l'exécution.

## Onglets de pages {#seiten-tabs}

À partir de la version **0.1.256**, les pages du projet s'affichent sous forme d'onglets compacts, situés directement au-dessus de l'espace de travail, entre la palette de widgets et le panneau des propriétés. Un simple clic permet de changer de page ; la page active est mise en évidence par une couleur. De nombreuses pages défilent horizontalement ; les noms longs sont tronqués, mais leur intitulé complet apparaît dans une info-bulle. Les pages masquées lors de l'exécution (runtime) restent accessibles dans l'éditeur ; leur onglet est alors entouré d'un bord en pointillés.

![Pages du projet sous forme d'onglets au-dessus de l'espace de travail](/images/grafik-visual-studio/page-tabs.png)

Lorsqu'un onglet est sélectionné, les touches **flèche gauche/droite** permettent de passer à la page adjacente, tandis que les touches **Début/Fin** (Pos1/Ende) permettent d'accéder à la première ou à la dernière page. Les modifications apportées aux widgets et non enregistrées sont conservées lors du changement de page ; en revanche, la sélection des widgets et les actions en cours sur les widgets sont réinitialisées. Les noms et l'ordre des pages correspondent à ceux définis dans le menu **Pages**. Les fonctions de création, renommage, duplication, gestion de la visibilité et suppression restent accessibles via ce menu. Ces onglets constituent une aide à la conception dans l'éditeur ; le mode exécution (runtime) continue d'utiliser son système de navigation habituel.

## Prise en main {#einstieg}

À partir de la version **0.1.184**, des couleurs d'arrière-plan permettent de distinguer les ensembles de widgets dans la palette : **Interactif** est vert olive, **Spécial** est bleu et **Flux de données** est violet. **Base** conserve son apparence actuelle. Les ensembles supplémentaires installés se voient attribuer une couleur spécifique. Ces couleurs s'appliquent aux boutons de sélection de la palette ; la mise en forme des widgets insérés reste, quant à elle, indépendante.

À partir de la version **0.1.185**, les zones de sélection de tous les ensembles présentent un design plus plat : la hauteur minimale passe de 42 px à 34 px, avec des aperçus de 32 × 26 px. Les libellés restent parfaitement lisibles. L'élément **Dashboard in widget** adopte l'icône standard `mdi:view-dashboard`.

![Zones de sélection plus plates dans la palette de widgets](/images/grafik-visual-studio/palette-compact.png)

À partir de la version **0.1.115** de Studio, un clic droit sur un widget, un onglet de groupe ou une zone vide de l'éditeur ouvre un menu contextuel proposant les options suivantes : **Sélectionner**, **Grouper**, **Dissocier**, **Modifier le groupe**, **Copier**, **Couper**, **Coller** et **Supprimer**. La rubrique **Plus** inclut les fonctions : Dupliquer, Premier plan/Arrière-plan, Verrouiller/Déverrouiller, Annuler/Rétablir, ainsi que l'importation/exportation de widgets. Les actions non disponibles apparaissent en grisé ; la touche Échap permet de fermer le menu, tandis que les flèches haut/bas permettent d'y naviguer. L'option « Sélectionner » propose l'ensemble des widgets ainsi que ceux situés sous le curseur de la souris.

Les groupes conservent les positions relatives de leurs éléments constitutifs ; ainsi, lorsqu'un élément du groupe ou l'onglet du groupe est déplacé, l'ensemble du groupe se déplace en bloc. Ces groupes sont enregistrés dans le projet ; Lorsqu'ils sont collés ou importés, les copies et exportations de plusieurs widgets sélectionnés forment des groupes indépendants. La fonction **Modifier le groupe** permet de modifier les éléments individuellement ; **Terminer la modification du groupe** — ou un clic sur l'onglet du groupe — permet de revenir à la sélection globale. La dissociation (dégroupage) préserve les positions et les dimensions. Les fonctions « Annuler » et « Rétablir » s'appliquent également aux opérations de regroupement et de déplacement. Les groupes sont à structure « plate » ; les lignes de connexion SVG ne peuvent pas être regroupées, et les groupes contenant des éléments verrouillés ne peuvent pas être déplacés par glisser-déposer. En mode exécution (Runtime), ni les cadres de groupe ni le menu d'édition ne sont affichés. Le regroupement ne génère pas de contenu d'onglet et n'importe pas de widgets VIS2.

Créez un projet dans le menu **Projets** et sélectionnez une page via **Pages**. Définissez la taille de la page, utilisez la **palette de widgets** située à gauche et insérez un élément depuis cette palette. La fonction **Rechercher des widgets**, située en haut de la palette, vous permet de filtrer les widgets disponibles par nom ou par type ; les groupes correspondants s'ouvrent lors de la recherche, sans modifier leur état de déploiement initial. Un clic sur un widget permet de le sélectionner ; ses propriétés s'affichent alors sur la droite. Utilisez **Runtime** pour vérifier l'affichage. La fonction **Enregistrer** permet une sauvegarde manuelle ; les paramètres de sauvegarde automatique (Auto-Save) et son délai peuvent être ajustés sous **Paramètres → Général**. Dans la section **Packs de widgets**, vous pouvez installer un pack local (`.wg.zip`) à partir de la version 0.1.80. La première interface (0.1) prend en charge des widgets texte validés dotés de propriétés ; les packs installés apparaissent sous forme d'un ensemble distinct dans la palette. Depuis la version 0.1.83, les images des widgets et des packs peuvent être des fichiers SVG ou PNG validés ; en l'absence d'image personnalisée, le symbole texte SVG intégré s'affiche. La suppression est bloquée si un widget issu d'un pack est utilisé dans un projet. À partir de la version 0.1.82, l'onglet **Outils** permet l'installation de packs locaux (`.tp.zip`). Le premier outil déclaratif affiche un aperçu et, après confirmation, modifie la couleur d'arrière-plan de la page active ; cette modification peut être annulée via la fonction **Annuler**. Les images des outils peuvent également être au format SVG ou PNG ; les boutons du Studio utilisent des symboles SVG. L'installation depuis GitHub ainsi que les mises à jour seront disponibles ultérieurement.

Dans le sélecteur de widgets situé sur la barre supérieure, vous pouvez sélectionner plusieurs widgets ou annuler la sélection. La barre d'actions propose les fonctions Couper, Copier, Coller, Dupliquer, Supprimer, ainsi que jusqu'à 50 niveaux d'annulation/rétablissement (Undo/Redo). Les dix actions d'alignement s'appliquent à plusieurs widgets standard sélectionnés ; le premier widget sélectionné sert de référence. Pour les paramètres **Largeur** et **Hauteur**, un appui long (environ 0,6 seconde) permet de saisir la valeur souhaitée en pixels.

L'environnement d'exécution (runtime) centre une page lorsqu'elle tient entièrement dans la fenêtre du navigateur. Pour les pages plus grandes, l'affichage commence en haut à gauche ; des barres de défilement horizontales et verticales permettent d'accéder à l'ensemble de la page, sans modifier les coordonnées des widgets.

## Sélection, copie et suppression de widgets {#widget-auswahl-kopieren-und-loschen}

À partir de la version **Studio 0.1.257**, les icônes de la barre d'outils correspondant à **Supprimer**, **Copier** et **Couper** s'activent dès qu'un widget est sélectionné. Si aucun widget n'est sélectionné, ces actions apparaissent grisées ; cela s'applique également lors d'un changement de page. La confirmation de suppression ainsi que la fonction « Annuler » restent disponibles.

![Liste de sélection de widgets avec dix entrées visibles](/images/grafik-visual-studio/widget-selector-ten.png)

Dans Studio **0.1.196**, la liste peut contenir dix entrées compactes. Si elle en contient davantage, il est possible de faire défiler le contenu ; les actions situées en haut et en bas restent visibles. Si le nombre d'entrées est inférieur, le menu est plus court. Sur les petits écrans, le nombre de lignes visibles s'adapte à la hauteur disponible.

Les lignes cochées sélectionnent les widgets correspondants sur l'espace de travail. La liste reste visible pendant cette opération ; les actions **Copier** et **Supprimer** s'appliquent à tous les widgets cochés.

![Déplacement groupé de plusieurs widgets collés](/images/grafik-visual-studio/multi-move.png)

Faites glisser l'un des widgets sélectionnés pour déplacer l'ensemble de la sélection, y compris après une opération de copier-coller. Les connexions et les points intermédiaires sélectionnés se déplacent également ; la présence de widgets verrouillés empêche le déplacement groupé. La fonction « Annuler » permet de revenir en arrière sur cette action.

![Confirmation de suppression avec option de masquage pendant cinq minutes](/images/grafik-visual-studio/delete-dialog.png)

Cliquez sur **Annuler** ou appuyez sur la touche Échap pour interrompre la suppression. La case à cocher permet de masquer les futures demandes de confirmation pendant cinq minutes au cours de la session d'édition actuelle. Les widgets supprimés peuvent toujours être récupérés via la fonction « Annuler ».

## Fichiers et sélection d'images {#dateien-und-bildauswahl}

![Recherche de fichiers sous le dossier racine de Studio](/images/grafik-visual-studio/files-search.png)

Le dossier racine est **/config/www/studio**. Studio tente de le créer automatiquement ; toute absence de droits d'écriture sera signalée. La sélection d'images pour les widgets utilise également ce dossier ; les chemins publics commencent par **/local/studio/**. La recherche prend en compte tous les sous-dossiers, ainsi que les noms de fichiers et les chemins d'accès, sans distinction entre majuscules et minuscules. Si le champ de recherche est vide, le dossier actuellement ouvert s'affiche à nouveau. Il est possible de sélectionner des images, y compris des fichiers GIF. La navigation vers le dossier parent reste limitée au périmètre de ce dossier racine.

## Langue de l'interface {#sprache-der-oberflache}

Accédez à **Paramètres → Général → Langue → Langue de l'application**, sélectionnez une option et cliquez sur **Enregistrer** :

| Sélection | Affichage |
| --- | --- |
| **Automatique (Home Assistant)** | Allemand si Home Assistant est configuré en allemand ; anglais pour toute autre langue. Si la langue de Home Assistant n'est pas détectable, la langue du navigateur est utilisée, avec la même logique de repli (allemand/anglais). |
| **Allemand** | L'interface reste en allemand. |
| **Anglais** | L'interface reste en anglais. |

Ce choix ne s'applique qu'au navigateur actuel et est conservé après un rechargement de la page. Les autres utilisateurs et navigateurs conservent leurs propres paramètres. La langue affecte les éléments de l'interface tels que les menus, les boîtes de dialogue, la palette de widgets et les propriétés ; en revanche, les noms de projets et de widgets définis par l'utilisateur, ainsi que le contenu des widgets, ne sont pas traduits.

## Clavier et souris {#tastatur-und-maus}

| Action | Manipulation |
| --- | --- |
| Annuler | `Strg+Z` (macOS : `⌘+Z`) |
| Rétablir | `Strg+Y` ou `Strg+Umschalt+Z` (macOS : `⌘+Y` ou `⌘+Umschalt+Z`) |
| Ajouter ou retirer un widget d'une sélection multiple | Maintenir `Strg+Umschalt` enfoncé et cliquer sur le widget |
| Déplacer un point d'extrémité libre d'une connexion | Faire glisser le point avec la souris ; déplacer le point sélectionné par incréments de 1 pixel à l'aide des touches fléchées |
| Déplacer un point de ligne plus rapidement | Maintenir `Umschalt` tout en appuyant sur une touche fléchée : déplacement par incréments de 10 pixels |
| Détacher un point de ligne ancré | Maintenir `Strg` et faire glisser le point ; également possible en utilisant `Strg` combiné à une touche fléchée |
| Déplacer une ligne de connexion entière | Faire glisser une ligne libre ; pour une ligne ancrée, maintenir `Alt` et faire glisser. Les ancrages existants sont alors supprimés. Le déplacement des poignées de points individuels ne déplace pas une sélection multiple ; le glissement s'active après un déplacement de 6 px. |
| Insérer un point intermédiaire ou un point de regroupement | Cliquer sur la ligne, sélectionner « Point intermédiaire » ou « Point de regroupement » et valider par **OK** |

Les raccourcis pour « Annuler » et « Rétablir » s'appliquent lorsque le focus n'est pas placé dans un champ de saisie, une zone de texte ou un champ de sélection. Des boutons sont disponibles pour les fonctions « Couper », « Copier » et « Coller » ; aucun raccourci global `Strg+X/C/V` n'est actuellement défini pour ces actions.

## Lignes de connexion et points d'ancrage {#verbindungslinien-und-andockpunkte}

Activez les **points d'ancrage** dans les propriétés d'un widget cible. Pour les nouveaux widgets, tous les points sont désactivés. L'option **Tous les points** permet d'activer simultanément les douze positions ; des points individuels peuvent ensuite être ajustés. La case à cocher du groupe active ou désactive l'ensemble de la zone. Les extrémités d'une connexion SVG peuvent être déplacées vers des points actifs. Un point intermédiaire divise le tracé en segments supplémentaires ; seul un **point de connexion** (sammelpunkt) explicitement activé peut servir de point de raccordement pour d'autres lignes. Un simple croisement ne relie pas les lignes entre elles. Pour la représentation visuelle, plusieurs options sont disponibles, notamment : lignes, tracés en zigzag ou à points multiples, couleurs, épaisseur, pointes de flèches, animations et gestion de l'ordre d'empilement (z-index).

## Visibilité et filtres {#sichtbarkeit-und-filter}

Les sections **Général** et **Visibilité** sont présentes sur chaque widget et sont désactivées par défaut. La section « Général » comprend, entre autres, le nom, un commentaire, une classe CSS, un mot-clé de filtrage et une option de verrouillage. Le filtre de l'éditeur permet de masquer des widgets en fonction de ce mot-clé ou, au contraire, de n'afficher que les éléments correspondants. En phase d'exécution (runtime), la visibilité peut être conditionnée par l'état d'une entité Home Assistant, en utilisant une condition et une valeur de comparaison ; l'évaluation par groupe n'est pas encore implémentée.
