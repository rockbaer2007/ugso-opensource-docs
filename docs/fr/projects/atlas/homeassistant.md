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

L’[intégration ATLAS Runtime](/fr/projects/atlas/frontend) installe un panneau
qui intègre le Runtime existant. Le type de dépôt HACS est **Integration** ;
le module utilise `/atlas_frontend/frontend/atlas-homeassistant-panel.js`.
Ne pas enregistrer ce module comme ressource Lovelace supplémentaire. Les cartes
exportées utilisent leur propre dépôt Dashboard et nom de script.

Les anciennes cibles de ressources de l’éditeur sont des métadonnées de
diagnostic ou de planification, distinctes des dépendances Mushroom ou Bubble :

| Usage | Chemin prévu |
| --- | --- |
| Serveur ATLAS | `/local/atlas/atlas-homeassistant-panel.js` |
| Ancienne cible HACS, pas le chemin d’installation de l’intégration | `/hacsfiles/atlas/atlas-homeassistant-panel.js` |

Le modèle peut vérifier la ressource ATLAS, les dépendances des cartes et
les déclarations JSON/YAML nécessaires. L’hébergement ATLAS autonome Docker
et l’application HA existent. L’[installateur Linux/systemd](/fr/projects/atlas/linux)
est implémenté et vérifié sous Debian 12 amd64 LXC et Raspberry Pi OS aarch64
sur Pi 4 ; l’intégration frontend
native ATLAS/HACS est disponible sous forme d’[intégration ATLAS Runtime](/fr/projects/atlas/frontend)
depuis 0.1.299. Son installation HACS native et les mises à jour vers 0.1.306,
avec redémarrage HA et conservation des données, sont vérifiées sur Pi 5 et Proxmox.
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

:::: details Référence détaillée issue de la documentation allemande

## ATLAS et Home Assistant {#atlas-und-home-assistant}

ATLAS 0.1.298 propose également un [installateur Linux/systemd](/fr/projects/atlas/linux) optionnel
pour une exécution autonome. Les procédures d'installation, de mise à jour, de sauvegarde et de restauration
ont été testées sur Debian 12 amd64 (LXC) et Raspberry Pi OS aarch64 (sur Raspberry Pi 4).
L'intégration native de l'interface ATLAS dans Home Assistant (via HACS)
est disponible sous forme d'une [intégration « ATLAS Runtime »](/fr/projects/atlas/frontend) optionnelle,
à partir de la version 0.1.299. L'installation via HACS, la mise à jour vers la version 0.1.306
et le redémarrage de Home Assistant ont été validés sur Raspberry Pi 5 et Proxmox, en garantissant la conservation des données.
Indépendamment de cela, l'application elle-même est en version 0.1.312.

Avec `@atlas/homeassistant`, ATLAS dispose de son propre paquet dédié à
l'intégration avec Home Assistant. L'accent est actuellement mis sur un flux de travail
permettant l'édition et l'exportation de cartes (cards) Home Assistant, d'entités en temps réel
et de paquets de cartes HACS.

La documentation détaillée concernant l'utilisation et les fonctionnalités de l'éditeur
est désormais disponible dans la section dédiée aux plugins : [Home Assistant Card Editor](/fr/projects/atlas-plugins/homeassistant-card-editor).

### Connexion depuis une tablette ou un smartphone {#verbindung-auf-tablet-und-smartphone}

L'URL de votre instance Home Assistant doit être accessible depuis le navigateur utilisé.
Si `homeassistant.local` fonctionne sur votre PC mais pas sur votre tablette,
il est possible que la résolution de noms locale fasse défaut. Sur l'appareil concerné,
commencez par vérifier si vous pouvez accéder à votre installation Home Assistant via son adresse IP
dans le navigateur, par exemple : `http://192.168.178.177:80`. Remplacez l'adresse IP exemple par votre propre adresse.

Si HA est accessible via cette adresse, saisissez-la dans la configuration de l'application ATLAS sous la référence `home_assistant_url`, enregistrez, puis redémarrez ATLAS. Laissez le jeton d'accès (Access Token) existant inchangé. Dans le cas d'une installation autonome d'ATLAS, modifiez plutôt l'URL dans la section « Administration » et enregistrez les paramètres.

**Le port 80 est autorisé.** `http://HOST:80` et `http://HOST` sont équivalents ; `ws://HOST/api/websocket` utilise également le port 80. ATLAS n'impose pas l'utilisation du port 8123. Utilisez le port réellement configuré et, dans le cas d'une connexion HTTPS, une adresse HTTPS appropriée. La seule apparition de `WebSocket closed with code 1006` ne signifie pas nécessairement que le jeton est invalide : vérifiez également l'accessibilité, la résolution de noms et, le cas échéant, la configuration du proxy. Lors d'un test sur une tablette Android, la connexion a été établie avec succès après le passage de `.local` à l'adresse IP accessible.

### Liens vers le plugin dans la barre latérale de Home Assistant {#plugin-links-in-der-home-assistant-seitenleiste}

À partir de la version `0.1.236` de l'application/du module complémentaire ATLAS, la boîte de dialogue de la barre latérale génère une URL de démarrage stable via le port `4176`, par exemple :

```text
http://<ATLAS_HOST>:4176/launch/atlas.plugin.file-studio
```

Si un plugin est déjà enregistré dans la barre latérale de Home Assistant,
ouvrez à nouveau la boîte de dialogue de la barre latérale dans ATLAS, copiez l'**URL**
qui y est indiquée et remplacez la valeur `url` actuelle par celle-ci
dans l'entrée `panel_iframe` correspondante. Vous pouvez également copier et
remplacer l'intégralité du bloc YAML. Redémarrez ensuite Home Assistant afin
que la configuration de la barre latérale soit rechargée. L'adresse de la page
Home Assistant, définie par `/atlas-studio/0`, reste inchangée ; seule la valeur
`url` du panneau intégré est modifiée. Le port `4176` doit être
accessible depuis le navigateur.

### Périmètre actuel {#aktueller-umfang}

- Aperçu de l'état dans ATLAS avec intégration des thèmes et du moteur de rendu
- Entités Home Assistant chargées localement ou en direct
- Connexion via le WebSocket de Home Assistant
- Gestion des jetons (tokens) dans l'administration Atlas, avec transmission et connexion automatique optionnelle à la session d'édition active
- Chargement des entités via `get_states`
- Chargement des ressources Lovelace via `lovelace/resources`
- Catalogue d'entités unifié pour le filtrage par type et la recherche
- Cibles de cartes pour les cartes natives de Home Assistant, Mushroom Template et Bubble Card
- Éditeur expert avec grille à 12 colonnes, glisser-déposer, redimensionnement et cartes conteneurs
- Cartes conteneurs pour `vertical-stack`, `horizontal-stack` et `custom:tabbed-card-v2`
- Importation de cartes via JSON/YAML, fichier, presse-papiers ou bundle HACS
- Détection des styles `card_mod` et `uix` lors de l'importation
- Dispositions (layouts) `single`, `horizontal-stack`, `vertical-stack`, `grid`, `conditional` et `tabbed-card-v2`
- Exportation au format JSON et YAML pour les cartes Home Assistant
- Packs de cartes Atlas et bundles compatibles HACS pour des allers-retours fluides dans l'éditeur
- Récapitulatif des cartes importées

### Raccourcis de travail {#arbeits-kurzbefehle}

Pour faciliter le travail dans l'éditeur ATLAS, des commandes courtes (type chat) peuvent être utilisées afin de déclencher rapidement des actions récurrentes :

| Code | Signification |
|---|---|
| `??` | répondre uniquement, sans rien appliquer |
| `>>` | appliquer intégralement l'étape décrite |
| `>>!` | exécuter et fournir un bref résumé |
| `<<` | annuler la dernière modification |
| `!!B` / `!!b` | créer une sauvegarde de l'état actuel |
| `!!D` / `!!d` | mettre à jour la documentation open source |

Les commandes abrégées peuvent être combinées. Par exemple, `!!D !!B` signifie
que l'état actuel est sauvegardé et que la documentation publique est mise à jour
en conséquence.

### Cibles de carte prises en charge {#unterstutzte-card-ziele}

| Sélection | Type Home Assistant | Dépendance |
|---|---|---|
| Entities | `entities` | inclus dans Home Assistant |
| Mushroom Template | `custom:mushroom-template-card` | Mushroom |
| Bubble Button | `custom:bubble-card` | Bubble Card |
| Tabbed Card V2 | `custom:tabbed-card-v2` | ATLAS Tabbed Card V2 |

### Sélecteur d'entités et recherche {#entity-picker-und-suche}

ATLAS intègre désormais un catalogue d'entités réutilisable, contenu dans le paquet
`@atlas/homeassistant`. Ce catalogue regroupe des entités locales d'exemple,
des groupes enregistrés et des entités chargées en temps réel depuis Home Assistant.

Le catalogue fournit :

- des identifiants d'entités (Entity IDs) uniques et triés
- une détection de domaines, tels que `sensor`, `binary_sensor`, `switch` ou `light`
- un ordre de raccourcis privilégié pour les domaines courants
- des libellés (labels) issus des entités actives, par exemple les noms conviviaux (*Friendly Names*)
- une fonction de recherche par identifiant d'entité ou par libellé, incluant la recherche par termes partiels comme `Hyper`

Ainsi, le sélecteur d'entités (*Entity Picker*) ne se limite plus à un simple code de démonstration ;
il devient une base commune destinée à une future intégration dans l'interface utilisateur (*frontend*) de Home Assistant.

### Indications relatives à HACS et aux ressources {#hacs-und-ressourcenhinweise}

ATLAS inscrit les chemins de ressources attendus directement dans les métadonnées d'exportation.
La démonstration peut donc indiquer si une carte personnalisée (*Custom Card*) est déjà
enregistrée dans Home Assistant, ou quel chemin de ressource est encore manquant.

| Cible (Carte) | Indication HACS | Chemin de ressource attendu |
|---|---|---|
| Entités | Non requis | Inclus dans Home Assistant |
| Mushroom Template | HACS > Frontend > Mushroom | `/hacsfiles/lovelace-mushroom/mushroom.js` |
| Bubble Button | HACS > Frontend > Bubble Card | `/hacsfiles/Bubble-Card/bubble-card.js` |

La vérification de tous les chemins de ressources Home Assistant et HACS attendus
tient strictement compte de la casse (majuscules et minuscules). Pour Bubble Card, par exemple, le chemin est défini
délibérément comme suit :

```text
/hacsfiles/Bubble-Card/bubble-card.js
```

Important : Home Assistant fonctionne généralement sous Linux. Dans ce système,
la casse (majuscules/minuscules) est prise en compte pour toutes les ressources.

Pour Mushroom et Bubble Card, ATLAS peut également générer un extrait (snippet) de ressource Lovelace prêt à être copié. Cet extrait combiné inclut la ressource frontend ATLAS ainsi que, si nécessaire, la dépendance requise par la carte choisie. Au format YAML, cela donne par exemple ceci pour ATLAS Server associé à Bubble Card :

```yaml
- url: "/local/atlas/atlas-homeassistant-panel.js"
  type: "module"
- url: "/hacsfiles/Bubble-Card/bubble-card.js"
  type: "module"
```

Cet extrait est destiné à l'enregistrement des ressources dans le tableau de bord Home Assistant. Dans le cas de la carte « Entities » (entités) native, seule la ressource frontend ATLAS est copiée.

### Modèle d'exportation {#export-modell}

ATLAS divise l'exportation des cartes Home Assistant en trois niveaux :

1. **Configuration de la carte** : l'objet « carte » Home Assistant proprement dit.
2. **Manifeste d'exportation** : nom de fichier, format, type MIME, destination, mise en page et
dépendance.
3. **Charge utile (payload) d'exportation** : le manifeste accompagné du contenu sérialisé au format JSON ou YAML.

Ainsi, les fonctions de copie et de téléchargement utilisent toutes deux le même contenu vérifié.

### Packs de cartes Atlas {#atlas-card-packages}

Outre l'exportation directe au format YAML/JSON, ATLAS permet de générer un paquet JSON portable. Ce paquet est conçu pour faciliter les flux de travail ultérieurs impliquant un éditeur ou l'intégration avec HACS.
Lorsqu'un paquet est exporté depuis le mode « Expert », il inclut également le plan de l'éditeur. Lors d'une importation ultérieure, ATLAS peut ainsi restaurer les champs placés et basculer automatiquement en mode « Expert ».
L'interface de démonstration propose, à cet effet, un champ dédié au nom du fichier de script HACS. Des noms tels que `Energy Kitchen` sont normalisés en `energy-kitchen.js`, enregistrés dans le plan de l'éditeur intégré, puis réintégrés dans le champ lors de la réimportation du paquet de carte Atlas.
Par ailleurs, le plan du paquet peut désormais générer une source JavaScript pour une carte personnalisée (*custom card*). Ce script contient le nom de fichier normalisé, le type de carte `custom:<name>` correspondant, le chemin de ressource `/hacsfiles/atlas/...`, une configuration par défaut `getStubConfig()` utilisant des entités de démonstration sûres, ainsi qu'une recommandation de remplacer ces entités par vos propres valeurs dans Home Assistant.
Dans la démonstration, cette source `.js` peut également être téléchargée directement via la fonction d'exportation de script de carte, permettant ainsi de vérifier cet élément indépendamment du paquet HACS complet.
L'étape suivante du processus de création de paquet génère un élément `.hacs.zip` autonome (sans dépendances). L'archive contient les fichiers nécessaires à la constitution ultérieure d'un dépôt *frontend* :
`hacs.json`, la carte JavaScript générée, un fichier README, un exemple de carte Lovelace, ainsi que le paquet de carte Atlas original pour toute modification ultérieure.
La démonstration est capable de reconnaître ces fichiers `.hacs.zip` lors de l'importation d'une carte dans Home Assistant. Elle lit la structure ZIP, signale les fichiers de bundle manquants et réimporte
l'élément `atlas/*.atlas-card.json` intégré dans l'Expert Editor. Cela permet
un premier cycle complet (roundtrip) de bundle HACS.

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

Dans la démo, ces fichiers se terminent par :

```text
.atlas-card.json
```

La même fonction d'importation permet de charger des cartes Home Assistant brutes (au format JSON/YAML) ainsi que des « Atlas Card Packages ».

Avant l'importation proprement dite, ATLAS peut examiner et classer les artefacts :

- ATLAS Card Package
- Carte Home Assistant brute (JSON ou YAML)
- Exportation potentielle depuis un outil externe de création de cartes (Card Builder)
- Contenu inconnu

Les fichiers externes assimilables à des « Card Builders » ne sont pas importés automatiquement.
Ils nécessitent au préalable une opération explicite de mappage de compatibilité ainsi qu'une
vérification de licence.

À l'issue de cet examen, une décision d'importation est générée pour l'interface :

- **Import** : artefacts ATLAS ou Home Assistant pris en charge.
- **Review** : artefacts externes assimilables à des « Card Builders ».
- **Reject** : contenus inconnus ou impossibles à classer avec certitude.

Pour la phase de révision, ATLAS fournit des points de contrôle structurés : limites de licence, blocs visuels détectés, emplacements d'entités (*entity slots*) identifiés, ainsi que l'étape suivante pour le mappage du schéma. L'interface utilisateur peut exploiter ces données pour générer un dialogue avant la conversion d'un artefact externe en champs ATLAS.

Par ailleurs, ATLAS est capable de générer un aperçu du mappage. Les types de blocs externes courants sont associés à des modèles (*templates*) ATLAS : les blocs de type « état » (*state*) sont mappés vers des boutons d'état, ceux de type « commutateur » (*switch*) vers des boutons de commutation, et les blocs de mise en page horizontaux ou verticaux vers des modèles de pile (*stack*) appropriés. Les blocs non reconnus restent visibles et doivent être évalués manuellement.

À partir de cet aperçu de mappage, ATLAS peut également générer un aperçu des champs validés destiné à l'interface « Expert ». Les champs sont disposés sur une grille ; ils contiennent initialement des entités vides et restent soumis à une révision. Cela permet à l'interface de présenter une conversion sans procéder à un import silencieux.

La démonstration de l'éditeur de cartes (*Card Editor*) intègre désormais cette vérification juste avant l'importation d'une carte Home Assistant. Les paquets ATLAS pris en charge ainsi que les cartes Home Assistant brutes sont importés ; les fichiers externes (similaires à ceux générés par un constructeur de cartes) génèrent un affichage de révision, tandis que les artefacts inconnus sont rejetés avant l'analyse (*parsing*).
L'aperçu d'état ATLAS (*Status Preview*) — qui sert de test rapide (*smoke test*) pour le rendu, les thèmes et les entités — est conservé, mais il est désormais placé dans une section « Diagnostics » repliable, en dehors du flux principal de l'éditeur de cartes. L'état d'ouverture ou de fermeture de cette section « Diagnostics » est mémorisé dans la configuration locale de la démonstration.

De plus, la démonstration inclut désormais l'éditeur visuel « Expert ». Il utilise
la palette de modèles commune, permet de sélectionner une famille de cartes,
place les éléments par simple clic ou par glisser-déposer au sein d'une grille limitée à 12 colonnes,
et génère le code correspondant pour les cartes imbriquées de Home Assistant. Les éléments peuvent
être sélectionnés, déplacés, supprimés et redimensionnés en mode édition. Lors du dépôt, ATLAS recherche un emplacement libre dans la grille,
évitant ainsi que les éléments nouveaux ou déplacés ne se superposent à des tuiles déjà occupées.

Le processus d'importation prend désormais en charge les cartes Home Assistant imbriquées. Une
carte `vertical-stack` peut ainsi contenir des lignes `horizontal-stack`,
des conteneurs `grid`, des cartes `conditional` ainsi que des cartes individuelles ;
ATLAS préserve la structure prise en charge tout en extrayant les entités qu'elle contient.
Les en-têtes « Bubble » ou les séparateurs dépourvus d'entité sont également acceptés.
Les colonnes « Bubble Switch » créées manuellement et les cartes `empty-column` sont
également reconnues. La prise en charge d'éléments avancés de « Bubble Card » — tels que
`modules`, `styles`, `grid_options`, les curseurs (sliders) et les sous-boutons —
est prévue pour une phase ultérieure.
Les cartes `custom:tabbed-card-v2` créées manuellement, incluant des `tabs[].card` et
des zones empilées (stacks) imbriquées, sont également détectées et ouvertes
en tant que conteneurs à onglets (tabbed containers) en mode expert.

### Éditeur de mise en page de cartes {#card-layout-editor}

ATLAS évolue vers un éditeur visuel permettant aux utilisateurs de construire
une carte Home Assistant par glisser-déposer. Le nom de la carte et le nom du fichier
JavaScript restent distincts : un utilisateur peut, par exemple, nommer une carte
`Energy Kitchen` et générer ultérieurement un fichier installable `energy-kitchen.js`,
au lieu d'être limité à un nom fixe tel que `atlas-card.js`.

En vue de l'exportation ultérieure du paquet de cartes HACS, il est également prévu d'inclure des entités de démonstration, telles que `binary_sensor.atlas_status` et `sensor.atlas_temperature`, comme configuration par défaut sécurisée. L'interface doit indiquer clairement que ces entités exemples doivent être remplacées par vos propres entités Home Assistant.

L'éditeur s'ouvre directement sur le flux de travail « Expert ». L'ancien mode « Simple » (qui était visible) ainsi que le sélecteur « Simple/Expert » ont été supprimés afin de rendre l'interface plus compacte et de privilégier l'espace d'édition. Pour chaque champ, il est possible de sélectionner le type de carte, par exemple : Entities, Bubble Card, Mushroom Template, `vertical-stack`, `horizontal-stack` ou Tabbed Card V2.

À partir du plan de l'éditeur, ATLAS déduit les types de cartes réellement utilisés. Dans le cas d'une mise en page « Expert » mixte, ATLAS identifie ainsi si des ressources HACS — comme Mushroom ou Bubble Card — sont nécessaires, tandis que les champs de type « Entities » standard ne requièrent aucune ressource de carte personnalisée (custom card) supplémentaire.

Par ailleurs, un plan créé dans l'éditeur peut être converti en une configuration de carte (card) pour Home Assistant. Le flux de travail « Expert » organise les champs occupés en fonction de leurs lignes et colonnes. Plusieurs champs situés sur une même ligne sont regroupés au sein d'un élément `horizontal-stack`, tandis que plusieurs lignes sont rassemblées via un élément `vertical-stack`. Un champ individuel peut également être défini comme `horizontal-stack` ou `vertical-stack` et contenir plusieurs entrées de cartes.
L'élément `custom:tabbed-card-v2` est pris en charge en tant que conteneur dédié : des onglets sont configurés et sélectionnés dans une fenêtre contextuelle (popup), puis garnis de cartes. Par conception, ces conteneurs sont créés sans entité associée et sans carte initiale générée automatiquement. Lors de leur création, ils se voient attribuer des titres techniques séquentiels, tels que `Tabbed 1`, `Vertical 1` ou `Horizontal 1` ; les cartes placées à l'intérieur conservent, quant à elles, leurs propres titres. La carte HACS prend également en charge des variables de style personnalisées pour les arrière-plans des onglets (actifs ou inactifs) ; la liste complète est disponible dans la [documentation de l'éditeur de cartes](/fr/projects/atlas/card-editor#tabbed-card-v2-styling).
Si un plan « Expert » ne contient pas encore de champs occupés, ATLAS utilise les entités de démonstration comme solution de repli sécurisée.

Dans la version de démonstration, le sélecteur de mise en page simplifié ainsi que le code standard des cartes Home Assistant sont masqués. Les fonctions d'exportation, d'exportation de paquet (package), de copie et de copie de ressources utilisent le code de carte HA « Expert » issu de l'interface de l'éditeur. La fonction de copie de ressources inclut toutes les dépendances Mushroom et Bubble déployées, ainsi que la ressource frontend ATLAS. Les éléments `Panel group`, `Group name`, `Card target`, `Card layout` ainsi que les
boutons d'action de groupe sont masqués, car la zone d'édition détermine
directement la structure de la carte à exporter. À cet effet, l'éditeur utilise
un champ dédié, `Expert card name`, pour les fonctions de copie, d'exportation et la
gestion du nom de fichier du paquet.

Une palette latérale de modèles (templates) est prévue pour l'utilisation. Elle propose
des composants visuels tels que « Entity List », « State Button », « Switch Button »,
`vertical-stack` et `horizontal-stack`. Dans la démo, cet élément a été configuré
comme une palette située à gauche, sans changement de mode : l'utilisateur peut
cliquer sur un composant ou le faire glisser-déposer dans la zone d'édition.
Les champs ajoutés apparaissent sous forme de tuiles déplaçables sur la grille.
La zone utilise une grille visible à 12 colonnes, rappelant davantage celle de
Home Assistant. Lors du déplacement de champs existants,
ATLAS s'appuie sur la grille interne réelle et conserve le point précis où la tuile a été saisie ;
cela permet de déplacer les champs vers le haut sans qu'ils ne sautent latéralement.
La grille visible se situe sur la même surface interne que les tuiles, avec
un espacement réduit entre les tuiles pour un empilement plus dense. Les tuiles sélectionnées peuvent
en outre être déplacées d'une cellule de la grille à l'aide des touches fléchées ; dans
En mode édition, `Shift` plus une touche fléchée modifie la taille de l’élément sélectionné
par pas de 1. Chaque composant de la
La palette peut définir ses propres colonnes de 1 à 12 ou `full`, ainsi que des lignes `auto` ou
de 1 à 8. Entity List, State Button, Switch Button, `horizontal-stack` et
`vertical-stack` commencent avec la même surface par défaut ; les piles horizontales peuvent
s’élargir lorsque plusieurs entités sont sélectionnées. La palette
peut utiliser les ressources Lovelace chargées pour indiquer si les familles de cartes personnalisées sont
installées, manquantes ou non vérifiées. Lors du placement sur la
surface Expert, ATLAS limite la colonne, la ligne et la taille aux
limites autorisées de la grille afin que les éléments restent dans la surface valide.
Les champs placés peuvent être sélectionnés et modifiés
en mode édition. La poignée en bas à droite apparaît uniquement dans ce mode ; elle permet de
redimensionner le champ dans la grille de 12 colonnes.
Les titres des champs placés sont modifiables. Les nouveaux champs reçoivent initialement
un titre numéroté automatiquement selon leur type, par exemple `Entity 1`,
`Bubble 1`, `Mushroom 1`, `Tabbed 1`, `Vertical 1` ou `Horizontal 1`.
Ce titre est utilisé lors de l’export comme titre Entities, nom du bouton Bubble ou
texte principal Mushroom. Un bouton Apply applique le titre
modifié manuellement au champ sélectionné.
Le bouton de reprise existant peut également utiliser directement
le nom de l’entité Home Assistant sélectionnée comme titre.
En mode Expert, sélectionner une entité dans le sélecteur ou la liste d’entités
l’attribue au champ actuellement sélectionné dans l’éditeur et préremplit le titre avec
le nom de l’entité.
Pour les champs Bubble, ATLAS affiche également une liste déroulante Bubble Button Type.
Les valeurs prises en charge sont `state`, `switch`, `slider` et `name` ; la valeur est
écrite dans `button_type` dans le code Bubble Card généré.
La palette Expert de gauche sépare les cartes Core et Community. Les cartes individuelles
peuvent être cochées comme favorites et enregistrées avec `Save favorites`.
Une fois les favoris enregistrés, ATLAS masque toutes les
...d'autres cartes. `Show all cards` permet de rouvrir la liste complète,
sans supprimer les favoris enregistrés. De plus, les éléments inutiles
peuvent être masqués dans la palette standard via une case à cocher rouge `Versteckt`,
et réaffichés ultérieurement depuis la liste complète.
Une option supplémentaire (à activer volontairement) permet d'associer automatiquement
des ressources enregistrées inconnues à un type de carte `custom:*` en se basant sur leur nom de fichier ; cette option se trouve parmi
les outils d'importation et est signalée par un avertissement de sécurité en rouge.
Cela permet de sélectionner facilement plusieurs favoris a posteriori, puis
de les enregistrer en une seule fois.
`Scan HA cards` lit les ressources Lovelace actuellement enregistrées dans Home
Assistant et ajoute à la palette les cartes communautaires détectées, telles que Mushroom ou Bubble Card.
Home Assistant ne fournit pas de registre complet des options
pour chaque carte personnalisée (*custom card*), mais les ressources installées peuvent servir
de point de départ. Les autres ressources Lovelace enregistrées apparaissent
comme des entrées « à analyser » (*scan-only*), jusqu'à ce qu'ATLAS dispose d'une correspondance (*mapping*) prédéfinie
soit disponible. L’utilisateur peut associer localement ces entrées à un type de carte `custom:*`
approprié. Une fois associés, ils peuvent être déplacés en tant que « cartes personnalisées » (Custom Cards) mappées ; ils sont exportés dans le
fichier YAML expert avec ce type de carte, et leur chemin de ressource est inclus dans le
fragment de ressource. Les ressources déjà mappées sont dédoublonnées,
afin d'éviter qu'elles n'apparaissent à nouveau sous forme de copie « en lecture seule » (scan-only).
La liste principale (Core) inclut désormais : Entité, Entités, Aperçu (Glance), Bouton,
Grille, Capteur, Pile (Stack), Pile horizontale, Thermostat, Lien et Page Web. La
page web est exportée comme carte Home Assistant `iframe`. Le modèle
modèle « Aperçu » (Glance) est initialisé sans entité de démonstration ; il reçoit automatiquement un nom
tel que `Glance 1` ou `Glance 2` et est configuré via une
fenêtre contextuelle (popup) dédiée aux entités.
Lors de la connexion à Home Assistant, ATLAS demande automatiquement
cette liste de ressources. L'activation des favoris enregistrés masque toutes les cartes non sélectionnées,
masquent, y compris les entrées analysées sous `/hacsfiles/`. Les cartes masquées restent
invisibles dans la vue normale jusqu’à ce que `Show all cards` soit utilisé et que
...le marquage « masqué » est supprimé. Les ressources HACS et HA
détectées (scan uniquement) peuvent également être marquées comme favorites. Les ressources auxiliaires
telles que les outils de cartes (card-tools), les tableaux de bord, les stratégies, les aides à la navigation, les packs d'icônes et
d'autres ressources identifiées comme n'étant pas des cartes sont masquées lors de l'analyse (scan) de la palette.
La vérification temporaire des ressources dispose d'une section de débogage activable. Via
`Ressourcen-Debug anzeigen`, il est possible d'afficher l'historique des requêtes WebSocket et
celles du proxy d'administration, afin de déterminer si le problème provient du WebSocket du navigateur,
du proxy WebSocket d'administration ou d'un mécanisme de secours (fallback).
La liste des entités Home Assistant est mise en cache localement dans le navigateur. À l'ouverture,
le dernier catalogue connu est immédiatement disponible pour le filtrage et la sélection ; lors
d'une connexion à Home Assistant, ATLAS synchronise la liste en temps réel et
indique, sous l'état de la connexion, si le catalogue provient du cache, s'il est en cours de
synchronisation, s'il est entièrement chargé ou si une erreur est survenue. Le message
signale également les entités ajoutées ou supprimées.
Un bouton de réinitialisation permet d'afficher à nouveau la liste complète. La palette elle-même est
dotée d'une barre de défilement et utilise des lignes de modèle compactes à deux colonnes : le nom de la carte et
le statut de favori figurent à gauche, tandis que les détails de mise en page et les commandes de taille se trouvent à droite.
Les paramètres de colonnes et de lignes des modèles sont enregistrés avec la
configuration locale de démonstration et peuvent être réinitialisées avec `Reset sizes` aux
valeurs par défaut.
Les champs de l'éditeur sélectionnés peuvent être redimensionnés à la souris, ou en ajustant leur largeur et leur hauteur par
incréments unitaires, jusqu'à cinq cellules de grille au-delà de la
taille par défaut du modèle. La zone de l'éditeur elle-même dispose, en bas à droite, d'une
poignée visible permettant de l'agrandir dans les deux directions, jusqu'à cinq unités de grille ;
la taille actuelle est conservée comme nouvelle référence par défaut. Un bouton de réinitialisation
permet de rétablir la taille par défaut de la zone de l'éditeur.
Les champs « Expert » placés, le champ sélectionné ainsi que la zone de l'éditeur
agrandie sont enregistrés localement dans le navigateur et restaurés
après un rechargement de la page.
L'interface de l'éditeur est disponible en allemand, anglais et français (DE/EN/FR).
Le sélecteur de langue situé dans l'en-tête définit la langue de l'interface utilisateur. Ce choix est également
enregistré localement et restauré lors de la prochaine ouverture de l'application. Outre les
libellés statiques, les retours provenant des sélecteurs d'entités, les résumés de piles (stacks),
les notifications de dépendances ainsi que les messages importants relatifs aux opérations d'importation/exportation sont tous
traités via une table de traduction partagée.
Le résumé détaillé (« expert summary ») fournit des informations sur les champs — notamment les champs renseignés, les emplacements vides,
les lignes occupées, la surface actuelle, les chevauchements, les cibles de carte, et
les types de disposition — avant que le code de la carte Home Assistant généré ne soit copié ou exporté.
Les champs de l'éditeur qui se chevauchent sont mis en évidence directement sur la surface.
`Auto arrange` organise les champs — en suivant l'ordre des lignes et des colonnes — dans les premiers
emplacements disponibles de la grille, réduisant ainsi les chevauchements sans modifier
le contenu de la carte. Lors des opérations classiques de glisser-déposer ou de repositionnement, ATLAS
recherche également un emplacement cible disponible si la position souhaitée dans la grille est déjà occupée.
La liste des entités sélectionnées, située sous l'éditeur, peut être repliée ;
elle est repliée par défaut, mais peut être développée si nécessaire.

### Importation YAML et styles {#yaml-import-und-styles}

L'éditeur peut intégrer des configurations brutes de cartes Home Assistant, au format YAML ou JSON. Les données YAML peuvent être saisies via une fenêtre de saisie, collées depuis le presse-papiers ou chargées à partir d'un fichier — en utilisant des extensions telles que `.yaml`, `.yml` ou `.txt`. Le code YAML importé demeure pratiquement inchangé ; Atlas ne le complète ou ne le modifie que lorsque l'utilisateur effectue des ajustements spécifiques au sein de l'éditeur.

Lors de l'importation, ATLAS identifie les styles `card_mod` et `uix`. Les styles propres à chaque entité sont associés aux entités importées et affichés dans l'aperçu via une fenêtre contextuelle de style compacte. Dans l'éditeur d'entités (vue d'ensemble), les styles détectés sont également affichés directement sous chaque entité, sous forme de code de style repliable. Les styles de carte globaux restent visibles séparément. Lors d'une « exportation experte », les styles associés aux entités sont conservés aux côtés de leurs blocs d'entités respectifs. Lors d'une exportation standard de carte Home Assistant, l'utilisateur peut choisir de conserver les styles sous la forme `card_mod` ou de les exporter sous la forme `uix`.

### Référence externe : Constructeur de cartes Home Assistant {#externe-referenz-home-assistant-card-builder}

Le projet
[`studiobts/home-assistant-card-builder`](https://github.com/studiobts/home-assistant-card-builder)
constitue une référence externe importante pour les éditeurs visuels de cartes Home Assistant. Il intègre déjà un constructeur par glisser-déposer, un système basé sur des blocs, un panneau dédié à Home Assistant ainsi qu'un moteur de rendu.

Actuellement, ATLAS n'intègre aucun code source provenant de ce projet. Celui-ci étant régi par la licence AGPL (3.0), toute création d'un véritable « fork » (dérivation) ou toute utilisation dérivée entraînerait des obligations strictes en matière de licence et d'attribution. Pour ATLAS, la stratégie retenue est la suivante : développer des définitions (contrats) et des modèles d'interface utilisateur (UI) indépendants, mentionner clairement l'origine, et envisager ultérieurement — au choix — une compatibilité d'import/export ou la création d'un « fork » explicitement identifié comme tel.

Le plan d'interopérabilité distingue trois approches :

- **Inspiration** : les idées de produits accessibles au public et les comportements documentés servent de base à la création de définitions (contrats) propres à ATLAS.
- **Compatibilité Import/Export** : à terme, ATLAS pourra analyser des artefacts documentés et proposer ses propres correspondances (« mappings »), sans pour autant copier le code source.
- **Fork / Dérivation** : cette option ne sera retenue que dans le cadre d'une décision délibérée, impliquant l'application de la licence AGPL (3.0-Erfüllung), une attribution visible et une vérification complète des conditions de licence.

### Résumé de l'importation {#import-summary}

Lors de l'importation, ATLAS normalise la carte sous forme d'un résumé contenant les éléments suivants :

- Titre
- Entités
- Format
- Cible
- Mise en page (Layout)
- Dépendances
- Indication précisant si la source était un « Atlas Card Package »

Cette approche permet de maintenir la logique propre à l'éditeur au sein du paquet `@atlas/homeassistant`, évitant ainsi qu'elle ne soit dispersée dans l'interface utilisateur.

### Vérification des ressources Lovelace {#lovelace-ressourcenprufung}

Lorsqu'ATLAS est connecté à Home Assistant, la démo peut récupérer les ressources Lovelace et vérifier si des composants tels que « Mushroom » ou « Bubble Card » sont enregistrés.

États possibles :

- `not-required` : « Entities Card » ne nécessite aucune ressource de carte personnalisée (*custom card*)
- `unchecked` : non encore vérifié
- `installed` : ressource attendue trouvée
- `missing` : ressource attendue manquante

### ATLAS en tant qu'interface (frontend) pour Home Assistant {#atlas-als-home-assistant-frontend}

L'intégration [ATLAS Runtime](/fr/projects/atlas/frontend), qui peut être installée,
intègre l'environnement d'exécution existant en tant que panneau (*panel*) dédié dans Home Assistant. Le type de dépôt HACS est
**Integration** (Intégration) et le chemin du module est
`/atlas_frontend/frontend/atlas-homeassistant-panel.js`. Ne pas enregistrer ce chemin en tant que
ressource Lovelace supplémentaire. En revanche, les cartes exportées utilisent
leur propre dépôt de tableau de bord (*dashboard*) ainsi que le nom de fichier de script généré spécifiquement.

Les anciennes cibles de ressources (*resource targets*) présentes dans l'éditeur demeurent des métadonnées de diagnostic ou de planification :

| Type d'utilisation | Objectif | Chemin de ressource attendu |
|---|---|---|
| Serveur ATLAS | Éditeur ATLAS auto-hébergé ou panneau (*panel*) | `/local/atlas/atlas-homeassistant-panel.js` |
| ATLAS HACS | Cible de ressource historique (ne correspond pas au chemin d'installation de l'intégration) | `/hacsfiles/atlas/atlas-homeassistant-panel.js` |

La vérification des ressources permet d'afficher ces informations distinctes :

- La ressource de l'interface ATLAS est-elle enregistrée ?
- La ressource de carte sélectionnée est-elle installée ?
- Manque-t-il des chemins HACS supplémentaires pour « Mushroom Card » ou « Bubble Card » ?
- L'exportation complète est-elle prête pour Home Assistant ? - Quelles ressources JSON ou YAML doivent être enregistrées dans Home Assistant ?

Pour l'installation effective du panneau, seul le guide d'intégration
(lien ci-dessus) fait foi. Un simple « Resource-Target » ne suffit pas à réaliser l'intégration.

### Démo actuelle {#aktuelle-demo}

Dans le dépôt ATLAS, la démo peut être lancée après la compilation (build) :

```sh
pnpm build
node examples/status-demo/server.mjs
```

Adresse par défaut :

```text
http://127.0.0.1:4174/
```

Sur les écrans larges, la démo utilise des grilles compactes à deux ou trois colonnes
pour la connexion, la configuration des cartes et le sélecteur d'entités ;
ainsi, les champs de saisie associés s'affichent côte à côte plutôt que
sur toute la largeur de la page.

### Feuille de route (Roadmap) {#roadmap}

L'intégration à Home Assistant est conçue pour deux modes d'utilisation :

- ATLAS en tant que serveur ou éditeur autonome
- ATLAS en tant qu'interface (frontend) pour Home Assistant, via l'intégration optionnelle HACS

Les paquets de cartes (« Card Packages ») et les ensembles HACS (« HACS Bundles »)
peuvent être exportés puis réimportés. Le processus complet via HACS
(dépôt, version, mise à jour, restauration) a été testé de manière isolée ;
les instructions et les limites sont détaillées dans l'[Éditeur de cartes](/fr/projects/atlas/card-editor).

Lors de l'exportation de paquets de cartes ou d'ensembles HACS, l'Éditeur de cartes
demande de sélectionner les langues souhaitées pour les cartes. Cela ne concerne
que la carte exportée, et non l'interface ATLAS elle-même. `en` est
toujours inclus par défaut (langue de secours obligatoire) ; d'autres langues
européennes peuvent être sélectionnées via des cases à cocher, y compris
`ru` pour les utilisateurs russophones. Tant qu'aucune traduction automatique n'est activée, ATLAS génère, pour les langues supplémentaires, des fichiers de secours en anglais accompagnés d'une mention indiquant que les fichiers `locales/*.json` correspondants doivent être traduits et vérifiés avant toute publication.

L'administration Atlas gère la sélection du module de traduction :
`none`, `chatgpt`, `gemini`, `deepl-free`, `deepl-pro` et `custom-ai`.
Cette sélection ne signifie pas pour autant que chaque adaptateur de fournisseur est déjà implémenté. Dans le Card Editor, une case à cocher permettant la traduction automatique peut être activée lors de l'exportation. L'interface affiche alors une barre de progression. Les fichiers qui n'ont pas été traduits par un fournisseur configuré restent marqués comme « solution de repli » (fallback). L'intégration avec ChatGPT/OpenAI nécessite une connexion Internet ; les fichiers traduits automatiquement doivent impérativement être vérifiés.
Pour DeepL, `https://www.deepl.com/de/pro#api` est prévu comme référence pour les options des API Free/Pro.
Le point de terminaison (endpoint) préparé pour DeepL Translate est
`https://api.deepl.com/v2/translate` ; les détails de la requête sont suivis via
`https://developers.deepl.com/api-reference/translate/request-translation`.
Ce point de terminaison relève de la configuration interne et ne doit pas apparaître comme un champ de saisie classique dans l'administration Atlas.
Pour Gemini, `https://ai.google.dev/gemini-api/docs/api-key` est prévu comme référence
pour la clé API et les consignes de sécurité. Les clés API des fournisseurs doivent être gérées dans l'administration Atlas ou dans des adaptateurs backend ultérieurs ; le Card Editor ne doit recevoir que les informations relatives au fournisseur, au point de terminaison et à l'état de configuration de la clé.
ChatGPT/OpenAI constitue le premier adaptateur intégré. À cet effet, le Card Editor sollicite l'administration Atlas via `/api/card-translation`, et le serveur d'administration utilise la clé OpenAI qui y est stockée pour interroger l'API OpenAI. Les fichiers de localisation générés avec succès sont marqués sous la référence `machine` et doivent impérativement être vérifiés avant toute publication. Le nom du modèle OpenAI utilisé peut être remplacé côté serveur via `ATLAS_OPENAI_TRANSLATION_MODEL`.
Lors du rechargement de l'interface d'administration Atlas, la page d'administration restaure le jeton (token) Home Assistant ainsi que les clés API des fournisseurs à partir d'un cookie d'administration chiffré à longue durée de vie. La clé de déchiffrement, conservée côté navigateur dans le stockage local de l'administration, garantit que le cookie lui-même ne contient ni clés de fournisseur ni jeton en clair.
Par ailleurs, la page d'administration peut actualiser les secrets en interrogeant le serveur d'administration local en cours d'exécution via `GET /api/admin-connection?includeSecrets=1`. Les clés et le jeton ne sont, en aucun cas, inscrits dans le cookie de transfert (« handoff cookie ») partagé ni dans les charges utiles (« payloads ») de transfert de l'éditeur de cartes. Pour les sauvegardes, l'interface d'administration permet une exportation via `atlas-admin-settings.json` : les paramètres classiques restent lisibles, tandis que le jeton et les clés API des fournisseurs sont intégrés sous forme d'un bloc chiffré en AES-GCM, identifié par `encryptedSecrets`.
Ces secrets chiffrés sont, en outre, liés à l'installation locale de l'administration Atlas. À cette fin, le serveur d'administration génère un identifiant d'installation stocké dans les données utilisateur locales (en dehors du dépôt), ou utilise `ATLAS_INSTANCE_ID` si une installation Docker ou serveur doit se voir attribuer une identité stable et définie. Si seul le dossier du serveur ou un fichier d'exportation est copié vers un environnement tiers, les secrets seront considérés comme invalides.
Si les paramètres classiques peuvent généralement être migrés ultérieurement, le transfert des secrets nécessite, quant à lui, une procédure spécifique, telle qu'une fonction de transfert dédiée ou l'utilisation d'une phrase secrète (« passphrase »).

La « Lovelace UV Card » est prévue comme projet ultérieur. Le projet `filipnet/haos-uv-index` a été retenu comme source d'inspiration pour cette carte. L'objectif n'est pas de reprendre le code, mais de s'inspirer des idées de produit : capteur d'indice UV, indicateur de risque par code couleur, recommandations de protection basées sur celles de l'OMS, affichage compatible avec le style « Mushroom » et automatisation optionnelle des notifications.

L'éditeur de cartes (Card Editor) pour Home Assistant constitue le premier plugin de référence ATLAS officiellement intégré. Il combine la sélection d'entités, les cibles de cartes, les fonctions d'import/export, la gestion de paquets (similaire à HACS) et l'administration au sein d'un véritable flux de travail (workflow).

Au sein du paquet Atlas, cette étape est déjà préparée par `createHomeAssistantCardEditorPlugin()`. Cela permet d'activer l'éditeur via l'interface de plugin « runtime » et de le retrouver dans le catalogue de plugins.
Par ailleurs, `createHomeAssistantCardEditorPluginInstallPackage()` génère un premier paquet d'installation incluant un manifeste, un fichier README et une configuration d'exemple.

Cette étape du plugin est déjà visible : l'administration minimale d'Atlas fonctionne comme une interface distincte sur le port `4175`, séparée de l'éditeur de cartes qui, lui, se trouve sur le port `4174`. Elle affiche l'éditeur de cartes en tant que plugin de référence installé et permet d'exporter le paquet du plugin sous la référence `.atlas-plugin.json`. L'interface d'administration marque également une limite de sécurité : les jetons (tokens) et les paramètres de connexion sont centralisés dans Atlas. L'éditeur ne reçoit le jeton que par transmission de session depuis l'administration, tandis que les plugins n'ont accès qu'à des chemins, des URL et des fonctionnalités spécifiquement autorisés.

::::
