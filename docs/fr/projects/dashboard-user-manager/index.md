---
title: Gestion des utilisateurs des tableaux de bord
description: Affecter des utilisateurs à toutes les vues HA ou individuellement, avec sauvegardes et DE/EN/FR.
---
# Gestion des utilisateurs des tableaux de bord

**Version 0.1.7 · DE / EN / FR · MIT · expérimental**

<img src="/images/dashboard-user-manager/icon.png" width="96" height="96" alt="Icône avec tableau, utilisateurs et coches" />

Depuis 0.1.7, l’icône PNG intégrée apparaît dans la vignette HA et l’en-tête de l’interface et sert de favicon de l’application. Le motif approuvé est inclus dans le ZIP et le paquet UGSo sans service d’images externe. La barre latérale HA conserve son symbole MDI configuré. Paramètres, présélection enregistrée et données des tableaux de bord sont conservés pendant la mise à jour de l’icône.

Une application HA indépendante : choisissez un tableau de bord, affichez les utilisateurs en colonnes et les vues en lignes, puis modifiez les affectations par cases à cocher. ATLAS n’est pas nécessaire. L’interface utilise 90 vw et 90 vh, des noms verticaux, des colonnes étroites et un défilement horizontal si nécessaire.

![Gestion des utilisateurs 0.1.7 avec son icône sur le système HA de test .177](/images/dashboard-user-manager/ha-177-fr-0.1.7.png)

Capture réelle du système de test .177, le 20 octobre 2026 : icône intégrée, interface française, 18 vues et quatre utilisateurs. Le tableau de bord existant n’a pas été modifié pour cette capture.

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

## Langue automatique

**Automatique (Home Assistant)** suit la langue de l’interface HA. Si le cadre HA ne peut pas être lu, la langue préférée du navigateur est utilisée. Les langues non prises en charge utilisent l’anglais. Vous pouvez aussi choisir DE, EN ou FR en haut ; cette préférence est enregistrée uniquement dans ce navigateur.

Les libellés, aides, dialogues, états, dates, textes d’accessibilité et messages du serveur sont traduits. Le changement de langue conserve les cases non enregistrées. Les noms personnalisés et données du tableau de bord ne sont jamais traduits. Aucun service de traduction en ligne ni clé supplémentaire n’est nécessaire.

## Sauvegardes et conflits

Avant chaque modification, un JSON complet est enregistré dans `/data/backups/`, dans le stockage privé de l’application. Utilisez **Télécharger le JSON** pour conserver une copie sur PC. Ces fichiers contiennent toutes les configurations des cartes et doivent rester confidentiels. Les mises à jour conservent ce stockage ; téléchargez les fichiers ou incluez l’application dans une sauvegarde HA avant désinstallation.

L’application compare le tableau de bord et les utilisateurs à l’état chargé, puis relit le résultat après l’écriture. Des changements intermédiaires bloquent l’enregistrement. HA ne propose pas de comparaison-et-écriture atomique : évitez toute modification simultanée dans un autre éditeur pendant l’enregistrement.

La restauration crée d’abord une nouvelle sauvegarde et est bloquée si le tableau de bord a été modifié depuis l’opération correspondante. Si l’enregistrement n’est pas confirmé, ne réessayez pas sans vérifier ; comparez l’état actuel avec la sauvegarde.

## Mettre à jour une installation ZIP locale

Après une sauvegarde complète, copiez tous les nouveaux fichiers dans `/addons/dashboard_user_manager/`, puis exécutez dans le terminal HA :

```sh
touch /addons/dashboard_user_manager/config.yaml
ha store reload
ha apps info local_dashboard_user_manager
```

Quand `version_latest` indique la nouvelle version, lancez la mise à jour dans HA. `touch` modifie uniquement l’horodatage et aide Supervisor à détecter les fichiers issus d’anciens ZIP. Ne désinstallez pas l’application. Les applications issues d’un dépôt se mettent à jour via leur dépôt.

## Vérification et limites

Version 0.1.7 mise à jour sur .177 après une sauvegarde complète : icône visible dans la vignette HA et l’en-tête, contrôlé et photographié en DE/EN/FR. Présélection, 18 vues, quatre utilisateurs et sauvegarde privée existante conservés. Aucune affectation enregistrée ; les quatre fichiers Lovelace restent identiques à la sauvegarde. Les 28 tests Python, onze tests Node, la livraison PNG, la comparaison des icônes ZIP et les builds Docker amd64/aarch64 réussissent. Préférence de langue remise sur automatique.

**Confirmation de l’utilisateur du 20 octobre 2026 pour 0.1.6 :** La mise à jour sur l’installation concernée a réussi. « Übersicht aktuell » n’apparaît plus qu’une fois et la présélection enregistrée des tableaux de bord est conservée. Ce retour confirme la correction du cas signalé et complète les tests automatisés des alias/doublons ainsi que le test de mise à jour sur .177. Aucun accès supplémentaire de l’agent au système de production n’a été effectué pour cette confirmation.

Version 0.1.5 vérifiée sur .177 après une sauvegarde complète : carte vide masquée, erreur de la vue d’ensemble non configurée affichée séparément, annulation et sélection vide/réactivée conservée après rechargement. Dialogue contrôlé visuellement en DE/EN/FR. Aucune affectation enregistrée ; les quatre fichiers Lovelace restent inchangés. Les 26 tests Python, dix tests Node et les builds Docker amd64/aarch64 réussissent.

L’utilisateur a validé les affectations globales et individuelles, l’enregistrement et le rechargement de 0.1.3. Après une sauvegarde complète, l’application locale sur .177 a été mise à jour vers 0.1.4. La langue automatique suit allemand → anglais → français → allemand sans recharger l’application. Noms et affectations sont conservés ; les quatre fichiers Lovelace, dont « Test für APP », ont les mêmes empreintes SHA-256 que la sauvegarde après le test. Les tests hors ligne d’interface, d’API, de conservation et de conflits réussissent également. Aucun système de production n’a été modifié. La restauration complète d’une sauvegarde HA de l’application reste à vérifier. Une vue d’ensemble par défaut non configurée peut renvoyer `config_not_found` ; choisissez un tableau de bord manuel existant.

- [Code et paquet de l’application sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/fr/projects-mqtt/)
- [Deutsch](/projects/dashboard-user-manager/) · [English](/en/projects/dashboard-user-manager/)
