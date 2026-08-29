---
title: Weitere Optionen
description: Weitere UIX-Styling-Funktionen und Randfälle.
---
# Weitere Styling-Optionen

Diese Seite sammelt kleinere Styling-Funktionen und Randfälle, die nicht in die anderen UIX-Styling-Kategorien passen.

UIX kann neben Karten, Rows, Badges, Bildern und Views auch andere Home-Assistant-Frontend-Bereiche über passende Theme-Variablen erreichen. Dazu gehören zum Beispiel Dialoge, Toasts, Sidebars, Konfigurationsseiten, Kalender, To-do-Ansichten, History-Ansichten und Persistent Notifications.

Wichtig ist immer, das DOM-Ziel zu prüfen und den passenden UIX-Kontext zu wählen:

- Für lokale Kartenänderungen: `uix:` direkt in der Karte.
- Für wiederverwendbare globale Regeln: UIX-Theme-Variablen wie `uix-card`, `uix-row`, `uix-dialog` oder `uix-config`.
- Für Shadow-DOM-Pfade: die jeweilige `-yaml`-Variante.
- Für dynamische Werte: Jinja2-Templates, Makros oder Billets.

Wenn ein Element nicht zuverlässig gefunden wird, prüfe zuerst [DOM-Navigation](../concepts/dom), Lade-Reihenfolge und mögliche Shadow-Root-Grenzen.
