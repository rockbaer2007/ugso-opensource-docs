---
title: INI Edit Translate 2026
description: Fonctions de l’éditeur Windows de fichiers INI de modèles EEP et d’Installation.eep avec traduction ChatGPT.
---

# INI Edit Translate 2026

**Version 2.1.37.0 · Windows 11 · .NET Framework 4.8**

Modifier les descriptions de modèles EEP et leurs fichiers d’installation. Développé
par Uwe Grimm / UGSo Software et publié sous licence MIT.

[Code source et README sur GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Interface de la version 2.1.37 avec barre de menus Lime, sans données personnelles](/eep/ini-edit-translate-2026/editor-v2-1-37-fr.png)

## Téléchargement

[Télécharger le ZIP Windows v2.1.37](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/download/v2.1.37/INI-Edit-Translate-2026-v2.1.37-windows.zip) · [Version GitHub et SHA-256](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/tag/v2.1.37)

Extraire tout le ZIP et lancer `INI Edit Translate 2026.exe`. Windows 11 et
.NET Framework 4.8 sont requis. Conserver les DLL et dossiers de langues ensemble.
Visual Studio sert uniquement à compiler les sources. Aucun installateur nécessaire.

## Fonctions

| Domaine | Possibilités |
| --- | --- |
| Textes de modèles | Modifier les noms et descriptions en EN/DE/FR/PL |
| Métadonnées | Modifier les références PDF, génération, années d’utilisation, pays et icône |
| Axes de mouvement et fonctions des signaux | Afficher, modifier et traduire les entrées par langue |
| Installation.eep | Modifier les noms et descriptions des sections d’installation prises en charge |
| Aperçu | Comparer le fichier original à l’aperçu du résultat |
| Export des tableaux | Export complet en UTF-8 avec BOM et séparateurs de tabulation |
| Sauvegardes | Copier les fichiers INI existants avant remplacement, en conservant leur nom d’origine |

## Traduction ChatGPT

L’application utilise uniquement l’API OpenAI Responses. Chaque texte source est
traduit vers les trois autres langues dans une seule requête, sans passer par une
traduction intermédiaire anglaise. Un cache temporaire évite les répétitions au sein
d’une même opération.

La fenêtre de progression propose **Annuler**. Le délai est de 60 secondes et la limite
de 24 000 caractères par texte. Les réponses incomplètes, langues manquantes et espaces
réservés modifiés, tels que `{0}`, `%s` ou `[e]`, sont rejetés. Les textes et tableaux
existants sont conservés en cas d’échec.

Les textes DE/EN/FR ont été révisés : caractères endommagés, mauvaises langues et
messages mélangés. Les clés INI techniques telles que `Name_GER` sont conservées.

## Installation et utilisation

1. Télécharger le ZIP Windows ci-dessus et extraire tous les fichiers.
2. Lancer `INI Edit Translate 2026.exe` depuis le dossier extrait en conservant ses DLL et dossiers de langues.
3. Ouvrir **À propos → Paramètres → Traduction OpenAI** et saisir sa propre clé API et le modèle ; `gpt-4.1-mini` par défaut.
4. Ouvrir d’abord une copie sauvegardée en mode **Lecture seule**.
5. Utiliser **Lire et traduire** ou un bouton de traduction. Choisir la langue source des axes et fonctions des signaux.
6. Vérifier l’aperçu et les textes, puis enregistrer explicitement.

La fenêtre d’information choisit l’aide révisée `Info.de.rtf`, `Info.en.rtf` ou `Info.fr.rtf` selon la langue de l’interface. Le fichier historique `Info.rtf` est conservé sans modification. L’aide actuelle décrit OpenAI et le programme de référence restauré.

## Mises à jour GitHub

Choisir **À propos → Rechercher des mises à jour** pour consulter la dernière version
publique sur GitHub. Aucune vérification automatique au démarrage. Seule une version
stable plus récente est proposée, avec son numéro et ses notes de publication.

**Télécharger et installer** récupère le ZIP Windows et sa somme SHA-256.
Le téléchargement et la vérification peuvent être annulés avant la fermeture du programme.
Enregistrer les fichiers ouverts et fermer Info_trans avant l’installation, puis confirmer.
Un programme auxiliaire attend la fermeture de l’éditeur, sauvegarde les fichiers existants
et installe le paquet.

Les paramètres et la clé OpenAI chiffrée sont conservés. Les fichiers FDB, CSV, DAT et
de configuration existants de l’aide, ainsi que l’Info.rtf d’origine, sont sauvegardés
sans être remplacés. Les fichiers de modèles restent intacts. En cas d’échec, le programme
tente de restaurer les fichiers déjà remplacés et consigne le résultat. Sauvegardes et
rapports : `%LOCALAPPDATA%/UGSo/IET2026/updates/<identifiant>/`.

Aucun identifiant de serveur nécessaire. Les sommes de contrôle vérifient l’intégrité ;
aucune signature numérique de paquet supplémentaire n’est implémentée.
32 tests isolés couvrent le téléchargement, l’annulation, les chemins, la conservation
des données, les fichiers verrouillés et la restauration après une écriture partielle.

## Second programme : Info_trans

Le paquet contient aussi `help/Info_trans.exe`. **Aide de référence** dans
l’éditeur ouvre ce programme dans la langue choisie. La véritable `IET2.FDB`
et son moteur natif Firebird 2.5.8 ont été récupérés dans l’archive de 2019.
Aucune installation séparée d’un serveur Firebird n’est nécessaire.

La base contient 5 entrées de bâtiments, 2 de marchandises et 2 de mises à jour.
Les tables des signaux, matériel roulant, objets de voie et paysage sont vides
dans l’original. Sont aussi inclus : 236 entrées d’icônes, 369 termes techniques
et 2 428 entrées corrigées dans le **dictionnaire DE/EN/FR**. L'anglais est la
référence ; les corrections allemandes confirmées et les traductions françaises
sont intégrées. Les fragments ont été réunis et les termes mélangés séparés.
Les variantes américaines et britanniques conservent leurs indications.
Toutes les questions de vérification du dictionnaire sont résolues. Le fichier
DE/EN original et la base source restent inchangés dans le paquet complet.

![Info_trans 2.1.37 avec onglets Lime et base d'origine chargée](/eep/ini-edit-translate-2026/info-trans-v2-1-37-fr.png)

![Dictionnaire trilingue Info_trans avec colonnes allemandes, anglaises et françaises lisibles](/eep/ini-edit-translate-2026/dictionary-v2-1-37-fr.png)

`Info_trans` est compilé pour x86, comme les DLL natives. Le fournisseur géré
FirebirdSql.Data.FirebirdClient 7.5.0.0 a été vérifié avec la vraie base Firebird 2.5.8.
Les tests lisent des copies séparées et comparent les sept tables avec l’interface
DE/EN/FR. Le paquet contient la base source inchangée.

Les composants absents ou illisibles sont signalés ; l’import SQL est alors
désactivé. Une sauvegarde locale précède tout import SQL manuel disponible.
La mise à jour automatique du programme reste désactivée.

## Données et confidentialité

Les anciennes inscriptions et bases personnelles ne sont pas importées. Les paramètres
sont séparés par utilisateur Windows. La configuration OpenAI et les sauvegardes sont
conservées sous `%LOCALAPPDATA%/UGSo/IET2026/`.

Windows DPAPI chiffre la clé API pour le compte Windows actuel. Les textes sélectionnés
sont envoyés à OpenAI avec `store: false`. Internet et une facturation API distincte sont
nécessaires ; un abonnement ChatGPT ne remplace pas cette facturation.

## Mise à jour et vérifications

**Les mises à jour GitHub sont lancées manuellement et leur installation doit être confirmée.** L’ancien serveur n’est pas utilisé. Google, LEO, Linguee et DeepL ne sont plus proposés.

41 contrôles locaux avec réponses API simulées et les compilations Debug/Release
vérifient les erreurs, l’annulation, la restauration, l’export et les interfaces rendues
DE/EN/FR. Aucun texte n’est envoyé à OpenAI pendant les tests. Un appel API réel et la
qualité des traductions produites restent à vérifier avec son propre compte.
Tous les schémas INI possibles ne sont pas pris en charge ; vérifier les données obtenues.

Le paquet local complet 2.1.37 a été contrôlé par l'utilisateur, qui a confirmé son
bon fonctionnement avant publication. Le ZIP contient les deux programmes, le
moteur Firebird natif, la base originale et le dictionnaire corrigé. L'intégrité
du ZIP et son SHA-256 ont été vérifiés ; les sept tables de la base ont été
comparées aux interfaces DE/EN/FR sur des copies séparées. Les captures montrent
le nouveau design avec des données neutres, sans paramètres privés.
