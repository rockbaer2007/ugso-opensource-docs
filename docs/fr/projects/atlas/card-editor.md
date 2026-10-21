---
title: Home Assistant Card Editor
description: "Guide de l’éditeur Expert ATLAS : connexion, palette, conteneurs, import, export et styles Tabbed Card V2."
---

# Home Assistant Card Editor

::: info Brouillons par onglet après import de fichier – App 0.1.331
Un **Importer** JSON de configuration complète confirmé sauvegarde aussi le projet
Editor comme brouillon local distinct par onglet, sans projet partagé préalable.
Un autre import dans le même onglet crée une nouvelle source et garde la précédente.
Les modifications ordinaires ne mettent ensuite à jour que le nouveau brouillon.
La reprise des réglages du premier import dans un espace normal reste conservée.

**Après recharge, vérifier le Brouillon local présélectionné puis Sauvegarder et
reprendre.** L’espace global du profil peut encore montrer le dernier import ;
il ne remplace pas la source propre à l’onglet, dont la reprise reste explicite.
Aucune application automatique ni donnée d’authentification dans les brouillons.
Stockage local plein ou session bloquée gardent leurs messages distincts et le
conseil d’export. Conserver aussi les fichiers sources.

Cela corrige le défaut 0.1.330 du nouveau profil : aucune source par onglet n’était
créée, et les deux affichaient seulement le dernier import après recharge.
Ce correctif concerne l’import JSON complet, pas une nouvelle qualification HACS.

Mise à jour et qualification native sur .68 avec HA 2026.10.2 réussies : fichiers
originaux en défaut, ordre inverse, même fichier répété, présélection propre après
recharge et reprises complètes. Annulation et fichier invalide ne modifient ni
espace ni sources. Écritures locales/de session bloquées affichent les bons
messages ; export et nouveaux essais conservent les versions précédentes. Les
48 anciennes sources restent identiques octet par octet, éditeurs et espace global
rétablis, fichiers de test nettoyés et trois sauvegardes complètes gardées. Nouvelles
sources de test et exports PC restent disponibles pour reprise. .177 inchangé.
:::

::: info Deux onglets vérifiés avec session bloquée et interruption HA
Sur .68 avec l’App 0.1.330 et HA 2026.10.2, deux brouillons différents restent
modifiables et exportables avec méthodes de session bloquées pendant un vrai
redémarrage HA. Les deux onglets se reconnectent automatiquement. Après recharge
sous blocage, aucune source n’est appliquée automatiquement : vérifier puis
reprendre explicitement le bon brouillon avec sauvegarde. Chaque export complet
de reprise correspond à son propre état pendant l’interruption, sauf date d’export.
Seule une sauvegarde ultérieure confirmée retire le message ; ensuite les pointeurs
restent distincts après recharge. Les 40 anciennes sources et les données sont
conservées, deux éditeurs originaux rétablis, objets de test nettoyés et trois
sauvegardes complètes gardées. .177 inchangé. Ni coupure Wi-Fi ni arrêt forcé du
processus navigateur ne sont qualifiés dans ce passage.
:::

::: info Messages distincts pour erreurs locales et de session – App 0.1.330
La qualification sur .68 avec HA 2026.10.2 réussit : quota réel de session avec
et sans pointeur existant, méthodes et accès de session bloqués, export, reprise
manuelle et messages DE/EN/FR. Stockage local plein et écritures locales bloquées
gardent leur erreur distincte. Les 31 anciennes sources restent identiques octet
par octet ; cinq éditeurs originaux et les données sont rétablis. Objets de test
nettoyés, trois sauvegardes complètes conservées, .177 inchangé. Ce passage ne
comprend ni nouvel arrêt forcé du navigateur ni remplissage du disque système.

Un brouillon écrit localement reste conservé même si son association à cet onglet
ne peut être garantie. Une session pleine ou bloquée affiche maintenant
**« Brouillon enregistré localement »** et signale que sa reprise par onglet
n’a pas pu être confirmée. Même un accès `sessionStorage` entièrement bloqué
n’empêche plus la sauvegarde locale du brouillon.

**Exporter avant de recharger ou fermer.** Ensuite, choisir le bon nom/la bonne
date dans **Brouillons locaux**, vérifier puis **Sauvegarder et reprendre**, sans
compter sur la présélection. Le message reste présent lors des changements de
langue DE/EN/FR et du rechargement des projets. Seule une sauvegarde confirmant
marque d’écriture et pointeur d’onglet le retire.

Un échec d’écriture locale reste une erreur distincte avec conseil d’export ;
seule la version locale précédente est alors sauvegardée. Aucune source existante
n’est supprimée ou appliquée automatiquement. Si l’accès local est entièrement
bloqué, exporter l’espace actuel et le reprendre depuis le fichier après
rétablissement de l’accès. Les sauvegardes HA ne contiennent pas les brouillons
du navigateur.

Le message de session absent découvert dans 0.1.329 est ainsi corrigé. Ce test
précédent a conservé les 20 sources existantes et leurs données. Il ne s’agit pas
d’une qualification générale de toutes les pannes de navigateur ou de disque.
:::

::: info Reprendre un brouillon plus récent après interruption – App 0.1.329
Avant d’écrire l’enregistrement, l’éditeur mémorise le brouillon prévu dans la
session de cet onglet. Si la sauvegarde s’arrête après l’écriture et avant la
mise à jour du pointeur, le chargement suivant détecte le nouvel enregistrement
correspondant exactement. Il est présélectionné ; **Vérifier le brouillon plus
récent** propose l’aperçu habituel puis **Sauvegarder et reprendre**. L’espace
actuel reste inchangé jusqu’à confirmation explicite et est sauvegardé avant reprise.

Version précédente confirmée, autres onglets et anciennes sources sont conservés.
L’association ne repose ni sur des noms similaires ni sur la date globale la plus
récente. Aucun signalement si la marque est absente, corrompue ou incohérente.
Les brouillons antérieurs à 0.1.329 et ceux sans stockage de session disponible
restent sélectionnables manuellement. Cette détection ne remplace pas un Export
avant d’effacer le stockage du navigateur ou de changer d’appareil.

**Vérifié sur .68 avec HA 2026.10.2 le 21/10/2026 :** après mise à jour, une
sauvegarde propre est interrompue précisément après l’écriture et avant le
pointeur. Le rechargement affiche le bon successeur et l’offre en DE/EN/FR.
Aperçu/annulation laissent l’espace inchangé ; la reprise confirmée restaure
exactement toutes les données projet. Aucun mélange avec un brouillon étranger
plus récent, aucune nouvelle offre après confirmation. Ce test utilise une
exception propre à cette frontière, pas un nouvel arrêt forcé du navigateur
ni un test de coupure électrique ou de panne de disque.
:::

::: info Brouillons locaux indépendants depuis l’App 0.1.328
Les projets Editor partagés disposent d’un brouillon local indépendant par
onglet. Après rechargement, le brouillon précédent de cet onglet est présélectionné.
**Brouillons locaux** propose aussi les versions conservées par nom et date.
**Vérifier le brouillon local** affiche l’aperçu ; **Sauvegarder et reprendre**
le restaure explicitement en sauvegardant l’espace actuel. La source sélectionnée
reste disponible.

L’ancien brouillon commun reste lisible comme « ancien brouillon ».
Les nouveaux enregistrements ne le remplacent pas. Les onglets dupliqués créent
aussi de nouvelles entrées lors de l’écriture ; un nouvel onglet n’applique pas
automatiquement le brouillon d’un autre. Les conflits de révision serveur restent
bloqués.

Les brouillons locaux appartiennent au profil du navigateur et à l’adresse ATLAS.
Ils ne font pas partie d’une sauvegarde HA complète. Conservez un **Export**
avant d’effacer le stockage du navigateur ou de changer d’appareil. La sauvegarde
locale fonctionne pendant l’arrêt de l’App ; aperçu et restauration nécessitent
le retour du serveur. Les erreurs d’écriture locale sont signalées : exportez alors
avant de recharger ou fermer. Les anciennes sources ne sont pas supprimées
automatiquement. Limites par brouillon : 5 000 champs et 4 Mio de données projet.

**Vérifié sur .68 avec HA 2026.10.2 le 21/10/2026 :** restauration complète
de deux brouillons différents après rechargement d’onglet et arrêt de l’App ;
exports identiques sauf leur date de création. Un nouvel onglet reprend
explicitement le brouillon d’un onglet fermé. Les anciennes sources restent
sélectionnables et les conflits serveur bloqués. DE/EN/FR réussissent. Éditeurs
initiaux, sept projets serveur, six plugins et dix fichiers capturés sont conservés.
Projet propre retiré, trois sauvegardes complètes sur .68 ; .177 inchangé.

**Le redémarrage complet de Chrome avec restauration de session réussit aussi
(21/10/2026, .68) :** l’utilisateur redémarre Chrome ; son processus principal
est remplacé. Chaque onglet restauré présélectionne son propre identifiant de
brouillon précédent. Après reprise explicite, les exports complets correspondent
aux versions respectives avant redémarrage, sauf la date d’export. Les autres
sources conservées restent sélectionnables manuellement. Révision serveur,
éditeurs initiaux et données capturées sont conservés ; projet propre retiré,
trois sauvegardes complètes gardées. .177 reste inchangé. Il s’agit d’un
redémarrage normal, pas d’un plantage, d’une coupure électrique ou de la
restauration d’un stockage de navigateur effacé.

**L’arrêt forcé du navigateur réussit aussi (21/10/2026, .68) :** l’utilisateur
termine Chrome 155 de force. Aucun processus Chrome ne reste avant sa réouverture.
Après restauration de session, chaque onglet garde son propre identifiant de
brouillon. Les brouillons repris explicitement, avec leurs titres de carte
différents, correspondent aux exports complets précédents, sauf leur date.
Quatre anciens brouillons sont exportés séparément et leurs données projet
vérifiées inchangées après le test. Éditeurs initiaux et données conservés,
projet serveur propre retiré, trois sauvegardes complètes sur .68 ; .177 inchangé.
L’arrêt suit une sauvegarde locale terminée, pas une écriture en cours.
Aucun test de coupure électrique ou panne de disque.

**Vérifié aussi pendant la sauvegarde locale (21/10/2026, .68) :** une sonde
de test propre suspend l’éditeur installé inchangé après l’écriture du nouvel
enregistrement, avant la mise à jour du pointeur d’onglet. L’utilisateur termine
Chrome de force ; aucun processus Chrome ne reste avant sa réouverture. Après
restauration de session, la version précédente confirmée reste présélectionnée.
**Sélectionner manuellement la nouvelle version complète dans Brouillons locaux,
la vérifier puis choisir Sauvegarder et reprendre.** Ses données projet, y compris
le nouveau titre de carte, correspondent exactement à la sauvegarde préalable.
L’onglet B et huit anciennes sources restent inchangés. Éditeurs initiaux et
données conservés, objets de test actifs retirés, trois sauvegardes complètes
sur .68 ; .177 inchangé. Ce test vise la frontière entre enregistrement et
pointeur, pas une interruption dans l’appel natif atomique, une coupure électrique
ou une panne de disque.
:::

Résultat tablette : [test 12/360/720 cartes](tablet-test.md) sur Galaxy Tab A6,
Android 11 / LineageOS, Chrome Mobile 155. L’utilisateur confirme 720 cartes
sur les deux hôtes, avec thèmes et reconnexion.
L’utilisateur confirme aussi [60 minutes avec UIX et 720 cartes](tablet-uix-dauertest.md)
par hôte. Objets propres retirés, données conservées et trois sauvegardes complètes par hôte.

::: info Import HACS limité et annulable avec l’App 0.1.327
La limite ZIP fixe est de **32 MiB**, vérifiée avant lecture : **2 048 entrées**,
**8 MiB par entrée**, **24 MiB au total** et **1 024 octets UTF-8 par chemin**.
Les limites des métadonnées précèdent le CRC, y compris les tailles décompressées
déclarées. La compression reste non prise en charge ; CRC32 n’est pas une signature.

Lecture et vérification utilisent un worker dédié. **Annuler l’import** le
termine pendant la lecture/vérification ou abandonne un résultat déjà prêt.
Un délai de surveillance de 15 secondes dépend de la planification du navigateur.
Une erreur de chargement/worker ne déclenche aucun import synchrone de secours.
L’éditeur reste inchangé jusqu’à **Appliquer le paquet vérifié** ; cette adoption
finale confirmée n’est pas une nouvelle étape de vérification annulable.
Après annulation, le même fichier peut être choisi sans rechargement.
Pour les grands projets, créer des paquets plus petits ; les limites sont fixes.
Annuler conserve sa position quand la vérification se termine et Appliquer apparaît.
:::

::: info Imports répétés de grands projets sur .177/.68
Vérification d’environ 25 minutes le 19/10/2026 avec l’App 0.1.327 et HA 2026.10.2 :
60 adoptions en série par hôte, avec 36 champs et 360 ou 720 cartes imbriquées
Core/Bubble/Mushroom. Au total, 238 annulations pendant la lecture/vérification
ou après validation préservent le brouillon ; 116 nouvelles sélections du même
fichier réussissent. Quatre cycles HACS réels produisent des archives identiques.
Un paquet valide de 24 MiB de contenu total est entièrement vérifié. Trois
rechargements par hôte réussissent ; éditeurs originaux et données contrôlées
sont préservés.

La portée est l’import dans Chrome sous Windows. Les mesures de mémoire couvrent
aussi les autres onglets et ne prouvent pas la stabilité mémoire isolée d’ATLAS.
Le rendu HA a ensuite été vérifié séparément ci-dessous ; une durée supérieure
reste hors périmètre. Chaque
import confirmé crée un groupe local ; les groupes de test ont été retirés en
restaurant la configuration originale complète.
:::

::: info Rendu HA de 360/720 cartes sur .177/.68
Vérifié le 19/10/2026 avec l’App 0.1.327 inchangée et HA 2026.10.2 : projets
exportés originaux et copies dynamiques propres au test, avec Core, Bubble 3.4.2
et Mushroom 5.2.3. **Card-Mod 4.2.1 et UIX 8.4.0 fonctionnent séparément.** UIX
traite `card_mod` et les styles natifs `uix`. 62 relevés stabilisés réussissent
33 120 comparaisons avec les cartes natives de référence, sans carte d’erreur :
clair/sombre, héritage CSS, bordures/arrondis et opacité Bubble. Mushroom Jinja
change texte, icône et couleur avec les états de test 18/28. Huit fermetures
WebSocket se reconnectent automatiquement sans recharger la page ; HA peut
reconstruire sa vue de cartes pendant la reprise.

Sauvegardes complètes avant le test ; les éditeurs existants ne sont ni ouverts
ni modifiés. Fichiers contrôlés, sept projets et six plugins par hôte sont
préservés. Les objets de test sont retirés et les fichiers WWW placés dans la
corbeille. Le navigateur testé est Chrome sous Windows ; FPS, performances du
navigateur tablette/ARM64, absence de fuite mémoire et longue durée ne sont pas
démontrés. Les mesures suivent la fin des transitions et du chargement des modules.
:::

::: warning Constat historique des tailles avec l’App 0.1.324
Vérification du 19/10/2026 avec l’App 0.1.324 et HA 2026.10.2 sur .177/.68 :
24 imports réels, dont 16 adoptions valides à 112/112 et huit refus.
Jusqu’à 30 008 fichiers, 64 MiB de contenu supplémentaire stocké et un README
de 16 MiB sont acceptés. Les ZIP tronqués et les archives Deflate avec 128 MiB
de contenu ou une taille déclarée de presque 4 GiB sont refusés. Le refus de
compression ne constitue pas une limite de taille ni une protection ZIP-bombe.

Les limites explicites de taille/nombre de fichiers et l’annulation fiable d’un
import actif manquaient en 0.1.324 ; le worker décrit ci-dessus s’applique désormais.
L’ancienne version lit le fichier entier avant la vérification
synchrone dans le thread UI. Un rechargement immédiat après sélection conserve
le brouillon original lors d’un essai par hôte, sans prouver une annulation
pendant le calcul CRC. Les deux éditeurs originaux complets et les données
vérifiées sont conservés. Tests dans Chrome Windows, pas dans un navigateur du Pi.
:::

::: info Import HACS sécurisé dès l’App 0.1.324
Plusieurs projets ATLAS ou scripts intégrés sont refusés avant toute sélection.
Les noms de scripts HACS, du paquet et du plan doivent correspondre ; les noms
des ressources, le Custom Element et les types de carte sont vérifiés. Les anciens
préfixes restent valides s’ils désignent le même fichier. Lecteur et import réel
exigent une vérification entièrement approuvée. Un rapport bloqué ou incomplet
ne peut plus remplacer l’éditeur. JSON/YAML valides, racine/dist et noms simples
comme temperature.js restent pris en charge. Les 418 tests, dont 40 nouvelles
régressions du gestionnaire livré, réussissent. Les données existantes ne sont
ni migrées ni réécrites automatiquement.

Les mises à jour sur .177/.68 avec HA 2026.10.2 réussissent après sauvegardes
complètes : 60 imports réels, 52 refus corrects et huit témoins valides à 112/112.
Les 14 anciens imports incorrects sont bloqués. Après chaque cas, rechargement
et exports complets des éditeurs d’origine correspondent aux sauvegardes.
Données contrôlées, sept projets et six plugins par hôte sont conservés.
:::

::: warning Constat historique : paquets HACS ambigus jusqu’à l’App 0.1.323
La vérification native sur .177/.68 avec HA 2026.10.2 trouve 14 imports incorrects
sur 46 cas. Six paquets par hôte contenant plusieurs projets ou scripts sont
adoptés malgré un rapport bloqué à 111/112. Pour des projets de même identité,
l’ordre des entrées ZIP détermine le contenu. Un nom de script contradictoire
dans le plan de l’éditeur est même accepté à 112/112 sur chaque hôte et repris
dans l’éditeur. Ces cas sont corrigés dès 0.1.324.

Les chemins identiques, les alias racine/dist et les conflits directs HACS/script
sont refusés correctement : 26 refus au total ; six témoins valides restent
importables. Les contrôles CRC et le diagnostic ZIP restent valides. Un rapport
bloqué ne protège pas à lui seul l’éditeur contre ces ambiguïtés. Utiliser des
exports non ambigus ; restaurer un brouillon remplacé depuis sa source ou sa
sauvegarde. Les tests restaurent les éditeurs complets après chaque cas et
préservent les données contrôlées. Cette ancienne vérification conservait 0.1.323.
:::

::: info Diagnostic ZIP précis dès l’App 0.1.323
Les erreurs CRC, d’en-têtes et de lecture ZIP font du contrôle ZIP le premier
blocage. Un inventaire écarté ne produit plus de faux fichiers absents : les
contrôles de fichiers et de contenu restent explicitement non vérifiés jusqu’à
la fourniture d’une archive intacte. L’import reste refusé et l’éditeur inchangé.
Les fichiers réellement absents d’un ZIP vérifié restent signalés. La liste
conserve 112 contrôles ; les 378 tests, dont 54 cas d’intégrité, réussissent.

Les mises à jour sur .177/.68 avec HA 2026.10.2 réussissent après sauvegardes
complètes : 60 refus et quatre témoins JSON/YAML valides sont confirmés. Les
26 cas sans inventaire ZIP vérifiable indiquent la cause ZIP en premier sans
faux fichiers absents. Les absences réelles restent détectées. Les configurations
complètes des éditeurs correspondent aux sauvegardes après refus/rechargement
et restauration des témoins valides. Données contrôlées, sept projets et six
plugins par hôte restent inchangés.
:::

::: info Contrôle de l’intégrité ZIP dès l’App 0.1.322
Avant l’import HACS, ATLAS vérifie le CRC32 de chaque entrée ZIP stockée, y compris
README, langues et fichiers supplémentaires. Les en-têtes locaux et centraux
doivent concorder : noms, indicateurs, méthode, CRC et tailles. Limites du
répertoire, nombre de fichiers et chevauchements sont contrôlés. Aucune donnée
de paquet endommagé n’est transmise à l’éditeur pour import. Les 52 nouveaux cas
d’intégrité et les 376 tests réussissent. Les archives originales valides restent
identiques, avec noms vides et espaces extérieurs préservés. La mise à jour native
de 0.1.321 vers 0.1.322 réussit sur .177/.68 avec HA 2026.10.2 après sauvegardes
complètes : 30 paquets endommagés/invalides par hôte sont refusés et deux originaux
JSON/YAML valides atteignent chacun 112/112. Après chaque refus et rechargement,
la configuration complète de l’éditeur reste inchangée. Le cas CRC initial est
refusé. Éditeurs d’origine et données, dont sept projets et six plugins par hôte,
sont conservés.

L’import prend en charge les entrées stockées (STORE). Compression, chiffrement,
descripteurs de données, archives multi-disques et ZIP64 sont refusés. Les
commentaires ZIP normaux restent valides. CRC32 détecte une corruption sans
authentifier le paquet ni sa source. En 0.1.322, l’inventaire écarté pouvait
produire de faux avis de fichiers absents après une erreur CRC. Dès 0.1.323,
ces contrôles dépendants sont indiqués comme non vérifiés.
:::

::: warning Constat CRC historique jusqu’à l’App 0.1.321 incluse
Après de nouvelles sauvegardes complètes, 21 imports réels par hôte sont vérifiés
sur .177/.68 avec HA 2026.10.2. Les noms absents, vides, composés d’espaces ou
contradictoires dans les manifestes HACS/paquet, sept fichiers obligatoires absents
y compris des langues déclarées, les ZIP illisibles/tronqués et le JSON invalide
des manifestes/paquets sont correctement refusés dans 19 cas par hôte. Après
chaque refus et rechargement, la configuration complète de l’éditeur reste
inchangée, hormis la date d’export. Le paquet témoin valide atteint 112/112.

Un ZIP dont le README est modifié avec une somme CRC désormais incorrecte est
pourtant accepté à 112/112 sur les deux hôtes et remplace l’éditeur local. Un
lecteur ZIP indépendant confirme l’erreur CRC. La validation de 0.1.321 ne prouvait
donc pas l’intégrité complète du ZIP. Le contrôle CRC est corrigé dès 0.1.322 et confirmé sur .177/.68 ; régénérer
les paquets endommagés depuis un original intact. Les deux éditeurs d’origine
sont restaurés exactement ; fichiers, projets, plugins et corbeille sont conservés.
:::

::: info Contrôles du titre HACS dès l’App 0.1.321
Les deux contrôles utilisent désormais le même nom de paquet que la cohérence
manifeste/script. Un premier nom Entity vide ou composé d’espaces ne provoque
plus de faux échec de titre. Noms originaux et archives restent inchangés.
Les 324 tests locaux réussissent, dont 28 nouveaux contrôles JSON/YAML, cartes
seules, piles, Conditional et manifestes invalides. Les quatre ZIP en échec
sauvegardés et quatre paquets témoins passent sans modification à 112/112 et
leur réexport est identique octet par octet. Les noms de manifeste absents ou
contradictoires restent refusés. La mise à jour native de 0.1.320 vers 0.1.321
réussit sur .177/.68 avec HA 2026.10.2 après de nouvelles sauvegardes complètes.
Les quatre ZIP JSON/YAML originaux en échec, sans carte témoin, atteignent chacun
112/112 dans le véritable éditeur et se réexportent à l’identique octet par octet.
Les huit cartes conservent exactement noms et conditions Conditional après import
et rechargement. Données, sept projets et six plugins par hôte ainsi que les deux
éditeurs locaux d’origine sont conservés. Ce contrôle complète la comparaison de
rendu HA précédente ; aucune ressource HA ni aucun tableau de bord n’est créé.
:::

::: info Noms Entity littéraux dès l’App 0.1.320
Les noms Entity explicites restent inchangés à l’import : `name: ''`, noms composés
d’espaces et espaces/tabulations extérieurs. Seul un nom absent conserve le nom
de remplacement existant. Les 296 tests locaux réussissent, dont 37 nouveaux
contrôles contre la source originale avant analyse, JSON/YAML, Conditional
imbriquées, restauration des brouillons, paquets Card et HACS. Renommage volontaire
et choix d’entité restent possibles. Aucune donnée enregistrée n’est réécrite ;
réimporter la source ou une sauvegarde pour récupérer les noms déjà normalisés.
La mise à jour native de 0.1.319 vers 0.1.320 est vérifiée sur .177/.68 avec
HA 2026.10.2 après sauvegardes complètes : 64 cas JSON/YAML par fichier/collage,
128 sorties capturées après import et rechargement, puis 16 cycles de paquets Card
réels conservent exactement les valeurs originales, même dans des Conditional
imbriquées. Données et deux éditeurs locaux d’origine restent inchangés. Ce cycle
est complété par un test HACS natif sur les deux hôtes avec une carte témoin nommée
avant les huit cas : quatre cycles ZIP JSON/YAML, chacun à 112/112 et réexports
identiques octet par octet. Les 72 paires export/référence HA concordent avant et
après rechargement (144 cartes observées). Le texte DOM conserve espaces et
tabulations ; le CSS HA les réduit visuellement comme dans les cartes natives.
Scripts et langues sont chargés sans modification depuis les vrais ZIP ; aucune
nouvelle installation de dépôt HACS n’est comprise.
:::

::: warning Défaut de validation HACS jusqu’à l’App 0.1.320 incluse
Si le paquet commence par un nom Entity vide, la validation affiche 110/112 :
`package-title-present` et `import-summary-title-present` échouent malgré le nom
du paquet. Un premier nom composé d’espaces échoue aussi au contrôle du titre.
Les noms restent intacts, mais la validation n’est pas fiable dans ce cas. Une
carte témoin nommée avant les huit cas permet la réussite. Le contrôle est corrigé
dès 0.1.321 et confirmé nativement sur .177/.68 avec les ZIP originaux.
L’échec natif en 0.1.320 avec une chaîne vide est reproduit ; le cas des espaces
découle de `trim()` dans le code du contrôle.
:::

::: info Correction des cartes seules dès l’App 0.1.319
Les cartes Conditional deviennent des champs Expert complets avec leurs conditions
et cartes imbriquées. Les cartes Entity seules conservent leur nom personnalisé ;
le renommage explicite et le choix d’entité restent possibles. Les 259 tests locaux
réussissent, dont 19 nouveaux contrôles de la conversion réelle de l’éditeur, de la
restauration des brouillons et de l’export JSON/YAML/HACS. Les données enregistrées
ne changent pas. Réimporter la source ou une sauvegarde pour récupérer un contenu
déjà perdu. La mise à jour native de .177/.68 est vérifiée avec HA 2026.10.2 après
sauvegardes complètes : 32 cas conservent la structure d’origine par import
JSON/YAML, fichier/collage et rechargement. Huit paquets Card réels passent
l’export, le réimport et le rechargement. Les données et les deux configurations
locales d’origine de l’éditeur restent inchangées.
:::

::: warning Limite jusqu’à l’App 0.1.319 incluse
L’analyseur remplace encore `name: ''` par `Imported entity card` et supprime
les espaces extérieurs des noms Entity. Seize contrôles supplémentaires confirment
cette normalisation sur les deux hôtes ; ils ne prouvent pas une conservation
littérale du nom source. Les anciens tests locaux comparaient après normalisation.
Les noms personnalisés ordinaires et les conditions Conditional sont vérifiés en
0.1.319, corrigeant les pertes correspondantes de 0.1.318. Ce cycle ne comprend
pas de nouveau test natif HACS ZIP ni de rendu HA.
:::

::: info Prévisualisation d’import dès l’App 0.1.318
La prévisualisation utilise le même analyseur que l’import réel, y compris les
cartes imbriquées et le contenu des paquets et exports. Les cartes Markdown
non prises en charge sont refusées avant toute modification de l’éditeur ;
cette correction n’ajoute pas le support de Markdown. Les cartes Entity et
Conditional seules sont aussi reconnues en JSON ; le YAML est analysé de façon
structurée. Les 240 tests locaux réussissent, dont 27 nouveaux tests de parité.
La mise à jour native de .177/.68 est vérifiée après sauvegardes complètes :
24 refus Markdown par fichier/collage conservent le code et huit imports
JSON/YAML imbriqués conservent la structure. Les données et les éditeurs locaux
d’origine sont conservés, même après rechargement. Les anciennes pertes des cartes
seules sont corrigées et revérifiées en 0.1.319 ; la normalisation est corrigée
dès 0.1.320 et sa validation native réussit sur .177/.68.
:::

::: info Affichage Conditional vérifié le 18/10/2026
Avec ATLAS 0.1.317 et HA 2026.10.2, les références natives et les scripts
exportés depuis JSON et YAML concordent dans 1 008 décisions de visibilité :
14 variantes, six cas d’état et des largeurs de 898 et 2560 pixels CSS sur les
deux systèmes de test autorisés. Le contrôle couvre ET implicite, ET/OU/NON
imbriqués, listes `state`/`state_not`, `entity_id`, bornes numériques strictes
avec zéro et références d’entité, conditions d’écran/utilisateur et cartes
Conditional imbriquées. L’enregistrement et la réouverture conservent exactement
JSON et YAML. Les conditions utilisateur incluent l’utilisateur connecté et un
identifiant de test exclu. Les deux formats réussissent aussi le réimport HACS
réel sur les deux hôtes : 112/112 contrôles par paquet et réexport identique octet
par octet. Les éditeurs locaux et les données existantes capturées sont conservés ;
les éléments de test sont nettoyés et les fichiers restent récupérables dans la
corbeille. Ce contrôle ne valide pas tous les types de cartes ou
conditions : les feuilles sont des cartes Core Entity. L’import réel a refusé une
feuille Markdown malgré une prévisualisation la déclarant importable. Les nouveaux
tests réseau sont limités à 192.168.178.177 et 192.168.178.68 ; les rapports sur
d’autres hôtes constituent des preuves historiques.
:::

Le **Home Assistant Card Editor** est le premier plugin de référence intégré
à ATLAS. Il permet de concevoir visuellement des cartes, d’importer le YAML
existant et de préparer des packages ou bundles destinés à HACS.

L’éditeur local utilise `http://127.0.0.1:4174/` ; les connexions sont gérées
par l’Administration sur `http://127.0.0.1:4175/`.

Depuis l’application HA **0.1.286**, le rechargement et l’import JSON/HACS
préservent les identifiants de modèles et les dimensions de référence du
redimensionnement. Le réimport d’un bundle compare les deux noms de manifeste,
même si le nom du projet diffère du titre de la première carte. Les contenus
et paramètres existants sont conservés.

Le parcours Administration → Hub → connexion HA → Expert → export/import a été
vérifié en DE/EN/FR avec un endpoint simulé, un profil isolé et un plugin de test,
y compris rechargement et redémarrage du conteneur. Les vérifications natives
complémentaires sur Pi 5 et Proxmox sont terminées ; leur périmètre et leurs limites sont consignés
dans l’[état du développement](/fr/projects/atlas/development-status).

## Signaler un problème (depuis 0.1.287)

Le signalement crée d’abord un aperçu local. Le bouton de copie utilise
le texte vérifié ; si le presse-papiers échoue, vous pouvez le copier
manuellement. Le bouton GitHub ouvre seulement le formulaire avec des
instructions. Le rapport n’est ni envoyé automatiquement ni intégré dans l’URL.

Le filtre retire les identifiants sensibles des champs structurés, du JSON/YAML,
des URL et des fragments de jeton, ainsi que le jeton HA connu dans le reste
du texte. Il ne lit ni cookies ni stockage du navigateur ; les indicateurs de
clé configurée sont des booléens. Relisez néanmoins les textes des cartes,
entités et informations personnelles avant partage. L’ouverture du rapport
ne modifie pas les projets, paramètres ou plugins.

## Workflow Expert

L’éditeur ouvre directement le workflow Expert. Le mode Simple et le sélecteur
Simple/Expert ont été supprimés ; les imports anciens pris en charge restent
compatibles. Import HA, collage YAML, diagnostic des ressources et sélection
des entités restent disponibles.

Déposez les cartes depuis la palette gauche sur une grille semblable à celle
de Home Assistant. Vous pouvez les déplacer, redimensionner, imbriquer et
exporter en YAML. Les cellules restent carrées ; X et Y règlent les colonnes
et lignes, tandis que Zoom modifie leur taille sans déformer la grille.

## Connexion Home Assistant

L’éditeur reçoit l’URL et le jeton uniquement comme transmission de session
depuis l’Administration ; il n’enregistre pas durablement le jeton lui-même.

Il prend en charge :

- l’API WebSocket Home Assistant ;
- les entités via `get_states` ;
- le cache local des entités et domaines ;
- l’état de synchronisation sous l’état de connexion ;
- la recherche par domaine, nom et identifiant ;
- la vérification Lovelace via le WebSocket du navigateur et le proxy Admin.

Le diagnostic des ressources permet d’identifier un blocage dans le WebSocket,
le proxy ou le mécanisme de repli. Pour les URL mobiles, le port 80 et l’erreur
1006, voir le [guide de connexion](/fr/projects/atlas/homeassistant).

## Liste des cartes

La palette Expert contient les cartes Core, les modèles locaux et les cartes
Community détectées :

- Entity, Entities et Overview / Glance ;
- Button, Grid et Sensor ;
- Vertical stack et Horizontal stack ;
- Thermostat, Link et Webpage ;
- Mushroom Template, Bubble Card et Tabbed Card V2.

Les ressources sans correspondance intégrée restent des informations de scan.
Une correspondance locale avec un type `custom:*` les rend déplaçables et
conserve leur chemin de ressource dans les exports. Les ressources auxiliaires
peuvent être masquées ; la liste complète permet de les rétablir.
La déduction automatique d’un type depuis le nom du fichier JavaScript est
facultative et affiche un avertissement rouge.

Les favoris enregistrés masquent les autres cartes. Une carte favorite ne peut
pas être masquée ; afficher toutes les cartes conserve les favoris.
Les tailles et favoris peuvent être réinitialisés séparément.

## Cartes conteneurs

Les conteneurs pris en charge sont `vertical-stack`, `horizontal-stack`
et `custom:tabbed-card-v2`. Ils acceptent des cartes par glisser-déposer.
Tabbed Card V2 gère ses onglets et leurs cartes ; les piles conservent leurs
enfants séparément et les présentent dans la boîte d’information.

## Import

Les sources prises en charge sont les fichiers YAML, le YAML collé,
le JSON, les packages ATLAS et les bundles HACS intégrant
`atlas/*.atlas-card.json`.

ATLAS détecte les styles `card_mod` et `uix`. Les styles d’entité sont
associés à leur entité ; les styles globaux restent visibles à part.
Le YAML d’origine est conservé autant que possible et évolue lorsque la carte
est modifiée. La conservation de toutes les options de cartes tierces n’est
pas garantie.

Les cartes `custom:tabbed-card-v2` écrites manuellement avec
`tabs[].card`, des piles imbriquées et des cartes personnalisées brutes
prises en charge ouvrent une structure de conteneurs Expert.

## Export

Les sorties comprennent le YAML Home Assistant, le YAML Expert, le script
de carte, le package ATLAS, le bundle HACS et la liste des ressources.

Lors de l’export HA, choisissez le format de styles `card_mod` ou `uix`.
Les noms de téléchargements peuvent recevoir un compteur afin de distinguer
les fichiers ; le comportement final dépend aussi du navigateur.

La langue de la carte exportée est indépendante de la langue ATLAS.
`en` est obligatoire comme repli. Les langues supplémentaires non traduites
sont identifiées comme replis à traduire et à vérifier. Le chemin réel
ChatGPT/OpenAI passe par l’Administration et nécessite Internet ; les fichiers
traduits automatiquement restent à relire. Voir le
[modèle d’export et les secrets](/fr/projects/atlas/homeassistant#feuille-de-route-et-langues-exportees).

### Aller-retour du bundle HACS vérifié

L’App **0.1.307** vérifie un projet mixte Core/Bubble/Mushroom dans HA Core
**2026.10.1** isolé : import ZIP, téléchargement réel dans le navigateur,
réimport et nouvel export conservent champs, grille et configuration des cartes.
Le ZIP réexporté est identique octet par octet dans ce test. Les contrôles
comparent le nom du projet au nom vérifié du package ; les noms différents
des cartes internes ne provoquent plus de faux conflits de titre.

Le script exporté fonctionne dans HA réel avec Bubble **3.4.2** et Mushroom
**5.2.3**, avec mise à jour des états en direct. HA utilise des piles générées ;
les métadonnées de grille conservées ne garantissent pas une géométrie identique
au pixel près. Les ressources isolées sont servies via `/local/` ; cela ne
valide pas le téléchargement depuis un dépôt HACS.

### Fichiers de langue du script exporté

Depuis l’App **0.1.308**, le script Card charge `locales/en.json` et la langue
choisie relativement à sa propre URL. Déployer le JavaScript et le dossier
voisin `locales/` ensemble sur la même origine HA ; déclarer la ressource
Lovelace avec le type `module`. La Card suit la langue HA. `language: de` ou
`language: fr` dans sa configuration permet de la fixer ; les variantes
`de-DE` et `fr-FR` utilisent leur langue de base.

Le titre, l’aide pour les entités de démonstration et le message d’erreur du
script utilisent ces textes. Chaque texte absent, invalide ou incomplet utilise
`en.json`, puis l’anglais intégré. Le script fonctionne aussi sans fichiers de
langue. Un `title` ou `replacement_hint` personnalisé distinct reste prioritaire.
Les noms des champs et identifiants d’entités restent intacts ; HA traduit ses
propres libellés et ceux des cartes communautaires. Chaque langue est chargée
une fois par visite. Recharger après modification ; après une mise à jour du
script, ajouter si nécessaire une nouvelle version à l’URL de la ressource.

Les exports EN/DE/FR sont indépendants de la langue de l’éditeur. Sans exécution
d’un adaptateur de traduction, DE/FR contiennent des replis anglais identifiés,
à traduire et vérifier.

### Distribution HACS commune depuis 0.1.309

Le ZIP exporté contient `hacs.json` à la racine, le script et les langues sous
`dist/`, par exemple `dist/energy-kitchen.js` et `dist/locales/en.json`.
Extraire le ZIP complet dans un dépôt GitHub dédié nommé `energy-kitchen`,
puis l’ajouter dans HACS comme dépôt Dashboard. Le nom du dépôt correspond au
nom du script sans `.js` ; utiliser un dépôt distinct de l’intégration ATLAS.

HACS installe le contenu de `dist/` dans `www/community/energy-kitchen/`.
La ressource module est `/hacsfiles/energy-kitchen/energy-kitchen.js` et les JSON
sont voisins dans `locales/`. HACS enregistre le module en mode stockage ; en
mode YAML, ajouter soi-même la ressource documentée dans le bundle.

Ne pas placer aussi le script à la racine ni publier de pièce jointe JavaScript
seule dans une release : HACS peut la préférer à `dist/`. Le ZIP exporté n’est
pas un paquet d’installation `zip_release`. HACS 2.0.5 peut omettre des langues
si le nom du script commence par `dist` ; ATLAS bloque cet export avec un message.
Choisir un autre nom de script HACS. Les projets existants restent intacts.

Le parcours réel GitHub/HACS est aussi vérifié sous HA 2026.10.1 isolé avec
HACS 2.0.5 : autorisation GitHub de l’appareil par l’utilisateur, enregistrement
comme dépôt Dashboard personnalisé et téléchargement depuis `main`. Le script
et EN/DE/FR sont installés avec les octets exacts de GitHub ; HACS enregistre
automatiquement le module. Les anciens bundles ATLAS restent importables.

Le [dépôt public d’export Card](https://github.com/rockbaer2007/atlas-hacs-delivery-card)
est explicitement un exemple de test. Dans le menu principal HACS, ouvrir
**Dépôts personnalisés**, saisir cette adresse GitHub, choisir **Dashboard** puis
**Ajouter**. Ouvrir **Locale test card**, confirmer **Télécharger** et recharger
le navigateur. La ressource est
`/hacsfiles/atlas-hacs-delivery-card/atlas-hacs-delivery-card.js`.
Dans `v0.1.0`, DE/FR sont des replis anglais identifiés. `v0.1.1` contient des
textes de test traduits manuellement : « Wohnzimmer 0.1.1 » et « Salon 0.1.1 ».
Cela ne démontre pas une traduction automatique. Bubble Card et Mushroom sont
aussi nécessaires pour cet exemple de Card mixte.

Le cycle étiqueté `v0.1.0` → `v0.1.1` → `v0.1.0` est également vérifié sous
HA 2026.10.1/HACS 2.0.5 isolé. Enregistrer d’abord une sauvegarde complète.
Dans le menu du dépôt, choisir **Actualiser les informations**. HACS détecte
la nouvelle version comme mise à jour en attente ; utiliser **Retélécharger**
pour installer la version proposée, puis recharger le navigateur.
Pour la réinstallation manuelle vérifiée de l’ancienne version, ouvrir
**Retélécharger**, développer **Besoin d'une version différente ?**, choisir
`v0.1.0` dans **Version**, télécharger et recharger. HACS recommande explicitement
de restaurer une sauvegarde plutôt que d’utiliser ce sélecteur pour revenir
en arrière. La réinstallation remplace les fichiers Card ; elle ne restaure
pas les données migrées à partir d’une sauvegarde.

Les deux releases utilisent `dist/` sans pièce jointe JavaScript séparée.
Le script et les trois fichiers de langue correspondent exactement au tag
choisi à chaque étape. La ressource module conserve son identifiant ; HACS
modifie son `hacstag`. Les autres ressources, paramètres, projets et dépendances
sont conservés. L’ancienne version fonctionne aussi après redémarrage du test.
HACS propose ensuite toujours `v0.1.1` comme mise à jour ; le choix de l’ancienne
version ne la verrouille pas définitivement.

Il s’agit d’un dépôt personnalisé, pas d’une inclusion dans la liste HACS par
défaut. Pi 5 et Proxmox restent inchangés.

### Mises à jour échouées ou interrompues

À partir d’ATLAS **0.1.310**, les scripts Card nouvellement générés vérifient EN
et toutes les langues sélectionnées pour l’export, y compris les langues inactives.
Les fichiers absents, illisibles ou JSON invalides avec des métadonnées de langue
incorrectes produisent un avis compact indiquant les chemins concernés. Le texte
de réparation EN/DE/FR est intégré indépendamment de ces fichiers. Cards et états
en direct restent utilisables avec le repli linguistique existant.

Dans HACS, retélécharger le paquet Card complet et recharger le navigateur ;
restaurer la sauvegarde si nécessaire. L’avis disparaît après réparation et
rechargement. Les scripts déjà installés doivent être réexportés et redistribués.
Ce contrôle détecte les fichiers absents/illisibles.

À partir de **0.1.311**, les scripts et langues nouvellement exportés partagent
aussi un identifiant de paquet déterministe (`_meta.packageId` dans les langues).
Un identifiant différent ou absent déclenche également l’avis ; les textes
concernés sont ignorés, avec repli EN ou anglais intégré. Conserver cet identifiant
lors de la traduction ; ne pas copier celui d’un autre paquet pour masquer l’avis.
Ce contrôle détecte les mélanges accidentels, pas les modifications de texte avec
un identifiant inchangé ; ce n’est pas une signature. Des exports identiques ont
le même identifiant. Les anciens scripts ne sont pas modifiés rétroactivement.
Il n’y a ni réparation ni restauration automatique.
Le nouveau contrôle est d’abord vérifié dans HA 2026.10.1/HACS 2.0.5 isolé :
EN/FR mélangés, identifiant absent, Cards toujours affichées et réparation après
rechargement. Pi 5 et Proxmox sont restés en 0.1.310 pendant ce contrôle isolé.

La mise à jour et le contrôle sont ensuite testés sur les deux hôtes en 0.1.311 :
Cards `/local/` propres au test, EN/FR mélangés, identifiant FR absent et réparation
après rechargement. Paramètres, projets et fichiers vérifiés restent intacts.
Constat historique distinct : la corbeille File Studio résidait dans le conteneur
App remplaçable. Seuls nos anciens dossiers de test y figuraient ; ils ont été
reconstitués depuis les copies PC avec leurs métadonnées initiales. App 0.1.312
corrige le stockage ; remplacement du conteneur et restauration sont vérifiés
en isolation. Avant la première mise à jour, transférer les anciennes données
dans l’ancien conteneur et sauvegarder le résultat ; voir [File Studio](../atlas-plugins/file-studio.md).
La reprise des anciens dossiers et la mise à jour 0.1.312 sont ensuite vérifiées
sur Pi 5 et Proxmox avec conservation des données. Il ne s’agit pas d’un
nouveau test d’installation native d’un dépôt HACS.

La mise à jour 0.1.310 et ce contrôle sont aussi testés sur Proxmox et Pi 5 après
de nouvelles sauvegardes : Cards de test distinctes nouvellement générées, FR et
EN absents, puis restauration après rechargement, avec paramètres, projets et
plugins externes conservés. La vérification native utilise des ressources de
test `/local/` distinctes, pas une nouvelle installation GitHub/HACS. Un échec
de lecture temporaire peut aussi déclencher l’avis ; un premier avis dans
l’aperçu Proxmox a disparu après rechargement. Un avis seul ne prouve pas une
corruption permanente.

Des pannes ont été injectées dans une copie isolée HA 2026.10.1/HACS 2.0.5 :
le nouveau script a réellement été téléchargé depuis GitHub et écrit, puis les
téléchargements des langues ont signalé un échec ou le processus a été arrêté
brutalement avant leur fin. Seule cette copie HACS contenait l’instrumentation de test.

Lors d’un échec signalé, HACS affiche une erreur et restaure automatiquement
l’ancienne Card avec EN/DE/FR. Un arrêt brutal laisse en revanche le nouveau
script sans les fichiers de langue, même après redémarrage. HACS peut encore
afficher l’ancienne version installée. Le repli EN intégré peut maintenir la
Card visible ; l’affichage et le numéro de version ne prouvent donc pas que
l’installation est complète.

Après suppression de la panne, **Retélécharger** avec l’ancienne release connue
a été vérifié avec succès. Recharger ensuite le navigateur et contrôler le script,
tous les fichiers de langue, la ressource et l’affichage. Une sauvegarde complète
distincte de la configuration Docker HA a aussi été restaurée dans un nouveau
volume de test vide : les 2 500 fichiers étaient identiques avant démarrage ;
HACS, les Cards et les états en direct fonctionnaient ensuite. Paramètres,
tableau de bord et dépendances ont été conservés.

La sauvegarde temporaire HACS ne remplace pas votre propre sauvegarde. La réparation
automatique après arrêt brutal n’est pas garantie. Ce test contrôlé et cette
restauration de volume Docker ne couvrent pas toutes les pannes réseau/disque,
la restauration des sauvegardes HAOS ni les autres versions HACS.

## Tabbed Card V2

Cette carte ATLAS est exportée sous le type :

```yaml
type: custom:tabbed-card-v2
```

Ressource attendue :

```text
/hacsfiles/tabbed-card-v2/tabbed-card-v2.js
```

**ATLAS Tabbed Card V2 doit être installé dans Home Assistant** avant
utilisation. Il appartient à la famille de cartes ATLAS, fournie via le dépôt
`https://github.com/rockbaer2007/atlas`. Il s’inspire de
`kinghat/tabbed-card` et reste une variante ATLAS séparée.

Son éditeur Home Assistant accepte YAML ou JSON. Les blocs multilignes
`>-` et `|-` restent des valeurs multilignes afin de conserver les
expressions Jinja, les modèles Mushroom et les styles `card_mod`.
Les opacités des arrière-plans actifs et inactifs sont calculées en valeurs
de couleur stables avant le changement d’onglet.

### Styles Tabbed Card V2

Les variables Material sont complétées par celles des arrière-plans, des
arrondis et des espacements :

| Nom | Valeur par défaut | Description |
| --- | --- | --- |
| `--mdc-theme-primary` | `--primary-color` | Texte actif, indicateur et couleur d’accent. |
| `--mdc-tab-text-label-color-default` | `--secondary-text-color` | Texte inactif ; une valeur `rgba(...)` permet la transparence. |
| `--mdc-typography-button-font-size` | `14px` | Taille du texte des onglets. |
| `--tabbed-card-v2-card-background` | Arrière-plan de carte HA | Fond extérieur ; `transparent` permet une superposition. |
| `--tabbed-card-v2-card-border` | Bordure de carte HA | Bordure extérieure. |
| `--tabbed-card-v2-card-border-radius` | Rayon de carte HA | Arrondi extérieur. |
| `--tabbed-card-v2-content-padding-side` | `0` | Espacement intérieur gauche et droit. |
| `--tabbed-card-v2-content-padding-bottom` | `0` | Espacement intérieur inférieur. |
| `--tabbed-card-v2-tabbar-background` | `transparent` | Fond de toute la barre d’onglets. |
| `--tabbed-card-v2-active-background` | `transparent` | Fond de l’onglet actif. |
| `--tabbed-card-v2-active-background-opacity` | `100` | Opacité active de `0` à `100`. |
| `--tabbed-card-v2-inactive-background` | `transparent` | Fond des onglets inactifs. |
| `--tabbed-card-v2-inactive-background-opacity` | `100` | Opacité inactive de `0` à `100`. |
| `--tabbed-card-v2-hover-background` | `--secondary-background-color` | Fond au survol ou à la focalisation. |
| `--tabbed-card-v2-tab-border-radius-top` | `0` | Arrondi supérieur gauche et droit. |
| `--tabbed-card-v2-tab-border-radius-bottom` | `0` | Arrondi inférieur gauche et droit. |
| `--tabbed-card-v2-tabs-padding-left` | `0` | Espacement avant le premier onglet. |
| `--tabbed-card-v2-tabs-padding-top` | `0` | Espacement au-dessus des onglets. |
| `--tabbed-card-v2-tabs-gap` | `0` | Espacement entre onglets. |
| `--tabbed-card-v2-indicator-inset` | `0` | Retrait horizontal de l’indicateur actif. |
| `--tabbed-card-v2-indicator-border-radius` | `0` | Arrondi de l’indicateur actif. |

![Styles Tabbed Card V2 dans l’éditeur Home Assistant](/images/atlas/tabbed-card-v2-0.1.7.png)

![Résultat avec onglets arrondis](/images/atlas/tabbed-card-v2-result-0.1.7.png)

Exemple :

```yaml
type: custom:tabbed-card-v2
styles:
  --mdc-theme-primary: "#ff9800"
  --mdc-tab-text-label-color-default: "rgba(255,255,255,0.75)"
  --tabbed-card-v2-card-background: "transparent"
  --tabbed-card-v2-card-border: "0.2px solid var(--primary-color)"
  --tabbed-card-v2-card-border-radius: "12px"
  --tabbed-card-v2-content-padding-side: "16px"
  --tabbed-card-v2-content-padding-bottom: "16px"
  --tabbed-card-v2-tabbar-background: "rgba(0,0,0,0.18)"
  --tabbed-card-v2-active-background: "#ff9800"
  --tabbed-card-v2-active-background-opacity: 35
  --tabbed-card-v2-inactive-background: "#ffffff"
  --tabbed-card-v2-inactive-background-opacity: 8
  --tabbed-card-v2-hover-background: "rgba(255,255,255,0.12)"
  --tabbed-card-v2-tab-border-radius-top: "12px"
  --tabbed-card-v2-tab-border-radius-bottom: "6px"
  --tabbed-card-v2-tabs-padding-left: "8px"
  --tabbed-card-v2-tabs-padding-top: "8px"
  --tabbed-card-v2-tabs-gap: "6px"
  --tabbed-card-v2-indicator-inset: "10px"
  --tabbed-card-v2-indicator-border-radius: "999px"
tabs:
  - attributes:
      label: Light
    card:
      type: button
      entity: light.bed_light
```

## État actuel

::: info Mise à jour 0.1.317 et projet combiné vérifiés sur Proxmox et Pi 5
Après de nouvelles sauvegardes HA, les mises à jour natives et le projet
Core/Bubble/Mushroom imbriqué réussissent sauvegarde/réouverture, YAML/JSON,
réimport HACS réel et réexport identique, avec 112/112 contrôles par hôte.
Les seuils numériques absents sont refusés ; `above: -1`, Jinja et CSS sont
conservés. Les lignes conditionnelles disparaissent à -2 et reviennent à 18.
Textes, icônes SVG et couleurs changent en direct. 756 comparaisons CSS
correspondent aux références natives. Deux changements clair/sombre par hôte
préservent les 19 instances observées sans rechargement. Les éditeurs se
reconnectent après un redémarrage ordonné de HA Core ; de nouvelles mises à jour
Jinja fonctionnent sans rechargement. L’état intermédiaire bref du Pi n’a pas été
échantillonné ; sa connexion et ses mises à jour ultérieures sont vérifiées.
Périmètre : Chrome sur le PC, HA 2026.10.1, Mushroom 5.2.3, UIX 8.4.0 existant/
Bubble 3.4.2 sur Proxmox et Card-Mod 4.2.1 temporaire séparé/Bubble 3.4.1 sur Pi.
La vue de cartes normale sert de référence CSS ; une vue panneau HA peut
remplacer les rayons. Projets locaux et thèmes par défaut sont rétablis ; les
fichiers de test restent récupérables dans la corbeille. Régénérer les anciens scripts.
:::

::: info Projet combiné validé isolément avec 0.1.317
Les imports conditionnels conservent toutes les données des conditions : seuils
comme `above: -1` et `below: 0`, listes d’états et conditions logiques imbriquées,
en YAML/JSON et HACS. Les seuils numériques absents ou invalides bloquent l’import
et la validation du paquet avec une explication. Le projet combiné réussit
sauvegarde/réouverture, réimport HACS réel avec réexport identique, textes/icônes/
couleurs Jinja dynamiques, masquage conditionnel, huit changements de thème sans
rechargement et 972 comparaisons CSS. Après arrêt/démarrage HA, les deux éditeurs
se reconnectent sans rechargement et reçoivent de nouvelles mises à jour des
modèles. Card-Mod 4.2.1 et UIX 8.4.0 sont testés séparément avec HA 2026.10.1,
Bubble 3.4.2 et Mushroom 5.2.3 dans Chrome sur le PC. Données existantes
conservées ; cet essai isolé avait laissé Pi 5 et Proxmox en 0.1.316. Les seuils déjà perdus
nécessitent la source/sauvegarde d’origine ; réexporter les scripts existants.
Il ne s’agit pas d’un validateur complet de tous les types de conditions HA.
:::

::: info Changements de thème vérifiés sur Proxmox et Pi 5 le 17/10/2026
Après de nouvelles sauvegardes HA, les changements sans rechargement passent
aussi sur les deux hôtes avec ATLAS 0.1.316 et HA 2026.10.1 : Card-Mod 4.2.1
et UIX 8.4.0 séparément, Mushroom 5.2.3, Bubble 3.4.2 sur Proxmox ou 3.4.1 sur Pi.
Douze cartes Core/Bubble/Mushroom natives/générées par hôte/moteur effectuent
sept transitions entre thèmes personnalisés/par défaut. 1 920 comparaisons CSS
passent ; document et instances des cartes restent identiques. Couleurs/rayons
hérités suivent le thème, les surcharges fixes sont conservées.
Les boutons de test utilisent le gestionnaire de thème natif HA. Installation
et changements de moteur sont hors des séquences mesurées sans rechargement.
Thèmes par défaut et configuration des extensions initiaux sont rétablis ;
fichiers, projets et plugins existants sont conservés. Capteurs passifs et Chrome
sur le PC sont utilisés ; ce n’est pas un benchmark de navigateur ARM64.
:::

::: info Changements de thème sans rechargement vérifiés isolément le 17/10/2026
Avec ATLAS 0.1.316 et HA 2026.10.1, les cartes Core, Bubble et Mushroom déjà
affichées passent du clair au sombre sans rechargement ni reconstruction.
Card-Mod 4.2.1 et UIX 8.4.0 sont testés séparément avec Bubble 3.4.2 et
Mushroom 5.2.3 : sept transitions par moteur entre thèmes personnalisés/par défaut,
960 comparaisons CSS calculées au total. Couleurs/rayons hérités changent ; les
surcharges explicites restent fixes. Références natives et scripts générés
concordent ; identités du document et des cartes restent stables.
Les commandes de test isolées utilisent le gestionnaire de thème natif HA ;
navigation de profil et rechargement sont hors de la séquence mesurée.
Données initiales, neuf projets et fichiers existants sont conservés.
Pi 5 et Proxmox n’ont été ni interrogés ni modifiés. Autres thèmes, navigateurs
et versions nécessitent leurs propres contrôles ; le parcours UI HACS n’est
pas répété dans cet essai.
:::

::: info CSS Bubble et héritage UIX corrigés dans 0.1.316
0.1.315 supprimait le CSS Bubble texte sous `styles: |` à l’import YAML/JSON.
0.1.316 conserve texte, espaces, retours à la ligne et chaîne vide dans les
cartes seules/imbriquées, l’export HACS et le réimport. Les objets `styles`
existants restent pris en charge.

Les nouveaux scripts utilisent le wrapper natif Home Assistant pour les racines
avec `uix`/`card_mod`. UIX peut alors appliquer le style à une pile racine sans
`ha-card` et transmettre ses variables CSS aux enfants. Les blocs ne sont ni
aplatis ni copiés sur d’autres cartes.

Vérification isolée : HA 2026.10.1, Bubble 3.4.2, Mushroom 5.2.3 et UIX 8.4.0.
Core/Bubble/Mushroom correspondent aux références natives en clair/sombre et
après rechargement (180 comparaisons CSS calculées). Les couleurs parent
vertes/violettes distinctes de la couleur de repli sont maintenant héritées.
Les surcharges Bubble conservent fond, bordure de 3 px et rayon de 9 px.
Sauvegarde/ouverture et réimport/réexport HACS dans l’interface passent ;
112/112 contrôles de paquet et ZIP identiques complètent le contrôle visuel.

**Cartes existantes :** après mise à jour, réexporter le projet original puis
remplacer le script avec ses fichiers de langue correspondants. Réimporter
le CSS Bubble déjà perdu depuis le YAML/JSON original ou une sauvegarde ;
la mise à jour ne peut pas recréer un contenu supprimé. Projets/fichiers stockés
ne sont pas réécrits automatiquement.

Après de nouvelles sauvegardes HA, la mise à jour de 0.1.315 vers 0.1.316 est
aussi validée sur Proxmox et Pi 5 : six cartes Core/Bubble/Mushroom par hôte,
UIX 8.4.0, HA 2026.10.1, Mushroom 5.2.3 et Bubble 3.4.2 (Proxmox) ou 3.4.1 (Pi).
240 comparaisons CSS calculées, rechargement inclus, passent. Les styles YAML/JSON
sont conservés ; réexports HACS identiques et 112/112 contrôles par paquet.
Les configurations locales initiales des éditeurs sont entièrement restaurées.
Les essais natifs utilisent le thème sombre existant et des capteurs passifs.
Les autres versions HA/styles demandent des vérifications séparées. Les changements
de thème sur cartes déjà montées sont vérifiés isolément comme décrit ci-dessus.
:::

::: info Vérification CSS native sur Proxmox et Pi 5, 17/10/2026
Après de nouvelles sauvegardes HA et des copies des fichiers ATLAS, Card-Mod
4.2.1 et UIX 8.4.0 sont également testés séparément sur les deux hôtes réels :
HA 2026.10.1, Mushroom 5.2.3, App ATLAS 0.1.315. Scripts ATLAS et références
natives concordent pour couleurs/bordures Jinja dynamiques, espacement de 3 px
dans le Shadow DOM, fond et rayons. Les couleurs changent naturellement à la
minute suivante, sans rechargement. Seuls des capteurs passifs et des cartes
de test distinctes sont utilisés ; aucun appareil n’est commandé.

UIX applique le rayon de 17 px et privilégie `uix` si les deux blocs existent
(37 au lieu de 31 px). Card-Mod ignore `uix`. Aucune extension n’applique les
7 px de marge intérieure de `uix_style`. Le rechargement réussit avec les deux
extensions. La mise à l’échelle existante du navigateur peut arrondir les
bordures calculées aux pixels physiques ; export et référence restent identiques.

Le changement d’extension nécessite des redémarrages HA. UIX déjà présent sur
Proxmox est réactivé ensuite ; l’intégration Pi supplémentaire et les seules
ressources de test sont retirées après vérification ; les seuls fichiers de
test restent dans la corbeille récupérable. Réglages, fichiers
originaux, quatre projets ATLAS existants par hôte et six plugins sont
conservés. Aucune nouvelle version ATLAS. Seules les versions et règles citées
sont couvertes, pas tout CSS ni tous les thèmes.
:::

::: info Rendu CSS vérifié isolément, 17/10/2026
Avec App 0.1.315, HA 2026.10.1 et Mushroom 5.2.3, **Card-Mod 4.2.1** et
**UIX 8.4.0** ont été testés dans deux instances HA distinctes. Les scripts
ATLAS générés reproduisent les styles calculés des cartes natives équivalentes :
couleur Jinja et bordure de 4 px passent du bleu au rouge puis au bleu sans
rechargement ; l’espacement dans le Shadow DOM est de 3 px. Le rayon UIX vaut
17 px. Une référence Core confirme fond, bordure de 6 px et rayon de 23 px.
Rechargement et redémarrage réussissent ; les cartes sans style partageant
l’entité restent inchangées. Pi 5 et Proxmox n’ont pas été modifiés pour ce test.

**Limites :** `uix_style` est conservé à l’import mais ne produit aucun effet
CSS dans ces versions. Utiliser `uix: { style: ... }` pour UIX. Si `card_mod`
et `uix` coexistent, UIX privilégie `uix` ; ATLAS ne fusionne pas les blocs.
Card-Mod n’exécute pas `uix`. L’export UIX convertit la structure, pas les
sélecteurs CSS ni les variables Jinja. L’ancien nom de test « UIX legacy »
était une étiquette de carte, pas la preuve d’un alias reconnu.

Dans les **modèles CSS** de ces extensions, utiliser `config.entity` ; les
modèles de texte/icône/couleur propres à Mushroom peuvent utiliser `entity`.
`mushroom-state-info$` ne correspond pas à cette version Mushroom. Le sélecteur
testé est `ha-tile-info$` ; les structures DOM internes peuvent changer.

```yaml
type: custom:mushroom-template-card
entity: input_boolean.votre_entite_test
primary: "{{ 'Allumé' if is_state(entity, 'on') else 'Éteint' }}"
card_mod: # Avec UIX, utiliser uix: à la place
  style:
    .: |
      ha-card {
        border: 4px solid {{ 'red' if is_state(config.entity, 'on') else 'blue' }};
      }
    ha-tile-info$: |
      .info { letter-spacing: 3px; }
```

Charger Card-Mod comme module frontend. Installer UIX comme intégration,
l’ajouter dans **Appareils et services**, puis recharger la page. Ne pas charger
les deux extensions : voir la
[migration UIX](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/faq.md),
l’[installation UIX](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/quick-start.md)
et [Card-Mod](https://github.com/thomasloven/lovelace-card-mod/tree/v4.2.1).
Seules les règles citées sont couvertes, pas tout CSS ni tous les thèmes.
Modèles originaux et données existantes sont sauvegardés ; seules les copies
de test ont été adaptées. Aucune modification du code d’exécution ATLAS.
:::

::: info Mise à jour native 0.1.315 vérifiée sur Proxmox et Pi 5, 17/10/2026
Après de nouvelles sauvegardes HA, les deux hôtes valident la mise à jour
0.1.313 vers 0.1.315 et l’export/réimportation : YAML/Card-Mod et JSON avec
export UIX réussissent chacun 112/112 contrôles avec un nouvel export identique
octet par octet. Styles racine et par carte, CSS multiligne, sélecteurs shadow
DOM, Jinja et `uix_style` restent correctement associés. Les objets de style
du script généré correspondent au contenu du paquet.

Paramètres, fichiers, trois anciens projets serveur par hôte, six plugins
actifs, corbeille et historique sont conservés. Les configurations locales
complètes de l’éditeur sont restaurées exactement ; les nouveaux projets de
test restent séparés. Hub direct et panneau Runtime intégré affichent toujours
six plugins actifs. HA reste 2026.10.1 et l’intégration 0.1.306. Aucun dashboard,
ressource HA ou test d’appareil n’a été créé. L’exécution de CSS arbitraire
par Card-Mod/UIX reste une validation séparée selon les extensions installées.
:::

::: info Styles Card-Mod/UIX importés depuis 0.1.315, vérifiés isolément le 17/10/2026
Les objets `card_mod`, `uix` et `uix_style` importés restent sur leur propre
carte dans l’éditeur, le YAML/JSON, le paquet HACS et le script généré. Les
cartes imbriquées, CSS multiligne, sélecteurs shadow DOM et valeurs Jinja sont
conservés. Des cartes partageant une entité ne reçoivent pas les styles des
autres. Les parcours HACS YAML et JSON réussissent 112/112 contrôles avec un
nouvel export identique octet par octet ; l’import JSON d’une carte seule est
également vérifié dans le navigateur.

L’option **uix:** convertit structurellement les propriétés `card_mod` en `uix`,
y compris en JSON et dans les scripts. Les objets `uix`/`uix_style` existants
sont conservés. Si `uix` existe déjà sur une carte, les deux blocs restent
présents sans écrasement ni fusion. **card-mod** conserve les clés importées,
sans conversion inverse de UIX. Cela vérifie les données, pas l’exécution de
tout CSS dans chaque version Card-Mod/UIX. L’extension de style doit être
configurée dans HA.

Fichiers, projets et plugins existants restent inchangés. Les styles déjà
perdus par une ancienne version nécessitent un nouvel import du fichier
original ou d’une sauvegarde. Ce test isolé laissait Pi 5 et Proxmox inchangés ;
la validation native suivante est documentée séparément ci-dessus.
:::

::: info Parcours HACS YAML/JSON à partir de 0.1.314, vérifié isolément le 17/10/2026
Choisir YAML ou JSON dans **Card format**, exporter le bundle HACS, puis
réimporter le `.hacs.zip` complet via **Import HA card**. Les deux formats
réussissent les mêmes 112 contrôles. Le format choisi, les champs de l’éditeur
et les modèles Mushroom de texte, icône et couleur, y compris les valeurs
multilignes, sont conservés ; le nouvel export est identique octet par octet
pour chaque format.

Le conteneur `atlas/*.atlas-card.json` et les fichiers de langue restent JSON ;
`manifest.format` décrit le code de carte YAML ou JSON qu’il contient. Le script
généré reste JavaScript. Les anciens bundles YAML valides ne nécessitent aucune
conversion. Le code de diagnostic `package-format-supported` remplace
`package-format-json`. Les contenus invalides et langues manquantes restent
refusés. La perte des styles `card_mod` constatée dans ce test est corrigée
depuis 0.1.315, voir ci-dessus. Pi 5 et Proxmox restent inchangés.
:::

::: info Correction Mushroom dans 0.1.313, vérifiée isolément le 17/10/2026
Les imports YAML/JSON habituels conservent `primary`, `secondary`, `icon`,
`color` et l’ancien `icon_color` pour les cartes Mushroom Template seules et
imbriquées. Les cartes seules restent de type Mushroom. Le YAML multiligne
conserve retraits et lignes vides ; le YAML incorrect est refusé.

Enregistrement, rechargement et export/import HACS conservent les expressions
testées. Avec HA 2026.10.1 et Mushroom 5.2.3, les cartes exportées changent leurs
textes, icônes et couleurs selon les états de test et se reconnectent après une
coupure de transport. HA évalue Jinja ; ATLAS conserve son code. Appliquer un
titre remplace volontairement `primary` ; changer l’entité conserve les autres
modèles. Les valeurs déjà perdues par un ancien import nécessitent le fichier
original pour être récupérées. Conserver les YAML/JSON originaux.

La vérification couvre les propriétés et cas cités, pas toutes les options
Mushroom ni tous les programmes Jinja. `icon_color` est vérifié pour sa
conservation ; le test d’exécution utilise `color`. Aucun champ de saisie Jinja
n’est ajouté. Les données existantes sont conservées ; la vérification isolée
de la correction laisse Pi 5 et Proxmox inchangés.
:::

::: info Mise à jour native 0.1.313 vérifiée sur Proxmox et Pi 5, 17/10/2026
Après de nouvelles sauvegardes HA et des copies de fichiers sur PC, les quatre
imports réussissent sur chaque hôte : YAML/JSON, cartes seules et piles. Textes,
icônes et modèles de couleur conservent leur code exact, lignes vides comprises.
Enregistrement, réouverture et véritable export/import HACS réussissent ; chaque
réexport est identique octet par octet et le contrôle JSON obtient 112/112.

Les aperçus HA réels non enregistrés changent textes, formes d’icônes et couleurs
calculées lors du changement naturel de minute Jinja, sans rechargement. Seuls
des capteurs passifs sont lus ; aucun appareil n’est commandé. Les 225/229 fichiers
ATLAS initiaux, deux projets serveur existants par hôte, six plugins, réglages,
corbeille et historique sont conservés. Les deux configurations locales complètes
de 36 champs sont restaurées exactement, sauf l’horodatage d’export. Les projets
de test restent séparés. L’intégration reste 0.1.306 ; aucun redémarrage HA n’est
nécessaire. Toutes les options Mushroom et tous les programmes Jinja ne sont
pas qualifiés par ce contrôle.
:::

::: info Test d’endurance isolé de 60 minutes le 17/10/2026
ATLAS 0.1.312 avec HA 2026.10.1 a validé une heure complète avec 36 entités
locales distinctes : douze cartes Core, douze Bubble et douze Mushroom.
720 cycles ont effectué 10 080 appels de service réussis et demandé 25 920
mises à jour de cibles sans erreur de service. Les deux vues du navigateur se
reconnectent automatiquement après des interruptions de transport de 15, 45
et 90 secondes, sans rechargement pendant l’heure. Tous les champs et cartes
restent présents ; les 36 états HA finaux correspondent aux valeurs attendues.
Enregistrement, réouverture et véritable export/import du navigateur sont
validés ; les deux exports sont identiques octet par octet. Fichiers de test,
projets, réglages des plugins, corbeille et historique initiaux sont conservés.
Les échantillons du groupe complet de processus ATLAS, à partir de la sixième
minute, vont de 168,1 à 168,6 MiB ; ceux du conteneur HA sur l’heure vont de
652 à 681 MiB. Chrome est mesuré globalement, avec les autres onglets ; ces
valeurs ne mesurent pas la mémoire de chaque carte.
L’heure utilise un paquet de test généré ; le véritable export du navigateur est
comparé séparément ensuite. Textes Jinja Mushroom dynamiques personnalisés,
performances ARM64 et capacité en production restent hors de ce contrôle.
Pi 5 et Proxmox n’ont été ni interrogés ni modifiés.
:::

::: info Parcours de 36 cartes sur Proxmox et Pi 5 le 16/10/2026
Après de nouvelles sauvegardes HA, ATLAS 0.1.312 et HA 2026.10.1 ont validé
douze cartes Core, douze Bubble et douze Mushroom sur chaque hôte.
Enregistrement, rechargement, réouverture et import du véritable export du
navigateur conservent les 36 champs et la configuration. Les deux exports par
hôte sont identiques octet par octet avec la même sélection EN/DE/FR.
Les configurations locales initiales ont ensuite été restaurées et comparées
intégralement.
Après un redémarrage réel de la VM Proxmox et une interruption LAN du Pi
effectuée par l’utilisateur, les éditeurs ouverts se reconnectent sans
rechargement ; les vues HA affichent toujours les 36 cartes sans carte d’erreur.
Ce contrôle utilise des capteurs existants passifs, sans les 360 changements
d’état artificiels du test isolé. Chrome sur le PC effectue le rendu ; ce
n’est pas un benchmark de navigateur ARM64 ni de CPU/RAM. Fichiers ATLAS,
projets, plugins, corbeille et historique existants sont conservés.
Un paramètre HACS modifié sur la ressource selfhst existante a été observé
séparément après le redémarrage de la VM et conservé.
:::

::: info Grand projet vérifié en isolation le 16/10/2026
ATLAS 0.1.312 et HA 2026.10.1 ont validé 36 champs Expert : douze cartes Core,
douze Bubble et douze Mushroom avec deux entités de test locales. Enregistrement,
rechargement et ouverture du projet serveur, puis export/import du bundle HACS,
conservent tous les champs et la configuration. Les exports avec les mêmes
langues sont identiques octet par octet. HA affiche les 36 cartes sans carte d’erreur.
Pendant 360 changements d’état sur un peu plus de trois minutes, l’éditeur et,
pour la coupure la plus longue, la vue HA se reconnectent automatiquement après
des interruptions de transport d’environ 12, 24 et 62 secondes. Les données de test
existantes sont conservées. Pi 5 et Proxmox n’ont été ni interrogés ni modifiés.
Cet essai fonctionnel limité ne constitue pas un benchmark matériel ni une
validation de toutes les tailles de projet.
Le véritable export du navigateur a été vérifié au complet à un nouveau chemin
de ressource. Un remplacement manuel sous la même URL peut mélanger un ancien
script en cache avec de nouveaux fichiers de langue et afficher l’avis de réparation.
:::

L’éditeur reste en développement actif. Le workflow Expert, l’import/export,
les entités, les vérifications de ressources, les conteneurs et les
correspondances locales sont utilisables. Des correspondances personnalisées
vérifiées seront ajoutées progressivement. L’[état du développement](/fr/projects/atlas/development-status)
distingue les essais isolés des vérifications natives et des limites ouvertes.
