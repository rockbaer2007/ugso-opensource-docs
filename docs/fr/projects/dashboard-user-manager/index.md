---
title: Gestion des utilisateurs des tableaux de bord
description: Affecter des utilisateurs à toutes les vues HA ou individuellement, avec sauvegardes et DE/EN/FR.
---
# Gestion des utilisateurs des tableaux de bord

**Version 0.1.4 · DE / EN / FR · MIT · expérimental**

Une application HA indépendante : choisissez un tableau de bord, affichez les utilisateurs en colonnes et les vues en lignes, puis modifiez les affectations par cases à cocher. ATLAS n’est pas nécessaire. L’interface utilise 90 vw et 90 vh, des noms verticaux, des colonnes étroites et un défilement horizontal si nécessaire.

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

L’utilisateur a validé les affectations globales et individuelles, l’enregistrement et le rechargement de 0.1.3. La version 0.1.4 ajoute des catalogues et les vrais scripts d’interface testés hors ligne en DE/EN/FR, ainsi que des tests API, de conservation et de conflits. Aucun système de production n’a été modifié pour cette traduction. La restauration complète d’une sauvegarde HA de l’application reste à vérifier. Une vue d’ensemble par défaut non configurée peut renvoyer `config_not_found` ; choisissez un tableau de bord manuel existant.

- [Code et paquet de l’application sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/main/dashboard_user_manager)
- [UGSo HA Apps](/fr/projects-mqtt/)
- [Deutsch](/projects/dashboard-user-manager/) · [English](/en/projects/dashboard-user-manager/)
