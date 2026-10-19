# Test prolongé UIX sur tablette : 720 cartes

Au 19/10/2026. **L’utilisateur confirme 60 minutes sur chaque hôte, .177 et .68,
avec thèmes et reconnexion fonctionnels.**
App 0.1.327, HA 2026.10.2, UIX 8.4.0 ; Card-Mod n’est pas chargé.
Appareil indiqué : Samsung Galaxy Tab A6, Android 11 / LineageOS,
Chrome Mobile 155.

Sauvegardes complètes et captures des données avant préparation. Tableaux propres
visibles dans la barre latérale sans Admin-only ; éditeurs, projets, plugins
et réglages existants préservés.

Résultat fonctionnel rapporté par l’utilisateur, sans journaux JSON tablette
collectés séparément, mesures FPS/mémoire ni résultats détaillés de rotation/
défilement. La vérification PC et la simulation locale restent distinctes.

## Procédure historique

Effectuer 60 minutes complètes par hôte, successivement :

Les vues propres `/atlas-tablet-uix-soak-20261019/720` sont retirées après le
test ; les anciens liens ne sont plus actifs. Préparer de nouvelles sauvegardes
et vues avant une future répétition.

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

## Clôture

Tableaux, ressources, états synthétiques et UIX temporaire sont retirés ; fichiers
WWW dans la corbeille récupérable File Studio. Sept projets et six plugins par
hôte, 551 fichiers existants capturés sur .177 et neuf sur .68, réglages initiaux
et anciennes entrées de corbeille restent inchangés. Trois sauvegardes complètes
par hôte ; sauvegardes PC et mises à jour conservées. Ne jamais charger Card-Mod
et UIX ensemble.
