---
title: UIX Forge
description: Überblick über UIX Forge, Molds, Foundries und Sparks.
---
# UIX Forge

UIX Forge erzeugt Home-Assistant-Elemente dynamisch. Du definierst eine `forge`-Konfiguration, ein Ziel-`element` und optional zusätzliche `sparks`, die Verhalten oder Darstellung erweitern.

Unterstützt werden die Molds `card`, `badge`, `row`, `picture-element`, `section`, `footer` und `card-feature`. Cross-Context-Molds erlauben, ein Element in einem anderen Kontext zu verwenden, zum Beispiel eine Karte als Zeile in einer Entities-Karte.

Ab **UIX 9.0.0-beta.0** ermöglicht die [geschichtete Konfiguration](./forge#layered-configuration), native Templates des eingebetteten Elements unverändert zu erhalten und darüber eine separate Forge-Konfiguration zu legen. Sie gilt für alle Molds und benötigt keinen visuellen Editor.

Für die vollständige Konfigurationsreferenz siehe [Forge-Referenz](./forge).

## Foundries

Eine **Foundry** ist eine wiederverwendbare UIX-Forge-Konfiguration. Damit kannst du `forge`, `element` und `uix` einmal definieren und an vielen Stellen wiederverwenden. Ab UIX 9.0.0-beta.0 können Foundries auch `element_base` bereitstellen; eine aufgelöste Basis aktiviert die geschichtete Konfiguration. `element_disabled_paths` bleibt ausschließlich lokal an der jeweiligen Forge-Instanz.

Mehr dazu: [Foundries](./foundries)

## Sparks

Sparks sind optionale Bausteine in `forge.sparks`. Jeder Spark hat einen `type` und eigene Optionen.

Verfügbare Sparks:

- :speech_balloon: [Tooltip](./sparks/tooltip) - Tooltip an ein Element hängen.
- :material-button-cursor: [Button](./sparks/button) - Button mit Aktionen einfügen.
- :label: [Attribute](./sparks/attribute) - Attribute hinzufügen, ersetzen oder entfernen.
- :zap: [Event](./sparks/event) - DOM-Events aufnehmen und als Template-Variablen nutzen.
- :star: [Tile Icon](./sparks/tile-icon) - `ha-tile-icon` ergänzen.
- :shield: [State Badge](./sparks/state-badge) - Status-Badge einfügen.
- :material-grid: [Grid](./sparks/grid) - CSS Grid auf Container anwenden.
- :mag: [Search](./sparks/search) - Elemente per CSS-Selektor suchen und verändern.
- :material-map: [Map](./sparks/map) - Kartenansicht bewahren sowie Touren, Verlaufsregler und Entity-Filter mit konfigurierbaren Positionen ergänzen.
- :material-lock: [Lock](./sparks/lock) - Interaktion per Sperre schützen.
- :material-star-four-points-outline: [Overlay Icon](./sparks/overlay-icon) - Icon über ein Element legen.
- :material-image-outline: [Background](./sparks/background) - Hintergrundfarbe, Bild, Video oder Kamera einfügen.
- :material-palette: [Theme](./sparks/theme) - Theme auf ein Element anwenden.
- [Formular](./sparks/form) - Home-Assistant-Formular mit optionalen Absende- und Leeren-Aktionen.
