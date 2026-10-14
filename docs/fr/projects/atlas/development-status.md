---
title: État du développement
description: État actuel du développement d'ATLAS.
---
# État du développement

## Variantes matérielles testées

| Variante | Environnement de test |
| --- | --- |
| amd64 | Home Assistant dans une machine virtuelle sous Proxmox |
| ARM64 | Home Assistant sur un Raspberry Pi 5 réel avec 8 Go de RAM |

Ces indications décrivent les installations testées ; le périmètre et les
vérifications restantes sont documentés dans l'état du développement ci-dessous.

## État actuel

**Correction des bundles Expert dans 0.1.297 :** les scripts générés et les bundles HACS conservent maintenant la disposition Expert structurée au lieu d’afficher uniquement une liste d’entités. Les helpers de cartes Home Assistant créent les cartes Core/Community intégrées ; les entités configurées sont remplacées et les changements d’état sont transmis sans recréer les cartes. Les projets existants et les anciens exports de scripts restent compatibles. La publication d’un dépôt HACS avec distribution des versions reste une étape distincte.

**Vérification native HA/HACS du 14 octobre 2026 :** Pi 5 et Proxmox exécutent ATLAS 0.1.296 après des mises à jour avec l’option de sauvegarde HA activée. Après l’installation HACS/Bubble/Mushroom sur Pi, les exports YAML ATLAS inchangés avec Core/Bubble/Mushroom s’exécutent sur les deux systèmes dans le véritable aperçu HA non enregistré, sans erreur de configuration. Un aperçu Mushroom Jinja supplémentaire sur Pi évalue l’état HA réel. Les projets d’origine et les exports Administration sont ensuite identiques, sauf les horodatages ; les six plugins restent actifs. Les tableaux de bord de test sont supprimés après confirmation. Ces aperçus ne vérifient ni l’installation complète des bundles, ni les commandes physiques, ni les performances sous charge.

**Renderer/thèmes dans la version 0.1.296 :** les états bloqué et en attente restent rouges et jaunes en mode sombre ; les lignes de champs Expert et les boutons de suppression restent lisibles dans les deux thèmes. Une vérification Chrome isolée avec 36 aperçus préparés Entity/Button/Sensor/Thermostat/Bubble/Mushroom confirme DE/EN/FR, clair/sombre/auto, rechargement et quatre tailles d’écran sans chevauchement ni débordement horizontal de la page. Les champs et les dimensions restent inchangés. Les événements de thème système sont simulés ; l’exécution native HA/HACS et les projets utilisateurs variés restent des vérifications A5 distinctes.

Les vérifications Docker effectuées le 14/10/2026 réussissent pour les images autonomes et du paquet HA sous Linux amd64 : compilation, véritable Administration/Card Editor, contrôles de santé, redémarrage du conteneur et mise à jour/restauration de plugins avec des données isolées. Neuf tests de régression backend/origin réussissent aussi dans l’image Linux. Cela ne remplace pas les vérifications natives Supervisor/Ingress, ARM64 ou navigateur ; les installations HA existantes n’ont pas été modifiées.

**Suite d’A5 du 14/10/2026 :** la version 0.1.295 respecte aussi l’état Administration enregistré dans le navigateur lors de l’ouverture des liens directs de lancement. Les plugins désactivés ou pas encore actifs ne sont pas lancés par cette voie. Il s’agit d’une préférence d’interface, pas d’un contrôle d’accès aux fichiers. Des tests isolés du véritable serveur vérifient installation, mises à jour refusées, remplacement, redémarrage, désinstallation et restauration du paquet ; les autres entrées et les données de test sont conservées. Ces tests ne remplacent pas une vérification native HA. A5 reste ouvert pour Renderer/Theme, les projets variés, la charge native et la reconnexion après fermeture du transport.

**A2 et A3 sont terminés (13/10/2026).** L'utilisateur accepte le périmètre actuel
des tests ARM64/mobiles. Les appareils iOS/Safari réels n'ont pas été testés ;
les simulateurs Chrome sont documentés séparément. Le Card Editor conserve
uniquement le workflow Expert. Le mode Simple et son sélecteur ne seront pas
réintroduits ; les imports de projets anciens pris en charge restent disponibles.

0.1.290 réduit la liste sur tablette à une fenêtre défilante avec deux cartes
côte à côte et dispose les boutons associés en deux colonnes.

0.1.291 replie Grille et zoom par défaut sur mobile et aligne les commandes du
titre sur tablette ; sur téléphone, les deux boutons partagent une rangée sous
le champ. Toutes les valeurs sont conservées.

0.1.292 supprime le choix du mode de démarrage dans la configuration HA et
l'Administration et traite les anciens réglages Simple comme Expert.

A5 a commencé : **0.1.293** corrige l'ordre des instantanés/événements et l'état
d'erreur lors du remplacement d'un socket. Un test PC isolé avec HA simulé valide
100 cartes affichées, 2001 entités, trois reconnexions, 150 mises à jour,
les changements de thème et les imports/exports de projets DE/EN/FR.
Les 162 tests HA réussissent. Ces mesures sont synthétiques.

La vérification native A5 charge 100 cartes compactes et 24 cartes plus grandes
sur Pi 5 et Proxmox, sans chevauchement. Les thèmes, rechargements et langues
DE/EN/FR conservent les champs. Les changements réels d'état des sauvegardes
arrivent en direct sur Pi ; Proxmox charge initialement 3711 entités et
143 ressources Lovelace. La valeur CPU observée sur la VM reste constante ;
un changement de valeur en direct n'y est donc pas établi. Des sauvegardes HA
locales chiffrées sont créées auparavant. Les configurations initiales de
l'éditeur et de l'Administration sont restaurées à l'identique, sauf les dates
d'export ; les six plugins restent actifs. Après un redémarrage de Proxmox
effectué par l'utilisateur, l'éditeur se reconnecte et le projet initial reste
inchangé.

Ces tests utilisent des dispositions d'entités préparées dans un navigateur
de bureau. Les projets utilisateurs variés, les mesures de charge du backend
natif, la reprise après fermeture du transport natif et les tests plus larges du cycle de vie des
plugins restent ouverts dans A5. Le rendu sur ordinateur n'est pas un benchmark
du Pi ; le redémarrage natif et les fermetures de socket simulées constituent
des preuves distinctes.

**0.1.294** corrige la reconnexion après une coupure réseau prolongée : les
tentatives continuent au-delà des trois premiers essais, avec un délai limité
à 30 secondes. Les erreurs d'authentification ou de protocole arrêtent les
tentatives jusqu'à la correction de la connexion. Un test isolé avec huit
secondes d'indisponibilité confirme la reprise sans rechargement et conserve
le projet. Pendant le test LAN réel, le câble du Pi a été débranché environ
douze secondes. Les 100 champs de test sont conservés et les données en direct
reprennent sans rechargement. La socket observée reste connectée ; cela ne
prouve pas une nouvelle connexion native. Les deux systèmes utilisent 0.1.294.
Les exports finaux confirment la conservation des paramètres Admin, des
métadonnées de chiffrement, des identifiants des plugins actifs et des projets
initiaux. Seul Icon Studio externe, mis à jour volontairement, change de version.
Un build Docker isolé et /health vérifient aussi la runtime commune
Administration/éditeur.
L'utilisateur confirme aussi le fonctionnement dans une VM macOS Ventura directement sur Proxmox,
mais signale une grande lenteur. Ce test fonctionnel comporte une limite de
performance ; la cause n'a pas encore été mesurée ou déterminée.

Au **13/10/2026** : framework **0.2.0-alpha.88**, application HA **0.1.294**.
Les quatre étapes de stabilisation sont terminées. La vérification couvre
870 tests des paquets, cinq tests supplémentaires, les contrôles de types et
les builds, ainsi que 15 étapes dans un navigateur isolé en DE/EN/FR. La migration
testée conserve les anciens réglages Admin, dépôts, thème et plugins actifs ;
les secrets passent dans le stockage chiffré.

A1 est vérifié sur l'installation HA réelle : mise à jour Supervisor de 0.1.287
à 0.1.288, redémarrage séparé et Ingress pour les six plugins installés.
Les réglages Admin, plugins actifs et la configuration complète de l'éditeur
restent identiques avant et après la mise à jour et le redémarrage, sauf les
horodatages d'export. Une sauvegarde HA locale chiffrée a été créée auparavant.
0.1.288 corrige la version affichée dans l'Administration ; les options HA et
contrats des plugins restent inchangés. L'éditeur se reconnecte et charge les
entités et ressources Lovelace réelles. Le canevas Expert existant était vide ;
les projets plus grands restent A5. Le matériel, les navigateurs mobiles, ARM64
et tous les formats de projets propres aux plugins ne sont pas vérifiés.

A2 est vérifié en émulation : images HA amd64 et ARM64 et contexte Chromium
mobile tactile à 360×800, 390×844, 844×390 et 768×1024 en DE/EN/FR. 0.1.289
corrige les débordements de l'Administration et de l'éditeur et adapte les
dialogues de rapport, import YAML et export aux écrans étroits. Les réglages,
projets de test remplis et données des plugins sont conservés après changement
de langue, import JSON/HACS et redémarrage. ARM64 est émulé sur x86 ; Raspberry
Pi natif, Android/iOS, glisser/redimensionner au toucher, clavier virtuel et
dialogues natifs de fichiers/téléchargements restent à vérifier. Ces tests
isolés ne modifient pas l'installation HA réelle.

Le test A2 natif sur **Raspberry Pi 5 / rpi5-64** réussit également : HA OS
18.3, ATLAS 0.1.289, `aarch64` et Node `arm64`. Les six plugins s'ouvrent via
Ingress ; Terminal, chemins File Studio autorisés et catalogue MDI fonctionnent.
Une sauvegarde HA locale chiffrée précède le redémarrage d'ATLAS. Les réglages
Admin, métadonnées des plugins et export complet de l'éditeur restent identiques,
sauf l'horodatage d'export. L'éditeur se reconnecte avec 27 entités réelles.
Le canevas existant est vide. Les vues Chrome de bureau à 390×844 et 844×390
s'adaptent à l'Ingress réel du Pi sans débordement. Les navigateurs mobiles
physiques, projets plus grands et mesures de charge/performance restent à
vérifier ; aucune mise à jour Supervisor ARM64 n'est effectuée ici.

L'utilisateur confirme aussi sur une **tablette Android réelle** : le Hub et
l'Administration fonctionnent en portrait et paysage et en DE/EN/FR. Remplacer
l'URL HA `homeassistant.local:80` par l'adresse IP accessible rétablit la
connexion ; le dialogue YAML et le rapport de problème sont également signalés
comme OK. Il s'agit d'une confirmation utilisateur, pas d'un test automatisé
sur appareil. [Conseils de connexion mobile](./homeassistant#connexion-sur-tablette-et-smartphone).
Les gestes de déplacement/redimensionnement, le clavier virtuel, les dialogues
natifs de fichiers/téléchargements et iOS n'ont pas été vérifiés indépendamment
sur chaque appareil. A2 est néanmoins terminé avec l'accord de l'utilisateur ;
ces limites ne sont plus des tâches A2 ouvertes.

ATLAS est en cours de développement. L'application Home Assistant comprend
l'Administration, le Hub des plugins et le Card Editor ; File Studio et
Automation Exporter / Editor sont distribués comme plugins indépendants.

La version actuelle de l'application Home Assistant est `0.1.297`.
L'Administration et le Hub des plugins proposent des interfaces en allemand,
anglais et français. Leur préférence de langue enregistrée est partagée entre
les deux interfaces, y compris lorsque leurs ports sont différents. Le
paramètre `language` d'une URL reste prioritaire pour la page ouverte.

## Suite du travail

1. **A5 – Production :** vérifier et améliorer Renderer, Theme et les API des plugins avec des projets réels plus grands, les mises à jour et reconnexions.
2. **A6 – Documentation française :** compléter les pages FR et aligner la structure et le contenu DE/EN/FR.
3. **A7 – Déploiement :** préparer l'installateur Linux/systemd et l'intégration native ATLAS HA/HACS avec le même runtime.

**A1 – Installation HA réelle et A4 – Nettoyage de la feuille de route sont terminés.** Les fonctions achevées
restent dans l'historique et ne sont plus des tâches ouvertes. Les plugins
indépendants conservent leurs propres listes de travaux.
La liste de référence se trouve dans la [feuille de route ATLAS](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
