---
title: Date et heure
---

# Date et heure

## Horaires et déclencheurs depuis 0.1.60

Cliquer sur le champ CRON dans **Déclencheurs → Horaire**. Le dialogue propose **Assistant / Simple / CRON**, suivant les fenêtres ioBroker. Simple définit des intervalles ; Assistant propose aussi une heure précise avec des jours numériques. CRON dispose d’onglets par champ et de secondes facultatives. **OK** applique une règle valide ; **Annuler** et Échap conservent la valeur précédente. Thèmes clair/sombre et textes DE/EN/FR disponibles.

![Horaire](/assets/blocks-for-ha/blocks/fr/ugso_schedule_trigger.png)

![Dialogue CRON](/assets/blocks-for-ha/schedule-fr.png)

![Dialogue CRON sombre](/assets/blocks-for-ha/schedule-dark-fr.png)

Cinq champs : minute, heure, jour du mois, mois, jour de semaine. Six champs commencent par les secondes. Nombres, listes, plages et pas sont acceptés. Exemples : `*/5 * * * *` toutes les cinq minutes ; `*/30 * * * * *` toutes les 30 secondes ; `30 7 * * 1-5` du lundi au vendredi à 07:30. Dimanche : 0 ou 7. Home Assistant exécute dans son heure locale, sans minuterie du navigateur. Les pas suivent les champs de l’horloge : `*/7` minutes recommence à la minute 0 de chaque heure.

La sortie utilise `time_pattern` ou `time` avec `weekday`. Mois et jour du mois doivent être `*`. Dates, périodes de validité, exécution unique et plages astronomiques jour/nuit ne sont pas encore implémentés dans ce dialogue. Les règles non prises en charge sont explicitement refusées. Les règles par jours sont limitées à 2000 heures individuelles ; au-delà, elles sont refusées. Déclencheurs calendrier et conditions HA restent disponibles séparément. Le JSON du projet conserve la règle CRON ; le YAML conserve la structure HA native équivalente.

| Déclencheur ioBroker | Blocks for HA / équivalent HA |
| --- | --- |
| Si objet / Si objets | Déclencheur d’état avec une ou plusieurs entités ; état précédent/suivant, attribut et durée. Pas d’identifiants d’objets ioBroker. |
| Déclenché par / confirmer la valeur | Pas d’équivalent ioBroker `ack` ici dans HA. Aucun bloc artificiel de confirmation. |
| ↪ Valeur / Message | Nouveau bloc de données : état actuel/précédent, ID d’entité, ID/type du déclencheur, message MQTT/JSON et données d’événement. Donnée absente : `none` ; convertir les nombres si nécessaire. |
| Astro avec décalage | Lever/coucher du soleil avec décalage facultatif en minutes. Autres conditions solaires via les blocs HA natifs. |
| Horaire / CRON | Dialogue ci-dessus, exécution HA native. Pas d’enregistrement dynamique d’horaires ioBroker nommés. |
| Message reçu | Déclencheur MQTT ou événement HA avec filtre ; pas de réception directe de messages entre scripts ioBroker. |
| Message de journal | Événement HA `system_log_event`, si HA est configuré pour fournir ces événements. Aucun écouteur ioBroker dédié. |
| Événements de fichiers/enums | Pas d’équivalent direct. Utiliser une intégration HA disponible et ses événements/entités. |
| Autres déclencheurs HA natifs | MQTT, modèle, webhook, appareil, tag, conversation, zone et géolocalisation figurent directement dans **Déclencheurs**, sans doublons dans HA avancé. |

![Données du déclencheur](/assets/blocks-for-ha/blocks/fr/ugso_trigger_value.png)

Références : [blocs ioBroker originaux](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_trigger.ts), [déclencheurs HA natifs](https://www.home-assistant.io/docs/automation/trigger/). L’apparence suit l’original ; exécution et données restent propres à HA.

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

:::: details Référence détaillée issue de la documentation allemande

## Date et heure {#datum-und-zeit}

### Planification et déclencheurs (depuis 0.1.60) {#zeitplan-und-ausloser-seit-0-1-60}

Dans la section **Déclencheurs → Planification**, cliquez sur la règle CRON. La boîte de dialogue propose les modes **Assistant / Simple / CRON**, calqués sur les fenêtres contextuelles d'ioBroker. Le mode « Simple » permet de créer des intervalles ; le mode « Assistant » ajoute la possibilité de définir une heure fixe ainsi que des jours de la semaine (sous forme numérique). Le mode « CRON » dispose d'onglets pour chaque champ et inclut, en option, la gestion des secondes. Le bouton **OK** valide la règle saisie, tandis que **Annuler** (ou la touche Échap) conserve la valeur précédente. L'affichage s'adapte au mode clair ou sombre. Tous les textes des boîtes de dialogue sont disponibles en allemand, anglais et français.

![Calendrier](/assets/blocks-for-ha/blocks/de/ugso_schedule_trigger.png)

![Dialogue CRON](/assets/blocks-for-ha/schedule-de.png)

![Dialogue CRON (thème sombre)](/assets/blocks-for-ha/schedule-dark-de.png)

Cinq champs : minute, heure, jour du mois, mois, jour de la semaine. Les formats à six champs commencent par les secondes. Il est possible d'utiliser des nombres, des listes, des plages et des pas (incréments). Exemples : `*/5 * * * *` toutes les cinq minutes ; `*/30 * * * * *` toutes les 30 secondes ; `30 7 * * 1-5` les jours ouvrables à 07h30. Le dimanche correspond à 0 ou 7. Home Assistant exécute l'automatisation selon son heure locale ; il ne s'agit pas d'un minuteur basé sur le navigateur. `/Schritte` se rapporte au champ temporel concerné : `*/7` pour les minutes, le décompte repart à 0 à chaque nouvelle heure.

La sortie utilise des déclencheurs natifs `time_pattern` ou `time` avec `weekday`. Le mois et le jour du mois doivent être `*`. Les dates, les plages de validité, les événements ponctuels et les fenêtres astronomiques (jour/nuit) ne sont pas encore implémentés dans la boîte de dialogue. Ces règles ne sont pas ignorées silencieusement. Les règles basées sur les jours de la semaine sont résolues en un maximum de 2000 horaires individuels ; les règles générant une fréquence supérieure sont explicitement rejetées. Les déclencheurs basés sur le calendrier et les conditions Home Assistant restent disponibles séparément. Le fichier JSON du projet intègre la règle CRON, tandis que le fichier YAML contient la structure native équivalente de Home Assistant.

| Déclencheur ioBroker | Blocks for HA / Adaptation pour HA |
| --- | --- |
| Si objet / Si objets | Déclencheur d'état basé sur une ou plusieurs entités ; paramètres : de/vers, attribut et durée de maintien. Pas d'identifiants d'objets ioBroker. |
| Déclenché par / Confirmation (ack) | HA ne dispose pas de l'équivalent du `ack` d'ioBroker. Pas de bloc de confirmation artificiel. |
| ↪ Valeur / Message | Nouveau bloc de données de déclenchement : valeur, ancienne valeur, ID d'entité, ID/type de déclencheur, message MQTT/JSON et données d'événement. Les données manquantes renvoient `none` ; conversion des nombres si nécessaire. |
| Astro avec décalage | Lever/coucher du soleil avec décalage optionnel en minutes. Autres conditions solaires gérées via les blocs natifs de HA. |
| Planification / CRON | Interface identique à celle décrite ci-dessus, exécution native dans HA. Pas d'enregistrement dynamique de planifications nommées issues d'ioBroker. |
| Réception de message | Déclencheur basé sur un événement MQTT ou HA avec filtre ; pas de réception directe de messages de scripts ioBroker. |
| Message de journal (Log) | Déclencheur d'événement HA utilisant `system_log_event`, sous réserve que HA fournisse ces événements. Pas d'écouteur de logs ioBroker dédié. |
| Événements de fichiers / Énumérations | Pas de transposition directe. Utiliser les intégrations HA existantes ou leurs événements/entités correspondants. |
| Autres déclencheurs natifs HA | Les déclencheurs MQTT, Template, Webhook, Appareil (Device), Tag, Conversation, Zone et Géolocalisation sont désormais disponibles directement sous **Déclencheurs**, sans doublon dans la section étendue HA. |

![Données de déclenchement](/assets/blocks-for-ha/blocks/de/ugso_trigger_value.png)

Références : [Blocs déclencheurs originaux d'ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_trigger.ts), [déclencheurs natifs de HA](https://www.home-assistant.io/docs/automation/trigger/). L'interface s'inspire de l'original ; l'exécution et les données restent spécifiques à HA.

Depuis **0.1.11**, la catégorie contient sept blocs supplémentaires. [Tous les blocs avec illustrations](/fr/projects/blocks-for-ha/blocks#datum-und-zeit-seit-0-1-11). L'interface utilise la bibliothèque Blockly originale ; la traduction vers Jinja (pour HA) est une implémentation propre à UGSo. Les références sont les [blocs temporels de l'adaptateur JavaScript d'ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_time.ts) ainsi que les [définitions des blocs Blockly](https://docs.blockly.com/guides/create-custom-blocks/define/block-definitions/).

### Blocs ioBroker / UGSo pour HA {#iobroker-ugso-blocks-fur-ha}

| ioBroker | Notre bloc / Implémentation |
| --- | --- |
| Heure actuelle, heure fixe | **Comparaison horaire** : inférieur à, inférieur ou égal à, supérieur à, supérieur ou égal à, égal à, compris entre et non compris entre. Le champ de fin apparaît lorsqu'il s'agit d'une plage temporelle. |
| Heure actuelle avec case à cocher et entrée connectable | **Comparaison horaire avec entrées** : blocs texte pour le début et la fin. Si la case est décochée, une entrée supplémentaire pour une valeur de date/heure à comparer devient disponible. |
| Heure actuelle sous forme d'objet date ou de valeur formatée | **Heure actuelle en tant que valeur de date** et **bloc de formatage** séparé. Cette distinction évite que des textes formatés ne soient interprétés par erreur comme des valeurs de date. |
| Temps calculé | **Début de période calendaire** : jour, jour suivant, semaine (lundi), mois et année. D'autres limites calendaires ioBroker ne sont pas encore disponibles. |
| Heure actuelle basée sur un événement astronomique avec décalage (offset) | **Événement solaire** : lever, coucher, aube/crépuscule, zénith et minuit solaire, avec un décalage en minutes (positif ou négatif). |
| Calcul temporel : base ± nombre, unité | **Calcul temporel** : valeur de date ± nombre ; en millisecondes, secondes, minutes, heures ou jours. |

### Connexions et utilisation {#anschlusse-und-bedienung}

Les comparaisons temporelles renvoient une valeur **booléenne** et s'intègrent dans des conditions (ET/OU/NON) ou des structures « si ». Les valeurs de date disposent d'un **connecteur temporel** : l'heure actuelle, le début de période calendaire, les événements solaires et les calculs temporels peuvent être imbriqués les uns dans les autres. Les nombres s'insèrent dans les champs de décalage (offset) ou de valeur ; les heures formatées (sous forme de texte) s'insèrent dans les limites de comparaison connectables. Le formatage propose : HH:mm, HH:mm:ss, date ISO, date au format allemand, date/heure, format ISO avec fuseau horaire et secondes Unix.

Exemple : **Heure actuelle → Calculer l'heure (+ 30 minutes) → Formater l'heure (HH:mm)**, puis définir le résultat en tant que variable. Le modèle (template) généré est le suivant :

```jinja
{{ (now() + timedelta(minutes=30)).strftime("%H:%M") }}
```

**Entre 22:00 et 06:00** : cette plage couvre la nuit et inclut le passage à minuit. L'heure de début est incluse, mais pas l'heure de fin. Si les bornes sont identiques, la période est considérée comme vide ; « pas entre » correspond à l'inverse. Les heures fixes doivent être au format HH:mm ou HH:mm:ss. Les bornes dynamiques doivent fournir le même format lors de l'exécution ; des valeurs non valides entraîneront une erreur dans le modèle HA (Home Assistant). La comparaison s'effectue à la seconde près ; ainsi, « égal à 12:00 » équivaut à 12:00:00 et ne constitue pas un déclencheur temporel fiable.

### Exécution et limites {#ausfuhrung-und-grenzen}

Les modèles (templates) générés sont évalués **dans Home Assistant**. Le navigateur construit le code YAML mais n'exécute pas de gestion temporelle propre. Les fonctions utilisent le fuseau horaire configuré dans HA : [Fonctions de date/heure HA](https://www.home-assistant.io/template-functions/#date-time). Le début d'une journée calendaire se base sur minuit heure locale ; les jours suivent le calendrier local, y compris lors des changements d'heure (passage à l'heure d'été/hiver). Un calcul de type « + 24 heures » ne garantit pas, lors d'un changement d'heure, l'écoulement de 24 heures réelles en temps universel (UTC).

Les données solaires proviennent des attributs de l'**intégration « Sun » (Soleil) de HA** ([HA-Sun-Integration](https://www.home-assistant.io/integrations/sun/#sensors)). Celles-ci fournissent l'**événement suivant**, et non systématiquement l'événement du jour en cours. La valeur en UTC est convertie en heure locale HA avant tout calcul ou formatage. L'absence de valeur — par exemple si l'intégration est indisponible ou si un événement ne peut être calculé — entraîne une erreur dans le modèle ; aucune heure de remplacement n'est générée automatiquement.

Une comparaison temporelle vérifie l'heure **au moment de l'évaluation de la condition**. Elle ne déclenche pas l'automatisation et n'attend pas que l'heure correspondante soit atteinte. Pour cela, il convient d'utiliser un déclencheur basé sur l'heure ou sur le soleil. Le nouveau bloc de données solaires ne remplace pas un déclencheur solaire.

Le projet « Blocks » (au format JSON) intègre des formulaires, des sélections et des entrées dynamiques. Lors de l'**ouverture en mode YAML**, le contenu de ces modèles temporels est préservé, mais ils apparaissent sous forme de blocs de modèles génériques. Une valeur de date préalablement stockée dans une variable HA peut être traitée comme du texte ; c'est pourquoi notre bloc de lecture de variables ne dispose pas de connecteur de type « heure » (Time). Imbriquez directement les valeurs de date ou, depuis la version **0.1.12**, convertissez le bloc de lecture de variables via l'option **Par date/heure**. [Conversion et unités](/fr/projects/blocks-for-ha/conversion). Les valeurs temporelles converties peuvent désormais être utilisées pour définir des montants ou des décalages par rapport au soleil (offset solaire).

Vérification : allers-retours Blockly/YAML, connexions typées, champs dynamiques ainsi que contrôles Jinja pour les limites nocturnes et l'heure d'été. L'exécution sur un système HA (Home Assistant) réel n'a pas encore été vérifiée.

::::
