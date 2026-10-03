---
title: SVG LineBox Math
---

# SVG LineBox Math

From Studio **0.1.138**, the enlarged dialog contains **four independent calculations**. Each has its own enabled state, formula or average mode, output list and result preview. Existing projects retain their previous calculation and outputs as calculation 1; calculations 2–4 and all internal input handoffs start disabled.

## Four calculations and output assignments

![Expanded SVG LineBox Math dialog with separate calculations and internal handoff to input C](/images/grafik-visual-studio/linebox-math-four-dialog.png)

First configure the port roles at the top. For each enabled calculation, enter the destination letters under **Outputs (e.g. E,F;H)**. Commas, semicolons and whitespace separate the letters; lowercase letters are also accepted. `E,F;H` assigns the same result to outputs E, F and H. Each port must be an active **Output**. An input letter produces a warning, and conflicting assignments cannot be applied. An output can belong to only one calculation. Unassigned outputs provide no value.

## Reusing results internally

Each calculation has an initially disabled **Pass result internally to input** option. Enabling it lets you select one active input letter under **Internal input**. Other calculations can then use that letter in their formulas. The internal handoff replaces external line values at the selected port; disabling it restores those connected line values. Only one internal result can supply a given input. Dependencies are resolved independently of calculation numbering.

Example with A = 150 and B = 30:

| Calculation | Formula | Outputs | Internal handoff | Result |
| --- | --- | --- | --- | --- |
| 1 | `A + B` | `E,F;H` | enabled → input C | 180 |
| 2 | `C * 2` | `G` | disabled | 360 |
| 3 | `A - B` | `I` | disabled | 120 |
| 4 | disabled | — | disabled | — |

A calculation must not pass its result back to an input on which it depends. Direct or indirect feedback and duplicate assignments are reported and rejected before applying changes. **Average of all occupied inputs** also includes internally assigned inputs; passing that average back into its own input set therefore creates feedback.

Arithmetic errors such as division by zero stop the affected calculation and its dependents. Independent calculations continue. Missing values matter only when the calculation uses that input; average mode requires valid values at all occupied inputs. The dialog displays per-calculation messages. Small screens use scrolling and stack calculation panels vertically.

## Basics and a single-calculation example

The following screenshot shows the original Studio 0.1.137 dialog. Its calculation is retained as calculation 1 in the expanded dialog.

![SVG LineBox Math calculation dialog with ports A–P, input values and an average of 90](/images/grafik-visual-studio/linebox-math-dialog.png)

The screenshot shows the German calculation dialog with **Average of all occupied inputs** selected. Input **A** already contains the sum of its two lines (100 + 50 = **150**), while input **B** supplies **30**, producing **90**. **G** is configured as an output and passes this result onward. Green letters A, B and G identify connected ports; orange letters have no connected line. An unconnected input shown as `—` is excluded from the average. This calculation mode disables the formula field but retains its previous expression.

From Studio 0.1.137, **SVG LineBox Math** is also available under **HA Grafik – Spezial**. Its square remains visible in both editor and runtime. Its 16 ports run clockwise from A at the top-left: A–E across the top, E–I down the right, I–M across the bottom and M–A up the left. Each side has three additional points between its corners. Connected editor markers are green and free markers orange, with contrasting letters; runtime hides the markers. Lines enter perpendicular to the edges. A/E enter from above, I/M from below; the remaining side ports enter through their respective edges.

Select the widget and open **Edit calculation**. Set the square size (96–2000 px), each letter's **Off**, **Input** or **Output** role, and the calculation. New docking points start disabled; assigning an input or output role in the dialog enables that point. The **Docking points** section can also enable all points together.

**Custom formula** supports `+`, `-`, `*`, `/`, parentheses, numbers with decimal points and letters A–P. Multiplication and division take precedence over addition and subtraction. Example: `(A + B) / C`. Multiple lines connected to one input first sum their signed values: A receiving 100 and 50 becomes 150; B receiving 30 gives 120 for `A - B`. **Average of all occupied inputs** counts each occupied input port once, producing `(150 + 30) / 2 = 90`; unconnected ports are excluded.

The preview shows input values and the result. Outputs pass the result internally to SVG-Lines, downstream LineBoxes and widgets with numeric docking input, without an additional HA entity. Missing or invalid connected values, unconnected formula inputs, division by zero and feedback cycles stop output. The widget then shows `—` with an error hint. Formulas are parsed without executing JavaScript. Changes apply only after **Apply** and support Undo.
