---
title: Widgets interactifs
description: Universal, curseur radial et comparaison Inventwo depuis Studio 0.1.295.
---

# Widgets interactifs

**Studio 0.1.296 :** Les **62 types restants** proposent des propriétés/messages DE/EN/FR, des commandes climatiques facultatives et une vérification des sources, attributs et unités. Projets et versions de paquet existants restent valides ; les nouveaux groupes sont initialement désactivés. [Guide et limites](./ha-quellen-climate). Les tests simulés ne valident pas les appareils réels/Companion. [Rapport](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/remaining-widget-audit-2026-10-12.md).

**Studio 0.1.295** ajoute les grandes fonctions de la [comparaison Inventwo VIS-2](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/inventwo-interactive-audit-2026-10-12.md). [Deutsch](/projects/grafik-visual-studio/interaktiv) · [English](/en/projects/grafik-visual-studio/interaktiv).

## Universal

En plus de la commutation et des cycles existants : valeur fixe, maintien avec restauration de la valeur précédente, augmenter/diminuer avec limites, navigation vers des pages Studio, fenêtres configurables et requêtes HTTP. Les anciens boutons conservent leur cycle tant qu’une nouvelle option n’est pas choisie. Groupes et réglages conservés.

Contenus par défaut/par état : **Vue intégrée**, **Sélecteur de couleur** et **Horloge analogique**. Les vues peuvent s’adapter à la taille ; les récursions sont empêchées. Zone/cercle de couleur, curseurs HSV/RGB, alpha/Kelvin facultatifs. HEX, HEX8, RGB, HSL, HSV et CIE xy peuvent être écrits dans un assistant texte ; les lumières HA reçoivent des commandes RGB/Kelvin validées. Alpha concerne HEX8, pas RGB HA. L’horloge utilise l’heure du navigateur avec chiffres/trotteuse et couleurs configurables.

**Langue interactive** choisit DE/EN/FR pour Universal et les curseurs radiaux, sans traduire les textes utilisateur, noms d’entités/pages ou valeurs techniques.

## Curseur radial et aperçus

Piste, piste active et curseur acceptent couleurs CSS ou `linear-gradient(90deg, red, rgb(255,200,0) 50%, green)`, positions en pourcentage et directions comme `to top`. Héritage des styles et anciennes couleurs conservés.

Les aperçus interactifs remplissent leur cadre depuis 0.1.294. Depuis 0.1.295 les icônes Material et leur symbole sont aussi agrandis dans la barre latérale et le sélecteur. Seule la mise à jour Studio est nécessaire.

## Comportement et limites

HTTP GET fonctionne dans le navigateur, avec délai de 15 secondes, sans identifiants Studio ni proxy serveur. CORS et restrictions HTTP/HTTPS s’appliquent. Le PIN de navigation est une barrière d’interface enregistrée dans le projet, pas une autorisation. Un arrêt du navigateur/réseau peut empêcher la restauration du maintien ; prévoir un délai HA pour les appareils critiques.

Studio utilise les entités HA et pages du projet. Les liaisons ioBroker arbitraires des composantes de couleur et tous les détails d’horloge ne sont pas reproduits ; aucune égalité parfaite des pixels n’est promise. L’interface globale reste DE/EN. [Guide détaillé DE/EN/FR](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/universal-0.1.295.md).
