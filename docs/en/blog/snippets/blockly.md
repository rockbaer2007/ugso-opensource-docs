---
title: Blockly Snippets
description: Custom Blockly blocks and JavaScript generators.
---

# Blockly

Blockly enables graphical programming with composable blocks.

## Simple Custom Block

```javascript
Blockly.Blocks['ugso_log_message'] = {
  init() {
    this.appendValueInput('MESSAGE')
      .setCheck('String')
      .appendField('Log message');

    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('Outputs a message to the console.');
  }
};
```

## JavaScript Generator

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

## Create a Blockly Workspace

```html
<div id="blocklyDiv" style="height: 480px; width: 100%;"></div>

<xml id="toolbox" style="display: none">
  <category name="Logic" colour="210">
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

## Generate JavaScript from Blocks

```javascript
const code = javascriptGenerator.workspaceToCode(workspace);
console.log(code);
```

::: info Spelling
The project is called **Blockly**. "Blocky" is sometimes used informally, but
it is not the official name.
:::
