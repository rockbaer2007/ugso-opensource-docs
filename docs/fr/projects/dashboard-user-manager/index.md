---
title: Gestion des utilisateurs des tableaux de bord
description: Affecter des utilisateurs à toutes les vues HA ou individuellement, avec sauvegardes et DE/EN/FR.
---
# Gestion des utilisateurs des tableaux de bord

**Version 0.1.10 · DE / EN / FR · MIT · stable**

<img src="/images/dashboard-user-manager/icon.png" width="96" height="96" alt="Icône avec tableau, utilisateurs et coches" />

Depuis 0.1.7, l’icône PNG intégrée apparaît dans la vignette HA et l’en-tête de l’interface et sert de favicon de l’application. Le motif approuvé est inclus dans le ZIP et le paquet UGSo sans service d’images externe. La barre latérale HA conserve son symbole MDI configuré. Paramètres, présélection enregistrée et données des tableaux de bord sont conservés pendant la mise à jour de l’icône.

Une application HA indépendante : choisissez un tableau de bord, affichez les utilisateurs en colonnes et les vues en lignes, puis modifiez les affectations par cases à cocher. ATLAS n’est pas nécessaire. L’interface utilise 90 vw et 90 vh, des noms verticaux, des colonnes étroites et un défilement horizontal si nécessaire.

![Version stable 0.1.10 après restauration sur .177](/images/dashboard-user-manager/ha-177-fr-0.1.10.png)

Capture réelle sur .177 le 20 octobre 2026, après restauration complète et mise à jour 0.1.10 : interface française, 18 vues et quatre utilisateurs. Le tableau de bord existant est inchangé.

## Filtrer et présélectionner les tableaux de bord

Depuis 0.1.6, une vue d’ensemble HA migrée n’apparaît qu’une fois : l’entrée `lovelace` et son ancien accès par défaut sont fusionnés. La présélection enregistrée par l’une des entrées est conservée. Les tableaux portant le même titre mais des chemins distincts restent séparés ; le titre seul n’identifie pas un doublon. Les anciennes sauvegardes restent compatibles. Cette logique suit la [correspondance de l’accès par défaut dans HA](https://github.com/home-assistant/core/blob/2026.10.2/homeassistant/components/lovelace/websocket.py).

![Présélection 0.1.5 avec cases à cocher sur .177](/images/dashboard-user-manager/selection-177-fr-0.1.5.png)

La liste ne contient que les tableaux chargés avec au moins une vue. Les entrées confirmées vides et les panneaux d’application sans vues sont masqués. Les erreurs sont affichées séparément par nom et ne sont pas considérées comme vides ; réessayez avec **Recharger**. Les tableaux YAML ou générés avec des vues restent indiqués en **lecture seule**.

**Présélection des tableaux de bord** ouvre une fenêtre avec une case par tableau disponible, **Tout sélectionner**, **Tout désélectionner**, **Annuler** et **Appliquer la présélection**. Seuls les éléments cochés apparaissent dans la liste. Le choix est enregistré par navigateur et adresse HA, sans modifier les tableaux ni les affectations. Une sélection vide est possible. Ajoutez les nouveaux tableaux à une présélection enregistrée si nécessaire. Les préférences antérieures sont conservées lors d’erreurs de chargement.

Conserver le tableau courant préserve les affectations non enregistrées. L’exclure demande confirmation avant de les abandonner. Si le stockage du navigateur est bloqué, une erreur est affichée et la présélection n’est pas annoncée comme enregistrée.

## Installation via UGSo HA Apps

Créez d’abord une sauvegarde HA complète. Ajoutez ce dépôt dans **Paramètres → Applications → Boutique d’applications → Dépôts** :

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Installez **Dashboard-Benutzerverwaltung**, démarrez-la et ouvrez-la via HA Ingress. Seuls les administrateurs HA actifs peuvent utiliser l’interface. Aucun port LAN supplémentaire ni jeton à saisir. Home Assistant avec Supervisor et un tableau de bord géré manuellement sont nécessaires. Les tableaux YAML et générés sont en lecture seule.

L’ajout du dépôt ne modifie pas une **application locale** existante. Les applications locale et issue du dépôt ont des identifiants et des données privées distincts. Avant de changer volontairement de source, créez une sauvegarde complète incluant l’ancienne application et téléchargez ses sauvegardes JSON. Ne désinstallez pas l’application locale sans préserver ses données ; utilisez une seule application à la fois pour les modifications.

## Affecter les utilisateurs

1. Choisissez un tableau de bord. Toutes ses vues, y compris les sous-vues, sont affichées.
2. Cochez par exemple **webuser** dans l’en-tête pour sélectionner cet utilisateur pour toutes les vues modifiables. Décochez l’en-tête pour le retirer de ces vues.
3. Corrigez les cases des vues individuelles. Un tiret dans l’en-tête indique une sélection partielle.
4. Cliquez sur **Enregistrer les modifications**. La sauvegarde et l’écriture ne se produisent qu’à ce moment. **Réinitialiser la sélection** abandonne uniquement les modifications non enregistrées.

**U vert = utilisateur, A rouge = administrateur.** Les rôles des comptes ne sont pas modifiés. Les noms d’origine, cartes, mises en page, chemins et vues non modifiées sont conservés. Les anciens identifiants d’utilisateurs ne sont pas supprimés silencieusement. Les vues modifiées utilisent des listes fixes ; les utilisateurs créés ultérieurement ne sont pas ajoutés automatiquement.

::: warning La visibilité ne constitue pas un contrôle d’accès
L’application contrôle la visibilité des onglets. Les URL directes restent accessibles ; elle ne remplace pas les droits HA. Voir la [documentation officielle HA](https://www.home-assistant.io/dashboards/views/#visible).
:::

## Délai, annulation et brouillon

Depuis 0.1.9, l’attente d’un enregistrement se termine au plus tard après 30 secondes. **Arrêter l’attente** l’interrompt plus tôt. Les cases cochées restent intactes ; **Télécharger le brouillon** conserve les affectations prévues dans un fichier JSON local. Il s’agit d’un relevé du brouillon, pas d’une sauvegarde complète ni d’un projet automatiquement réimportable. Le télécharger avant de fermer l’onglet.

Si aucune demande d’écriture n’a été envoyée, il est possible de réessayer après correction de la cause. Si le résultat est incertain, l’enregistrement reste bloqué : **Vérifier l’état du serveur** lit l’état réel et empêche l’exécution tardive d’un plan encore inutilisé. La vérification distingue le brouillon déjà enregistré, le serveur inchangé et les modifications concurrentes, sans réécrire. Elle est également limitée dans le temps et annulable. En cas de conflit, télécharger le brouillon avant de recharger volontairement.

L’annulation arrête uniquement l’attente locale ; une écriture déjà reçue par le serveur peut encore se terminer. Ne pas réessayer aveuglément. Un redémarrage de l’application peut nécessiter une nouvelle session : télécharger d’abord le brouillon, recharger la session puis reprendre volontairement les changements. Aucune réécriture automatique ; la fermeture/le rechargement ne conserve pas le brouillon sans le fichier téléchargé.

## Langue automatique

**Automatique (Home Assistant)** suit la langue de l’interface HA. Si le cadre HA ne peut pas être lu, la langue préférée du navigateur est utilisée. Les langues non prises en charge utilisent l’anglais. Vous pouvez aussi choisir DE, EN ou FR en haut ; cette préférence est enregistrée uniquement dans ce navigateur.

Les libellés, aides, dialogues, états, dates, textes d’accessibilité et messages du serveur sont traduits. Le changement de langue conserve les cases non enregistrées. Les noms personnalisés et données du tableau de bord ne sont jamais traduits. Aucun service de traduction en ligne ni clé supplémentaire n’est nécessaire.

## Sauvegardes et conflits

Avant chaque modification, un JSON complet est enregistré dans `/data/backups/`, dans le stockage privé de l’application. Utilisez **Télécharger le JSON** pour conserver une copie sur PC. Ces fichiers contiennent toutes les configurations des cartes et doivent rester confidentiels. Les mises à jour conservent ce stockage ; téléchargez les fichiers ou incluez l’application dans une sauvegarde HA avant désinstallation.

L’application compare le tableau de bord et les utilisateurs à l’état chargé, puis relit le résultat après l’écriture. Des changements intermédiaires bloquent l’enregistrement. HA ne propose pas de comparaison-et-écriture atomique : évitez toute modification simultanée dans un autre éditeur pendant l’enregistrement.

La restauration crée d’abord une nouvelle sauvegarde et est bloquée si le tableau de bord a été modifié depuis l’opération correspondante. Si l’enregistrement n’est pas confirmé, ne réessayez pas sans vérifier ; comparez l’état actuel avec la sauvegarde.

## Restaurer l’application ou une sauvegarde HA complète

Une sauvegarde HA complète doit inclure **Gestion des utilisateurs des tableaux de bord** dans les applications : elle contient les sauvegardes privées des tableaux. Les tableaux de bord eux-mêmes font partie de la configuration HA. Créer une sauvegarde complète récente avant toute restauration et éviter les changements concurrents.

Dans **Paramètres → Système → Sauvegardes**, ouvrir la sauvegarde choisie. Sélectionner uniquement l’application pour restaurer celle-ci et ses sauvegardes privées, sans changer la configuration actuelle des tableaux HA. Pour une restauration complète, sélectionner **Home Assistant**, paramètres/historique, dossiers concernés et toutes les applications nécessaires. Tout le périmètre sélectionné revient à l’instant de la sauvegarde, y compris la suppression des objets de test créés ensuite. HA est indisponible pendant son redémarrage.

Après la restauration, rouvrir l’application par la barre latérale HA. Vérifier sa version, les sauvegardes existantes, le nombre de vues/utilisateurs et la présélection du navigateur. Reprendre les modifications uniquement après confirmation du serveur. Conserver les sauvegardes complètes et JSON privés de manière confidentielle ; une présélection du navigateur ne remplace pas une sauvegarde.

## Mettre à jour une installation ZIP locale

Après une sauvegarde complète, copiez tous les nouveaux fichiers dans `/addons/dashboard_user_manager/`, puis exécutez dans le terminal HA :

```sh
touch /addons/dashboard_user_manager/config.yaml
ha store reload
ha apps info local_dashboard_user_manager
```

Quand `version_latest` indique la nouvelle version, lancez la mise à jour dans HA. `touch` modifie uniquement l’horodatage et aide Supervisor à détecter les fichiers issus d’anciens ZIP. Ne désinstallez pas l’application. Les applications issues d’un dépôt se mettent à jour via leur dépôt.

## Vérification et limites

**0.1.10 – Restauration vérifiée, mention expérimentale retirée :** Sauvegarde complète récente créée sur .177 le 20 octobre 2026. La restauration de l’application seule récupère les douze sauvegardes privées d’origine et retire le marqueur de test supplémentaire, sans changer la configuration HA actuelle. La restauration complète de HA 2026.10.2 inclut ensuite paramètres/historique, share, médias, SSL et toutes les applications. HA et l’application redémarrent ; « Test für APP » conserve 18 vues, quatre utilisateurs, la langue automatique et la présélection.

Après redémarrage, 21 fichiers HA, dont tous les fichiers Lovelace existants, sont identiques. Les deux autres registres vérifiés conservent les 22 appareils et 73 entités avec leurs réglages ; seuls les horodatages de modification et la version de l’application relevée par HA sont actualisés. Sept projets ATLAS, la gestion des plugins et la corbeille sont inchangés. La connexion ATLAS-HA existante fonctionne sans ressaisir les identifiants. La restauration complète retire le tableau de test créé après la sauvegarde. Ce test restaure l’installation existante ; il ne reconstruit pas un matériel vierge. 33 tests Python, 19 tests Node et les builds Docker amd64/aarch64 réussissent. 0.1.10 retire uniquement la mention expérimentale et actualise version/preuves ; logique d’enregistrement et droits inchangés. .68 et les systèmes de production n’ont pas été utilisés.

Une coupure exactement entre l’écriture HA et sa confirmation reste couverte uniquement par les tests automatisés ; aucune coupure réseau réelle à cet instant précis n’a été provoquée. Les consignes relatives aux écritures incertaines restent applicables.

![Application après restauration HA complète sur .177, tableau d’origine conservé, en allemand](/images/dashboard-user-manager/ha-177-full-restore-0.1.9.png)

### Vérifications précédentes – état à cette date

**Conflits et interruption de connexion vérifiés avec 0.1.8 sur .177 :** Après une sauvegarde complète, deux onglets ont ouvert le même tableau de bord de test distinct. L’onglet A a enregistré une modification ; le brouillon périmé de B a été refusé avec un message de conflit. Sa sélection est restée visible et l’état serveur de A est resté identique. Après réinitialisation/rechargement volontaire, la seconde modification a pu être enregistrée sans écraser la première.

Lors de l’arrêt contrôlé de l’application, un enregistrement en cours s’est terminé entièrement et a été confirmé. La tentative suivante, application arrêtée, n’a modifié aucune donnée. Après redémarrage, le message d’erreur de connexion/session est apparu, le brouillon a été conservé et aucune nouvelle écriture automatique n’a eu lieu. Après comparaison du serveur et rechargement, l’enregistrement volontaire fonctionnait à nouveau. Cartes, noms et sous-vue ont été conservés ; le tableau de bord de test a ensuite été supprimé.

**0.1.9 – Défaut de délai/annulation corrigé :** Installation sur .177 après une sauvegarde complète. Application totalement arrêtée, la limite locale de 30 secondes fonctionne ; l’annulation manuelle et les erreurs de connexion conservent aussi les deux lignes modifiées. Aucune demande d’écriture ; fichier serveur identique. Le brouillon téléchargé contient les deux affectations prévues, sans jeton. Après redémarrage et renouvellement de session, l’enregistrement volontaire réussit ; cartes, noms, chemins et sous-vue sont conservés. Tableau de test supprimé, présélection et langue automatique rétablies ; les quatre fichiers Lovelace existants, dont « Test für APP », sont identiques à la sauvegarde.

33 tests Python et 19 tests Node réussis : délai de requête/lecture de réponse, réponses tardives, annulation, écriture incertaine, comparaison serveur sans réécriture, conflits et confirmation perdue après une écriture HA terminée. Builds Docker amd64/aarch64 et CI UGSo réussis. Une coupure brutale exactement entre l’écriture HA et sa confirmation reste non démontrée en situation réelle ; ce scénario est testé automatiquement. La restauration complète application/sauvegarde HA reste ouverte ; le statut expérimental est conservé. .68 et les systèmes de production sont inchangés.

![Délai atteint et brouillon conservé – test réel 0.1.9 sur .177 en allemand](/images/dashboard-user-manager/ha-177-timeout-0.1.9.png)

![Enregistrement périmé refusé et brouillon conservé – test réel .177 en allemand](/images/dashboard-user-manager/ha-177-conflict-0.1.8.png)

**0.1.8 – Traduction de la confirmation corrigée :** La phrase complète et le nombre de vues utilisent une traduction unique DE/EN/FR, indépendamment de la langue de l’API. Le message déjà affiché suit les changements de langue sans rechargement. Le défaut de langue mixte signalé ci-dessous pour 0.1.7 est ainsi corrigé.

Mise à jour sur .177 après une sauvegarde complète, puis vérification avec un tableau de bord distinct de deux vues : trois enregistrements réels en DE/EN/FR et les changements de langue ultérieurs réussissent. Chaque enregistrement a modifié deux affectations sans toucher aux cartes ni aux noms. Langue automatique et présélection initiale rétablies ; sauvegardes existantes conservées. Les 28 tests Python et douze tests Node, dont une réponse API anglaise, les changements de langue ultérieurs et un résultat inchangé, réussissent. Builds Docker amd64/aarch64 et CI de l’application UGSo validés. .68 et systèmes de production inchangés. Le statut expérimental reste jusqu’à la fin des vérifications de restauration/conflits encore ouvertes.

![Confirmation d’enregistrement entièrement française sur .177 avec 0.1.8](/images/dashboard-user-manager/ha-177-save-fr-0.1.8.png)

**Enregistrement et restauration avec 0.1.7 validés sur .177 le 20 octobre 2026 :** Après une sauvegarde HA complète, un tableau de bord temporaire distinct comportant six vues a été testé. La sélection/désélection globale de webuser et une correction individuelle ont modifié exactement trois vues. Après enregistrement et rechargement, seules les listes d’utilisateurs prévues avaient changé. Les valeurs de visibilité non modifiées (`true`, `false`, `[]`), les cartes et leur contenu imbriqué, les chemins, la sous-vue et les noms d’origine avec espaces périphériques ont été conservés.

La sauvegarde automatique téléchargée contenait exactement la configuration complète d’origine. La restauration a d’abord créé une sauvegarde de l’état modifié, puis rétabli le fichier de stockage d’origine à l’octet près. Le tableau de bord temporaire a été supprimé, la présélection initiale rétablie et les quatre fichiers Lovelace existants, dont « Test für APP » et le catalogue, sont restés identiques. Trois sauvegardes complètes restent sur .177 ; les preuves privées de restauration et les sauvegardes PC sont conservées. .68 et les systèmes de production n’ont pas été modifiés.

![Restauration réussie du tableau de bord de test distinct sur .177 avec 0.1.7, interface allemande](/images/dashboard-user-manager/ha-177-restore-0.1.7.png)

La restauration complète de l’application depuis une sauvegarde HA et les tests réels de conflits/interruption restent à vérifier. Petit défaut d’affichage connu en 0.1.7 : le message de réussite de l’enregistrement peut contenir une phrase anglaise dans l’interface allemande ; celui de restauration était correctement en allemand. La vérification fonctionnelle est réussie.

Version 0.1.7 mise à jour sur .177 après une sauvegarde complète : icône visible dans la vignette HA et l’en-tête, contrôlé et photographié en DE/EN/FR. Présélection, 18 vues, quatre utilisateurs et sauvegarde privée existante conservés. Aucune affectation enregistrée ; les quatre fichiers Lovelace restent identiques à la sauvegarde. Les 28 tests Python, onze tests Node, la livraison PNG, la comparaison des icônes ZIP et les builds Docker amd64/aarch64 réussissent. Préférence de langue remise sur automatique.

**Confirmation de l’utilisateur du 20 octobre 2026 pour 0.1.6 :** La mise à jour sur l’installation concernée a réussi. « Übersicht aktuell » n’apparaît plus qu’une fois et la présélection enregistrée des tableaux de bord est conservée. Ce retour confirme la correction du cas signalé et complète les tests automatisés des alias/doublons ainsi que le test de mise à jour sur .177. Aucun accès supplémentaire de l’agent au système de production n’a été effectué pour cette confirmation.

Version 0.1.5 vérifiée sur .177 après une sauvegarde complète : carte vide masquée, erreur de la vue d’ensemble non configurée affichée séparément, annulation et sélection vide/réactivée conservée après rechargement. Dialogue contrôlé visuellement en DE/EN/FR. Aucune affectation enregistrée ; les quatre fichiers Lovelace restent inchangés. Les 26 tests Python, dix tests Node et les builds Docker amd64/aarch64 réussissent.

L’utilisateur a validé les affectations globales et individuelles, l’enregistrement et le rechargement de 0.1.3. Après une sauvegarde complète, l’application locale sur .177 a été mise à jour vers 0.1.4. La langue automatique suit allemand → anglais → français → allemand sans recharger l’application. Noms et affectations sont conservés ; les quatre fichiers Lovelace, dont « Test für APP », ont les mêmes empreintes SHA-256 que la sauvegarde après le test. Les tests hors ligne d’interface, d’API, de conservation et de conflits réussissent également. Aucun système de production n’a été modifié. La restauration complète d’une sauvegarde HA de l’application reste à vérifier. Une vue d’ensemble par défaut non configurée peut renvoyer `config_not_found` ; choisissez un tableau de bord manuel existant.

- [Code et paquet de l’application sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/fr/projects-mqtt/)
- [Deutsch](/projects/dashboard-user-manager/) · [English](/en/projects/dashboard-user-manager/)
