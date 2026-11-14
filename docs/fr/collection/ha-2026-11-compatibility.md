---
title: Vérification de compatibilité HA 2026.11
description: Vérifications confirmées, tests locaux et problèmes ouverts des extensions UGSo sous Home Assistant 2026.11.
---
# Vérification de compatibilité HA 2026.11

**État au 05/11/2026 · Core 2026.11.0 · Frontend 20261028.4 · Système de test système de test ARM (Pi 5) (port 80).**

Cette synthèse distingue les vérifications réelles, les confirmations de l’utilisateur et les tests locaux. Elle ne certifie pas toutes les fonctions ni toutes les variantes matérielles. La vérification initiale n’a modifié aucune version logicielle ; le correctif ultérieur de la barre latérale est documenté séparément ci-dessous.

## ATLAS et plugins

| Paquet | Résultat et périmètre |
| --- | --- |
| App ATLAS **0.1.334**, Card Editor **0.2.0-alpha.115** | En conditions réelles : Ingress, hub avec six plugins actifs, éditeur, connexion HA avec 35 entités réelles et liste des projets existants chargés. Les 431 tests du paquet HA, 74 tests app/frontend et contrôles TypeScript des onze paquets du workspace ont réussi. |
| File Studio **0.1.52** | En conditions réelles : arborescence, interface d’édition et chemins autorisés chargés. Quatre tests de paquet et validation du catalogue réussis. Aucun fichier existant modifié. |
| Automation Exporter / Editor **0.1.28** | En conditions réelles : fichier système des automatisations lu après sa propre sauvegarde ; aucune automatisation préexistante. Neuf tests locaux réussis. Aucune écriture dans les fichiers système HA. |
| Terminal **0.1.10** | Interface vérifiée en conditions réelles. **L’utilisateur confirme le 05/11/2026 : ATLAS Terminal fonctionne.** Cette confirmation complète le contrôle initial de l’interface ; elle ne valide pas séparément toutes les cibles SSH ni tous les thèmes Oh My Posh. |
| Bibliothèque d’icônes **0.1.9** | En conditions réelles : 7 447 icônes MDI (7.4.47) chargées, recherche fonctionnelle. Dix tests et validation du paquet réussis. |
| Icon Studio **0.1.17** | En conditions réelles : collection, aperçu SVG et interface de dessin chargés. Quinze tests et validation du paquet réussis ; collection existante inchangée. |

Le paquet de l’app ATLAS passe aussi la vérification sans écriture de 523 fichiers. Le test Python isolé du contrat de l’intégration HA n’a pas pu être exécuté localement, Home Assistant n’étant pas importable ; Docker n’était pas démarré. Un nouveau cycle complet d’écriture/restauration/HACS des projets ne fait pas partie de cette vérification.

## Autres extensions HA

| Paquet | Résultat et limite |
| --- | --- |
| [Dashboard Layout Card V2 **0.1.181**](/fr/collection/dashboard-layout-card-v2/) | Test réel distinct réussi : ajout/modification de cartes dans la deuxième section, bouton d’ajout flottant, en-tête/pied de page et rechargement complet. |
| [Automation Status Card **0.1.3**](/fr/projects/automation-status-card/) | Tests réels réussis : affichage, activation/désactivation confirmée par HA, exécution en cours, lecture des traces, fin normale, cases à cocher, tout sélectionner/désélectionner et rechargement. Exemples individuels Bubble/Mushroom affichés. Vingt et un tests locaux réussis. Les erreurs et alertes de durée n’ont pas été provoquées à nouveau sous 2026.11. |
| [Sidebar Manager **0.1.9**](/fr/projects/sidebar-manager/) | Mise à jour de 0.1.7 vers **0.1.9** sur le système de test ARM (Pi 5). Tests réels réussis : couleurs du texte/des icônes des entrées et groupes dans le dialogue natif, opacité, annulation, enregistrement, réinitialisation au thème et rechargement complet. Les 72 tests locaux réussissent. Objets de test supprimés ; disposition exportée identique à la sauvegarde initiale. |
| [Sidebar Colors **0.1.1**](/fr/projects/sidebar-colors/) | **0.1.1** corrige le même sélecteur de lignes. Les 27 tests locaux réussissent, y compris les régressions DOM des anciens/nouveaux éléments HA et l’enregistrement/annulation. Aucune installation parallèle supplémentaire sur le système de test ARM (Pi 5). |
| [Gestion des utilisateurs **0.1.11**](/fr/projects/dashboard-user-manager/) | En conditions réelles : 19 vues et quatre utilisateurs chargés, aucune modification enregistrée. **Ouvert : avertissement de chargement supplémentaire pour l’ancien tableau de bord `lovelace`.** Cause non définitivement établie. Trente-trois tests Python et dix-neuf tests Node de l’app réussis. |
| [HA Grafik Visual Studio **0.1.296**](/fr/projects/grafik-visual-studio/) | 109 tests Python et 388 tests Node réussis. Aucun test réel dédié sur le système de test ARM (Pi 5), où l’app n’est pas installée. |
| [Blocks for HA **0.1.66**](/fr/projects/blocks-for-ha/) | Dix tests Python et 172 tests Node réussis ; sept tests facultatifs ignorés. Aucun test réel sur le système de test ARM (Pi 5). |
| [Client MQTT **0.1.17**](/fr/projects/mqtt-client/) | Trente-six tests Python réussis ; deux tests nécessitant un broker MQTT distinct ignorés. Aucun nouveau test réel avec un broker externe. |
| [CallMeBot Whatsapp **0.1.6**](/fr/projects/callmebot/) / [Signal **0.1.2**](/fr/projects/callmebot-signal/) | 17/18 tests Python et trois tests d’identifiant de requête par app réussis. Aucun message envoyé à de vrais destinataires. |
| Tabbed Card V2 / Editor **0.1.7**, intégration HA **0.1.3** | Syntaxe JavaScript/Python vérifiée ; aucune validation réelle de l’extension non installée. |
| [FRITZ!Box to MQTT **0.1.41**](/fr/projects/fritzbox-to-mqtt/) / [Fioul to MQTT **0.1.15**](/fr/projects/heizoel-to-mqtt/) | Syntaxe Python vérifiée ; appareils, source de données et découverte MQTT non testés en conditions réelles. |
| Paquet de widgets Materialdesign / [Ultimate Timer Blueprint](/fr/projects/ultimate-timer/) | Inclus dans l’inventaire ; aucun nouveau test fonctionnel réel complet. |

## Problèmes connus et prochaines vérifications

**Corrigé dans Sidebar Manager 0.1.9 et Sidebar Colors 0.1.1 :** les couleurs prennent en charge l’ancien `ha-md-list-item` et le nouveau `ha-list-item-button`. Manager testé sur le système de test ARM (Pi 5) : couleurs du texte/des icônes des entrées et groupes, opacité, annulation, enregistrement, réinitialisation au thème et rechargement complet. Les 72 tests Manager et 27 tests Colors réussissent. Colors testé séparément en local, sans chargement parallèle sur le système de test ARM (Pi 5). Aucune migration des couleurs enregistrées nécessaire.

L’avertissement `lovelace` de la gestion des utilisateurs nécessite une investigation distincte. Une lecture échouée ne doit toujours pas être considérée comme un tableau de bord vide. Cet avertissement n’est pas encore attribué avec certitude à une régression de 2026.11.

Les apps non installées et les cycles d’écriture, de restauration, d’appareils ou de brokers non exécutés nécessitent d’autres tests réels. Les projets tiers comme UIX, Calendar Card Pro, Zendure et Frosted Glass n’ont pas été entièrement audités ici.

## Sauvegarde et nettoyage

Une nouvelle sauvegarde complète a précédé la vérification. L’automatisation de test n’exécutait qu’un délai, sans déclencheur automatique ni action sur des appareils. Elle et son tableau de bord ont été supprimés ; paramètres, projets, plugins existants et « Test für APP » sont conservés. Après autorisation explicite de supprimer la plus ancienne sauvegarde, exactement trois sauvegardes complètes restent disponibles ; sauvegardes de mise à jour d’app et copies PC conservées.

## Références

- [Changements officiels de HA 2026.11](https://www.home-assistant.io/blog/2026/11/04/release-202611/)
- [Composants du frontend en 2026.11](https://contributors.home-assistant.io/blog/2026/10/28/frontend-component-updates-2026.11/)
- [Retours des config entries : booléens toujours acceptés pour les intégrations personnalisées](https://contributors.home-assistant.io/blog/2026/10/23/config-entry-methods-return-none/)
- [Éditeur d’affichage original 20261028.4](https://github.com/home-assistant/frontend/blob/20261028.4/src/components/ha-items-display-editor.ts)
