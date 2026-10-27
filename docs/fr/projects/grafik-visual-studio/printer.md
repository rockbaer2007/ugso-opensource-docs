---
title: Imprimante – Imprimante et cartouches
description: Ensemble de widgets (widgetset) autonome pour imprimante, affichant l'état et jusqu'à six cartouches réparties automatiquement de manière uniforme.
---

# Imprimante {#printer}

À partir de la version **Studio 0.1.273**, l'option est accessible via **Propriétés → WIDGET → Cartouches → Style → Cartouches / Barres**. Le mode **Cartouches** affiche les graphismes habituels côte à côte ; le mode **Barres** affiche 1 à 6 lignes comprenant le nom, un indicateur de niveau horizontal et un pourcentage. Les entités, les couleurs et le seuil d'alerte s'appliquent aux deux styles. Les valeurs manquantes sont représentées par **—** ; l'ancienne option « Toner » est désormais intégrée sous forme de barres. Le paramètre de taille (pleine/demi) des cartouches ne s'applique qu'aux graphismes de type « cartouche ». Le **pack Imprimante 0.1.1** contient cette option corrigée ; les instances existantes basées sur **0.1.0-Pakete** restent compatibles avec la version mise à jour de Studio.

**Printer 0.1.1** est un ensemble de widgets externe créé par **rockbaer2007**. Pour utiliser les styles présentés ici, la version **Grafik Visual Studio 0.1.273 (ou ultérieure)** est requise. Il affiche une imprimante avec son état actuel ainsi que **1 à 6 niveaux d'encre ou de toner**, représentés au choix par des graphismes de cartouches ou par des barres horizontales.

### Style : Cartouches {#stil-patronen}

L'image montre l'interface en cours d'exécution (runtime) avec des données de test.

![Imprimante avec six cartouches et un indicateur d'alerte](/images/grafik-visual-studio/printer-six.png)

### Style : Barres {#stil-balken}

Sous **Propriétés → WIDGET → Cartouches → Style**, sélectionnez l'option **Barres**. L'image d'exécution (runtime) suivante présente six niveaux de remplissage avec des données de test : le niveau **Jaune (18 %)** est inférieur au seuil d'alerte de 20 % et apparaît donc mis en évidence. Pour la couleur **Gris**, aucune mesure n'est disponible ; la barre est hachurée et affiche **—** au lieu d'une valeur en pourcentage arbitraire.

![Affichage de type « barres » pour imprimante, avec six niveaux de remplissage, une alerte pour le jaune et un niveau inconnu pour le gris](/images/grafik-visual-studio/printer-bars.png)

## Projet original {#originalprojekt}

Ce composant s'inspire de la carte [HA Printer Card d'ADNPolymerase](https://github.com/ADNPolymerase/ha-printer-card), publiée sous [licence MIT](https://github.com/ADNPolymerase/ha-printer-card/blob/main/LICENSE). L'original est une carte Lovelace. « Printer » utilise son propre dessin SVG, son propre moteur de rendu (Studio Renderer) et des entités Home Assistant spécifiquement sélectionnées. Le code et les graphismes originaux ne sont pas intégrés. Il fait partie d'un ensemble distinct dans la palette, et non de la catégorie « Industrial ».

## Installation {#installieren}

1. Mettez à jour Grafik Visual Studio vers la version **0.1.273 ou ultérieure**.
2. Téléchargez le fichier [ugso.printer.wg](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/printer/ugso.printer.wg).
3. Installez-le via **Paramètres → Packs de widgets → Local**.
4. Insérez l'élément **Printer → Imprimante** depuis la palette, puis sélectionnez les entités correspondant à l'état et aux niveaux de remplissage à l'aide du bouton **…**.

Le pack contient une définition déclarative du widget, une icône dédiée pour la palette, une documentation et la licence MIT. Il ne contient aucun code exécutable. [Code source et documentation du pack](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/printer).

## Paramètres {#einstellungen}

À partir de la version **0.1.270** du studio, les sections **CSS Font & Text** (Police et texte), **CSS Hintergrund** (Arrière-plan), **CSS Ränder** (Bordures) et **CSS Schatten und Abstand** (Ombres et espacements) sont disponibles sous **Propriétés → WIDGET**, en complément de la section **CSS Allgemein** (CSS général). Ces nouveaux groupes sont désactivés par défaut. Activez-les en cochant la case correspondante pour configurer la police, l'arrière-plan (ou l'image), la couleur, l'épaisseur et le style des bordures, le rayon des angles (**0 = angles vifs**), ainsi que les ombres et les espacements. Le CSS s'applique à la carte d'imprimante visible, et non à l'arrière-plan situé derrière celle-ci. Les couleurs relatives à l'état et aux cartouches conservent leurs propres paramètres. Continuez à utiliser le paquet existant.

| Section | Paramètre |
| --- | --- |
| Imprimante | Nom, entité d'état, modèle : `mfp` (multifonction), `inkjet` (jet d'encre) ou `office` (imprimante de bureau). |
| Cartouches | Nombre (**1–6**), **Style → Cartouches / Barres**, seuil d'alerte (**0–100 %**, valeur par défaut : **20 %**). |
| Cartouche 1–6 | Entité dédiée au niveau de remplissage (en pourcentage), libellé et couleur. Les N premières entrées sont actives. Les liaisons configurées pour des entrées ultérieures restent enregistrées, mais ne sont sollicitées que si le nombre total d'entrées est augmenté. |
| Message d'état | Peut être masqué. Entité distincte facultative ; sinon, utilise `state_message` ou `state_reason` de l'entité imprimante. |
| Valeurs supplémentaires | Entités facultatives pour la puissance (consommation) et le compteur de pages. |
| Couleurs et dimensions | Couleurs de l'arrière-plan, de la police et de l'état de l'imprimante. Dimensions par défaut : **480 × 440 px** ; dimensions minimales : **240 × 280 px**. |

Le nombre d'éléments détermine la répartition ; il n'est pas nécessaire de définir manuellement les positions X pour chaque cartouche. En cas d'espace restreint, les noms longs sont tronqués. Les noms complets et les valeurs sont affichés dans une info-bulle. À partir de la version **Studio 0.1.263**, seules les cartouches sélectionnées apparaissent dans les propriétés : pour 4 cartouches, les groupes **Cartouche 1–4** s'affichent ; pour 5, les groupes **Cartouche 1–5**. Les paramètres des cartouches masquées sont conservés et réapparaissent si le nombre total est augmenté.

## Photo personnalisée de l'imprimante et taille des cartouches {#eigenes-druckerfoto-und-patronengroße}

À partir de la version **Studio 0.1.262**, la section **Modèle d'imprimante et image** propose désormais un champ pour saisir un nom de modèle personnalisé, une option pour choisir entre **Graphique standard / Image personnalisée**, ainsi qu'un champ pour la **Photo de votre imprimante (URL ou chemin d'accès local /local/...)**. La saisie d'un chemin d'accès active automatiquement l'affichage de la photo personnalisée ; les URL d'images sans extension de fichier sont également prises en charge. Par ailleurs, la fonction **Importer une image** permet d'ajouter directement au projet un fichier au format PNG, JPEG, WebP, GIF ou SVG (jusqu'à 2 Mo). Les images importées sont intégrées au projet enregistré. Dans le cas d'URL ou de chemins d'accès de type `/local/...`, la source de l'image doit rester accessible lors de l'exécution (runtime).

La photo est ajustée proportionnellement. En l'absence d'image ou en cas d'erreur de chargement, le graphique standard s'affiche. L'état et les cartouches restent actifs, indépendamment de la photo ; l'animation des feuilles est associée au graphique standard. Le paramètre **Taille des cartouches** propose les options **Taille réelle / Demi-taille**, avec **Demi-taille** comme valeur par défaut. Seuls les éléments graphiques sont réduits ; les libellés et les pourcentages conservent leur taille d'origine. Ces paramètres sont disponibles même si le pack imprimante est déjà installé ; aucune réinstallation du pack n'est nécessaire.

## État et mesures {#status-und-messwerte}

La langue s'aligne automatiquement sur le paramètre du Studio (**DE/EN**), y compris par reprise automatique depuis Home Assistant. Il n'existe pas de sélection de langue spécifique au widget. Les états, indications et propriétés sont traduits ; en revanche, les libellés personnalisés, les noms de modèles et les messages propres à l'entité restent inchangés.

Les états « Prêt », « Impression », « Veille », « Avertissement », « Arrêté », « Hors ligne » et « Inconnu » sont détectés à partir des valeurs d'état courantes. Lors d'une impression, une feuille se déplace et le voyant LED clignote. L'option du navigateur relative à la « réduction des animations » permet de désactiver ces effets visuels. Les erreurs et les bourrages papier sont prioritaires ; un simple avertissement de niveau bas n'interrompt pas l'animation d'impression.

L'éditeur et l'environnement d'exécution (runtime) lisent les mêmes valeurs actuelles provenant de Home Assistant. Les niveaux manquants ou invalides s'affichent sous la forme **—** (et non 0 %). Les valeurs numériques valides sont limitées à une plage de **0 à 100 %**. Lorsque les valeurs sont inférieures ou égales au seuil d'avertissement, la cartouche concernée ainsi que sa valeur sont mises en évidence ; les noms correspondants s'affichent en dessous.

## Interface web {#weboberflache}

**URL de l'interface web (auto = depuis l'imprimante)** affiche un lien **Web ↗**. Une URL saisie manuellement est prioritaire. `auto` utilise la première adresse HTTP/HTTPS trouvée parmi `configuration_url`, `web_url`, `url`, `device_url` ou `printer_uri` de l'entité d'état. Si aucune adresse n'est présente, le lien reste masqué ; aucune recherche d'appareil n'est effectuée. Un champ vide entraîne également le masquage du lien. L'interface web s'ouvre dans un nouvel onglet.

## Contenu de cette version {#umfang-dieser-version}

Cette première version utilise des entités spécifiquement sélectionnées. Elle ne propose pas de recherche automatique d'appareils ou de cartouches, de gestion des pièces d'usure, de contrôle de prises électriques ni d'impression de test. Toutes les connexions sont en mode lecture seule. La carte originale, disponible séparément, offre des fonctionnalités supplémentaires.
