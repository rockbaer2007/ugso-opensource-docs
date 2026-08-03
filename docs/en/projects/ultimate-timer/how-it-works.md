# How It Works

## Flow

1. The start trigger changes to `on`.
2. RUNNING is activated.
3. DONE is deactivated.
4. The timer waits for the configured duration.
5. When the duration expires, RUNNING is deactivated.
6. DONE is activated.
7. During the daily reset, RUNNING and DONE are switched off.

## STOP

When the stop trigger is activated:

- RUNNING is deactivated immediately
- the stop helper is reset
- DONE is not set as a regular completion

## Daily Reset

If no custom reset time is configured, the blueprint uses:

```text
00:01:00
```

## Parallel Operation

The blueprint uses:

```yaml
mode: parallel
max: 10
```

This allows several independent instances to run at the same time.
