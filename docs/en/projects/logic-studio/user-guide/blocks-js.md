# Blocks JS

## First example

The test run reads a simulated entity state and writes it to the log.

1. Choose **New project → Blocks JS**. Open **System** and drag **Log** into the workspace.
2. Drag **State of** from the same category into the open input on the log block. Select your test entity. The screenshot uses `binary_sensor.bewegung`.
3. Start a **test run** and open the **Log**. The demo shows the state and message `on`. This script only reads and logs the value.

[![Blocks JS with an entity state block and the resulting log](/images/logic-studio/user-guide/blocks-js-en.png)](/images/logic-studio/user-guide/blocks-js-en.png)

## Features

### System, Actions and Sendto

Read states, control approved targets, message scripts or query history. Dynamic inputs can use an entity ID from a loop.

### Triggers, time and timeouts

Start on state changes, sun events or schedules. Use simple and named CRON jobs, delays, intervals and stop blocks.

### Value blocks

Conversion, objects, logic, math, text, lists and colors produce values. Loops repeat operations.

### Variables and functions

Use variables for intermediate values and functions for reusable steps and return values.

### ioBroker import

In Expert mode, paste the export and check the report. Map entities explicitly and read each block's guidance.

### Imported HTTP blocks

Select an approved HA REST command for the URL, timeout and request headers. The imported POST Content-Type is shown in the block.

### Test run and Play

Use simulation first. Save before Play and check actual results in the log.

## Check an import step by step

1. Enable **Expert mode** in the project menu. In the editor, open **Expert tools → Paste ioBroker export**.
2. Paste Blockly XML or an ioBroker JavaScript export with embedded Blockly data. Check the import and read which blocks need a mapping.
3. Open the import as a project and resolve the guidance on the affected blocks. For example, select the HA REST command that defines the headers and timeout for an imported POST.
4. Save and start with a **test run**. Use **Play** for live execution, check the **log**, and press **Stop** when finished.

## If something goes wrong

Replace or adapt unsupported placeholders before running the script.
