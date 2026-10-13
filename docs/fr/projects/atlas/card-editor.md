---
title: Accueil Assistant Card Editor
description: Page française préparée pour Accueil Assistant Card Editor dans la documentation UGSo Open Source.
---
# Accueil Assistant Card Editor

## Signaler un problème (depuis 0.1.287)

Le bouton crée d'abord un aperçu local. La copie utilise le texte vérifié ; si
le presse-papiers échoue, l'aperçu reste disponible pour une copie manuelle.
Le bouton GitHub ouvre seulement le formulaire avec des instructions. Le rapport
n'est ni envoyé automatiquement ni placé dans l'URL GitHub.

Le filtre masque les identifiants dans les champs structurés, le JSON/YAML entre
guillemets, les URL et leurs fragments, ainsi que le jeton HA de session connu
dans le reste du texte. Les cookies et le stockage du navigateur ne sont pas lus.
Les indicateurs de clés configurées sont uniquement booléens. Vérifiez quand même
les textes, entités et données personnelles avant de partager. L'ouverture du
rapport ne modifie ni les projets, ni les réglages, ni les plugins.

## Mise à jour 0.1.286

Le rechargement et l'import JSON/HACS conservent les identifiants des modèles
et les dimensions de référence du redimensionnement. Un paquet HACS peut être
réimporté lorsque le nom du projet diffère du titre de la première carte : les
noms des deux manifestes sont comparés. Le contenu des cartes et les réglages
existants sont conservés.

Le parcours Administration → Plugin Hub → connexion HA → éditeur Expert →
export/import a été vérifié en DE/EN/FR avec un serveur HA simulé, un profil de
navigateur isolé et un plugin de test, y compris le rechargement et le redémarrage
du conteneur. Cela ne remplace pas une vérification sur une installation HA réelle.

Cette page française a été ajoutée afin que la documentation Open Source dispose d'un chemin de langue complet. La traduction détaillée sera encore enrichie.

La page anglaise correspondante est actuellement la référence de structure : [`en/projects/atlas/card-editor.md`](/en/projects/atlas/card-editor).

## Statut

- Le chemin de langue existe.
- La navigation et le build peuvent résoudre cette page.
- La traduction détaillée pourra être affinée lors d'une passe de documentation ultérieure.
