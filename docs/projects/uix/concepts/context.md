---
description: Wie UIX-Kontexte das Verhalten in bestimmten Bereichen der Home-Assistant-Oberfläche festlegen.
---

> Übersetzt aus der [englischen UIX-Dokumentation](https://github.com/Lint-Free-Technology/uix/blob/509b2c2475ce6b574876a8353f88aedf87e7b2e3/docs/source/concepts/context.md) von Lint-Free-Technology/uix unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Geprüfter Quellstand **9.1.0-beta.2**. Stabile Basis **9.0.0**, Home Assistant ab **2026.11.0**.

# UIX-Kontexte

::: info Verfügbarkeit
UIX-Kontexte und der Kontext für Entitätsnamen sind seit **9.0.0-beta.3** verfügbar.
:::

UIX-Kontexte legen ein strukturiertes Verhalten für einen UIX-Host und alle Elemente darunter fest. So können Elemente auf ihren Platz in der Oberfläche reagieren, ohne jeweils eigene Auswahlregeln zu benötigen.

## Einen Kontext definieren

Theme-Bindungen verwenden `uix-<thing>-context-yaml` für ein beliebiges UIX-Ziel. Der Wert ist eine YAML-Liste mit Bindungen. `anchor` legt den Geltungsbereich fest. Verwende dafür dieselbe [Host-/Element-Selektorsyntax](dom.md#host-element-pfad-auswahl) wie beim UIX-Styling. Die erste passende Bindung gilt.

Ein Element, das bereits `uix:` unterstützt, kann seinen Kontext direkt über `uix.context` definieren. Die direkte Konfiguration hat auf demselben Host Vorrang vor einer passenden Theme-Bindung.

Ein Kontext gilt auch unterhalb seines Hosts. Der Kontext einer Ansicht erreicht daher ihre Karten und Zeilen. Eine Karte oder Zeile kann für ihren eigenen Teilbaum einen spezifischeren Kontext definieren.

## Kontext für Entitätsnamen

`entity_name` bestimmt die Bestandteile automatisch erzeugter Entitätsnamen. Ein vom Benutzer gesetzter Anzeigename bleibt erhalten.

### Beispiel für das Energie-Dashboard

```yaml
my-uix-theme:
  uix-theme: my-uix-theme
  uix-root-context-yaml: |
    - anchor: "&ha-panel-energy"
      entity_name:
        rules:
          - when:
              request: [parent_device, device]
            use: [entity]
```

Das Beispiel ersetzt auf dem Energie-Dashboard die Bestandteile für übergeordnetes Gerät und Gerät durch den Entitätsnamen.

### Beispiel für eine Ansicht

Eine Ansicht kann mit dem vorhandenen Ziel `view` wiederholte Gerätenamen in ihren Karten ausblenden. Eine Anfrage nach Geräte- und Entitätsnamen liefert dann nur den Entitätsnamen.

```yaml
my-uix-theme:
  uix-theme: my-uix-theme
  uix-view-context-yaml: |
    - anchor: "&hui-view"
      entity_name:
        rules:
          - when:
              request: [device, entity]
            use: [entity]
```

Eine Karte kann über `uix.context` eine spezifischere Ausnahme definieren, wenn eine Entität ihren Gerätenamen benötigt.

### Beispiel für eine Karte

Mit dem vorhandenen Ziel `card` kann eine Karte wiederholte Gerätenamen in ihren Zeilen ausblenden. Eine Anfrage nach Geräte- und Entitätsnamen liefert dann nur den Entitätsnamen. Hier passen nur Entitätskarten mit der UIX-Klasse `type-entities`.

```yaml
  uix-card-context-yaml: |
    - anchor: "&.type-entities"
      entity_name:
        rules:
          - when:
              - request: default
              - request: [device, entity]
            use: [entity]
```

### Direktes Beispiel für eine Karte

Einer Karte lässt sich ein Kontext direkt hinzufügen.

```yaml
uix:
  context:
    entity_name:
      rules:
        - when:
            - request: default
            - request:
                - device
                - entity
          use:
            - entity
```

### Regeln

`when.request` ist entweder `default` oder die exakte Liste angefragter Namensbestandteile. `when` kann mehrere Anfragen als Liste bündeln, wenn sie dasselbe Ergebnis verwenden. `use` akzeptiert dieselbe Kurzform als Liste. Zulässig sind `floor`, `area`, `parent_device`, `device` und `entity`.

```yaml
entity_name:
  rules:
    - when:
        - request: default
        - request: [device, entity]
      use: [entity]
```

Das Beispiel verwendet den Entitätsnamen sowohl für eine Standardanfrage als auch für eine Anfrage nach Geräte- und Entitätsnamen.

```yaml
entity_name:
  rules:
    - when:
        request: [parent_device, device]
      use:
        - type: device
        - type: text
          text: "-"
        - type: entity
```

Home Assistant trennt Namensbestandteile normalerweise durch Leerzeichen. Das Beispiel ergibt daher `Device - Entity`. Für eine genaue Kontrolle der Zeichensetzung lässt sich die Objektform mit einem expliziten Trennzeichen verwenden.

```yaml
entity_name:
  rules:
    - when:
        request: [parent_device, device]
      use:
        items:
          - type: device
          - type: text
            text: " — "
          - type: entity
        options:
          separator: ""
```

### Direkte Konfiguration

Ein Element, das bereits `uix:` unterstützt, kann einen Kontext für Entitätsnamen direkt definieren.

```yaml
uix:
  context:
    entity_name:
      rules:
        - when:
            request: default
          use: [entity]
```

## Fehlersuche

Wähle im Browser-Inspektor ein betroffenes Element aus und führe `uix_context($0)` in der Konsole aus. Die Ausgabe zeigt die geerbten Kontexte und bietet mit `format()` eine Funktion zum Prüfen einer konkreten Namensanfrage.

```js
uix_context($0).format("sensor.sun_next_dusk", [
  { type: "device" },
  { type: "entity" },
]);
```

Setze beim Einrichten `debug: true` im Kontext. Das Protokoll zeigt dann den angewendeten Kontext und den ersten Treffer für jede Regel für Entitätsnamen.

```yaml
uix:
  context:
    debug: true
    entity_name:
      rules:
        - when:
            request: default
          use: [entity]
```
