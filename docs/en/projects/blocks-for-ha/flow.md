---
title: Timeouts, objects, logic and loops
description: Comparing ioBroker, original Blockly and native HA control flow.
---
# Timeouts, objects, logic and loops

This page describes the 18 additions in 0.1.13 (68 block types at that time). The current total is **105**, including the additional [math, text, list and loop blocks in 0.1.14](./collections).

Version **0.1.13** adds 18 blocks, bringing the total to **68 block types**. [Images and functions](./blocks#flow-objects-and-lists-added-in-0-1-13). The comparison uses the actual ioBroker JavaScript adapter [timeout](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_timeout.ts), [object](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_object.ts), [logic](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_logic.ts) and [switch](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_switch.ts) definitions. Similar appearance does not imply identical execution. ioBroker JavaScript is not imported.

## Timeouts

| ioBroker | UGSo Blocks for HA | Difference |
| --- | --- | --- |
| Pause with ms/sec/min | **Pause**, ms/seconds/minutes/hours and connected duration | Native HA delay; the current sequence waits. No browser blocking. |
| Execute named timeout, fixed/calculated delay | **Pause**, followed by actions | Sequential HA steps; no independent callback or named JavaScript handle. |
| Stop timeout | **Stop HA script** for a separately started script; **Stop this run** for the current sequence | Stop terminates this entire run, not a selected JavaScript timeout. |
| Timeout handle value | No handle block | Use existing script/timer helper actions. Starting a timer helper does not run an embedded callback. |
| Execute interval every … | **Repeat while/until** with **Pause** in the body | Sequential: execution time plus pause determines the interval. No setInterval or overlapping ticks. |
| Stop cyclic execution | Change the loop condition or stop a separate HA script | Stop this run also stops outer loops; it is not a local break. |
| Interval handle value | No handle block | A separately started script can be stopped using script.turn_off. |
| Additional UGSo controls | **Wait until**, counted repetition, for-each | Native HA controls, timeout continuation checkbox and optional error termination. |

**Wait until** generates wait_template with a required timeout. With the continuation checkbox off, the run stops when the timeout expires. With it on, the next steps also run if the condition was not met. Use entity-dependent conditions: templates depending only on time/now() are not continuously updated during wait_template. HA provides wait.completed afterwards, accessible through the template block. [HA waits and repeats](https://www.home-assistant.io/docs/scripts/).

**While** checks before each iteration; **until** checks afterwards and runs at least once. Add a pause in the body to avoid a tight loop. Millisecond delays are minimum waits, not real-time guarantees. Restarting HA terminates active delays/waits. Use a separate timer/trigger strategy for persistent scheduling. [Timer helpers](https://www.home-assistant.io/integrations/timer/).

Constant duration: 0–86400 seconds with an explicit unit. Constant count: 1–10000 whole iterations. Connected variables/templates must produce valid runtime numbers; HA validates them during execution. Constant editor limits are not guaranteed runtime limits for templates.

## Objects

| ioBroker | UGSo block | Behavior |
| --- | --- | --- |
| New object with gear | **New object** with gear and +/− | 0–100 attributes, unique names, arbitrary values including nested objects/lists. |
| Set object attribute | **Set attribute in variable** | Reassigns a previously initialized HA object variable to a new dictionary. Other variable copies are unchanged. |
| Delete attribute | **Remove attribute from variable** | New dictionary without the key; an absent key leaves the contents unchanged. |
| Object has attribute | **Object has attribute** | Boolean test for a dictionary key. |
| Object attributes | **Object attributes** | List of keys, usable in a for-each loop. |
| Read attribute, under ioBroker System | **Attribute of object** | Key lookup instead of dot access; missing key returns null. Names such as keys/items work. |

These objects are local values within an automation run. They do not create entities, modify HA entity attributes or represent ioBroker datapoint definitions. The setter uses a variable selector to identify the assignment target. Initialize it with **New object**, a dictionary template or **JSON to object** first. Other types cause a runtime template error.

The [immutable Jinja sandbox](https://jinja.palletsprojects.com/en/stable/sandbox/) forbids direct mutation through update/pop. UGSo therefore constructs dictionary copies and reassigns them. No JavaScript mutation or HA system access is involved.

## Logic and original Blockly

Original [Blockly logic definitions](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/logic.ts) cover if/else-if/else, a fixed if/else variant, comparisons, AND/OR, NOT, Boolean, null and conditional values. UGSo already provides these: **If** under Actions, values under **Logic**, and expandable AND/OR/NOT groups under Conditions and now also Logic. Connection shapes and editing come from the original Blockly library; UGSo generates HA YAML/Jinja.

| ioBroker extension | UGSo | Semantics |
| --- | --- | --- |
| Expandable AND/OR | Existing group, also under Logic | 1–100 Boolean inputs, +/− and gear for reordering. |
| Switch/case/action | **Case selection** | 1–100 cases with +/− and gear, optional populated default body. First match wins; no JavaScript fallthrough. |
| min ≤ value ≤ max | **Range comparison** | Independently strict/inclusive bounds. No automatic string-to-number conversion; use **To number** for sensor/template values. |
| If empty, fallback | **Fallback value**, two modes | Default null/undefined preserves zero, false and empty text. Empty/false/zero mode also replaces empty lists/dictionaries. |

ioBroker's fallback uses JavaScript OR, where empty arrays/objects are truthy. Jinja/Python considers them false. The additional null mode preserves valid numeric/Boolean values. Sensor states unknown/unavailable are strings, not null, and are not automatically replaced.

Case comparisons use HA/Jinja equality; Boolean and numeric comparisons can differ from JavaScript switch. The test expression is evaluated for each checked HA branch. Store changing values in a variable first and use it as the case input when every case should compare the same snapshot.

## Loops and lists

Original [Blockly loops](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts) now map to **Repeat count**, **while/until** and **For each item**. **Create list**, **List length** and **List is empty** follow the [original list blocks](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). These also exist in ioBroker categories outside the three screenshots; they are not presented as exclusive gaps in ioBroker.

Create list supports 0–100 arbitrary items with gear/+−. For each requires a list. The current item and 1-based index are available as HA repeat.item and repeat.index through a template block. Length/empty require lists rather than strings or dictionaries; invalid runtime types can raise template errors.

```yaml
actions:
  - variables:
      data: '{{ {"attribute1": "old"} }}'
  - variables:
      data: '{{ dict((data if data is mapping else none), **{"attribute1": "new"}) }}'
  - repeat:
      count: 3
      sequence:
        - delay:
            milliseconds: 1000
        - action: system_log.write
          data:
            message: '{{ repeat.index }}'
            level: info
```

## Persistence and pending features

Project JSON preserves block shapes, row order and attribute names. YAML opens pauses, waits, stop and repeat directly as dedicated blocks. Cases reopen as the existing If/choose block. Complex object/list/logic values reopen as general templates. YAML behavior is preserved; original block shapes cannot be reconstructed uniquely. Since 0.1.39, combined duration mappings, literal for_each lists and supported additional HA options are preserved. [Extended flows and Jinja](./advanced).

Periodic triggers, timer.finished and parallel branches are now supported. Named timers use native HA timer actions; local break/continue semantics remain pending. Fixed integer counting loops and list editing are added in [0.1.14](./collections). **Stop this run** is explicitly not exported as break/continue. Dedicated entity state/attribute value blocks remain separate tasks. Original Blockly core has no ioBroker timeout engine or the corresponding ioBroker object blocks; these are adapter extensions.

Verified: model/YAML/project round trips, invalid input rejection, runtime values in an immutable Jinja sandbox, browser categories, mutator and undo. Testing against a real HA instance remains pending.
