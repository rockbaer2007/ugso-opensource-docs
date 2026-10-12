---
title: Material Design
description: Material Design 1.1.0 pour Studio 0.1.292 avec DE/EN/FR et mises à jour compatibles.
---

# Material Design

Depuis **Studio 0.1.295**, les icônes et leur symbole remplissent le cadre de la barre latérale et du sélecteur. Graphiques et réglages conservés ; aucune mise à jour du paquet nécessaire. [Nouveautés interactives](/fr/projects/grafik-visual-studio/interaktiv).

**Paquet 1.1.0 · Studio 0.1.292 ou plus récent · 49 widgets · MIT.** Moteurs indépendants inspirés de [ioBroker VIS2 Material Design de typhosj/Scrounger](https://github.com/typhosj/ioBroker.vis2-materialdesign). Les icônes MDI originales restent des SVG locaux. Identifiant technique : <code>ugso.materialdesign</code>.

[Deutsch](/projects/grafik-visual-studio/materialdesign) · [English](/en/projects/grafik-visual-studio/materialdesign) · [Code source](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign)

## Installation et conservation des réglages

1. Exporter le projet Studio existant en JSON.
2. Mettre Studio à jour vers **0.1.292 ou plus récent**, puis redémarrer.
3. [Télécharger Material Design 1.1.0](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/dist/ugso.materialdesign-1.1.0.wg). Installer via **Paramètres → Paquets de widgets → Local**, ou le lien direct du fichier GitHub.
4. La mise à jour est additive. Recharger la page et vérifier le projet existant.

L’installation **ne réécrit aucun fichier de projet**. Champs, valeurs par défaut, ordre et identifiants techniques restent protégés. De nouveaux champs/groupes et choix sont ajoutés. Couleurs, textes, dimensions, entités et groupes désactivés restent enregistrés. Les anciens paquets publiés restent disponibles.

Les anciens widgets **State Multi** conservent leur cycle. Le mode multicible se choisit explicitement. Les anciennes Advanced Views gardent leurs associations ; noms/ID et indices numériques sont des modes supplémentaires. Les nouveaux widgets incluent les modes de l’original. Changer de style ne modifie pas les cibles.

## Langues et apparence

**Langue Material** suit Studio ou choisit **allemand, anglais ou français** pour le widget et ses propriétés Material. Les textes personnels et identifiants ne sont pas traduits. L’interface générale du Studio reste DE/EN ; le français concerne ici Material.

**Classique**, **Material 3** et **Défaut du projet** restent disponibles. Les couleurs suivent la page ou imposent Clair/Sombre. Couleurs, tailles et espacements explicites restent prioritaires. L’aperçu conserve les 26 palettes et le fond blanc classique de l’original.

## Widgets et fonctions proches de l’original

| Famille | Fonctions et commandes |
| --- | --- |
| Buttons / Icon Buttons | Textes/couleurs/icônes d’état, couleur à l’appui, bouton momentané, addition bornée, nouvelle fenêtre, navigation et déverrouillage temporisé |
| State Multi | Ancien cycle ou plusieurs entités avec valeurs et délais distincts |
| Checkbox / Switch | Valeurs MARCHE/ARRÊT ou mode booléen, position du libellé et véritable interrupteur |
| Input / Select / Autocomplete | Formes, affixes, aide/compteur, icônes, survol/sélection, clavier et masque : # = chiffre, A = lettre, * = lettre/chiffre |
| Slider / Slider Round | Poignée/piste, limites/pas, graduations, entité de travail, écriture pendant l’utilisation ou au relâchement, arc/angle initial |
| Progress | Linéaire/circulaire, déterminé/indéterminé, taille/rotation, seuils de couleurs et texte |
| Value / Icon / Version | Nombre/booléen/texte/date/durée, facteur/décalage, conditions, lien et effet ; icône statique ou d’état ; version réelle |
| HTML Card | Titre/sous-titre, image, dispositions, couleurs, actualisation d’image et HTML isolé |
| List / Icon List / Table / Alerts | Sous-textes, navigation/liens/commandes, barres d’état JSON, images, formatage, en-tête fixe, tri et acquittement |
| Quatre graphiques | Barres, secteurs/anneau, JSON et Recorder ; quatre axes Y, piles, remplissage/escaliers, infobulles, valeurs, palettes et légendes |
| Calendar | Mois/semaine/jour/année/liste, numéros de semaine, couleurs et grille horaire en DE/EN/FR |
| Top App Bar | Panneau modal/permanent/automatique, sous-entrées et index sélectionné ; anciens liens conservés dans un mode séparé |
| Grid/Masonry / Advanced Views | Colonnes adaptatives, visibilité par vue, associations/nom/index, booléens 0/1, préchargement et conservation des vues |

**Afficher les options avancées** révèle les détails sans supprimer les valeurs masquées. Définir le nombre de cibles, vues, séries ou entrées souhaité.

## Home Assistant et données

Actions HA validées : <code>switch/input_boolean</code>, <code>number/input_number</code>, <code>text/input_text</code>, <code>select/input_select</code>, <code>button/input_button</code> avec <code>PRESS</code>, luminosité, pourcentage de ventilateur et position de volet. États, options et plages sont vérifiés. Capteurs, attributs et entités indisponibles restent en lecture seule.

Les actions multicibles sont séquentielles et s’arrêtent en cas d’erreur ou de changement de page. Les actions déjà exécutées ne sont pas annulées. Les services HA arbitraires et expressions ioBroker exécutables ne sont pas proposés.

Top App Bar en **mode État** écrit son index dans l’entité. **Advanced View in Widget 8**, avec la même entité et le **mode Index**, affiche la page Studio correspondante. Sans entité, utiliser le flux de données Studio existant ; les valeurs locales d’aperçu séparées ne sont pas partagées automatiquement.

Les listes lisent des lignes d’éditeur ou du JSON ; les tableaux utilisent les clés configurées. Le HTML facultatif des listes est nettoyé : sans scripts, gestionnaires d’événements ni contenus intégrés actifs. Les cartes HTML restent isolées. Les sites externes peuvent bloquer les iFrames.

Recorder est limité à **dix entités et 1–168 heures**. Les graphiques lisent <code>axisLabels/graphs</code>, <code>labels/datasets</code> ou des points. L’axe X respecte les intervalles réels. Agrégation : aucune, moyenne, minimum, maximum, somme ou dernière valeur ; intervalle en minutes. Aucun état manquant n’est inventé.

Pas d’import automatique de projets ioBroker : entités HA, Recorder et pages Studio remplacent objets, adaptateurs d’historique et vues VIS. Les graphiques SVG sont indépendants ; aucune identité universelle au pixel près n’est garantie.

## Vérifications et publication

Les tests navigateur couvrent les 49 entrées en DE/EN/FR, Classique/Material 3 et Clair/Sombre ainsi que les interactions. La mise à jour avec les vrais paquets conserve les projets à l’identique, octet par octet. Vérifier aussi les appareils dans sa propre installation HA.

[Projet de comparaison](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/materialdesign-widgetvergleich.json) · [Audit initial](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/AUDIT-2026-10-12.md)

Enregistrer **1.1.0**, Studio minimal **0.1.292**, ID <code>ugso.materialdesign</code> et MIT dans le [catalogue](https://visualstudio.ugso-software.de/?lang=fr). Publier sur GitHub n’approuve pas automatiquement le paquet. Empreinte : <code>dist/SHA256SUMS</code>.
