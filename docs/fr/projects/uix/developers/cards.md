---
description: Informations pour les développeurs de cartes personnalisées.
---
# Développeurs - Cartes personnalisées

En règle générale, UIX devrait fonctionner avec toutes les cartes personnalisées.

::: tip Cas où UIX fonctionne directement
- La carte personnalisée est chargée par Home Assistant et n'est pas enfant d'une autre carte personnalisée. UIX intervient alors via `<hui-card>`.
- La carte personnalisée inclut `<ha-card>` et stocke sa configuration dans la propriété `config` ou `_config`. UIX intervient alors via `<ha-card>`.

:::
::: warning Cas où UIX nécessite du code ou un style fourni par la carte parente
- La carte personnalisée est chargée par une autre carte personnalisée qui n'utilise PAS la méthode moderne `<hui-card>` ET :
  - la carte personnalisée n'utilise PAS `<ha-card>` ; OU
  - elle utilise `<ha-card>` mais ne stocke PAS sa configuration dans `config` ou `_config`. UIX ne peut alors pas trouver la configuration `uix:` à appliquer.

:::
Si votre carte personnalisée ne fonctionne pas lorsqu'elle est utilisée avec d'autres cartes personnalisées, vous pouvez appliquer UIX directement avec `uix.applyToElement()`.

```js
customElements.whenDefined("uix-node").then((uix) => {
  uix.applyToElement(
    el, // The root element
    "type", // Determines which theme variables should apply (uix-<type>, uix-<type>-yaml)
    config, // The UIX configuration. See below
    variables, // Any variables passed on to jinja templates, preferably { config: <element configuration> }. Default: {}
    shadow // whether the styles should be based in the #shadow-root of el. Default: true
    cls // An extra class to apply to the element. Default: undefined
  )
}
```

La configuration UIX est un objet qui accepte les propriétés facultatives suivantes :

- `style` - définition du style UIX (chaîne ou objet) ;
- `theme` - nom du thème Home Assistant appliqué uniquement à la branche de cet élément (`uix.theme` est prioritaire sur le thème hérité ou actif) ;
- `class` - chaîne ou tableau de classes à appliquer à l'élément ;
- `debug` - booléen qui active le mode de débogage de l'élément (par défaut `false`).

Lorsque `theme` est défini, UIX applique directement à l'élément cible la logique `applyThemesOnElement()` du frontend Home Assistant avant de traiter les styles et macros du thème UIX.

## Exemple

Custom card javascript:

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
        <h1> This is a custom card</h1>
        <div class="my-class">
          Cette carte sert à tester la configuration UIX des cartes personnalisées.
          Elle ne contient pas d'élément <b>ha-card</b>,
          mais elle peut tout de même utiliser les styles de carte de la configuration ou du thème UIX
          lorsqu'elle est intégrée à une autre carte personnalisée.
        </div>
      </div>
    `;
  }
}

customElements.define("my-awesome-card", MyAwesomeCard);
```

With the following dashboard configuration:

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

And this theme:

```yaml
UIX Test:
  uix-theme: UIX Test
  uix-card: |
    b {
      color: orange;
    }
  dark:
```

![Output](../assets/page-assets/developers/custom-card.png)
