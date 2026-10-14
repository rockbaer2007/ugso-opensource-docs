# ATLAS dans le frontend Home Assistant

Depuis **0.1.299**, ATLAS fournit l’intégration facultative **ATLAS Runtime**.
Elle enregistre son propre panneau latéral réservé aux administrateurs HA.
Il ouvre le Hub des plugins, Card Editor Expert et l’Administration du Runtime
existant. Le panneau suit la langue HA DE/EN/FR et le thème clair ou sombre.

## Prérequis et préservation des données

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
des autres panneaux. Le téléchargement HACS de **0.1.299** sur Proxmox est
confirmé jusqu’au statut **Redémarrage en attente**. Configuration et intégration
sur ce système, mises à jour, autres versions HA et installation HACS native
sur ARM64/Pi restent à qualifier séparément.

Références : [panneaux personnalisés HA](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
et [structure des intégrations HACS](https://www.hacs.xyz/docs/publish/integration/).
