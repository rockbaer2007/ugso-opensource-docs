---
title: Linux et systemd
description: Installer, mettre à jour et sauvegarder ATLAS sous Linux.
---

# Linux et systemd

L’installateur Linux, introduit dans ATLAS **0.1.298**, utilise le même serveur
combiné que Docker et l’application HA. Administration et Card Editor fonctionnent
ensemble ; les plugins externes restent installables séparément.
L’intégration frontend native ATLAS HA/HACS est une autre tâche A7.

## Prérequis

- Linux avec systemd actif, Node.js 22 ou ultérieur et accès root pour l’installation.
- Un package Linux correspondant à l’architecture CPU, à libc et à l’ABI Node de la cible.
- Trois ports libres : 4176 pour l’application, 4175 et 4174 pour les interfaces internes.
- Assez d’espace pour deux versions du Runtime au moins et les sauvegardes de données.

La construction prend en charge AMD64 et ARM64 et utilise Debian Bookworm/glibc.
Un package Alpine/musl n’est pas interchangeable. Les autres distributions et
installations Linux ARM64 natives nécessitent une qualification séparée ;
les vérifications HA ARM64 ne la remplacent pas.

L’installateur utilise le compte système `atlas`. Il refuse un compte existant
avec un autre répertoire personnel ou groupe principal et ne reprend pas
silencieusement une autre installation ATLAS.

## Préparer un package

Sur un hôte Linux avec les dépendances de construction habituelles :

```sh
corepack enable
pnpm install --frozen-lockfile
pnpm build
pnpm test:linux
pnpm linux:prepare
```

`output/linux-runtime` contient l’application compilée, les dépendances,
le plugin de référence et `atlas-linux-runtime.json`.
Un répertoire de sortie existant n’est pas écrasé.

Autre méthode, avec Docker hors du LXC cible :

```sh
docker build -f packaging/linux/Dockerfile --target export --output type=local,dest=output/linux-export .
```

L’export comprend une archive, un manifeste, des sommes de contrôle et le
binaire Node avec sa licence provenant de l’image officielle Node. Vérifiez
la provenance et les SHA-256 avant utilisation. Utilisez une installation Node
compatible ; ne remplacez pas une version existante sans vérification.
Conservez les liens symboliques relatifs de `node_modules` pendant le transfert.

## Installation

Avec un package vérifié et extrait et une version Node compatible :

```sh
sudo node /chemin/linux-runtime/scripts/atlas-linux-installer.mjs install --source /chemin/linux-runtime
sudo systemctl status atlas
curl --fail http://127.0.0.1:4176/health
```

L’installateur valide le package, l’architecture et les modules natifs,
crée une sauvegarde, installe une version séparée et démarre le service.
La vérification exige les deux interfaces, la version attendue et la cible
de distribution Linux. Aucun service tiers n’est arrêté pour libérer un port occupé.

## Données persistantes

| Chemin | Contenu |
| --- | --- |
| `/opt/atlas/releases/` | Versions du Runtime séparées. |
| `/opt/atlas/current` | Lien symbolique vers la version actuelle. |
| `/opt/atlas/installation.json` | État de l’installation et version précédente. |
| `/var/lib/atlas/` | Données, plugins, identité, historique de fichiers et corbeille. |
| `/etc/atlas/atlas.env` | Configuration protégée, conservée lors des mises à jour. |
| `/etc/systemd/system/atlas.service` | Service géré. |
| `/etc/systemd/system/atlas.service.d/` | Compléments systemd locaux. |
| `/var/backups/atlas/` | Sauvegardes horodatées. |

Les projets de l’éditeur et une partie de l’Administration résident dans le
navigateur. Exportez-les séparément depuis leurs interfaces : une sauvegarde
serveur ne capture pas le stockage du navigateur. Conservez l’adresse du
navigateur, le chemin des données et l’identité de l’installation lors des
mises à jour pour préserver les identifiants chiffrés liés localement.
Les données Docker/HA ne sont pas migrées silencieusement.

## Mise à jour et retour à la version précédente

```sh
sudo node /chemin/nouveau-package/scripts/atlas-linux-installer.mjs update --source /chemin/nouveau-package
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs rollback
```

ATLAS est arrêté et sauvegardé avant la mise à jour. Le fichier d’environnement,
les plugins installés et les compléments systemd sont conservés.
Le lien actuel change de Runtime. En cas d’échec, le Runtime précédent est
rétabli. Une installation précédemment arrêtée reste arrêtée après vérification ;
l’activation au démarrage est conservée.

Le retour change le programme, pas les données utilisateur. De futures migrations
de données nécessitent une vérification de rétrocompatibilité distincte.
Les anciennes versions et sauvegardes ne sont pas supprimées automatiquement.
Utilisez `systemctl edit atlas` pour vos compléments au lieu de modifier directement
le service géré.

## Sauvegarde et restauration

```sh
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs backup
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs status
```

La sauvegarde à service arrêté comprend données, configuration, service,
compléments et manifeste d’installation. Un service auparavant actif redémarre
ensuite. Les sauvegardes sont réservées à root et peuvent contenir des identifiants.
Sauvegardez séparément les chemins externes, clés SSH hors des données ATLAS
et projets du navigateur.

Pour restaurer manuellement, arrêtez ATLAS, sauvegardez à nouveau l’état actuel
et restaurez les données/configurations sélectionnées aux chemins d’origine
avec les propriétaires appropriés. Conservez l’identité de l’installation,
préparez le Runtime correspondant puis vérifiez `/health`. Copier la sauvegarde
sur une autre installation ne déverrouille pas ses secrets locaux.
Un snapshot VM/LXC avant installation permet aussi de restaurer l’hôte entier.

## Réseau et plugins

Toutes les interfaces utilisent loopback par défaut ; Terminal est désactivé.
L’installateur n’ouvre aucun pare-feu. L’administrateur peut modifier délibérément
`ATLAS_APP_HOST` pour le LAN et limiter cet accès ; les ports internes restent
locaux. L’Administration ne doit pas être exposée sans protection sur Internet.

File Studio nécessite des permissions Linux correspondant aux chemins approuvés.
Les fichiers HA situés sur un autre hôte ne sont pas montés automatiquement.
SSH et Oh My Posh pour le Terminal externe sont des prérequis supplémentaires
facultatifs, non inclus dans le package Linux.

## Périmètre des tests

Les régressions utilisent des données temporaires pour vérifier conservation,
sauvegarde, échec de mise à jour, retour de version, état du service,
installation sans écrasement et validation des chemins/ABI.
Un test conteneur avec service simulé ne remplace pas un test systemd natif.
Les preuves natives et plateformes ouvertes figurent dans
l’[état du développement](/fr/projects/atlas/development-status).
