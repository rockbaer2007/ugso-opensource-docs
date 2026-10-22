---
title: Themes entwickeln
---
# Themes entwickeln

Themes können UIX-Variablen bereitstellen und dadurch wiederverwendbare Styling-Regeln ermöglichen.

Verteile **keine Teile der UIX-Integration separat mit einem Theme**. Verweise Nutzer zur Installation auf den [Schnellstart](../quick-start). Verwendet eine andere Custom Integration UIX, muss sie UIX als Abhängigkeit in ihrer `manifest.json` deklarieren; so wird UIX vor Nutzung vorausgesetzt. Fragen gehören in die [UIX-Diskussionen](https://github.com/Lint-Free-Technology/uix/discussions).

## Empfehlungen

- Theme-Variablen klar benennen.
- Globale Regeln sparsam halten.
- Lokale Kartenregeln nicht unnötig durch Themes erschweren.
- Dark-Mode-Werte immer mitprüfen.

## Beispiel

```yaml
my_theme:
  uix-card-yaml: |
    ha-card {
      box-shadow: none;
    }
```
