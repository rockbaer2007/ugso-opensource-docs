---
title: USB Extender pour Home Assistant
description: Relier des touches USB, Stream Deck et claviers à macros à trois courtiers MQTT. Installation illustrée, apprentissage, topics et résultats pratiques.
---

# USB Extender pour Home Assistant

**0.1.31 · Version de test publique · Raspberry Pi · Mise à jour du 22 novembre 2026**

Un clavier USB connecté au Raspberry Pi peut servir de commande pour Home
Assistant ou ioBroker. USB Extender lit les entrées et les publie vers **trois
courtiers MQTT simultanément** au maximum. L’interface Web sert à la configuration
et peut ensuite être arrêtée ; le service USB/MQTT continue indépendamment.

[GitHub / README allemand et anglais](https://github.com/rockbaer2007/usb-extender-home-assistant)
· [ZIP 0.1.31](https://github.com/rockbaer2007/usb-extender-home-assistant/releases/tag/v0.1.31)
· [Modifications](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/CHANGELOG.md)

Il s’agit d’un programme autonome pour Raspberry Pi, pas d’une application HA à
installer dans le magasin, ni d’un logiciel officiel de Home Assistant ou Elgato.
Ce n’est **pas un tunnel USB sur IP** : les imprimantes et caméras ne sont pas
transmises comme périphériques USB distants.

Les captures fournies par l’utilisateur proviennent du montage réel en 0.1.5.
L’interface est actuellement en allemand. Cliquer sur les images larges pour les
ouvrir à leur taille d’origine.

[![Liste large des touches et groupes de canaux MQTT](/images/usb-extender/key-list.png)](/images/usb-extender/key-list.png)

## Nouveautés 0.1.31 : T650, périphériques et droits d’installation {#release-031}

0.1.31 inclut les modifications auparavant locales des versions 0.1.29 et 0.1.30.
**Tasten & Anzeigen** regroupe les périphériques par ordre alphabétique, repliés
initialement. Un seul groupe et une seule touche restent ouverts à la fois.
Les touches de volume, de luminosité et d’éclairage du clavier proposent un filtre
de pas 1–5 sous **Bearbeiten** : 3 envoie les pas 3, 6, 9, etc. Le relâchement
arrête la répétition du volume, même lorsque certains pas sont ignorés.

Les numéros de série uniques et les identifiants Logitech HID++ disponibles
conservent l’affectation lors d’un changement de port. Sans identifiant unique,
affecter explicitement le nouvel appareil USB à une entrée hors ligne enregistrée ;
touches, pages et topics sont conservés. La suppression confirmée par la corbeille
sauvegarde les métadonnées et conserve les icônes partagées. Révoquer séparément
la confiance Mobile.

### T650 : glissement à un doigt et X/Y {#t650}

Dans **USB / Virtuelle Geräte**, autoriser le T650, activer **Touchpad-Gesten
auswerten**, puis ouvrir **Ein-Finger-Slide und optionale X/Y-Werte**. Régler la
sensibilité et la fréquence maximale, enregistrer, puis apprendre les directions
souhaitées. Le pilote Linux doit fournir le multitouch de type B ; un simple
événement de clic ne suffit pas.

| Mouvement | Action à apprendre |
| --- | --- |
| Gauche / droite | `TOUCHPAD_SLIDE_LEFT` / `TOUCHPAD_SLIDE_RIGHT` |
| Haut / bas | `TOUCHPAD_SLIDE_UP` / `TOUCHPAD_SLIDE_DOWN` |
| Haut gauche / haut droite | `TOUCHPAD_SLIDE_UP_LEFT` / `TOUCHPAD_SLIDE_UP_RIGHT` |
| Bas gauche / bas droite | `TOUCHPAD_SLIDE_DOWN_LEFT` / `TOUCHPAD_SLIDE_DOWN_RIGHT` |

Huit secteurs de 45° distinguent les directions. La **sensibilité 1–10** définit
le mouvement nécessaire : 10 est plus sensible, 1 demande un mouvement plus ample ;
valeur initiale 5. La **fréquence 1–30/s** est une limite par flux d’actions
directionnelles et par paire X/Y, initialement 10/s. Une paire X/Y représente deux
messages MQTT par courtier cible ; les autres canaux de touche activés peuvent
produire des messages supplémentaires.

**X/Y est désactivé initialement.** L’activation suivie de l’enregistrement crée
des topics lisibles, par exemple `t650-touchpad/x` et `t650-touchpad/y`. Des topics
personnalisés sont possibles ; les topics enregistrés restent identiques après
renommage. Les deux axes utilisent les courtiers cibles de l’appareil et envoient
des nombres entiers **0–100**, sans JSON. X : gauche 0, droite 100 ; Y : haut 0,
bas 100. Il s’agit de la position absolue sur le pavé tactile.

Après un glissement reconnu, aucun tapotement supplémentaire n’est produit au
relâchement. Les positions inchangées ne sont pas retransmises. Une dernière paire
en attente peut suivre le relâchement au prochain intervalle autorisé. Plusieurs
doigts, un clic mécanique, une perte d’entrée ou une modification des options
annulent les valeurs en attente. Pas de conservation MQTT ni de renvoi aux
courtiers précédemment déconnectés ; X/Y reste muet pendant l’apprentissage.

### Test réel du T650 et limites {#t650-test}

Test du 22 novembre 2026 avec un véritable T650 et un Raspberry Pi 4 en 64 bits :

- Les huit directions attendues sont reconnues ; **aucun tapotement** pendant les
  glissements. Un test séparé a produit quatre tapotements, sans sortie X/Y.
- Trois courtiers MQTT de test locaux ont reçu chacun **752 messages identiques**,
  dont 200 paires X/Y. Les axes transmettent des entiers dans la plage 0–100.
- **En direct** : sensibilité 5, limite de 10/s ; intervalle minimal 0,100000 s.
- **Relecture des mêmes enregistrements réels** : la sensibilité 1/5/10 a produit
  33/38/39 actions lors des mouvements rapides. Les limites 1/5/30 ont donné des
  intervalles X/Y minimaux de 1,006229 / 0,201979 / 0,037912 s. Cela ne remplace pas
  un nouveau test en direct des réglages Web ou de nouveaux gestes à chaque valeur.
- Deux événements de direction voisine et un appui long ont aussi été enregistrés.
  Aucune garantie d’une direction exclusivement unique pour chaque geste, ni de
  validation générale des autres gestes multitouch ou modèles de pavés tactiles.
- Seul le T650 a été évalué ; K400/T400 sont inchangés. La mesure isolée utilisait
  des réglages temporaires et des courtiers de boucle locale, sans cible de production.

[Rapport complet du T650 et de l’installation](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/v0.1.31/docs/tests/t650-0.1.31-20261122.md).
L’outil de mesure a également été corrigé : la purge bornée consomme le générateur
evdev ; un message de départ et un compte à rebours rendent la fenêtre de mesure visible.

### Correction de l’installateur et conservation des données {#installer-031}

Un `umask 077` hérité pouvait rendre le nouvel environnement Python inaccessible
au compte de service (`Permission denied` à l’étape 6). L’installateur définit
désormais `umask 022` pour les fichiers du programme et `umask 077` pour les archives
privées. Aucune modification globale des droits des données utilisateur n’est requise.

L’installation suivante sur le Pi a été vérifiée : CLI et service actif indiquent
**0.1.31**, USB/MQTT et Web sont actifs, avec **NRestarts=0** chacun. Mobile est
actif et la liste d’erreurs est vide. Cinq contrôles SHA256 de `config.json`,
`switches.json`, `mobile-identity.json`, `mobile-trust.json` et `mobile-devices.json`
confirment des réglages et jumelages identiques octet par octet. Une sauvegarde a
précédé l’installation. Ce contrôle du démarrage ne constitue pas un nouveau test
d’endurance après installation.

## Quels périphériques sont détectés ? {#hardware}

**Détecté** signifie d’abord que Linux peut répertorier le périphérique USB.
**Utilisable** exige aussi un pilote capable de lire ses entrées et votre
autorisation explicite dans l’application. Ce sont deux capacités distinctes.

| Périphérique | Fonctions prévues | Vérification |
| --- | --- | --- |
| Claviers USB, y compris claviers multimédias Windows | Codes de touches, appui/relâchement, bascule, état d’appui, clic/double-clic/appui long | Claviers Trust/HCT utilisés dans le montage réel |
| Touches de volume et multimédias | `KEY_VOLUMEUP`, `KEY_VOLUMEDOWN`, `KEY_MUTE` ; autres touches de lecture/piste signalées par le matériel | Volume/muet observés ; autres touches à tester par modèle |
| Claviers à macros HID et pédales USB | Même traitement si Linux fournit des codes de touches ordinaires | Selon le modèle ; retours bienvenus |
| Logitech T650 | Huit directions à un doigt, X/Y 0–100 optionnel | Test isolé T650/MQTT réel réussi ; limites ci-dessus |
| Elgato Stream Deck physiques | Pilote HID dédié ; fonctions d’affichage et d’entrée ci-dessous | Implémentées ; aucun Stream Deck physique encore testé dans ce projet |
| Autres appareils à touches LCD | Entrées clavier éventuellement via HID ; affichage nécessitant le pilote du fabricant | Aucune compatibilité générale garantie |
| Imprimantes, caméras, stockage USB, interfaces audio, appareils série et autres contrôleurs | Inventaire ; fonctions particulières nécessitant des adaptateurs spécifiques | Pas de transmission générale d’impression, caméra, audio, MIDI ou série |
| Stream Deck Mobile / application Android | Serveur réseau expérimental optionnel avec jumelage QR, images et MQTT | Jumelage, transfert d’icônes, couleurs et grille 8×8 confirmés par l’utilisateur ; stabilité à long terme encore à vérifier |

Un appareil répertorié n’est pas automatiquement activé. Dans **USB / Virtuelle Geräte**,
attribuer un nom, cocher **Gerät für Eingaben freigeben**, puis choisir les courtiers
destinataires. Les identifiants uniques de série ou d’appareil sont indépendants
du port. Sans identifiant unique, affecter l’appareil reconnecté à une entrée hors
ligne enregistrée.

[![Inventaire USB et autorisation explicite des entrées](/images/usb-extender/devices.png)](/images/usb-extender/devices.png)

## Installation sur le Pi {#installation}

Configuration conseillée : Raspberry Pi 4, Raspberry Pi OS Lite **64 bits,
Bookworm ou ultérieur**, Python 3.11+, systemd, sudo et Internet pour apt/PyPI.
Plusieurs appareils avec écran peuvent nécessiter un hub USB alimenté séparément.
Le système Pi OS 32 bits n’a pas encore été validé en pratique.

Copier le ZIP sur le Pi, ouvrir un terminal dans son dossier de téléchargement et lancer :

```bash
sudo apt-get update && sudo apt-get install -y unzip
unzip USB-Extender-Home-Assistant-0.1.31-Raspi4.zip
cd USB-Extender-Home-Assistant-0.1.31
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
3. Dans **USB / Virtuelle Geräte**, nommer et autoriser l’appareil, choisir ses cibles et enregistrer.
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
- Jusqu’à huit pages indépendantes par deck avec touches de navigation ; profils supplémentaires encore à réaliser. Les icônes animées sont implémentées.

### Éditeur graphique et liste compacte des touches {#editor}

L’onglet **Stream Deck** reste visible hors ligne et conserve l’éditeur et la
dernière grille. Autoriser l’appareil et enregistrer, puis choisir une touche :
texte, icône, image de fond, position et couleurs. L’état **enfoncé** accepte une
seconde icône et des couleurs de texte/fond distinctes. Un texte en haut/bas
réserve sa place à côté de l’icône ajustée. L’aperçu ne déclenche aucune action MQTT.
Enregistrer ensuite.

[![Éditeur avec appareil simulé](/images/usb-extender/editor-022.png)](/images/usb-extender/editor-022.png)

Cette image est une **démonstration locale**, pas un essai matériel.
Dans **Tasten & Anzeigen**, les lignes repliées montrent **Appareil – Key – Nom** ;
une seule touche est dépliée. **Speichern** enregistre toutes les modifications en
attente ; **Abbrechen** annule seulement celles de cette touche. Des repères signalent
les modifications non enregistrées. **Bearbeiten** ouvre les options MQTT avancées
et les délais.

## Pages et navigation sur le deck {#pages}

**USB / Virtuelle Geräte** regroupe les périphériques USB et les decks Mobile
virtuels jumelés. Chaque téléphone/tablette conserve ses pages et affectations.

1. Dans **Stream Deck**, **Neue Seite** ajoute une page, jusqu’à huit par appareil.
   Les numéros continuent : 1–15 puis 16–30 pour 15 touches ; 1–64 puis 65–128
   pour 8×8. La grille vient toujours de l’appareil ou de l’application Android.
2. Choisir une touche, puis **Gestaltung → Tastenfunktion** : MQTT, **Vor**
   (suivante), **Zurück** (précédente), **Home** (première) ou **Gehe zu** (aller à)
   avec **Zielseite** (page cible). Après **Speichern**, la touche navigue sur
   la tablette sans envoyer d’action MQTT.
3. **Seitennummer anzeigen** ajoute un compteur. Home revient à la page 1 ;
   suivante/précédente s’arrêtent aux limites. Les boutons de l’éditeur changent
   seulement l’aperçu, pas la page réellement affichée sur l’appareil.
4. **Aktuelle Seite löschen** supprime les affectations de cette page après
   confirmation ; **la page 1 est protégée**. Enregistrer pour appliquer.
   Les IDs/topics des autres pages restent stables même si les numéros affichés
   changent. Les cibles suivent leur page renumérotée ; supprimer la cible
   redirige la touche vers la page 1.

La navigation conserve les affectations MQTT existantes ; choisir de nouveau
MQTT les réactive. Les nouvelles pages reçoivent des topics stables tels que
`tablet-page-2-key-0/press` ; ceux de la première page restent inchangés.
Un redémarrage du service ouvre la page 1. Changer de page termine les touches
maintenues et clics en attente ; un retour MQTT d’une autre page n’écrase pas
la page visible. Les champs d’apparence et de couleur sont plus compacts.

[![Pages et champs compacts, simulation locale](/images/usb-extender/pages-028.png)](/images/usb-extender/pages-028.png)

## Stream Deck Mobile : optionnel et expérimental {#mobile}

1. Activer **Mobile-Server**, saisir l’adresse accessible du Pi et le port
   (**28198** par défaut), puis enregistrer.
2. Choisir **Kopplung starten · QR-Code** et scanner avec **Ajouter un ordinateur** dans Android.
3. Comparer l’empreinte à six chiffres. Seulement si elle correspond, cliquer sur
   **Gerät vertrauen** dans **Mobile-Verbindungen**. La confiance reste enregistrée.
4. Ouvrir un deck dans Android, autoriser l’appareil Mobile dans USB Extender et
   enregistrer. Affecter l’apparence et MQTT dans l’éditeur Stream Deck.
5. **Régler lignes et colonnes dans Android.** L’éditeur suit la grille annoncée
   jusqu’à 8×8 ; aucun remplacement de grille côté éditeur.

Le service Mobile fonctionne indépendamment du service Web. Le jumelage exige
l’interface Web ; elle peut ensuite être arrêtée. Port WebSocket local, sans
découverte cloud/Bonjour ni modification des droits d’achat Pro de l’application.

**Mobile-Verbindungen** affiche compteurs d’images/métadonnées, ping/pong et dernière
déconnexion. Pour des touches **statiques** inchangées, les compteurs d’images doivent
cesser d’augmenter. Le maintien de connexion n’envoie pas de nouvelles images ;
les animations en transmettent volontairement. L’utilisateur a confirmé jumelage,
icônes, couleurs et 8×8. L’essai de 15 minutes avec navigation et repos ci-dessous est réussi.

### 0.1.28 : essai de 15 minutes réussi {#stability}

Les images Mobile sont envoyées en petits lots : au plus quatre images par
itération avec un budget de travail souple de 25 ms. Les entrées et le heartbeat
sont traités entre les lots. Un envoi réseau déjà commencé peut durer plus
longtemps ; le délai heartbeat reste de 20 secondes. Le journal de déconnexion
ajoute Ping/Pong, type/âge du dernier message et images en attente, sans contenu
des messages ni identifiants de connexion.

Le **22 novembre 2026**, une vraie **SM-T580 avec grille 8×8 et deux pages** a
été observée pendant 900 secondes : plusieurs passages suivante/précédente,
puis environ 14 minutes au repos. L’utilisateur a lancé le moniteur SSH en
lecture seule ; ses 16 mesures et le journal final ont été examinés directement.

| Mesure | Résultat |
| --- | --- |
| Période selon l’horloge du Pi | 11:39:17–11:54:17 ; durée contrôlée par un minuteur monotone |
| Connexion tablette | Ouverte et autorisée aux 16 mesures |
| Ping/Pong | 56/56 → 232/232 ; les 176 pings supplémentaires ont reçu une réponse |
| Repos | 1 228 images / 19 paquets de métadonnées inchangés dès la minute 1 |
| Journal final | Aucun nouveau timeout heartbeat, aucune déconnexion ni relance du service |

Une entrée supplémentaire « connection open » ne précise aucun appareil ; les
compteurs tablette continuent sans remise à zéro. [Mesures complètes, rapport allemand](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/docs/tests/mobile-0.1.28-15min-20261122.md).
Cet intervalle est réussi. Écran éteint, fonctionnement en arrière-plan, autres
réseaux et Stream Deck physiques ne sont pas vérifiés ici ; cela ne prouve pas
rétrospectivement la cause de toutes les déconnexions précédentes.

## Bibliothèque d’icônes, animations et import de packs {#icons}

**Sélecteur graphique au lieu de longues listes :** icônes normales/enfoncées,
fonds et retours MQTT utilisent le même sélecteur. Déplier un pack, rechercher,
choisir une icône et **Übernehmen** (ou double-cliquer). **Abbrechen**/Échap
conservent l’ancien choix ; **Speichern** enregistre ensuite. Seules les miniatures
PNG 48×48 sont chargées, première image d’une animation, avec au plus 96 cases
visibles par page de pack. Le Pi les crée à la demande dans
`icons/.cache/thumbnails/` ; le Pi et le navigateur authentifié réutilisent le cache.

Les mêmes IDs/contenus apparaissent une fois par pack ; les noms alternatifs
restent recherchables. Originaux et IDs enregistrés ne sont ni supprimés ni
réécrits. Styles distincts et packs noir/blanc restent séparés.
**MDI-Favoriten hinzufügen · 40 Icons** importe, sur demande, le pack SteelBlue
fourni avec 20 paires marche/arrêt. Aucune installation ou affectation MQTT
automatique ; choisir soi-même les icônes normales/enfoncées ou les retours.

[![Sélecteur graphique et cache de miniatures, démonstration locale](/images/usb-extender/picker-028.png)](/images/usb-extender/picker-028.png)

Déplier les packs séparément ou rechercher noms de packs, fichiers et sous-dossiers.
Survol/focus affiche nom et aperçu. Miniatures 48×48 dans des cases compactes 52×52 ;
la licence figure une fois dans l’en-tête du pack. Espace libre et total en haut de page.

[![Packs avec aperçu, démonstration locale](/images/usb-extender/icons-022.png)](/images/usb-extender/icons-022.png)

Importer images seules, dossiers du navigateur, dossiers sur le Pi et packs locaux
ZIP, `.streamDeckIconPack` ou `.streamDeckPlugin`. Les plugins fournissent seulement
les images des dossiers pris en charge, jamais le code exécutable. Les métadonnées
JSON reconnues donnent le nom du pack, sinon le nom du dossier/de l’archive est utilisé.
Les noms et sous-dossiers d’origine sont conservés. Aucun téléchargement automatique
du Marketplace ; respecter les droits d’utilisation.

PNG/JPEG et SVG statiques sont pris en charge. GIF/WebP s’animent dans les états
**normal et enfoncé**, jusqu’à 120 images et 10 images/s. Les animations SVG ne sont
pas lues ; les fonds restent statiques. La lecture réelle doit être vérifiée par modèle.

Originaux : `/var/lib/ugso-usbhub/icons/IconPacks/` ; index : `icons/index.json` ;
aperçus dérivés : `icons/.cache/`. La suppression d’un pack crée d’abord une
sauvegarde et bloque les packs utilisés par des affectations enregistrées.

**Depuis 0.1.22 :** enregistrer l’index une fois à la fin et créer aperçus/données
d’animation à la demande. Les dossiers du navigateur sont envoyés en un ZIP,
en conservant plusieurs packs et leurs chemins. La progression utilise les vrais
compteurs du serveur. **Terminer un import en cours avant toute mise à jour.**

| Comparaison unique sur PC Windows local | Avant | 0.1.22 |
| --- | --- | --- |
| Itsyhome, 240 PNG réels | 4,262 s | 0,395 s |
| 6 800 PNG synthétiques | 458,323 s | 10,464 s |

Écritures de l’index : auparavant 240 ou 6 800, désormais une par import.
Ces mesures concernent le PC, pas le Pi/la carte SD. Lors du précédent import de
6 862 icônes, la page de connexion est réapparue à 2 898, sans message d’erreur.
Après installation de la mise à jour, l’utilisateur indique que cela fonctionne
à nouveau. La fin de l’import des 6 862 icônes n’est pas encore confirmée.

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

La version 0.1.28 réussit 168 tests Python locaux ainsi que des vérifications
JavaScript/DOM et Chrome pour pages, enregistrement, affichage mobile, choix
d’icônes, packs et animations. L’essai réel de 15 minutes ci-dessus est réussi.
Ajout/suppression de page, Home et Gehe zu sont vérifiés localement ; leur
vérification matérielle complète et les Stream Deck physiques restent à tester.

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
