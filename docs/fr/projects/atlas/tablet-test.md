# Test tablette : commencer petit

Au 19/10/2026, App 0.1.327 et HA 2026.10.2. **Préparé, pas encore validé sur
tablette.** Les contrôles sur PC ne prouvent pas les performances de la tablette.
Hôtes autorisés : `192.168.178.177` et `192.168.178.68` uniquement.

## Vérifier d’abord le navigateur

Sur un ancien Galaxy Tab A qui réagit déjà mal aux tableaux de bord ordinaires,
ne pas commencer par une forte charge. Conserver sa configuration Stream Deck.
Ouvrir dans un onglet séparé la page temporaire légère :

- [Vérification navigateur .177](http://192.168.178.177/local/atlas-tablet-20261019/index.html)
- [Vérification navigateur .68](http://192.168.178.68/local/atlas-tablet-20261019/index.html)

Ces pages ne chargent ni HA ni grandes cartes. Elles affichent fonctions et
identification du navigateur, sans télémétrie ni modification des réglages.
Une fonction disponible ne garantit ni compatibilité HA complète ni performances.
Âge du matériel, version Android et version du navigateur sont distincts ; les
versions exactes restent inconnues ici. Si une fonction manque ou la page ralentit,
arrêter. Ne pas effacer les données, désactiver la sécurité ou remplacer Stream Deck.

## Petit test initial

Seulement si la page reste fluide, choisir « Kleinen HA-Einstieg öffnen ».
Les tableaux séparés sont réservés aux administrateurs, hors barre latérale.
Se connecter soi-même avec le compte HA existant si nécessaire ; ne pas partager
identifiants ni jetons.

1. **Start** : choisir « Testzustand 18 », vérifier « HA verbunden ».
2. **12 Karten** : portrait/paysage, défiler jusqu’en bas puis remonter ; vérifier
   chevauchements, boutons coupés et retard des commandes.
3. « Testzustand 28 », « Hell », « Dunkel », puis « Theme zurück » après les
   transitions. L’état initial capturé est le thème standard en mode automatique.
4. « Wiederverbindung testen » une fois, sans recharger. Attendre « HA verbunden »,
   un compteur augmenté et « alter Socket geschlossen » ; réessayer l’état 18.

Arrêter si l’interaction bloque. Pour Stream Deck, cette petite étape est plus
pertinente qu’une forte charge imposée à cet appareil.

## Grandes étapes facultatives

Uniquement après une étape légère fluide : **360 Karten**, puis **720 Karten**.
Répéter rotation, défilement, états 18/28, clair/sombre et reconnexion. Mushroom
change Kühl/Warm, flocon/feu et bleu/rouge. Seule une entité synthétique propre
au test change ; aucun appareil réel n’est commandé. Cette préparation utilise
**Card-Mod 4.2.1 seul**, sans UIX ; elle ne valide pas UIX sur tablette.

## Résultats et nettoyage

Indiquer hôte/étape, portrait/paysage, défilement, thèmes, reconnexion et commandes
fluides, retardées ou bloquées. Ne pas extrapoler aux étapes non testées. Les
versions Android/navigateur sont utiles ; un blocage ne démontre pas sa cause
ni un défaut ATLAS.

Sauvegardes complètes et captures des données avant préparation ; éditeurs
existants inchangés. Vues temporaires conservées jusqu’au retour tablette.
Ensuite retirer états/ressources/tableaux propres au test, placer les fichiers
WWW dans la corbeille File Studio et garder les trois sauvegardes complètes
réussies les plus récentes par hôte. Conserver les sauvegardes PC.
