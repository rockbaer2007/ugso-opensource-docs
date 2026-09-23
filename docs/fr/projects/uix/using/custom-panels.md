---
description: Apprenez à styliser les panneaux personnalisés.
---
# Styliser les panneaux personnalisés

UIX peut styliser directement les panneaux personnalisés qui ne sont pas chargés dans une iframe. Il peut également styliser ceux qui y sont chargés. Cette fonction expérimentale doit être activée au préalable. Consultez [Extras — Styliser les panneaux personnalisés](../extras/style-custom-panels.md).

::: info Panneau personnalisé chargé dans une iframe — fonctionnement
1. Un correctif dans `ha-panel-custom` crée une version modifiée du fichier `customPanelJS` du frontend Home Assistant, utilisée par l'iframe du panneau. Elle exécute le `customPanelJS` standard, puis un module JavaScript UIX allégé.
2. Si UIX détecte qu'aucun thème n'est appliqué, il applique UIX Styling avec le thème actuellement chargé dans le frontend Home Assistant. Certains panneaux, comme [HACS](https://hacs.xyz), appliquent déjà le thème ; dans ce cas, le style UIX hérite de celui-ci.
3. La configuration des [panneaux personnalisés Home Assistant](https://www.home-assistant.io/integrations/panel_custom/) contient un champ `name:`. UIX Styling utilise ce nom pour créer la variable de thème UIX qui stylise les panneaux chargés dans une iframe.

:::
## Exemples

### Styliser les panneaux personnalisés chargés directement

Utilisez la variable de thème directe `uix-panel-custom(-yaml)`.

Exemple de style appliqué uniquement au panneau Browser Mod :

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-panel-custom-yaml: |
    browser-mod-browser-panel $: |
      browser-mod-browser-settings-card {
        --card-background-color: red;
        --primary-text-color: white;
        --secondary-text-color: whitesmoke;
        --ha-color-form-background: darkorange;
      }
```

Exemple de style appliqué à tous les panneaux personnalisés chargés directement :

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-panel-custom: |
    ha-panel-custom > * {
      --card-background-color: red;
      --primary-text-color: white;
      --secondary-text-color: whitesmoke;
      --ha-color-form-background: darkorange;
    }
```

Dans les deux cas, le résultat est identique lorsque le panneau de navigateur Browser Mod est affiché.

::: example Browser Mod browser panel styling
![Browser Mod browser panel styling](../assets/page-assets/using/custom-panel-browser-mod.png)

:::
::: info
La structure DOM de certains panneaux personnalisés peut ne pas utiliser de DOM fantôme ni d'éléments Home Assistant. Inspectez le panneau pour savoir quels éléments peuvent être thématisés.

:::
### Styliser les panneaux personnalisés chargés par iframe

Utilisez la variable de thème `uix-<name>(-yaml)`, où `name` correspond au [nom du panneau personnalisé](https://www.home-assistant.io/integrations/panel_custom/). En cas de doute, inspectez sur ordinateur le premier élément du DOM de l'iframe : le nom de sa balise indique celui du panneau.

Exemple de style pour le panneau personnalisé [HACS](https://hacs.xyz) chargé dans une iframe :

Le nom du panneau HACS est `hacs-frontend` ; sa variable de thème UIX Styling est donc `uix-hacs-frontend(-yaml)`. Le thème ci-dessous applique un dégradé arc-en-ciel à sa barre d'outils et définit des variables de style pour les cartes.

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-hacs-frontend-yaml: |
    hacs-dashboard $ hass-tabs-subpage-data-table $ hass-tabs-subpage $: |
      .toolbar {
        background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
      }
    hacs-repository-dashboard $:
      .: |
        ha-card {
          background-color: orange;
        }
      hass-subpage $: |
        .toolbar {
          background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
        }
      hass-loading-screen $: |
        .toolbar {
          background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
        }
```

::: example HACS panel styling
![HACS panel styling](../assets/page-assets/using/custom-panel-hacs.png)

:::
::: warning Mise à jour des thèmes
Les mises à jour du thème sélectionné par l'utilisateur sont appliquées pendant l'affichage du panneau personnalisé. Toutefois, si vous changez le thème de l'utilisateur pendant qu'il consulte le panneau, actualisez celui-ci pour appliquer le nouveau thème.
:::
