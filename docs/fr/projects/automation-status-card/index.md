---
title: Automation Status Card
description: Liste automatique, sélection par cases, exécutions et diagnostic des traces. Version 0.1.3, DE/EN/FR.
---
# Automation Status Card

**HA 2026.11.0, 05/11/2026, .177 :** la version 0.1.3 passe l’affichage, l’activation/désactivation confirmée par HA, l’exécution en cours, la lecture des traces, la fin normale, les cases à cocher, tout sélectionner/désélectionner et le rechargement. Les exemples individuels Bubble/Mushroom s’affichent. Objets de test supprimés. Les erreurs et alertes de durée n’ont pas été provoquées à nouveau sous cette version de HA ; les résultats antérieurs restent distincts.

[Périmètre, résultats et problèmes ouverts](/fr/collection/ha-2026-11-compatibility).

<img src="/images/automation-status-card/icon.svg" width="80" height="80" alt="Automation Status Card" />

**0.1.3 · DE / EN / FR · MIT**

[GitHub](https://github.com/rockbaer2007/automation-status-card) · [Télécharger 0.1.3](https://github.com/rockbaer2007/automation-status-card/releases/tag/v0.1.3) · [Documentation](https://opensource.ugso-software.de/fr/projects/automation-status-card/)

Vérifié sur .177 avec HA 2026.10.4 : carte de base 0.1.0 et sélection/diagnostics dans la version corrigée 0.1.3. Traces HA réelles, erreur, fin normale, alerte de durée, alerte désactivée, cases à cocher et sélection enregistrée vérifiées. [Rapport et captures](https://github.com/rockbaer2007/automation-status-card/blob/main/docs/TESTING.md).

Liste automatiquement toutes les entités `automation.*` disponibles pour l’utilisateur HA connecté, par ordre alphabétique. Huit lignes sont visibles par défaut ; les autres sont accessibles par défilement vertical. Les nouvelles automatisations et suppressions sont prises en compte automatiquement. Aucune bibliothèque de cartes supplémentaire n’est requise.

## Installation et réglages

### HACS / Marketplace

HACS / Marketplace : ajouter `https://github.com/rockbaer2007/automation-status-card` comme dépôt personnalisé **Dashboard** (`plugin`). Ressource : `/hacsfiles/automation-status-card/automation-status-card.js`. La compatibilité HACS ne signifie pas une inclusion au catalogue par défaut ; aucune installation Marketplace séparée n’a été testée. Ce n’est pas une application Supervisor. Ne pas charger simultanément les copies HACS et manuelle.

### Installation manuelle

Sauvegardez HA. Copiez le fichier `automation-status-card.js` du paquet vers `/config/www/automation-status-card/automation-status-card.js`. Ajoutez `/local/automation-status-card/automation-status-card.js` dans **Paramètres → Tableaux de bord → Ressources**, type **Module JavaScript**, sans retirer les ressources existantes. Rechargez le tableau de bord et choisissez **Automation Status Card**.

```yaml
type: custom:automation-status-card
title: Automatisations
visible_rows: 8
allow_toggle: false
language: auto
```

L’éditeur visuel permet de modifier le titre, les lignes visibles (entier 1–50), **Autoriser la commutation** et la langue (`auto`, `de`, `en`, `fr`). Un titre vide masque l’en-tête. La langue automatique suit HA, avec l’anglais comme repli.

Dans **Afficher les automatisations**, toutes les entrées sont initialement cochées : **cochée = affichée**, décochée = masquée uniquement dans cette carte. **Tout sélectionner** affiche toutes les entrées ; **Tout désélectionner** masque toutes les entrées actuellement répertoriées. Les nouvelles automatisations sont sélectionnées par défaut. La sélection est enregistrée par carte sans modifier les automatisations ni les autres cartes. Les entités décochées temporairement indisponibles restent répertoriées pour pouvoir être sélectionnées à nouveau. En YAML : `hidden_entities: [automation.mon_automatisation]` contient les identifiants décochés. Sans ce paramètre, le comportement précédent reste inchangé.

Le statut indique **activée/désactivée**, pas une exécution en cours. Le nom ouvre les détails HA. Lorsque la commutation est autorisée, chaque interrupteur active/désactive cette seule automatisation ; la carte ne déclenche pas ses actions. La désactivation utilise `stop_actions: false` pour ne pas arrêter explicitement une exécution existante. Les autorisations HA restent applicables ; l’affichage seul n’est pas une restriction d’accès.

Les états indisponibles/inconnus et une connexion interrompue interdisent la commutation. L’interrupteur est bloqué jusqu’à confirmation de l’état. Une erreur ou confirmation manquante est signalée, sans nouvelle tentative automatique ni succès supposé.

## Exécutions et diagnostics

HA ne signale certaines interruptions que par `aborted`, notamment une condition fausse ou un arrêt explicite en erreur. Elles sont indiquées de façon neutre : **Dernière exécution interrompue – vérifier la raison dans les traces HA**, sans affirmer un succès ni un échec. Les durées issues des traces sont toujours plafonnées au temps observé par cette carte, afin qu’une différence d’horloge entre HA et le navigateur ne déclenche pas d’alerte prématurée.

`show_health: true` (par défaut) ajoute le nombre d’exécutions et leur durée à partir de l’attribut HA `current`, indépendamment de l’activation. `runtime_warning_seconds: 300` avertit après cinq minutes ; `0` désactive l’alerte, maximum 604800 secondes (7 jours). Tous ces réglages figurent dans l’éditeur visuel. Une longue durée ne prouve pas un blocage : les délais et attentes peuvent être volontaires. Rien n’est arrêté ou redémarré automatiquement.

Avec une liste complète de traces correspondantes, la durée commence au début de la plus ancienne exécution active. Sinon, elle commence prudemment à l’observation par cette carte, avec une mention explicite. `last_triggered` seul ne sert pas de durée ; un déclenchement plus récent que la dernière demande de traces impose également cette estimation. Navigation, rechargement et déconnexion réinitialisent l’observation locale. Ce n’est pas une surveillance en arrière-plan.

`check_traces: true` (par défaut) lit uniquement les résumés `trace/list` des automatisations, au maximum toutes les 30 secondes pour les administrateurs, avec un bouton d’actualisation manuelle. Aucune trace complète, variable ni configuration n’est demandée. La dernière exécution terminée est signalée en erreur uniquement si HA rapporte une erreur. Un arrêt normal ou une condition fausse n’est pas automatiquement une erreur. Une exécution terminée plus récente sans erreur signalée remplace l’ancienne indication d’erreur. L’horodatage figure dans l’infobulle ; le nom ouvre toujours les détails HA.

L’absence de droits administrateur, d’identifiant d’automatisation ou de traces, une API non compatible et les erreurs de connexion indiquent des diagnostics indisponibles, pas une erreur d’automatisation. La déconnexion masque les états d’exécution périmés. Aucun droit supplémentaire n’est accordé. Une erreur ignorée par `continue_on_error` peut manquer dans le résumé. L’API HA peut évoluer. Sources : [attributs](https://www.home-assistant.io/docs/automation/basics/), [API des traces](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/trace/websocket_api.py), [schéma des résumés](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/trace/models.py).

## Bubble Card et Mushroom : une seule automatisation

Les fichiers `examples/bubble-single-readonly.yaml`, `bubble-single-control.yaml`, `mushroom-single-readonly.yaml` et `mushroom-single-control.yaml` visent chacun **une automatisation**. Remplacez `automation.replace_me` par son identifiant. Les exemples d’affichage désactivent les actions ; les exemples de commande utilisent l’action toggle habituelle de l’extension et son comportement standard. Ce sont des modèles YAML indépendants, pas une liste automatique ni du code d’extension supplémentaire. Le réglage `allow_toggle` de la carte principale n’agit pas sur ces cartes séparées.

Installez l’extension concernée séparément. Chemins sensibles à la casse :

- Bubble Card : `/hacsfiles/Bubble-Card/bubble-card.js`
- Mushroom : `/hacsfiles/lovelace-mushroom/mushroom.js`

Aucune carte existante n’est modifiée et aucun code tiers n’est inclus. [Bubble Card](https://github.com/Clooos/Bubble-Card) · [Mushroom](https://github.com/piitaya/lovelace-mushroom).

## Portée

La version publiée comprend le fichier JS compilé et un ZIP complet avec les instructions et exemples. Pour une mise à jour manuelle, conserver le chemin existant, actualiser `?v=0.1.3` et recharger complètement le navigateur. Node 22+ : `npm ci`, `npm run check`, `npm run build`, `npm test`. [Vérifications](https://github.com/rockbaer2007/automation-status-card/blob/main/docs/TESTING.md).

Licence MIT. Aucun service externe, identifiant d’accès ni télémétrie. HA enregistre la configuration du tableau de bord ; la carte ne modifie pas les définitions d’automatisations.


![HA test: run warning and failure](/images/automation-status-card/health-177-013.png)

![HA editor: selection](/images/automation-status-card/selection-177-013.png)

![Single-automation examples, initial-version test](/images/automation-status-card/cards-177.png)
