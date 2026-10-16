# ATLAS dans le frontend Home Assistant

Depuis **0.1.299**, ATLAS fournit l’intégration facultative **ATLAS Runtime**.
Elle enregistre son propre panneau latéral réservé aux administrateurs HA.
Il ouvre le Hub des plugins, Card Editor Expert et l’Administration du Runtime
existant. Le panneau suit la langue HA DE/EN/FR et le thème clair ou sombre.

## Prérequis et préservation des données

Au 16/10/2026 : **App 0.1.312**, **intégration 0.1.306**, versions indépendantes.
Les versions d’introduction et de test ci-dessous ne demandent pas de rétrograder
une App plus récente. Restauration HAOS complète et changement volontaire
d’adresse sont décrits dans le [guide de sauvegarde](../atlas-plugins/file-studio) ;
les données locales du navigateur nécessitent toujours leur propre export.

ATLAS doit déjà fonctionner comme application/add-on, conteneur Docker ou
[service Linux/systemd](/fr/projects/atlas/linux). HACS installe l’intégration HA ;
le serveur Node et les plugins externes restent dans leur Runtime existant.
L’entrée Ingress existante de l’add-on n’est pas remplacée.

Sauvegardez HA avant l’installation. Exportez aussi les projets et paramètres
Administration dans ATLAS. Conservez l’adresse navigateur actuelle : projets,
cookies et paramètres chiffrés dépendent de l’adresse ou de l’identité
d’installation. Changer de nom d’hôte, de protocole ou de port ne migre pas les données.

Le navigateur peut aussi séparer le stockage du Runtime intégré à un site
externe de celui de son ouverture directe. Si des projets ou paramètres
chiffrés manquent dans le panneau, utilisez **Ouvrir séparément** à l’adresse
précédente et exportez-les ; l’intégration ne déplace ni ne supprime ces données.
[Référence sur le partitionnement du stockage](https://privacysandbox.google.com/cookies/storage-partitioning).

## Installation HACS

1. Ouvrez HACS et ses dépôts personnalisés.
2. Ajoutez `https://github.com/rockbaer2007/atlas` avec le type **Intégration**.
3. Téléchargez **ATLAS Runtime** et redémarrez Home Assistant.
4. Ouvrez **Paramètres → Appareils et services → Ajouter une intégration → ATLAS Runtime**.
5. Saisissez l’adresse de base actuelle accessible au navigateur, par exemple
   `http://atlas-server:4176/` ou `https://atlas.example.org/atlas/`.

L’intégration ne demande ni jeton HA ni clé de fournisseur. La connexion HA
reste configurée dans l’Administration ATLAS. Le panneau ne transmet ni
authentification HA ni données d’entités à la fenêtre intégrée. Les mises à jour
ordinaires des états HA ne la rechargent pas.

Il s’agit d’un dépôt HACS personnalisé ; aucune inclusion au catalogue général
HACS n’est annoncée. Choisissez **Intégration**, pas Dashboard. Les packages
de cartes HACS exportés restent un processus distinct.

### HACS affiche « Unknown error »

Consultez l’entrée correspondante dans **Paramètres → Système → Journaux**.
Lors du premier téléchargement sur Proxmox, `hacs_repository_download` a signalé
`AttributeError: 'NoneType' object has no attribute 'data'` : HACS ne retrouvait
pas son entrée de dépôt, avant même le téléchargement du package. Rechargez
la page HACS, ouvrez à nouveau **ATLAS Runtime** et relancez le téléchargement.
Dans le cas vérifié, le statut est ensuite passé à **Redémarrage en attente**.
Cela confirme le téléchargement ; la configuration après le redémarrage HA
reste une étape distincte. Les autres causes de « Unknown error » nécessitent
leur entrée de journal correspondante.

## Gestion partagée des plugins depuis 0.1.300

L’application/Ingress et le Runtime peuvent conserver dépôts, métadonnées des
plugins importés et états d’activation sur le même serveur ATLAS. Mettez d’abord
**l’application/le Runtime ATLAS** à jour vers 0.1.300 ; une mise à jour HACS
seule ne suffit pas.

1. Ouvrez l’**accès habituel de l’application ATLAS**, contenant tous vos plugins.
2. Ouvrez Administration → Gestionnaire de plugins → **Gestion partagée des plugins**.
3. Choisissez **Reprendre l’état local** et vérifiez les nombres de dépôts,
   plugins, activations et les conflits affichés.
4. Les conflits conservent les valeurs du serveur par défaut. Choisissez l’état
   local uniquement si vous souhaitez reprendre ses valeurs.
5. Cliquez sur **Sauvegarder et reprendre**. Un téléchargement sauvegarde les
   métadonnées ; le serveur sauvegarde aussi son état précédent et les données
   reçues avant l’enregistrement atomique.
6. Rouvrez le Runtime ou utilisez **Charger l’état serveur**. Les modifications
   suivantes sont partagées ; les Administrations ouvertes vérifient l’état toutes
   les 15 secondes. Une écriture concurrente avec une ancienne révision est refusée.

Une reprise vide ne supprime aucune entrée du serveur. La gestion locale reste
valide jusqu’à la première reprise confirmée, qui ne supprime pas les anciennes
données du navigateur. Les modifications non enregistrées disposent d’une copie
locale de récupération et peuvent être vérifiées à nouveau. **Vérifier une sauvegarde**
affiche l’aperçu d’un export de métadonnées ou d’un instantané serveur ; la reprise
fusionne les entrées.

L’état se trouve dans `ATLAS_PLUGIN_DATA_ROOT/.management/state.json`, les
sauvegardes dans `.management/backups/`. L’application/add-on et Docker utilisent
le répertoire persistant des plugins. Incluez-le dans les sauvegardes du Runtime.
Aucun package n’est installé ou supprimé automatiquement. Jetons HA, clés de
fournisseurs, permissions de fichiers, projets Editor et paramètres propres
aux plugins externes restent hors de cette reprise.

## Projets Editor partagés depuis 0.1.301

Mettez l’application/le Runtime ATLAS à jour vers **0.1.301**. Ouvrez l’éditeur
habituel de l’application avec votre projet. Dans **Projets Editor partagés**,
choisissez **Nouveau projet serveur → Vérifier et enregistrer**, vérifiez nom
et nombre de champs, puis **Sauvegarder et reprendre**. Choisissez à nouveau
**Nouveau projet serveur** pour un autre projet local. Les noms identiques sont
acceptés et ne remplacent jamais automatiquement un autre projet.

Dans le Runtime : **Charger les projets**, sélectionner, **Vérifier l’ouverture**,
vérifier l’aperçu et **Sauvegarder et reprendre**. Champs Expert et configurations
des cartes, noms du projet/script, taille de surface et de grille sont conservés.
Enregistrez explicitement les modifications avec **Vérifier et enregistrer**.
Les révisions détectent les modifications concurrentes du même projet. Un autre
navigateur ne remplace jamais automatiquement votre espace de travail.

Avant ouverture/enregistrement, l’espace de travail est sauvegardé sous
`ATLAS_PLUGIN_DATA_ROOT/.projects/workspaces/` et téléchargé. Les anciens états
serveur sont dans `.projects/backups/`, les projets dans `.projects/projects.json`.
Sauvegardez le répertoire persistant des plugins. **Vérifier une sauvegarde**
prévisualise un téléchargement de sauvegarde. **Vérifier le brouillon local**
récupère un travail partagé non enregistré dans ce navigateur ; après rechargement,
il n’est pas ouvert automatiquement.

Le projet local d’origine reste dans son stockage navigateur. Le travail partagé
utilise un brouillon distinct. Paramètres, identifiants HA, gestion des plugins,
favoris de palette et projets des plugins externes ne sont pas transférés. Un
fichier serveur endommagé n’est jamais remplacé. Limites : 100 projets, 4 MiB
par projet et 64 MiB pour le fichier de stockage.

## Installation manuelle et mises à jour

Copiez uniquement `custom_components/atlas_frontend` depuis le dépôt vers
`/config/custom_components/atlas_frontend`. Sauvegardez un dossier existant avant
de le remplacer et conservez les autres composants. Redémarrez HA et ajoutez
l’intégration comme indiqué. `manifest.json` contient la version.

Pour une mise à jour HACS, actualisez cette intégration et redémarrez HA.
L’adresse du Runtime reste dans l’entrée de configuration HA. Actualisez le
serveur ATLAS séparément par son mode de déploiement existant. **Configurer**
permet de changer l’adresse ; exportez les données ATLAS avant un changement
volontaire. Retirer l’intégration supprime son propre accès au panneau,
pas le Runtime ATLAS, ses plugins ou ses projets.

Depuis l’intégration **0.1.306**, les vérifications de migration refusent les
formats de configuration inconnus sans réécrire l’entrée. Le format existant
**1.1** reste inchangé ; la version du paquet est indépendante du format.
Le retour à une intégration antérieure est vérifié uniquement avec un format
compatible. Sauvegardez la configuration HA et les données ATLAS avant la mise
à jour ; un futur changement de format exige la sauvegarde correspondante pour
la restauration. Une adresse Runtime enregistrée invalide produit une erreur
de configuration et peut être corrigée via **Configurer**.

## HTTP, HTTPS et intégration dans la page

HA en HTTPS nécessite un Runtime HTTPS pour l’intégration. Une cible HTTP
affiche une indication et **Ouvrir séparément**. L’adresse de base ne doit
contenir ni identifiants, ni paramètres de requête, ni fragment. Le port 80
est accepté et les préfixes de proxy inverse sont conservés.

Le proxy inverse doit transmettre correctement les sous-chemins ATLAS et
autoriser l’intégration depuis l’origine HA. Si la vue reste vide, vérifiez
**Ouvrir séparément**, l’accès réseau, le routage du proxy et les en-têtes de
protection des frames. La découverte automatique ou le stockage permanent
d’une adresse de session Ingress ne fait pas partie de cette intégration ;
utilisez toujours l’accès Ingress existant de l’add-on.

La restriction administrateur du panneau HA ne protège pas l’accès direct
au serveur ATLAS externe. Conservez ses restrictions d’accès existantes.
Le panneau utilise `atlas-runtime` et ne remplace aucune autre entrée latérale.
Son module est fourni sous `/atlas_frontend/frontend/atlas-homeassistant-panel.js` ;
ce n’est pas une ressource Lovelace supplémentaire sous `/hacsfiles/atlas/`.

## Périmètre vérifié

Les vérifications isolées utilisent Home Assistant Core **2026.10.1**, un Runtime
ATLAS séparé et des données de test. Elles couvrent configuration/options,
panneau administrateur, rechargement, redémarrage, module statique et conservation
des autres panneaux. Installation HACS et affichage intégré sont vérifiés sur
Proxmox/x86_64 et Pi 5/ARM64. Le cycle isolé **0.1.301 → 0.1.306**, retour à
0.1.301 puis nouvelle mise à jour conserve l’entrée et les autres panneaux après
de vrais redémarrages HA. Un format de test inconnu est refusé sans modifier
l’entrée. Sur Pi 5 et Proxmox, mise à jour HACS vers 0.1.306, redémarrage HA,
panneau, entités en direct et conservation des données sont vérifiés.
L’App ATLAS séparée reste en 0.1.305 pendant cette vérification de l’intégration.

La version stable supplémentaire **2026.9.4** est vérifiée avec l’intégration et
le Runtime **0.1.306** dans une installation amd64 isolée et neuve :
configuration/options, rechargement de l’intégration, redémarrage complet de HA,
Hub, Administration et Editor intégrés, détection authentifiée de la version
et sélection d’entités en direct. L’entrée, les autres panneaux, le projet de
test, les données du plugin et le fichier de configuration sont conservés.
Pi 5 et Proxmox restent inchangés pour cette vérification supplémentaire.
Téléchargement HACS, Supervisor, ARM64 et retour à une ancienne intégration
n’ont pas été revérifiés sous 2026.9.4.

La matrice CI vérifie onze contrats d’intégration avec **2026.9.4** et
**2026.10.1**. Cela ne remplace pas les tests séparés avec HA en fonctionnement
et ne valide pas toutes les versions intermédiaires. Les autres versions HA et
les conversions réelles entre formats de données restent à qualifier séparément.

Références : [panneaux personnalisés HA](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
et [structure des intégrations HACS](https://www.hacs.xyz/docs/publish/integration/).
