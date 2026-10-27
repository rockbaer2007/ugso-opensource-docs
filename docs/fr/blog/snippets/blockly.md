---
title: Extraits Blockly
description: Blocs Blockly personnalisés et générateurs JavaScript.
---
<a id="blockly-snippets"></a>
<a id="statut"></a>


# Blockly {#blockly}

Blockly permet la programmation graphique à l'aide de blocs emboîtables.

## Bloc simple personnalisé {#eigener-einfacher-block}

```javascript
Blockly.Blocks['ugso_log_message'] = {
  init() {
    this.appendValueInput('MESSAGE')
      .setCheck('String')
      .appendField('Log ausgeben');

    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('Gibt eine Nachricht in der Konsole aus.');
  }
};
```

## Générateur JavaScript {#javascript-generator}

```javascript
javascriptGenerator.forBlock['ugso_log_message'] = function(block, generator) {
  const message =
    generator.valueToCode(
      block,
      'MESSAGE',
      generator.ORDER_NONE
    ) || "''";

  return `console.log(${message});\n`;
};
```

## Création d'un espace de travail Blockly {#blockly-arbeitsbereich-erstellen}

```html
<div id="blocklyDiv" style="height: 480px; width: 100%;"></div>

<xml id="toolbox" style="display: none">
  <category name="Logik" colour="210">
    <block type="controls_if"></block>
    <block type="logic_compare"></block>
  </category>

  <category name="Text" colour="160">
    <block type="text"></block>
    <block type="text_print"></block>
  </category>
</xml>
```

```javascript
const workspace = Blockly.inject('blocklyDiv', {
  toolbox: document.getElementById('toolbox'),
  trashcan: true,
  scrollbars: true
});
```

## Génération de code JavaScript à partir de blocs {#javascript-aus-blocken-erzeugen}

```javascript
const code = javascriptGenerator.workspaceToCode(workspace);
console.log(code);
```

::: info Orthographe
Le projet s'appelle **Blockly**. Le terme « Blocky » est souvent utilisé dans le langage courant, mais ce n'est pas le nom officiel.
:::
