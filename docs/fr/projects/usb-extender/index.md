---
title: USB Extender pour Home Assistant
description: Relier des touches USB, Stream Deck et claviers à macros à trois courtiers MQTT. Installation illustrée, apprentissage, topics et résultats pratiques.
---

# USB Extender pour Home Assistant

**0.1.5 · Raspberry Pi · Mise à jour du 21 novembre 2026**

Un clavier USB connecté au Raspberry Pi peut servir de commande pour Home
Assistant ou ioBroker. USB Extender lit les entrées et les publie vers **trois
courtiers MQTT simultanément** au maximum. L’interface Web sert à la configuration
et peut ensuite être arrêtée ; le service USB/MQTT continue indépendamment.

[GitHub / README allemand et anglais](https://github.com/rockbaer2007/usb-extender-home-assistant)
· [ZIP 0.1.5](https://github.com/rockbaer2007/usb-extender-home-assistant/releases/tag/v0.1.5)
· [Modifications](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/CHANGELOG.md)

Il s’agit d’un programme autonome pour Raspberry Pi, pas d’une application HA à
installer dans le magasin, ni d’un logiciel officiel de Home Assistant ou Elgato.
Ce n’est **pas un tunnel USB sur IP** : les imprimantes et caméras ne sont pas
transmises comme périphériques USB distants.

Les captures fournies par l’utilisateur proviennent du montage réel en 0.1.5.
L’interface est actuellement en allemand. Cliquer sur les images larges pour les
ouvrir à leur taille d’origine.

[![Liste large des touches et groupes de canaux MQTT](/images/usb-extender/key-list.png)](/images/usb-extender/key-list.png)

## Quels périphériques sont détectés ? {#hardware}

**Détecté** signifie d’abord que Linux peut répertorier le périphérique USB.
**Utilisable** exige aussi un pilote capable de lire ses entrées et votre
autorisation explicite dans l’application. Ce sont deux capacités distinctes.

| Périphérique | Fonctions prévues | Vérification |
| --- | --- | --- |
| Claviers USB, y compris claviers multimédias Windows | Codes de touches, appui/relâchement, bascule, état d’appui, clic/double-clic/appui long | Claviers Trust/HCT utilisés dans le montage réel |
| Touches de volume et multimédias | `KEY_VOLUMEUP`, `KEY_VOLUMEDOWN`, `KEY_MUTE` ; autres touches de lecture/piste signalées par le matériel | Volume/muet observés ; autres touches à tester par modèle |
| Claviers à macros HID et pédales USB | Même traitement si Linux fournit des codes de touches ordinaires | Selon le modèle ; retours bienvenus |
| Elgato Stream Deck physiques | Pilote HID dédié ; fonctions d’affichage et d’entrée ci-dessous | Implémentées ; aucun Stream Deck physique encore testé dans ce projet |
| Autres appareils à touches LCD | Entrées clavier éventuellement via HID ; affichage nécessitant le pilote du fabricant | Aucune compatibilité générale garantie |
| Imprimantes, caméras, stockage USB, interfaces audio, appareils série et autres contrôleurs | Inventaire ; fonctions particulières nécessitant des adaptateurs spécifiques | Pas de transmission générale d’impression, caméra, audio, MIDI ou série |
| Stream Deck Mobile / application sur tablette | Ce n’est pas un périphérique USB directement connecté au Pi | Non intégré actuellement |

Un appareil répertorié n’est pas automatiquement activé. Dans **USB-Geräte**,
attribuer un nom, cocher **Gerät für Eingaben freigeben**, puis choisir les courtiers
destinataires. Les appareils sans numéro de série sont identifiés par leur port
USB ; un changement de port peut nécessiter une nouvelle affectation.

[![Inventaire USB et autorisation explicite des entrées](/images/usb-extender/devices.png)](/images/usb-extender/devices.png)

## Installation sur le Pi {#installation}

Configuration conseillée : Raspberry Pi 4, Raspberry Pi OS Lite **64 bits,
Bookworm ou ultérieur**, Python 3.11+, systemd, sudo et Internet pour apt/PyPI.
Plusieurs appareils avec écran peuvent nécessiter un hub USB alimenté séparément.
Le système Pi OS 32 bits n’a pas encore été validé en pratique.

Copier le ZIP sur le Pi, ouvrir un terminal dans son dossier de téléchargement et lancer :

```bash
sudo apt-get update && sudo apt-get install -y unzip
unzip USB-Extender-Home-Assistant-0.1.5-Raspi4.zip
cd USB-Extender-Home-Assistant-0.1.5
sudo bash install.sh
```

L’installateur présente neuf étapes, vérifie les dépendances et installe les
paquets manquants. Lors d’une mise à jour, il sauvegarde les données existantes
dans `/var/backups/` et conserve réglages et icônes. Le ZIP n’est pas une image
système entièrement utilisable hors ligne. Pour une mise à jour, extraire le
nouveau ZIP séparément et lancer son installateur.

Définir un mot de passe Web lors de la première configuration ; aucun mot de
passe par défaut n’est installé. Au besoin : `sudo usb-extender password`. Puis :

```bash
sudo usb-extender web start
```

Ouvrir `http://<adresse-du-Pi>:8098` dans le navigateur et se connecter. Remplacer
les adresses d’exemple des captures par celles de vos courtiers. Utiliser HTTP
uniquement dans un réseau local de confiance, sinon prévoir VPN/HTTPS. Ne pas
exposer directement l’interface sur Internet.

## Configurer les courtiers et apprendre les touches {#setup}

1. Dans **MQTT-Broker**, saisir hôte, port et identifiants éventuels. Activer les
   connexions souhaitées et enregistrer. Chaque courtier dispose de sa connexion ;
   une touche peut envoyer aux trois.
2. Activer la découverte pour HA. Pour ioBroker, choisir **Aus – nur MQTT-Daten senden**
   afin que son adaptateur de découverte HA ne signale pas de déclencheurs non pris en charge.
3. Dans **USB-Geräte**, nommer et autoriser l’appareil, choisir ses cibles et enregistrer.
4. Dans **Tasten & Anzeigen**, choisir l’appareil puis **Anlernen starten**.
   Appuyer et relâcher chaque touche souhaitée. Les répétitions et touches déjà
   présentes ne créent pas de doublons.
5. Choisir **Anlernen beenden → Tasten übernehmen → Speichern**. Les nouvelles
   lignes sont alors actives. Pendant l’apprentissage, l’appareil sélectionné
   n’envoie aucune action MQTT.
6. Modifier les cases des canaux, les topics ou les noms par ligne. **Bearbeiten**
   ouvre le choix des courtiers, le comportement Switch et les délais. Les nouveaux
   canaux supplémentaires des lignes existantes sont initialement désactivés ;
   les nouvelles touches apprises ont tous les canaux préparés.

[![Trois profils de courtiers dans le montage réel](/images/usb-extender/brokers.png)](/images/usb-extender/brokers.png)

[![Mode d’apprentissage avec appareil USB sélectionné](/images/usb-extender/learning.png)](/images/usb-extender/learning.png)

Si le navigateur se ferme pendant l’apprentissage, la pause expire au plus tard
après 15 secondes sans nouvelle confirmation. Les brouillons d’apprentissage
restent uniquement dans le navigateur jusqu’à leur application et enregistrement.
Les affectations déjà enregistrées sont conservées.

## Topics et fonctions des touches {#topics}

Le nom **Trust1** et la touche **F1** donnent par exemple `trust1-key-f1/press`.
Les noms sont adaptés à MQTT ; les caractères allemands de « Büro » deviennent
`buero`. Les noms identiques reçoivent au besoin `-2`, `-3`, etc. Les topics
enregistrés restent stables après un changement de nom et sont identiques sur
tous les courtiers choisis. Ils sont modifiables individuellement.

| Suffixe après `trust1-key-f1` | Valeur et fonction |
| --- | --- |
| `/press` | `press` immédiatement à l’appui |
| `/release` | `release` au relâchement |
| `/press-plus`, `/release-plus` | Même action, puis message vide après 50 ms sur ce canal |
| `/switch` | Premier appui `ON`, suivant `OFF` ; relâcher ne change rien |
| `/state` | Touche enfoncée `ON`, relâchée `OFF` |
| `/button` | `click`, `double_click` ou `hold` selon le geste |
| `/button-plus` | Même action Button, puis vide après 50 ms |
| `/click`, `/double-click`, `/hold` | Le geste individuel correspondant |

Le mot `plus` est écrit en toutes lettres, car `+` est un caractère générique MQTT.
Les onze canaux sont activables séparément. Seuls les canaux Plus reviennent au
vide ; vide ne signifie **pas** relâchement physique. Les valeurs Switch sont
conservées dans `switches.json` après un redémarrage et resynchronisées à la reconnexion.

**Clic/double-clic/appui long :** un clic attend la fenêtre de double-clic
(300 ms après relâchement par défaut). Un second clic dans cette fenêtre produit
uniquement `double_click`. Un appui de 700 ms produit `hold` une fois, sans clic
au relâchement. Maintenir le second appui remplace la séquence en attente par Hold.
Les délais sont réglables par touche. La répétition native du clavier ne compte
pas comme nouveau clic ou nouvel appui sur Switch.

**Volume :** les canaux Press/Press+ actifs peuvent se répéter pendant l’appui,
par défaut après 500 ms toutes les 150 ms. Le relâchement arrête la répétition ;
une limite de sécurité de 30 secondes s’applique aussi. L’automatisation HA ou la
logique ioBroker définit le pas de volume. Press/Release restent immédiats,
indépendamment de la reconnaissance différée des gestes Button.

Les messages utilisent QoS 0 sans Retain. Les entrées hors connexion ne sont pas
rejouées. Plusieurs canaux actifs peuvent déclencher plusieurs automatisations
associées ; choisir le canal adapté à la fonction unique souhaitée.

## Affichage dans Home Assistant et ioBroker {#integration}

La découverte HA regroupe toutes les touches sous le nom choisi avec un
identifiant stable commun. Les actions sont des déclencheurs d’appareil avec
filtrage de valeur. Switch et l’état d’appui sont des **capteurs binaires** indiquant
un état ; commander un autre appareil nécessite une automatisation ou une affectation.

<img src="/images/usb-extender/ha-states.png" alt="HA indique Switch activé et état d’appui désactivé après relâchement" width="280">

Dans la capture utilisateur, Switch est **activé** après l’appui et l’état d’appui
est **désactivé** après relâchement. Des valeurs inconnues peuvent apparaître avant
le premier message d’état reçu ; cela ne prouve pas une détection défectueuse.

<details><summary>Avant les premiers messages d’état</summary>

<img src="/images/usb-extender/ha-before.png" alt="États HA avant réception des premières valeurs des touches" width="280">

</details>

Dans ioBroker, les points de données séparés apparaissent sous l’adaptateur MQTT
à la première réception de chaque topic. La capture montre des valeurs simples :
`press`, `release`, `click`, `hold`, `ON` et `OFF`. Les canaux Plus affichent ici
`(null)` après leur remise à vide. C’est attendu ; le point de données reste présent.
Un point double-clic apparaît seulement après l’envoi du message correspondant.
Les anciens points contenant l’événement JSON initial ne sont pas modifiés
automatiquement. Les configurations de découverte restent volontairement en JSON.

[![Points de données ioBroker séparés avec valeurs simples](/images/usb-extender/iobroker-states.png)](/images/usb-extender/iobroker-states.png)

## Stream Deck et appareils similaires {#stream-deck}

Le pilote intégré `python-elgato-streamdeck` 0.10.0 connaît notamment Original/MK.2,
Mini, XL, Neo, Pedal et Plus. Cette liste décrit le pilote, **pas des essais matériels
physiques déjà effectués** dans ce projet.

- Touches avec écran : icônes/texte personnels, luminosité par appareil, retour
  d’état MQTT pour changer une icône et commandes d’affichage ciblées.
- Touches : Press/Release, clic/double-clic/appui long, Switch et état d’appui comme ci-dessus.
- Molettes présentes : sens de rotation et appui comme entrées.
- Écran tactile présent : événements tactiles ; pas d’éditeur d’écran librement composé.
- Pedal et autres modèles sans écran : entrées, mais pas d’icônes sur touches d’affichage.
- Une disposition fixe ; changement de profil/page et icônes animées restent à réaliser.

Dans **Iconbibliothek**, importer des images ou un dossier situé sur le Pi. Les
archives ZIP et `.streamDeckIconPack` disponibles localement sont également
acceptées. Aucun téléchargement automatique depuis le Marketplace Elgato.
Respecter les droits de chaque pack ; l’application utilise la première image
d’une animation.

Pour un appareil ressemblant à un Stream Deck, la partie clavier peut déjà
fonctionner via HID. LCD, tactile et commandes propres au fabricant peuvent
nécessiter un adaptateur dédié. Merci de tester un modèle précis et de décrire
les résultats plutôt que de supposer une compatibilité complète d’après son aspect.

## Arrêter l’interface Web et sauvegarder {#operation}

```bash
sudo usb-extender web start
sudo usb-extender web stop
sudo usb-extender web status
sudo usb-extender web enable
sudo usb-extender web disable
sudo usb-extender backup
sudo journalctl -u ugso-usbhub -n 50
```

`web stop` ferme le service HTTP ; fermer le navigateur seul ne le fait pas.
Le service USB/MQTT continue. Réglages, icônes et valeurs Switch se trouvent dans
`/var/lib/ugso-usbhub/`. Les dix versions précédentes de configuration sont
sauvegardées automatiquement ; une sauvegarde CLI complète inclut aussi icônes
et valeurs Switch. Ne pas publier les sauvegardes.

[![Commandes système et diagnostic](/images/usb-extender/system.png)](/images/usb-extender/system.png)

## Qu’est-ce qui est démontré en pratique ? {#tests}

Les captures utilisateur montrent 0.1.5, trois profils MQTT indiqués en ligne,
des touches de fonction apprises, des états HA et des points ioBroker individuels.
Le journal montre la remise des publications à HA, IOB et Testserver. Cette
indication seule ne prouve pas leur réception sur chaque courtier ; les captures
HA/ioBroker apportent une preuve visible supplémentaire. Toutes les fonctions
ne sont pas pour autant testées sur chaque appareil.

[![Événements F12 avec topics sélectionnés et trois destinations MQTT](/images/usb-extender/events.png)](/images/usb-extender/events.png)

En complément, 61 tests Python locaux et deux vérifications JavaScript/DOM
réussissent, notamment double-clic, persistance Switch après redémarrage,
routage et erreurs. Le test d’un Stream Deck physique reste ouvert.

## Tester votre matériel et faire un retour {#feedback}

Vous possédez un Stream Deck, un appareil à touches LCD similaire, un clavier à
macros ou une pédale USB ? Testez-le et [communiquez les résultats sur GitHub](https://github.com/rockbaer2007/usb-extender-home-assistant/issues/new?template=hardware-test.yml).
Les signalements d’erreurs et contributions sont bienvenus.

Indiquer modèle/révision, modèle du Pi, système et version de l’application.
Distinguer inventaire et vrais codes de touches. Décrire séparément appui/
relâchement, clic/double-clic/appui long, icônes/texte, luminosité, molettes,
tactile et débranchement/rebranchement ; préciser les fonctions non testées.
Commencer par un topic MQTT sans risque et sans action sur des appareils réels.
Les captures de l’inventaire et des événements aident. Ne pas publier de mots de
passe, jetons, `config.json` ou archives de sauvegarde.
