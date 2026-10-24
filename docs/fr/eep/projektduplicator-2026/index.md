---
title: Projektduplicator 2026
description: Dupliquer et modifier des projets de modèles EEP avec interface multilingue, sauvegardes ZIP et mises à jour GitHub manuelles.
---

# Projektduplicator 2026

Projektduplicator 2026 est l’outil Windows indépendant d’UGSo Software pour dupliquer et modifier des projets de modèles EEP. L’interface est disponible en allemand, anglais, français et néerlandais.

## Téléchargement et démarrage

- [Télécharger le ZIP Windows 4.6.6.59](https://github.com/rockbaer2007/projektduplicator-2026/releases/download/v4.6.6.59/Projektduplicator-2026-v4.6.6.59-windows.zip)
- [Version, empreinte SHA-256 et sources](https://github.com/rockbaer2007/projektduplicator-2026/releases/tag/v4.6.6.59)
- [Dépôt GitHub](https://github.com/rockbaer2007/projektduplicator-2026)

Extraire tout le ZIP dans un dossier accessible en écriture et lancer `Projektduplicator_2017.exe`. Ce nom technique est conservé pour assurer la compatibilité des paramètres existants. Windows avec .NET Framework 4.8 est nécessaire ; la solution se compile dans Visual Studio 2026.

## Fonctions

- Dupliquer des projets de modèles EEP et modifier les informations des modèles.
- Modifier les noms et descriptions multilingues et les traduire avec Google Translate.
- Changer la langue de l’interface pendant l’utilisation.
- Créer des instantanés ZIP des projets dans le dossier de sauvegarde configuré.
- Rechercher manuellement des versions GitHub avec les boutons de mise à jour, les télécharger et les installer après confirmation.

La traduction Web Google nécessite Internet et dépend du format des réponses du site Google. Elle n’utilise pas d’API officielle de Google. En cas d’échec, les textes existants sont conservés.

## Paramètres et mises à jour

Sauvegarder les projets avant toute modification. Fermer les éditeurs et enregistrer les listes de chemins et de splines avant une mise à jour. Aucune recherche automatique de mise à jour n’a lieu au démarrage.

Le programme de mise à jour vérifie le paquet et son empreinte SHA-256, sauvegarde les fichiers du programme et les paramètres existants, puis redémarre après une installation réussie. Projets, listes de chemins et contenu personnalisé d’`info.txt` sont conservés. Si `info.txt` manque, la copie fournie est installée ; une copie ancienne existante n’est volontairement pas remplacée automatiquement.

## Version vérifiée

La version 4.6.6.59 a été approuvée par l’utilisateur après contrôle local. Le concepteur Form1 a été vérifié dans Visual Studio. La description et les remerciements d’`info.txt` ont été révisés en DE/EN/FR/NL. Les 49 vérifications locales ont réussi : langues, correspondance des champs, validation du paquet, conservation des données, annulation, restauration et transfert entre processus.

Un test réel de mise à jour depuis la version GitHub publique, avec installation et redémarrage, reste à effectuer séparément. Les vérifications actuelles utilisent des réponses GitHub simulées et des installations temporaires.

## Sources et mentions

Le code UGSo est sous licence MIT ; les dépendances conservent leurs licences et copyrights respectifs. Voir `LICENSE` et `THIRD-PARTY-NOTICES.md` dans le dépôt. EEP et Google Translate appartiennent à leurs titulaires respectifs.
