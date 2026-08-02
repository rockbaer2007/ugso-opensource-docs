---
title: Blockly-Snippets
description: Eigene Blockly-Blöcke und JavaScript-Generatoren.
---

# Blockly

Blockly ermöglicht grafische Programmierung mit zusammensetzbaren Blöcken.

## Eigener einfacher Block

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

## JavaScript-Generator

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

## Blockly-Arbeitsbereich erstellen

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

## JavaScript aus Blöcken erzeugen

```javascript
const code = javascriptGenerator.workspaceToCode(workspace);
console.log(code);
```

::: info Schreibweise
Das Projekt heißt **Blockly**. „Blocky“ wird häufig umgangssprachlich verwendet, ist aber nicht der offizielle Name.
:::
