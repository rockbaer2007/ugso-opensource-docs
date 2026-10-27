---
title: Interface de gestion des paquets d'outils
description: Création et installation d'outils d'édition locaux pour l'interface graphique HA dans Visual Studio.
---

# Interface de gestion des paquets d'outils 0.1 {#tool-paket-schnittstelle-0-1}

À partir de la version **0.1.208**, si la confirmation des risques est omise lors d'un clic sur **Installer**, elle est mise en surbrillance en rouge et l'affichage défile automatiquement pour la rendre visible. Une fois la case cochée, la mise en surbrillance disparaît.

À partir de la version **0.1.207**, l'onglet s'ouvre automatiquement sur le catalogue fraîchement chargé, affichant l'état d'installation actuel. Après une suppression, un paquet publié dans le catalogue redevient disponible à l'installation, même s'il avait été installé localement auparavant. Les nouveaux paquets mis à disposition apparaissent lors de la prochaine ouverture.

Depuis la version **0.1.205**, les paquets du catalogue et les paquets d'outils installés localement s'affichent sous forme de **deux cartes côte à côte**, chacune accompagnée d'une icône. Si elle est disponible, l'icône propre au paquet installé est utilisée ; dans le cas contraire, une icône générique « boîte à outils » s'affiche. Les fonctions de mise à jour, de suppression et les actions propres aux outils restent disponibles.

Depuis la version **0.1.206**, la barre de sélection **Local / Catalogue / GitHub** reste visible en haut lors du défilement. L'ensemble du contenu de l'onglet partage **une zone de défilement unique** ; il n'y a plus de zones de défilement imbriquées pour le catalogue et les paquets installés.

À partir de la version Studio **0.1.204**, la section **Paramètres → Outils** propose les sources suivantes : **Local / Catalogue / GitHub**. Le catalogue affiche la licence, la description, la version de Studio requise ainsi que l'état de l'installation (y compris pour le sélecteur de couleurs et les outils de test). Pour GitHub, un lien public direct vers le fichier **`.tp`** est nécessaire. Une confirmation des risques est requise avant toute installation ; les téléchargements depuis le catalogue sont vérifiés via SHA-256 et l'identifiant/version du paquet sélectionné. La fenêtre des paramètres reste ouverte, tandis que la liste des paquets et la barre d'outils se mettent à jour instantanément. Une version plus récente d'un outil, choisie explicitement, peut remplacer la version existante ; les versions identiques ou antérieures sont refusées. Les projets et les favoris du sélecteur de couleurs sont conservés. L'outil d'empaquetage autonome (« Packer ») est disponible dans la section **Outils supplémentaires** sur la page web du catalogue.

Les paquets et outils complémentaires sont proposés de manière centralisée sur [visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=de). Ce site open source contient des descriptions et des instructions ; le téléchargement s'effectue via le catalogue de paquets.

Depuis la version Studio **0.1.89**, il est possible d'installer des paquets au format ZIP portant l'extension **`.tp`**. Les fichiers **`.tp.zip`** existants restent utilisables ; l'extension et le manifeste doivent correspondre au type de paquet d'outils.

Via **Paramètres → Outils**, vous pouvez installer un composant local de type `*.tp.zip`. Les outils installés apparaissent sous forme d'icônes réparties sur deux lignes dans la barre d'outils de l'éditeur ; l'icône en forme de mallette permet d'accéder directement à l'onglet de gestion des outils. Ces « packs d'outils » enrichissent l'éditeur, et non la palette de widgets ou l'environnement d'exécution (runtime). L'interface 0.1 prend en charge une action déclarative : la définition de la couleur d'arrière-plan de la page active. Un clic sur l'icône de l'outil — ou l'utilisation de la fonction **Exécuter** dans l'onglet des outils — affiche d'abord un aperçu ; la modification n'est réellement appliquée qu'après avoir cliqué sur **Appliquer**. Cette opération peut être annulée via la fonction **Annuler** et est enregistrée selon le processus habituel du projet. Aucune action n'est exécutée lors de l'installation.

## Sélecteur de couleurs (Colorpicker) UGSo 1.2.0 {#ugso-colorpicker-1-2-0}

À partir de la version **0.1.113** du Studio, le sélecteur de couleurs et la section des favoris conservent la même taille de fenêtre lors du passage d'un onglet à l'autre. Sur les écrans larges, les favoris s'affichent sur deux colonnes, tandis qu'ils n'en occupent qu'une seule sur les écrans plus étroits. Les listes longues peuvent être parcourues par défilement (scroll) au sein de l'onglet. Si l'outil est déjà installé, une simple mise à jour du Studio suffit.

**Mise à jour 1.2.0 (Studio 0.1.112) :** En plus de la fonction de copie, le sélecteur de couleurs propose désormais l'option **Enregistrer comme favori**. Le second onglet, intitulé **Favoris**, permet de stocker jusqu'à 15 couleurs, identifiées par leur code HEX et leur nom. Cette liste est automatiquement enregistrée au sein de l'add-on et, grâce à la fonctionnalité Ingress, elle est accessible aux administrateurs HA (Home Assistant) depuis plusieurs ordinateurs. Les utilisateurs standards peuvent utiliser le sélecteur de couleurs, mais n'ont pas accès aux favoris. Les couleurs en doublon n'occupent pas d'espace supplémentaire. Lorsque la liste est pleine, le message **Favoris pleins** s'affiche en jaune et l'option d'enregistrement est désactivée. Chaque entrée dispose d'un bouton permettant de copier sa valeur HEX (au format SVG) et d'une icône de corbeille pour la supprimer ; les éléments restants se décalent alors pour combler l'espace. Un clic sur une couleur l'applique dans le sélecteur de couleurs (Colorpicker). La liste partagée est rechargée lors de l'ouverture de l'onglet des favoris.

La fonction **Importer les favoris locaux** fusionne vos favoris existants (stockés dans le navigateur) avec la liste partagée. Les couleurs qui ne peuvent pas être intégrées à cette liste sont conservées localement. Une mise à jour ou une réinstallation de l'outil n'entraîne pas la suppression des favoris. Pensez à sauvegarder les données de l'extension avant toute désinstallation ou migration vers un autre serveur. Si la vérification des droits d'administration échoue, rouvrez Studio via Home Assistant ; dans ce cas, les favoris ne seront pas enregistrés localement en guise de solution de repli.

[Télécharger le sélecteur de couleurs (Colorpicker) 1.2.0](https://visualstudio.ugso-software.de/?kind=tool&lang=de).

Cet outil complémentaire nécessite **HA Grafik Visual Studio 0.1.112 ou une version ultérieure**. Installez le fichier `.tp` téléchargé via **Paramètres → Outils**. Si le sélecteur de couleurs est déjà installé, une simple mise à jour de Studio suffit pour accéder à la nouvelle interface. Le sélecteur de couleurs s'ouvre en cliquant sur l'icône en forme de cercle chromatique dans la barre d'outils ou en utilisant la commande **Exécuter**.

- Sélectionnez la teinte et la saturation sur le cercle chromatique ; réglez la luminosité séparément ou saisissez directement le code HEX.
- Choisissez **HEX** ou **Nom de couleur** comme sortie et cliquez sur **Copier**. Sans accès au presse-papiers du navigateur, sélectionnez le résultat et copiez-le manuellement.
- Les 31.918 noms de couleurs de [meodai/color-names](https://github.com/meodai/color-names) sont fournis localement ; aucun accès à Internet n’est nécessaire. Les correspondances exactes sont distinguées des correspondances les plus proches. La similarité est calculée par distance RGB.
- Les noms de couleurs sont des désignations, pas des valeurs de couleur CSS. Copiez le code HEX pour les champs de couleur des widgets.
- L’outil ne nécessite aucun droit sur le projet ou Home Assistant et ne modifie aucune donnée du projet. Sur le cercle chromatique, les flèches gauche/droite changent la teinte et les flèches haut/bas la saturation.

La nouvelle action déclarative `color-picker` utilise `capabilities: []`. La boîte de dialogue et la liste des noms de couleurs font partie de la version « Studio » ; le paquet de données seul active l'outil. Les anciennes versions « Studio » ne prennent pas en charge cette action. La licence et les mentions relatives aux sources sont accessibles via la boîte de dialogue. L'action existante `set-page-background` demeure inchangée.

## Construction du paquet {#paket-aufbauen}

Le fichier ZIP contient `manifest.json` (encodé en UTF-8) ainsi que, le cas échéant, des images SVG ou PNG référencées sous `icons/`. Aucun autre type de fichier n'est autorisé. L'identifiant du paquet est structuré avec des points ; l'identifiant de l'outil s'inscrit dans l'espace de nommage du paquet. La version du paquet suit le format `x.y.z`. Un paquet d'outils contient exactement un seul outil.

```json
{
  "format": "ha-grafik-tool-package",
  "apiVersion": "0.1",
  "id": "beispiel.tools",
  "name": "Beispiel Tools",
  "version": "1.0.0",
  "license": "MIT",
  "tools": [{
    "id": "beispiel.tools/background",
    "definitionVersion": "0.1",
    "label": "Seitenfarbe",
    "description": "Setzt die Farbe der aktuellen Seite.",
    "context": "page",
    "capabilities": ["project.read", "project.write"],
    "action": { "kind": "set-page-background", "defaultColor": "#224466" }
  }]
}
```

`defaultColor` est un code couleur hexadécimal à six caractères ; il peut être modifié dans la prévisualisation. Les fonctionnalités mentionnées ne s'appliquent qu'à cette action spécifique validée dans l'éditeur. Elles ne confèrent pas au code du paquet une autorisation générale d'écriture. Le paquet ou l'outil peut, en option, faire référence à une image via `"icon": "icons/name.svg"` ou `.png`. Le fichier doit être inclus dans l'archive ZIP ; les boutons d'action du Studio continuent d'utiliser des icônes au format SVG.

L'archive ZIP ne doit pas dépasser 2 Mo, le manifeste 200 Ko et chaque image 50 Ko. Les images PNG sont limitées à 1024 × 1024 pixels ; les fichiers SVG sont soumis à une vérification visant à détecter tout contenu passif.

## Installation et gestion {#installieren-und-verwalten}

1. Créez, par exemple, un élément `seitenfarbe.tp` incluant `manifest.json` ainsi que les images référencées, le cas échéant. L'utilisation de `seitenfarbe.tp.zip` reste également prise en charge.
2. Sélectionnez le fichier sous **Paramètres → Outils**. La liste affiche l'identifiant du paquet, sa version, sa licence et l'outil qu'il contient.
3. Ouvrez la prévisualisation de l'outil — soit via son icône dans la barre d'outils de l'éditeur, soit en utilisant la fonction **Exécuter** dans l'onglet « Outils » — puis validez la modification de page souhaitée en cliquant sur **Appliquer**.

Les paquets peuvent être supprimés dans l'onglet « Outils » (Tool-Tab). Les scripts personnalisés, les services Home Assistant, les URL externes, l'installation depuis GitHub et les mises à jour ne font pas encore partie de 0.1. Les règles de compatibilité et d'extension prévues sont détaillées dans les [règles relatives aux outils, disponibles dans le code source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/tool-rules.md).
