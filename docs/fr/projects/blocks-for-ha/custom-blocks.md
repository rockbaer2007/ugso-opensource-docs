---
title: Blocs et modèles personnalisés
---

# Blocs et modèles personnalisés

Le bouton **Block-/Template-Editor** ouvre un éditeur occupant environ **95 % de la largeur et de la hauteur** de l’écran. Il crée plusieurs blocs dans un paquet, avec aperçu Blockly et sorties HA/Jinja. Les définitions sont déclaratives ; aucun générateur JavaScript importé n’est exécuté.

## Créer un paquet

1. Renseigner ID, version, nom, auteur, licence et description du paquet.
2. Ajouter les blocs puis choisir valeur, condition, action ou déclencheur.
3. Déclarer les champs : texte, nombre, case à cocher ou entité, et les entrées de valeurs typées.
4. Renseigner le modèle de sortie : expression Jinja pour une valeur/condition, structure YAML native pour une action/déclencheur.
5. Vérifier l’aperçu et les diagnostics ; appliquer le paquet.

Les blocs appliqués apparaissent dans **Personnalisés**, avant la recherche. Les IDs techniques sont placés dans un espace de noms propre au paquet. Les noms de champs, variables et IDs ne sont pas traduits. Les libellés des paquets restent dans la langue de leur auteur.

## Copier, télécharger et importer

**JSON prüfen** vérifie le JSON collé. **ZIP einlesen** lit l’archive du même format. Après vérification, **Übernehmen** installe le paquet localement. JSON et ZIP contiennent la même définition ; ils ne doivent pas contenir du code exécutable arbitraire.

Les projets de format 3 incluent les définitions des paquets utilisés pour permettre la restauration sur un autre navigateur. Les paquets installés sont également conservés localement. Les collisions de types et imports invalides sont refusés ; le contrôle préalable évite une installation partielle.

Pour publier, fournir nom, description, auteur, licence, version et image, avec du JSON copiable et des téléchargements JSON/ZIP. Aucune publication automatique depuis l’éditeur. [Catalogue des paquets](./catalog/).

## Limites

Le JSON de définition produit par le [Blockly Developer Tools](https://docs.blockly.com/guides/create-custom-blocks/blockly-developer-tools/) décrit la forme d’un bloc, mais ne suffit pas à produire une automatisation HA. Il faut un modèle de sortie et un schéma de paquet vérifiable. Les générateurs Python, PHP, JavaScript, Lua et Dart du Block Factory ne sont pas les générateurs HA/Jinja de ce projet.

Les menus déroulants personnalisés, champs variable/image, conteneurs d’instructions, mutateurs et entrées dynamiques supplémentaires restent des pistes d’évolution. Les références à des blocs inconnus et les sorties non représentables sont refusées.

Le [paquet capteur et lampe](./catalog/sensor-light) illustre une valeur de capteur, une condition de seuil et une action de luminosité. Tester les résultats et remplacer les entités avant utilisation dans HA.

:::: details Référence détaillée issue de la documentation allemande

## Blocs personnalisés et paquets de modèles (templates) {#eigene-blocks-und-template-pakete}

Depuis la version **0.1.18**, l'**éditeur de blocs/modèles** (Block-/Template-Editor) ouvre, à côté du nom de l'automatisation, une fenêtre occupant 95 % de la largeur et de la hauteur de l'écran. Sur les appareils mobiles, elle occupe 98 % de l'espace et dispose d'un défilement interne. Des champs permettent de configurer le bloc ; sur la droite s'affichent un aperçu Blockly, le résultat HA (Home Assistant) avec des exemples de valeurs, ainsi qu'un code JSON du paquet pouvant être copié.

### Création et application {#erstellen-und-ubernehmen}

1. Saisissez l'identifiant du paquet, la version, le nom, l'auteur, la licence et la description, ou sélectionnez **Charger un exemple**.
2. Ajoutez un ou plusieurs blocs : **Valeur/Jinja**, **Condition/Jinja**, **Action/HA-YAML** ou **Déclencheur/HA-YAML**.
3. Créez des champs (pour du texte, des nombres, des booléens ou des entités) ainsi que des entrées de valeur (pour des nombres, des chaînes de caractères, des booléens ou des valeurs génériques).
4. Saisissez l'expression Jinja ou le mappage déclaratif HA, puis vérifiez l'aperçu.
5. Cliquez sur **Appliquer** pour installer le paquet localement. Ses blocs seront alors disponibles dans la section **Personnalisé** (Benutzerdefiniert), juste avant la barre de recherche.

Les expressions Jinja doivent être saisies sans les doubles accolades de modèle. Les espaces réservés (placeholders), tels que `${ENTITY}`, font référence aux noms des champs ou des entrées. Les champs sont insérés en respectant leur type, tandis que les entrées de valeur sont intégrées sous forme d'expressions entre accolades. Le mappage HA utilise des valeurs JSON complètes, comme `{"$field":"ENTITY"}` ou `{"$input":"VALUE"}`. L'[exemple « Capteur et lumière »](/fr/projects/blocks-for-ha/catalog/sensor-light) illustre l'ensemble de ces mappages.

### Deux méthodes d'importation et publication {#zwei-importwege-und-veroffentlichung}

- **Insérer le code :** Collez le JSON du paquet dans la section « Importer du code JSON ou un fichier ZIP », **vérifiez le JSON**, consultez l'aperçu, puis **validez**.
- **Charger un fichier ZIP :** Sélectionnez le fichier du paquet, consultez l'aperçu, puis **validez**.

Les options **Télécharger le JSON**, **Copier le code** et **Télécharger le catalogue (ZIP)** permettent toutes d'exporter le même paquet. Le fichier ZIP contient `block-package.json` et `README.md`. Les pages open source présentent les paquets et proposent du code ainsi que des téléchargements ; le [catalogue](https://visualstudio.ugso-software.de/blocks), quant à lui, dispose de sa propre page dédiée aux paquets de blocs. Les nouvelles publications sont examinées manuellement ; l'éditeur ne procède à aucun téléversement automatique. [Catalogue et exemple](/fr/projects/blocks-for-ha/catalog/).

### Stockage et conflits {#speicherung-und-konflikte}

Format de paquet : `ugso-ha-block-package`, `schemaVersion: 1` ; les identifiants de paquets ou de blocs sont composés de lettres minuscules, de chiffres et de traits de soulignement simples. Les paquets installés restent stockés dans le navigateur. Le format de projet **3** intègre les paquets utilisés ainsi que leurs dépendances. Les formats de projet 1 et 2 restent lisibles. En cas d'échec lors de l'importation d'un projet, aucune nouvelle définition de paquet n'est installée.

Des paquets identiques peuvent être réimportés. Un identifiant de paquet (ID) existant associé à un contenu ou une version différente sera rejeté. Pour créer une variante personnalisée, utilisez un nouvel identifiant de paquet ; les mises à jour automatiques et la désinstallation seront implémentées ultérieurement. Les dépendances doivent être présentes dans la version exacte requise, ou être incluses dans le projet. Les dépendances cycliques sont rejetées.

Limites : 16 paquets installés, 32 blocs par paquet, 12 champs et 8 entrées de valeur par bloc ; le fichier JSON ne doit pas dépasser 500.000 caractères, et le fichier ZIP ne doit pas excéder 1 Mo (compressé ou décompressé). Les fichiers ZIP ne peuvent contenir que les deux fichiers spécifiés.

### Limites de la première version de l'éditeur {#grenzen-des-ersten-editors}

L'éditeur est une interface dédiée, conçue pour HA (Home Assistant) et dotée d'un aperçu Blockly. L'outil original [Blockly Block Factory](https://docs.blockly.com/guides/create-custom-blocks/blockly-developer-tools/) n'est pas encore intégré. Le code JSON brut des blocs généré par cet outil ne contient, en soi, aucune fonctionnalité HA et ne constitue pas un paquet UGSo importable. Les générateurs de code (JavaScript, Python, PHP, Lua, Dart) ne sont ni importés ni exécutés.

Les menus déroulants, champs de variables, images, conteneurs d'instructions, « mutateurs » et connecteurs dynamiques ne sont pas encore disponibles dans l'éditeur (ils figurent sur la feuille de route). Les entrées de valeur font l'objet d'une vérification de type ; les blocs existants qui ne comportent que des champs numériques fixes ne peuvent pas accepter de valeurs numériques dynamiques.

L'aperçu vérifie la structure du paquet et les structures HA prises en charge, mais n'exécute pas le code Jinja. Les propriétés des appareils et les plages de paramètres valides doivent être vérifiées au sein de HA ; les champs numériques ne permettent pas, pour l'instant, de définir librement des limites minimales ou maximales. L'éditeur n'exécute aucune action HA. L'exportation au format YAML génère des structures natives HA ; Lors de la réimportation YAML, la représentation native correspondante est générée. Les formes de blocs personnalisées initiales sont préservées grâce au fichier de projet JSON.

::::
