<a id="configuration"></a>
<a id="statut"></a>

# Configuration {#konfiguration}

## Entrées {#eingaben}

| Champ | Description |
|---|---|
| Utiliser MQTT | Utilise MQTT au lieu d'assistants (helpers) |
| Déclencheur de démarrage | Démarre le minuteur |
| Déclencheur d'arrêt | Arrête le minuteur prématurément |
| État « En cours » | Indique que le minuteur est en cours d'exécution |
| État « Terminé » | Indique que le minuteur est terminé |
| Sujet MQTT « En cours » | Sujet MQTT pour l'état « En cours » (RUNNING) |
| Sujet MQTT « Terminé » | Sujet MQTT pour l'état « Terminé » (DONE) |
| Durée | Durée du minuteur au format `hh:mm:ss` |
| Heure de réinitialisation | Heure pour la réinitialisation quotidienne |

## Fonctionnement avec des « Helpers » {#helper-betrieb}

Pour un fonctionnement standard avec des « Helpers » (entités auxiliaires), les éléments suivants sont nécessaires :

- un « Helper » de démarrage (Start-Helper)
- éventuellement un « Helper » d'arrêt (Stop-Helper)
- un « Helper » d'état actif (Running-Helper)
- un « Helper » d'état terminé (Done-Helper)

Les entités de type `input_boolean` conviennent à cet usage.

## Fonctionnement via MQTT {#mqtt-betrieb}

Lorsque le mode MQTT est activé, les états RUNNING et DONE sont publiés sur les « topics » (sujets) configurés.

Valeurs par défaut :

```text
timer/running/set
timer/done/set
```

## Exemple de durée {#beispiel-fur-die-dauer}

```text
00:05:00
```

correspond à cinq minutes.
