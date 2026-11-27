---
title: Home Summary Spark
description: Festlegen, welche Entitäten in einer nativen Home-Zusammenfassung gezählt werden.
---

# Home Summary Spark

::: info Verfügbar ab UIX 9.2.0-beta.3
Entwicklungsfunktion; stabile Basis dieser Dokumentation bleibt 9.1.0.
:::

Wähle, welche Entitäten für eine native Home-Zusammenfassung wie Wartung, Licht oder Sicherheit zählen. So lässt sich beispielsweise der Batteriesensor eines alten Tablets von der Wartungszählung ausschließen.

## Einzelne Home-Summary-Karte filtern {#filter-one-home-summary-card}

Erstelle das Label in HA und weise es auszuschließenden Entitäten zu. Ergänze dann diese Card Forge im Dashboard. Die Karte behält die HA-Wartungslogik und aktualisiert sich bei Änderungen der verbleibenden Entitäten.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: home-summary
      exclude:
        - label: excluded_from_maintenance
element:
  type: home-summary
  summary: maintenance
```


Das ändert die Zählung der Karte. Ihr Klick öffnet weiterhin die normale Wartungsseite, auf der ausgeschlossene Entitäten vorkommen können. Zum Filtern beider Stellen das [vollständige Home-Dashboard-Beispiel](config.md#wrap-generated-cards) verwenden: Es hüllt erzeugte Zusammenfassungskarten ein und verknüpft eine gefilterte Unteransicht.

## Spark-Optionen {#spark-options}

Eine Card Forge kann einen Home Summary Spark verwenden und muss eine native Karte mit `type: home-summary` einhüllen. Bei einer durch eine Strategie erzeugten Karte ergänzt die Configuration-Operation [`wrap_card`](config.md#wrap-generated-cards) diesen Spark.

| Option | Typ | Standard | Bedeutung |
| --- | --- | --- | --- |
| `type` | Zeichenfolge | — | Pflichtwert `home-summary`. |
| `include` | Liste aus Filtern oder Abfragereferenzen | Alle Entitäten | Nur Entitäten zählen, die mindestens einen Eintrag erfüllen. `include: []` zählt keine. |
| `exclude` | Liste aus Filtern oder Abfragereferenzen | `[]` | Passende Entitäten ausschließen, auch wenn `include` sie gewählt hat. |

### Filter {#filters}

Einträge direkt unter `include` oder `exclude` schreiben. Es gelten dieselben Regeln wie bei [Entities-Filtern](entities.md#filters), etwa `domain`, `label` und `attributes`. Dieses Beispiel schließt Browser-Mod-Lichter und Entitäten mit dem Wartungsausschlusslabel aus.

```yaml
exclude:
  - domain: light
    integration: browser_mod
  - label: excluded_from_maintenance
```


### Entities-Spark-Filter wiederverwenden {#reuse-an-entities-spark-filter}

Benötigen mehrere Karten oder Patches dieselbe Liste, benenne einen Entities Spark und lasse `path` weg. Der Home Summary Spark liest sein Ergebnis mit `$in_entities` aus derselben Card Forge. Der folgende `forge`-Block ersetzt den des ersten Beispiels.

```yaml
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
    - type: home-summary
      exclude:
        - $in_entities: excluded_from_maintenance
```


Wenn mehrere Forges den Filter benötigen, speichere die Abfrage in einer Foundry. Jede Forge führt sie selbst aus. Siehe [Filter über eine Foundry teilen](entities.md#reuse-an-entities-foundry-query-in-another-element).

## Aktualisierungen {#updates}

Die Karte erhält weiterhin Live-Aktualisierungen für die gezählten Entitäten. UIX bündelt Filteränderungen über 500 ms. Der Filter gilt ausschließlich für diese Karte. Andere Karten, die Zielseite und Serviceaktionen wie das Ausschalten aller Lichter eines Bereichs behalten ihr normales Verhalten.




> Deutsche Bearbeitung der [kanonischen UIX-Dokumentation von Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quelle: `dev` / **9.2.0-beta.3**, Revision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), geprüft am 2026-11-27. Stabile Basis **9.1.0**, HA ab **2026.11.0**. Maßgeblich bleibt das [englische Original](https://uix.lf.technology/).
