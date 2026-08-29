---
title: Frosted Glass Theme Manager
description: Hinweise zum Frosted Glass Theme Manager und zur getesteten UIX-Testvariante.
---
# Frosted Glass Theme Manager

Der Frosted Glass Theme Manager ist eine Home-Assistant-Custom-Integration zum Erzeugen angepasster Frosted-Glass-Theme-Dateien. Farben und Hintergrundbilder können über die Home-Assistant-Oberfläche gesetzt werden.

::: warning Inoffizielle Notiz
Diese Seite ist keine offizielle Dokumentation des Projekts. Das Original-Repository bleibt maßgeblich.
:::

| Feld | Wert |
| --- | --- |
| Originalprojekt | [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager) |
| Fork mit UIX-Testvariante | [rockbaer2007/frosted-glass-manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager) |
| Pull Request | [wessamlauf/frosted-glass-manager#15](https://github.com/wessamlauf/frosted-glass-manager/pull/15) |
| Kategorie | HA Integrationen |

## Original-Manager

Der originale Manager erzeugt Frosted-Glass-Theme-Dateien für die normale Nutzung mit card-mod.

[![Frosted Glass Theme Manager in HACS öffnen](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wessamlauf&repository=frosted-glass-manager&category=integration)

Repository:

- [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager)

## UIX-Testvariante

Für Installationen, die UIX statt card-mod nutzen, gibt es einen getesteten UIX-Arbeitsstand als Fork.

[![Frosted Glass UIX Theme Manager in HACS öffnen](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=frosted-glass-manager&category=integration)

Repository:

- [Frosted Glass UIX Theme Manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager)

Die UIX-Testvariante nutzt eine eigene Home-Assistant-Integrationskennung:

- `frosted_glass_uix_manager`

Sie erzeugt eigene Theme-Dateien und kollidiert dadurch nicht mit den normalen Frosted-Glass-Dateinamen:

- `Frosted Glass UIX Custom.yaml`
- `Frosted Glass UIX Custom Lite.yaml`

Die Standard-Hintergründe werden lokal mitgeliefert und beim Start nach Home Assistant kopiert:

- `config/www/frosted-glass-uix/frosted-glass-light-background.jpg`
- `config/www/frosted-glass-uix/frosted-glass-dark-background.jpg`

In den erzeugten Themes werden sie über `/local/frosted-glass-uix/...` eingebunden. Dadurch ist die Standardoptik nicht von einem externen CDN abhängig.

## Hinweis

Die UIX-Testvariante ist bereits praktisch getestet, bleibt aber eine experimentelle Variante. Für allgemeine Fragen zum Originalprojekt sollte weiterhin das Original-Repository genutzt werden.
