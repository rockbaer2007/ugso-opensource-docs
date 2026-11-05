---
title: Couleurs du menu latéral
description: Couleurs et opacité par entrée du menu HA, directement dans l’éditeur natif. HACS et Marketplace, DE/EN/FR.
---
# Couleurs du menu latéral / Sidebar Colors

::: info HA 2026.11 : sélecteur corrigé
La version **0.1.1** prend en charge `ha-md-list-item` et `ha-list-item-button` dans le dialogue natif. Les 27 tests locaux réussissent : régressions DOM des deux types de lignes HA, opacité, annulation, enregistrement, réouverture et réinitialisation au thème. Le correctif correspondant du Manager a été testé sur .177 ; Sidebar Colors n’a pas été installé en parallèle. Couleurs et clés de stockage existantes conservées.
:::

[Périmètre, résultats et problèmes ouverts](/fr/collection/ha-2026-11-compatibility).

<img src="/images/packages/projects-sidebar-colors.svg" width="80" height="80" alt="Sidebar Colors" />

**0.1.1 · Extension frontend · DE / EN / FR · MIT**

Attribuer une couleur propre à l’icône et au libellé de chaque entrée Home Assistant. Le nouveau carré de couleur se trouve directement dans **Modifier la barre latérale**, entre le nom et l’œil. La visibilité et l’ordre restent réglables avec les commandes natives habituelles.

[GitHub](https://github.com/rockbaer2007/ha-sidebar-colors) · [Téléchargement / Versions](https://github.com/rockbaer2007/ha-sidebar-colors/releases/latest) · [Ouvrir dans HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=ha-sidebar-colors&category=plugin)

## Sélecteur de couleur

Zone de saturation/luminosité, curseur de teinte, saisie HEX et opacité avec aperçu immédiat. Le damier représente la transparence. **Appliquer** ferme le sélecteur ; seul **Enregistrer** dans la fenêtre HA sauvegarde durablement. **Annuler** abandonne le brouillon correspondant. **Couleur du thème** supprime la couleur personnalisée de l’entrée.

![Sélecteur ATLAS avec une opacité de 70 pour cent](/images/sidebar-colors/farbwaehler.png)

## Exemples de l’utilisateur

Les images montrent des couleurs choisies individuellement pour les icônes et les textes. Des noms identiques restent distincts grâce aux chemins des panneaux. Aucune palette n’est imposée.

<div class="sidebar-color-examples">
<figure><a href="/images/sidebar-colors/beispiel.png" target="_blank" rel="noopener noreferrer"><img src="/images/sidebar-colors/beispiel.png" alt="Menu coloré avec Vue d’ensemble, ATLAS et HACS" /></a><figcaption>Premier résultat avec des couleurs personnalisées.</figcaption></figure>
<figure><a href="/images/sidebar-colors/weiteres-beispiel.png" target="_blank" rel="noopener noreferrer"><img src="/images/sidebar-colors/weiteres-beispiel.png" alt="Autre exemple avec les outils ATLAS et Zigbee2MQTT" /></a><figcaption>Autre configuration avec les outils ATLAS.</figcaption></figure>
</div>

## Prérequis et vérifications

Version minimale prévue : **Home Assistant Core 2026.10.3**. Tests réels sous **2026.10.4** : choix des couleurs, opacité de 70 % et de 0 %, aperçu, enregistrement/annulation, rechargement, retour au thème, synchronisation entre deux onglets et commandes natives de visibilité/tri. L’utilisateur confirme le résultat. La couleur temporaire du test a été supprimée ; ses couleurs personnelles ont été conservées.

La version minimale repose sur les interfaces disponibles, sans test réel distinct sous 2026.10.3. Marketplace à partir de **2026.11** utilise le même format compatible HACS ; aucun test d’exécution séparé n’y est revendiqué. [Description officielle de Marketplace](https://contributors.home-assistant.io/marketplace/how-it-works/)

## Installation HACS / Marketplace

Créer d’abord une sauvegarde complète de HA. C’est un **plugin frontend**, pas une application Supervisor ni une carte à insérer. Il est d’abord disponible comme dépôt personnalisé ; sa publication ne l’ajoute pas automatiquement au catalogue par défaut.

1. Dans HACS, ajouter `https://github.com/rockbaer2007/ha-sidebar-colors` via **Dépôts personnalisés**, catégorie **Tableau de bord** (`plugin`), puis télécharger **Sidebar Colors**.
2. À partir de 2026.11, utiliser la procédure correspondante sous **Paramètres → Marketplace**. Marketplace reprend les réglages HACS ; aucun format de migration séparé n’est requis.
3. Compléter la section `frontend:` existante. Garder les thèmes et modules présents ; ne pas créer une section en double :

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/ha-sidebar-colors/ha-sidebar-colors.js
```

4. Vérifier la configuration, redémarrer HA puis recharger le navigateur. Une ressource de tableau de bord seule ne suffit pas si une autre page HA est ouverte d’abord. L’entrée de module charge aussi l’extension sur ces pages.
5. Maintenir l’en-tête **Home Assistant** du menu latéral puis cliquer sur un carré de couleur.

## Installation manuelle ou migration

Copier le fichier unique `ha-sidebar-colors.js` de la version publiée dans `/config/www/ha-sidebar-colors.js` et utiliser `/local/ha-sidebar-colors.js` comme module. Le ZIP contient le même fichier, la licence et la documentation. Ne pas charger les deux méthodes simultanément.

Pour l’ancien prototype à trois fichiers, remplacer `/local/ugso-sidebar-colors/0.1.0/sidebar-colors.js` par le nouveau chemin, redémarrer HA puis recharger le navigateur. Le stockage des couleurs reste identique ; les anciens fichiers peuvent rester comme sauvegarde.

## Conserver les réglages et mettre à jour

Les couleurs sont enregistrées par utilisateur HA sous la clé séparée `ugso_sidebar_colors_v1` et synchronisées sur les appareils où l’extension est chargée. Les chemins des panneaux évitent les confusions de noms. Un enregistrement de couleurs seul ne réécrit ni l’ordre natif, ni les éléments masqués, ni le thème. Configurations des tableaux de bord et autorisations restent inchangées.

Avant l’enregistrement, l’ancien état des couleurs et des préférences est conservé localement dans `ugso-sidebar-colors-backup:<user-id>`. Cela ne remplace pas une sauvegarde HA complète. Un stockage navigateur plein ou bloqué empêche l’enregistrement. Aucun nouvel identifiant, script externe ou service de traduction cloud n’est nécessaire.

Mettre à jour via le même dépôt HACS/Marketplace, garder le chemin du module puis recharger le navigateur. Pour désinstaller, retirer uniquement l’entrée du module, redémarrer HA et recharger. Les couleurs du thème reviennent et les réglages natifs sont conservés.

## Limites

L’extension utilise des méthodes internes des fenêtres HA ; la revérifier après les mises à jour du frontend. Les conflits et confirmations incertaines gardent le brouillon ouvert ; aucune répétition aveugle. Cette API n’offre pas de comparaison/enregistrement atomique. Couleurs et ordre natif sont deux opérations distinctes, avec compensation contrôlée au mieux en cas d’échec.

À 0 % d’opacité, icône et texte peuvent être invisibles, mais le carré reste accessible. Fond de sélection, titres et droits restent inchangés. Les pannes et conflits ont été simulés localement ; aucun test réel sur téléphone/tablette ni coupure réseau provoquée sous Marketplace n’est revendiqué. [Détails des tests et code source](https://github.com/rockbaer2007/ha-sidebar-colors/blob/main/docs/TESTING.md).

<style>
.sidebar-color-examples{display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start}.sidebar-color-examples figure{margin:0;max-width:100%}.sidebar-color-examples img{max-height:720px;width:auto;max-width:100%;display:block;border-radius:8px}.sidebar-color-examples figcaption{font-size:.85em;max-width:300px;margin-top:8px}
</style>
