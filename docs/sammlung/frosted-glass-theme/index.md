---
title: Frosted Glass Theme
description: Deutsche Kurznotiz zum Frosted Glass Theme für Home Assistant.
---
# Frosted Glass Theme

Frosted Glass Theme ist ein modernes Theme für Home Assistant. Es setzt auf transparente Karten, Weichzeichnung, abgerundete Flächen, helle und dunkle Varianten sowie optionale Lite-Versionen ohne Blur für schwächere Geräte.

::: warning Inoffizielle Notiz
Diese Seite ist keine offizielle Dokumentation des Projekts. Sie fasst die wichtigsten Installations- und Nutzungshinweise deutsch zusammen. Das Original-Repository bleibt maßgeblich.
:::

| Feld | Wert |
| --- | --- |
| Originalprojekt | [wessamlauf/homeassistant-frosted-glass-themes](https://github.com/wessamlauf/homeassistant-frosted-glass-themes) |
| Geprüfter Commit | [`8cb950369e64444bcdc068f7f90283d58f65d80d`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/commit/8cb950369e64444bcdc068f7f90283d58f65d80d) |
| Release | [`v1.3`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/releases/tag/v1.3) |
| Lizenz | [MIT](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/blob/main/LICENSE) |
| Kategorie | HA Dashboard -> Themes |

## Installation

Das Theme ist über HACS installierbar.

1. HACS installieren, falls noch nicht vorhanden.
2. `card-mod` oder `UIX` installieren.
3. Frosted Glass Theme über HACS installieren.
4. Home Assistant neu starten.
5. Im Benutzerprofil das Theme auswählen.

Direktlink:

[Frosted Glass Theme in HACS öffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=WessamLauf&repository=homeassistant-frosted-glass-themes&category=theme)

::: warning card-mod oder UIX erforderlich
Das Theme benötigt `card-mod` oder `UIX`, damit Blur- und Styling-Effekte korrekt funktionieren.
:::

## Varianten

Das Repository enthält mehrere Theme-Dateien:

- `Frosted Glass.yaml`
- `Frosted Glass Light.yaml`
- `Frosted Glass Dark.yaml`
- `Frosted Glass Lite.yaml`
- `Frosted Glass Light Lite.yaml`
- `Frosted Glass Dark Lite.yaml`

Die Lite-Varianten verzichten auf Blur-Effekte. Das ist besonders sinnvoll auf älteren Tablets, schwacher Hardware oder wenn Dropdowns durch Blur-Effekte falsch dargestellt werden.

## Theme Manager

Zum Anpassen von Farben und Hintergrundbildern gibt es ein separates Projekt:

- [Frosted Glass Theme Manager](https://github.com/wessamlauf/frosted-glass-manager)

Damit können Farben per UI gewählt, Hintergrund-URLs gesetzt und Standard- sowie Lite-Versionen erzeugt werden.

### UIX-Testvariante

Für Installationen, die UIX statt card-mod nutzen, gibt es einen getesteten UIX-Arbeitsstand als Fork:

- [Frosted Glass UIX Theme Manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager)

Diese Variante erzeugt eigene Theme-Dateien und kollidiert dadurch nicht mit den normalen Frosted-Glass-Dateinamen:

- `Frosted Glass UIX Custom.yaml`
- `Frosted Glass UIX Custom Lite.yaml`

Die Standard-Hintergründe werden lokal mitgeliefert und beim Start nach Home Assistant kopiert:

- `config/www/frosted-glass-uix/frosted-glass-light-background.jpg`
- `config/www/frosted-glass-uix/frosted-glass-dark-background.jpg`

In den erzeugten Themes werden sie über `/local/frosted-glass-uix/...` eingebunden. Dadurch ist die Standardoptik nicht von einem externen CDN abhängig.

## Bekannte Hinweise

- Text-only Markdown Cards erhalten trotzdem das Glas-/Border-Styling des Themes.
- Blur kann Dropdowns in HACS oder tieferen Home-Assistant-Menüs stören.
- `stack-in-card` kann wegen tief verschachtelter Styles schwierig sein.
- Auf leistungsschwachen Geräten sind Lite-Versionen meist die bessere Wahl.

Plain Markdown Card per `card_mod` entschärfen:

```yaml
card_mod:
  style: |
    ha-card {
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
      box-shadow: none !important;
      border: none !important;
    }
    ha-card::before {
      content: none !important;
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
    }
```
