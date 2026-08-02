# Funktionsweise

## Ablauf

1. Der Start-Trigger wechselt auf `on`.
2. RUNNING wird aktiviert.
3. DONE wird deaktiviert.
4. Der Timer wartet die eingestellte Dauer.
5. Nach Ablauf wird RUNNING deaktiviert.
6. DONE wird aktiviert.
7. Beim täglichen Reset werden RUNNING und DONE ausgeschaltet.

## STOP

Wird der Stop-Trigger aktiviert:

- RUNNING wird sofort deaktiviert
- der Stop-Helper wird zurückgesetzt
- DONE wird nicht als regulärer Ablauf gesetzt

## Täglicher Reset

Ist keine eigene Reset-Zeit angegeben, verwendet der Blueprint:

```text
00:01:00
```

## Parallelbetrieb

Der Blueprint verwendet:

```yaml
mode: parallel
max: 10
```

Dadurch können mehrere unabhängige Instanzen gleichzeitig verwendet werden.
