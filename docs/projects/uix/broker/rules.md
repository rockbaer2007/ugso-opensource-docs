---
title: Rules
description: UIX-Broker-Interaktionen gegen Elemente, Captured Data und Browser-Identität prüfen.
---
# Rules

::: info Versionsstand
UIX Broker gehört zur stabilen Basis 8.2.0. Die Regeln `user` und `user_is_admin` sind ab 8.3.0-beta.1 verfügbar.
:::

Alle Regeln einer Interaktion müssen passen, bevor Broker die Direktiven ausführt. Regeln nutzen standardmäßig den Interaction Anchor, können aber einen relativen oder absoluten Override-Anchor definieren.

Bei Interaktionen ohne `block` versucht UIX Broker einen fehlenden Regel-Anchor alle 50 ms bis zu zwei Sekunden lang erneut zu finden.

## Host-Element-Regeln

Kompakte String-Regeln nutzen den [UIX Host-Element-Pfad](../concepts/dom#host-element-pfad-auswahl) und prüfen ihn gegen den Interaction Anchor oder einen Override-Anchor.

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

Typisierte Regeln haben einen `type`-Schlüssel. Unterstützt werden `browserid`, `user`, `user_is_admin`, `hash`, `search`, `captured` und `panel`.

### Browser-Identität

Die Regel `browserid` prüft eine [Browser Mod](https://github.com/thomasloven/hass-browser_mod)-Browser-ID. Nutze `id`, `browser_id` oder `value` für die erwartete Browser-Identität.

```yaml
rules:
  - type: browserid
    id: kitchen-tablet
```

### Home-Assistant-Benutzer

`type: user` prüft den angemeldeten Benutzer anhand des Anzeigenamens (`hass.user.name`) oder der stabilen Benutzer-ID (`hass.user.id`). Der Anmeldename ist im Frontend-Benutzerobjekt nicht verfügbar und wird nicht unterstützt. Setze entweder `match` oder `value`. Beide verwenden dieselben Operatoren wie [Captured-Data-Regeln](#captured-data-regeln), einschließlich Wildcards, regulärer Ausdrücke und boolescher Verknüpfungen.

```yaml
rules:
  - type: user
    match: Darryn
  # Wenn bekannt, vorzugsweise die stabile ID verwenden:
  - type: user
    match: 9f1362c9e0a24d918c66d4fdcf12b001
```

Bei einem positiven Vergleich genügt ein Treffer bei Name oder ID. Ein negierter Vergleich mit `not` oder `!=` muss beide Felder ausschließen:

```yaml
rules:
  - type: user
    match:
      not: wall-panel
```

`type: user_is_admin` prüft den Administratorstatus. Ohne Vergleich bedeutet die Regel „ist Administrator“. Mit `match: false` oder `value: false` passt sie auf Nicht-Administratoren. Auch die erweiterten Matcher-Objekte werden unterstützt.

```yaml
rules:
  - type: user_is_admin
```

Nicht-Administrator mit einem Namen oder einer ID, die mit `wall-` beginnt:

```yaml
rules:
  - type: user
    match: wall-*
  - type: user_is_admin
    match: false
```

### URL-Fragment

`type: hash` prüft den Teil der Browser-URL nach `#`; ein `path` wird nicht benötigt. `match` und `value` unterstützen dieselben Vergleiche wie Captured-Data-Regeln.

```yaml
rules:
  - type: hash
    match: settings
```

Die Direktiven laufen hier nur, wenn die aktuelle URL mit `#settings` endet.

### URL-Suchparameter

`type: search` prüft einen benannten URL-Parameter. `path` gibt dessen Namen an; `match` und `value` verwenden dieselbe Vergleichssyntax wie Captured-Data-Regeln.

```yaml
rules:
  - type: search
    path: entity_id
    match: "light.kitchen*"
```

Die Regel passt nur bei einem entsprechenden `?entity_id=`-Parameter. Mit `exists: false` lässt sich ein fehlender Parameter prüfen.

## Captured-Data-Regeln

Mit `type: captured` werden Daten geprüft, die aus dem auslösenden Event gesammelt wurden. `path` ist ein dot-separierter Optional-Chaining-Pfad relativ zu den Captured Data. Er beginnt nicht mit `@captured`.

Array-Indizes können als `items.0` oder `items[0]` geschrieben werden. Für Property-Namen mit Satzzeichen funktionieren Schlüssel in Anführungszeichen und Klammern, etwa `settings['icon-color']`.

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

## Panel-Regeln

`type: panel` prüft das aktuelle UIX-Panel-Objekt. Broker ermittelt es asynchron. Es enthält dieselben `panel`-Felder wie [Templates](../using/templates), beispielsweise `fullUrlPath`, `panelUrlPath`, `viewUrlPath` und `panelComponentName`.

`path` oder sein Alias `property` ist ein dot-separierter Optional-Chaining-Pfad relativ zu diesem Objekt. `match` und `value` unterstützen alle Captured-Data-Vergleiche, einschließlich Wildcards, regulärer Ausdrücke, Zahlenvergleiche, `exists` und Verknüpfungen mit `and`, `or` und `not`.

```yaml
rules:
  - type: panel
    path: fullUrlPath
    match: "lovelace/kitchen*"
  - type: panel
    path: fullUrlPath
    match:
      operator: contains
      value: automation/edit
  - type: panel
    path: panelComponentName
    match:
      operator: "="
      value: lovelace
```

::: warning Panel-Regeln und Blocking
Eine Interaktion mit Panel-Regel darf keine `block`-Direktive verwenden. Panel-Zustände werden asynchron ermittelt; das Blockieren eines Browser-Events muss dagegen im synchronen Aufruf erfolgen. Broker überspringt solche Interaktionen und protokolliert eine Warnung.
:::
