---
description: Learn how to display a full-screen camera stream, video, or image as a view background using UIX theme CSS variables.
---
# Arrière-plans des vues

UIX peut afficher un **flux de caméra**, une **vidéo** ou une **image** en plein écran derrière les vues de votre tableau de bord Home Assistant et les panneaux de configuration. L'arrière-plan est entièrement contrôlé par des variables CSS définies dans votre thème et prend en charge les modèles Jinja2 ; vous pouvez donc changer de source selon la vue sans code personnalisé.

::: info How it works
Le correctif de style de `ha-drawer` contrôle également l'arrière-plan de la vue, ce qui permet à cette fonction de s'appliquer aux vues du tableau de bord *et* aux panneaux de configuration. Définissez les variables sur `:host` dans la clé de thème `uix-drawer` afin qu'elles soient accessibles via `getComputedStyle(ha-drawer)`. Comme `ha-drawer` persiste pendant la navigation, l'élément d'arrière-plan est **réutilisé** entre les vues lorsque la source (vidéo ou image) est identique ; il n'est pas détruit puis recréé.

:::
## Variables CSS

| Variable | Description |
|---|---|
| `--uix-view-background-camera-entity` | Camera entity ID — UIX renders a muted `ha-camera-stream` which manages all stream connection and any authentication. |
| `--uix-view-background-image-entity` | Any entity with `entity_picture` — UIX manages any URL authentication and renders a cover-sized background image |
| `--uix-view-background-video` | Plain video URL — UIX renders a `<video autoplay muted loop playsinline>` |
| `--uix-view-background-image` | Plain image URL — UIX renders a cover-sized CSS `background-image` |
| `--uix-view-background` | Full CSS `background` shorthand value — applied directly to the background div; user is responsible for `url()`, sizing, positioning, etc. |
| `--uix-view-background-cover` | `view` (default) or `full` — controls viewport coverage (see [below](#coverage-modes)) |
| `--uix-camera-position`| Camera background position keyword — `center` (default), `top`, `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right` |
| :camera:  `--uix-camera-zoom` | Scale factor — values greater than `1` zoom in, less than `1` zoom out. |
| :camera:  `--uix-camera-pan-x` | Horizontal shift.  Accepts any CSS length or percentage. Positive values move the stream right (showing more of the left side of the camera). |
| :camera:  `--uix-camera-pan-y` | Vertical shift.  Accepts any CSS length or percentage. Positive values move the stream down (showing more of the top of the camera). |

:camera: The camera CSS zoom and pan CSS variables can be set either on `:host` inside `uix-drawer` or inside `uix-view-background`. See [camera positioning](#camera-positioning) and [camera zoom and pan](#camera-zoom-and-pan).

**Priority order**: `camera-entity` → `image-entity` → `video` → `image` → `background`.  All five slots can be active simultaneously as independent layers.

::: tip
Il n'est pas nécessaire d'entourer de `url()` les variables CSS d'entité caméra, d'entité image, de vidéo ou d'image pour les arrière-plans de vue. UIX ajoute `url()` si nécessaire. Vous **devez** toutefois le fournir si vous utilisez `--uix-view-background`.

:::
## Modes de couverture

La variable `--uix-view-background-cover` contrôle la partie de la fenêtre occupée par l'arrière-plan.

| Value | Description |
|---|---|
| `view` *(default)* | Background fills only the **content area** — offset below the top bar (`--header-height`) and to the right of the sidebar.  The offset adjusts automatically when the sidebar is resized or toggled. NOTE: For any config panels like developer tools which have double header height, the view will not compensate beyond `--header-height`. |
| `full` | Background fills the **entire viewport**, sitting behind the top bar and sidebar. |

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

::: tip Use template debug to check variables
Pour vérifier quelles variables `panel` sont disponibles, utilisez un modèle dans votre thème avec le débogage UIX et un commentaire CSS. Dans la console de votre navigateur, repérez `UIX: Template updated`, puis développez `variables` et enfin `panel`.
```yaml
uix-drawer: |
  {# uix.debug #}
  {{ '/* testing */' }}
```

:::
## Styliser l'arrière-plan avec `uix-view-background`

UIX styling for the view background is available using the theme variables `uix-view-background`.  This lets you style the background content using the `uix-view-background` theme key — exactly like any other UIX theme target.

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

| Type | Element |
| - | - |
| Camera entity | `ha-camera-stream` |
| Entity image | `div.uix-bg-image` |
| Video | `video` |
| Image | `div.uix-bg-image` |
| Background shorthand | `div.uix-bg-image` |

### Positionnement de la caméra

Par défaut, les arrière-plans de caméra sont **centrés** : le flux remplit le conteneur et le débordement dû au rapport hauteur/largeur est rogné symétriquement de chaque côté. Utilisez `--uix-camera-position` pour modifier le point d'ancrage du flux en cas de débordement :

| Value | Description |
|---|---|
| `center` *(default)* | Centred horizontally and vertically |
| `top` | Anchored to the top edge |
| `bottom` | Anchored to the bottom edge |
| `left` | Anchored to the left edge |
| `right` | Anchored to the right edge |
| `top-left` | Anchored to the top-left corner |
| `top-right` | Anchored to the top-right corner |
| `bottom-left` | Anchored to the bottom-left corner |
| `bottom-right` | Anchored to the bottom-right corner |

```yaml
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-camera-position: top;
    }
```

### Zoom et déplacement de la caméra

UIX injects a default transform rule into every camera background so that you can zoom and pan the stream by setting CSS custom properties.  The variables can be set in **`uix-drawer`** (alongside `--uix-view-background-camera-entity`, for convenience) or in **`uix-view-background`** (for more targeted control).  When set in both places the `uix-drawer` value takes precedence.

| Variable | Default | Description |
|---|---|---|
| `--uix-camera-zoom` | `1` | Scale factor — values greater than `1` zoom in, less than `1` zoom out. |
| `--uix-camera-pan-x` | `0%` | Horizontal shift.  Accepts any CSS length or percentage. Positive values move the stream right (showing more of the left side of the camera). |
| `--uix-camera-pan-y` | `0%` | Vertical shift.  Accepts any CSS length or percentage. Positive values move the stream down (showing more of the top of the camera). |

**Centering**: `--uix-camera-position: center;` ensures zooming always scales from the centre of the stream — so the camera stays centred at every zoom level.  The pan variables shift from that centred position in screen space, independently of the current zoom level (10% pan is always a 10% screen-space shift).

**Everything in one place (position + zoom + camera entity in `uix-drawer`):**

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

**Zoom in and centre on the upper-left quadrant:**

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

**Per-view zoom with templates:**

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

**Responsive zoom with media queries:**

CSS variables set inside a `@media` block apply only when that query matches, so you can zoom in on large screens while leaving the camera at natural size on smaller screens:

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

[Example](https://github.com/ngocjohn/hass-config/blob/40288532f57eacbbf9dd38b14f20b31ea615a9f5/config/themes/graphite-auto.yaml#L758-L768) as shared by `@ngocjohn` on Home Assistant Community Forum.

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
