---
title: Widgets Basic
---

# Widgets Basic

**Studio 0.1.293** complète les 48 entrées Basic après la comparaison avec VIS-2. Ce sont des réalisations HA indépendantes. Les anciens projets conservent identifiants, clés des groupes, valeurs, CSS et modes précédents. Les nouvelles apparences changent les anciens widgets uniquement après sélection explicite.

**Langue Basic** suit Studio ou choisit DE/EN/FR séparément pour réglages, conseils et nouveaux messages Basic. Textes utilisateur et valeurs d’entité restent inchangés. L’interface générale Studio reste DE/EN.

## Valeurs et actions

Number propose séparateur de milliers, décimales automatiques, entité de qualité et classes CSS. Le mode de référence active explicitement le parsing du préfixe numérique et le singulier après formatage ; le mode précédent reste. Bool HTML/control ajoutent sentinelles marche/arrêt, préfixe/suffixe HTML et cibles HA supplémentaires. Le serveur vérifie entités prises en charge, disponibilité et limites. Actions principale et supplémentaire ne sont pas atomiques ; un échec de l’écriture supplémentaire empêche l’action URL suivante.

AckFlag HTML utilise une entité ou un attribut de confirmation explicitement choisi. HA n’a pas d’indicateur ACK ioBroker. Les anciens projets conservent leur source d’état ; une confirmation manquante n’est jamais affichée comme confirmée.

Les liens choisissent leur fenêtre cible. Les notes peuvent afficher du HTML nettoyé ; le dialogue écrit seulement du texte dans un input_text disponible sans attribut. Les nouveaux widgets utilisent un formatage inerte ; le balisage et les anciens modes restent sans réécriture des données. Utilisez iFrame pour les pages complexes. Les liaisons ioBroker exécutables ne sont pas importées.

## Apparence et navigation

La commande supplémentaire propose cible principale plus action supplémentaire ou cible séparée uniquement. Le second mode écrit exclusivement dans la cible séparée ; une direction non configurée reste désactivée sans revenir à la cible principale.

Checkbox, Select et Bar proposent apparence précédente/native/moderne. Les tableaux ajoutent classes tclass et mode moderne avec en-tête fixe tout en conservant JSON, événements, sélection, confirmation, détails et colonnes. Le CSS VIS personnalisé peut nécessiter une adaptation ; le balisage n’est pas identique au pixel.

Les nouveaux widgets plein écran utilisent des icônes suivant l’état du navigateur, détectent Échap et sont désactivés dans l’éditeur ; les anciens boutons texte restent. HTML navigation peut remplacer la page d’une sous-vue View-in-widget sans quitter la page principale. Screen Resolution peut afficher les détails du projet et de la page. Le groupement utilise le modèle Studio existant.

Le temps localisé propose auto, éléments date/heure, noms de mois/jours, horloge 12 heures, millisecondes et `[littéraux]`. Choisissez explicitement secondes ou millisecondes pour les horodatages numériques ; auto utilise une heuristique de taille. Le temps relatif s’actualise chaque seconde. TimesValue et Timestamp Value restent volontairement deux entrées avec la même source.

## Voix, sortie et groupes

Speech to Text démarre uniquement au clic et propose une fois/démarrer-arrêter/continu, langues DE/EN/FR, mots-clés, cinq icônes d’état et couleurs. La sortie reste locale ou va dans input_text disponible. Navigateur compatible, autorisation du microphone et généralement HTTPS sont nécessaires ; la reconnaissance peut nécessiter internet.

HTML logout quitte l’exécution vers une URL de retour ou tente de fermer une fenêtre ouverte par script. **Il ne déconnecte pas le compte HA.**

La visibilité par groupe accepte les IDs HA comme `system-admin` et `system-users`, séparés par points-virgules. Seuls les utilisateurs actifs confirmés par le proxy Ingress reçoivent des groupes ; les utilisateurs inconnus/locaux n’en ont aucun. Masquer/désactiver s’applique si groupe ou condition d’état échoue. Il s’agit d’affichage, pas d’autorisation API.

[Guide détaillé DE/EN/FR](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/basic-widgets-0.1.293.md) · [Audit VIS-2 de l’état précédent](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/vis2-basic-audit-2026-10-12.md) · [Deutsch](/projects/grafik-visual-studio/basic) · [English](/en/projects/grafik-visual-studio/basic).
