---
title: Calendar +
description: Ensemble de widgets de calendrier dédié, incluant la détection automatique des calendriers, une liste des événements et une fenêtre contextuelle
  (pop-up) pour les détails.
---

# Calendar + {#calendar}

**Calendar + 0.1.1** est un ensemble de widgets externe, créé par **rockbaer2007** pour **Grafik Visual Studio (version 0.1.267 ou ultérieure)**. Il détecte automatiquement tous les calendriers disponibles dans Home Assistant et affiche les événements à venir sous forme de carte compacte ou de liste détaillée. Par défaut, tous les calendriers sont activés.

L'environnement d'exécution avec des données d'exemple :

![Calendar + avec des tuiles de calendrier colorées, des regroupements par jour et une liste d'événements](/images/grafik-visual-studio/calendar-plus.png)

## Projet original {#originalprojekt}

Ce projet s'inspire de **[calendar-card-plus de xBourner](https://github.com/xBourner/calendar-card-plus)**, publié sous [licence MIT](https://github.com/xBourner/calendar-card-plus/blob/main/LICENSE), Copyright (c) 2026 xBourner. Calendar + utilise sa propre implémentation dans Studio ainsi qu'une icône de palette dédiée. Le code source et les éléments graphiques originaux ne sont pas inclus. Cet ensemble est indépendant de « Industrial » et de la carte Lovelace originale (utilisable séparément).

## Installation {#installieren}

1. Mettre à jour Studio vers la version **0.1.267 ou ultérieure**.
2. Télécharger [ugso.calendar-plus.wg](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/calendar-plus/ugso.calendar-plus.wg).
3. Procéder à l'installation via **Paramètres → Packs de widgets → Local**.
4. Faire glisser **Calendar + → Kalender +** depuis la palette vers la page.

Le pack contient des données déclaratives, une icône, une documentation et la licence MIT. Le moteur de rendu hôte (`calendar-plus`) est fourni par Studio ; le pack ne contient aucun script exécutable. [Code source et documentation du pack](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/calendar-plus).

## Mes calendriers {#meine-kalender}

Toutes les entités `calendar.*` disponibles sont détectées, y compris les calendriers ne figurant pas dans le registre. Les entrées désactivées dans le registre de Home Assistant sont ignorées. Sous **Mes calendriers**, une section dédiée s'affiche pour chaque calendrier, comprenant un identifiant d'entité, une **case à cocher en haut à droite** (pour afficher ou masquer le calendrier), une **couleur** et, en option, une **couleur d'arrière-plan**. Il n'est pas nécessaire de saisir manuellement le nombre de calendriers.

À partir de la version Studio **0.1.268**, le groupe est désormais intitulé **Paramètres des tuiles** (auparavant « Couleurs »). L'option **Taille des tuiles du calendrier** propose quatre tailles fixes : **Très petite 36 × 44 px**, **Petite 44 × 52 px**, **Moyenne 58 × 64 px** (par défaut) et **Grande 76 × 82 px**. Ce choix s'applique à la liste des événements ainsi qu'à la fenêtre contextuelle (pop-up) de détails. La taille du texte d'en-tête est d'au moins **12 px** et celle du chiffre du jour d'au moins **24 px**, indépendamment de la taille de police globale. Même les widgets étroits conservent la taille sélectionnée. Les paquets existants (0.1.0/0.1.1) bénéficieront de ces paramètres lors de la mise à jour de Studio ; aucune réinstallation n'est nécessaire. Le calendrier ne nécessite pas de configuration de flux de données ni de points d'entrée/sortie.

La sélection et les couleurs sont conservées en fonction de l'ID de l'entité. Les calendriers nouvellement ajoutés sont affichés automatiquement ; les calendriers masqués ne font l'objet d'aucune interrogation concernant les événements. Le nombre de calendriers détectés n'est pas limité. Les requêtes sont effectuées par groupes de 20 calendriers maximum via l'interface Home Assistant.

## Paramètres {#einstellungen}

À partir de la version Studio **0.1.270**, il est possible, via **Paramètres des tuiles → Rayon des coins des tuiles (px)**, de définir un rayon commun pour les quatre coins de la tuile de date : **0 = angles droits**, valeur par défaut **10 px**, maximum **100 px**. Ce paramètre s'applique également à la fenêtre contextuelle (pop-up) de détails.

Le calendrier et l'imprimante proposent désormais, sous **Propriétés → WIDGET**, toutes les sections CSS : **CSS Général**, **CSS Police et texte**, **CSS Arrière-plan**, **CSS Bordures** ainsi que **CSS Ombres et espacements**. Les quatre groupes supplémentaires sont désactivés par défaut afin de préserver l'affichage actuel. Cochez la case correspondant au groupe souhaité, puis configurez la police, l'arrière-plan/image, les bordures, le rayon, les ombres et les espacements. Ces paramètres définissent l'apparence de la zone visible ; le rayon extérieur, situé sous **CSS Bordures**, est indépendant du rayon des petites cases de date. Les couleurs spécifiques — telles que celles des calendriers ou les états de l'imprimante — conservent leurs propres paramètres de configuration. La section **CSS Général** reste active pour la gestion de la position, de la taille et de la visibilité. Aucun nouveau paquet n'est requis.

À partir de la version Studio **0.1.269**, les **paramètres des cases** incluent désormais la **taille de police en haut** (mois/jour de la semaine, jusqu'à 72 px) et la **taille de police en bas** (numéro du jour, jusqu'à 120 px). La valeur **0 = automatique** applique les paramètres par défaut liés à la taille de case choisie. Il est possible de définir des valeurs personnalisées plus petites ; celles-ci seront automatiquement ajustées en cas d'espace insuffisant. Les valeurs que vous avez enregistrées sont conservées, ce qui permet aux cases de plus grande taille d'utiliser, le cas échéant, une police plus grande.

La zone d'en-tête colorée s'adapte à la taille de la police supérieure et à un certain espacement interne, tout en restant limitée à **un tiers maximum de la hauteur de la tuile**. Le numéro du jour est intégré dans l'espace restant. La taille de la tuile demeure inchangée. Ces paramètres s'appliquent à la liste des événements ainsi qu'à la fenêtre contextuelle (pop-up) de détails et ne nécessitent pas de nouveau paquet de widgets.

| Zone | Paramètre |
| --- | --- |
| Configuration | Libellé, aperçu sur **1 à 90 jours**, **1 à 20** événements visibles, déploiement des événements, fenêtre contextuelle de détails, séparateurs. |
| Regroupement | Par jour, avec possibilité de regrouper également par calendrier ; option pour afficher les jours vides. |
| Événements à venir | Affichage/masquage des indications temporelles relatives telles que « Demain », « Dans 2 jours » ou « En cours ». |
| Texte et visibilité | Activation/désactivation individuelle du nom du calendrier, de la date, du lieu, de la durée, de l'heure et du jour de la semaine ; jour de la semaine en format complet ou abrégé ; inversion possible du mois et du jour de la semaine dans la tuile de date. |
| Paramètres des tuiles | Quatre tailles de tuiles, thème du navigateur (automatique ou fixe : clair/sombre), couleur d'accentuation et taille de police (**10 à 24 px**). Couleurs de calendrier et arrière-plans configurables séparément pour chaque calendrier. |
| Taille | Taille par défaut **480 × 460 px**, taille minimale **260 × 180 px** ; en cas d'espace restreint, la liste des événements devient défilante. |

Lorsque la liste n'est pas déployée, un événement reste visible. Lors de l'utilisation, un clic sur un événement ou sur « Tous les événements » ouvre la fenêtre contextuelle de détails, pouvant afficher jusqu'à 100 événements. Celle-ci présente la date complète, le lieu et la description (si disponible). Les textes sont affichés en format texte brut. **Fermer**, la touche Échap ou un clic en dehors de la fenêtre permettent de fermer le popup.

## Données et mise à jour {#daten-und-aktualisierung}

L'éditeur et le runtime récupèrent les événements via `calendar.get_events`. Pour les événements sur toute la journée, la date de fin est exclue ; les événements passés sont supprimés. La mise à jour automatique peut être désactivée sous **Configuration → Mise à jour automatique (60 s)** (activée par défaut). Lors de l'ouverture d'une page dans le runtime, le calendrier et les événements sont rechargés, même si la mise à jour automatique est désactivée. Le bouton **↻** permet une mise à jour manuelle ; la détection des calendriers est alors également actualisée.

Les mises à jour ne remplacent que les listes d'événements ; elles préservent la position de défilement ainsi que l'affichage d'une fenêtre de détails ouverte. Les changements d'état d'autres widgets « live » n'entraînent pas la reconstruction du calendrier (si celui-ci reste inchangé). La mise à jour s'arrête lorsque l'utilisateur quitte la page.

« Aucun calendrier trouvé », « Tous les calendriers masqués », « Aucun événement à venir » et une erreur de chargement correspondent à des états distincts. Une erreur n'est pas affichée comme un calendrier vide. La langue s'adapte automatiquement au paramètre **DE/EN** défini dans le Studio ; les libellés personnalisés et le contenu des événements restent inchangés.

## Contenu de cette version {#umfang-dieser-version}

Cette version permet de lire des événements (rendez-vous). Les fonctionnalités **Nouvel événement**, **Modifier** et **Supprimer** ne sont pas encore incluses. Les calendriers doivent être disponibles dans Home Assistant ; il n'existe pas de connexion directe aux fichiers ICS ou à Google Agenda. Il n'est pas nécessaire d'installer la carte originale via HACS.
