---
title: Rules
description: UIX-Broker-Interaktionen gegen Elemente, Captured Data und Browser-Identität prüfen.
---
# Rules

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

Alle Regeln einer Interaktion müssen passen, bevor Broker die Direktiven ausführt. Regeln nutzen standardmäßig den Interaction Anchor, können aber einen relativen oder absoluten Override-Anchor definieren.

Bei Interaktionen ohne `block` versucht UIX Broker einen fehlenden Regel-Anchor alle 50 ms bis zu zwei Sekunden lang erneut zu finden.

## Host-Element-Regeln

Kompakte String-Regeln nutzen den [UIX Host-Element-Pfad](../concepts/dom#hostelement-path-selection) und prüfen ihn gegen den Interaction Anchor oder einen Override-Anchor.

Unterstützt werden Tag-, Klassen-, ID-, Attribut- und Property-Selektoren.

```yaml
rules:
  - "ha-button.action-button[data-action]"
  - "{.config.entity=light.example}"
  - "{.controller=undefined}"
  - "{!.uixBrokerGuard}"
```

Diese Regeln passen, wenn der Anchor `ha-button.action-button[data-action]` ist, `config.entity` den Wert `light.example` hat, `controller` vorhanden aber `undefined` ist und `uixBrokerGuard` nicht existiert.

Die erweiterte Form wird genutzt, wenn eine Regel ein anderes Anchor-Element prüfen soll:

```yaml
rules:
  - anchor: "$ ha-dialog"
    match: "ha-dialog"

  - anchor: "&home-assistant $$ ha-automation-sidebar"
    match: "ha-automation-sidebar"

  - anchor:
      select_tree: "home-assistant $$ ha-automation-sidebar"
    match: "{._yamlMode=false}"
```

::: tip
Regel-Anchors verwenden dieselbe `select_tree`-Syntax wie Direktiven-Anchors und werden während einer nicht blockierenden Interaktion erneut gesucht.
:::

::: tip
`{.property=undefined}` passt nur, wenn die Property existiert und ihr Wert `undefined` ist. `{!.property}` passt nur, wenn die Property fehlt.
:::

## Typisierte Regeln

Typisierte Regeln haben einen `type`-Schlüssel. Unterstützt werden `browserid` und `captured`.

### Browser-Identität

Die Regel `browserid` prüft eine [Browser Mod](https://github.com/thomasloven/hass-browser_mod)-Browser-ID. Nutze `id`, `browser_id` oder `value` für die erwartete Browser-Identität.

```yaml
rules:
  - type: browserid
    id: kitchen-tablet
```

## Captured-Data-Regeln

Mit `type: captured` werden Daten geprüft, die aus dem auslösenden Event gesammelt wurden. `path` ist ein dot-separierter Optional-Chaining-Pfad relativ zu den Captured Data. Er beginnt nicht mit `@captured`.

Bei Browser- und Shortcut-Interaktionen beginnen Captured Data beim `detail`-Objekt des DOM-Events. Bei Server-Interaktionen liegen Home-Assistant-Eventdaten unter `data`. Array-Indizes werden unterstützt.

```yaml
rules:
  - type: captured
    path: data.new_state.state
    match:
      operator: ">="
      value: 20
```

Einfache Match-Werte unterstützen exakte Werte, Wildcards, reguläre Ausdrücke und numerische Vergleiche:

```yaml
rules:
  - type: captured
    path: button
    match: "save*"
  - type: captured
    path: room
    match: "/^kitchen/i"
  - type: captured
    path: count
    match: ">= 20"
```

### Erweitertes Matching

Ein Matcher-Objekt unterstützt `operator`, `value` oder `match`, `ignore_case`, `exists` sowie verschachtelte `and`-, `or`- und `not`-Kompositionen.

Unterstützte Operatoren sind `>`, `<`, `=`, `<=`, `>=`, `==`, `!=`, `contains`, `starts_with`, `ends_with` und `is_undefined`.

```yaml
rules:
  - type: captured
    path: button
    match:
      or:
        - "save*"
        - "/^submit$/i"
  - type: captured
    path: count
    match:
      and:
        - "> 0"
        - "<= 10"
  - type: captured
    path: data.value
    match:
      operator: is_undefined
      exists: true
```

`is_undefined` mit `exists: true` unterscheidet eine vorhandene Property mit Wert `undefined` von einem fehlenden Pfad. `exists: false` passt ausdrücklich auf einen fehlenden Pfad.

### Kompakte Captured-Data-Form

Für kompakte Konfigurationen können ein oder mehrere Captured-Pfade direkt in einer Objekt-Regel abgebildet werden. Jeder Eintrag muss passen. Der Prefix `@captured` bleibt nur in dieser kompakten Form erhalten.

```yaml
rules:
  - "@captured.user.role": admin
    "@captured.enabled": true
```
