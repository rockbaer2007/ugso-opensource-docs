---
title: Badge Spark
description: Text- und Symbol-Badges mit Theme-Farben, Animation und optionaler Platzierung.
---
# Badge Spark

Der Spark `badge` fügt ein `uix-badge` vor oder nach einem Element im Forge-Ergebnis ein. Er verwendet Home Assistants angepasste Web-Awesome-Badge-Basis und übernimmt die Theme-Farben. UIX registriert dabei keinen globalen `wa-badge`.

Diese kompakte Referenz basiert auf der [Originalseite im Release 8.4.0](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/forge/sparks/badge.md), unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) von Lint-Free-Technology/uix. Weitere bebilderte Beispiele stehen in der [englischen Dokumentation](https://uix.lf.technology/forge/sparks/badge/).

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: badge
      after: hui-tile-card $ ha-tile-icon
      content: 3
      variant: danger
      pill: true
element:
  type: tile
  entity: light.bed_light
```

## Konfiguration

| Schlüssel | Typ | Standard | Bedeutung |
| --- | --- | --- | --- |
| `type` | string, erforderlich | — | `badge` |
| `after` | string | Bei Blank Cards `uix-forge-blank-card $ div.content`, sonst `""` | Referenzelement; normalerweise Einfügen danach. Eines von `after`/`before` angeben, sofern kein Blank-Card-Standard greift. |
| `before` | string | — | Referenzelement; normalerweise Einfügen davor. |
| `content` | string / number | `""` | Inhalt als Text, kein HTML. |
| `variant` | string | `brand` | `brand`, `neutral`, `success`, `warning`, `danger` |
| `appearance` | string | `accent` | `accent`, `filled`, `outlined`, `filled-outlined` |
| `pill` | boolean | `false` | Vollständig abgerundete Form. |
| `attention` | string | `none` | `none`, `pulse`, `bounce`. Bei `pulse` verwenden `accent`/`filled` die Füllfarbe, die anderen Darstellungen die Rahmenfarbe. |
| `placement` | string | Automatisch bei `ha-button`/`ha-tile-icon`: `top-end`; sonst nicht gesetzt | Position am Element beziehungsweise am Elternelement, siehe unten. |
| `start_icon` / `end_icon` | string | — | MDI-Symbol vor/nach dem Inhalt. |
| `style` | object | — | Flache Zuordnung von CSS-Eigenschaften zu Text- oder Zahlenwerten; inline am Badge. |

Nur der erste Treffer des Selektors wird verwendet. Für ein Badge in der Ecke einer Tile Card `ha-tile-icon` wählen, nicht das den restlichen Zeilenplatz belegende `ha-tile-info`.

## Platzierung

Automatische Platzierung gibt es nur für `ha-button` und `ha-tile-icon`: jeweils oben am logischen Ende (`top-end`). Bei `ha-button` liegt das Badge im Button; bei `ha-tile-icon` im dokumentierten Standard-Slot mit Home Assistants kompakten Badge-Abständen. `after`/`before` wählt hier das Ziel und nicht die Einfügereihenfolge.

Ein von einem Button Spark erzeugter `display: contents`-Wrapper wird erkannt; das Badge wird am enthaltenen `ha-button` platziert. Die eingebaute Button Card `hui-button-card` enthält dagegen keinen `ha-button` und bekommt keine automatische Platzierung.

Bei allen anderen Zielen bleibt das Badge ohne `placement` ein benachbartes Element. Mit `placement` liegt es am Rand des **Elternelements**. UIX misst oder verändert das Ziel dabei nicht. Bei mehreren sichtbaren Kindern bezieht sich die Position auf den gesamten Elterncontainer.

Zulässige Werte: `top`, `top-start`, `top-end`, `bottom`, `bottom-start`, `bottom-end`, `left`, `left-start`, `left-end`, `right`, `right-start`, `right-end`.

Platzierte Badges verwenden standardmäßig `var(--ha-font-size-xs)` und `0.25em 0.5em` Padding. Offsets akzeptieren Längen und Prozentwerte. Bei `right`, `top-end` und `bottom-end` gleicht `--uix-badge-offset-x: -50%` die halbe Ecküberlappung aus; bei `left`, `top-start` und `bottom-start` entsprechend `50%`. Kombinationen wie `calc(-50% - 20px)` sind möglich.

## CSS-Variablen

Am Badge, einem Vorfahren oder in seiner `style`-Map setzen. Die Variablen gelten auch für Broker-Badges.

| Variable | Standard | Wirkung |
| --- | --- | --- |
| `--uix-badge-font-size` | `max(var(--wa-font-size-3xs, var(--ha-font-size-xs)), 0.75em)`; platziert: `var(--ha-font-size-xs)` | Schriftgröße. |
| `--uix-badge-font-weight` | `var(--wa-font-weight-semibold)` | Schrift-/Symbolgewicht. |
| `--uix-badge-padding` | `0.375em 0.625em`; platziert: `0.25em 0.5em` | Innenabstand. |
| `--uix-badge-min-width` | Platziert: `calc(1.5em + 2px)` | Mindestbreite inklusive Standardrahmen von je 1 px. |
| `--uix-badge-max-width` | `none` | Maximalbreite. |
| `--uix-badge-overflow` | `visible` | Überlauf; mit Maximalbreite z. B. `hidden` oder `clip`. |
| `--uix-badge-color` | Web-Awesome-Füllfarbe | Hintergrundfarbe. |
| `--uix-badge-content-color` | Web-Awesome-Inhaltsfarbe | Text-/Symbolfarbe. |
| `--uix-badge-border` | Web-Awesome-Rahmen | Vollständiger CSS-Rahmen, z. B. `1px solid rgb(255 255 255 / 50%)`. |
| `--uix-badge-border-color` | Web-Awesome-Rahmenfarbe | Rahmenfarbe; fällt auf gesetztes `--uix-badge-color` zurück. |
| `--uix-badge-box-shadow` | `none` | Statischer Schatten. |
| `--uix-badge-attention-color` | Füll- oder Rahmenfarbe der Darstellung | Farbe des pulsierenden Rings. |
| `--uix-badge-color-hover` | Normale Hintergrundfarbe | Hintergrund bei Hover. |
| `--uix-badge-content-color-hover` | Normale Inhaltsfarbe | Text/Symbole bei Hover. |
| `--uix-badge-border-color-hover` | Normale Rahmenfarbe | Rahmen bei Hover. |
| `--uix-badge-attention-color-hover` | Normale Aufmerksamkeitsfarbe | Pulsierender Ring bei Hover. |
| `--uix-badge-pointer-events` | Platziert: `auto` | `none` lässt Zeigerereignisse durch und deaktiviert Hover. |
| `--uix-badge-z-index` | `auto`; platziert: `1` | Ebenenreihenfolge. |
| `--uix-badge-offset-x` | `0px` | Horizontaler Versatz; positiv nach rechts. |
| `--uix-badge-offset-y` | `0px` | Vertikaler Versatz; positiv nach unten. |

Alle Farbvariablen akzeptieren CSS-Farben einschließlich transparenter `rgba()`- und moderner `rgb()`-Werte. Bei `attention: pulse` bleibt der statische Schatten erhalten; UIX ergänzt den wachsenden Ring. Hover-Farben greifen bei platzierten Badges nur direkt über dem Badge.

## Beispiel: Platzierung an einer Button Card

Die Button Card füllt hier ihren Elterncontainer. Explizites `placement` positioniert das Badge am Container, ohne den internen DOM der Karte zu verändern.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: badge
      after: hui-button-card
      content: 3
      variant: danger
      pill: true
      placement: top-end
      style:
        "--uix-badge-offset-x": -6px
        "--uix-badge-offset-y": 6px
        "--uix-badge-font-size": 24px
element:
  type: button
  entity: light.bed_light
```

Weitere Originalbeispiele zeigen Status-Badges neben `ha-tile-info` mit `flex: 1`, Template-gesteuerte Aufmerksamkeit, Badges an Button Sparks und eine zentrierte Blank Card.
