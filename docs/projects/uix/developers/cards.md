---
description: Informationen fuer Entwickler eigener Custom Cards
---
# Entwickler - Custom Cards

UIX sollte grundsaetzlich mit allen Custom Cards funktionieren.

!!! hint "Wo UIX ohne Zusatzcode funktioniert"
    - Die Custom Card wird direkt von Home Assistant geladen und ist nicht Kind einer anderen Custom Card. UIX patched dann ueber `<hui-card>`.
    - Die Custom Card enthaelt ein `<ha-card>` und speichert ihre Kartenkonfiguration in `config` oder `_config`. UIX patched dann ueber `<ha-card>`.

!!! warning "Wo UIX ohne weiteren Code oder Styling der Elternkarte nicht funktioniert"
    - Die Custom Card wird von einer anderen Custom Card geladen, die nicht die moderne `<hui-card>`-Methode nutzt und
    - die Custom Card nutzt kein `<ha-card>` oder
    - die Custom Card nutzt zwar `<ha-card>`, speichert die Konfiguration aber nicht in `config` oder `_config`.

    In diesem Fall kann UIX die `uix:`-Konfiguration fuer das Styling nicht finden und wendet sie nicht an.

Wenn deine Custom Card in einen solchen Fall faellt, kannst du UIX direkt mit `uix.applyToElement()` anwenden.

```js
customElements.whenDefined("uix-node").then((uix) => {
  uix.applyToElement(
    el, // Das Root-Element
    "type", // Bestimmt, welche Theme-Variablen gelten: uix-<type>, uix-<type>-yaml
    config, // Die UIX-Konfiguration, siehe unten
    variables, // Variablen fuer Jinja-Templates, vorzugsweise { config: <element configuration> }
    shadow, // Styles im #shadow-root von el anwenden. Standard: true
    cls // Zusaetzliche Klasse fuer das Element. Standard: undefined
  );
});
```

Die UIX-Konfiguration ist ein Objekt mit folgenden optionalen Eigenschaften:

- `style`: UIX-Style-Definition als String oder Objekt.
- `theme`: Home-Assistant-Theme, das nur auf diesen Element-Unterbaum angewendet wird. `uix.theme` hat Vorrang vor dem geerbten oder aktuellen Theme.
- `class`: String oder Array von Klassen, die UIX auf das Element setzt.
- `debug`: Boolean fuer den Debug-Modus dieses Elements, Standard `false`.

Wenn `theme` gesetzt ist, wendet UIX die Home-Assistant-Frontend-Logik `applyThemesOnElement()` direkt auf das Zielelement an, bevor UIX Theme-Styles und Makros verarbeitet.

## Beispiel

JavaScript einer Custom Card:

```js
const LitElement = customElements.get("ha-panel-lovelace")
  ? Object.getPrototypeOf(customElements.get("ha-panel-lovelace"))
  : Object.getPrototypeOf(customElements.get("hc-lovelace"));
const html = LitElement.prototype.html;

class MyAwesomeCard extends LitElement {
  setConfig(config) {
    this._config = config;
  }

  firstUpdated() {
    customElements
      .whenDefined("uix-node")
      .then((uix) =>
        uix.applyToElement(
          this,
          "card",
          this._config.uix,
          { config: this._config },
          true,
          "type-custom-my-awesome-card"
        )
      );
  }

  render() {
    return html`
      <div class="content">
        <h1>Das ist eine Custom Card</h1>
        <div class="my-class">
          Diese Karte testet die UIX-Konfiguration fuer Custom Cards.
          Sie besitzt kein <b>ha-card</b>, kann aber trotzdem UIX-Styles
          aus der Kartenkonfiguration oder aus dem Theme nutzen, wenn sie
          in anderen Custom Cards eingesetzt wird.
        </div>
      </div>
    `;
  }
}

customElements.define("my-awesome-card", MyAwesomeCard);
```

Dazu passende Dashboard-Konfiguration:

```yaml
type: custom:my-awesome-card
uix:
  style: |
    .content {
      padding: 0 20px 20px 20px;
    }
    h1 {
      color: red;
    }
```

Und dieses Theme:

```yaml
UIX Test:
  uix-theme: UIX Test
  uix-card: |
    b {
      color: orange;
    }
  dark:
```
