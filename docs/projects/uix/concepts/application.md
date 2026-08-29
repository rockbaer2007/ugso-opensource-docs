---
title: Anwendung
description: Wie UI eXtension Home-Assistant-Elemente patcht und UIX auf sie anwendet.
---
# UIX-Anwendung

UIX erreicht nahezu vollständige Abdeckung der Standardkarten des Home-Assistant-Frontends und unterstützt gleichzeitig Custom Cards, die nicht den modernen Home-Assistant-Rendering-Container für Karten verwenden.

::: info Begriffe
1. **Patch/Patching**: UIX führt injizierten Code in der Elementklasse aus.
2. **Application/Applying**: UIX wendet ein `<uix-node>` auf ein Element an, meist im Shadow Root, und auf Kindpfade gemäß Selektoren.
3. **Ignore/Ignoring**: Der UIX-Patching-Code erkennt das Element, unternimmt auf Elementebene aber nichts.
:::

## Standardkarten-Struktur

::: details Beispiel mit `tile`-Karte
- UIX wird nicht direkt auf Kartenebene (`tile`) angewendet, weil dafür viele unterschiedliche CSS-Regeln nötig wären und Theming unübersichtlich würde.
- Basis-CSS läuft über `:host { }`, Kartenstyles oft über `ha-card { }`.
:::

```console
hui-card           <= UIX patcht hier
  -> tile          <= dies ist `:host` für UIX und hier wird `class` gesetzt
    -> shadowRoot  <= UIX wendet Styles hier an, `ha-card` liegt im Light DOM
      -> ha-card   <= UIX v4 patcht hier ebenfalls, ignoriert aber wegen bekannter Standardstruktur
```

## Custom-Card-Struktur: button-card als Beispiel

::: details Beispiel
- `button-card` enthält ein `div` vor `ha-card` und ist daher keine Standardkarten-Struktur.
- Da die Karte selbst weiterhin gepatcht wird, können CSS-Variablen über `:host { }` gesetzt werden.
- Ebenso können YAML-Selektorpfade genutzt werden.
- Das Legacy-`ha-card`-Patching und die Anwendung laufen auf `ha-card`-Ebene, wo `ha-card { }` funktioniert.
:::

```console
hui-card                 <= UIX patcht hier
  -> button-card         <= dies ist `:host` für UIX und hier wird `class` gesetzt
    -> shadowRoot        <= UIX wendet Styles hier an
      -> div
        -> ha-card       <= UIX patcht und wendet hier an, weil es keine Standardstruktur ist
          -> shadowRoot
```

## Custom-Card-Struktur: streamline-card mit tile

::: details Beispiel
- Da die Host-Karte weiterhin gepatcht wird, können CSS-Variablen über `:host { }` gesetzt werden.
- YAML-Selektorpfade sind ebenfalls möglich.
- Das Legacy-`ha-card`-Patching und die Anwendung für die geladene Karte laufen auf `ha-card`-Ebene, wo `ha-card { }` funktioniert.
:::

```console
hui-card                 <= UIX patcht hier
  -> streamline-card     <= `:host` für UIX, Klasse aus der UIX-Konfiguration der Host-Karte
    -> shadowRoot        <= UIX wendet Styles für die Host-Custom-Card hier an
      -> tile
        -> shadowRoot
          -> ha-card     <= UIX patcht und wendet hier für die geladene Karte an
            -> shadowRoot
```

## Hinweise

- Wrapper-Custom-Cards wie `streamlined-card` können jede Karte in `<hui-card>` kapseln. Dadurch funktionieren Home-Assistant-Funktionen wie `visibility`-Bedingungen oder die neue `disabled`-Option zuverlässiger. `expander-card` nutzt diesen Ansatz.
- Die Theme-Variable `uix-card` gilt für das neue `<hui-card>`-Patching und das Legacy-`<ha-card>`-Patching.
- Wenn Karten sowohl normal als auch über eine Custom Card wie `layout-card` geladen werden, können Themes doppelte CSS-Selektoren verwenden, um beide Strukturen zu treffen.
- Wenn ein übergeordnetes `<hui-card>`-Patch bekannt ist, kann das Theme passend formuliert werden. Bei `streamlined-card` kann etwa `*` den unbekannten Kartentyp in der Struktur matchen.
- Die Beispiele zeigen UIX an einer Karte. Ähnliche Muster funktionieren auch in Themes.

::: details Doppelte CSS-Selektoren

Der Selektor `:host(.my-class) ha-card` zielt auf Karten, die vom Frontend geladen werden. `ha-card.myclass` zielt auf Custom Cards mit abweichender Struktur oder auf Karten, die von Custom Cards geladen wurden.

```yaml
uix:
  style: |
    :host(.my-class) ha-card,
    ha-card.myclass {
      background-color: red !important;
    }
```

:::

::: details Streamlined-card-Strukturbeispiele

```yaml
uix:
  style:
    "* $": |
      ha-card {
        --card-background-color: red;
      }
```

Oder:

```yaml
uix:
  style:
    "* $ ha-card": |
      :host {
        --card-background-color: red;
      }
```

:::
