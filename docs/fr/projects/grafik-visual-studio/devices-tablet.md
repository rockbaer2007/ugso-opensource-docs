---
title: Appareils et tablette
description: Tuiles, marqueurs sur plan, retour de tablette et capacités des paquets dans Studio 0.1.297.
---

# Appareils et tablette

**Studio 0.1.297** ajoute le groupe intégré **Appareils** dans la palette. Aucune installation de paquet supplémentaire nécessaire. [Mise à jour GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-visual-studio-v0.1.297).

## Ajouter des appareils

Développer le groupe, glisser un widget sur la surface puis choisir son entité HA dans les propriétés. **Interrupteur, variateur, lumière colorée, thermostat et mesure** existent en **tuile** et en **marqueur sur plan avec fenêtre contextuelle** : dix entrées. Position et dimensions restent libres ; il ne s’agit pas d’une grille adaptative automatique. Les cinq groupes CSS standard sont disponibles ; les nouveaux groupes optionnels restent désactivés. Langues des widgets : DE/EN/FR ; interface générale de Studio : DE/EN.

![Tuiles et marqueurs sur plan, démonstration locale](/images/grafik-visual-studio/devices-desktop-297.jpg)

| Widget | Source et commandes |
| --- | --- |
| Interrupteur | `switch`, `light` ou `input_boolean` ; marche/arrêt |
| Variateur | `light` ; luminosité selon les capacités HA |
| Lumière colorée | `light` ; marche/arrêt, luminosité et RGB selon les modes pris en charge |
| Thermostat | `climate` ; consigne unique respectant limites et pas natifs |
| Mesure | État et unité ; lecture seule |

Le mode d’exécution propose uniquement les commandes prises en charge par l’entité. **Lecture seule** interdit l’écriture. L’éditeur ne commande aucun appareil ; les entités indisponibles sont désactivées. La validation serveur reste active. Une requête acceptée ne confirme pas le retour physique de l’appareil. Pour les fonctions avancées comme les plages de température, utiliser [Technic/Climate](./ha-quellen-climate).

## Retour de tablette et page d’accueil

Dans **Paramètres → Général**, l’option d’actualisation au retour de la tablette recharge les valeurs HA lorsque la page redevient visible, est restaurée ou retrouve le réseau. La page entière n’est pas rechargée. Les temporisateurs suspendus par le navigateur ou la tablette sont pris en compte au retour.

Le délai et la page d’accueil après inactivité désignent une page visible du projet courant. **0 seconde = désactivé**, valeur par défaut. Les dialogues ouverts, écritures en cours et modifications actives reportent la navigation. Aucun réglage kiosque ni droit d’accès n’est modifié.

![Vue à 1280 × 800, démonstration locale](/images/grafik-visual-studio/devices-tablet-297.jpg)

![Fenêtre de lumière sur tablette, démonstration locale](/images/grafik-visual-studio/devices-tablet-popup-297.jpg)

## Valeurs dans les titres

Les titres des cadres et appareils peuvent afficher un état HA ou un attribut, avec décimales et unité. Sélectionner l’entité et l’attribut éventuel dans le groupe de propriétés correspondant. Les titres existants sont conservés ; les valeurs HA sont insérées comme texte.

## Rendu et capacités des paquets

Appareils, météo, pièces chauffées, vue des fenêtres, notification au propriétaire, listes d’états Technic et palettes Material chargent leurs modules de rendu à la demande. Les modules communs de l’éditeur restent chargés normalement. Les demandes simultanées partagent un chargement.

Les manifestes installés sont vérifiés toutes les **30 secondes** et au retour. Les modifications actualisent la palette sans redémarrage. Cela n’installe pas automatiquement les mises à jour proposées dans le catalogue. Un remplacement invalide conserve le catalogue précédent ; les définitions retirées restent en mémoire pour les projets ouverts mais disparaissent de la palette des nouveaux widgets. Les projets ne sont pas migrés automatiquement. Voir [l’installation des paquets](./widget-packages).

`optionalCapabilities` est une déclaration optionnelle du manifeste : `entity-state`, `history`, `light-color`, `climate`. La liste indique leur prise en charge. Une capacité inconnue ne donne aucun droit. Les anciens manifestes restent valides ; les commandes dépendent toujours de HA et des capacités de l’entité.

![Import avec deux widgets et affichage des capacités sur .177](/images/grafik-visual-studio/package-import-297.jpg)

## Vérification et limites

Le **8 novembre 2026**, tests sur **.177 / HA 2026.11.0 / Raspberry Pi 5 ARM64** et **.193 / HA 2026.10.4 / Proxmox amd64** : sauvegarde/rechargement du projet, commande réelle d’un assistant HA temporaire avec retour d’état et retour après inactivité. Sur .177, dialogue du marqueur et import local manuel du paquet 1.1.0 avec deux widgets et affichage des capacités également vérifiés. Paquet et assistants de test ensuite supprimés ; délai remis à 0 seconde. Studio reste installé sur les deux systèmes, projets et réglages existants conservés.

Luminosité, RGB et thermostat testés avec des entités locales simulées. Vues contrôlées dans un navigateur de bureau à 1440 × 1000 et dans une vue tablette à 1280 × 800. Cela ne confirme ni une tablette physique ni tous les types de lampes/chauffages. 394 vérifications JavaScript et 109 Python réussies, plus 7 vérifications JavaScript ciblées et 17 Python pour les paquets. [Rapport technique](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/devices-tablet-0.1.297.md).

Implémentation HA indépendante sans code ni illustrations VIS-2 copiés. Web Components et conteneur de grille adaptative restent des projets ultérieurs distincts.
