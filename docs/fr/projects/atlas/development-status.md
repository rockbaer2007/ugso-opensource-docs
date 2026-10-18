---
title: État du développement
description: État actuel du développement d'ATLAS.
---
# État du développement

## Variantes matérielles testées

| Variante | Environnement de test |
| --- | --- |
| amd64 | Home Assistant dans une machine virtuelle sous Proxmox |
| ARM64 | Home Assistant sur un Raspberry Pi 5 réel avec 8 Go de RAM |

Ces indications décrivent les installations testées ; le périmètre et les
vérifications restantes sont documentés dans l'état du développement ci-dessous.

## État actuel

**État au 18/10/2026 · App HA 0.1.321 · intégration HACS 0.1.306.**

L’App 0.1.321 corrige les faux échecs de titre HACS avec un premier nom Entity
vide sans changer les noms. Les deux contrôles utilisent le nom du paquet.
Les 324 tests locaux réussissent ; les huit archives originales/témoins sauvegardées
passent sans modification à 112/112 et se réexportent à l’identique. Les manifestes
invalides restent refusés. La mise à jour native de .177/.68 reste à vérifier ;
ces hôtes restent en 0.1.320. Voir [Card Editor](./card-editor).

L’App 0.1.320 conserve littéralement les noms Entity vides et les espaces ou
tabulations extérieurs. Les 296 tests locaux réussissent ; 37 nouveaux contrôles
comparent à la source originale avant analyse : JSON/YAML, brouillons, paquets
Card et HACS. Un nom absent conserve son remplacement. Aucune donnée enregistrée
n’est modifiée. La mise à jour native de .177/.68 réussit avec HA 2026.10.2 après
de nouvelles sauvegardes complètes : 64 cas d’import, 128 sorties identiques à la
source et 16 cycles de paquets Card réels. Paramètres, fichiers, sept projets et
six plugins par hôte, corbeille et éditeurs locaux d’origine sont conservés.
Les deux hôtes sont maintenant en 0.1.320. Voir [Card Editor](./card-editor).

Le test HACS/HA natif suivant réussit avec une carte témoin nommée : quatre
cycles ZIP à 112/112, réexports identiques et 72 paires export/référence concordantes
avant/après rechargement. Un nouveau défaut reste ouvert : un premier nom Entity
vide provoque deux échecs de titre (110/112), malgré le nom du paquet. Les noms
restent intacts ; ce défaut est corrigé localement en 0.1.321. Périmètre et
comportement CSS dans [Card Editor](./card-editor).

L’App 0.1.319 corrige les pertes des cartes seules lors du transfert réel vers
l’éditeur : conditions Conditional et noms Entity sont conservés. Les 259 tests
locaux réussissent, dont 19 nouveaux contrôles éditeur/brouillon/export. Les
données enregistrées ne changent pas. La mise à jour native de .177/.68 avec
HA 2026.10.2 est vérifiée après sauvegardes complètes : 32 cas JSON/YAML par
fichier/collage conservent la source après rechargement et huit paquets Card réels
passent l’export/réimport. Données, sept projets et six plugins par hôte ainsi que
les deux éditeurs locaux d’origine sont conservés. Seize contrôles supplémentaires
ont révélé une limite en 0.1.319 : noms Entity vides remplacés et espaces extérieurs supprimés.
Les anciens tests locaux comparaient après normalisation ; leur affirmation trop
large est corrigée. Voir [Card Editor](./card-editor) pour le périmètre et les limites.

L’App 0.1.318 aligne la prévisualisation d’import sur l’analyseur réel et refuse
les cartes Markdown non prises en charge, même imbriquées. Les 240 tests locaux
réussissent, dont 27 nouveaux tests de parité. La mise à jour native de .177/.68
avec HA 2026.10.2 est vérifiée après sauvegardes complètes :24 refus Markdown
conservent l’éditeur et huit imports imbriqués conservent la structure. Les données
et éditeurs locaux sont conservés. Défauts constatés en 0.1.318 : les cartes Conditional seules
perdent leurs conditions lors du transfert vers l’éditeur ; les cartes Entity
seules perdent leur nom personnalisé (JSON/YAML sur les deux hôtes).

Les conditions étendues sont vérifiées sur les systèmes de test autorisés .177
et .68 avec HA 2026.10.2 : 1 008 décisions de visibilité, JSON/YAML,
enregistrement/réouverture et cycles HACS identiques octet par octet avec 112/112
contrôles chacun. Les données existantes et les éditeurs locaux sont conservés.
La divergence de prévisualisation Markdown est corrigée localement en0.1.318 ; voir le
[Card Editor](./card-editor) pour les limites. Les nouveaux tests réseau sont
limités à ces deux adresses ; les rapports sur d’autres hôtes sont historiques.
Les numéros de version de l’App et de l’intégration sont indépendants.

0.1.317 corrige l’import conditionnel et bloque les conditions numériques sans
seuils valides. Le projet combiné isolé réussit sauvegarde, cycle HACS, Jinja,
thèmes et reconnexion, avec 972 comparaisons CSS identiques.
Après de nouvelles sauvegardes, la mise à jour native passe aussi sur Proxmox
et Pi 5 : 112/112 contrôles chacun, cycles HACS identiques, 756 comparaisons CSS
supplémentaires, Conditional/Jinja, thèmes et connexion automatique après
redémarrage HA Core. Cet essai utilise UIX existant sur Proxmox et Card-Mod
temporaire sur Pi. Les projets Editor locaux initiaux sont rétablis.
Voir le [Card Editor](./card-editor#état-actuel).

Après de nouvelles sauvegardes, les changements de thème sans rechargement passent
aussi sur Proxmox et Pi 5 : Card-Mod/UIX séparément, 28 transitions,
1 920 comparaisons CSS et identités cartes/document stables. Thèmes et réglages
des extensions initiaux sont rétablis ; les données existantes sont conservées.
Voir le [Card Editor](./card-editor#état-actuel).

Les changements clair/sombre sans rechargement passent maintenant isolément
avec Core, Bubble et Mushroom : Card-Mod 4.2.1 et UIX 8.4.0 séparément, sept
transitions chacun, 960 comparaisons CSS et identités des cartes/document stables.
Les surcharges fixes restent intactes, couleurs/rayons hérités suivent le thème.
Pi 5 et Proxmox restent inchangés pendant cet essai supplémentaire. Voir le
[Card Editor](./card-editor#état-actuel) pour le périmètre et les versions.

0.1.316 corrige la perte de CSS Bubble à l’import et l’héritage UIX à la racine
des scripts exportés. Après les essais isolés, les mises à jour sur Proxmox et
Pi 5 passent aussi après de nouvelles sauvegardes HA : YAML/JSON, parcours HACS
identiques avec 112/112 contrôles chacun et 240 comparaisons CSS supplémentaires
dans le thème sombre existant, rechargement inclus. Les configurations locales
initiales des éditeurs sont restaurées. Réexporter les cartes existantes ;
récupérer le CSS déjà perdu dans les originaux/sauvegardes.
Voir [Card Editor](./card-editor#état-actuel).

Après de nouvelles sauvegardes, la vérification CSS native réussit aussi sur
Proxmox et Pi 5 avec Card-Mod 4.2.1 et UIX 8.4.0 : scripts générés et références
natives concordent pour les règles dynamiques et statiques testées. Extensions
séparées, capteurs passifs et aucune commande d’appareil. La configuration
d’origine des extensions est rétablie ; quatre anciens projets par hôte et
six plugins sont conservés. Voir le [Card Editor](./card-editor#état-actuel)
pour le détail et les limites de version.

Le rendu CSS est également vérifié isolément avec HA 2026.10.1, Mushroom
5.2.3, Card-Mod 4.2.1 et séparément UIX 8.4.0 : scripts générés et références
natives concordent pour couleurs/bordures dynamiques, styles Shadow DOM et
rayons UIX. `uix_style` n’a aucun effet CSS ; le Jinja CSS nécessite
`config.entity`. Voir le [Card Editor](./card-editor#état-actuel) pour
l’installation, les exemples et limites. Pi 5 et Proxmox restent inchangés ;
aucune nouvelle version de l’App.

0.1.315 conserve les objets `card_mod`, `uix` et `uix_style` importés dans
l’éditeur, le YAML/JSON, les paquets HACS et scripts. Conversion UIX, attribution
des styles, réimportation et conservation sont vérifiées isolément. Voir le
[Card Editor](./card-editor) pour le périmètre et les limites.

Après de nouvelles sauvegardes, la mise à jour 0.1.313 → 0.1.315 réussit aussi
sur Proxmox et Pi 5. YAML/Card-Mod et JSON/UIX valident chacun 112/112 contrôles
et un nouvel export identique octet par octet. Données existantes, trois anciens
projets par hôte et six plugins actifs sont conservés ; les configurations
locales complètes de l’éditeur sont restaurées exactement. L’exécution CSS
par les extensions installées reste une vérification séparée.

0.1.314 harmonise export HACS YAML/JSON, contrôle du paquet et réimportation.
Les deux formats réussissent le parcours navigateur isolé avec 112/112 contrôles
et un nouvel export identique octet par octet. Les données existantes sont
conservées. Ce test isolé antérieur laissait Pi 5 et Proxmox inchangés.
La perte de styles constatée alors est corrigée depuis 0.1.315.

0.1.313 corrige les pertes lors de l’import Mushroom YAML/JSON et de cartes
seules, vérifiées isolément : textes, icônes et modèles de couleur sont conservés.
Voir le [Card Editor](./card-editor) pour le périmètre. Après de nouvelles
sauvegardes, la mise à jour réussit aussi sur Proxmox et Pi 5 : les quatre
imports, l’affichage dynamique et la conservation des données sont vérifiés.
Les projets de test restent séparés ; les configurations locales complètes
existantes sont restaurées exactement.

| Lot | État actuel |
| --- | --- |
| A5 – Stabilisation et vérification | Terminé dans son périmètre documenté. Les projets utilisateurs variés et mesures longues restent des vérifications complémentaires. |
| A6 – Documentation française | Terminée ; DE/EN/FR sont maintenus ensemble. Les traductions partielles des interfaces de plugins externes restent signalées séparément. |
| A7 – Déploiement et compatibilité | Linux/systemd et intégration native HA/HACS implémentés et vérifiés. Autres versions HA, plateformes et migrations de formats si nécessaires restent ouvertes. |

- Installation Linux, mise à jour, retour arrière et récupération vérifiés sous
  Debian 12 amd64 LXC et Raspberry Pi OS aarch64 sur Pi 4. Le Pi 4 valide aussi
  redémarrage du système, démarrage automatique et connexion HA persistante
  depuis 0.1.305.
- Gestion partagée des plugins, projets serveur et mises à jour HACS de
  l’intégration avec redémarrage HA vérifiés sur Pi 5 et Proxmox. La matrice HA
  couvre 2026.10.1 et aussi 2026.9.4 isolément, pas toutes les versions HA.
- Export/import des cartes, enregistrement réel du dépôt HACS, releases
  étiquetées, mises à jour et récupération vérifiés isolément. Fichiers de langue
  manquants et versions mélangées sont détectés ; les contrôles de 0.1.310/0.1.311
  réussissent aussi sur Pi 5 et Proxmox.
- 0.1.312 conserve corbeille et historique après les mises à jour de l’App ;
  reprise des anciens dossiers et mise à jour vérifiées sur les deux hôtes.
  Une restauration HAOS complète chiffrée dans des instances amd64 vierges
  séparées réussit avec la même IP et une autre IP. Les 154 fichiers vérifiés,
  projet, six plugins, corbeille et historique sont conservés. Une nouvelle IP
  nécessite des changements explicites des URL HA de l’App et Runtime de
  l’intégration ; les adresses ne sont pas réécrites automatiquement.

Détails : [feuille de route ATLAS](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md)
et [guide de récupération](/fr/projects/atlas-plugins/file-studio).

## Vérifications historiques jusqu’au 14/10/2026

Les rapports suivants conservent leur périmètre d’origine. Les mentions
« ouvert » ou « prochaine priorité » concernent leur date. Consulter l’état
actuel ci-dessus et les prochaines étapes ci-dessous pour les tâches actuelles.

**A7 – Frontend HA en 0.1.299 (14/10/2026) :** l’[intégration ATLAS Runtime](/fr/projects/atlas/frontend) facultative est implémentée : structure compatible HACS, dialogues configuration/options et panneau administrateur propre. Elle intègre le Runtime existant sans transmettre d’identifiants HA et conserve la fenêtre pendant les mises à jour ordinaires des états. Un véritable HA Core 2026.10.1 isolé valide installation, options, panneau, rechargement, redémarrage et conservation des autres panneaux ; le navigateur confirme l’utilisation de l’éditeur et la conservation du projet. Six tests frontend et sept tests Python réussissent, ainsi que les régressions HA/application et les builds. Les installations Pi/VM/LXC existantes sont inchangées. Téléchargement/mise à jour HACS sur les véritables systèmes Pi/Proxmox et autres versions HA restent la prochaine qualification A7.

**A7 – Linux/systemd (14/10/2026, ATLAS 0.1.298) :** l’[installateur Linux](/fr/projects/atlas/linux) facultatif est implémenté. Les vérifications natives sous Debian 12 amd64 LXC sur Proxmox réussissent : installation, mise à jour, retour arrière, sauvegarde, redémarrage du service et récupération automatique après une mise à jour défectueuse. Configuration, identité d’installation et octets des données de test plugin/projet sont conservés ; FHEM reste désactivé et ses fichiers inchangés. Administration et éditeur Expert sont vérifiés sur le LAN en DE/EN/FR. Les 17 tests de l’installateur et les 163 tests HA réussissent, ainsi que les vérifications application, workspace, Docker et documentation. L’installation Linux ARM64 native, les autres distributions et Bare Metal restent à qualifier. L’intégration frontend native ATLAS HA/HACS reste ouverte sous A7. Les installations HA existantes sont inchangées.

**A6 – Documentation harmonisée (14/10/2026) :** les 21 pages ATLAS et plugins par langue ont été comparées en DE/EN/FR. Les pages françaises provisoires sont remplacées par des guides ; navigation, changement de langue, chemins de ressources, packages d’exemple et indications sur traduction et identifiants sont corrigés. Certains plugins externes conservent une interface française partielle, signalée explicitement. A7 est la prochaine priorité convenue : Linux/systemd et intégration frontend native ATLAS HA/HACS. Aucune modification du Runtime, des installations HA ou des données des plugins.

**Phase de vérification A5 terminée (14/10/2026, application HA 0.1.297) :** la revue finale couvre renderer/thèmes, grands projets préparés, exécution native Core/Bubble/Mushroom, templates actifs, observations courtes CPU/RAM et reconnexion dans chaque périmètre documenté. Les tests renouvelés réussissent : Runtime 55, Renderer 532, Theme 12, HA 163 et application/cycle de vie 11, soit 773 régressions ; les builds du workspace et de la documentation réussissent. Ce n’est ni une approbation de production ni une promesse d’API plugin stable. Restent ouverts : projets utilisateurs variés, tests longs et instrumentés de pannes sous charge, politique API/versions stable, distribution des releases HACS et vérification complète des langues des cartes. A6 est la prochaine priorité convenue : réviser et compléter la documentation française. Les paragraphes historiques ci-dessous conservent leur périmètre et leurs limites d’origine.

**Interruption réseau d’environ trois minutes confirmée (14/10/2026) :** l’utilisateur confirme avoir déconnecté le LAN du Pi et l’interface réseau de la VM Proxmox pendant environ trois minutes chacun. Il observe une reconnexion automatique des deux éditeurs ATLAS, sans rechargement ni connexion manuelle. Les vérifications indépendantes après récupération confirment de nouvelles données HA, des projets d’origine et exports Administration identiques sauf les horodatages, ainsi que six plugins actifs par système. Les 100 champs de test prévus n’étaient pas chargés avant l’interruption ; aucune trace Console des états du socket ou du nombre de tentatives n’est disponible. Ce scénario de trois minutes observé par l’utilisateur est terminé ; les répétitions instrumentées sous charge projet restent un périmètre distinct.

**Observation native CPU/RAM (14/10/2026) :** les statistiques Supervisor existantes mesurent HA Core et ATLAS avec 4 observations initiales, 14 sous charge et 4 après fermeture. La charge comprend 120 véritables cartes et 40 templates d’horloge actualisés. Médianes HA Core (avant → charge → après) : Pi CPU 0,13 → 0,18 → 0,09 %, RAM 461,10 → 460,55 → 460,71 MiB ; VM CPU 2,50 → 1,71 → 1,92 %, RAM 1374,49 → 1390,87 → 1388,90 MiB. Le plus grand échantillon CPU de la VM sous charge atteint 21,71 %. Les intégrations actives et les requêtes statistiques contribuent aussi à la charge ; les écarts ne sont pas attribuables uniquement aux cartes de test. Ces observations courtes concernent les conteneurs, pas l’ensemble des appareils ou le navigateur ; elles ne comparent pas le matériel et ne prouvent pas l’absence de fuite mémoire. Projets et Administration restent identiques sauf les horodatages, six plugins actifs par système ; les tableaux de bord temporaires sont supprimés.

**40 templates actifs parmi 120 véritables cartes HA vérifiés (14/10/2026) :** pour ce test natif, la configuration ATLAS vérifiée est complétée par 40 sorties Jinja Mushroom distinctes pour l’heure et l’état du capteur. Sur Pi et Proxmox, les 40 heures changent automatiquement sans rechargement ; 40 cartes Core, 40 Bubble et 40 Mushroom restent montées sans erreur de configuration. Les aperçus sont abandonnés, les projets et l’Administration restent identiques sauf les horodatages, avec six plugins actifs par système. Cela vérifie une évaluation simple des templates côté serveur et les changements d’heure en direct. Ce n’est ni une mesure CPU/RAM, ni un test de nombreuses entités changeantes, ni une nouvelle fonction de création de templates ATLAS.

**120 cartes HA réellement rendues vérifiées (14/10/2026) :** l’export ATLAS mixte complet s’exécute sur Pi 5 ARM64 et Proxmox amd64 dans le véritable aperçu HA non enregistré. Après une étape de 30 cartes, les 120 cartes comprennent 40 instances Core, 40 Bubble et 40 Mushroom avec des dimensions non nulles, sans erreur de configuration. Les détails des entités restent accessibles. Les aperçus sont abandonnés et les tableaux de bord temporaires vides supprimés après confirmation ; projets et Administration restent identiques sauf les horodatages, avec six plugins actifs sur chaque système. Le test utilise Chrome Windows et un seul capteur partagé. Les actions de rendu observées sous une seconde incluent l’automatisation et ne mesurent pas les performances du backend ou du matériel. CPU/RAM, entités variées, templates coûteux et pannes prolongées restent ouverts.

**Test mixte de l’éditeur avec 120 champs (14/10/2026) :** sur Pi 5 et Proxmox, 40 champs Core, 40 Bubble et 40 Mushroom conservent leurs données complètes après modification du titre, rechargement, DE/EN/FR, clair/sombre et requêtes HA répétées. Aucun champ ne se chevauche. Après restauration, les projets d’origine et les exports Administration correspondent exactement, sauf les horodatages ; les six plugins restent actifs. Les tuiles de l’éditeur ne sont pas des cartes Lovelace entièrement rendues. Les actions observées d’environ une à deux secondes incluent l’automatisation du navigateur et ne mesurent pas le backend. Les mesures natives CPU/mémoire, les grands tableaux de bord rendus et de nouveaux changements d’état réels sous charge mixte restent ouverts.

**Reconnexion après fermeture du transport vérifiée (14/10/2026) :** avec ATLAS 0.1.297, des onglets de test natifs séparés sur Pi 5 ARM64 et Proxmox amd64 ferment chacun le WebSocket HA existant. La vérification Console exécutée par l’utilisateur confirme l’ancien socket fermé et l’éditeur reconnecté, sans rechargement. La récupération de données HA fonctionne ; les 24 champs conservent identifiants, entités, positions et dimensions. Après restauration, les projets d’origine et les exports Administration correspondent exactement aux sauvegardes, sauf les horodatages ; les six plugins restent actifs sur chaque système. Ce test avec Chrome Windows vérifie une fermeture limitée du socket. Les pannes réseau prolongées, la charge native du backend et les projets utilisateurs variés restent ouverts. Les anciennes mentions d’une vérification de fermeture encore ouverte sont désormais dépassées pour ce périmètre limité.

**Installation locale du bundle vérifiée :** le script exporté depuis 0.1.297 a été installé comme ressource HA distincte sur Pi 5 et Proxmox. L’exemple ZIP inchangé charge la carte générée et ses cartes Core/Bubble/Mushroom sans erreur de configuration. Les cartes de test n’ont pas été enregistrées ; les ressources, fichiers et le tableau de bord Pi temporaires ont été supprimés après confirmation. Les exports Administration restent identiques sauf les horodatages et les six plugins restent actifs. Cela vérifie l’installation manuelle ; publication du dépôt HACS, couverture complète des langues, charge et reconnexion restent des tâches distinctes.

**Correction des bundles Expert dans 0.1.297 :** les scripts générés et les bundles HACS conservent maintenant la disposition Expert structurée au lieu d’afficher uniquement une liste d’entités. Les helpers de cartes Home Assistant créent les cartes Core/Community intégrées ; les entités configurées sont remplacées et les changements d’état sont transmis sans recréer les cartes. Les projets existants et les anciens exports de scripts restent compatibles. La publication d’un dépôt HACS avec distribution des versions reste une étape distincte.

**Vérification native HA/HACS du 14 octobre 2026 :** Pi 5 et Proxmox exécutent ATLAS 0.1.296 après des mises à jour avec l’option de sauvegarde HA activée. Après l’installation HACS/Bubble/Mushroom sur Pi, les exports YAML ATLAS inchangés avec Core/Bubble/Mushroom s’exécutent sur les deux systèmes dans le véritable aperçu HA non enregistré, sans erreur de configuration. Un aperçu Mushroom Jinja supplémentaire sur Pi évalue l’état HA réel. Les projets d’origine et les exports Administration sont ensuite identiques, sauf les horodatages ; les six plugins restent actifs. Les tableaux de bord de test sont supprimés après confirmation. Ces aperçus ne vérifient ni l’installation complète des bundles, ni les commandes physiques, ni les performances sous charge.

**Renderer/thèmes dans la version 0.1.296 :** les états bloqué et en attente restent rouges et jaunes en mode sombre ; les lignes de champs Expert et les boutons de suppression restent lisibles dans les deux thèmes. Une vérification Chrome isolée avec 36 aperçus préparés Entity/Button/Sensor/Thermostat/Bubble/Mushroom confirme DE/EN/FR, clair/sombre/auto, rechargement et quatre tailles d’écran sans chevauchement ni débordement horizontal de la page. Les champs et les dimensions restent inchangés. Les événements de thème système sont simulés ; l’exécution native HA/HACS et les projets utilisateurs variés restent des vérifications A5 distinctes.

Les vérifications Docker effectuées le 14/10/2026 réussissent pour les images autonomes et du paquet HA sous Linux amd64 : compilation, véritable Administration/Card Editor, contrôles de santé, redémarrage du conteneur et mise à jour/restauration de plugins avec des données isolées. Neuf tests de régression backend/origin réussissent aussi dans l’image Linux. Cela ne remplace pas les vérifications natives Supervisor/Ingress, ARM64 ou navigateur ; les installations HA existantes n’ont pas été modifiées.

**Suite d’A5 du 14/10/2026 :** la version 0.1.295 respecte aussi l’état Administration enregistré dans le navigateur lors de l’ouverture des liens directs de lancement. Les plugins désactivés ou pas encore actifs ne sont pas lancés par cette voie. Il s’agit d’une préférence d’interface, pas d’un contrôle d’accès aux fichiers. Des tests isolés du véritable serveur vérifient installation, mises à jour refusées, remplacement, redémarrage, désinstallation et restauration du paquet ; les autres entrées et les données de test sont conservées. Ces tests ne remplacent pas une vérification native HA. A5 reste ouvert pour Renderer/Theme, les projets variés, la charge native et la reconnexion après fermeture du transport.

**A2 et A3 sont terminés (13/10/2026).** L'utilisateur accepte le périmètre actuel
des tests ARM64/mobiles. Les appareils iOS/Safari réels n'ont pas été testés ;
les simulateurs Chrome sont documentés séparément. Le Card Editor conserve
uniquement le workflow Expert. Le mode Simple et son sélecteur ne seront pas
réintroduits ; les imports de projets anciens pris en charge restent disponibles.

0.1.290 réduit la liste sur tablette à une fenêtre défilante avec deux cartes
côte à côte et dispose les boutons associés en deux colonnes.

0.1.291 replie Grille et zoom par défaut sur mobile et aligne les commandes du
titre sur tablette ; sur téléphone, les deux boutons partagent une rangée sous
le champ. Toutes les valeurs sont conservées.

0.1.292 supprime le choix du mode de démarrage dans la configuration HA et
l'Administration et traite les anciens réglages Simple comme Expert.

A5 a commencé : **0.1.293** corrige l'ordre des instantanés/événements et l'état
d'erreur lors du remplacement d'un socket. Un test PC isolé avec HA simulé valide
100 cartes affichées, 2001 entités, trois reconnexions, 150 mises à jour,
les changements de thème et les imports/exports de projets DE/EN/FR.
Les 162 tests HA réussissent. Ces mesures sont synthétiques.

La vérification native A5 charge 100 cartes compactes et 24 cartes plus grandes
sur Pi 5 et Proxmox, sans chevauchement. Les thèmes, rechargements et langues
DE/EN/FR conservent les champs. Les changements réels d'état des sauvegardes
arrivent en direct sur Pi ; Proxmox charge initialement 3711 entités et
143 ressources Lovelace. La valeur CPU observée sur la VM reste constante ;
un changement de valeur en direct n'y est donc pas établi. Des sauvegardes HA
locales chiffrées sont créées auparavant. Les configurations initiales de
l'éditeur et de l'Administration sont restaurées à l'identique, sauf les dates
d'export ; les six plugins restent actifs. Après un redémarrage de Proxmox
effectué par l'utilisateur, l'éditeur se reconnecte et le projet initial reste
inchangé.

Ces tests utilisent des dispositions d'entités préparées dans un navigateur
de bureau. Les projets utilisateurs variés, les mesures de charge du backend
natif, la reprise après fermeture du transport natif et les tests plus larges du cycle de vie des
plugins restent ouverts dans A5. Le rendu sur ordinateur n'est pas un benchmark
du Pi ; le redémarrage natif et les fermetures de socket simulées constituent
des preuves distinctes.

**0.1.294** corrige la reconnexion après une coupure réseau prolongée : les
tentatives continuent au-delà des trois premiers essais, avec un délai limité
à 30 secondes. Les erreurs d'authentification ou de protocole arrêtent les
tentatives jusqu'à la correction de la connexion. Un test isolé avec huit
secondes d'indisponibilité confirme la reprise sans rechargement et conserve
le projet. Pendant le test LAN réel, le câble du Pi a été débranché environ
douze secondes. Les 100 champs de test sont conservés et les données en direct
reprennent sans rechargement. La socket observée reste connectée ; cela ne
prouve pas une nouvelle connexion native. Les deux systèmes utilisent 0.1.294.
Les exports finaux confirment la conservation des paramètres Admin, des
métadonnées de chiffrement, des identifiants des plugins actifs et des projets
initiaux. Seul Icon Studio externe, mis à jour volontairement, change de version.
Un build Docker isolé et /health vérifient aussi la runtime commune
Administration/éditeur.
L'utilisateur confirme aussi le fonctionnement dans une VM macOS Ventura directement sur Proxmox,
mais signale une grande lenteur. Ce test fonctionnel comporte une limite de
performance ; la cause n'a pas encore été mesurée ou déterminée.

Au **13/10/2026** : framework **0.2.0-alpha.88**, application HA **0.1.294**.
Les quatre étapes de stabilisation sont terminées. La vérification couvre
870 tests des paquets, cinq tests supplémentaires, les contrôles de types et
les builds, ainsi que 15 étapes dans un navigateur isolé en DE/EN/FR. La migration
testée conserve les anciens réglages Admin, dépôts, thème et plugins actifs ;
les secrets passent dans le stockage chiffré.

A1 est vérifié sur l'installation HA réelle : mise à jour Supervisor de 0.1.287
à 0.1.288, redémarrage séparé et Ingress pour les six plugins installés.
Les réglages Admin, plugins actifs et la configuration complète de l'éditeur
restent identiques avant et après la mise à jour et le redémarrage, sauf les
horodatages d'export. Une sauvegarde HA locale chiffrée a été créée auparavant.
0.1.288 corrige la version affichée dans l'Administration ; les options HA et
contrats des plugins restent inchangés. L'éditeur se reconnecte et charge les
entités et ressources Lovelace réelles. Le canevas Expert existant était vide ;
les projets plus grands restent A5. Le matériel, les navigateurs mobiles, ARM64
et tous les formats de projets propres aux plugins ne sont pas vérifiés.

A2 est vérifié en émulation : images HA amd64 et ARM64 et contexte Chromium
mobile tactile à 360×800, 390×844, 844×390 et 768×1024 en DE/EN/FR. 0.1.289
corrige les débordements de l'Administration et de l'éditeur et adapte les
dialogues de rapport, import YAML et export aux écrans étroits. Les réglages,
projets de test remplis et données des plugins sont conservés après changement
de langue, import JSON/HACS et redémarrage. ARM64 est émulé sur x86 ; Raspberry
Pi natif, Android/iOS, glisser/redimensionner au toucher, clavier virtuel et
dialogues natifs de fichiers/téléchargements restent à vérifier. Ces tests
isolés ne modifient pas l'installation HA réelle.

Le test A2 natif sur **Raspberry Pi 5 / rpi5-64** réussit également : HA OS
18.3, ATLAS 0.1.289, `aarch64` et Node `arm64`. Les six plugins s'ouvrent via
Ingress ; Terminal, chemins File Studio autorisés et catalogue MDI fonctionnent.
Une sauvegarde HA locale chiffrée précède le redémarrage d'ATLAS. Les réglages
Admin, métadonnées des plugins et export complet de l'éditeur restent identiques,
sauf l'horodatage d'export. L'éditeur se reconnecte avec 27 entités réelles.
Le canevas existant est vide. Les vues Chrome de bureau à 390×844 et 844×390
s'adaptent à l'Ingress réel du Pi sans débordement. Les navigateurs mobiles
physiques, projets plus grands et mesures de charge/performance restent à
vérifier ; aucune mise à jour Supervisor ARM64 n'est effectuée ici.

L'utilisateur confirme aussi sur une **tablette Android réelle** : le Hub et
l'Administration fonctionnent en portrait et paysage et en DE/EN/FR. Remplacer
l'URL HA `homeassistant.local:80` par l'adresse IP accessible rétablit la
connexion ; le dialogue YAML et le rapport de problème sont également signalés
comme OK. Il s'agit d'une confirmation utilisateur, pas d'un test automatisé
sur appareil. [Conseils de connexion mobile](./homeassistant#connexion-depuis-une-tablette-ou-un-telephone).
Les gestes de déplacement/redimensionnement, le clavier virtuel, les dialogues
natifs de fichiers/téléchargements et iOS n'ont pas été vérifiés indépendamment
sur chaque appareil. A2 est néanmoins terminé avec l'accord de l'utilisateur ;
ces limites ne sont plus des tâches A2 ouvertes.

ATLAS est en cours de développement. L'application Home Assistant comprend
l'Administration, le Hub des plugins et le Card Editor ; File Studio et
Automation Exporter / Editor sont distribués comme plugins indépendants.

La version actuelle de l'application Home Assistant est `0.1.312`.
L'Administration et le Hub des plugins proposent des interfaces en allemand,
anglais et français. Leur préférence de langue enregistrée est partagée entre
les deux interfaces, y compris lorsque leurs ports sont différents. Le
paramètre `language` d'une URL reste prioritaire pour la page ouverte.

## Suite du travail

1. **Projets réels et endurance :** entités, Custom Cards et thèmes variés, mesures CPU/RAM longues et pannes réseau instrumentées sous charge de projets.
2. **Récupération sur d’autres matériels :** étendre la restauration HAOS amd64 isolée aux appareils physiques ou ARM64, avec systèmes de test séparés et sauvegardes.
3. **Compatibilité complémentaire :** qualifier autres versions HA, distributions Linux, contrats plugin/API et migrations de formats si nécessaires.

**A1, A4, A5 et A6 sont terminés ; les déploiements A7 sont implémentés.** Les fonctions achevées
restent dans l'historique et ne sont plus des tâches ouvertes. Les plugins
indépendants conservent leurs propres listes de travaux.
La liste de référence se trouve dans la [feuille de route ATLAS](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
