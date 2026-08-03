---
title: ioBroker Blockly
description: Introduction to Blockly in the ioBroker JavaScript adapter with an official starter example.
---

# ioBroker Blockly

Blockly is the graphical script editor of the **ioBroker JavaScript adapter**.
Automations are built from blocks without having to write all JavaScript code by
hand.

::: info Official documentation
This page only gives a short introduction. The complete description of all
blocks and more examples are available in the official ioBroker documentation.
:::

## Official Sources

- [ioBroker.javascript - official repository](https://github.com/ioBroker/ioBroker.javascript)
- [German JavaScript adapter documentation](https://github.com/ioBroker/ioBroker.javascript/tree/master/docs/de)
- [Complete Blockly documentation](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md)

## Example 1: Switch a Data Point Based on Another Data Point

The official starter example shows a typical motion detection workflow:

- A motion data point is used as the trigger.
- On a state change, a light data point is controlled.
- The current value of the motion detector is passed to the light data point.
- Motion turns the light on.
- No motion turns the light off again.

[![Official ioBroker Blockly example 1](https://raw.githubusercontent.com/ioBroker/ioBroker.javascript/master/docs/de/img/getting_started_1_de.png)](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

<small>
Image source and rights note: The image comes from the official
<a href="https://github.com/ioBroker/ioBroker.javascript" target="_blank" rel="noopener">ioBroker.javascript repository</a>.
Rights and license terms follow the project and license published there.
</small>

## Required Blockly Blocks

### 1. Trigger

Use the **If object** block from the **Trigger** section.

Select the motion detector data point there.

### 2. Control Data Point

Insert the **Control** block from the **System** section.

Select the light data point as the target.

### 3. Use the Current Value

Insert **Value of object ID** into the control block.

Select the motion data point again. The light then uses the current true/false
state of the motion detector.

## Simplified Flow

```text
When the motion detector changes
    set the state of the light
    to the current value of the motion detector
```

## Import Blockly

The official documentation provides the full importable XML code directly under
**Example 1**:

[Open example 1 with Blockly XML](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

Copy the XML code there and paste it into the Blockly editor through the import
function.

## More Official Examples

The official documentation also contains:

- **Example 2:** Turn on a light on motion and turn it off again after ten
  minutes without further motion.
- **Example 3:** Send an email when the outside temperature exceeds a threshold.

[View all official Blockly examples](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#getting-started)

## Own Blockly Posts in the Blog

For custom examples, this structure is recommended:

1. describe the task
2. list required object IDs
3. add a screenshot of the Blockly structure
4. provide exported Blockly XML code
5. explain adjustments and requirements

Screenshots are stored in the documentation project here:

```text
docs/public/images/blog/
```

Embedding in a post:

```md
![ioBroker Blockly](/images/blog/my-blockly.png)
```

::: warning
Object IDs from examples must always be adapted to your own ioBroker system.
:::
