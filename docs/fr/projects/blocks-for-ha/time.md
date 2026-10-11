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
