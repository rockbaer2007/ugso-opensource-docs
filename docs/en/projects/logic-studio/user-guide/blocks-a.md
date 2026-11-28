# Blocks A

**0.1.136 scope:** The new state trigger and automatic confirmed write order apply to **Blocks JS**. Blocks A YAML retains its native event bridge. Both sensor variants remain available; permissions and saved projects are retained. Field commits without Enter and **Clear log** are shared Studio UI features. 99 local tests passed; Additionally live-tested on 28 November 2026 after a full backup on HA 2026.11.3 (.193, port 80): Blocks JS state/attribute branches, writing before debug, decimal input without Enter, the previous-code warning and log clearing. Test values restored, projects and permissions preserved; examples stopped. [Live test evidence](../#zustandstrigger-reihenfolge).

**0.1.135:** All 51 direct entity fields in 285 registered Blocks A/JS blocks were checked for HA selection. The new multi-selector and compact change triggers affect Blocks JS. Existing structured HA target fields, lists and saved mappings in Blocks A are retained. 68 Node tests and 12 server tests passed; no HA live test for this version.

## Set sensor state {#sensorzustand-setzen}

### Enter decimal values directly {#sensor-dezimalzahl}

Since **0.1.134**: Choose **System → Set sensor state · Decimal number**, select a sensor and enter the value directly. The default is `0.5`; enter values such as `33.25` using a decimal point. Values are not rounded to integers and survive saving and reloading. The existing value-input block remains available. WRITE permission and sensor attributes are handled in the same way. Blocks A requires the running Studio app.

**Verified:** 72 local tests plus, after backup on HA 2026.11.3, `0.5` and `33.25` through Blocks JS Play and the generated and inspected Blocks A event data. Both fields were confirmed after reloading; settings and attributes were retained.

From **0.1.133**, **System** includes **Set sensor state**:

1. Select an existing `sensor.*` using HA-style entity selection.
2. Connect a number, text or calculation block to the value input (state length: at most 255 characters).
3. Permit this sensor under **WRITE – individual targets** (`runtime_write_entities`) in the app configuration. Preserve existing entries. READ alone is insufficient.
4. Choose **Check blocks → Open as HA YAML**. Review and install the automation in Home Assistant yourself.

Example generated action:

```yaml
actions:
  - event: logic_studio_set_sensor_state
    event_data:
      entity_id: sensor.example
      state: 43
```

The running Studio app receives the event and checks WRITE. Without the app, it is not processed. No general EVENT permission is required for this internal input. Errors appear in the app log; successfully firing an event does not confirm that the write succeeded.

The block retains unit, device class and other attributes. It behaves like **Developer Tools → States**, controls no device and creates no persistent sensor. The owning integration may replace the value later. YAML previews perform no writes.

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
