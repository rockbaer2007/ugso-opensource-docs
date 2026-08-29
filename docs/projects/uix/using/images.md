---
title: Bilder
description: Alles über das Styling von Entitätsbildern.
---
# Entitätsbilder stylen

UIX kann das Hintergrundbild von Entitäten ersetzen, das von folgenden Elementen angezeigt wird:

- `ha-entity-marker` für Entity-Marker in Map-Karten
- `ha-tile-icon` für Icons in Tile-Karten
- `state-badge` für State-Badges
- `ha-user-badge` für Benutzer-Badges
- `ha-person-badge` für Personen-Badges

Das Styling kann über einen [Override für eine Entität](#override-fur-eine-entitat) oder über einen [generischen Override](#generischer-override) erfolgen.

## Override für eine Entität

Definiere eine CSS-Variable in der Form `--uix-image-for-<entity_id>`. Dabei wird jeder Punkt `.` in der Entity-ID durch `_` ersetzt. Wenn ein Element für die passende Entität gerendert wird, ersetzt UIX das Hintergrundbild durch die angegebene URL.

Templates werden unterstützt.

```yaml
type: tile
entity: person.jim
uix:
  style: |
    :host {
      --uix-image-for-person_jim: /local/photos/jim.jpg;
    }
```

::: tip
- Die Variable kann auf jeder übergeordneten Ebene im DOM gesetzt werden. UIX erkennt sie über berechnete Styles am Element. Wenn die Variable nicht gesetzt ist oder die Entität nicht passt, bleibt das ursprüngliche Bild unverändert.
- Für einen Override im gesamten Home-Assistant-Frontend setze `--uix-image-for-<entity_id>` in den Theme-Variablen `uix-root(-yaml)`, `uix-config(-yaml)` und `uix-more-info(-yaml)`.
:::

## Generischer Override

Definiere die generische CSS-Variable `--uix-image` im Kontext des Bildes, das überschrieben werden soll. Das kann zum Beispiel ein Element sein, das `ha-entity-marker` in einer Map-Karte, `ha-tile-icon` in einer Tile-Karte oder `state-badge` in einer Entities-Zeile enthält.

Wenn ein unterstütztes Element in diesem Kontext gerendert wird, ersetzt UIX das Hintergrundbild durch die angegebene URL, unabhängig von der Entity-ID.

Templates werden unterstützt.

::: tip
Wenn sowohl `--uix-image` als auch `--uix-image-for-<entity_id>` definiert sind, hat `--uix-image` Vorrang.
:::
