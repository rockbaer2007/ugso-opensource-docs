# Blocks A

## First example

The example turns on a hallway light when the motion sensor changes to `on`.

1. Choose **New project → Blocks A** and name the project. The workspace contains an **Automation** block.
2. Open **Triggers** and drag the state trigger into **When**. The screenshot uses `binary_sensor.flur_bewegung` and the state `on`. Select your own test helper or sensor.
3. Open **Actions** and drag a switch action into **Then**. The example uses `light.flur` and **turn on**. You can target a second test helper instead. Leave **Only if** empty for this example.
4. Click the flag icon to check the blocks. When the check passes, choose **Open as HA YAML** and review `triggers` and `actions` before exporting.

[![Blocks A with a state trigger in When and a switch action in Then](/images/logic-studio/user-guide/blocks-a-en.png)](/images/logic-studio/user-guide/blocks-a-en.png)

## Features

### Palette and connectors

Pick blocks by their role. Connector shapes indicate where a value or an action fits.

### Triggers and conditions

A trigger starts the automation. A condition can check whether the other helper is off.

### Actions

Stack actions in the order they should run.

### HA selectors

Choose entities, actions, devices, areas, labels or floors. Check the corresponding ID in YAML.

### HA-YAML draft

Open the generated automation as a draft that identifies its source project.

### Export

Check the YAML and use it in HA. Test the trigger and inspect the automation trace there.

## If something goes wrong

If a selector is empty, check the connected HA system for matching entries.
