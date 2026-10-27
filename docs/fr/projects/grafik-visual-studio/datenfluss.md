---
title: Flux de données – Valeurs, conversion et calcul
---

# HA Grafik – Flux de données {#ha-grafik-–-datenfluss}

À partir de la version **0.1.287**, il est possible de masquer **tous les widgets** via l'option **WIDGET → Masquer à l'exécution (In Runtime verstecken)**. Enregistrez le projet après avoir effectué cette opération. Un widget de type « Number » (nombre) masqué peut continuer à transmettre des valeurs à un module de calcul (« Math ») ; une « MathBox » masquée continue également d'effectuer ses calculs. Cette option ne désactive pas la source des données et fonctionne indépendamment de l'index Z (Z-index). Dans l'éditeur, tous les éléments restent modifiables.

À partir de la version **0.1.285** : les éléments « SVG-Line » et « Wert-Verbindung » (connexion de valeurs) prennent en charge le paramètre **Ligne → Position de départ verticale**. Les lignes verticales à angle droit se tracent d'abord verticalement, puis s'orientent vers la gauche ou la droite pour atteindre la hauteur cible. Les poignées de contrôle apparaissent après un déplacement de 6 px ; elles ne permettent pas de déplacer une sélection multiple. Pour déplacer des lignes ancrées dans leur intégralité, utilisez la touche **Alt**. Une ligne SVG standard avec un **index Z (Z-index) de -100 ou moins** reste également invisible lors de l'exécution, sans pour autant perdre ses valeurs. Elle peut servir à relier un widget « Number » à un module « Math » ; consultez les instructions et l'exemple de valeur nulle sous [LineBox Math](/fr/projects/grafik-visual-studio/svg-linebox-math).

À partir de la version **0.1.141**, la palette dédiée **HA Grafik – Flux de données** propose trois widgets. Tous les calculs et conversions sont effectués dans le navigateur de l'appareil d'affichage utilisé. Home Assistant fournit les valeurs des entités ; aucune entité HA supplémentaire n'est requise pour le traitement interne. La visualisation doit être ouverte pour cela.

| Widget | Dans l'éditeur | En exécution (Runtime) |
| --- | --- | --- |
| **Liaison de valeur** | Ligne SVG simple sans animation, orientée du départ vers l'arrivée | Invisible ; les valeurs sont transmises |
| **Convertisseur de valeur** | Widget et boîte de dialogue dédiée avec boutons radio, type d'entrée/sortie et aperçu | Toujours invisible ; la conversion reste active |
| **Calcul de valeur** | Éditeur identique à celui de [SVG LineBox Math](/fr/projects/grafik-visual-studio/svg-linebox-math), avec quatre calculs et des connecteurs A–P | Invisible par défaut ; tous les calculs et sorties restent actifs |

La « Liaison de valeur » et le « Calcul de valeur » utilisent en interne les types existants *SVG Line* et *SVG LineBox Math*. Cela permet de conserver les fonctionnalités d'ancrage, de déplacement, de copie, d'import/export de projet, ainsi que la logique de calcul commune. Pour *SVG LineBox Math*, l'option **Masquer en exécution** peut également être activée. Dans le cas du « Calcul de valeur », vous pouvez désactiver cette option si vous souhaitez rendre le widget de calcul visible.

## Connecter une source {#eine-quelle-verbinden}

![Point de départ unique avec sélection de position](/images/grafik-visual-studio/output-point.png)

Depuis la version 0.1.154, la section CSS « Général » reste obligatoirement active, même pour ces widgets ; les autres sections CSS sont facultatives.


À partir de la version **0.1.143**, les sections CSS facultatives sont désactivées par défaut pour les nouveaux widgets de flux de données ; pour les widgets de calcul de valeur, la section « Affichage » est également désactivée par défaut. Les fonctions de calcul et de conversion restent actives. Ces sections peuvent être activées si nécessaire ; les champs CSS désactivés ne sont pas exportés. Les nouvelles connexions de valeurs ne comportent pas de pointes de flèche aux extrémités. Les widgets déjà enregistrés conservent leurs paramètres actuels.

1. Pour un widget doté d'une valeur d'entité ou d'une valeur de prévisualisation, activez l'option **Activer le point de départ** dans la section **Flux de données**. Utilisez les boutons radio (**Haut**, **Bas**, **Droite** ou **Gauche**) pour définir le point de départ au milieu du côté correspondant ; par défaut, il est situé à droite. Ce point de départ unique fonctionne indépendamment de la section **Points d'ancrage** et peut être désactivé. Vous pouvez définir sa couleur spécifique via **Paramètres → Point de départ**. Ce point n'est visible que dans l'éditeur ; la transmission de la valeur reste active lors de l'exécution (runtime). Les widgets ne disposant pas de valeur (par exemple, les simples cadres) ne transmettent aucune valeur. Les configurations existantes des points d'ancrage sont conservées ; les éléments *LineBox*, *LineBox Math* et les convertisseurs continuent d'utiliser leurs propres points de connexion.
2. Ajoutez une **connexion de valeur** : reliez le point de départ (source) à l'entrée du convertisseur ou du récepteur. Le flux de données suit toujours cette direction, même en l'absence de pointes de flèche visibles ; l'animation des lignes est désactivée.
3. Dans le convertisseur, ouvrez **Modifier la conversion**, sélectionnez l'entrée et la sortie, puis activez l'option **Activer les points d'ancrage d'entrée/sortie sélectionnés**. Les nouveaux points d'ancrage restent inactifs tant qu'ils ne sont pas explicitement activés. 4. Sélectionnez la conversion et vérifiez l'aperçu. Pour les éléments **Number** (Nombre) et **String** (Chaîne) du jeu de base, activez l'option **Activer le point d'entrée** sous la rubrique **Flux de données**. Pour les autres récepteurs standards, activez l'option **Reprendre la valeur du flux de données** ainsi que leur point d'ancrage d'entrée. Dans le cas de **Number**, il est également possible d'utiliser le mécanisme existant de reprise sur point d'ancrage numérique ; ce dernier permet de continuer à additionner plusieurs valeurs numériques.

Un convertisseur et le mécanisme général de reprise du flux de données autorisent **exactement une source par entrée**. Plusieurs connexions sortantes peuvent distribuer un même résultat vers différents récepteurs. Le convertisseur n'effectue pas d'addition de textes ou d'états de commutation. Le composant « LineBox Math » conserve son propre mécanisme d'addition pour les entrées numériques multiples.

### Point d'entrée pour Number et String {#eingangspunkt-bei-number-und-string}

À partir de la version **0.1.274**, les deux widgets de base disposent, dans la section **Flux de données**, d'un point d'entrée dédié. Tout comme pour la sortie, vous pouvez choisir entre **Haut**, **Bas**, **Droite** ou **Gauche** ; par défaut, l'entrée est située à gauche. Cette entrée fonctionne indépendamment de la zone des **points d'ancrage**. Une fois activé, le widget récupère la valeur de la source connectée, aussi bien dans l'éditeur qu'en phase d'exécution (*runtime*). Lors d'un changement de page, les connexions d'entrée existantes sont conservées. Si une sortie est également activée, la valeur reçue peut être transmise vers un autre élément.

Lorsque la réception du flux de données est désactivée, le widget affiche à nouveau sa valeur d'entité ou sa valeur de prévisualisation. Les points de flux de données ne sont visibles que dans l'éditeur.

## Boîte de dialogue du convertisseur {#konverterdialog}

![Boîte de dialogue du convertisseur avec boutons radio et prévisualisation pour la conversion d'un texte de température en nombre](/images/grafik-visual-studio/dataflow-converter-dialog.png)

| Conversion | Paramètres et résultat |
| --- | --- |
| Nombre → Texte | 0 à 10 décimales, point ou virgule décimale, unité optionnelle |
| Texte → Nombre | Détection du point/virgule décimale et de l'unité associée ; sortie sous forme de nombre |
| État de commutation → Nombre | Marche → 1, Arrêt → 0 ; inversion possible |
| Nombre → État de commutation | Marche si valeur ≥ seuil, sinon Arrêt ; inversion possible |
| État de commutation → Texte | Textes personnalisés pour « Marche » et « Arrêt » ; inversion possible |
| Normalisation de l'état de commutation | Lecture de `on/off`, `true/false` ou `1/0` ; sortie sous forme de booléens réels, de nombres ou de texte `on/off` |
| Mise à l'échelle d'un nombre | `Wert * Faktor + Offset`, unité cible facultative ; par ex. °C → °F avec un facteur de 1,8 et un décalage (offset) de 32 |

La casse (majuscules/minuscules) et les espaces aux extrémités sont tolérés pour les états de commutation. Les états inconnus sont signalés. Seuls les paramètres correspondant au mode sélectionné sont affichés. Les modifications ne sont prises en compte qu'après avoir cliqué sur **Appliquer** ; il est possible d'annuler les changements.

## Unités et erreurs {#einheiten-und-fehler}

`23,5 °C` est dissocié en une valeur numérique, **23,5**, et une unité, **°C**. S'il ne s'agit que d'une valeur, l'unité HA (Home Assistant) définie dans `unit_of_measurement` — ou, à défaut, l'unité du widget — est utilisée. Si aucune de ces deux options n'est disponible, vous pouvez définir une unité de secours (fallback). Si une unité est déjà présente dans le texte, elle est prioritaire et n'est pas ajoutée une seconde fois lors de l'affichage. L'option **Inclure l'unité dans le texte** est facultative. La simple détection d'une unité n'entraîne aucune conversion ; pour effectuer une conversion, vous devez sélectionner explicitement **Mettre à l'échelle la valeur** (ou « Mise à l'échelle du nombre ») en précisant le facteur, le décalage (offset) et l'unité cible appropriés.

Les valeurs vides, `unknown`, `unavailable`, les nombres invalides, les états de commutation inconnus, les entrées inactives, les sources multiples et les rétroactions génèrent une erreur. Par défaut, aucune valeur n'est alors émise. L'option **Activer une valeur de remplacement en cas d'erreur** est désactivée par défaut ; si elle est activée, elle renvoie le texte de remplacement saisi. Il ne s'agit pas d'une conversion automatique en nombre ou en booléen.

Exemple : Affichage de température `23,5 °C` → Convertisseur **Texte → Nombre** → Calcul de valeur `A * 2` → Nombre **47,0**. En mode exécution (Runtime), seuls l'affichage de la température et le nombre sont visibles. Les résultats sont transmis en interne et ne sont pas automatiquement enregistrés dans Home Assistant. Un seuil simple ne dispose actuellement pas d'hystérésis ; le changement s'opère directement au niveau de la limite.
