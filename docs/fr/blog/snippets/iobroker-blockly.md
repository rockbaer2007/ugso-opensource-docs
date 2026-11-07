---
title: ioBroker Blockly
description: Introduction à Blockly, intégré à l'adaptateur JavaScript d'ioBroker, à travers un exemple de démarrage officiel.
---
<a id="statut"></a>


# ioBroker Blockly {#iobroker-blockly}

Blockly est l'éditeur de scripts graphique de l'**adaptateur JavaScript d'ioBroker**. Les automatisations sont construites à l'aide de blocs, ce qui évite d'avoir à rédiger manuellement l'intégralité du code JavaScript.

::: info Documentation officielle
Cette page ne propose qu'une brève introduction. La description complète de tous les blocs ainsi que d'autres exemples sont disponibles dans la documentation officielle d'ioBroker.
:::

## Relier Home Assistant à ioBroker et VIS 2 par MQTT {#mqtt-vis2-helper}

Cet exemple original UGSo complète l’introduction à Blockly : le **MQTT-Client pour Home Assistant** transmet les entités sélectionnées à un broker MQTT externe. Le **script JavaScript ioBroker 0.1.34** présenté ici les prépare pour VIS 2 et propose une structure plate facultative avec noms courts. Remplacez le script complet en conservant vos réglages pour utiliser cette option.

::: warning JavaScript, pas un import Blockly
Collez le script complet dans l’**adaptateur JavaScript ioBroker**, en tant que JavaScript. Il ne va ni dans Home Assistant ni dans l’importateur XML Blockly. Les exemples Blockly existants ci-dessous restent indépendants.
:::


### Nouveauté 0.1.36 : conserver les réglages après les mises à jour {#settings-persistence-0136}

**Les réglages enregistrés dans l’application sont désormais conservés lorsque le Supervisor Home Assistant régénère son fichier d’options pendant une mise à jour.** Cela concerne notamment la case des mesures associées, la structure MQTT des nouvelles entités, les autres réglages enregistrés et les identifiants de connexion. L’application les conserve séparément dans son fichier privé `/data/mqtt-settings.json`. Les affectations de chemins MQTT restent dans `/data/mqtt-routes.json` ; les points et références VIS-2 existants ne changent pas.

**Premier passage depuis la version 0.1.35 ou antérieure :** Exportez les réglages dans l’application avant la mise à jour. S’ils ont déjà été réinitialisés lors de ce premier passage, importez ensuite la sauvegarde ou sélectionnez de nouveau les deux options une fois, puis cliquez sur **Enregistrer et connecter**. Les réglages déjà perdus ne peuvent pas être reconstitués de façon fiable ; les mesures supplémentaires ne sont jamais activées sans votre choix.

Modifiez de préférence ces réglages dans l’application. Les modifications réelles de la configuration Supervisor sont reprises au redémarrage ; ses valeurs par défaut inchangées ne réinitialisent pas les choix de l’application. Pour revenir explicitement à un choix par défaut, sélectionnez-le et enregistrez-le dans l’application. Les sauvegardes de réglages existantes restent utilisables et excluent toujours les mots de passe et clés TLS privées. Le script JavaScript reste en version **0.1.34** ; ce correctif ne nécessite pas de le remplacer à nouveau.

Contexte : le Supervisor gère `/data/options.json` ; le répertoire privé `/data` fournit le stockage persistant de l’application. [Documentation officielle HA](https://contributors.home-assistant.io/apps/reference/environment/).


### Nouveauté 0.1.34 : chemins MQTT plats pour les nouvelles entités uniquement {#mqtt-layout-0134}

Dans **Transmission et TLS → Structure MQTT des nouvelles entités**, choisissez **Plate avec noms courts**, puis **Enregistrer et connecter**. La structure existante reste le choix par défaut. Ce réglage concerne les entités manuelles et les membres d’un label rencontrés pour la première fois ensuite, y compris les mesures facultatives du même appareil.

Les entités connues conservent leurs chemins. Les affectations sont enregistrées durablement dans `/data/mqtt-routes.json` et incluses dans la sauvegarde exportée des réglages. Retirer puis resélectionner un label, renommer, redémarrer ou mettre à jour réutilise le chemin attribué. Lors de la première mise à jour, les sélections existantes et les topics enregistrés sont conservés ; la sélection existante du label est fixée au premier rapprochement réussi. Ne supprimez pas ce fichier. Revenir au réglage précédent ne migre pas les entités déjà affectées.

Exemples de nouveaux topics MQTT plats :

```text
ha_external/geraet/schalter
ha_external/geraet/schalter_set
ha_external/geraet/schalter_attribute/device_class
ha_external/geraet/energie
ha_external/geraet/leistung
ha_external/geraet/licht_brightness
ha_external/geraet/licht_brightness_set
```

Les anciens topics comme `ha_external/geraet/switch/state` et `…/switch/set` restent valides en parallèle. Les noms courts en conflit reçoivent un suffixe unique. Les points, valeurs, alias et références VIS-2 existants ne sont ni renommés ni supprimés.

**Avant d’activer les chemins MQTT plats, remplacez le script JavaScript complet par la version 0.1.34 en conservant vos réglages.** Il lit les deux structures grâce au catalogue transmis, qui indique les chemins exacts des états et commandes. Vérifiez la prévisualisation, puis choisissez `mode: 'apply'`. Les anciens scripts ne reconnaissent pas les nouveaux chemins MQTT plats. L’option indépendante du script `virtualLayout: 'flat'` détermine uniquement la présentation sous `0_userdata.0.ugso_mqtt`. Les rôles manuels et références existants restent protégés.

### À quoi sert le script ? {#mqtt-helper-purpose}

MQTT utilise des topics séparés pour les retours d’état et les commandes. Le script les réunit via **un point virtuel par valeur** sous `0_userdata.0.ugso_mqtt`. Dans VIS 2, ce seul point suffit pour l’affichage et la commande.

```text
HA -> MQTT state -> 0_userdata.0.ugso_mqtt -> VIS 2
VIS 2 -> 0_userdata.0.ugso_mqtt -> MQTT set -> HA
```

- Les retours HA actualisent le point virtuel avec `ack: true`.
- La commande dans VIS 2 écrit avec `ack: false` ; seul un canal de retour autorisé est utilisé. La remise au broker n’est confirmée qu’après un nouveau retour HA réel.
- Les valeurs de lampe compatibles sont normalisées, par exemple la luminosité sur 0–100 %. Les mesures et dates restent en lecture seule.
- Les métadonnées HA adaptées fournissent les types, unités et rôles non ambigus. Les valeurs existantes, rôles manuels et objets tiers restent protégés.
- Le script traite uniquement les changements MQTT concernés. Il ne reconstruit pas l’ensemble à chaque modification de mesure sans rapport.

### Prérequis et installation {#mqtt-helper-setup}

1. Configurez le MQTT-Client HA et l’adaptateur MQTT ioBroker. L’application transmet au broker externe ; le canal de retour décrit ici utilise l’adaptateur MQTT ioBroker en mode **Server/Broker**.
2. Sélectionnez les entités ou attribuez l’étiquette HA configurée. **Les mesures supplémentaires nécessitent explicitement « Inclure automatiquement les mesures et valeurs de batterie du même appareil », puis « Enregistrer et connecter ».** Seuls les capteurs existants et compatibles du même appareil HA sont ajoutés.
3. Créez un script JavaScript dans l’adaptateur JavaScript ioBroker et collez le code complet ci-dessous. Le script a été testé avec l’adaptateur **10.4.10**.
4. Autorisez **setObject** dans les réglages de l’adaptateur et désactivez **Do not subscribe to all states on start**. Le script nécessite les caches synchrones d’objets/états. Aucune autorisation n’est nécessaire pour simplement consulter le code.
5. Vérifiez les chemins du bloc de réglages et conservez d’abord `mode: 'preview'`. L’aperçu crée uniquement les dossiers de base/points de sauvegarde manquants du script et journalise les affectations prévues ; il ne crée pas de valeurs virtuelles commandables et n’envoie aucune commande.
6. Après vérification, choisissez `mode: 'apply'` et redémarrez le script. Les points virtuels sont alors créés et synchronisés.
7. Dans VIS 2, sélectionnez le point virtuel adapté, **pas le point MQTT `set` brut**.

### Réglages et sauvegarde {#mqtt-helper-settings}

| Réglage | Signification |
| --- | --- |
| `mqttRoot` | Arborescence MQTT entrante ; valeur par défaut `mqtt.0.ha_external`. |
| `mode` | `preview` : vérifier ; `apply` : appliquer ; `restore` : annuler prudemment les propres modifications sauvegardées du script. |
| `outputMode` | `virtual` pour les points VIS-2 ; `roles` pour l’affectation alternative de rôles/alias. |
| `virtualLayout` | `nested` : anciens identifiants (par défaut) ; `flat` : points courts directement dans le dossier de l’appareil. |
| `virtualRoot` | Arborescence cible des valeurs virtuelles. |
| `virtualBackupId`, `backupId` | Journaux de sauvegarde du script ; les sauvegardes existantes sont conservées. |
| `aliasRoot` | Cible des alias en lecture seule en mode rôles. |
| `excludeIds` | Identifiants sources exacts à préserver. |

Lors du remplacement d’un script existant, conservez vos réglages. `restore` ne restaure pas toute l’installation ioBroker : les objets modifiés manuellement depuis restent protégés ; les valeurs/références virtuelles sont conservées et leurs commandes désactivées. Consultez le [guide complet du script](/fr/projects/mqtt-client/iobroker-roles) pour les détails, dont le tableau des rôles, les sauvegardes et les limites.

### Structure plate facultative avec noms courts {#mqtt-helper-flat-layout}

Dans le **script complet 0.1.34**, choisissez `virtualLayout: 'flat'` dans le bloc de réglages. La valeur par défaut reste `virtualLayout: 'nested'` ; une configuration existante sans ce réglage conserve également l’ancienne structure. Vérifiez d’abord l’aperçu, puis passez à `mode: 'apply'`.

```text
0_userdata.0.ugso_mqtt.pc_tv_wohnzimmer
  schalter
  energie
  leistung
  spannung
  stromstaerke
```

Les identifiants techniques utilisent ces noms allemands courts dans toutes les langues : énergie, puissance, tension et courant sont reconnus à partir de la classe d’appareil ; sinon, une partie adaptée de l’identifiant d’entité est utilisée. Les noms affichés sont aussi raccourcis, par exemple **Energie** ou **Stromstärke**. Les lampes utilisent **licht**, **helligkeit**, **farbe**, **effekt** et **farbtemperatur**.

Plusieurs valeurs correspondantes reçoivent **leistung**, **leistung_2**, **leistung_3**, etc. Les noms attribués sont enregistrés dans le journal existant et restent stables lors des changements de sélection ultérieurs. Les dossiers occupés, points tiers ou identifiants de sauvegarde ne sont pas écrasés ; un suffixe libre est attribué.

**Les points existants du script ne sont ni supprimés ni déplacés :** anciens et nouveaux identifiants restent synchronisés et conservent leurs canaux de commande autorisés. Les références VIS-2 existantes peuvent donc rester. Les nouveaux widgets peuvent utiliser les identifiants courts ; les anciens dossiers restent visibles au départ. Revenez en arrière avec `virtualLayout: 'nested'` dans le nouveau script. L’ancien fichier 0.1.27 ne peut pas lire les journaux contenant des entrées plates.

Les objets MQTT, chemins des topics, valeurs et rôles manuels restent inchangés. Si le retour à l’ancienne structure nécessite un dossier occupé par un point existant, ce nouveau chemin cible est ignoré et journalisé ; aucune valeur existante n’est remplacée.


### Script complet avec bouton de copie et téléchargement {#mqtt-helper-code}

<a href="/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.34.js" download>Télécharger le script JavaScript 0.1.34 (.js)</a>

Le bouton de copie en haut à droite du bloc reprend le **script entier**. Le bloc et le téléchargement utilisent le même fichier inchangé, sans identifiants personnels. Vérifiez ensuite les chemins et le mode pour votre installation.

<div class="mqtt-helper-code">

<<< @/public/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.34.js

</div>

### Valeurs ou confirmations absentes {#mqtt-helper-troubleshooting}

- **Seulement « Preview VIS 2 » dans le journal :** après vérification, passez à `mode: 'apply'`.
- **« setObject is not allowed » :** l’autorisation de l’adaptateur décrite ci-dessus manque.
- **Énergie, tension, courant ou puissance absents :** activez la case des mesures, enregistrez, puis ouvrez **« Vérifier les mesures associées »** dans l’application HA. Des noms similaires ne remplacent pas l’association à un appareil HA.
- **La commande fonctionne, mais sans confirmation :** vérifiez d’abord l’état MQTT brut. S’il reste ancien, le retour HA manque déjà en amont du script. Celui-ci ne fabrique jamais de confirmation et ne répète pas automatiquement les commandes.
- **La valeur MQTT `set` brute ne change pas :** les commandes passent par l’API du broker sans retain ; la valeur brute enregistrée ne doit pas nécessairement changer.

[Documentation MQTT-Client et mise à jour de l’application](/fr/projects/mqtt-client/) · [Guide du script et tableau complet des rôles](/fr/projects/mqtt-client/iobroker-roles)

<style scoped>
.mqtt-helper-code :deep(div[class*='language-']) { max-height: 36rem; overflow: auto; }
.mqtt-helper-code :deep(div[class*='language-'] pre) { max-height: none; overflow: visible; }
</style>


## Sources officielles {#offizielle-quellen}

- [ioBroker.javascript – dépôt officiel](https://github.com/ioBroker/ioBroker.javascript)
- [Documentation de l'adaptateur JavaScript (en allemand)](https://github.com/ioBroker/ioBroker.javascript/tree/master/docs/de)
- [Documentation complète de Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md)

## Exemple 1 : Commuter un point de données en fonction d'un autre point de données {#beispiel-1-datenpunkt-abhangig-von-einem-anderen-datenpunkt-schalten}

L'exemple d'introduction officiel illustre un scénario typique de détection de mouvement :

- Un point de données lié au mouvement sert de déclencheur.
- Lors d'un changement d'état, un point de données lié à l'éclairage est piloté.
- La valeur actuelle du détecteur de mouvement est transmise au point de données de l'éclairage.
- La détection d'un mouvement allume la lumière.
- L'absence de mouvement éteint la lumière.

[![Exemple Blockly officiel n° 1 pour ioBroker](https://raw.githubusercontent.com/ioBroker/ioBroker.javascript/master/docs/de/img/getting_started_1_de.png)](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

<small>
Source de l'image et droits : L'image provient du dépôt officiel
<a href="https://github.com/ioBroker/ioBroker.javascript" target="_blank" rel="noopener">ioBroker.javascript</a>.
Les droits et les conditions de licence sont régis par le projet qui y est publié et par sa licence associée.
</small>

## Blocs Blockly nécessaires {#benotigte-blockly-blocke}

### 1. Déclencheur (Trigger) {#_1-trigger}

Dans la catégorie **Déclencheur** (Trigger), on utilise le bloc **Si objet** (Falls Objekt).

On y sélectionne le point de données correspondant au détecteur de mouvement.

### 2. Piloter un point de données {#_2-datenpunkt-steuern}

Dans la catégorie **Système**, on insère le bloc **Piloter** (Steuere).

Le point de données correspondant à l'éclairage est sélectionné comme cible.

### 3. Récupérer la valeur {#_3-wert-ubernehmen}

Le bloc « commander » (ou « piloter ») intègre la **valeur de l'ID d'objet**.

On y sélectionne à nouveau le point de données correspondant au mouvement. Ainsi, l'éclairage adopte l'état actuel (Vrai/Faux) du détecteur de mouvement.

## Processus simplifié {#vereinfachter-ablauf}

```text
Falls sich der Bewegungsmelder ändert
    setze den Zustand des Lichts
    auf den aktuellen Wert des Bewegungsmelders
```

## Importer le bloc Blockly {#blockly-importieren}

Le code XML complet, prêt à être importé, est fourni dans la documentation officielle, juste en dessous de l'**Exemple 1** :

[Ouvrir l'Exemple 1 avec le code XML Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

Il suffit de copier ce code XML et de l'insérer dans l'éditeur Blockly via la fonction d'importation.

## Autres exemples officiels {#weitere-offizielle-beispiele}

La documentation officielle propose également :

- **Exemple 2 :** Allumer la lumière en cas de détection de mouvement et l'éteindre après dix minutes sans nouveau mouvement.
- **Exemple 3 :** Envoyer un e-mail lorsque la température extérieure dépasse un certain seuil.

[Voir tous les exemples officiels Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#getting-started)

## Partager vos propres exemples Blockly sur le blog {#eigene-blockly-beitrage-im-blog}

Pour vos propres exemples, la structure suivante est recommandée :

1. Décrire la tâche
2. Indiquer les ID d'objets nécessaires
3. Insérer une capture d'écran de la configuration Blockly
4. Fournir le code XML Blockly exporté
5. Expliquer les adaptations et les prérequis

Les captures d'écran sont stockées dans le projet de documentation ici :

```text
docs/public/images/blog/
```

Intégration dans l'article :

```md
![ioBroker Blockly](/images/blog/mein-blockly.png)
```

::: warning
Les ID d'objets présents dans les exemples doivent toujours être adaptés à votre propre système ioBroker.
:::
