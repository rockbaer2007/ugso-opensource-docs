---
title: SVG LineBox – Collecte et transmission de valeurs de lignes
---

# SVG LineBox {#svg-linebox}

À partir de la version Studio 0.1.136, la ligne de sortie propose une option supplémentaire : **Ajustement automatique du diviseur (SVG LineBox)**, avec sa propre vitesse cible (0,05 à 5 cycles/s ; valeur par défaut : 1). Cela permet de conserver une animation fluide et bien réglée, même pour des sommes importantes. Cette option est indépendante du mécanisme de division automatique utilisé pour les entités numériques ; voir [SVG-Line](/fr/projects/grafik-visual-studio/svg-line).

La **SVG LineBox**, située dans la section **HA Grafik – Spezial**, agrège les valeurs numériques provenant des « SVG-Lines » qui y sont connectées. Elle calcule une somme algébrique (tenant compte des signes) et peut transmettre le résultat à des lignes de sortie, voire, en option, à une entité numérique auxiliaire (« helper ») de Home Assistant. Ce bloc est visible dans l'éditeur, mais disparaît lors de l'exécution (runtime) ; les lignes actives convergent alors visuellement vers son centre.

## Configuration dans l'éditeur {#im-editor-einrichten}

1. Ajoutez une **SVG LineBox** ainsi que les **SVG-Lines** nécessaires.
2. Activez les **points d'ancrage** sur la LineBox, en ne sélectionnant que les positions requises. Par défaut, les douze points sont désactivés. L'option **Tous les points** permet de les activer ou désactiver simultanément ; il est également possible de sélectionner chaque position individuellement.
3. Dans la section **Connexions**, chaque point actif se voit attribuer un rôle : **Entrée**, **Remise à zéro** ou **Sortie**. Le rôle **Remise à zéro** est défini par défaut ; il n'est pas pris en compte dans le calcul. Aucun rôle ne peut être attribué aux points désactivés.
4. Reliez les lignes d'entrée aux entrées, et connectez une autre « SVG-Line » à une sortie. À partir de la version Studio 0.1.126, une ligne peut reprendre la valeur d'un widget numérique connecté à son autre extrémité (par exemple, une entité de type « Number »). Alternativement, vous pouvez sélectionner une **entité numérique** via le paramètre **Animation → Source de direction** ; cette source de ligne dédiée est prioritaire.
5. Activez l'option **Transmettre la valeur calculée** au niveau de la sortie, et **Activer l'animation** sur la ligne de sortie. Ce n'est qu'alors que la somme en pilotera la direction et la vitesse.

Les points d'ancrage présentent les mêmes douze positions que sur les autres widgets : à gauche et à droite (en haut, au milieu, en bas) ; en haut et en bas (au quart, au milieu et aux trois quarts). Vous pouvez connecter plusieurs lignes à un même point. Ce sont les fonctions **Entrée** et **Sortie** qui déterminent le rôle, et non la simple orientation visuelle de la ligne.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="SVG LineBox im Editor bearbeiten">
<source src="/videos/grafik-visual-studio/linebox_edit.mp4" type="video/mp4">
<a href="/videos/grafik-visual-studio/linebox_edit.mp4">Ouvrir la vidéo de l'éditeur</a>
</video>

[Ouvrir directement la vidéo de l'éditeur](/videos/grafik-visual-studio/linebox_edit.mp4)

## Comment la somme est générée {#wie-die-summe-entsteht}

La LineBox prend en compte les lignes SVG visibles connectées à ses **entrées** si elles portent une valeur numérique valide. Une entité numérique explicitement associée à la ligne est prioritaire ; en son absence, la valeur est récupérée depuis le widget numérique connecté ou depuis une sortie LineBox activée. Dans le cas d'un widget de type « Number », le multiplicateur est appliqué, sans arrondir la valeur affichée. L'animation d'une ligne d'entrée définie manuellement reste indépendante du transfert de valeur. Concernant les valeurs transmises par les lignes : si la ligne se termine au niveau de la LineBox, sa valeur est ajoutée à la somme avec son signe d'origine ; si elle y prend naissance, elle est comptabilisée avec le signe inversé. Les valeurs provenant automatiquement de widgets sont converties en fonction de l'orientation de la ligne. Chaque ligne n'est comptabilisée qu'une seule fois au maximum. Les états manquants ou invalides sont ignorés ; en l'absence d'entrée valide, aucun calcul n'est effectué. La valeur zéro est considérée comme valide. Les boucles de rétroaction internes sont interrompues.

**Exemple sans éléments auxiliaires supplémentaires :** connectez un widget « Number » (réglé sur 125) et un autre « Number » (réglé sur 79) à des entrées via deux lignes : la LineBox affichera **204**. Connectez ensuite la sortie activée à un autre widget (de type « Number », « Red Number », « Gauge » ou « Bar »). Dans les paramètres de ce widget, sous **Source de la valeur → Valeur depuis le point d'ancrage**, sélectionnez le **point d'ancrage d'entrée** et activez-le dans la section **Points d'ancrage**. La valeur est alors directement reprise par l'affichage ; si plusieurs lignes valides sont connectées à ce point, leurs valeurs sont additionnées en tenant compte de leur signe. En l'absence de valeur valide, le code `--` s'affiche. Les autres sources disponibles sont : **Entité Home Assistant / Aperçu** (comportement existant) et **Valeur d'aperçu** (qui ignore toute entité renseignée).

Exemple : Deux lignes d'entrée aboutissent à la LineBox, identifiées par `1000` et `-300`. La somme est représentée par `700`. Pour une troisième ligne, partant d'une **sortie** et ayant l'option **Transmettre la valeur calculée** activée, `700` indique un flux allant du début vers la fin. Si la ligne de sortie se termine au niveau de la boîte, le signe correspondant à son orientation est inversé. Ses couleurs, ses pointes de flèche et son type de trait restent inchangés. Si son animation est désactivée, elle demeure immobile même lorsqu'une valeur lui est transmise ; de même, `0` ou l'absence d'entrée valide entraîne son arrêt. L'utilisation de l'option **Diviseur SVG LineBox (lors de la transmission)** sur la ligne de sortie permet d'obtenir `700 ÷ 100 = 7` cycles/s. La plage générale pour l'animation numérique se situe entre 0,05 et 20 cycles/s.

En position **zéro**, un point ne contribue ni à la somme ni à la sortie. Désactivez l'option **Transmettre la valeur calculée** sur une sortie si vous souhaitez que la ligne SVG connectée soit à nouveau pilotée uniquement par ses propres paramètres d'animation. Un simple croisement de lignes n'établit aucune liaison.

## Point de connexion et exécution (Runtime) {#verbindungspunkt-und-runtime}

En mode exécution (Runtime), les lignes actives sont dirigées vers le centre de la zone invisible. Le groupe **Point de connexion** contrôle l'affichage :

| Propriété | Effet |
| --- | --- |
| **Afficher le cercle** | Affiche ou masque le cercle situé au-dessus des extrémités des lignes. Par défaut : activé. Il apparaît lorsqu'au moins deux lignes connectées sont visibles. |
| **Diamètre (px)** | Diamètre souhaité du cercle (de 4 à 100 px) ; pour les lignes épaisses, il s'agrandit si nécessaire afin de recouvrir leurs extrémités. |
| **Couleur de remplissage**, **Couleur de bordure**, **Épaisseur de bordure (px)** | Couleurs et épaisseur de la bordure du cercle ; l'épaisseur peut être réglée entre 0 et 20 px. |
| **Afficher la valeur de sortie** | **Désactivé** (par défaut), **Au-dessus du cercle** ou **En dessous du cercle**. Affiche la somme des entrées (avec signe) ; en l'absence d'entrée valide, un tiret s'affiche. Cet affichage peut être utilisé même si le cercle est masqué. |

La valeur affichée est mise à jour en mode exécution, y compris lors du déplacement d'un curseur (slider). Visuellement, le cercle se superpose aux lignes connectées, masquant ainsi leurs extrémités anguleuses.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="SVG LineBox in der Runtime">
<source src="/videos/grafik-visual-studio/linebox_runtime.mp4" type="video/mp4">
<a href="/videos/grafik-visual-studio/linebox_runtime.mp4">Ouvrir la vidéo du mode exécution</a>
</video>

[Ouvrir directement la vidéo du mode exécution](/videos/grafik-visual-studio/linebox_runtime.mp4)

## « Helper » (assistant) numérique optionnel dans Home Assistant {#optionaler-home-assistant-zahlenhelfer}

La transmission aux lignes de sortie s'effectue en interne et ne nécessite aucun « helper » (assistant) supplémentaire. Si vous souhaitez également traiter la somme dans Home Assistant, activez l'option **Écrire en plus dans un assistant numérique** (sous la rubrique **Sortie de l'assistant numérique**) et sélectionnez un assistant de type `input_number.*` existant. Lors de l'exécution, l'application n'effectue une écriture que lorsque la valeur change ; les variations rapides sont regroupées. La plage de valeurs autorisée pour cet assistant doit englober la somme potentielle. Si ce même assistant sert également de source de données pour une ligne d'entrée de cette LineBox, l'écriture est bloquée afin d'éviter une boucle de rétroaction directe. Aucune écriture n'a lieu en l'absence d'entrée valide.

La première version lit des entités numériques via les lignes d'entrée. Il n'existe pas encore de gestion spécifique des entités par connexion. L'ancien nom de palette **Linebox** reste utilisable comme terme de recherche ; les projets enregistrés conservent le type technique `linebox` ainsi que les noms de widgets personnalisés existants.

Vous trouverez des paramètres supplémentaires concernant l'historique, les couleurs, les flèches et les animations dans la section [SVG-Line](/fr/projects/grafik-visual-studio/svg-line).
