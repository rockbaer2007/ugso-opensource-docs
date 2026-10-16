---
title: ATLAS File Studio
description: "Plugin externe de fichiers : édition, transferts, archives, sauvegardes et autorisations des chemins Home Assistant."
---

# ATLAS File Studio

ATLAS File Studio est le deuxième plugin indépendant de l’écosystème ATLAS.
Il permet de parcourir et modifier les fichiers dans les chemins approuvés,
sans accès libre à la racine par défaut.

## Corbeille et historique après une mise à jour

À partir d’ATLAS **0.1.312**, les données gérées par le backend résident par défaut
dans `ATLAS_PLUGIN_DATA_ROOT/.file-studio/{trash,history}`. Docker doit conserver
le volume des plugins ; l’App HA utilise `/data/atlas-plugins`. Les chemins Linux
existants et `ATLAS_FILE_STUDIO_TRASH_ROOT` / `ATLAS_FILE_STUDIO_HISTORY_ROOT`
restent valides. Les chemins personnalisés doivent aussi être persistants et sauvegardés.

**Premier passage depuis un ancien conteneur :** sauvegarder d’abord ses anciens
dossiers corbeille/historique et les données persistantes. Suspendre les écritures
File Studio jusqu’à la mise à jour. Copier l’outil autonome de la version ATLAS
vérifiée dans l’ancien conteneur encore présent :

```sh
docker cp scripts/atlas-file-studio-retention.mjs ANCIEN_CONTENEUR:/tmp/atlas-file-studio-retention.mjs
docker exec ANCIEN_CONTENEUR node /tmp/atlas-file-studio-retention.mjs --app-root /app --plugin-root /data/atlas-plugins
```

Ces chemins concernent l’image standard ; vérifier les installations personnalisées.
Pour l’App HA, exécuter le même outil dans son terminal existant avant la mise à
jour. Il reprend une fois les anciens dossiers accessibles, conserve sources et
identifiants et refuse les fichiers cibles différents. Examiner les conflits avec
la sauvegarde. Sauvegarder ensuite les données persistantes, puis remplacer le
conteneur. Un marqueur empêche de réimporter les éléments déjà restaurés au redémarrage.

Les fichiers déjà perdus avec un ancien conteneur nécessitent toujours une sauvegarde.
Après la vérification isolée, la mise à jour de 0.1.311 vers 0.1.312 a aussi été
vérifiée sur Proxmox et Pi 5 le 16/10/2026 : sauvegardes HA récentes, migration
dans l’ancien conteneur et copies PC des données initiales et préparées avant
la mise à jour. Les deux anciens éléments de corbeille et les douze fichiers
d’historique sont conservés sur chaque hôte, ainsi que paramètres, fichiers
actifs, projets et plugins. Ce n’est pas un test de restauration HAOS complète.

## Dépôt

- GitHub : `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Installation : `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Catalogue : `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## État actuel

Le plugin est installable via le dépôt de démonstration dans l’Administration
et le Hub. Version documentée du plugin : **0.1.51** ; application HA ATLAS :
**0.1.297** au 14/10/2026. Ce sont deux versions distinctes.

Le sélecteur DE/EN/FR traduit l’en-tête, les principaux contrôles et les avis
de limite d’envoi. Les dialogues et les autres messages ne sont pas encore
entièrement traduits ; une documentation française complète ne signifie pas
que toute l’interface du plugin l’est.

Fonctions documentées :

- Arborescence de `/config` et surface flexible à deux colonnes avec limites
  facultatives de largeur et hauteur.
- Barre compacte sous l’arborescence ; création de fichier/dossier, actualisation
  et fermeture de tous les dossiers près du chemin.
- Éditeur CodeMirror 6 embarqué, avec défilement interne des grands fichiers
  conservant la ligne de statut visible.
- Liens directs vers les fichiers, même hors des branches initialement chargées,
  notamment les sorties de l’Automation Exporter.
- Coloration YAML, JSON, JavaScript, TypeScript et Markdown.
- Validation YAML avant sauvegarde avec indications Home Assistant pour
  `configuration.yaml`, `automations.yaml`, `scripts.yaml` et packages :
  clés racines usuelles, structure d’automatisation/script et secrets saisis directement.
- Enregistrement du fichier ouvert, sauvegarde automatique avant écriture,
  historique, comparaison et restauration d’une sauvegarde sélectionnée.
- Sauvegarde locale, envoi par glisser-déposer, envoi multiple et téléchargement.
- Enregistrement des envois dans le dossier sélectionné et actualisation de
  l’arborescence sans ouverture automatique du fichier.
- Noms de téléchargements numérotés dans le navigateur, par exemple
  `configuration.yaml`, `configuration-1.yaml`, `configuration-2.yaml`.
- Dialogue de conflits proposant remplacement, renommage ou annulation.
- Suppression, copie et déplacement avec sélection multiple.
- Corbeille et restauration ; son icône est grise quand elle est vide et rouge
  lorsqu’elle contient des entrées.
- Favoris de fichiers/dossiers, icônes de type colorées et badges compacts.
- Recherche avec filtres, recherche facultative dans le contenu, ligne trouvée
  et aperçu du résultat.
- Signalement facultatif avec aperçu et lien GitHub préparé ; sans jetons HA,
  clés de fournisseurs ou contenu de fichiers.
- Envoi binaire de fichiers de 64 Mio maximum vers un dossier autorisé.
  Au-delà, l’envoi est arrêté avant transfert et le plugin recommande
  l’[extension Samba](https://github.com/home-assistant/addons/tree/master/samba).
- Aperçu ZIP, TAR, TAR.GZ et TGZ ; extraction d’un fichier individuel sans
  décompresser toute l’archive.
- Extraction TAR complète avec validation des chemins et limites par fichier
  et taille totale.
- Autorisations supplémentaires pour `www`, `custom_components`,
  `addons` et `parent-of-config`.
- Encadré d’accès compact avec typographie normale et couleur distincte
  pour chaque chemin. `/addons` reste verrouillé sans autorisation explicite.

CodeMirror est livré avec le plugin : aucun CDN n’est nécessaire pour l’éditeur.

Les aperçus SVG, PNG, JPG/JPEG et WebP peuvent s’ouvrir dans Icon Studio,
installé séparément. Les images matricielles deviennent des aperçus ; les
SVG simples composés de chemins sont importés dans son jeu monochrome.
Les plugins doivent être sur le même serveur ATLAS. Le transfert utilise
une clé temporaire locale au navigateur et l’accès approuvé de File Studio ;
le fichier n’est ni téléversé ni dupliqué.

Les limites de l’extraction TAR sont de 64 Mio par fichier et 512 Mio au total ;
les liens symboliques et les types non pris en charge sont ignorés.

## Modèle de sécurité

| Chemin | Par défaut | Autorisation |
| --- | --- | --- |
| `/config` | Actif. | Sans autorisation supplémentaire. |
| `/config/www` | Visible comme capacité. | Administration ou option de l’application HA. |
| `/config/custom_components` | Visible comme capacité. | Administration ou option de l’application HA. |
| `/addons` | Désactivé. | Administration ou option de l’application HA. |
| `parent-of-config` | Désactivé. | Accord explicite de l’administrateur. |
| `/` | Désactivé. | Accès libre interdit par défaut. |

`/config` contient normalement la configuration HA, automatisations,
tableaux de bord, thèmes, blueprints, scripts et fichiers web locaux sous `www`.

`/addons` peut contenir des extensions HA locales avec `config.yaml`,
`Dockerfile`, scripts de démarrage, icônes et documentation. Les modifications
peuvent affecter les extensions installables ; ce chemin nécessite une autorisation.

Dans l’application HA, les autorisations viennent de sa configuration.
Dans Docker ou une installation Linux, l’Administration contrôle les mêmes
capacités. Les plugins reçoivent les chemins approuvés, sans secrets bruts
de longue durée.

## Mise à jour Home Assistant

Chaque mise à jour visible du package ATLAS augmente la version de
l’application HA. Home Assistant compare `old` (installée) et `target`
(dépôt). Le dernier package documenté est **0.1.297**. Si une ancienne version
cible apparaît, actualisez les informations du dépôt dans le magasin
d’extensions, puis mettez ATLAS à jour ou redémarrez-le.

Le plugin File Studio et l’application ATLAS ont des versions distinctes ;
la mise à jour de la documentation ne modifie pas les fichiers HA.

## Extensions ultérieures

- Aide YAML plus avancée, avec vérification des schémas et services depuis HA.
- Prise en charge RAR/RAR5 si un outil librement utilisable est disponible.
- Enregistrement d’icônes SVG sous `/config/www/custom_local_icons/` avec
  l’intégration HA correspondante.
- Choix entre `/config` et le dossier de sortie Automation Exporter lorsque
  ce plugin externe est installé.
