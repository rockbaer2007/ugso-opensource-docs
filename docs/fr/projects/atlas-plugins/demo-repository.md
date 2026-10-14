# Dépôt de démonstration

Le dépôt de démonstration est la source réelle de test du processus
d’installation ATLAS :

`https://github.com/rockbaer2007/atlas-plugin-repository-demo`

Pour créer votre propre dépôt de plugins, utilisez le
[modèle de plugin ATLAS](https://github.com/rockbaer2007/atlas-plugin-template).

## Objectifs

- Ajouter un dépôt de plugins dans l’Administration.
- Valider les marqueurs du dépôt.
- Afficher les plugins disponibles dans le Hub et l’Administration.
- Comparer les versions et signaler les mises à jour.
- Tester la page de transition vers l’installation.
- Charger ATLAS File Studio comme deuxième entrée de plugin réelle.
- Vérifier l’installation et les mises à jour de l’application Home Assistant
  à partir de dépôts GitHub réels.

## Page d’installation

La page publique est hébergée sur GitHub Pages :

`https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

Le bouton copie l’URL du dépôt ATLAS et explique comment la coller dans
l’Administration. Il n’ouvre pas le magasin d’extensions Home Assistant :
les plugins ATLAS et les extensions Home Assistant utilisent des formats
de dépôt différents.

## Test de mise à jour

Toute modification fonctionnelle d’un package doit augmenter sa version.
L’Administration peut alors détecter la mise à jour par rapport à la version
installée.

Cette règle concerne aussi les packages de test : les changements d’interface,
de manifeste, d’icônes, de contenu ou de comportement doivent être accompagnés
d’une nouvelle version publiée.
