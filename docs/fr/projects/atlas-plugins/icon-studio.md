---
title: ATLAS Icon Studio
description: Gérer, importer, supprimer et enregistrer des jeux d’icônes Home Assistant avec ATLAS Icon Studio.
---
# ATLAS Icon Studio

ATLAS Icon Studio est un plugin installé séparément pour créer et gérer des jeux d’icônes Home Assistant avec le préfixe `atlas:`. La version 0.1.15 prend en charge les grandes collections sans limite fixe du nombre d’icônes ; la liste affiche 24 éléments à la fois.

## Gestion des icônes

Version actuelle du plugin : **0.1.17**. Elle corrige un import de validation
manquant lors de la création de texte dans le dessin. La version 0.1.16 avait
corrigé le démarrage du sélecteur d’export. Les formats de stockage restent inchangés.

La collection est dans IndexedDB local au navigateur. Les anciennes données
sont reprises ; exporter en JSON avant de changer de navigateur ou d’adresse.

## Dessin et aperçu d’images

Une zone séparée crée des SVG en couleur avec formes, dessin libre et texte,
ordre des calques et dix étapes d’annulation/rétablissement au maximum.
Enregistrer sous exporte SVG, PNG ou WebP, avec fond transparent en option.
Les images matricielles peuvent être affichées et vectorisées en option, mais
ne deviennent pas directement des icônes `atlas:` ; le jeu HA nécessite des
chemins SVG. File Studio transmet les images prises en charge à Icon Studio sur
le même serveur ATLAS. Les téléchargements ne sont pas copiés automatiquement dans HA.

## Modifier la collection

Sélectionnez une icône dans la collection et utilisez **Supprimer l’icône**. Icon Studio sélectionne ensuite automatiquement la prochaine icône supprimable. Vous pouvez ainsi en supprimer plusieurs à la suite sans devoir en sélectionner une après chaque suppression. L’icône de référence `atlas:home` est protégée et ne peut pas être supprimée. La collection conserve toujours au moins une icône.

La recherche, la navigation au clavier et l’export portent sur toute la collection, même si seule une petite partie est affichée. Les collections peuvent être sauvegardées et restaurées au format JSON ; les conflits de noms peuvent être remplacés, ignorés ou renommés automatiquement.

## Home Assistant

Les jeux d’icônes peuvent être exportés localement sous `atlas-iconset.js` ou lus directement depuis `/config/www/atlas-iconset.js` avec File Studio. Lors de l’enregistrement, vous pouvez remplacer le fichier existant ; File Studio crée d’abord une sauvegarde. Icon Studio peut aussi créer un nouveau fichier numéroté et afficher son chemin de ressource `/local/...` à enregistrer dans Home Assistant. L’accès direct nécessite que `/config/www` soit autorisé dans File Studio.

Consultez le [README du plugin](https://github.com/rockbaer2007/atlas-icon-studio-plugin#readme) pour les détails d’installation, de formats et de chemins.

## Restauration sécurisée du plugin

Sauvegarder la collection en JSON, exporter le jeu d’icônes et enregistrer
séparément les dessins en SVG. Dans **Administration → Gestionnaire de plugins →
Icon Studio → Restaurer**, choisir une sauvegarde et vérifier version/compatibilité.
L’action d’application sauvegarde aussi le plugin actuel. Annuler le conserve.

::: info Vérification isolée du 16/10/2026
Avec ATLAS 0.1.312 : **0.1.16 → 0.1.17**, puis **0.1.17 → 0.1.16 → 0.1.17
sauvegardée**, redémarrage compris. Les douze fichiers correspondent aux paquets.
Une collection de 131 icônes et un dessin avec deux textes sont conservés dans
le même profil et à la même origine. Les nouveaux exports JSON, JavaScript et
SVG sont identiques octet par octet. Création de texte, duplication et annulation
fonctionnent. Fichiers de test, jeu existant, projet, autre plugin, corbeille et
historique sont conservés. Dépôts, données serveur et exports du navigateur ont
été sauvegardés avant les changements. **Pi 5 et Proxmox n’ont été ni interrogés
ni modifiés pendant cet essai isolé.** Les migrations de format restent distinctes.
:::

::: info Vérification sur Pi 5 et Proxmox le 16/10/2026
Après sauvegardes HA locales, copies de fichiers sur PC et exports du navigateur,
l’administration a validé **0.1.16 → 0.1.17 → 0.1.16 d’origine → 0.1.17**.
Les douze fichiers du paquet correspondent ; paramètres, fichiers existants,
six plugins actifs, projet, corbeille et historique sont conservés. ATLAS 0.1.312
et HA 2026.10.1 ne nécessitent aucun redémarrage. Les deux systèmes terminent
avec Icon Studio 0.1.17. Si un aperçu de mise à jour périmé est refusé après une
restauration, recharger l’administration puis sélectionner à nouveau la mise à jour.
Accès direct et HA Ingress vérifiés sur chaque hôte : trois icônes de référence
et un brouillon vide par contexte. Le JSON de collection reste identique octet
par octet et le brouillon est inchangé après rechargement. Création de texte et
annulation fonctionnent. Les grandes collections et dessins remplis ont été
vérifiés dans l’essai isolé.
:::

Restaurer le paquet ne restaure pas les données supprimées du navigateur.
IndexedDB et le brouillon local dépendent du profil et de l’origine (protocole,
hôte et port). Une sauvegarde HA/serveur ne contient pas ces données. JSON de
collection et JavaScript d’icônes excluent les dessins en couleur ; le SVG
exporté n’est pas une sauvegarde complète du brouillon modifiable et des annulations.
Formes et nom du fichier courant persistent localement ; outils, recherche et
historique d’annulation/rétablissement appartiennent à la session.
