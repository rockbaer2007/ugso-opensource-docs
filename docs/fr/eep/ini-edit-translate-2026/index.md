---
title: INI Edit Translate 2026
description: Fonctions de l’éditeur Windows de fichiers INI de modèles EEP et d’Installation.eep avec traduction ChatGPT.
---

# INI Edit Translate 2026

## Version 2.1.54 : abréviations ferroviaires dans Info_trans

Info_trans ajoute l’onglet **Abréviations ferroviaires** avec 14 entrées :
Bf, Hbf, Hp, Gbf, Rbf, Abzw, BÜ, Stw, EG, OL, Gl., Bstg., DWW et Kr.
Le tableau présente l’allemand, l’anglais, le français et le polonais, avec les
abréviations étrangères attestées. La ligne Kr., auparavant vide, est complétée
pour une traversée de voies. Cliquer sur une cellule copie son contenu, comme
dans les autres tableaux de référence. Le tableau est en lecture seule, les colonnes
peuvent être triées et les textes longs passent à la ligne.
L’onglet allemand s’appelle **Bahnabkürzung**, l’anglais **Railway abbreviations**.
Le tableau est intégré dans Info_trans. Un fichier externe existant
`help/railway-abbreviations.csv` reste utilisable. Ce tableau de référence
ne modifie pas les règles de traduction automatique. Sauvegarde effectuée avant
modification ; dictionnaire, base de données, paramètres, identifiants d’accès et
liste externe des constructeurs sont conservés.
Le ZIP de mise à jour utilise uniquement les chemins acceptés par le programme
de mise à jour 2.1.53. Téléchargement et validation sont distincts ; 100 % n’est affiché
qu’après validation. Les détails d’erreur sont visibles et une nouvelle tentative est possible.
Les deux projets conservent .NET Framework 4.8 et utilisent son concepteur Visual Studio
hors processus. Info_trans référence explicitement System.Configuration.
Recharger la solution après modification. Compilation de conception et chargement
WinForms DesignSurface vérifiés ; Visual Studio lui-même n’a pas été piloté à distance.

114 vérifications locales réussies : contenu du tableau et affichage DE/EN/FR
aux échelles 100 et 150 %, sans appel réel aux API.


## Version 2.1.53 : abréviations ferroviaires et codes de constructeurs

20 abréviations ferroviaires utilisent désormais une correspondance locale fixe
dans les noms de modèles et les textes traduits par le fournisseur choisi.
EW signifie aiguillage simple, sans exiger un angle après le code.
Par exemple, `GK3 DKW DR DB (V8)[e]EEP16.2` devient
`GK3 TJD DR DB (V8)[e]EEP16.2` en français.

La liste initiale fournie contient 272 codes de constructeurs uniques de trois caractères.
Le premier démarrage crée un fichier UTF-8 externe :
`%LOCALAPPDATA%\UGSo\IET2026\constructor-codes.txt`.
Ajouter les nouveaux codes de deux lettres et un chiffre, un par ligne, puis redémarrer.
Les mises à jour n’écrasent jamais ce fichier personnel. Les ajouts sont fusionnés
avec la liste de base. Lignes vides, commentaires et entrées invalides sont ignorés.
Un fichier illisible est conservé et la liste de base sert de solution de repli. Les codes sont conservés partout, avec ou sans parenthèses.
La reconnaissance générale des autres codes reste active. DR, DB, types,
indications de version comme `(V8)` ou `(v8.2)`, versions EEP et `[e]` restent inchangés.

| DE | EN | FR | PL |
| --- | --- | --- | --- |
| DKW | DSS | TJD | Rkpd |
| EKW | SS | TJS | Rkp |
| EW | single turnout | BS | Rz |
| ABW | contrary-flexure turnout | ABW* | Rłd |
| IBW | similar-flexure turnout | IBW* | Rłj |
| BW | locomotive depot | dépôt de locomotives | lokomotywownia |
| Bf | station | gare | stacja |
| Hbf | main station | gare principale | dworzec główny |
| Hp | halt | halte ferroviaire | przystanek osobowy |
| Gbf | freight station | gare de marchandises | stacja towarowa |
| Rbf | marshalling yard | gare de triage | stacja rozrządowa |
| Abzw | junction | bifurcation | posterunek odgałęźny |
| BÜ | level crossing | passage à niveau | przejazd kolejowo-drogowy |
| Stw | signal box | poste d’aiguillage | nastawnia |
| EG | station building | bâtiment voyageurs | budynek dworca |
| OL | overhead line equipment | caténaire | sieć trakcyjna |
| Gl. | track | voie | tor |
| Bstg. | platform | quai | peron |
| DWW | three-way turnout | branchement à trois voies | rozjazd potrójny |
| Kr. | diamond crossing | traversée de voies | skrzyżowanie torów |

*En français, ABW/IBW sont conservés en attendant une validation terminologique.
Les autres entrées utilisent des abréviations attestées ou des traductions en toutes
lettres, sans prétendre à une norme universelle.
Autres abréviations reconnues en entrée : DS/DSS/SS, TJD/TJS/BS, Rkpd/Rkp/Rz/Rłd/Rłj,
PO, Jn, PODG, LC, PN, BV et OLE. Le polonais ambigu ST/St n’est pas converti.
Hp désigne ici une halte ferroviaire et Kr. une traversée de voies.
Les types techniques `Hp0`, `DKW190` et identifiants comme `DKW_190` ne sont pas découpés.

Les termes vérifiés sont remplacés temporairement par des marqueurs protégés pour
la traduction en ligne, puis rétablis dans la langue cible après validation,
y compris lorsque l’anglais sert de langue intermédiaire. Une erreur ou un marqueur
modifié empêche toute application partielle. Fichiers originaux, paramètres et
identifiants d’accès sont conservés. Sauvegarde effectuée avant modification.
MyMemory reste le choix par défaut des nouvelles configurations.

111 vérifications locales réussies : tous les 272 codes, DE/EN/FR/PL,
import/enregistrement/relecture, versions et erreurs, sans appel réel aux API.
Le ZIP complet inclut `docs/railway-glossary.md` et `docs/constructor-codes.txt`.


## Version 2.1.52 : mots descriptifs dans les noms de modèles

Les mots descriptifs sont désormais traduits dans les noms de modèles, même si leur
description est vide. « Haus Helios Typ4 UD1 » devient **House / Maison / Dom Helios Typ4 UD1**.

La traduction des noms utilise une liste locale limitée de mots vérifiés pour protéger
les noms propres. Les mots inconnus et éléments de noms sont conservés sans être
envoyés à un service en ligne pour traduire le nom. Ce n’est pas une reconnaissance
générale automatique des noms propres : les autres mots descriptifs doivent être
ajoutés après vérification. Les noms existants sans mot descriptif reconnu ne sont
pas écrasés. Types, codes de constructeurs, versions EEP, `[e]`, séparateurs et
écriture des éléments protégés sont conservés. Les abréviations ferroviaires encore
en cours de collecte ne sont pas ajoutées dans cette modification.

Les descriptions utilisent toujours le fournisseur choisi. Noms et descriptions ne
sont appliqués ensemble qu’après réussite ; une erreur conserve les contenus existants.
Le bouton indépendant du fournisseur s’appelle **Traduire les textes**.

**MyMemory/translated.net est le choix par défaut des nouvelles configurations.**
Les choix, clés API, comptes et modèles déjà enregistrés sont conservés.
Pour changer volontairement : **À propos → Paramètres → Paramètres de traduction → MyMemory → Enregistrer**.

105 vérifications locales réussies : DE/EN/FR/PL, descriptions vides, protection des
noms et codes, erreurs, enregistrement et relecture. Sauvegarde effectuée ;
fichiers originaux et identifiants conservés.

## Version 2.1.51 : message lors de la sélection d’un dossier

Sélectionner un dossier dans l’arborescence affiche **« Veuillez sélectionner un fichier INI. »**
Les textes, tableaux, aperçu et fichier sélectionné sont conservés.
Un dossier n’est plus lu comme un fichier et aucune traduction n’est lancée.

Cela concerne le dossier racine et les sous-dossiers de tout nom, y compris ceux
portant une extension `.ini`. Les fichiers disparus et autres types de fichiers
affichent le même message. Seul un fichier INI existant est ouvert ; `.INI` en
majuscules est également reconnu. Le nœud sélectionné remplace la position du pointeur,
y compris pour la navigation au clavier. Message disponible en allemand, anglais et français.

101 vérifications locales réussies, dont conservation des données lors de la sélection
d’un dossier dans les trois langues et ouverture d’un INI sans dépendre du pointeur.
Sauvegarde effectuée ; données personnelles et identifiants conservés.

## Version 2.1.50 : protéger les contrôles EEP, identifiants et versions

`[e]` reste un code de saut de ligne EEP : il n’est ni traduit ni remplacé par un vrai
saut de ligne. L’écriture exacte, le nombre et l’ordre des marqueurs protégés sont vérifiés.

Les identifiants de constructeurs sont reconnus par des motifs lettres/chiffres, sans
liste de noms fixe : `(GK3)`, `(AG3)`, `(DL1)`, mais aussi les anciens codes sans
parenthèses au début, au milieu ou à la fin. Aucun code n’est ajouté s’il est absent.
Les ajouts ordinaires tels que `(Winter)` restent traduisibles. Sans liste supplémentaire,
les codes particuliers composés uniquement de lettres ne peuvent pas être distingués
de façon fiable des mots ordinaires.

Les versions comme `EEP16.2`, `eep16.2` et `EEP 16.2` gardent leur casse et ponctuation.
MyMemory ne reçoit pas les segments protégés ; les codes ou contrôles modifiés ou
inventés par OpenAI/ChatGPT sont rejetés. La protection par restauration reste active.

Une entrée de configuration ajoutée en 2.1.49 pouvait empêcher le démarrage.
Elle est corrigée et la configuration distribuée est désormais vérifiée.
**Si 2.1.49 ne démarre plus :** sauvegarder `INI Edit Translate 2026.exe.config`,
télécharger le fichier de configuration supplémentaire de la version 2.1.50,
le renommer `INI Edit Translate 2026.exe.config` et remplacer celui situé à côté
de l’EXE. Démarrer puis installer normalement la mise à jour 2.1.50.
Ne pas remplacer les fichiers INI, bases de données ou paramètres personnels.

99 vérifications locales réussies. Un test d’installation avec code initial, version,
code entre parenthèses et deux contrôles `[e]` a réellement été traduit via MyMemory,
enregistré et relu. Fichiers originaux et identifiants conservés.

## Version 2.1.49 : conserver le dernier dossier

Activer **Conserver le dernier dossier** dans **À propos → Paramètres**, puis
**Enregistrer**. Le dernier dossier choisi est conservé après redémarrage et mise à jour.
L’arborescence et les sélecteurs de fichiers INI / Installation.eep repartent de ce dossier.
Aucun fichier n’est ouvert ni traduit automatiquement.

L’option est désactivée par défaut. Si un dossier ou lecteur réseau est indisponible,
un message apparaît et le chemin est conservé pour le prochain démarrage. Les données
et identifiants existants sont conservés. 94 vérifications locales réussies, dont
enregistrement/relecture, désactivation, dossier indisponible et affichage DE/EN/FR
aux échelles 100/150 %.

**Version 2.1.54.0 · Windows 11 · .NET Framework 4.8**

Modifier les descriptions de modèles EEP et leurs fichiers d’installation. Développé
par Uwe Grimm / UGSo Software et publié sous licence MIT.

[Code source et README sur GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Interface de la version 2.1.37 avec barre de menus Lime, sans données personnelles](/eep/ini-edit-translate-2026/editor-v2-1-37-fr.png)

## Version 2.1.48 : rétablir la traduction des noms de sous-ensembles

Les noms et descriptions des cinq sous-ensembles `Install_00` à `Install_04` sont
de nouveau traduits. Seuls les noms de modèles dans la section des modèles restent
protégés. Les textes sources sont conservés ; l’allemand et le français utilisent
toujours l’anglais comme langue intermédiaire.

Les cinq boutons et l’importation automatique utilisent la même correspondance
vérifiée des champs. Le bouton du deuxième sous-ensemble traite désormais ses propres
champs. Les résultats ne sont appliqués qu’après traduction complète ; une erreur
ou une annulation conserve les noms et descriptions du sous-ensemble.

91 vérifications locales réussies. Un sous-ensemble de test nommé « Detailmodell
Großdiesellokomotive V140 001 DRG » a réellement été traduit via MyMemory, enregistré
et relu ; les noms de modèles et un champ INI supplémentaire ont été conservés.
Le fichier de l’ordinateur de jeu distant n’a pas été modifié.

## Téléchargement

[Télécharger le ZIP Windows v2.1.54](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/download/v2.1.54/INI-Edit-Translate-2026-v2.1.54-windows.zip) · [Version GitHub et SHA-256](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/tag/v2.1.54)

Extraire tout le ZIP et lancer `INI Edit Translate 2026.exe`. Windows 11 et
.NET Framework 4.8 sont requis. Conserver les DLL et dossiers de langues ensemble.
Visual Studio sert uniquement à compiler les sources. Aucun installateur nécessaire.

## Fonctions

| Domaine | Possibilités |
| --- | --- |
| Textes de modèles | Modifier les noms et descriptions en EN/DE/FR/PL |
| Métadonnées | Modifier les références PDF, génération, années d’utilisation, pays et icône |
| Axes de mouvement et fonctions des signaux | Afficher, modifier et traduire les entrées par langue |
| Installation.eep | Modifier les noms et descriptions des sections d’installation prises en charge |
| Aperçu | Comparer le fichier original à l’aperçu du résultat |
| Export des tableaux | Export complet en UTF-8 avec BOM et séparateurs de tabulation |
| Sauvegardes | Copier les fichiers INI existants avant remplacement, en conservant leur nom d’origine |

## Fournisseurs de traduction

Dans **Options → Paramètres de traduction**, choisir API OpenAI, abonnement ChatGPT ou
**MyMemory**. MyMemory nécessite Internet, mais aucune clé ni aucun compte.
Une adresse e-mail facultative est envoyée avec chaque requête : selon le fournisseur,
5 000 caractères par jour sans identification, jusqu’à 50 000 avec une adresse valide.
Chaque langue cible compte séparément. Les textes longs sont découpés en segments de
500 octets UTF-8 maximum. Un cache temporaire évite les répétitions pendant une opération.

L’allemand est la langue par défaut. La langue choisie pour l’interface définit la langue
source initiale ; les axes/fonctions des signaux gardent leur sélecteur de source.
L’allemand et le français sont d’abord traduits en anglais ; les autres langues cibles
utilisent ce texte intermédiaire anglais. Cela vaut pour tous les fournisseurs.
Le texte source choisi et les noms de modèles sont conservés.

MyMemory peut conserver durablement les textes transmis. L’application utilise uniquement
la requête de traduction et ne publie pas d’entrées supplémentaires dans un dictionnaire.
Aucun changement automatique de fournisseur. Les clés API, connexions ChatGPT, modèles
et dictionnaires existants sont conservés. L’enregistrement INI préserve les caractères
polonais grâce à Unicode ; si nécessaire, le fichier de sortie sauvegardé est enregistré
en UTF-16 avec BOM. Le traitement réel de cet encodage dans EEP n’a pas été testé ici.

90 vérifications locales ont réussi. Le fichier INI fourni a été ouvert, traduit par de
véritables appels MyMemory et enregistré dans une copie ; l’original reste inchangé.
Relire les traductions automatiques des termes techniques avant utilisation.

[API MyMemory](https://mymemory.translated.net/doc/spec.php) ·
[Quotas](https://mymemory.translated.net/doc/usagelimits.php) ·
[Utilisation des données](https://mymemory.translated.net/terms-and-conditions)

## Installation et utilisation

1. Télécharger le ZIP Windows ci-dessus et extraire tous les fichiers.
2. Lancer `INI Edit Translate 2026.exe` depuis le dossier extrait en conservant ses DLL et dossiers de langues.
3. Ouvrir **À propos → Paramètres → Paramètres de traduction**. Choisir MyMemory, API OpenAI ou abonnement ChatGPT. MyMemory ne nécessite pas de connexion ; l’e-mail est facultatif.
4. Ouvrir d’abord une copie sauvegardée en mode **Lecture seule**.
5. Utiliser **Lire et traduire** ou un bouton de traduction. Choisir la langue source des axes et fonctions des signaux.
6. Vérifier l’aperçu et les textes, puis enregistrer explicitement.

La fenêtre d’information choisit l’aide révisée `Info.de.rtf`, `Info.en.rtf` ou `Info.fr.rtf` selon la langue de l’interface. Le fichier historique `Info.rtf` est conservé sans modification. L’aide actuelle décrit OpenAI et le programme de référence restauré.

## Mises à jour GitHub

Choisir **À propos → Rechercher des mises à jour** pour consulter la dernière version
publique sur GitHub. Aucune vérification automatique au démarrage. Seule une version
stable plus récente est proposée, avec son numéro et ses notes de publication.

**Télécharger et installer** récupère le ZIP Windows et sa somme SHA-256.
Le téléchargement et la vérification peuvent être annulés avant la fermeture du programme.
Enregistrer les fichiers ouverts et fermer Info_trans avant l’installation, puis confirmer.
Un programme auxiliaire attend la fermeture de l’éditeur, sauvegarde les fichiers existants
et installe le paquet.

Les paramètres et la clé OpenAI chiffrée sont conservés. Les fichiers FDB, CSV, DAT et
de configuration existants de l’aide, ainsi que l’Info.rtf d’origine, sont sauvegardés
sans être remplacés. Les fichiers de modèles restent intacts. En cas d’échec, le programme
tente de restaurer les fichiers déjà remplacés et consigne le résultat. Sauvegardes et
rapports : `%LOCALAPPDATA%/UGSo/IET2026/updates/<identifiant>/`.

Aucun identifiant de serveur nécessaire. Les sommes de contrôle vérifient l’intégrité ;
aucune signature numérique de paquet supplémentaire n’est implémentée.
36 tests isolés couvrent le téléchargement, l’annulation, les chemins, la conservation
des données, les fichiers verrouillés et la restauration après une écriture partielle.

### Correction du programme de mise à jour 2.1.48

Le transfert utilise désormais un handle de processus Windows stable au lieu de
lire les modules de l’éditeur en cours de fermeture. Quatre tests supplémentaires
couvrent x86/x64, les processus terminés, les identités incorrectes et les délais
d’attente. Si l’ancien programme 2.1.37 échoue avant l’installation, extraire
d’abord le ZIP 2.1.48 complet dans un nouveau dossier. Sauvegarder ses données et
ne pas remplacer les bases et dictionnaires existants par ceux du paquet.

Le parcours complet de la version publiée 2.1.37 vers 2.1.48 a réussi sur une
copie de test sauvegardée : téléchargement GitHub, installation et redémarrage
automatique. Les 32 valeurs de configuration précédentes, 17 fichiers de données
et de modèles contrôlés et 18 configurations utilisateur existantes ont été
conservés. Une clé de test DPAPI synthétique est restée identique et déchiffrable ;
l’état initial sans clé a ensuite été rétabli. Aucun appel OpenAI n’a été effectué.
Le redémarrage a été confirmé par l’identifiant du processus, les versions, les
empreintes et la configuration ; la capture de fenêtre Windows a échoué ensuite.
Un nouveau test du dialogue GitHub en lecture seule a bien détecté 2.1.48.

## Second programme : Info_trans

Le paquet contient aussi `help/Info_trans.exe`. **Aide de référence** dans
l’éditeur ouvre ce programme dans la langue choisie. La véritable `IET2.FDB`
et son moteur natif Firebird 2.5.8 ont été récupérés dans l’archive de 2019.
Aucune installation séparée d’un serveur Firebird n’est nécessaire.

La base contient 5 entrées de bâtiments, 2 de marchandises et 2 de mises à jour.
Les tables des signaux, matériel roulant, objets de voie et paysage sont vides
dans l’original. Sont aussi inclus : 236 entrées d’icônes, 369 termes techniques
et 2 428 entrées corrigées dans le **dictionnaire DE/EN/FR**. L'anglais est la
référence ; les corrections allemandes confirmées et les traductions françaises
sont intégrées. Les fragments ont été réunis et les termes mélangés séparés.
Les variantes américaines et britanniques conservent leurs indications.
Toutes les questions de vérification du dictionnaire sont résolues. Le fichier
DE/EN original et la base source restent inchangés dans le paquet complet.

![Info_trans 2.1.37 avec onglets Lime et base d'origine chargée](/eep/ini-edit-translate-2026/info-trans-v2-1-37-fr.png)

![Dictionnaire trilingue Info_trans avec colonnes allemandes, anglaises et françaises lisibles](/eep/ini-edit-translate-2026/dictionary-v2-1-37-fr.png)

`Info_trans` est compilé pour x86, comme les DLL natives. Le fournisseur géré
FirebirdSql.Data.FirebirdClient 7.5.0.0 a été vérifié avec la vraie base Firebird 2.5.8.
Les tests lisent des copies séparées et comparent les sept tables avec l’interface
DE/EN/FR. Le paquet contient la base source inchangée.

Les composants absents ou illisibles sont signalés ; l’import SQL est alors
désactivé. Une sauvegarde locale précède tout import SQL manuel disponible.
La mise à jour automatique du programme reste désactivée.

## Données et confidentialité

Les anciennes inscriptions et bases personnelles ne sont pas importées. Les paramètres
sont séparés par utilisateur Windows. La configuration OpenAI et les sauvegardes sont
conservées sous `%LOCALAPPDATA%/UGSo/IET2026/`.

Windows DPAPI chiffre la clé API pour le compte Windows actuel. Les textes sélectionnés
sont envoyés à OpenAI avec `store: false`. Internet et une facturation API distincte sont
nécessaires ; un abonnement ChatGPT ne remplace pas cette facturation.

## Mise à jour et vérifications

**Les mises à jour GitHub sont lancées manuellement et leur installation doit être confirmée.** L’ancien serveur n’est pas utilisé. Google, LEO, Linguee et DeepL ne sont plus proposés.

41 contrôles locaux avec réponses API simulées et les compilations Debug/Release
vérifient les erreurs, l’annulation, la restauration, l’export et les interfaces rendues
DE/EN/FR. Aucun texte n’est envoyé à OpenAI pendant les tests. Un appel API réel et la
qualité des traductions produites restent à vérifier avec son propre compte.
Tous les schémas INI possibles ne sont pas pris en charge ; vérifier les données obtenues.

Le paquet local complet 2.1.37 a été contrôlé par l'utilisateur, qui a confirmé son
bon fonctionnement avant publication. Le ZIP contient les deux programmes, le
moteur Firebird natif, la base originale et le dictionnaire corrigé. L'intégrité
du ZIP et son SHA-256 ont été vérifiés ; les sept tables de la base ont été
comparées aux interfaces DE/EN/FR sur des copies séparées. Les captures montrent
le nouveau design avec des données neutres, sans paramètres privés.
