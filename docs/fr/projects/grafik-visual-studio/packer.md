---
title: Outil de création (packer) pour les paquets de widgets et d'outils
description: Vérification des paquets pour « HA Grafik Visual Studio » et création de fichiers au format .wg ou .tp.
---

# Outil de création (packer) pour les paquets de widgets et d'outils {#packer-fur-widget-und-tool-pakete}

Les paquets et outils complémentaires sont proposés de manière centralisée sur [visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=de). Ce site open source contient des descriptions et des instructions ; le téléchargement s'effectue via le catalogue de paquets.

L'outil d'empaquetage (« Packer ») crée, à partir d'un dossier source, un paquet de widgets (`.wg`) ou un paquet d'outils (`.tp`) pour HA Grafik Visual Studio. Ces deux fichiers sont des archives ZIP dotées d'une extension spécifique. Avant l'exportation, l'outil vérifie le manifeste, la structure du paquet, les images SVG/PNG référencées ainsi que les contraintes définies par l'interface des paquets de widgets (./widget-pakete) ou l'interface des paquets d'outils (./tool-pakete). Dans la version actuelle de l'interface (0.1), les fichiers de paquet ne contiennent aucun code exécutable.

## Création d'un paquet {#paket-erstellen}

1. Placez le fichier `manifest.json` dans le répertoire racine d'un dossier source. Les images référencées doivent être placées conformément aux spécifications `icons/`. Les pages décrivant ces interfaces présentent les champs requis ainsi que des exemples.
2. Dans l'outil d'empaquetage, sélectionnez **Paquet de widgets** ou **Paquet d'outils**, puis indiquez le dossier source et un dossier d'exportation existant.
3. Vérifiez la liste des résultats ainsi que l'identifiant du paquet, la version, la licence et le nom de destination. L'option **Exporter** ne devient active que si le paquet est valide et si le nom de destination est disponible. L'outil d'empaquetage ne remplace aucun fichier existant.
4. Installez le fichier généré (`.wg` ou `.tp`) dans le Studio via **Paramètres → Paquets de widgets** ou **Paramètres → Outils**. Les anciennes extensions `.wg.zip` et `.tp.zip` restent utilisables.

L'outil d'empaquetage effectue ses vérifications en appliquant les mêmes règles que l'outil d'importation intégré au Studio. Le paquet 0.3.0 prend en charge jusqu'à 64 widgets par paquet ; Un paquet d'outils contient exactement un outil dans l'interface 0.1. Le Studio effectue en outre sa propre vérification pour chaque paquet importé.

## GitHub et enregistrement direct {#github-und-direkte-registrierung}

À partir de la version de test **0.3.1**, l'outil de création de paquets (« Packer ») affiche en vert les paquets déjà enregistrés dont le contenu est identique, sous la mention **Fichier enregistré** ; cet état est conservé même après un redémarrage. Une nouvelle exportation reste désactivée. Si le contenu diffère, le mécanisme de vérification empêche toujours l'écrasement du fichier. Le bouton large **GitHub & Catalogue…** se situe juste en dessous de la liste de vérification.

Depuis la version **Packer 0.3.0**, l'option **GitHub & Catalogue…** permet d'ouvrir un paquet `.wg` ou `.tp` exporté, en vue de sa vérification et de sa publication. La version de test **0.3.1** (proposée ci-dessous) intègre cette extension ainsi qu'une correction concernant l'affichage des fichiers enregistrés.

1. Installez la [GitHub CLI](https://cli.github.com/) et connectez-vous via le terminal en utilisant `gh auth login`. Indiquez votre dépôt public et sélectionnez **Charger les versions (Releases)**.
2. Sélectionnez le tag de la version (release tag) et validez en choisissant **Publier le paquet sur GitHub**. Pour une nouvelle version, activez l'option **Créer une version (Release) pour un tag Git existant** ; le tag doit déjà être présent sur GitHub. Les fichiers existants ne seront pas écrasés.
3. Le lien de téléchargement sera récupéré automatiquement. Alternativement, vous pouvez saisir directement un lien HTTPS (déjà publié) correspondant à une version fixe (`.wg` ou `.tp`), ce qui vous permet de sauter l'étape GitHub.
4. Renseignez le lien vers la licence, la description, l'adresse de contact interne ainsi que la version minimale requise du Studio. Indiquez si le paquet contient de nouvelles fonctionnalités en choisissant **Non / Oui / Incertain**. Si vous choisissez « Oui » ou « Incertain », une description est requise ; la version minimale peut, quant à elle, rester inconnue.
5. Consultez les [instructions d'enregistrement](https://visualstudio.ugso-software.de/privacy), confirmez l'acceptation du traitement des données et des droits de distribution, puis sélectionnez **Enregistrer dans le catalogue**. Avant l'envoi, l'outil d'empaquetage (Packer) affiche les destinataires et les informations saisies. Le paquet original est transmis pour une analyse automatique.
6. Une fois la soumission effectuée avec succès, copiez le lien de gestion privé. Le paquet apparaîtra dans le catalogue après une vérification manuelle et une validation. En cas de réponse réseau ambiguë, vérifiez d'abord si la version a bien été enregistrée ; l'outil ne relance pas automatiquement la soumission.

L'adresse de contact est transmise en interne au catalogue et, le cas échéant, à sa boîte de réception dédiée aux vérifications. Le nom, l'adresse e-mail et le site web ne sont pas rendus publics. L'outil d'empaquetage conserve uniquement le dépôt et le lien vers la licence (par souci de commodité) ; il ne stocke ni l'adresse de contact, ni les jetons GitHub, ni les consentements, ni les liens de gestion. Les opérations réseau s'exécutent en arrière-plan. Les dossiers sources des widgets peuvent également contenir `LICENSE.txt` et `README.md`.

## Programme et extensions de fichiers {#programm-und-dateiendungen}

L'interface Qt fonctionne sous Windows et Linux. Le bouton **Enregistrer les extensions** affiche d'abord un aperçu ; après confirmation, il configure des icônes spécifiques ainsi que des entrées « Ouvrir avec » pour `.wg` et `.tp` pour l'utilisateur actuel. L'application par défaut existante n'est pas modifiée. L'outil d'empaquetage permet d'ouvrir un paquet existant pour vérification, sans l'installer. Si le programme est déplacé, l'enregistrement des types de fichiers doit être effectué à nouveau.

La version **0.3.1** est disponible en tant que version de test signée pour Windows et Linux dans le [catalogue de paquets](https://visualstudio.ugso-software.de/?kind=helper&lang=de) :

| Système | Téléchargement | SHA-256 |
| --- | --- | --- |
| Windows x86_64 | [Télécharger le ZIP](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.3.1-windows-x86_64.zip) | `7047e6ee5bb2327cf80432d2c37e0f82516284c22c0d4910ff3d4d64950efd8a` |
| Linux x86_64 | [Télécharger le TAR.GZ](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.3.1-linux-x86_64.tar.gz) | `e094331c7281957764dee38a8a117d932a2589581117daf68f1e146b71fd9a19` |

Décompressez entièrement l'archive et lancez `HA-Grafik-Packer.exe` ou `HA-Grafik-Packer`. Le dossier `_internal` doit rester à côté ; il contient également les bibliothèques Qt, qui peuvent être remplacées séparément. Les deux versions (pour les différentes plateformes) ont été vérifiées au moyen de tests et d'un autotest après décompression. Sous Linux, les bibliothèques système Qt sont requises pour EGL/OpenGL. Les textes de licence et diverses informations sont inclus dans l'archive.

## Vérification du téléchargement {#download-prufen}

Pour la version 0.3.1, téléchargez [SHA256SUMS-0.3.1](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS-0.3.1) et [SHA256SUMS-0.3.1.sig](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS-0.3.1.sig). Le [fichier de confiance pour OpenSSH](https://raw.githubusercontent.com/rockbaer2007/ugso-opensource-docs/main/docs/public/keys/packer-allowed-signers) et la [clé publique de publication](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) sont fournis séparément de la version publiée. L'empreinte Ed25519 est `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`. Les anciens fichiers de sommes de contrôle, dépourvus de numéro de version, correspondent à 0.2.0.

Vérifiez d'abord la signature. Sous Linux, dans le dossier de téléchargement :

```sh
ssh-keygen -Y verify -f packer-allowed-signers -I packer-release -n ha-grafik-visual-studio-packer-release -s SHA256SUMS-0.3.1.sig < SHA256SUMS-0.3.1
sha256sum -c SHA256SUMS-0.3.1
```

Sous Windows, les mêmes paramètres de signature fonctionnent dans `cmd.exe` en utilisant la redirection d'entrée indiquée. Comparez ensuite `certutil -hashfile DATEINAME SHA256` avec la valeur contenue dans `SHA256SUMS-0.3.1`. Avant d'effectuer la vérification, téléchargez la clé et le fichier de confiance depuis les sources indiquées par les liens ci-dessus. Le code source de l'outil de compression demeure dans le dépôt de développement privé.
