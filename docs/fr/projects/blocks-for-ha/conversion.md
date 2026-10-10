---
title: Conversion
---

# Conversion

Les conversions sont évaluées dans **HA/Jinja**. Elles ne reposent pas sur les coercitions de JavaScript. [Catalogue illustré](./blocks).

| Bloc | Résultat et limites |
| --- | --- |
| Convertir en nombre | `float()` HA exige une valeur numérique complète. Pas de préfixe `parseFloat` ni de valeur de secours implicite. |
| Convertir en booléen | `bool()` HA reconnaît true/false, on/off, yes/no, 1/0. Valeur non reconnue : erreur. |
| Convertir en texte | Représentation Jinja ; booléens True/False. Ce n’est pas une sérialisation JSON. |
| Type de | `typeof()` HA retourne les types Python : str, int, float, bool, dict, list, NoneType. HA ≥ 2023.4. |
| Convertir en date/heure | Texte ISO, secondes Unix ou millisecondes Unix. Préférer un fuseau explicite ; résultat en heure locale HA. |
| Formater date/heure | Objet date, texte ISO, formats d’heure/date, unités Unix, composantes de calendrier ou format personnalisé. Le raccord change selon le résultat. |
| Durée | Millisecondes ou secondes vers hh:mm:ss, hh:mm ou mm:ss. Fractions tronquées ; heures/minutes peuvent dépasser 24/60, signe conservé. |
| JSON vers valeur | Objet, liste ou valeur JSON simple. JSON invalide : erreur. |
| Valeur vers JSON | Sérialisation HA avec indentation facultative. Convertir les dates auparavant. |

Les formats personnalisés utilisent **Python strftime** : `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`. Les formats de date ioBroker ne sont pas directement interchangeables.

Une conversion numérique produit un nombre à l’exécution. Elle peut alimenter calculs, variables et conditions de modèle, mais pas les seuils fixes des déclencheurs numériques. Les comparaisons de capteurs doivent convertir leurs états textuels explicitement.

Les allers-retours de projet/YAML conservent les formats pris en charge. JSONata n’est pas proposé sans moteur réellement disponible à l’exécution dans HA. [Documentation des modèles HA](https://www.home-assistant.io/docs/configuration/templating/) · [Référence ioBroker](https://github.com/ioBroker/ioBroker.javascript).
