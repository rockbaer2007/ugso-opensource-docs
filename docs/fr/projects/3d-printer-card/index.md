---
title: 3D Printer Card
description: Carte compacte Home Assistant pour Klipper et Moonraker avec profils, caméra et courbes de température.
---

# 3D Printer Card

[Deutsch](/projects/3d-printer-card/) · [English](/en/projects/3d-printer-card/)

**Version 0.1.7. Fonctionne uniquement avec Klipper et Moonraker.** L'[intégration Moonraker](https://github.com/marcolivierarsenault/moonraker-home-assistant) doit être installée et configurée pour chaque imprimante. La carte utilise ses entités HA sans identifiants ni connexion supplémentaires.

## Installation

[![Ouvrir dans Marketplace](/images/3d-printer-card/marketplace.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=3d-printer-card&category=plugin)

1. Sauvegardez les paramètres. Installez et configurez l'[intégration Moonraker dans Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=marcolivierarsenault&repository=moonraker-home-assistant&category=integration).
2. Ajoutez `https://github.com/rockbaer2007/3d-printer-card` comme dépôt personnalisé **Dashboard** dans Marketplace et téléchargez-le. Pas encore au catalogue Marketplace par défaut.
3. Vérifiez la ressource `/hacsfiles/3d-printer-card/3d-printer-card.js`, de type **module JavaScript**, puis rechargez le navigateur. Remplacez l'ancienne ressource locale sans charger les deux versions.
4. Ajoutez **3D Printer Card**. Le type reste `custom:moonraker-display-card`.

Installation manuelle : copiez le fichier JS dans `/config/www/3d-printer-card/` et enregistrez `/local/3d-printer-card/3d-printer-card.js?v=0.1.7` comme module JavaScript. Aucun redémarrage HA nécessaire. Remplacez toutes les entités d'exemple.

## Affichage et profils

- État, fichier, progression, durées écoulée/restante/estimée, heure de fin, couches, vitesse, ventilateur et messages.
- Températures réelle/cible de la buse et du plateau dans un graphique ; températures réelles de la carte et du pad dans un autre. L'historique nécessite ces entités dans HA Recorder.
- Caméra à droite sur environ un tiers de la largeur, miniature optionnelle. Sur petit écran, les éléments sont empilés.
- Champs compacts, graphiques peu hauts, largeur initiale de 24 colonnes et hauteur automatique. Utilisez une vue en sections ; une vue panneau impose la pleine largeur.
- Jusqu'à 20 profils avec leurs propres entités et caméras.

Dans l'éditeur, ouvrez **Profil hinzufügen** (ajouter) ou **Profil bearbeiten** (modifier). Sélectionnez le capteur `current_print_state` dans **Drucker erkennen** pour détecter le préfixe. Adaptez les caméras et correspondances avec les sélecteurs HA natifs. Cliquez sur **Profil übernehmen**, puis **Speichern** dans l'éditeur principal. Éditeur actuellement en allemand ; documentation DE/EN/FR. Les profils existants restent compatibles.

## Annulation et vérifications

La seule commande est l'annulation d'une impression active/en pause sur une imprimante prête, via le bouton HA existant, avec confirmation et nouvelle vérification de l'état. Changer de profil n'envoie aucune commande. Pas de consommation de filament ni de statistiques globales.

Affichage, caméra, graphiques et modification des profils vérifiés avec des entités réelles sous HA 2026.11.3, paramètres conservés. Également 16 tests automatisés et essais navigateur à 390, 800 et 1500 pixels sans débordement ni appel de service involontaire. Aucune impression réelle en cours n'a été annulée pendant les essais.

## Téléchargements

Messages de forum prêts à copier : [Deutsch](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forenbeitrag-de.md) · [English](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forum-post-en.md).

- [GitHub et guide complet](https://github.com/rockbaer2007/3d-printer-card)
- [Release 0.1.7 avec ZIP et JavaScript](https://github.com/rockbaer2007/3d-printer-card/releases/tag/v0.1.7)
- [Historique des modifications](https://github.com/rockbaer2007/3d-printer-card/blob/main/CHANGELOG.md)

Licence MIT. Projet frontend indépendant de l'intégration Moonraker.
