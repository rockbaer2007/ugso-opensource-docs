---
title: Date et heure
---

# Date et heure

Les blocs utilisent l’heure locale et le fuseau de **Home Assistant**, pas l’horloge du navigateur. Une date calculée reste un objet date Jinja ; convertir explicitement avant de l’afficher ou de la sérialiser en JSON. [Images et fonctions](./blocks).

| Fonction | Comportement |
| --- | --- |
| Comparaison de l’heure actuelle | Avant, avant ou égal, après, après ou égal, égal, entre ou hors de. Format `HH:mm` ou `HH:mm:ss`. |
| Comparaison avec entrée | Heure sous forme de texte raccordé. Décocher l’heure actuelle fait apparaître une entrée de date à comparer. |
| Entre deux heures | Début inclus, fin exclue, y compris à travers minuit. Bornes égales : plage vide. |
| Date actuelle | `now()` de HA, avec fuseau, pour calculer ou formater. |
| Date calculée | Début du jour, du jour suivant, de la semaine (lundi), du mois ou de l’année. |
| Événement solaire | Prochain lever, coucher, aube, crépuscule, midi ou minuit solaire dans `sun.sun`. Décalage en minutes ; événement éventuellement demain. |
| Décaler une date | Ajouter/soustraire millisecondes, secondes, minutes, heures ou jours. Nombre fini requis. |
| Formater | Texte d’heure/date, ISO avec fuseau ou secondes Unix. |
| Date du jour | Comparer une date de calendrier complète, année incluse, avec le calendrier de HA. |

Une comparaison est une **condition**, pas un déclencheur périodique. Pour démarrer à une heure ou un événement solaire, utiliser les déclencheurs correspondants. Une valeur solaire absente provoque une erreur de modèle ; elle n’est pas remplacée silencieusement.

Les frontières de calendrier et changements d’heure suivent les calculs de HA. Pour un intervalle de durée fixe, distinguer durée écoulée et changement de jour du calendrier. Les tests vérifient notamment les plages passant par minuit et les frontières de fuseau.

Les variantes ioBroker ont servi de référence fonctionnelle ; les expressions sont une implémentation UGSo pour HA/Jinja. Voir [source ioBroker](https://github.com/ioBroker/ioBroker.javascript) et [modèles HA](https://www.home-assistant.io/docs/configuration/templating/).
