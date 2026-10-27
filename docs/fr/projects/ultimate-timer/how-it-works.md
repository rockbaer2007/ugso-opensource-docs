<a id="how-it-works"></a>
<a id="statut"></a>

# Fonctionnement {#funktionsweise}

## Déroulement {#ablauf}

1. Le déclencheur de démarrage (Start-Trigger) passe à `on`.
2. L'état RUNNING est activé.
3. L'état DONE est désactivé.
4. Le minuteur attend la durée définie.
5. Une fois la durée écoulée, RUNNING est désactivé.
6. L'état DONE est activé.
7. Lors de la réinitialisation quotidienne, RUNNING et DONE sont désactivés.

## STOP {#stop}

Si le déclencheur d'arrêt (Stop-Trigger) est activé :

- RUNNING est immédiatement désactivé.
- L'auxiliaire d'arrêt (Stop-Helper) est réinitialisé.
- DONE n'est pas activé comme lors d'un cycle normal.

## Réinitialisation quotidienne {#taglicher-reset}

Si aucune heure de réinitialisation spécifique n'est indiquée, le blueprint utilise :

```text
00:01:00
```

## Fonctionnement en parallèle {#parallelbetrieb}

Le blueprint utilise :

```yaml
mode: parallel
max: 10
```

Cela permet d'utiliser plusieurs instances indépendantes simultanément.
