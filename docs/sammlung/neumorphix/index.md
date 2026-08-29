---
title: NeuMorphix
description: Deutsche Kurznotiz zum NeuMorphix Home-Assistant-Theme.
---
# NeuMorphix

NeuMorphix ist ein Home-Assistant-Theme mit neumorpher Optik. Es setzt auf weiche Schatten, runde Flächen und einen leicht plastischen Look für Dashboards.

::: warning Inoffizielle Notiz
Diese Seite ist keine offizielle Dokumentation des Projekts. Sie fasst die wichtigsten Installations- und Nutzungshinweise deutsch zusammen. Das Original-Repository bleibt maßgeblich.
:::

| Feld | Wert |
| --- | --- |
| Originalprojekt | [yakidd/NeumorphixHome](https://github.com/yakidd/NeumorphixHome) |
| Geprüfter Commit | [`269c298e47b02faaac4f08c8c9dfccf49d70d860`](https://github.com/yakidd/NeumorphixHome/commit/269c298e47b02faaac4f08c8c9dfccf49d70d860) |
| Release | [`1.0.3`](https://github.com/yakidd/NeumorphixHome/releases/tag/1.0.3) |
| Lizenz | laut README: MIT |
| Kategorie | HA Dashboard -> Themes |

## Installation

NeuMorphix ist als HACS-Theme installierbar.

[![NeuMorphix in HACS öffnen](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=yakidd&repository=NeumorphixHome&category=theme)

1. HACS installieren, falls noch nicht vorhanden.
2. `card-mod` installieren, wenn die Original-Theme-Dateien genutzt werden.
3. NeuMorphix über HACS als Theme installieren.
4. Home Assistant neu starten.
5. Im Benutzerprofil oder in den Dashboard-Einstellungen eine NeuMorphix-Variante auswählen.

Für Home Assistant muss die Theme-Einbindung aktiv sein:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Für die originale card-mod-Variante wird zusätzlich die card-mod-Ressource benötigt:

```yaml
frontend:
  themes: !include_dir_merge_named themes
  extra_module_url:
    - /hacsfiles/lovelace-card-mod/card-mod.js
```

## Varianten

Das Originalprojekt liefert zwei Theme-Dateien:

- `themes/neumorphix.yaml`
- `themes/neumorphix-inset.yaml`

Darin enthalten sind sechs Theme-Varianten:

- `neumorphix-light`
- `neumorphix-dark`
- `neumorphix-claude`
- `neumorphix-light-inset`
- `neumorphix-dark-inset`
- `neumorphix-claude-inset`

`Raised` wirkt wie eine angehobene Oberfläche. `Inset` wirkt eher eingedrückt oder in die Fläche eingelassen.

## UIX-Variante

Für UIX wurde ein ergänzender Branch erstellt, der die originalen card-mod-Dateien nicht ersetzt, sondern zusätzliche UIX-Theme-Dateien hinzufügt:

- [UIX-Branch im Fork](https://github.com/rockbaer2007/NeumorphixHome/tree/experiment/uix-theme-variant)
- [Pull Request zum Originalprojekt](https://github.com/yakidd/NeumorphixHome/pull/4)

Der UIX-Branch ergänzt:

- `themes/neumorphix-uix.yaml`
- `themes/neumorphix-uix-inset.yaml`

Die zusätzlichen Theme-Namen lauten:

- `neumorphix-light-uix`
- `neumorphix-dark-uix`
- `neumorphix-claude-uix`
- `neumorphix-light-uix-inset`
- `neumorphix-dark-uix-inset`
- `neumorphix-claude-uix-inset`

Technisch wurden die zusätzlichen Dateien auf UIX-Theme-Schlüssel gemappt:

- `card-mod-theme` -> `uix-theme`
- `card-mod-root-yaml` -> `uix-root-yaml`
- `card-mod-sidebar-yaml` -> `uix-drawer-yaml`

## Hinweise

- Das Originalprojekt nennt in der README MIT als Lizenz, hat aber keine separate `LICENSE`-Datei im Repository.
- Die UIX-Variante ist als Ergänzung gedacht. Die bestehenden card-mod-Dateien bleiben unverändert.
- Bei den Inset-Varianten kann die Haupt-Einstellungsseite von Home Assistant abweichend reagieren, weil diese Oberfläche anders gerendert wird als normale Dashboards.
