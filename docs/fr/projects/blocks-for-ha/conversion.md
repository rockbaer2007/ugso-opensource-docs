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

:::: details Référence détaillée issue de la documentation allemande

## Conversion {#konvertierung}

Depuis la version **0.1.12**, cette catégorie propose neuf nouveaux blocs. [Voir tous les blocs de conversion en images](/fr/projects/blocks-for-ha/blocks#konvertierung-seit-0-1-12). Leur fonctionnement est basé sur celui des [blocs de conversion ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_convert.ts). Ces blocs utilisent la bibliothèque Blockly originale, avec une traduction spécifique UGSo vers le langage Jinja de Home Assistant. La conversion effective a lieu uniquement lors de l'exécution dans Home Assistant.

### Blocs ioBroker / UGSo pour HA {#iobroker-ugso-blocks-fur-ha}

| ioBroker | Notre bloc | Comportement / Différence |
| --- | --- | --- |
| en nombre | **En nombre** | HA `float` : convertit une valeur numérique complète. `21.5` fonctionne ; `21W` et la virgule décimale ne fonctionnent pas. Contrairement à `parseFloat`, aucun préfixe numérique n'est extrait. |
| en valeur logique | **En valeur logique** | HA `bool` : booléen ou valeurs reconnues telles que true/false, on/off, yes/no et 1/0. Les textes inconnus ne sont pas considérés automatiquement comme une valeur « vrai ». |
| en chaîne de caractères | **En chaîne de caractères** | Représentation textuelle Jinja. Un booléen donne par exemple `True`/`False` ; la représentation JSON des objets n'est pas garantie. |
| type de | **Type de** | HA `typeof`, à partir de HA 2023.4. Renvoie les noms de types Python (str, int, float, bool, dict, list, NoneType) au lieu des noms de types JavaScript. |
| en date/heure | **En date/heure** | Texte au format ISO ou secondes/millisecondes Unix spécifiées → valeur de date selon l'heure locale de HA. Utiliser le format ISO avec « Z » ou un décalage (offset). |
| date/heure en… | **Date/heure en…** | Valeur de date, format ISO/heure/date, nombre Unix, année/mois/jour/heure/minute/seconde/milliseconde, jour de la semaine, numéro de semaine ou temps écoulé depuis minuit. L'option « format personnalisé » fait apparaître un champ de texte supplémentaire. |
| formater la différence de temps | **Formater la différence de temps** | Durée numérique exprimée en millisecondes (par défaut) ou en secondes. Formats hh:mm:ss, hh:mm, mm:ss. Les durées négatives conservent leur signe ; les valeurs d'heures ou de minutes élevées ne subissent pas de conversion modulo 24 ou 60. |
| JSON vers objet | **JSON vers valeur** | `from_json`, prend également en charge les listes et les valeurs isolées. Un JSON invalide génère une erreur de modèle ; aucun objet de remplacement vide n'est créé silencieusement. |
| Objet vers JSON, avec formatage | **Valeur vers JSON, avec formatage** | `to_json`, avec une case à cocher pour l'indentation. Seules les valeurs sérialisables en JSON sont acceptées ; les dates doivent être converties au préalable au format ISO ou en nombre Unix. |
| Appliquer une expression JSONata à | **En attente** | Aucun adaptateur d'exécution JSONata n'est disponible dans l'éditeur. Les modèles HA personnalisés peuvent déjà utiliser Jinja pour accéder aux valeurs d'objets ou de listes. Une véritable intégration de JSONata doit également être fonctionnelle lors de l'exécution ultérieure dans HA. |

Références pour les règles HA : [float](https://www.home-assistant.io/template-functions/float/), [bool](https://www.home-assistant.io/template-functions/bool/), [typeof](https://www.home-assistant.io/template-functions/typeof/), [from_json](https://www.home-assistant.io/template-functions/from_json/), [to_json](https://www.home-assistant.io/template-functions/to_json/).

### Connexions et champs de formatage {#anschlusse-und-formatfelder}

Les valeurs booléennes sont compatibles avec les conditions et la logique. Les nombres convertis sont des **nombres dynamiques (valeurs d'exécution)** : ils peuvent être utilisés dans des comparaisons de valeurs, des variables, le formatage de durées, ainsi que pour définir des montants ou des décalages dans les blocs temporels. En revanche, les seuils fixes (`numeric-state`), les temps d'attente et les incréments nécessitent toujours des blocs de type « nombre » (constantes). Il est donc impossible d'y connecter par erreur des nombres dynamiques. La configuration dynamique de la haute disponibilité (HA) pour ces champs n'est pas encore implémentée.

Les valeurs de date utilisent le connecteur « Time ». Dans le bloc **Date/Heure vers…**, la sélection détermine la sortie : valeur de date, nombre (durée) ou texte. Le format personnalisé utilise Python `strftime` avec `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`. Les codes de formatage ioBroker, tels que `YYYY`, ne sont pas interchangeables. Les noms des mois et des jours de la semaine (dépendants de la langue), les autres formats de durée ainsi qu'un masque de durée personnalisé ne sont pas encore implémentés. Pour les jours de la semaine, le comptage va de lundi=1 à dimanche=7 ; le numéro de semaine suit la norme ISO. Les fractions de seconde dans une durée sont tronquées, et non arrondies.

### Exemples {#beispiele}

Convertir le texte d'un capteur en nombre et le comparer à 20 : Valeur de modèle (template) avec état du capteur → Vers nombre → Comparaison. La sortie HA contient :

```jinja
{{ (float((states('sensor.temperatur'))) > 20) }}
```

Texte JSON → JSON vers valeur → Valeur vers JSON (formatage) :

```jinja
{{ (('{"wert":21.5}' | from_json) | to_json(pretty_print=true)) }}
```

Une différence temporelle de `3661000` millisecondes devient `01:01:01` ; `-3661000` devient `-01:01:01`. Il convient de bien distinguer les millisecondes des secondes. Le bloc formate une durée déjà existante ; il ne calcule pas automatiquement la différence entre deux valeurs de date.

### Erreurs, enregistrement et développements futurs {#fehler-speichern-und-offene-erweiterung}

Les blocs n'attribuent pas de valeurs par défaut implicites en cas de nombre, de booléen ou de JSON invalide. Si une valeur de remplacement est nécessaire, elle peut être définie explicitement dans le modèle (template) HA général. Les variables HA peuvent interpréter les résultats des modèles comme des valeurs natives ; la spécification d'un type « chaîne de caractères » (string) constitue une information destinée à l'éditeur, mais ne garantit pas que HA n'appliquera pas sa propre interprétation de type lors de l'enregistrement d'un résultat.

Les projets JSON conservent leurs formes de blocs, leurs cases à cocher et leur format spécifique. Lors de l'ouverture au format YAML, ces expressions sont préservées sous forme de blocs de modèle (template) génériques. Les conversions effectuées au sein d'une action sur une variable peuvent générer des objets ou des listes lors de l'exécution ; en revanche, les variables de type objet ou liste enregistrées directement en YAML ne sont toujours pas importables. L'action HA générique attend actuellement des données d'action JSON statiques ; il n'est pas encore possible d'y intégrer directement des blocs de conversion.

**En attente :** Extension de la gestion des accès aux objets/listes, suivie de l'examen d'un adaptateur d'exécution JSONata optionnel. Une évaluation effectuée uniquement dans le navigateur ne refléterait pas le comportement d'une automatisation exécutée ultérieurement au sein de HA.

Les cycles de conversion entre Blockly et YAML, les vérifications de connexions et l'évaluation Jinja (utilisant des fonctions d'assistance HA simulées) ont été testés. L'exécution sur un véritable système HA n'a pas encore été vérifiée.

::::
