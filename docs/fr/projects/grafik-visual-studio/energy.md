---
title: Widgets Énergie
description: 'Flux d''énergie, consommation, stockage sur batterie et tarifs : un ensemble de widgets externe pour Home Assistant.'
---

# Widgets Énergie {#energy-–-widgets}

**Energy 0.1.0** est un ensemble externe dédié, conçu pour **Grafik Visual Studio 0.1.255 ou une version ultérieure**. Il ne fait pas partie du pack « Industrial ». La sélection des entités et les valeurs en temps réel fonctionnent aussi bien dans l'éditeur qu'en mode exécution (runtime) ; la sélection de la période temporelle est gérée localement lors de l'exécution, sans écrire d'états dans Home Assistant.

## Projet original et origine {#originalprojekt-und-herkunft}

Ce projet s'inspire de [ioBroker.vis-2-widgets-energy](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy), créé par **bluefox / GermanBluefox et ses contributeurs**, et publié sous **licence MIT**. La [documentation originale](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy/tree/main/docs/de) décrit la version pour ioBroker. Version du code source vérifiée : [d0a53871](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy/commit/d0a53871ea7e57c5100de2a1f2ef7b2ee82059c7), 7 octobre 2026.

« Energy » est une **adaptation autonome pour Home Assistant, réalisée par rockbaer2007** ; il ne s'agit ni d'un portage à l'identique, ni d'une publication officielle issue d'ioBroker. Le moteur de rendu, les icônes et l'intégration avec Home Assistant ont été entièrement redéveloppés ; le code source React/vis-2 ainsi que les images originales ne sont pas inclus. Les informations concernant la source et la licence figurent également dans la documentation du paquet.

## Images {#bilder}

Les images illustrent le mode exécution (runtime) avec des **données de test** ; il ne s'agit pas de mesures en temps réel.

![Flux d'énergie entre le réseau, la maison, le système photovoltaïque, la batterie de stockage et la borne de recharge](/images/grafik-visual-studio/energy-distribution.png)

| Batterie de stockage | Prix dynamique de l'électricité |
| --- | --- |
| ![Batterie avec état de charge, puissance et temps restant](/images/grafik-visual-studio/energy-battery.png) | ![Prix de l'électricité heure par heure, avec indication des heures les moins chères et les plus chères](/images/grafik-visual-studio/energy-price.png) |

## Installation {#installation}

1. Mettez à jour Studio vers la version **0.1.255 ou ultérieure** et rechargez la page avec **Ctrl+F5**.
2. Téléchargez [ugso.energy.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/energy/ugso.energy.wg).
3. Installez-le via **Paramètres → Packs de widgets → Local**. L'ensemble apparaîtra sous le nom **Energy** dans la palette de widgets.
4. Insérez le widget et sélectionnez les sources de mesure via **…** en utilisant le sélecteur d'entités de Home Assistant.

Le fichier contient huit widgets déclaratifs, des icônes SVG personnalisées pour la palette, ainsi qu'une licence et des instructions. Il ne contient aucun code exécutable. [Code source et instructions du pack](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/energy).

## Les huit widgets {#die-acht-widgets}

| Widget | Fonction et sources de mesure |
| --- | --- |
| Flux d'énergie | Maison et réseau, plus **1 à 10 nœuds supplémentaires**. Pour chaque nœud : nom, couleur, entité de puissance, multiplicateur, inversion du sens du flux et, en option, une seconde valeur avec unité. Animation des flux désactivable. |
| Consommation d'énergie | Jusqu'à **six séries de données (enregistreurs)**, affichées sous forme de barres ou de lignes ; différences de compteurs ou somme de consommations individuelles ; par heure/jour/mois selon la période choisie. |
| Comparaison de consommation | Valeurs actuelles pour un maximum de **six appareils** ; affichage en barres, lignes ou graphiques circulaires ; paramètres personnalisables (tri, couleur, unité) pour chaque série. Les unités différentes ne sont pas combinées sur un même axe. |
| Sélection temporelle | Jour, semaine, mois ou année ; choix de la date ; navigation (précédent/aujourd'hui/suivant). Un sélecteur peut piloter plusieurs widgets d'historique sur une même page. |
| Autarcie et autoconsommation | Deux anneaux représentant la production, les échanges avec le réseau (import/export) et, en option, la consommation domestique. Si la source « maison » n'est pas définie, le bilan est calculé automatiquement. |
| Stockage sur batterie | État de charge, puissance, capacité, énergie stockée et estimation du temps restant avant charge complète ou décharge totale. Signe configurable pour la charge ; puissance exprimée en W ou kW. |
| Coûts de l'énergie | Consommation × prix d'achat + abonnement (par jour calendaire) − revenus de l'injection ; basé sur les compteurs actuels ou sur une période d'enregistrement. Devise paramétrable. |
| Prix dynamique de l'électricité | Données JSON issues d'un état ou d'un attribut ; affichage par barres horaires ; identification des heures actuelles, les moins chères et les plus chères, ainsi que la moyenne. Les prix négatifs sont pris en compte. |

## Unités et valeurs inconnues {#einheiten-und-unbekannte-werte}

**Les multiplicateurs doivent être configurés explicitement** : p. ex. B. `0.001` pour Wh → kWh ou W → kW. Un capteur de puissance (W) ne se transforme pas automatiquement en compteur d'énergie (Wh). L'autarcie nécessite des données de même nature et exprimées dans la même unité : soit des puissances, soit des énergies se rapportant à la même période.

Réseau : valeur positive = prélèvement (achat), valeur négative = injection (vente). Si une source d'injection distincte est configurée, elle remplace la composante négative du réseau. Flux d'énergie : par défaut, les valeurs positives au niveau des nœuds correspondent à un flux vers la maison, et les valeurs négatives à un flux sortant ; pour les consommateurs ou les batteries dont le comptage est inversé, activez l'option **Inverser le sens du flux**.

En l'absence de source configurée ou valide, le symbole **—** s'affiche. Les valeurs inconnues ne sont pas remplacées par des estimations fictives. Si le dénominateur est égal à 0, les taux restent inconnus. La durée restante est une estimation basée sur la puissance actuelle et la capacité ; il ne s'agit pas d'une prévision générée par l'installation elle-même.

## Enregistreur (Recorder) et sélecteur de période {#recorder-und-zeitauswahl}

Pour afficher l'historique et les coûts passés, Home Assistant doit enregistrer les entités numériques via le composant **Recorder**. Dans le champ **ID du sélecteur de période**, saisissez l'identifiant (ID) du widget de sélection présent sur la même page (par ex. `widget-3`). Sans cette liaison, la période et la date propres au widget sont utilisées. Si le champ est laissé vide, la date actuelle est prise en compte.

**counter** calcule les différences entre les relevés de compteurs en se basant sur les états conservés par le « recorder ». Les états inconnus ou une réinitialisation du compteur créent une lacune ; les réinitialisations ne sont pas comptabilisées comme de la consommation. **sum** additionne les quantités consommées individuellement et ne convient pas aux compteurs cumulatifs. Les périodes en cours ne contiennent que les données déjà enregistrées ; les segments futurs restent inconnus. Un coût total ne s'affiche que si les données sont complètes et valides pour la partie déjà enregistrée.

Limites : **366 jours**, **six entités**, **20.000 états par ligne**. Si la réponse est trop volumineuse, elle est interrompue et un message d'avertissement est affiché. Les limites temporelles suivent le fuseau horaire local du navigateur. Certaines périodes anciennes peuvent être absentes en raison de la politique de conservation des données du « recorder ». Cette version n'utilise **pas les statistiques à long terme de HA** (Home Assistant), ni l'historique ioBroker, et ne propose pas d'intégration automatique de la puissance. Les frais fixes s'appliquent à la période calendaire sélectionnée ; en mode « coûts en temps réel », les valeurs des compteurs doivent correspondre à cette période.

## Données tarifaires {#preisdaten}

Les tableaux (arrays) contenus dans un état ou dans un attribut sélectionné sont pris en charge, y compris lorsqu'ils sont imbriqués dans `prices`, `today`, `data`, `values` ou `result`. Les champs temporels sont détectés à partir de `startsAt`, `start_timestamp`, `start`, `date` et `x` ; les champs tarifaires, à partir de `total`, `marketprice`, `price`, `value` et `y`. Il est possible de saisir d'autres noms. Les horodatages peuvent être au format ISO, en secondes ou en millisecondes. Un tableau de nombres correspond aux heures de la journée locale en cours.

Définir le facteur de prix par rapport à la source : **100** pour EUR/kWh → ct/kWh, **0.1** pour EUR/MWh → ct/kWh. À partir de maintenant, il est possible de configurer le nombre d'heures, ainsi que les heures « avantageuses » ou « coûteuses » et leurs couleurs respectives.

## Différences par rapport à l'original {#unterschiede-zum-original}

Les huit types de widgets s'inspirent de l'original ; les paramètres et la connectivité ont été adaptés pour Studio et Home Assistant. Cette première version propose une sélection locale de la période temporelle et utilise les états du « Recorder » (historique HA) ; elle ne prend pas en charge les OID ioBroker ni les instances d'historique, n'intègre pas l'ensemble des options de mise en page ou de graphique de vis-2, et ne permet pas l'écriture directe vers les appareils.
