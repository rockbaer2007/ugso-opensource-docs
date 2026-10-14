---
title: ATLAS et Home Assistant
description: Connexion Home Assistant, éditeur Expert, ressources HACS, import, export et gestion des identifiants dans ATLAS.
---

# ATLAS et Home Assistant

Le package `@atlas/homeassistant` fournit les contrats et workflows pour
l’éditeur de cartes, les entités en direct et les exports destinés à HACS.
Le Home Assistant Card Editor est le plugin de référence intégré à ATLAS.
Voir aussi son [guide utilisateur](/fr/projects/atlas/card-editor) et sa
[documentation de plugin](/fr/projects/atlas-plugins/homeassistant-card-editor).

## Connexion depuis une tablette ou un téléphone

Utilisez une adresse Home Assistant accessible depuis l’appareil. Si
`homeassistant.local` ne fonctionne pas sur le réseau mobile, essayez
l’adresse IP locale. Une URL `http://homeassistant.local:80` ou
`http://<IP>:80` est acceptée ; le port 80 n’est pas exclu.

Le jeton enregistré appartient à l’Administration. Dans l’application HA,
vérifiez l’URL dans la configuration de l’application, enregistrez puis
redémarrez ATLAS ; en installation autonome, enregistrez la connexion dans
l’Administration. Gardez le jeton existant tant qu’il reste valide.
`WebSocket closed with code 1006` peut indiquer un problème d’adresse,
de résolution de nom, de réseau ou de transport ; il ne prouve pas à lui
seul que le jeton est invalide. Une page HTTPS ne doit pas tenter un
WebSocket non sécurisé bloqué par le navigateur.

## Liens des plugins dans la barre latérale de Home Assistant

Depuis l’application HA **0.1.236**, les plugins externes utilisent une URL
de lancement stable, par exemple :

```text
http://<HOTE_ATLAS>:4176/launch/atlas.plugin.file-studio
```

Dans `panel_iframe`, modifiez uniquement l’URL si nécessaire, sans changer
les chemins ou projets existants. Redémarrez Home Assistant après modification
de sa configuration YAML. Le port 4176 doit être accessible depuis le navigateur.

## Périmètre actuel

- Aperçu de statut et intégration du moteur de rendu et des thèmes.
- Catalogue d’entités local ou en direct, filtrage et recherche.
- API WebSocket Home Assistant, `get_states` et ressources Lovelace.
- Connexion et connexion automatique gérées par l’Administration.
- Cartes Core, Mushroom et Bubble, ainsi que Tabbed Card V2.
- Éditeur Expert sur grille de 12 colonnes, déplacement et redimensionnement.
- Conteneurs `vertical-stack`, `horizontal-stack` et onglets imbriqués.
- Import JSON/YAML depuis fichier ou presse-papiers et packages ATLAS/HACS.
- Styles `card_mod` et `uix`, exports JSON/YAML et réimport de packages.
- Résumé de l’import et vérification des ressources nécessaires.

Les vérifications natives A5 incluent des cartes Core, Bubble et Mushroom sur
Pi 5 ARM64 et sur une VM Proxmox AMD64. Leur périmètre reste limité :
elles ne garantissent ni toutes les cartes tierces ni une API de production stable.
Voir l’[état du développement](/fr/projects/atlas/development-status).

## Raccourcis de travail

Ces commandes concernent le travail avec Codex dans le dépôt ATLAS :

| Commande | Action |
| --- | --- |
| `??` | Répondre sans modifier les fichiers. |
| `>>` | Mettre en œuvre la dernière demande. |
| `>>!` | Mettre en œuvre et fournir un résumé. |
| `<<` | Annuler la dernière modification demandée. |
| `!!B`, `!!b` | Créer une sauvegarde. |
| `!!D`, `!!d` | Mettre à jour la documentation Open Source. |

Les commandes peuvent se combiner, par exemple `!!D !!B` : sauvegarder
le contenu actuel avant de mettre à jour la documentation.

## Types de cartes pris en charge

| Famille | Type Lovelace | Dépendance |
| --- | --- | --- |
| Entities | `entities` | Carte native Home Assistant. |
| Mushroom Template | `custom:mushroom-template-card` | Mushroom. |
| Bubble Button | `custom:bubble-card` | Bubble Card. |
| Tabbed Card V2 | `custom:tabbed-card-v2` | ATLAS Tabbed Card V2. |

La palette comprend aussi Entity, Glance, Button, Grid, Sensor, Thermostat,
Link, Webpage et les piles verticales et horizontales. Cette liste ne signifie
pas que toute carte personnalisée ou toute option tierce est automatiquement
prise en charge.

## Sélecteur d’entités et recherche

Le catalogue peut provenir de données de démonstration, du cache local ou
de Home Assistant. Les identifiants sont uniques et triés ; les préfixes
de domaine facilitent le filtrage. La recherche accepte le nom lisible,
l’identifiant et des fragments de texte.

Le dernier catalogue connu est disponible dès l’ouverture. Après connexion,
ATLAS synchronise les entités et indique si le catalogue est en cache, en
cours de synchronisation, à jour ou en erreur, ainsi que les ajouts et retraits.
Choisir une entité l’applique au champ Expert sélectionné et propose son nom
comme titre. Les instantanés et événements sont traités dans leur ordre
d’arrivée ; les messages d’une connexion fermée sont ignorés.

## HACS et ressources

Les chemins respectent la casse Linux :

```text
/hacsfiles/Bubble-Card/bubble-card.js
/hacsfiles/lovelace-mushroom/mushroom.js
/hacsfiles/tabbed-card-v2/tabbed-card-v2.js
```

Exemple de déclaration des ressources :

```yaml
resources:
  - url: /local/atlas/atlas-homeassistant-panel.js
    type: module
  - url: /hacsfiles/Bubble-Card/bubble-card.js
    type: module
  - url: /hacsfiles/lovelace-mushroom/mushroom.js
    type: module
```

La ressource de panneau ATLAS est une cible d’intégration préparée ;
ce chemin ne prouve pas qu’un panneau natif a été installé. Les cartes Core
ne nécessitent pas Mushroom ou Bubble. Les cartes personnalisées doivent
avoir leur propre ressource installée et enregistrée.

## Modèle d’export

Un export comprend la configuration de carte, un manifeste indiquant le nom
du fichier, le format, le type MIME, la cible, la disposition et les dépendances,
puis le contenu sérialisé utilisé pour copier ou télécharger.

Le nom de la carte Expert et le nom du script sont distincts. Les noms de
scripts sont normalisés, par exemple `energy-kitchen.js`. Remplacez les
entités de démonstration par des entités réelles avant utilisation.

## Packages de cartes ATLAS

Les packages JSON conservent la configuration et le plan Expert afin de
retrouver les champs et leurs positions au réimport. Les projets anciens
pris en charge sont importés dans l’éditeur Expert ; aucun autre mode n’est proposé.

Le script exporté fournit le type de carte personnalisé, les informations
de ressource et une configuration de démonstration sûre via
`getStubConfig`. Les exemples peuvent utiliser
`binary_sensor.atlas_status` et `sensor.atlas_temperature` ; ils doivent
être remplacés dans Home Assistant.

Un bundle `.hacs.zip` contient :

- `hacs.json`
- le script JavaScript généré
- `README.md`
- un exemple de carte Lovelace
- le package intégré `atlas/*.atlas-card.json`
- les langues sélectionnées dans `locales/*.json`

L’import inspecte le ZIP et lit les packages intégrés pris en charge.
Il distingue les packages ATLAS, les cartes HA brutes, les artefacts de
constructeurs externes et les formats inconnus ; il peut importer, demander
une vérification ou rejeter le contenu. Un artefact externe n’est pas
silencieusement converti en projet complet. La prévisualisation des correspondances
peut proposer des champs avec entités vides à vérifier.

Exemple de package :

```json
{
  "version": 1,
  "kind": "atlas.homeassistant.card",
  "manifest": {
    "name": "Office Light",
    "filename": "office-light-bubble-single.yaml",
    "format": "yaml",
    "mimeType": "text/yaml",
    "target": "bubble",
    "layout": "single"
  },
  "content": "type: \"custom:bubble-card\"\ncard_type: button\nbutton_type: state\nentity: light.office\n"
}
```

## Éditeur de disposition des cartes

L’éditeur ouvre uniquement le workflow Expert. Les anciens contrôles de groupe,
de cible globale et le sélecteur Simple/Expert ne sont plus affichés.
Les outils d’import, de ressources et d’entités restent disponibles.

Ajoutez les cartes depuis la palette gauche par clic ou glisser-déposer.
Les champs se déplacent dans les limites de la grille ; la position du point
saisi est conservée. Les flèches déplacent le champ focalisé d’une cellule ;
en mode édition, Maj + flèche le redimensionne. La poignée inférieure droite
apparaît pour le champ sélectionné en édition.

Chaque modèle propose de 1 à 12 colonnes ou `full`, et des lignes `auto`
ou de 1 à 8. Les tailles des modèles sont enregistrées localement et peuvent
être réinitialisées. Les champs disposent de contrôles Largeur/Hauteur et
d’une extension limitée par rapport au modèle. La surface possède également
une poignée et une remise à zéro ; champs, sélection et taille de surface
sont restaurés après rechargement.

Les titres sont numérotés par type. Vous pouvez appliquer un titre saisi
ou utiliser le nom de l’entité sélectionnée. Bubble propose
`state`, `switch`, `slider` et `name`, exportés dans `button_type`.
Les conteneurs démarrent sans carte ni entité imposée. Les piles et les
onglets acceptent des cartes imbriquées ; les champs sont exportés selon
leur structure et leur ordre dans la grille.

La palette sépare Core et Community. Les favoris enregistrés masquent les
autres entrées ; afficher toutes les cartes ne les supprime pas. Une carte
favorite ne peut pas être masquée. Les entrées masquées restent accessibles
dans la liste complète. Vous pouvez réinitialiser les tailles ou les favoris.

Le scan charge les ressources Lovelace enregistrées, pas une liste exhaustive
des options de chaque carte. Les familles connues deviennent des modèles ;
les ressources inconnues restent informatives jusqu’à une correspondance locale
avec un type `custom:*`. Une correspondance conserve son chemin de ressource,
devient déplaçable et est dédupliquée. Les ressources auxiliaires connues,
par exemple outils ou jeux d’icônes, sont écartées du scan de cartes.
La déduction automatique du type depuis un nom de fichier est facultative
et accompagnée d’un avertissement rouge.

Le panneau de diagnostic facultatif permet d’examiner la requête WebSocket
du navigateur, le proxy WebSocket de l’Administration et les solutions de repli.
Le résumé Expert signale champs remplis ou vides, lignes occupées,
dimensions, types et chevauchements. La disposition automatique cherche des
emplacements libres sans modifier le contenu. Les déplacements et dépôts
recherchent également une position libre si la cible est occupée.
La liste des entités sélectionnées est repliée par défaut.

L’interface de l’éditeur est disponible en DE/EN/FR ; la langue est mémorisée.
Les libellés, indications d’entités, résumés, dépendances et messages utilisent
le même catalogue de traductions. Sur tablette, les cartes de la palette se
présentent deux par deux ; les commandes de grille et zoom sont repliées par
défaut sur téléphone et tablette. Voir les
[détails des commandes mobiles](/fr/projects/atlas-plugins/homeassistant-card-editor).

## Import YAML et styles

L’import accepte YAML/JSON, fichiers `.yaml`, `.yml` et `.txt`,
texte collé et presse-papiers. Les structures imbriquées
`vertical-stack`, `horizontal-stack`, `grid`, `conditional` et
les onglets pris en charge deviennent une structure Expert.
Les en-têtes et séparateurs Bubble sans entité ainsi que les colonnes vides
prises en charge ne nécessitent pas une entité fictive.

ATLAS détecte `card_mod` et `uix`. Les styles d’entité restent associés
à leur entité ; les styles globaux restent visibles séparément. L’éditeur
Glance expose les styles détectés sous l’entité correspondante.
L’export HA permet de choisir `card_mod` ou `uix`.
Le YAML d’origine est conservé autant que possible jusqu’à une modification
dans l’éditeur. Cette prise en charge ne garantit pas la conservation de
toute option avancée de toute carte tierce.

## Référence externe : Home Assistant Card Builder

Le projet
[studiobts/home-assistant-card-builder](https://github.com/studiobts/home-assistant-card-builder)
est une référence pour l’évaluation de l’interopérabilité. ATLAS développe
ses propres contrats et modèles sans copier aveuglément le code externe.

Trois chemins restent distincts : inspiration par les idées publiques,
correspondances explicites pour importer/exporter des artefacts documentés,
et éventuel fork ou dérivé après une décision et une revue de licence
AGPL-3.0 avec attribution.

## Résumé d’import

Le package `@atlas/homeassistant` normalise le titre, les entités,
le format, la cible, la disposition, la dépendance et l’origine éventuelle
d’un package ATLAS. Cette logique reste dans le package plutôt que dispersée
dans l’interface.

## Vérification des ressources Lovelace

À la connexion, ATLAS demande les ressources et vérifie les dépendances
des cartes. Les états sont :

| État | Signification |
| --- | --- |
| `not-required` | La carte native ne nécessite pas de ressource personnalisée. |
| `unchecked` | Vérification non effectuée. |
| `installed` | Ressource attendue trouvée. |
| `missing` | Ressource attendue absente. |

## ATLAS comme interface Home Assistant

Les cibles préparées pour le panneau ATLAS sont distinctes des dépendances
Mushroom ou Bubble :

| Usage | Chemin prévu |
| --- | --- |
| Serveur ATLAS | `/local/atlas/atlas-homeassistant-panel.js` |
| Intégration HACS ATLAS prévue | `/hacsfiles/atlas/atlas-homeassistant-panel.js` |

Le modèle peut vérifier la ressource ATLAS, les dépendances des cartes et
les déclarations JSON/YAML nécessaires. L’hébergement ATLAS autonome Docker
et l’application HA existent ; l’intégration frontend native ATLAS/HACS
et l’installateur Linux/systemd restent la priorité A7.
Exporter une carte HACS ne signifie pas installer ATLAS lui-même via HACS.

## Démonstration actuelle

Après compilation dans le dépôt ATLAS :

```sh
pnpm build
node examples/status-demo/server.mjs
```

Adresse de l’éditeur :

```text
http://127.0.0.1:4174/
```

L’Administration utilise le port 4175. `pnpm start:app` démarre l’application
combinée sur le port 4176 avec `/health`.
Sur écran large, les contrôles sont organisés en colonnes compactes.

## Feuille de route et langues exportées

La langue de la carte exportée est indépendante de celle de l’interface ATLAS.
Les packages et bundles incluent toujours `en` comme repli obligatoire ;
d’autres langues européennes et `ru` peuvent être sélectionnées.
Les fichiers supplémentaires non traduits contiennent un repli anglais et
sont marqués comme nécessitant traduction et vérification avant publication.

L’Administration possède le choix du fournisseur :
`none`, `chatgpt`, `gemini`, `deepl-free`, `deepl-pro` et
`custom-ai`. Le choix ne signifie pas que chaque adaptateur est implémenté.
Le chemin ChatGPT/OpenAI est connecté : l’éditeur appelle
`/api/card-translation` et le serveur Admin utilise sa clé pour l’API
OpenAI Responses. Les fichiers effectivement générés sont marqués
`machine` et nécessitent toujours une revue. Le modèle peut être défini
par `ATLAS_OPENAI_TRANSLATION_MODEL`. La traduction automatique nécessite
une connexion Internet et affiche sa progression ; un repli n’est jamais
présenté comme une traduction automatique achevée.

Références conservées pour les autres adaptateurs :
`https://www.deepl.com/de/pro#api`,
`https://developers.deepl.com/api-reference/translate/request-translation`
et `https://ai.google.dev/gemini-api/docs/api-key`.
L’URL interne DeepL `https://api.deepl.com/v2/translate` n’est pas un champ
ordinaire à saisir dans l’Administration.

Les clés des fournisseurs appartiennent à l’Administration ; l’éditeur reçoit
uniquement fournisseur, endpoint et indicateur de clé configurée.
Le jeton HA n’est transmis qu’en session au plugin de référence ; les autres
plugins reçoivent des URL, chemins et capacités approuvés, sans jeton brut.

L’Administration peut restaurer ses secrets après rechargement depuis un
cookie Admin chiffré de longue durée. La clé de déchiffrement du navigateur
reste dans le stockage local Admin ; les cookies partagés et les données
de transmission à l’éditeur ne contiennent pas de secrets bruts.
L’Admin peut aussi restaurer la connexion depuis son serveur local via
`GET /api/admin-connection?includeSecrets=1`.

L’export `atlas-admin-settings.json` contient les paramètres lisibles
et un bloc `encryptedSecrets` chiffré AES-GCM. Les secrets sont liés
à l’identité de l’installation, créée dans les données utilisateur hors dépôt
ou fixée par `ATLAS_INSTANCE_ID`. Copier un dossier serveur ou un export
sur une autre installation ne rend pas ces secrets utilisables ; un transfert
explicite ou une procédure par phrase secrète reste nécessaire.

Le plugin de référence se crée avec
`createHomeAssistantCardEditorPlugin()` et son package avec
`createHomeAssistantCardEditorPluginInstallPackage()`. Le catalogue,
le cycle de vie Runtime, l’Administration et le Hub le rendent découvrable.
L’Administration exporte son package `.atlas-plugin.json`.

La carte Lovelace UV reste un projet séparé ultérieur. La référence
`filipnet/haos-uv-index` sert d’inspiration pour les capteurs UV, les
couleurs de risque, les conseils de protection, la présentation compatible
Mushroom et les notifications facultatives ; elle ne constitue pas un plan
de copie de code.
