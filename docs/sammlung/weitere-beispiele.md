---
title: Weitere interessante Beispiele
description: Community- und Fremdbeispiele rund um Home Assistant, UIX und Lovelace.
---
# Weitere interessante Beispiele

Hier sammeln wir externe Praxisbeispiele, Community-Gists und interessante Ideen, die nicht direkt Teil einer Projekt- oder Übersetzungsdokumentation sind.

Diese Seite ist bewusst von den einzelnen Projektdokumentationen getrennt. So bleiben Übersetzungen nah am jeweiligen Original, während hilfreiche Zusatzideen trotzdem auffindbar bleiben.

## UIX Theme-Sammlung von Mariusthvdb

Ein umfangreiches Praxisbeispiel für UIX-Themes wird von Mariusthvdb als Gist gepflegt:

- [UIX themes von Mariusthvdb](https://gist.github.com/Mariusthvdb/ecdd6ac6776d501b09e859888b01a9c6)

Der Gist zeigt unter anderem:

- globale UIX-Theme-Variablen
- `uix-macros-yaml` mit wiederverwendbaren Makros
- Icon- und Farbregeln für Entitäten
- Sidebar-, Header-, Badge- und View-Styling
- Animationen und Zustandsfarben

::: warning Community-Beispiel
Dieses Beispiel ist kein Bestandteil der offiziellen UIX-Dokumentation und stark auf die eigene Home-Assistant-Installation des Autors zugeschnitten. Nutze es als Ideensammlung und passe Entitäten, Labels, Farben, Makros und UIX-Version an deine Installation an.
:::

Kleine Auszüge können als Orientierung dienen. Das vollständige YAML sollte direkt aus dem Gist übernommen und vor der Nutzung geprüft werden.

```yaml
theme-mods:
  uix-top-app-bar-fixed: |
    header.top-app-bar {
      background: var(--header-background);
      color: var(--text-color-off);
    }

  uix-macros-yaml: |
    power_color:
      template: >
        {% for entity in label_entities('power') %}
        --uix-icon-color-for-{{ entity.replace('.','_') }}:
        {{ 'var(--success-color)' if states(entity)|int(0) < 2500 else 'var(--alert-color)' }};
        {% endfor %}
```
