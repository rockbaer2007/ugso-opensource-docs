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

## Connect Home Assistant to ioBroker and VIS 2 over MQTT {#mqtt-vis2-helper}

This original UGSo example supplements the Blockly introduction: the **MQTT-Client for Home Assistant** forwards selected entities to an external MQTT broker. The **ioBroker JavaScript helper 0.1.34** shown here prepares them for VIS 2 and offers an optional flat layout with short names. Replace the complete helper and retain your settings to use the new option.

::: warning JavaScript, not a Blockly import
Paste the complete script into the **ioBroker JavaScript adapter** as JavaScript. It does not belong in Home Assistant or the Blockly XML importer. The existing Blockly examples below remain independent.
:::


### New in 0.1.36: retain settings across updates {#settings-persistence-0136}

**Saved app settings now survive the Home Assistant Supervisor regenerating its options file during an update.** This includes the related-measurements checkbox, the MQTT layout for new entities, other saved app settings and credentials. The app stores them independently in its private `/data/mqtt-settings.json` file. MQTT path assignments remain in `/data/mqtt-routes.json`; existing points and VIS-2 references are unchanged.

**One-time upgrade from 0.1.35 or earlier:** Export settings in the app before updating. If they have already been reset during the first upgrade, import that backup afterwards or select both options again once and click **Save and connect**. Already lost settings cannot be reliably reconstructed; additional measurements are never enabled without your selection.

Prefer editing these settings in the app. Actual Supervisor configuration changes are merged on restart; unchanged Supervisor defaults do not reset app choices. To explicitly return an app choice to its default, select and save it in the app. Existing settings backups remain usable and still exclude passwords and private TLS keys. The JavaScript helper remains **0.1.34**; no further helper replacement is required for this fix.

Background: Supervisor manages `/data/options.json`; the private `/data` directory provides persistent storage for the app. [Official HA documentation](https://contributors.home-assistant.io/apps/reference/environment/).


### New in 0.1.34: flat MQTT paths for new entities only {#mqtt-layout-0134}

Under **Transmission and TLS → MQTT structure for new entities**, select **Flat with short names** and **Save and connect**. The existing structure remains the default. This preference applies to manually selected entities and label members first encountered afterwards, including optional device measurements.

Known entities keep their existing paths. Assignments persist in `/data/mqtt-routes.json` and are included in exported settings backups. Removing and reselecting a label, renaming, restarting or updating reuses the assigned path. On the first upgrade, existing selections and recorded topics are preserved; the existing label selection is pinned during its first successful reconciliation. Do not delete this file. Changing the preference back does not migrate previously assigned entities.

Example new flat MQTT topics:

```text
ha_external/geraet/schalter
ha_external/geraet/schalter_set
ha_external/geraet/schalter_attribute/device_class
ha_external/geraet/energie
ha_external/geraet/leistung
ha_external/geraet/licht_brightness
ha_external/geraet/licht_brightness_set
```

Existing topics such as `ha_external/geraet/switch/state` and `…/switch/set` remain valid alongside them. Short-name collisions receive unique suffixes. Existing points, values, aliases and VIS-2 references are neither renamed nor removed.

**Before enabling flat MQTT paths, replace the complete JavaScript helper with 0.1.34 and retain your settings.** It reads both MQTT structures from the published selection catalog with exact state and command paths. Review preview first, then choose `mode: 'apply'`. Older helpers cannot discover new flat MQTT paths. The independent helper option `virtualLayout: 'flat'` only controls the layout below `0_userdata.0.ugso_mqtt`. Existing manual roles and references remain protected.

### What does the helper do? {#mqtt-helper-purpose}

MQTT uses separate topics for feedback and commands. The helper joins them through **one virtual state per value** under `0_userdata.0.ugso_mqtt`. In VIS 2, this one point is sufficient for display and control.

```text
HA -> MQTT state -> 0_userdata.0.ugso_mqtt -> VIS 2
VIS 2 -> 0_userdata.0.ugso_mqtt -> MQTT set -> HA
```

- HA feedback updates the virtual point with `ack: true`.
- VIS 2 control writes with `ack: false`; only an authorized return channel is used. A broker handoff is confirmed only after new actual HA feedback.
- Supported light values are normalized appropriately, such as brightness to 0–100%. Measurements and dates remain read-only.
- Suitable HA metadata supplies data types, units and unambiguous roles. Existing values, manual roles and unrelated objects remain protected.
- The script processes affected MQTT changes selectively. It does not rebuild everything on every unrelated measurement update.

### Requirements and setup {#mqtt-helper-setup}

1. Configure the HA MQTT-Client and ioBroker MQTT adapter. The app sends to the external broker; the return channel described here uses the ioBroker MQTT adapter in **Server/Broker** mode.
2. Select entities or assign the configured HA label. **Additional device measurements explicitly require “Automatically include related measurements and battery values from the same device” and then “Save and connect”.** Only existing, supported sensors of the same HA device are added.
3. Create a JavaScript script in the ioBroker JavaScript adapter and paste the complete code below. The helper has been tested with adapter **10.4.10**.
4. Enable **setObject** in the adapter settings and disable **Do not subscribe to all states on start**. The script requires synchronous object/state caches. No permissions are required merely to view the code.
5. Check the paths in the settings block and initially keep `mode: 'preview'`. Preview creates only missing helper base folders/backup points and logs planned mappings; it creates no controllable virtual values and sends no commands.
6. After review, set `mode: 'apply'` and restart the script. Virtual points are now created and synchronized.
7. In VIS 2 select the appropriate virtual point, **not the raw MQTT `set` point**.

### Settings and backup {#mqtt-helper-settings}

| Setting | Meaning |
| --- | --- |
| `mqttRoot` | Incoming MQTT tree; default `mqtt.0.ha_external`. |
| `mode` | `preview`: inspect; `apply`: apply; `restore`: safely undo the helper’s own backed-up changes. |
| `outputMode` | `virtual` for VIS-2 points; `roles` for alternative role/alias mapping. |
| `virtualLayout` | `nested`: original IDs (default); `flat`: short points directly inside the device folder. |
| `virtualRoot` | Target tree for virtual values. |
| `virtualBackupId`, `backupId` | Helper backup journals; existing backups are preserved. |
| `aliasRoot` | Target for read-only aliases in role mode. |
| `excludeIds` | Exact source IDs to leave untouched. |

When replacing an existing script, retain your settings. `restore` does not restore the entire ioBroker installation: objects changed manually afterwards remain protected; virtual values/references are retained and their controls disabled. See the [complete helper guide](/en/projects/mqtt-client/iobroker-roles) for details, including the role table, backups and limitations.

### Optional flat layout with short names {#mqtt-helper-flat-layout}

In the **complete helper 0.1.34**, select `virtualLayout: 'flat'` in the settings block. The default remains `virtualLayout: 'nested'`; missing settings in existing configurations also mean the original layout. Review preview first and then switch to `mode: 'apply'`.

```text
0_userdata.0.ugso_mqtt.pc_tv_wohnzimmer
  schalter
  energie
  leistung
  spannung
  stromstaerke
```

Technical IDs use these short German names in all languages: energy, power, voltage and current are detected from the device class; otherwise a suitable part of the entity ID is used. Display names are shortened accordingly, for example **Energie** or **Stromstärke**. Lights use **licht**, **helligkeit**, **farbe**, **effekt** and **farbtemperatur**.

Multiple matching values receive **leistung**, **leistung_2**, **leistung_3**, etc. Assigned names are stored in the existing journal and remain stable when selections change later. Occupied folders, unrelated points or backup IDs are not overwritten; a free suffix is used instead.

**Existing helper points are neither deleted nor moved:** old and new IDs remain synchronized and retain authorized command channels. Existing VIS-2 references therefore do not need changing. New widgets can use the short IDs; old folders remain visible initially. Switch back using `virtualLayout: 'nested'` in the new helper. The old 0.1.27 file cannot read journals containing flat entries.

MQTT objects, topic paths, values and manual roles remain unchanged. If switching back requires a folder occupied by an existing state, that new target path is skipped and logged; existing values are not replaced.


### Complete script with copy button and download {#mqtt-helper-code}

<a href="/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.34.js" download>Download JavaScript helper 0.1.34 (.js)</a>

The copy button at the top right of the code block copies the **entire script**. The code block and download use the same unchanged file, without personal credentials. Review paths and mode for your installation afterwards.

<div class="mqtt-helper-code">

<<< @/public/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.34.js

</div>

### Missing values or confirmations {#mqtt-helper-troubleshooting}

- **Only “Preview VIS 2” in the log:** After review, switch to `mode: 'apply'`.
- **“setObject is not allowed”:** The adapter permission described above is missing.
- **Missing energy, voltage, current or power:** Enable the measurements checkbox, save, and open **“Check related measurements”** in the HA app. Similar names do not replace an HA device association.
- **Commands work but confirmation is missing:** Check the raw MQTT state first. If it remains old, HA feedback is already missing before the helper. The helper never fabricates confirmation or retries commands automatically.
- **The raw MQTT `set` value does not change:** Commands are published through the broker API without retain; the stored raw value does not have to change.

[MQTT-Client documentation and app update](/en/projects/mqtt-client/) · [Helper guide and complete role mapping](/en/projects/mqtt-client/iobroker-roles)

<style scoped>
.mqtt-helper-code :deep(div[class*='language-']) { max-height: 36rem; overflow: auto; }
.mqtt-helper-code :deep(div[class*='language-'] pre) { max-height: none; overflow: visible; }
</style>


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
