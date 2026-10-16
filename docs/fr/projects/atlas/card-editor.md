---
title: Home Assistant Card Editor
description: "Guide de l’éditeur Expert ATLAS : connexion, palette, conteneurs, import, export et styles Tabbed Card V2."
---

# Home Assistant Card Editor

Le **Home Assistant Card Editor** est le premier plugin de référence intégré
à ATLAS. Il permet de concevoir visuellement des cartes, d’importer le YAML
existant et de préparer des packages ou bundles destinés à HACS.

L’éditeur local utilise `http://127.0.0.1:4174/` ; les connexions sont gérées
par l’Administration sur `http://127.0.0.1:4175/`.

Depuis l’application HA **0.1.286**, le rechargement et l’import JSON/HACS
préservent les identifiants de modèles et les dimensions de référence du
redimensionnement. Le réimport d’un bundle compare les deux noms de manifeste,
même si le nom du projet diffère du titre de la première carte. Les contenus
et paramètres existants sont conservés.

Le parcours Administration → Hub → connexion HA → Expert → export/import a été
vérifié en DE/EN/FR avec un endpoint simulé, un profil isolé et un plugin de test,
y compris rechargement et redémarrage du conteneur. Les vérifications natives
complémentaires sur Pi 5 et Proxmox sont terminées ; leur périmètre et leurs limites sont consignés
dans l’[état du développement](/fr/projects/atlas/development-status).

## Signaler un problème (depuis 0.1.287)

Le signalement crée d’abord un aperçu local. Le bouton de copie utilise
le texte vérifié ; si le presse-papiers échoue, vous pouvez le copier
manuellement. Le bouton GitHub ouvre seulement le formulaire avec des
instructions. Le rapport n’est ni envoyé automatiquement ni intégré dans l’URL.

Le filtre retire les identifiants sensibles des champs structurés, du JSON/YAML,
des URL et des fragments de jeton, ainsi que le jeton HA connu dans le reste
du texte. Il ne lit ni cookies ni stockage du navigateur ; les indicateurs de
clé configurée sont des booléens. Relisez néanmoins les textes des cartes,
entités et informations personnelles avant partage. L’ouverture du rapport
ne modifie pas les projets, paramètres ou plugins.

## Workflow Expert

L’éditeur ouvre directement le workflow Expert. Le mode Simple et le sélecteur
Simple/Expert ont été supprimés ; les imports anciens pris en charge restent
compatibles. Import HA, collage YAML, diagnostic des ressources et sélection
des entités restent disponibles.

Déposez les cartes depuis la palette gauche sur une grille semblable à celle
de Home Assistant. Vous pouvez les déplacer, redimensionner, imbriquer et
exporter en YAML. Les cellules restent carrées ; X et Y règlent les colonnes
et lignes, tandis que Zoom modifie leur taille sans déformer la grille.

## Connexion Home Assistant

L’éditeur reçoit l’URL et le jeton uniquement comme transmission de session
depuis l’Administration ; il n’enregistre pas durablement le jeton lui-même.

Il prend en charge :

- l’API WebSocket Home Assistant ;
- les entités via `get_states` ;
- le cache local des entités et domaines ;
- l’état de synchronisation sous l’état de connexion ;
- la recherche par domaine, nom et identifiant ;
- la vérification Lovelace via le WebSocket du navigateur et le proxy Admin.

Le diagnostic des ressources permet d’identifier un blocage dans le WebSocket,
le proxy ou le mécanisme de repli. Pour les URL mobiles, le port 80 et l’erreur
1006, voir le [guide de connexion](/fr/projects/atlas/homeassistant).

## Liste des cartes

La palette Expert contient les cartes Core, les modèles locaux et les cartes
Community détectées :

- Entity, Entities et Overview / Glance ;
- Button, Grid et Sensor ;
- Vertical stack et Horizontal stack ;
- Thermostat, Link et Webpage ;
- Mushroom Template, Bubble Card et Tabbed Card V2.

Les ressources sans correspondance intégrée restent des informations de scan.
Une correspondance locale avec un type `custom:*` les rend déplaçables et
conserve leur chemin de ressource dans les exports. Les ressources auxiliaires
peuvent être masquées ; la liste complète permet de les rétablir.
La déduction automatique d’un type depuis le nom du fichier JavaScript est
facultative et affiche un avertissement rouge.

Les favoris enregistrés masquent les autres cartes. Une carte favorite ne peut
pas être masquée ; afficher toutes les cartes conserve les favoris.
Les tailles et favoris peuvent être réinitialisés séparément.

## Cartes conteneurs

Les conteneurs pris en charge sont `vertical-stack`, `horizontal-stack`
et `custom:tabbed-card-v2`. Ils acceptent des cartes par glisser-déposer.
Tabbed Card V2 gère ses onglets et leurs cartes ; les piles conservent leurs
enfants séparément et les présentent dans la boîte d’information.

## Import

Les sources prises en charge sont les fichiers YAML, le YAML collé,
le JSON, les packages ATLAS et les bundles HACS intégrant
`atlas/*.atlas-card.json`.

ATLAS détecte les styles `card_mod` et `uix`. Les styles d’entité sont
associés à leur entité ; les styles globaux restent visibles à part.
Le YAML d’origine est conservé autant que possible et évolue lorsque la carte
est modifiée. La conservation de toutes les options de cartes tierces n’est
pas garantie.

Les cartes `custom:tabbed-card-v2` écrites manuellement avec
`tabs[].card`, des piles imbriquées et des cartes personnalisées brutes
prises en charge ouvrent une structure de conteneurs Expert.

## Export

Les sorties comprennent le YAML Home Assistant, le YAML Expert, le script
de carte, le package ATLAS, le bundle HACS et la liste des ressources.

Lors de l’export HA, choisissez le format de styles `card_mod` ou `uix`.
Les noms de téléchargements peuvent recevoir un compteur afin de distinguer
les fichiers ; le comportement final dépend aussi du navigateur.

La langue de la carte exportée est indépendante de la langue ATLAS.
`en` est obligatoire comme repli. Les langues supplémentaires non traduites
sont identifiées comme replis à traduire et à vérifier. Le chemin réel
ChatGPT/OpenAI passe par l’Administration et nécessite Internet ; les fichiers
traduits automatiquement restent à relire. Voir le
[modèle d’export et les secrets](/fr/projects/atlas/homeassistant#feuille-de-route-et-langues-exportees).

### Aller-retour du bundle HACS vérifié

L’App **0.1.307** vérifie un projet mixte Core/Bubble/Mushroom dans HA Core
**2026.10.1** isolé : import ZIP, téléchargement réel dans le navigateur,
réimport et nouvel export conservent champs, grille et configuration des cartes.
Le ZIP réexporté est identique octet par octet dans ce test. Les contrôles
comparent le nom du projet au nom vérifié du package ; les noms différents
des cartes internes ne provoquent plus de faux conflits de titre.

Le script exporté fonctionne dans HA réel avec Bubble **3.4.2** et Mushroom
**5.2.3**, avec mise à jour des états en direct. HA utilise des piles générées ;
les métadonnées de grille conservées ne garantissent pas une géométrie identique
au pixel près. Les ressources isolées sont servies via `/local/` ; cela ne
valide pas le téléchargement depuis un dépôt HACS.

### Fichiers de langue du script exporté

Depuis l’App **0.1.308**, le script Card charge `locales/en.json` et la langue
choisie relativement à sa propre URL. Déployer le JavaScript et le dossier
voisin `locales/` ensemble sur la même origine HA ; déclarer la ressource
Lovelace avec le type `module`. La Card suit la langue HA. `language: de` ou
`language: fr` dans sa configuration permet de la fixer ; les variantes
`de-DE` et `fr-FR` utilisent leur langue de base.

Le titre, l’aide pour les entités de démonstration et le message d’erreur du
script utilisent ces textes. Chaque texte absent, invalide ou incomplet utilise
`en.json`, puis l’anglais intégré. Le script fonctionne aussi sans fichiers de
langue. Un `title` ou `replacement_hint` personnalisé distinct reste prioritaire.
Les noms des champs et identifiants d’entités restent intacts ; HA traduit ses
propres libellés et ceux des cartes communautaires. Chaque langue est chargée
une fois par visite. Recharger après modification ; après une mise à jour du
script, ajouter si nécessaire une nouvelle version à l’URL de la ressource.

Les exports EN/DE/FR sont indépendants de la langue de l’éditeur. Sans exécution
d’un adaptateur de traduction, DE/FR contiennent des replis anglais identifiés,
à traduire et vérifier.

### Distribution HACS commune depuis 0.1.309

Le ZIP exporté contient `hacs.json` à la racine, le script et les langues sous
`dist/`, par exemple `dist/energy-kitchen.js` et `dist/locales/en.json`.
Extraire le ZIP complet dans un dépôt GitHub dédié nommé `energy-kitchen`,
puis l’ajouter dans HACS comme dépôt Dashboard. Le nom du dépôt correspond au
nom du script sans `.js` ; utiliser un dépôt distinct de l’intégration ATLAS.

HACS installe le contenu de `dist/` dans `www/community/energy-kitchen/`.
La ressource module est `/hacsfiles/energy-kitchen/energy-kitchen.js` et les JSON
sont voisins dans `locales/`. HACS enregistre le module en mode stockage ; en
mode YAML, ajouter soi-même la ressource documentée dans le bundle.

Ne pas placer aussi le script à la racine ni publier de pièce jointe JavaScript
seule dans une release : HACS peut la préférer à `dist/`. Le ZIP exporté n’est
pas un paquet d’installation `zip_release`. HACS 2.0.5 peut omettre des langues
si le nom du script commence par `dist` ; ATLAS bloque cet export avec un message.
Choisir un autre nom de script HACS. Les projets existants restent intacts.

Le parcours réel GitHub/HACS est aussi vérifié sous HA 2026.10.1 isolé avec
HACS 2.0.5 : autorisation GitHub de l’appareil par l’utilisateur, enregistrement
comme dépôt Dashboard personnalisé et téléchargement depuis `main`. Le script
et EN/DE/FR sont installés avec les octets exacts de GitHub ; HACS enregistre
automatiquement le module. Les anciens bundles ATLAS restent importables.

Le [dépôt public d’export Card](https://github.com/rockbaer2007/atlas-hacs-delivery-card)
est explicitement un exemple de test. Dans le menu principal HACS, ouvrir
**Dépôts personnalisés**, saisir cette adresse GitHub, choisir **Dashboard** puis
**Ajouter**. Ouvrir **Locale test card**, confirmer **Télécharger** et recharger
le navigateur. La ressource est
`/hacsfiles/atlas-hacs-delivery-card/atlas-hacs-delivery-card.js`.
Dans `v0.1.0`, DE/FR sont des replis anglais identifiés. `v0.1.1` contient des
textes de test traduits manuellement : « Wohnzimmer 0.1.1 » et « Salon 0.1.1 ».
Cela ne démontre pas une traduction automatique. Bubble Card et Mushroom sont
aussi nécessaires pour cet exemple de Card mixte.

Le cycle étiqueté `v0.1.0` → `v0.1.1` → `v0.1.0` est également vérifié sous
HA 2026.10.1/HACS 2.0.5 isolé. Enregistrer d’abord une sauvegarde complète.
Dans le menu du dépôt, choisir **Actualiser les informations**. HACS détecte
la nouvelle version comme mise à jour en attente ; utiliser **Retélécharger**
pour installer la version proposée, puis recharger le navigateur.
Pour la réinstallation manuelle vérifiée de l’ancienne version, ouvrir
**Retélécharger**, développer **Besoin d'une version différente ?**, choisir
`v0.1.0` dans **Version**, télécharger et recharger. HACS recommande explicitement
de restaurer une sauvegarde plutôt que d’utiliser ce sélecteur pour revenir
en arrière. La réinstallation remplace les fichiers Card ; elle ne restaure
pas les données migrées à partir d’une sauvegarde.

Les deux releases utilisent `dist/` sans pièce jointe JavaScript séparée.
Le script et les trois fichiers de langue correspondent exactement au tag
choisi à chaque étape. La ressource module conserve son identifiant ; HACS
modifie son `hacstag`. Les autres ressources, paramètres, projets et dépendances
sont conservés. L’ancienne version fonctionne aussi après redémarrage du test.
HACS propose ensuite toujours `v0.1.1` comme mise à jour ; le choix de l’ancienne
version ne la verrouille pas définitivement.

Il s’agit d’un dépôt personnalisé, pas d’une inclusion dans la liste HACS par
défaut. Pi 5 et Proxmox restent inchangés.

### Mises à jour échouées ou interrompues

À partir d’ATLAS **0.1.310**, les scripts Card nouvellement générés vérifient EN
et toutes les langues sélectionnées pour l’export, y compris les langues inactives.
Les fichiers absents, illisibles ou JSON invalides avec des métadonnées de langue
incorrectes produisent un avis compact indiquant les chemins concernés. Le texte
de réparation EN/DE/FR est intégré indépendamment de ces fichiers. Cards et états
en direct restent utilisables avec le repli linguistique existant.

Dans HACS, retélécharger le paquet Card complet et recharger le navigateur ;
restaurer la sauvegarde si nécessaire. L’avis disparaît après réparation et
rechargement. Les scripts déjà installés doivent être réexportés et redistribués.
Ce contrôle détecte les fichiers absents/illisibles.

À partir de **0.1.311**, les scripts et langues nouvellement exportés partagent
aussi un identifiant de paquet déterministe (`_meta.packageId` dans les langues).
Un identifiant différent ou absent déclenche également l’avis ; les textes
concernés sont ignorés, avec repli EN ou anglais intégré. Conserver cet identifiant
lors de la traduction ; ne pas copier celui d’un autre paquet pour masquer l’avis.
Ce contrôle détecte les mélanges accidentels, pas les modifications de texte avec
un identifiant inchangé ; ce n’est pas une signature. Des exports identiques ont
le même identifiant. Les anciens scripts ne sont pas modifiés rétroactivement.
Il n’y a ni réparation ni restauration automatique.
Le nouveau contrôle est d’abord vérifié dans HA 2026.10.1/HACS 2.0.5 isolé :
EN/FR mélangés, identifiant absent, Cards toujours affichées et réparation après
rechargement. Pi 5 et Proxmox sont restés en 0.1.310 pendant ce contrôle isolé.

La mise à jour et le contrôle sont ensuite testés sur les deux hôtes en 0.1.311 :
Cards `/local/` propres au test, EN/FR mélangés, identifiant FR absent et réparation
après rechargement. Paramètres, projets et fichiers vérifiés restent intacts.
Constat historique distinct : la corbeille File Studio résidait dans le conteneur
App remplaçable. Seuls nos anciens dossiers de test y figuraient ; ils ont été
reconstitués depuis les copies PC avec leurs métadonnées initiales. App 0.1.312
corrige le stockage ; remplacement du conteneur et restauration sont vérifiés
en isolation. Avant la première mise à jour, transférer les anciennes données
dans l’ancien conteneur et sauvegarder le résultat ; voir [File Studio](../atlas-plugins/file-studio.md).
Pi 5 et Proxmox restent inchangés pour ce contrôle. Il ne s’agit pas d’un
nouveau test d’installation native d’un dépôt HACS.

La mise à jour 0.1.310 et ce contrôle sont aussi testés sur Proxmox et Pi 5 après
de nouvelles sauvegardes : Cards de test distinctes nouvellement générées, FR et
EN absents, puis restauration après rechargement, avec paramètres, projets et
plugins externes conservés. La vérification native utilise des ressources de
test `/local/` distinctes, pas une nouvelle installation GitHub/HACS. Un échec
de lecture temporaire peut aussi déclencher l’avis ; un premier avis dans
l’aperçu Proxmox a disparu après rechargement. Un avis seul ne prouve pas une
corruption permanente.

Des pannes ont été injectées dans une copie isolée HA 2026.10.1/HACS 2.0.5 :
le nouveau script a réellement été téléchargé depuis GitHub et écrit, puis les
téléchargements des langues ont signalé un échec ou le processus a été arrêté
brutalement avant leur fin. Seule cette copie HACS contenait l’instrumentation de test.

Lors d’un échec signalé, HACS affiche une erreur et restaure automatiquement
l’ancienne Card avec EN/DE/FR. Un arrêt brutal laisse en revanche le nouveau
script sans les fichiers de langue, même après redémarrage. HACS peut encore
afficher l’ancienne version installée. Le repli EN intégré peut maintenir la
Card visible ; l’affichage et le numéro de version ne prouvent donc pas que
l’installation est complète.

Après suppression de la panne, **Retélécharger** avec l’ancienne release connue
a été vérifié avec succès. Recharger ensuite le navigateur et contrôler le script,
tous les fichiers de langue, la ressource et l’affichage. Une sauvegarde complète
distincte de la configuration Docker HA a aussi été restaurée dans un nouveau
volume de test vide : les 2 500 fichiers étaient identiques avant démarrage ;
HACS, les Cards et les états en direct fonctionnaient ensuite. Paramètres,
tableau de bord et dépendances ont été conservés.

La sauvegarde temporaire HACS ne remplace pas votre propre sauvegarde. La réparation
automatique après arrêt brutal n’est pas garantie. Ce test contrôlé et cette
restauration de volume Docker ne couvrent pas toutes les pannes réseau/disque,
la restauration des sauvegardes HAOS ni les autres versions HACS.

## Tabbed Card V2

Cette carte ATLAS est exportée sous le type :

```yaml
type: custom:tabbed-card-v2
```

Ressource attendue :

```text
/hacsfiles/tabbed-card-v2/tabbed-card-v2.js
```

**ATLAS Tabbed Card V2 doit être installé dans Home Assistant** avant
utilisation. Il appartient à la famille de cartes ATLAS, fournie via le dépôt
`https://github.com/rockbaer2007/atlas`. Il s’inspire de
`kinghat/tabbed-card` et reste une variante ATLAS séparée.

Son éditeur Home Assistant accepte YAML ou JSON. Les blocs multilignes
`>-` et `|-` restent des valeurs multilignes afin de conserver les
expressions Jinja, les modèles Mushroom et les styles `card_mod`.
Les opacités des arrière-plans actifs et inactifs sont calculées en valeurs
de couleur stables avant le changement d’onglet.

### Styles Tabbed Card V2

Les variables Material sont complétées par celles des arrière-plans, des
arrondis et des espacements :

| Nom | Valeur par défaut | Description |
| --- | --- | --- |
| `--mdc-theme-primary` | `--primary-color` | Texte actif, indicateur et couleur d’accent. |
| `--mdc-tab-text-label-color-default` | `--secondary-text-color` | Texte inactif ; une valeur `rgba(...)` permet la transparence. |
| `--mdc-typography-button-font-size` | `14px` | Taille du texte des onglets. |
| `--tabbed-card-v2-card-background` | Arrière-plan de carte HA | Fond extérieur ; `transparent` permet une superposition. |
| `--tabbed-card-v2-card-border` | Bordure de carte HA | Bordure extérieure. |
| `--tabbed-card-v2-card-border-radius` | Rayon de carte HA | Arrondi extérieur. |
| `--tabbed-card-v2-content-padding-side` | `0` | Espacement intérieur gauche et droit. |
| `--tabbed-card-v2-content-padding-bottom` | `0` | Espacement intérieur inférieur. |
| `--tabbed-card-v2-tabbar-background` | `transparent` | Fond de toute la barre d’onglets. |
| `--tabbed-card-v2-active-background` | `transparent` | Fond de l’onglet actif. |
| `--tabbed-card-v2-active-background-opacity` | `100` | Opacité active de `0` à `100`. |
| `--tabbed-card-v2-inactive-background` | `transparent` | Fond des onglets inactifs. |
| `--tabbed-card-v2-inactive-background-opacity` | `100` | Opacité inactive de `0` à `100`. |
| `--tabbed-card-v2-hover-background` | `--secondary-background-color` | Fond au survol ou à la focalisation. |
| `--tabbed-card-v2-tab-border-radius-top` | `0` | Arrondi supérieur gauche et droit. |
| `--tabbed-card-v2-tab-border-radius-bottom` | `0` | Arrondi inférieur gauche et droit. |
| `--tabbed-card-v2-tabs-padding-left` | `0` | Espacement avant le premier onglet. |
| `--tabbed-card-v2-tabs-padding-top` | `0` | Espacement au-dessus des onglets. |
| `--tabbed-card-v2-tabs-gap` | `0` | Espacement entre onglets. |
| `--tabbed-card-v2-indicator-inset` | `0` | Retrait horizontal de l’indicateur actif. |
| `--tabbed-card-v2-indicator-border-radius` | `0` | Arrondi de l’indicateur actif. |

![Styles Tabbed Card V2 dans l’éditeur Home Assistant](/images/atlas/tabbed-card-v2-0.1.7.png)

![Résultat avec onglets arrondis](/images/atlas/tabbed-card-v2-result-0.1.7.png)

Exemple :

```yaml
type: custom:tabbed-card-v2
styles:
  --mdc-theme-primary: "#ff9800"
  --mdc-tab-text-label-color-default: "rgba(255,255,255,0.75)"
  --tabbed-card-v2-card-background: "transparent"
  --tabbed-card-v2-card-border: "0.2px solid var(--primary-color)"
  --tabbed-card-v2-card-border-radius: "12px"
  --tabbed-card-v2-content-padding-side: "16px"
  --tabbed-card-v2-content-padding-bottom: "16px"
  --tabbed-card-v2-tabbar-background: "rgba(0,0,0,0.18)"
  --tabbed-card-v2-active-background: "#ff9800"
  --tabbed-card-v2-active-background-opacity: 35
  --tabbed-card-v2-inactive-background: "#ffffff"
  --tabbed-card-v2-inactive-background-opacity: 8
  --tabbed-card-v2-hover-background: "rgba(255,255,255,0.12)"
  --tabbed-card-v2-tab-border-radius-top: "12px"
  --tabbed-card-v2-tab-border-radius-bottom: "6px"
  --tabbed-card-v2-tabs-padding-left: "8px"
  --tabbed-card-v2-tabs-padding-top: "8px"
  --tabbed-card-v2-tabs-gap: "6px"
  --tabbed-card-v2-indicator-inset: "10px"
  --tabbed-card-v2-indicator-border-radius: "999px"
tabs:
  - attributes:
      label: Light
    card:
      type: button
      entity: light.bed_light
```

## État actuel

L’éditeur reste en développement actif. Le workflow Expert, l’import/export,
les entités, les vérifications de ressources, les conteneurs et les
correspondances locales sont utilisables. Des correspondances personnalisées
vérifiées seront ajoutées progressivement. L’[état du développement](/fr/projects/atlas/development-status)
distingue les essais isolés des vérifications natives et des limites ouvertes.
