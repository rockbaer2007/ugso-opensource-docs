---
title: Blocks for HA
description: Créer visuellement des automatisations Home Assistant avec Blockly, YAML et Jinja.
---

# Blocks for HA

Nouveau en **0.1.66** : textes d’exemple inutiles supprimés dans toutes les catégories, notamment MQTT, objets, listes, conversions et valeurs de remplacement. Réponses Assist et texte Jinja vides sur une ligne. Séparateurs, structures JSON valides, réglages techniques et valeurs des projets existants conservés.

Nouveau en **0.1.65** : champ texte sur une ligne sans ligne d’aide, nouveaux textes vides et aucun bloc Bonjour prébranché dans Créer du texte avec. Texte existant conservé.

Nouveau en **0.1.64** : Templates par usage pour texte, plage horaire, variation et résultats si/sinon typés. Code Jinja libre une seule fois dans Templates. Commandes d’applications et d’automatisations sur deux lignes comme ioBroker. DE/EN/FR complets. [Guide et images](./system-template).

Nouveau en **0.1.63** : entrées de valeurs typées directes dans Template, comme Écrire un fichier dans ioBroker, avec ajout automatique d’une entrée. Sans engrenages sur les blocs Template. Les anciennes chaînes sont converties au chargement. [Guide](./system-template).

Nouveau en **0.1.62** : ID et valeurs d’entités partagées dans Système, instantané unique, commandes d’applications et d’automatisations, constructeur visuel de Templates. Relier texte, mathématiques, variables et valeurs système ; ajouter formatage, remplacement, nouvelle ligne et sortie conditionnelle. Clic droit pour Jinja et aperçu HA. DE/EN/FR. [Guide](./system-template).

Nouveau en **0.1.61** : blocs **et / ou / non** séparés. Ajouter, retirer et ordonner les champs HA facultatifs par engrenage. Champs obligatoires et valeurs importées conservés. DE/EN/FR. [Blocs examinés et utilisation](./advanced).

Nouveau en **0.1.60** : **Horaire** avec dialogue Assistant/Simple/CRON, onglets et secondes facultatives, jours, données du déclencheur et décalage solaire. Déclencheurs HA natifs avancés directement dans **Déclencheurs**. DE/EN/FR. [Comparaison ioBroker et limites](./time).

Nouveau en **0.1.59** : libellés et éditeurs proches d’ioBroker, **Commentaire** dans Système avec commentaires YAML et **Message MQTT** dans Messages sans sélection d’instance. Textes et images en DE/EN/FR. [Détails et images](./blocks).

## Démarrage vide depuis 0.1.52

Depuis **0.1.54**, **Nouvelle automatisation** propose **Enregistrer et recommencer**, **Recommencer sans enregistrer** ou **Annuler**. Avant de vider l’éditeur, la sauvegarde est téléchargée au format `.blocks.json` avec les blocs, les données d’automatisation et le YAML collé. **Ouvrir le projet** permet de la restaurer. Annuler ou Échap conserve le travail actuel. Recommencer réinitialise les blocs, l’historique d’annulation, le nom, la description et les champs. La langue, l’apparence, la connexion HA et les paquets de blocs installés restent disponibles.

Sans projet enregistré, l’éditeur démarre entièrement vide. Glisser **Automation** depuis **Système** dans l’espace de travail ou importer du YAML. L’import dans un éditeur vide ne nécessite pas « Remplacer complètement l’automatisation actuelle ». Les exemples s’ouvrent uniquement avec **Charger l’exemple**.

Les projets enregistrés sont restaurés au démarrage suivant. Un projet vide reste vide après rechargement ou changement de langue. Si le projet local ne peut pas être chargé, l’éditeur s’ouvre vide avec un avertissement, sans exemple.

Nouveau en **0.1.47** : [fonctions d’action avec paramètres et valeurs de retour conditionnelles](./blockly-audit). Le catalogue prend désormais en charge 166 types de blocs.

Nouveau en **0.1.46** : **Langue → Système / DE / EN / FR** concerne toute l’interface, les dialogues, états, confirmations et messages de validation. Noms personnels, données d’entités, libellés des paquets et YAML/Jinja ne sont pas traduits automatiquement.

![Interface française ; données de test et noms personnels conservés dans leur langue d’origine](/assets/blocks-for-ha/ui/fr.png)

Nouveau en **0.1.45** : quatre doublons retirés de la boîte à outils. Nombre uniquement dans Mathématiques, texte dans Texte, couleur dans Couleur, groupe ET/OU/NON dans Logique. Valeurs contient le pourcentage ; projets existants compatibles.

Nouveau en **0.1.44** : sélection avec recherche des actions et cibles, cinq types de cibles, choix multiple et saisie Jinja. [Utilisation et limites](./entities).

Nouveau en **0.1.42** : trois boutons compacts de même taille pour l’import YAML, avec des libellés sur deux lignes si nécessaire. **Eingabefeld leeren**, à droite, efface le texte collé et l’erreur d’import. L’automatisation actuelle et la case de remplacement sont conservées.

Nouveau en **0.1.41** : 15 types de blocs Jinja imbriqués, 163 types au total. Modifier entités, filtres, comparaisons, calculs et modèles if/else/for simples. Texte exact conservé jusqu’à modification ; modèles non pris en charge conservés en blocs originaux. [Décomposition et limites](./advanced#jinja-experimental).

Depuis **0.1.40**, tous les thèmes utilisent une **police de 16 px**. Le menu de blocs reste à **100 %** : ajustement, molette et zoom modifient uniquement l’espace de travail. Zoom initial 100 %, ajustement 85–120 %, zoom manuel 50–240 %. Les grandes automatisations restent défilables ; l’ajustement ne descend pas sous 85 % afin de préserver la lisibilité. Vérifié en Full HD, 2560 px et HiDPI.

Nouveau en **0.1.39** : 148 types, déclencheurs/conditions HA avancés, cibles/variables/options, attente, branches parallèles, groupes d’actions et **Jinja (expérimental)** avec reconnaissance et texte original conservé. [Guide, limites et sources](./advanced).

Blocks for HA assemble des automatisations Home Assistant avec des blocs visuels. Les déclencheurs, conditions et actions produisent du YAML natif ; les expressions utilisent Jinja dans Home Assistant. Blockly fournit l’éditeur, pas le moteur d’exécution de HA.

**Version 0.1.47 · 166 types de blocs · code source Apache-2.0**

[Code source sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha) · [Documentation DE](/projects/blocks-for-ha/) · [Documentation EN](/en/projects/blocks-for-ha/)

## Langue de l’application

Le sélecteur **Langue** propose **Langue du système**, **Deutsch (DE)**, **English (EN)** et **Français (FR)**. Le mode système utilise les langues préférées du navigateur, y compris les variantes comme `fr-CA` ou `de-CH`. Si aucune langue prise en charge n’est trouvée, l’anglais est utilisé.

Ce choix concerne toute l’application : commandes, libellés, menus déroulants, infobulles, catégories, recherche et dialogues, notamment la création de variables. La préférence est locale à ce navigateur et indépendante des thèmes.

Un changement sauvegarde le projet puis recharge l’éditeur. Terminer les blocs incomplets avant de changer de langue. Si le stockage du navigateur est indisponible, l’éditeur conserve les blocs et refuse le rechargement. Les IDs d’entités, noms de variables, textes saisis, modèles, paramètres et YAML ne sont pas traduits. Les blocs des paquets personnalisés conservent la langue définie par leur auteur.

Les captures du [catalogue des blocs](./blocks) sont générées avec les véritables blocs français. Les pages DE et EN utilisent leurs propres images.

## Installation et connexion

L’application est distribuée dans le [dépôt des applications HA UGSo](https://github.com/rockbaer2007/ugso-ha-mqtt-addons). Elle peut aussi être lancée localement depuis `blocks_for_ha` avec `npm install` puis `npm run dev` sur `http://127.0.0.1:4180/`. Pour compiler : `npm run build`.

Dans HA, ouvrir l’application via Ingress. La connexion aux entités utilise le service serveur supervisé, sans transmettre de jeton HA au navigateur. Hors HA, l’éditeur fonctionne avec saisie manuelle des IDs. Voir [Entités](./entities).

## Construire une automatisation

1. Donner un nom à l’automatisation et choisir son mode : `single`, `restart`, `queued` ou `parallel`. Les deux derniers proposent une limite maximale.
2. Placer les déclencheurs orange dans **Quand**, les conditions violettes dans **Seulement si**, puis les actions bleues dans **Alors**.
3. Rechercher ou saisir les IDs des entités. Remplacer les IDs d’exemple par ceux de son installation.
4. Vérifier le YAML et les diagnostics. Un indicateur valide vérifie la structure ; il ne confirme pas la disponibilité des services ou entités dans HA.
5. Copier le format **Einzelne Automation · HA-Editor** dans l’éditeur d’automatisation HA, via **Modifier en YAML**. Enregistrer et vérifier dans HA.

Les connexions sont typées : un déclencheur ne peut pas rejoindre une chaîne d’actions. Les valeurs numériques fixes et celles calculées à l’exécution ont des usages différents. Les blocs isolés ou incomplets peuvent empêcher l’export au lieu d’être ignorés.

## Importer et sauvegarder

**Kopieren** copie le YAML ; **Speichern** télécharge un fichier YAML nommé d’après l’automatisation. **Öffnen** lit un fichier pris en charge. Le format liste contient une seule automatisation. L’import ne convertit pas arbitrairement tout le YAML Home Assistant : les éléments non représentables sont refusés.

Pour coller du YAML, choisir **YAML → Code importieren**. Le panneau de sortie devient une zone de saisie ; **Importieren** remplace le bouton de sauvegarde. Taille maximale : **1 Mo en UTF-8**.

- Sans coche, l’import ajoute les déclencheurs, conditions et actions au projet valide actuel. Les conditions sont combinées avec ET ; les déclencheurs ajoutés peuvent entraîner davantage d’exécutions. Nom et réglages actuels sont conservés.
- Avec **Aktuelle Automation vollständig ersetzen**, une confirmation demande de remplacer tous les blocs. Après acceptation, les métadonnées et blocs importés remplacent le projet. Annulation ou erreur : état précédent conservé.

**Projekt sichern** télécharge le projet JSON complet, avec disposition et définitions des paquets utilisés. **Projekt öffnen** restaure ce projet. Le dernier état est également enregistré localement dans le navigateur. Cette sauvegarde locale ne remplace pas un fichier de sauvegarde.

## Espace de travail

Les commandes permettent d’annuler/rétablir, d’ajuster la vue et de chercher les blocs déjà placés. La recherche de la boîte à outils, en bas du menu, cherche les blocs disponibles. `Ctrl+F` ou `Cmd+F` dans Blockly ouvre la recherche de l’espace de travail ; Entrée/Maj+Entrée parcourt les résultats, Échap ferme la recherche. Le bouton **?** affiche les raccourcis de navigation.

Le panneau YAML peut être replié vers la droite ; l’éditeur récupère sa largeur. Le réglage est enregistré localement. Sur petit écran, le panneau replié forme une barre sous l’éditeur. Aucun changement du projet ou du YAML.

Le thème de l’application **Hell / Dunkel / System** est indépendant des palettes Blockly **UGSo Standard / Dark / Modern / Tritanopia**. Voir [Thèmes et zoom](./themes).

## Guides

| Sujet | Guide |
| --- | --- |
| Tous les types, images et fonctions | [Catalogue des blocs](./blocks) |
| Dates, comparaisons d’heure, soleil | [Date et heure](./time) |
| Nombres, booléens, dates, JSON | [Conversion](./conversion) |
| Délais, objets, conditions et choix | [Délais, objets et logique](./flow) |
| Calculs, textes, listes et boucles | [Mathématiques, textes, listes et boucles](./collections) |
| Différences Blockly/ioBroker/HA | [Comparaison et fonctions](./blockly-audit) |
| Connexion en lecture aux entités | [Entités](./entities) |
| Éditeur de paquets JSON/ZIP | [Blocs personnalisés](./custom-blocks) |
| Code copiable et téléchargements | [Catalogue des paquets](./catalog/) |

## Limites et direction

Les scripts ioBroker ne sont pas exécutés dans HA. Les intervalles nommés, `sendTo`, objets ioBroker et JSONata nécessiteraient une adaptation réelle. Le navigateur ne simule pas ces capacités. Les actions sont exécutées uniquement après utilisation du YAML dans Home Assistant.

Les prochaines possibilités comprennent la sélection des services et appareils HA, les variables typées, davantage de formes dans l’éditeur de blocs personnalisés et la gestion des versions de paquets. Le Block Factory original reste une référence ; ses définitions JSON seules ne contiennent pas un générateur HA complet.

## Licences

Projet communautaire indépendant, sans affiliation officielle à Home Assistant ou Blockly. Blockly est une bibliothèque de la Raspberry Pi Foundation, initialement développée chez Google. Les dépendances sont intégrées localement ; aucune bibliothèque Blockly n’est chargée depuis un CDN. Blockly et ses plugins : Apache-2.0 ; YAML : ISC ; fflate : MIT. Les notices sont incluses dans l’application.

<a class="blockly-attribution" href="https://www.blockly.com/" target="_blank" rel="noopener noreferrer"><img class="badge-light" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-white.svg" alt="Built with Blockly" width="87" height="32"><img class="badge-dark" src="/assets/blocks-for-ha/branding/built-with-blockly-badge-black.svg" alt="Built with Blockly" width="87" height="32"></a>

Depuis **0.1.28** : **États en liste JSON**, par exemple `["1_single","1_double"]` ; IDs facultatifs dans tous les déclencheurs standard ; **Déclenché par ID** comme condition native (ID individuel ou liste JSON). Les actions HA génériques acceptent **Cibles en liste JSON**, des métadonnées facultatives et conservent explicitement les données vides. Les automatisations à quatre boutons et quatre branches `choose` sont entièrement importables.

La sortie **Automatisation individuelle · Éditeur HA** omet l’`id` principal. Les IDs des déclencheurs restent présents. Les projets et la sortie **liste automations.yaml** conservent l’ID existant de l’automatisation.

[Home Assistant: Trigger IDs](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Trigger condition](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

Depuis **0.1.29**, l’espace Blockly occupe toute la hauteur du panneau jusqu’à la légende. Un panneau YAML plus haut agrandit aussi l’espace de travail ; la sortie reste repliable.

Depuis **0.1.30** : activer **Heures en liste JSON** pour plusieurs heures fixes, par exemple `["10:00:00","13:00:00","19:00:00"]`. **Tout changement** omet `to` ; **Entités en liste JSON** surveille plusieurs entités. Sans `to`, HA réagit aussi aux changements d’attributs. Les événements acceptent par exemple `timer.finished` avec un filtre de données JSON facultatif. Les conditions horaires natives conservent `before`/`after` : heures fixes, après inclusif et avant exclusif, même à travers minuit. Des bornes identiques couvrent toute la journée. Assistants horaires, modèles horaires et filtres de jours restent hors de l’import pris en charge. L’automatisation complète conserve le modèle multiligne du minuteur et les branches `choose` imbriquées.

[Home Assistant: triggers](https://www.home-assistant.io/docs/automation/trigger/) · [Time condition](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

Depuis **0.1.31**, le nouveau bloc prend en charge temperature.changed natif. Cible (JSON) : entity_id texte ou liste. Seuil (JSON) : type any, above, below, between ou outside. any exige seulement type ; above/below exigent value, between/outside value_min et value_max. Nombres : number et unit_of_measurement (°C/°F). Références : entity (sensor, number ou input_number). ID facultatif. Autres cibles (zone/appareil/étiquette) non prises en charge. Les topics MQTT, qos/retain/evaluate_payload et contenus JSON/Jinja multilignes restent présents.

[Home Assistant: temperature.changed](https://www.home-assistant.io/triggers/temperature.changed/)

**0.1.32:** Calendriers et variables de réponse. [→](./blocks)

**0.1.33:** Déclencheurs numériques avec durée de maintien. [→](./blocks)

**0.1.34:** Plusieurs variables dans une action. [→](./blocks)

**0.1.35:** Délai en texte ou modèle. [→](./blocks)

**0.1.36:** Noms d’action HA dynamiques. [→](./blocks)


**0.1.37:** [Déclencheur de motif horaire](./blocks).


**0.1.38:** [Entités cibles dynamiques](./blocks).

## Repères historiques et compatibilité

Ces repères complètent l’historique allemand ; ils ne remplacent pas les nouveautés plus récentes ci-dessous.

- **0.1.4 et versions antérieures :** les anciens projets migrent vers les nouveaux connecteurs. Les chaînes de conditions deviennent des groupes ET de même sens ; les fichiers YAML restent importables.
- **0.1.6 :** blocs Système pour le journal, les scripts HA et l’actualisation d’entités, ainsi qu’un bloc texte. Démarrer sans attendre utilise `script.turn_on`, arrêter utilise `script.turn_off`, appeler et attendre utilise directement `script.name`. `homeassistant.update_entity` demande une actualisation sans définir l’état et sans sémantique ioBroker `ack`. Paramètres supplémentaires via l’action HA générique ; données non représentables conservées dans cette action.
- **0.1.7 :** recherche en bas du menu, texte multiligne, pourcentage, couleurs, action lumineuse, date et listes d’assistants dépendantes. Depuis **0.1.58**, toutes les extensions, y compris Sinon, passent uniquement par l’engrenage. Retirer un connecteur détache ses blocs sans les supprimer. Le comparateur de date utilise `now().strftime('%Y-%m-%d')` et le fuseau HA : c’est une condition, pas un déclencheur. Vérifier les capacités des appareils dans HA.
- **0.1.8 :** création, affectation et lecture des variables ; catégorie Templates pour valeurs et conditions. Les variables produisent des actions HA `variables` ; Jinja est évalué uniquement dans HA. [Guide](./blocks#variablen-und-templates-verwenden).
- **0.1.9 :** comparaison, ET/OU compact, NON, booléens, null et sélection conditionnelle de valeurs. Variables booléennes et null prises en charge. [Logique](./blocks#logik-blocks-seit-0-1-9).
- **0.1.10 :** incrémenter une variable avec un pas initial de `1`, négatif ou décimal. [Exemple](./blocks#erhohen-und-verringern-seit-0-1-10).
- **0.1.11 :** sept blocs de date/heure : comparaison, plages traversant minuit, valeurs de date, début de calendrier, événements solaires, calcul et formatage. [Guide](./time).
- **0.1.12 :** neuf conversions : nombre, booléen, chaîne, type, date/heure, format/composants de date, différence et JSON. Format dynamique et formatage JSON ; JSONata reste une piste. [Guide](./conversion).
- **0.1.13 :** 18 blocs pour délais, objets, logique, boucles et listes ; pauses natives, attente avec délai limite, arrêt, répétition, dictionnaires, choix, intervalles, remplacement et listes. [Comparaison et limites](./flow).
- **0.1.15 :** mélange et couleurs aléatoires. Concaténation de texte et manipulation de listes sont également réalisées.
- **0.1.16 :** thèmes UGSo Standard/Dark/Modern/Tritanopia et ajustement du zoom, enregistrés localement. À ce stade : 111 types de blocs. [Guide](./themes).
- **0.1.17 :** catalogue d’entités HA en lecture, recherche par nom/ID, filtres lumière/script/assistant, IDs manuels hors connexion et identifiants gérés côté serveur. [Guide](./entities).
- **0.1.18 :** éditeur de blocs/modèles à 95 % de l’écran, catégorie personnalisée, plusieurs blocs par paquet, JSON copiable et import/export ZIP. [Guide](./custom-blocks).
- **0.1.19 :** badge Blockly officiel inchangé, de 32 pixels de haut, avec espace libre et lien vers Blockly. Les deux variantes SVG sont fournies localement. [Attribution originale](https://docs.blockly.com/guides/app-integration/attribution/).
- **0.1.20 :** icône monochrome `mdi:toy-brick-outline` dans la barre latérale HA. Mettre l’app à jour, la redémarrer et activer l’affichage dans la barre latérale ; recharger HA si l’ancienne icône persiste. L’icône UGSo colorée reste dans la boutique et l’éditeur.
- **0.1.21 :** recherche dans l’espace de travail, distincte de la recherche de la boîte à outils.
- **0.1.23 :** introduction et paramètres plus compacts, champs/boutons de 32 pixels, état de connexion HA et nombre d’entités dans la barre de réglages, y compris sur écran étroit.
- **0.1.24 :** flèche en haut à droite pour replier la sortie HA ; Blockly récupère la place disponible. La barre étroite rouvre le panneau. État enregistré localement ; une ligne compacte subsiste sur mobile. Aucun changement du YAML ou des projets.
- **0.1.25 :** importer via YAML → Code importé. Sans remplacement complet, ajout des déclencheurs, conditions et actions ; les conditions sont réunies par ET. Pour remplacer, cocher explicitement le remplacement et confirmer. Une seule automatisation, objet ou liste d’un élément, au maximum 1 Mo. Annulation ou code invalide conserve les blocs ; le texte collé reste disponible au changement de mode.

## Bibliothèque et démarrage local

La bibliothèque originale **Blockly 13.3.0** fournit l’espace de travail, la boîte à outils, les connecteurs typés, les blocs fantômes, les mutateurs, menus, zoom, corbeille et repères d’insertion. Les blocs HA, la validation, la migration des projets et la génération YAML sont du code UGSo. Aucun JavaScript ioBroker n’est exécuté.

Dans le dossier `blocks_for_ha` du [dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha), avec Node.js 22.12 ou plus récent :

```sh
npm install
npm run dev
```

Éditeur local : `http://127.0.0.1:4180/`. Les projets JSON conservent les positions ; le navigateur sauvegarde le dernier état localement. L’import YAML accepte une seule automatisation et refuse les structures non prises en charge.
