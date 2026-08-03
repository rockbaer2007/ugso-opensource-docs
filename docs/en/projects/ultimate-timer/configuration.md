# Configuration

## Inputs

| Field | Description |
|---|---|
| Use MQTT | Uses MQTT instead of helpers |
| Start Trigger | Starts the timer |
| Stop Trigger | Stops the timer early |
| Running State | Shows the running timer |
| Done State | Shows an expired timer |
| MQTT Running Topic | MQTT topic for RUNNING |
| MQTT Done Topic | MQTT topic for DONE |
| Duration | Timer duration in `hh:mm:ss` format |
| Reset Time | Time for the daily reset |

## Helper Mode

For regular helper mode, the following are required:

- a start helper
- optionally a stop helper
- a running helper
- a done helper

`input_boolean` entities work well for this.

## MQTT Mode

When MQTT mode is enabled, RUNNING and DONE are published through the configured
topics.

Default values:

```text
timer/running/set
timer/done/set
```

## Duration Example

```text
00:05:00
```

means five minutes.
