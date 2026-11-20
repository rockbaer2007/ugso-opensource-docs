---
description: Afficher un flux caméra, une vidéo ou une image en arrière-plan avec les variables CSS du thème UIX.
---
# Arrière-plans des vues

UIX peut afficher un **flux de caméra**, une **vidéo** ou une **image** en plein écran derrière les vues de votre tableau de bord Home Assistant et les panneaux de configuration. L'arrière-plan est entièrement contrôlé par des variables CSS définies dans votre thème et prend en charge les modèles Jinja2 ; vous pouvez donc changer de source selon la vue sans code personnalisé.

::: info Fonctionnement
Le correctif de style de `ha-drawer` contrôle également l'arrière-plan de la vue, ce qui permet à cette fonction de s'appliquer aux vues du tableau de bord *et* aux panneaux de configuration. Définissez les variables sur `:host` dans la clé de thème `uix-drawer` afin qu'elles soient accessibles via `getComputedStyle(ha-drawer)`. Comme `ha-drawer` persiste pendant la navigation, l'élément d'arrière-plan est **réutilisé** entre les vues lorsque la source (caméra, vidéo ou image) est identique ; il n'est pas détruit puis recréé.

:::
## Variables CSS

| Variable | Description |
|---|---|
| `--uix-view-background-camera-entity` | Identifiant d’entité caméra : UIX affiche un `ha-camera-stream` sans son, qui gère la connexion au flux et son authentification. |
| `--uix-view-background-image-entity` | Entité possédant `entity_picture` : UIX gère l’authentification de l’URL et affiche l’image en couvrant l’arrière-plan. |
| `--uix-view-background-video` | URL vidéo simple : UIX affiche un élément `<video autoplay muted loop playsinline>`. |
| `--uix-view-background-image` | URL d’image simple : UIX affiche une `background-image` CSS couvrant l’arrière-plan. |
| `--uix-view-background` | Valeur complète du raccourci CSS `background`, appliquée directement au conteneur. Vous devez fournir `url()`, la taille, la position et les autres propriétés nécessaires. |
| `--uix-view-background-cover` | `view` (par défaut) ou `full` : détermine la zone couverte (voir [ci-dessous](#coverage-modes)). |
| `--uix-camera-position`| Position du flux caméra : `center` (par défaut), `top`, `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right`. |
| :camera:  `--uix-camera-zoom` | Facteur d’échelle : une valeur supérieure à `1` agrandit le flux ; une valeur inférieure à `1` le réduit. |
| :camera:  `--uix-camera-pan-x` | Décalage horizontal, exprimé par une longueur CSS ou un pourcentage. Une valeur positive déplace le flux vers la droite et montre davantage son côté gauche. |
| :camera:  `--uix-camera-pan-y` | Décalage vertical, exprimé par une longueur CSS ou un pourcentage. Une valeur positive déplace le flux vers le bas et montre davantage sa partie supérieure. |

:camera: Les variables CSS de zoom et de déplacement de la caméra peuvent être définies sur `:host` dans `uix-drawer` ou dans `uix-view-background`. Consultez le [positionnement](#camera-positioning) et le [zoom et déplacement de la caméra](#camera-zoom-and-pan).

**Ordre de priorité** : `camera-entity` → `image-entity` → `video` → `image` → `background`. Les cinq emplacements peuvent être actifs simultanément en tant que couches indépendantes.

::: tip
Il n'est pas nécessaire d'entourer de `url()` les variables CSS d'entité caméra, d'entité image, de vidéo ou d'image pour les arrière-plans de vue. UIX ajoute `url()` si nécessaire. Vous **devez** toutefois le fournir si vous utilisez `--uix-view-background`.

:::
<span id="coverage-modes"></span>

## Modes de couverture

La variable `--uix-view-background-cover` contrôle la partie de la fenêtre occupée par l'arrière-plan.

| Valeur | Description |
|---|---|
| `view` *(par défaut)* | L’arrière-plan remplit uniquement la **zone de contenu**, sous la barre supérieure (`--header-height`) et à droite de la barre latérale. Le décalage s’adapte automatiquement au redimensionnement ou au masquage de la barre latérale. Pour les panneaux à double en-tête, tels que les outils de développement, la compensation reste limitée à `--header-height`. |
| `full` | L’arrière-plan remplit **toute la fenêtre**, derrière la barre supérieure et la barre latérale. |

## Exemples de base

### Arrière-plan de flux caméra

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-view-background-cover: view;
    }
  uix-view-background: |
    :host { opacity: 0.7; }
```

### Arrière-plan vidéo

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-video: /local/background.mp4;
      --uix-view-background-cover: full;
    }
  uix-view-background: |
    :host { opacity: 0.5; }
```

### Arrière-plan d'image

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.jpg;
      --uix-view-background-cover: view;
    }
```

### Raccourci d'arrière-plan

Utilisez `--uix-view-background` lorsque vous avez besoin de la propriété raccourcie CSS `background` complète : dégradés, images multiples ou `url()` avec taille et position dans une seule valeur. Vous devez fournir la valeur complète.

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background: url('/local/background.jpg') center / cover no-repeat;
      --uix-view-background-cover: full;
    }
```

Les dégradés fonctionnent également :

```yaml
  uix-drawer: |
    :host {
      --uix-view-background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%);
    }
```

## Changer par vue avec des modèles

Comme le style `uix-drawer` prend en charge les modèles Jinja2 et que la variable de modèle `panel` indique la vue actuelle, vous pouvez changer automatiquement la source d'arrière-plan :

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      {%- if panel.viewUrlPath == 'garage' -%}
      --uix-view-background-camera-entity: camera.garage
      {%- elif panel.viewUrlPath == 'driveway' -%}
      --uix-view-background-camera-entity: camera.driveway
      {%- endif -%};
      --uix-view-background-cover: view;
    }
```

Consultez [Modèles](./templates.md) pour la documentation complète des variables de modèle.

::: tip Vérifier les variables avec le débogage des modèles
Pour vérifier quelles variables `panel` sont disponibles, utilisez un modèle dans votre thème avec le débogage UIX et un commentaire CSS. Dans la console de votre navigateur, repérez `UIX: Template updated`, puis développez `variables` et enfin `panel`.
```yaml
uix-drawer: |
  {# uix.debug #}
  {{ '/* testing */' }}
```

:::
## Styliser l'arrière-plan avec `uix-view-background`

La clé de thème `uix-view-background` permet d’appliquer des styles au contenu de l’arrière-plan de la vue, comme pour les autres cibles de thème UIX.

Les usages courants comprennent le réglage de l'opacité, du niveau de gris, du flou et de la luminosité :

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
    }
  uix-view-background: |
    :host {
      opacity: 0.6;
      filter: grayscale(30%) blur(2px);
    }
```

Pour ajuster la position ou d'autres propriétés de l'arrière-plan de la vue, vous pouvez modifier les paramètres d'affichage du conteneur hôte ainsi que ceux de l'élément affiché. Cet élément dépend du type indiqué dans le tableau ci-dessous.

| Type | Élément |
| - | - |
| Entité caméra | `ha-camera-stream` |
| Image d’une entité | `div.uix-bg-image` |
| Vidéo | `video` |
| Image | `div.uix-bg-image` |
| Raccourci d’arrière-plan | `div.uix-bg-image` |

<span id="camera-positioning"></span>

### Positionnement de la caméra

Par défaut, les arrière-plans de caméra sont **centrés** : le flux remplit le conteneur et le débordement dû au rapport hauteur/largeur est rogné symétriquement de chaque côté. Utilisez `--uix-camera-position` pour modifier le point d'ancrage du flux en cas de débordement :

| Valeur | Description |
|---|---|
| `center` *(par défaut)* | Centré horizontalement et verticalement |
| `top` | Ancré au bord supérieur |
| `bottom` | Ancré au bord inférieur |
| `left` | Ancré au bord gauche |
| `right` | Ancré au bord droit |
| `top-left` | Ancré dans le coin supérieur gauche |
| `top-right` | Ancré dans le coin supérieur droit |
| `bottom-left` | Ancré dans le coin inférieur gauche |
| `bottom-right` | Ancré dans le coin inférieur droit |

```yaml
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-camera-position: top;
    }
```

<span id="camera-zoom-and-pan"></span>

### Zoom et déplacement de la caméra

UIX insère une règle de transformation par défaut dans chaque arrière-plan caméra. Vous pouvez ainsi agrandir et déplacer le flux avec des propriétés CSS personnalisées, définies dans **`uix-drawer`** (à côté de `--uix-view-background-camera-entity`) ou dans **`uix-view-background`** (pour un réglage plus ciblé). Si les deux emplacements définissent une même variable, la valeur de `uix-drawer` est prioritaire.

| Variable | Par défaut | Description |
|---|---|---|
| `--uix-camera-zoom` | `1` | Facteur d’échelle : au-dessus de `1`, le flux est agrandi ; en dessous, il est réduit. |
| `--uix-camera-pan-x` | `0%` | Décalage horizontal en longueur CSS ou pourcentage. Une valeur positive déplace le flux vers la droite et montre davantage son côté gauche. |
| `--uix-camera-pan-y` | `0%` | Décalage vertical en longueur CSS ou pourcentage. Une valeur positive déplace le flux vers le bas et montre davantage sa partie supérieure. |

**Centrage** : `--uix-camera-position: center;` fait varier l’échelle depuis le centre du flux ; la caméra reste centrée à chaque niveau de zoom. Les variables de déplacement décalent cette position dans l’espace de l’écran, indépendamment du zoom : un déplacement de 10 % reste un déplacement de 10 % à l’écran.

**Tout au même endroit : position, zoom et entité caméra dans `uix-drawer` :**

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-camera-position: center;
      --uix-camera-zoom: 1.5;
      --uix-camera-pan-x: -10%;
    }
```

**Agrandir et centrer sur le quadrant supérieur gauche :**

Avec un zoom de 2×, le flux fait deux fois la taille du conteneur. Pour afficher le centre du quadrant supérieur gauche, déplacez l'image vers la droite et vers le bas de 50 % des dimensions du conteneur :

```yaml
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-camera-zoom: 2;
      --uix-camera-pan-x: 50%;
      --uix-camera-pan-y: 50%;
    }
```

**Adapter le zoom à la vue avec des modèles :**

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      {%- if panel.viewUrlPath == 'living-room' -%}
      --uix-camera-zoom: 1.8;
      --uix-camera-pan-x: -15%;
      {%- endif %}
    }
```

**Adapter le zoom à la taille de l’écran avec les requêtes média :**

Les variables CSS d’un bloc `@media` ne s’appliquent que si sa condition est remplie. Vous pouvez donc agrandir le flux sur les grands écrans et conserver sa taille naturelle sur les petits :

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      /* No zoom on small / mobile screens */
      --uix-camera-zoom: 1;
    }
    /* Zoom in on large screens (≥ 1280 px wide) */
    @media (min-width: 1280px) {
      :host {
        --uix-camera-zoom: 1.4;
        --uix-camera-pan-y: -5%;
      }
    }
```

Vous pouvez combiner ce réglage avec `--uix-camera-position` pour les écrans de proportions différentes :

```yaml
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      /* Portrait / mobile: show the top of the feed */
      --uix-camera-position: top;
    }

    /* Landscape / desktop: centre the feed and zoom in slightly */
    @media (min-aspect-ratio: 16/9) {
      :host {
        --uix-camera-position: center;
        --uix-camera-zoom: 1.3;
      }
    }
```

### Personnaliser les propriétés CSS de l'arrière-plan d'image

Les arrière-plans **d'image issue d'une entité** et **d'image simple** sont rendus dans un `<div class="uix-bg-image">`. Par défaut, ce div utilise `background-size: cover; background-position: center; background-repeat: no-repeat`. Vous pouvez remplacer ces propriétés ou en ajouter d'autres avec le sélecteur `.uix-bg-image` :

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.png;
    }
  uix-view-background: |
    :host { opacity: 0.8; }

    /* Tile the image instead of stretching it to cover */
    .uix-bg-image {
      background-size: 300px 300px !important;
      background-repeat: repeat !important;
      background-position: top left !important;
    }
```

## Rendre la barre d'application et la barre latérale transparentes

Vous pouvez appliquer un style UIX à `uix-top-app-bar-fixed` pour rendre transparentes la barre supérieure de l'application et la barre latérale. Certains panneaux de configuration possèdent leur propre barre d'outils ; vous devrez peut-être également la styliser avec `uix-config`.

[Exemple](https://github.com/ngocjohn/hass-config/blob/40288532f57eacbbf9dd38b14f20b31ea615a9f5/config/themes/graphite-auto.yaml#L758-L768) partagé par `@ngocjohn` sur le forum de la communauté Home Assistant.

```yaml
  uix-top-app-bar-fixed: |
    :host {
      --mdc-top-app-bar-fixed-box-shadow: none;
      --sidebar-background-color: #ffffff00;
      --app-header-background-color: #ffffff00;
      --app-header-backdrop-filter: blur(2em);
      --app-header-border-bottom: none;
    }
```

## Indicateur de chargement

Pendant le chargement du média, UIX affiche au centre du conteneur d'arrière-plan un indicateur animé réalisé uniquement en CSS. Il disparaît automatiquement lorsque le média est prêt : démarrage du flux caméra, lecture possible de la vidéo ou chargement de l'image terminé.

Vous pouvez personnaliser cet indicateur avec `uix-view-background` : la classe `.uix-spinner` désigne l'anneau et le pseudo-élément `.uix-spinner::after` l'arc animé.

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.jpg;
    }
  uix-view-background: |
    :host { opacity: 0.7; }

    /* Make the spinner larger */
    .uix-spinner::after {
      width: 120px;
      height: 120px;
    }

    /* Change spinner colour to match your theme */
    .uix-spinner::after {
      border-color: rgba(0, 128, 255, 0.2);
      border-top-color: rgba(0, 128, 255, 0.9);
    }
```

## Récupération de la visibilité d'un onglet

Les navigateurs suspendent les flux WebRTC/HLS et la lecture vidéo lorsqu'un onglet reste longtemps en arrière-plan. Lorsque vous revenez dans l'onglet, UIX recrée automatiquement les éléments de flux caméra et de vidéo afin de rétablir le flux ou la lecture sans intervention manuelle.

Les arrière-plans constitués d'images statiques ne sont pas concernés.
