---
title: Thèmes et zoom
---

# Thèmes et zoom

## Logique et Objets depuis 0.1.56

Dans Standard/Dark, les blocs logiques sont bleus et les objets bruns, avec des libellés blancs lisibles. Modern et Tritanopia conservent leurs propres palettes. **Si / sinon si / sinon** est désormais disponible dans **Logique** : l’engrenage ouvre le constructeur de branches ; les branches sinon si et Sinon peuvent y être ajoutées ou retirées. Les conditions et séquences d’actions produisent une branche native HA. Les projets existants restent compatibles.

## Grille de points depuis 0.1.51

L’espace de travail affiche une grille native Blockly bien visible, avec un espacement de 25 unités et l’alignement automatique, inspirée de [l’éditeur Blockly d’ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/BlocklyEditor.tsx). Le fond et les points suivent immédiatement l’apparence **Clair / Sombre / Système**, y compris les changements du système. La palette Blockly détermine toujours les couleurs des blocs et des menus ; le fond suit l’application même avec la palette Dark.

Le zoom et le déplacement font suivre la grille. Ajuster ne modifie pas la taille des blocs du menu. L’apparence et la palette ne changent ni l’automatisation ni le YAML.

![Grille claire](/assets/blocks-for-ha/grid/fr/light.png)

![Grille sombre](/assets/blocks-for-ha/grid/fr/dark.png)

Depuis **0.1.27**, les blocs UGSo Standard/Dark utilisent des libellés blancs. Les fonds bleus et bruns intermédiaires sont légèrement assombris pour un contraste d’au moins **4,5:1**. Les couleurs claires originales de Modern/Tritanopia utilisent une écriture sombre suffisamment contrastée. Les champs éditables restent distincts et lisibles. Les images DE/EN/FR du catalogue ont été régénérées avec cette correction.

Le thème de l’application et la palette Blockly sont **indépendants**. La langue des blocs est également un réglage distinct. Ni thèmes ni zoom ni langue ne modifient le YAML.

## Palette Blockly

| Choix | Apparence | Source originale |
| --- | --- | --- |
| UGSo Standard | Couleurs des groupes UGSo, menu sombre et panneau de blocs clair | Adaptation UGSo de Blockly Classic |
| Dark | Espace de travail et panneau sombres, fond du menu distinct | [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| Modern | Palette Modern originale avec bordures marquées et groupes UGSo | [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| Tritanopia | Palette des groupes standard adaptée, complétée pour les groupes HA | [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |

Tritanopia vise les personnes présentant cette déficience de vision des couleurs. Les blocs clairs ont des libellés sombres, les blocs sombres des libellés clairs. Les champs éditables restent visuellement distincts. Les noms des catégories apportent un repère supplémentaire. Cela ne constitue pas une certification complète d’accessibilité.

![Palette Dark, blocs français](/assets/blocks-for-ha/themes/fr/dark.png)

![Palette Tritanopia, blocs français](/assets/blocks-for-ha/themes/fr/tritanopia.png)

Le choix est sauvegardé localement. Une préférence inconnue revient au standard ; si le stockage est bloqué, le changement reste possible pour la page actuelle.

## Zoom

Depuis **0.1.40**, tous les thèmes utilisent une **police de 16 px**. Le menu de blocs reste à **100 %** : ajustement, molette et zoom modifient uniquement l’espace de travail. Zoom initial 100 %, ajustement 85–120 %, zoom manuel 50–240 %. Les grandes automatisations restent défilables ; l’ajustement ne descend pas sous 85 % afin de préserver la lisibilité. Vérifié en Full HD, 2560 px et HiDPI.

## Apparence de l’application

**Darstellung** propose **Hell**, **Dunkel** et **System** pour l’en-tête, les panneaux, formulaires, YAML, dialogues et éditeurs. System suit immédiatement la préférence de couleur du navigateur/système ; un choix manuel la remplace. Préférence locale, indépendante de la palette Blockly. Le badge Built with Blockly utilise automatiquement la variante adaptée.

Blockly et les plugins de thèmes/zoom sont épinglés à 13.3.0 et intégrés localement sous Apache-2.0. [Catalogue et liens des plugins](./blocks).

:::: details Référence détaillée issue de la documentation allemande

## Thèmes et zoom {#themes-und-zoom}

### Logique et objets depuis 0.1.56 {#logik-und-objekte-seit-0-1-56}

Dans les thèmes « Standard » et « Dark », les blocs de logique sont bleus et les blocs d'objets sont bruns, avec un texte blanc bien lisible. Les thèmes « Modern » et « Tritanopia » conservent leurs propres palettes. La structure **Si / Sinon si / Sinon** est désormais intégrée directement dans la section **Logique** : l'icône en forme de roue dentée ouvre un menu permettant de gérer les branches supplémentaires (ajout ou suppression de branches et du bloc « Sinon »). Les conditions et les chaînes d'actions sont générées sous forme de structures conditionnelles natives de HA. Les projets existants restent compatibles.

### Grille de points depuis 0.1.51 {#punktraster-seit-0-1-51}

L'espace de travail affiche une grille de points Blockly native, clairement visible, avec un espacement de 25 unités et une fonction d'alignement (magnétisme), inspirée de l'[éditeur Blockly d'ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/BlocklyEditor.tsx). L'arrière-plan et les points s'adaptent instantanément au mode d'affichage de l'application (**Clair / Sombre / Système**), y compris en cas de modification des paramètres système. Le choix du thème Blockly détermine toujours les couleurs des blocs et des menus ; l'espace de travail suit le mode d'affichage de l'application, même lorsque la palette « Sombre » est sélectionnée.

Le zoom et le déplacement (panoramique) entraînent la grille en même temps que l'espace de travail. L'ajustement à l'écran (« Fit ») ne modifie pas la taille des blocs dans les menus. Le mode d'affichage et la palette n'affectent ni les automatisations ni le code YAML.

![Grille de points en mode clair](/assets/blocks-for-ha/grid/de/light.png)

![Grille de points en mode sombre](/assets/blocks-for-ha/grid/de/dark.png)

Depuis la version **0.1.27**, les blocs UGSo (en modes Standard/Sombre) présentent des libellés en blanc. Les zones bleues et brunes de teinte moyenne sont légèrement assombries pour garantir un rapport de contraste d'au moins **4,5:1**. Pour les couleurs claires d'origine (thèmes « Modern » / « Tritanopia »), une police sombre offrant un contraste suffisant est utilisée. Les champs de saisie restent lisibles indépendamment. Les visuels des blocs dans le catalogue ont été régénérés pour les langues DE/EN/FR en intégrant cette correction.

Depuis la version **0.1.16**, la barre d'outils située au-dessus de l'espace de travail inclut un **sélecteur de thème**. Celui-ci s'applique à l'environnement Blockly, y compris aux catégories, au sélecteur de blocs et aux blocs eux-mêmes. La palette Blockly est indépendante du mode d'affichage de l'application. Le nombre de types de blocs reste inchangé (111).

| Sélection | Affichage | Source originale |
| --- | --- | --- |
| UGSo Standard | Couleurs de groupe UGSo habituelles, menu sombre et sélection de blocs claire | Personnalisation UGSo spécifique basée sur Blockly Classic |
| Dark | Espace de travail sombre, sélection de blocs sombre et menu des catégories distinct | [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| Modern | Palette « Modern » originale avec des bordures plus marquées et groupes d'extension UGSo | [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| Tritanopia | Palette originale pour les groupes standard et couleurs supplémentaires pour les groupes spécifiques à HA | [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |

Le mode « Tritanopia » est conçu pour les personnes présentant ce type de trouble de la vision des couleurs. Les blocs et catégories propres à UGSo utilisent désormais des styles de thème plutôt que des couleurs fixes. Les blocs clairs présentent des inscriptions sombres, tandis que les blocs sombres affichent des inscriptions claires ; les champs de saisie restent lisibles. La catégorie sélectionnée, quelle que soit la palette utilisée, présente un fond sombre avec une écriture claire. Les noms des catégories et le texte des blocs restent visibles pour faciliter le repérage. Ceci ne constitue pas une certification complète en matière d'accessibilité.

![Mode « Dark » dans l'éditeur UGSo](/assets/blocks-for-ha/themes/de/dark.png)

![Mode « Tritanopia » dans l'éditeur UGSo](/assets/blocks-for-ha/themes/de/tritanopia.png)

### Changer et enregistrer {#wechseln-und-speichern}

Le thème est commuté instantanément, sans qu'il soit nécessaire de reconstruire l'espace de travail. Les blocs, les connexions, la disposition et le code YAML sont conservés. Ce choix est enregistré dans le navigateur — indépendamment du projet — et est réappliqué après un rechargement de la page. Les fichiers de projet et le code YAML ne transmettent pas ce paramètre d'affichage aux autres navigateurs. En cas de paramètres inconnus, le système revient au thème par défaut « UGSo » ; si le stockage du navigateur est bloqué, le changement reste effectif pour la session en cours.

Le moteur de rendu **Geras** existant demeure actif pour tous les thèmes, garantissant ainsi la préservation de la géométrie des connecteurs et des modalités d'interaction. Le thème « Modern » original préconise l'utilisation de Zelos/Thrasos ; dans ce contexte, sa palette de couleurs et de bordures est appliquée et validée avec Geras. Le changement de moteur de rendu ne constitue pas une option supplémentaire dans cette version.

### Ajuster tous les blocs {#alle-blocks-einpassen}

La fonctionnalité originale [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) est complétée par une icône représentant quatre flèches, située à côté des commandes de zoom. Un simple clic permet d'ajuster les blocs à l'espace de travail disponible. Ce bouton est également accessible via la touche Tabulation et peut être activé avec les touches Entrée ou Espace. Le zoom modifie la vue, mais n'affecte pas l'automatisation elle-même.

Depuis **0.1.40**, les blocs utilisent une police de **16 px** dans tous les thèmes. Le menu des blocs reste fixé à **100 %** : les fonctions d'ajustement, la molette de la souris et les commandes de zoom n'agissent que sur l'espace de travail. Le zoom initial est de 100 %, l'ajustement automatique varie entre 85 % et 120 %, et le zoom manuel est possible de 50 % à 240 %. Les automatisations de grande taille restent déplaçables ; la fonction d'ajustement ne réduit leur taille qu'à 85 % au minimum, afin de garantir la lisibilité du texte. Testé en résolution Full HD, 2560 px et sur écrans HiDPI.

Les quatre plugins originaux supplémentaires sont définis sur **13.3.0**, intègrent Blockly via **13.3.0** et sont sous licence Apache (**2.0**). Les six plugins originaux existants restent sous **13.2.0**. Les paquets sont fournis localement ; aucune dépendance externe (fichiers de thème ou CDN). Les sources originales et les mentions de licence sont également disponibles dans le [catalogue de blocs](/fr/projects/blocks-for-ha/blocks).

Éléments vérifiés : quatre thèmes, typographie sur les blocs clairs (mode Tritanopie), sortie projet/YAML inchangée, mémorisation de la sélection, gestion des paramètres de stockage inconnus ou verrouillés, ajustement à l'écran et largeur pour mobile. Le fonctionnement de HA (Home Assistant) n'est pas altéré par cette modification d'affichage.

### Apparence de l'application : Clair, Sombre ou Système {#app-darstellung-hell-dunkel-oder-system}

Depuis **0.1.22**, une option d'**affichage** est disponible dans l'en-tête, proposant les modes **Clair**, **Sombre** et **Système** pour l'ensemble de l'interface de l'application : en-tête, panneaux, formulaires, sortie YAML, boîtes de dialogue, sélecteur d'entités et éditeur de blocs/modèles personnalisé. Le mode « Système » est activé par défaut ; toute modification de la préférence de couleur au niveau du système d'exploitation ou du navigateur est immédiatement prise en compte. Une sélection manuelle prévaut sur le réglage système. Ce paramètre est enregistré localement dans le navigateur ; si le stockage du navigateur est désactivé, le changement de mode reste fonctionnel pour la page en cours.

Les thèmes Blockly restent sélectionnables séparément dans la barre d'outils, incluant notamment les thèmes « Modern » et « Tritanopia ». Le choix de l'affichage n'affecte ni les blocs, ni le code YAML généré, ni les projets. Le badge original « Built-with-Blockly » s'adapte automatiquement à la variante claire ou sombre correspondante.

::::
