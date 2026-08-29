---
title: Ansichtshintergründe
description: Kamera, Video oder Bild als vollflächigen View-Hintergrund mit UIX-Theme-Variablen anzeigen.
---
# Ansichtshintergründe

UIX kann einen vollflächigen **Kamera-Stream**, ein **Video** oder ein **Bild** als Hintergrund hinter Home-Assistant-Dashboard-Views und Konfigurations-Panels anzeigen. Der Hintergrund wird vollständig über CSS-Variablen im Theme gesteuert und unterstützt Jinja2-Templates. So können Quellen pro View gewechselt werden, ohne eigenen Code zu schreiben.

::: info So funktioniert es
Der Styling-Patch für `ha-drawer` steuert auch den View-Hintergrund. Dadurch funktioniert diese Funktion in Dashboard-Views und in Konfigurations-Panels. Die Variablen müssen auf `:host` innerhalb des Theme-Schlüssels `uix-drawer` gesetzt werden, damit sie über `getComputedStyle(ha-drawer)` gelesen werden können. Da `ha-drawer` bei Navigation bestehen bleibt, wird das Hintergrundelement bei Wechsel zwischen Views mit gleicher Kamera, gleichem Video oder gleichem Bild wiederverwendet.
:::

## CSS-Variablen

| Variable | Beschreibung |
| --- | --- |
| `--uix-view-background-camera-entity` | Camera-Entity-ID. UIX rendert ein stummes `ha-camera-stream`, das Stream-Verbindung und Authentifizierung verwaltet. |
| `--uix-view-background-image-entity` | Eine Entity mit `entity_picture`. UIX verwaltet URL-Authentifizierung und rendert ein cover-großes Hintergrundbild. |
| `--uix-view-background-video` | Einfache Video-URL. UIX rendert `<video autoplay muted loop playsinline>`. |
| `--uix-view-background-image` | Einfache Bild-URL. UIX rendert ein cover-großes CSS-`background-image`. |
| `--uix-view-background` | Vollständiger CSS-`background`-Kurzschreibwert. Der Nutzer ist für `url()`, Größe, Position usw. verantwortlich. |
| `--uix-view-background-cover` | `view` als Standard oder `full`. Steuert die Abdeckung des Viewports. |
| `--uix-camera-position` | Position für Kamera-Hintergründe: `center`, `top`, `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right`. |
| `--uix-camera-zoom` | Zoomfaktor. Werte größer als `1` zoomen hinein, kleinere heraus. |
| `--uix-camera-pan-x` | Horizontale Verschiebung als CSS-Länge oder Prozentwert. Positive Werte verschieben den Stream nach rechts. |
| `--uix-camera-pan-y` | Vertikale Verschiebung als CSS-Länge oder Prozentwert. Positive Werte verschieben den Stream nach unten. |

Die Kamera-Variablen für Zoom und Pan können entweder auf `:host` in `uix-drawer` oder innerhalb von `uix-view-background` gesetzt werden.

**Priorität:** `camera-entity` -> `image-entity` -> `video` -> `image` -> `background`. Alle fünf Slots können gleichzeitig als unabhängige Ebenen aktiv sein.

::: tip
Für Kamera-Entity, Image-Entity, Video oder Bild muss kein `url()` angegeben werden. UIX ergänzt es bei Bedarf. Bei `--uix-view-background` muss der komplette CSS-Wert inklusive `url()` selbst angegeben werden.
:::

## Abdeckungsmodi

`--uix-view-background-cover` steuert, wie viel vom Viewport gefüllt wird.

| Wert | Beschreibung |
| --- | --- |
| `view` | Standard. Füllt nur den Inhaltsbereich, also unterhalb der Top-Bar und rechts neben der Sidebar. Die Offsets passen sich automatisch an. |
| `full` | Füllt den kompletten Viewport und liegt hinter Top-Bar und Sidebar. |

## Grundbeispiele

### Kamera-Stream als Hintergrund

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

### Video-Hintergrund

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

### Bild-Hintergrund

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.jpg;
      --uix-view-background-cover: view;
    }
```

### Background-Kurzschreibweise

Nutze `--uix-view-background`, wenn du die vollständige CSS-`background`-Kurzschreibweise brauchst, etwa für Gradients, mehrere Bilder oder `url()` mit Größe und Position.

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background: url('/local/background.jpg') center / cover no-repeat;
      --uix-view-background-cover: full;
    }
```

Auch Gradients funktionieren:

```yaml
uix-drawer: |
  :host {
    --uix-view-background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%);
  }
```

## Pro View mit Templates wechseln

Da `uix-drawer` Jinja2-Templates unterstützt und `panel` die aktuelle View beschreibt, kann die Hintergrundquelle automatisch pro View wechseln:

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      &#123;%- if panel.viewUrlPath == 'garage' -%&#125;
      --uix-view-background-camera-entity: camera.garage
      &#123;%- elif panel.viewUrlPath == 'driveway' -%&#125;
      --uix-view-background-camera-entity: camera.driveway
      &#123;%- endif -%&#125;;
      --uix-view-background-cover: view;
    }
```

Siehe [Templates](./templates) für die vollständige Dokumentation der Template-Variablen.

::: tip Template-Debug für Variablen
Um zu prüfen, welche `panel`-Variablen verfügbar sind, kann in einem Theme ein Template mit UIX-Debug und CSS-Kommentar genutzt werden. In der Browser-Konsole erscheinen dann `UIX: Template updated`-Meldungen.

```yaml
uix-drawer: |
  &#123;# uix.debug #&#125;
  &#123;&#123; '/* testing */' &#125;&#125;
```
:::

## Hintergrund mit `uix-view-background` stylen

Das Hintergrundelement selbst kann über die Theme-Variable `uix-view-background` gestylt werden. Typische Anwendungen sind Opacity, Graustufen, Blur und Helligkeit.

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

Welches Element angezeigt wird, hängt vom Hintergrundtyp ab:

| Typ | Element |
| --- | --- |
| Camera entity | `ha-camera-stream` |
| Entity image | `div.uix-bg-image` |
| Video | `video` |
| Image | `div.uix-bg-image` |
| Background shorthand | `div.uix-bg-image` |

### Kamera-Positionierung

Kamera-Hintergründe sind standardmäßig zentriert. Der Stream füllt den Container und überstehende Bereiche werden symmetrisch abgeschnitten. Mit `--uix-camera-position` lässt sich ändern, wo der Stream verankert wird.

| Wert | Beschreibung |
| --- | --- |
| `center` | Standard, horizontal und vertikal zentriert |
| `top` | Oben verankert |
| `bottom` | Unten verankert |
| `left` | Links verankert |
| `right` | Rechts verankert |
| `top-left` | Oben links |
| `top-right` | Oben rechts |
| `bottom-left` | Unten links |
| `bottom-right` | Unten rechts |

```yaml
uix-drawer: |
  :host {
    --uix-view-background-camera-entity: camera.garden;
    --uix-camera-position: top;
  }
```

### Kamera-Zoom und Pan

UIX injiziert eine Standard-Transform-Regel in jeden Kamera-Hintergrund. Damit kann der Stream über CSS-Properties gezoomt und verschoben werden. Die Variablen können in `uix-drawer` oder in `uix-view-background` gesetzt werden. Wenn beides gesetzt ist, hat `uix-drawer` Vorrang.

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-camera-zoom` | `1` | Zoomfaktor. Größer als `1` zoomt hinein, kleiner als `1` zoomt heraus. |
| `--uix-camera-pan-x` | `0%` | Horizontale Verschiebung. |
| `--uix-camera-pan-y` | `0%` | Vertikale Verschiebung. |

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

Bei 2x-Zoom kann die obere linke Bildhälfte in den Mittelpunkt geschoben werden:

```yaml
uix-drawer: |
  :host {
    --uix-view-background-camera-entity: camera.garden;
    --uix-camera-zoom: 2;
    --uix-camera-pan-x: 50%;
    --uix-camera-pan-y: 50%;
  }
```

Zoom pro View mit Templates:

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      &#123;%- if panel.viewUrlPath == 'living-room' -%&#125;
      --uix-camera-zoom: 1.8;
      --uix-camera-pan-x: -15%;
      &#123;%- endif %&#125;
    }
```

Responsive Zoom per Media Query:

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-camera-entity: camera.garden;
      --uix-camera-zoom: 1;
    }
    @media (min-width: 1280px) {
      :host {
        --uix-camera-zoom: 1.4;
        --uix-camera-pan-y: -5%;
      }
    }
```

Kamera-Position und Zoom können für unterschiedliche Seitenverhältnisse kombiniert werden:

```yaml
uix-drawer: |
  :host {
    --uix-view-background-camera-entity: camera.garden;
    --uix-camera-position: top;
  }

  @media (min-aspect-ratio: 16/9) {
    :host {
      --uix-camera-position: center;
      --uix-camera-zoom: 1.3;
    }
  }
```

### CSS-Eigenschaften von Bildhintergründen anpassen

Entity-Bilder und normale Bilder werden als `<div class="uix-bg-image">` gerendert. Standard ist `background-size: cover`, `background-position: center` und `background-repeat: no-repeat`. Über `.uix-bg-image` können diese Eigenschaften überschrieben werden.

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.png;
    }
  uix-view-background: |
    :host { opacity: 0.8; }

    .uix-bg-image {
      background-size: 300px 300px !important;
      background-repeat: repeat !important;
      background-position: top left !important;
    }
```

## Top App Bar und Sidebar transparent machen

Mit UIX Styling auf `uix-top-app-bar-fixed` können Top App Bar und Sidebar transparent gemacht werden. Weitere Konfigurations-Panels können eigene Toolbars besitzen, die zusätzlich über `uix-config` gestylt werden müssen.

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

## Lade-Spinner

Während Medien geladen werden, zeigt UIX einen rein per CSS animierten Spinner in der Mitte des Hintergrundcontainers. Der Spinner blendet automatisch aus, sobald das Medium bereit ist.

Der Spinner kann über `uix-view-background` angepasst werden. Er nutzt die Klasse `.uix-spinner` für den Ring und `.uix-spinner::after` für den animierten Bogen.

```yaml
my-theme:
  uix-theme: my-theme
  uix-drawer: |
    :host {
      --uix-view-background-image: /local/background.jpg;
    }
  uix-view-background: |
    :host { opacity: 0.7; }

    .uix-spinner::after {
      width: 120px;
      height: 120px;
    }

    .uix-spinner::after {
      border-color: rgba(0, 128, 255, 0.2);
      border-top-color: rgba(0, 128, 255, 0.9);
    }
```

## Wiederherstellung nach Tab-Wechsel

Browser pausieren WebRTC-/HLS-Streams und Videowiedergabe, wenn ein Tab lange im Hintergrund war. UIX erzeugt Kamera-Stream- und Video-Elemente automatisch neu, wenn du zum Tab zurückkehrst. Dadurch wird der Stream oder die Wiedergabe ohne manuelles Eingreifen wiederhergestellt.

Statische Bildhintergründe sind davon nicht betroffen.
