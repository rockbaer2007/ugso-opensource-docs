---
title: Home Assistant Automation Exporter
description: Documentation en français concernant un outil Windows permettant d'exporter des automatisations Home Assistant individuelles depuis le fichier
  `automations.yaml`.
---
<a id="orientation-actuelle"></a>

# Home Assistant Automation Exporter {#home-assistant-automation-exporter}

**Home Assistant Automation Exporter** est un outil portable pour Windows qui permet de charger un fichier Home Assistant `automations.yaml` et d'en exporter le contenu sous forme de fichiers YAML individuels.

Cela s'avère utile si vous souhaitez sauvegarder des automatisations séparément, les partager, les documenter ou les réimporter individuellement dans Home Assistant ultérieurement.

![Home Assistant Automation Exporter](/images/ha-automation-exporter/automations-exporter.png)

## Projet {#projekt}

| Élément | Lien |
| --- | --- |
| Dépôt GitHub | [rockbaer2007/ha-automation-exporter](https://github.com/rockbaer2007/ha-automation-exporter) |
| Version actuelle | [Télécharger la v0.3.4](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.4) |
| Plateforme | Windows |
| Base | C# / .NET 9 |

## Fonctionnalités {#funktionen}

- Interface graphique Windows (sans ligne de commande).
- Affichage de la version du programme dans le titre de la fenêtre.
- Chargement d'un fichier Home Assistant `automations.yaml`.
- Recherche d'automatisations par alias, ID, nom de fichier ou contenu YAML.
- Affichage de toutes les automatisations dans un tableau avec cases à cocher.
- Accès à des vues détaillées incluant les entités détectées et le code YAML complet.
- Exportation des automatisations sélectionnées sous forme de fichiers individuels `.yaml`.
- Ouverture directe du dossier d'exportation dans l'Explorateur Windows. - Enregistre les paramètres de manière portable, à côté du fichier EXE, dans `HaAutomationExporter.settings.json`.

## Exigences {#voraussetzungen}

Pour une utilisation en tant que version finale (release) :

- Windows
- Téléchargement du fichier de la version actuelle depuis GitHub

Pour le développement ou l'exécution à partir du code source :

- Windows
- .NET 9 SDK
- Dépôt cloné localement

```powershell
dotnet run --project .\HaAutomationExporter.csproj
```

## Utilisation {#bedienung}

1. Lancer le programme.
2. Sélectionner le fichier Home Assistant `automations.yaml`.
3. Modifier éventuellement le dossier d'exportation dans les paramètres.
4. Sélectionner les automatisations dans le tableau.
5. Vérifier des automatisations individuelles via `Details`.
6. Exporter les automatisations sélectionnées.
7. Importer les fichiers YAML générés dans Home Assistant, si nécessaire.

## Vue détaillée {#detailansicht}

La vue détaillée permet de vérifier une automatisation avant son exportation. Cela s'avère particulièrement utile lorsque de nombreuses automatisations portent des noms similaires, ou lorsqu'il est nécessaire de contrôler des modèles (templates) et des entités.

![Détails de l'automatisation : Entités](/images/ha-automation-exporter/details-entities.png)

L'onglet **Entités** affiche les entités Home Assistant détectées, en précisant leur source, le numéro de ligne et le contexte. Les éléments détectés au sein de modèles (templates) sont identifiés par une approche heuristique.

![Détails de l'automatisation : YAML](/images/ha-automation-exporter/details-yaml.png)

L'onglet **YAML** affiche le code complet de l'automatisation et propose une fonction de copie.

## Exportation pour Home Assistant {#export-fur-home-assistant}

Les fichiers exportés sont préparés de manière à faciliter leur utilisation individuelle dans Home Assistant.

L'outil d'exportation supprime la ligne initiale `id:` et normalise les différentes syntaxes YAML :

| Source | Exportation |
| --- | --- |
| `triggers` | `trigger` |
| `conditions` | `condition` |
| `actions` | `action` |
| `- trigger: ...` | `- platform: ...` |
| Actions de service | `- service: domain.service` |

Cela permet d'exporter de manière plus uniforme les automatisations provenant de différentes versions de Home Assistant, d'exemples sur GitHub ou de messages sur des forums.

## Langues {#sprachen}

L'interface prend en charge :

- Système
- Allemand
- Anglais
- Français
- Espagnol
- Polonais
- Russe

L'option `System` détecte la langue du système Windows pour `de`, `en`, `fr`, `es`, `pl` et `ru`. Si une langue système n'est pas prise en charge, l'application bascule sur l'anglais.

## Ligne de commande {#kommandozeile}

Le projet est conçu comme une application Windows, ce qui lui permet de démarrer sans fenêtre de console. En interne, il reste toutefois possible de traiter des arguments.

```powershell
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export pool
```

L'interface graphique est prévue pour une utilisation courante.

## Remarques {#hinweise}

- Avant toute importation dans Home Assistant, il est conseillé de vérifier brièvement chaque automatisation exportée.
- Les automatisations contenant des modèles (templates) complexes peuvent nécessiter une vérification manuelle.
- Le fichier source `automations.yaml` est uniquement lu et n'est pas modifié.
- Le dossier d'exportation doit être situé en dehors de la configuration de production de Home Assistant, tant que les fichiers n'ont pas été vérifiés.
