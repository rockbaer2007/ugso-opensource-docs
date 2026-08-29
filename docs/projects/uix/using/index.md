---
title: UIX Styling
description: UI eXtension Styling in Home Assistant verwenden.
---
# UIX Styling verwenden

UIX Styling erlaubt CSS-Anpassungen an fast allen sichtbaren Elementen der Home-Assistant-Oberfläche. Du kannst Karten, Zeilen, Badges, Icons, Bilder, Abschnitte, Ansichten und Theme-Variablen gezielt anpassen.

## Themen

- :bar_chart: [Karten stylen](./cards)
- :bulb: [Entitäten, Badges, Elemente und Marker stylen](./entities)
- :red_circle: [Icons stylen](./icons)
- :adult: [Entitätsbilder stylen](./images)
- :white_square_button: [Abschnittshintergründe](./section-backgrounds)
- :film_frames: [Ansichtshintergründe mit Kamera, Video oder Bild](./view-backgrounds)
- :clipboard: [Templates](./templates)
- :art: [Themes](./themes)
- :hammer_and_pick: [Weitere Optionen](./other)

## Grundprinzip

UIX-Konfiguration wird meist direkt in YAML unter `uix:` geschrieben:

```yaml
uix:
  style: |
    ha-card {
      border-radius: 12px;
    }
```

Je nach Element kann UIX andere DOM-Ziele ansprechen, verschachtelte Shadow-Roots erreichen und Templates auswerten.
