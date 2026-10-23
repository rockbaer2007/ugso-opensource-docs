---
title: INI Edit Translate 2026
description: Fonctions de l’éditeur Windows de fichiers INI de modèles EEP et d’Installation.eep avec traduction ChatGPT.
---

# INI Edit Translate 2026

**Version 2.1.35.0 · Windows 11 · .NET Framework 4.8**

Modifier les descriptions de modèles EEP et leurs fichiers d’installation. Développé
par Uwe Grimm / UGSo Software et publié sous licence MIT.

[Code source et README sur GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Interface française vérifiée, sans données personnelles](/eep/ini-edit-translate-2026/editor-fr.png)

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

1. Compiler avec Visual Studio 2026, le développement de bureau .NET et le Developer Pack
   .NET Framework 4.8. Les commandes figurent dans la README.
2. Lancer `INI Edit Translate 2026.exe` depuis Release en conservant ses DLL et dossiers de langues.
3. Ouvrir **À propos → Paramètres → Traduction OpenAI** et saisir sa propre clé API et le modèle ; `gpt-4.1-mini` par défaut.
4. Ouvrir d’abord une copie sauvegardée en mode **Lecture seule**.
5. Utiliser **Lire et traduire** ou un bouton de traduction. Choisir la langue source des axes et fonctions des signaux.
6. Vérifier l’aperçu et les textes, puis enregistrer explicitement.

## Données et confidentialité

Les anciennes inscriptions et bases personnelles ne sont pas importées. Les paramètres
sont séparés par utilisateur Windows. La configuration OpenAI et les sauvegardes sont
conservées sous `%LOCALAPPDATA%/UGSo/IET2026/`.

Windows DPAPI chiffre la clé API pour le compte Windows actuel. Les textes sélectionnés
sont envoyés à OpenAI avec `store: false`. Internet et une facturation API distincte sont
nécessaires ; un abonnement ChatGPT ne remplace pas cette facturation.

## Mise à jour et vérifications

**La mise à jour est entièrement désactivée** : aucune connexion à l’ancien serveur
et aucun menu de mise à jour. Google, LEO, Linguee et DeepL ne sont plus proposés.

30 contrôles locaux avec réponses API simulées et les compilations Debug/Release
vérifient les erreurs, l’annulation, la restauration, l’export et les interfaces rendues
DE/EN/FR. Aucun texte n’est envoyé à OpenAI pendant les tests. Un appel API réel et la
qualité des traductions produites restent à vérifier avec son propre compte.
Tous les schémas INI possibles ne sont pas pris en charge ; vérifier les données obtenues.
