---
title: Cache
---
# Cache-Probleme

Nach Updates kann der Browser oder die Companion App alte Ressourcen behalten. In diesem Fall:

- Home Assistant neu laden.
- Browser hart neu laden.
- Companion-App-Cache leeren.
- Prüfen, ob UIX eine Reload-Meldung zeigt.

## Typische Anzeichen

- Alte Styles bleiben sichtbar.
- Neue YAML-Regeln wirken erst nach mehreren Reloads.
- Desktop-Browser und Companion App zeigen unterschiedliche Ergebnisse.
- Nach einem UIX-Update erscheint kurz eine Reload-Meldung.

## Empfehlung

Die UIX-Aktion [`clear-cache`](../extras/uix-actions#clear-cache-home-assistant-frontend-cache-leeren), Alias `clear_cache`, leert gezielt den HA-Frontend-Anwendungscache und lädt den Browser neu. **`localStorage` bleibt erhalten**, etwa die Browser-Mod-Browser-ID. Das ist vom pauschalen Löschen aller Browser-/App-Daten zu unterscheiden; für ein Ressourcenproblem ist solches Löschen nicht erforderlich.

Erst Home Assistant neu laden, dann den Browser hart neu laden. In der Companion App kann zusätzlich das Leeren des Frontend-Caches nötig sein.
