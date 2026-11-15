# User guide

This guide is for beginners. Open HA Logic Studio Pro in Home Assistant, select **New project**, then choose an editor and a name. For the examples, create a toggle helper under **Settings → Devices & services → Helpers**. The examples use `input_boolean.studio_test`. Use your helper’s actual entity ID.

## Which editor should I use?

- **Function plan** for signals, timers and counters on a canvas.
- **Rules** for IF → THEN or ELSE rules.
- **Blocks A** to assemble Home Assistant automations from blocks.
- **Blocks JS** to assemble scripts from blocks and import ioBroker projects.
- **JavaScript** or **TypeScript** to write scripts.
- **HA-YAML** to edit, check and visualize automations and scripts.

## Common controls

- **Save** stores changes. Orange indicates pending edits. Gray means there is nothing to save.
- **Cancel** discards edits made since the last save and restores the saved version.
- **Test run** uses simulation in the script editors. In the function plan, you can toggle simulated inputs.
- **Play** starts the saved version in the runtime for Function plan, Blocks JS, JavaScript and TypeScript. Approved HA actions can change real entities there. **Stop** ends the run.
- **Check** shows problems before exporting or running. **Export** creates a file you can use in Home Assistant.
- **Expert mode** in the project menu shows additional editor tools. The **Log** shows output and errors for the open project.

## Editors

- [Function plan](./user-guide/function-plan)
- [Rules](./user-guide/rules)
- [Blocks A](./user-guide/blocks-a)
- [Blocks JS](./user-guide/blocks-js)
- [JavaScript](./user-guide/javascript)
- [TypeScript](./user-guide/typescript)
- [HA-YAML](./user-guide/ha-yaml)
- [Report issues and contribute](./user-guide/feedback)
