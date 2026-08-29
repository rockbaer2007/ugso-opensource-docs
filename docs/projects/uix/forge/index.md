---
title: UIX Forge
description: Überblick über UIX Forge, Molds, Foundries und Sparks.
---
# UIX Forge

UIX Forge erzeugt Home-Assistant-Elemente dynamisch. Du definierst eine `forge`-Konfiguration, ein Ziel-`element` und optional zusätzliche `sparks`, die Verhalten oder Darstellung erweitern.

Unterstützte Elementtypen sind unter anderem Karten, Badges, Zeilen, Abschnitte und Picture-Elements. Cross-Context-Molds erlauben, ein Element in einem anderen Kontext zu verwenden, zum Beispiel eine Karte als Zeile in einer Entities-Karte.

Für die vollständige Konfigurationsreferenz siehe [Forge-Referenz](./forge).

## Foundries

Eine **Foundry** ist eine servergespeicherte UIX-Forge-Vorlage. Damit kannst du `forge`, `element` und `uix` einmal definieren und an vielen Stellen wiederverwenden. Lokal überschreibst du nur die Werte, die sich unterscheiden.

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
- :material-map: [Map](./sparks/map) - Kartenansicht stabil halten.
- :material-lock: [Lock](./sparks/lock) - Interaktion per Sperre schützen.
- :material-star-four-points-outline: [Overlay Icon](./sparks/overlay-icon) - Icon über ein Element legen.
- :material-image-outline: [Background](./sparks/background) - Hintergrundfarbe, Bild, Video oder Kamera einfügen.
- :material-palette: [Theme](./sparks/theme) - Theme auf ein Element anwenden.
