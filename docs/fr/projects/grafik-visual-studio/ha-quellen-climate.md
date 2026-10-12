---
title: Langues des widgets, sources HA et Climate
description: DE/EN/FR, attributs, unités et commandes climatiques facultatives depuis Studio 0.1.296.
---

# Langues des widgets, sources HA et Climate

Depuis **Studio 0.1.296**, les **62 types restants** (Spécial, jauges, flux de données et sept paquets inclus) proposent leurs propriétés et messages d’exécution en **DE/EN/FR**. L’interface générale du Studio reste DE/EN. [Deutsch](/projects/grafik-visual-studio/ha-quellen-climate) · [English](/en/projects/grafik-visual-studio/ha-quellen-climate).

## Choisir une langue

**Widget-Sprache** dans les paramètres du projet définit la langue par défaut. Le groupe **Langue du widget** peut la remplacer. Calendar+, Energy, Industrial, Printer, Solar, Technic et Weather/Heating fonctionnent avec les versions de paquet existantes. Les textes personnels, identifiants d’entité et clés enregistrées restent inchangés.

## Vérifier une source HA

Les sources liées en lecture proposent le groupe **Sources et unités HA**, initialement désactivé. Un attribut vide lit l’état ; sinon saisissez un attribut. **Vérifier la source** actualise la valeur, découvre les noms d’attribut et signale unité, données manquantes ou conversion incompatible. Les données structurées reçoivent une indication JSON. L’attribut doit correspondre au schéma attendu par le widget.

La conversion est facultative. Pour une source Energy, elle remplace l’ancien facteur sans le supprimer. Les affichages/calculs fixes suivent leur unité : Solar W/°C/%, énergie de batterie kWh, unité de température native Climate. Leur champ d’unité cible est verrouillé. Les sources configurables acceptent des unités compatibles de puissance, énergie, température, prix, longueur, volume, vitesse et pression. Sans métadonnées ou avec des unités incompatibles, la valeur est inconnue. Les cibles d’écriture HA restent natives.

Energy peut lire des attributs numériques Recorder ; un attribut manquant crée un espace dans l’historique. Des attributs historiques différents d’une même entité nécessitent des widgets de suivi séparés. La conversion C/F avec décalage ne s’applique pas à l’historique Energy. L’historique distinct du thermostat conserve ses sources HA natives ; les options de source concernent son affichage actuel. Recorder ne remplace pas entièrement le tableau de bord Énergie et les statistiques à long terme.

## Commandes climatiques

Activez **Commandes climatiques** sur **Technic Thermostat – Temperature**, puis choisissez les options nécessaires :

- Plage chauffage/refroidissement avec deux consignes et application commune.
- Mode de fonctionnement et préréglage.
- Ventilateur, oscillation verticale et horizontale.
- Humidité cible et marche/arrêt.

L’exécution propose uniquement les fonctions/valeurs annoncées par l’appareil. Limites et pas sont revérifiés côté serveur. La consigne unique existante reste disponible ; les appareils à deux consignes utilisent les commandes de plage. L’éditeur, la lecture seule et les états indisponibles désactivent les commandes. Agrandissez les widgets avec de nombreuses options ; la zone supplémentaire défile dans les petits widgets.

Les nouveaux groupes sont initialement désactivés. Projets, groupes et facteurs existants restent valides. Un service réussi confirme la transmission à HA, pas l’état physique de l’appareil. Appareils réels, Ingress/Companion, intégration de pages externes et réception des notifications nécessitent des tests sur l’installation.

[HA Climate](https://www.home-assistant.io/integrations/climate/) · [Fonctions des appareils](https://developers.home-assistant.io/docs/core/entity/climate/) · [Rapport de revue](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/remaining-widget-audit-2026-10-12.md)
