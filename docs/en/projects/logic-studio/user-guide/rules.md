# Rules

## First example

In the wizard, choose a state trigger, your helper and `on`. Add a THEN action to turn on a second helper. Export the YAML and check it in HA.

The Rules editor shows the palette on the left and the IF, THEN and ELSE sections in the workspace.

![Rules editor with the palette and rule branches](/images/logic-studio/0.1.60-rules-test-193.png)

## Features

### Wizard and palette

The wizard guides you through the rule. Search the palette or drag an item into the matching section.

### Triggers

Choose a state change with from/to, attribute and duration, a numeric threshold, fixed or helper time, sun with offset, MQTT, HA event, HA start, area or label.

### Conditions

Check a state, number, attribute, time or weekday. AND requires all checks, OR any, and NOT reverses a check.

### Triggered by

Assign IDs such as `first` and `second` and use the ID as a condition to select THEN or ELSE.

### Template

In Expert mode, add a native HA template whose result decides whether the condition passes.

### Actions and branches

Add actions in order. Choose a target and parameters, add a delay, wait for a state, call a script or send a notification.

### YAML and Rules JSON

Use YAML in HA and Rules JSON to reopen the rule in the editor.

## If something goes wrong

A threshold triggers again after the value leaves the range and re-enters.
