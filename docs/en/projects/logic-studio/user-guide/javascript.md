# JavaScript

Since **0.1.136**, HA write APIs return promises. For ordered execution, use `await ha.setSensorState("sensor.example", 1.5);` and then read with `ha.readState("sensor.example")`. The sensor API waits for HA confirmation and makes the confirmed value available in the readable snapshot. `await ha.callAction(...)` waits for request acceptance, not a physical device movement. Timers and explicit callback blocks remain separate continuations. 99 local tests passed; Additionally live-tested on 28 November 2026 after a full backup on HA 2026.11.3 (.193, port 80): Blocks JS state/attribute branches, writing before debug, decimal input without Enter, the previous-code warning and log clearing. Test values restored, projects and permissions preserved; examples stopped. [Live test evidence](../#zustandstrigger-reihenfolge).

## First example

This example writes a message to the log with one line of code.

1. Choose **New project → JavaScript** and replace the sample code with `ha.log('Studio-Test');`.
2. Click the test run button at the top right. You can try the code before saving it.
3. Look for `Studio-Test` in the `message` field in the **Log**. Click **Save** to keep the draft.

[![JavaScript test run showing Studio-Test in the log](/images/logic-studio/user-guide/javascript-en.png)](/images/logic-studio/user-guide/javascript-en.png)

## Features

### Completion and signatures

Start typing an API name to see suggestions and expected arguments.

### Test values and test run

Use simulated states and check the output and errors.

### Error lines

Go to the reported line in the original source and inspect the expression.

### Global functions

Export functions from a global script and select that script in the project that uses them.

### Play and autostart

Save and start with Play. Enable autostart per project if it should start after an app restart.

### Runtime log

Read log entries after an app restart. Retention is limited by age and size.

## If something goes wrong

If HA rejects an action, check the app's approved entities and actions.
