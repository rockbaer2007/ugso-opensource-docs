---
title: Frosted Glass Theme
description: Deutsche Kurznotiz zum Frosted Glass Theme fuer Home Assistant.
---
# Frosted Glass Theme

Frosted Glass Theme ist ein modernes Theme fuer Home Assistant. Es setzt auf transparente Karten, Weichzeichnung, abgerundete Flaechen, helle und dunkle Varianten sowie optionale Lite-Versionen ohne Blur fuer schwaechere Geraete.

::: warning Inoffizielle Notiz
Diese Seite ist keine offizielle Dokumentation des Projekts. Sie fasst die wichtigsten Installations- und Nutzungshinweise deutsch zusammen. Das Original-Repository bleibt massgeblich.
:::

| Feld | Wert |
| --- | --- |
| Originalprojekt | [wessamlauf/homeassistant-frosted-glass-themes](https://github.com/wessamlauf/homeassistant-frosted-glass-themes) |
| Gepruefter Commit | [`8cb950369e64444bcdc068f7f90283d58f65d80d`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/commit/8cb950369e64444bcdc068f7f90283d58f65d80d) |
| Release | [`v1.3`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/releases/tag/v1.3) |
| Lizenz | [MIT](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/blob/main/LICENSE) |
| Kategorie | HA Dashboard -> Themes |

## Installation

Das Theme ist ueber HACS installierbar.

1. HACS installieren, falls noch nicht vorhanden.
2. `card-mod` oder `UIX` installieren.
3. Frosted Glass Theme ueber HACS installieren.
4. Home Assistant neu starten.
5. Im Benutzerprofil das Theme auswaehlen.

Direktlink:

[Frosted Glass Theme in HACS oeffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=WessamLauf&repository=homeassistant-frosted-glass-themes&category=theme)

::: warning card-mod oder UIX erforderlich
Das Theme benoetigt `card-mod` oder `UIX`, damit Blur- und Styling-Effekte korrekt funktionieren.
:::

## Varianten

Das Repository enthaelt mehrere Theme-Dateien:

- `Frosted Glass.yaml`
- `Frosted Glass Light.yaml`
- `Frosted Glass Dark.yaml`
- `Frosted Glass Lite.yaml`
- `Frosted Glass Light Lite.yaml`
- `Frosted Glass Dark Lite.yaml`

Die Lite-Varianten verzichten auf Blur-Effekte. Das ist besonders sinnvoll auf aelteren Tablets, schwacher Hardware oder wenn Dropdowns durch Blur-Effekte falsch dargestellt werden.

## Theme Manager

Zum Anpassen von Farben und Hintergrundbildern gibt es ein separates Projekt:

- [Frosted Glass Theme Manager](https://github.com/wessamlauf/frosted-glass-manager)

Damit koennen Farben per UI gewaehlt, Hintergrund-URLs gesetzt und Standard- sowie Lite-Versionen erzeugt werden.

## Bekannte Hinweise

- Text-only Markdown Cards erhalten trotzdem das Glas-/Border-Styling des Themes.
- Blur kann Dropdowns in HACS oder tieferen Home-Assistant-Menues stoeren.
- `stack-in-card` kann wegen tief verschachtelter Styles schwierig sein.
- Auf leistungsschwachen Geraeten sind Lite-Versionen meist die bessere Wahl.

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
