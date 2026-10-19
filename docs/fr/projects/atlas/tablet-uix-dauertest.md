# Test prolongé UIX sur tablette : 720 cartes

Au 19/10/2026. **Préparé, pas encore de résultat tablette de 60 minutes.**
App 0.1.327, HA 2026.10.2, UIX 8.4.0 ; Card-Mod n’est pas chargé.
Appareil indiqué : Samsung Galaxy Tab A6, Android 11 / LineageOS,
Chrome Mobile 155.

Sauvegardes complètes et captures des données avant préparation. Tableaux propres
visibles dans la barre latérale sans Admin-only ; éditeurs, projets, plugins
et réglages existants préservés.

## Sur la tablette

Effectuer 60 minutes complètes par hôte, successivement :

- [Test UIX .177](http://192.168.178.177/atlas-tablet-uix-soak-20261019/720)
- [Test UIX .68](http://192.168.178.68/atlas-tablet-uix-soak-20261019/720)

1. Brancher l’alimentation, garder l’écran éveillé et fermer les autres
   applications comme au test précédent. Garder la page au premier plan.
   Se connecter avec son compte HA existant sans partager les identifiants.
2. Vérifier « HA verbunden », puis appuyer une fois sur **60 Minuten starten**.
   Le compteur doit avancer ; ne pas recharger ni quitter la vue.
3. Toutes les dix minutes alterner portrait/paysage, défiler vers le bas et
   remonter. Observer blocages, chevauchements, textes coupés et cartes d’erreur.
   Textes, icônes et couleurs Mushroom suivent l’état synthétique.
4. Le contrôleur alterne 18/28 environ toutes les dix secondes, clair/sombre
   aux minutes 10/20/30/40/50 et reconnexion à 15/30/45. Une brève déconnexion
   est attendue, puis « HA verbunden » doit revenir sans rechargement.
5. À **60 Minuten beendet**, noter le résultat. **Ergebnis markieren**
   sélectionne le JSON local pour la copie normale. Si difficile sur tablette,
   indiquer d’abord hôte, durée finale, nombre de reconnexions et erreurs.
6. Répéter sur le second hôte. En cas de blocage ou déconnexion persistante,
   choisir **Stoppen / Theme zurück** et indiquer la durée avant le problème.

Seuls des états synthétiques propres changent, aucun appareil réel. Les écarts
du minuteur et temps de requête HA ne mesurent pas FPS/latence de rendu. Signaler
veille ou arrière-plan comme interruption. Fin/arrêt restaure le thème initial.
Recharger ne reprend pas automatiquement le test.

## Après le retour

La vérification PC ne remplace pas le test tablette. Retirer ensuite objets
propres et UIX temporaire, placer les fichiers WWW dans la corbeille récupérable,
comparer les données et garder trois sauvegardes HA complètes récentes par hôte.
Conserver sauvegardes PC et mises à jour. Ne jamais charger Card-Mod et UIX ensemble.
