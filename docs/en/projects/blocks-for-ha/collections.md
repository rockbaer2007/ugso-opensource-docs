---
title: Math, text, lists and loops
description: Mapping Blockly and ioBroker blocks to native UGSo HA output.
---
# Math, text, lists and loops

**Since 0.1.14:** 37 additional block types, **105** in total. [All blocks with actual editor images](./blocks). The two supplied text screenshots show the same category and are considered once. These are original HA-YAML/Jinja generators; ioBroker JavaScript is not executed.

## Comparison with upstream

References: original Blockly [loops](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts), [math](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/math.ts), [text](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/text.ts) and [lists](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). ioBroker additions for [decimal precision](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_number.ts) and [text](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_text.ts) were also reviewed. The target output follows [HA template functions](https://www.home-assistant.io/template-functions/) and [HA script actions](https://www.home-assistant.io/docs/scripts/).

| Area / upstream | UGSo implementation | Differences / pending variants |
| --- | --- | --- |
| Repeat, while/until | Existing native HA repeat blocks | While tests before, until after each iteration. |
| Count from/to/step | New counting block | Fixed integer bounds, step magnitude, inclusive end on the step grid, automatically ascending/descending, at most 10000 values. Dynamic/fractional bounds remain pending. |
| For each list item | Additional named-variable block | Assigns the variable from repeat.item before each body. |
| break / continue | Pending | HA Stop ends the entire run. Local control flow needs a separate model and nested-loop tests. |
| Number, variable change | Already available | Initialize variables first; increment requires numbers. |
| Arithmetic, single-number math, trig, constants | New Math category | Root, abs, negation, ln/log10, powers; angles in degrees. Infinity is not offered. |
| Number properties | Even/odd/whole/positive/negative/divisible | Prime test remains pending. |
| Rounding / ioBroker decimal places | Shared block: normal/up/down, 0–10 places | HA/Jinja rounding rather than JavaScript Math.round. |
| Math on list | Sum, min/max, mean, median, random item | Blockly mode as a list of all most frequent values and standard deviation remain pending; HA statistical_mode alone would not have the same meaning. |
| Modulo, constrain, random | New value blocks | Negative modulo follows Jinja. Integer random has inclusive bounds and at most 10000 choices; fractions use increments of 0.00001. |
| atan2 | Additional original Blockly operation | Not visible in supplied math screenshots; not presented as an ioBroker deficiency. |
| Single/multiline text | Existing text block | Original multiline field. |
| Newline, join, append | New text blocks | LF/CRLF/CR; join with gear/+−; append assigns a new text variable value. |
| Text length/empty/contains/find/character/substring | New text blocks | 1-based indices, missing search returns 0. Inclusive substring bounds from start; substring bounds from end remain pending. |
| Case, trim, count, replace, reverse | New text blocks | Literal matching rather than regex, Unicode/Python rules. Reverse is also in original Blockly. |
| print / prompt | Existing log action; prompt pending | A browser prompt would not be an input dialog for an automation running later in HA. |
| Empty list / create with items | Existing list block with 0–100 inputs | Gear/+− changes the items. |
| Repeat item, length/empty, index, get, sublist | Existing and new list blocks | Get from start/end/first/last/random. Inclusive sublist bounds from start. |
| Set/insert/remove list item | New action blocks | New list assigned to a variable; other variables are not mutated. Combined get-and-remove value block, edits from end and random removal remain pending. |
| Split/join, sort, reverse | New list blocks | Numeric/text/case-insensitive sorting; original stays unchanged. |

## Controls and runtime values

Menu, pale flyout and colored blocks remain distinct; **Search stays last**. Math is blue-purple, text dark green, lists purple and loops green. Values connect to variables, comparisons, templates and runtime pauses. Fixed numeric trigger limits still accept number literals rather than calculated templates.

Text join has 0–100 inputs. Create variable remains in the Variables category; text/list modification blocks select that variable. Initialize it with the matching type before appending/modifying. Explicitly convert HA state strings to numbers when needed. Invalid types or fractional indices cause template errors rather than silent conversion.

Index **1** means the first item; from end, 1 means the last. Out-of-range reads return empty text or null; out-of-range list edits leave the list unchanged. Inserting at length+1 appends. A substring/sublist with start above end or below 1 returns empty. An end beyond length is truncated.

Example: count `i` from 1 to 5 by 2, with a template value containing `i` in the body log action:

```yaml
actions:
  - repeat:
      for_each: '{{ range(1, 6, 2) | list }}'
      sequence:
        - variables:
            i: '{{ repeat.item }}'
        - action: system_log.write
          data:
            level: info
            message: '{{ i }}'
```

This produces 1, 3, 5. Use distinct variables in nested loops; repeat.item always refers to the innermost iteration. Store random/time-dependent expressions in a variable first if the same value is needed in multiple places: nested templates may evaluate inputs more than once.

## JavaScript differences and persistence

- At zero decimal places, 2.5 rounds to 2 and 3.5 to 4; JavaScript Math.round differs. Up/down use ceil/floor.
- Negative modulo: −9 modulo 2 produces 1. Angles convert between degrees and HA radians.
- Text operations count Unicode code points. An emoji may use two JavaScript UTF-16 units; combining characters/graphemes may still span several code points. Title case and trim use Python/Jinja rules.
- Empty search text explicitly returns 0 for count and leaves replace unchanged. Matches do not overlap. Searching is literal and case-sensitive.
- Empty list: sum 0; other math aggregates and random item null. Numeric aggregation/sorting requires actual numbers rather than Boolean/text values. Python equality may consider 1 and true equal, unlike JavaScript reference equality.
- List modification uses copies, slices and native HA variable assignment, without list.append/pop mutation in the immutable sandbox.

Project JSON preserves shapes, fields, dropdowns, order and connected items. YAML import preserves meaning, reopening complex expressions as general templates and counting loops as native For-each with a variable assignment. YAML does not contain enough information to reconstruct original Blockly shapes uniquely.

Verified: all 37 new types through JSON/YAML, edge cases, immutable Jinja sandbox with HA math helpers, categories and text + button in the browser, app/docs builds and Docker preview. Execution against a real Home Assistant instance remains pending.
