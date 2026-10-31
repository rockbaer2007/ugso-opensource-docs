---
title: Eigene Seitenleisten-Verknüpfungen
description: UIX-Einträge in der Home-Assistant-Seitenleiste mit internen Weiterleitungszielen erstellen.
---
# Eigene Seitenleisten-Verknüpfungen

::: info Verfügbar ab UIX 9.0.0-beta.6
Diese Funktion gehört zur Vorschau auf `dev`, nicht zur stabilen Basis 8.4.0. Abgeglichen am 31.10.2026 mit der [englischen Quelle](https://github.com/Lint-Free-Technology/uix/blob/e6fb84dd715ea4bac9a330357705897ea8d44690/docs/source/using/custom-sidebar-panels.md).
:::

UIX kann eigene Einträge zur Home-Assistant-Seitenleiste hinzufügen, die direkt auf eine andere Home-Assistant-Seite weiterleiten. Das eignet sich für häufig verwendete Seiten, die sonst erst über Einstellungen oder ein anderes Panel erreichbar sind.

Öffne **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren** und wähle **Manage custom sidebar panels** (eigene Seitenleisten-Panels verwalten). Wähle beim Hinzufügen ein Symbol, gib einen Titel ein und bestimme das Ziel mit der Navigationsauswahl.

Aktiviere **Admin required**, wenn das Seitenleisten-Panel nur für Administratorkonten zugänglich sein soll.

Als Ziele sind ausschließlich Navigationspfade innerhalb derselben Home-Assistant-Instanz zulässig. Eigene Seitenleisten-Panels leiten nicht auf externe Webseiten weiter.

Jedes Panel erhält eine feste interne URL, die UIX verwaltet. Titel, Symbol und Ziel lassen sich ändern, ohne das Panel neu anzulegen. Beim Löschen verschwindet der Seitenleisteneintrag sofort.

::: tip Reihenfolge der Seitenleiste
Jeder Benutzer kann die [Seitenleisteneinträge in seinem Home-Assistant-Profil umsortieren oder ausblenden](https://www.home-assistant.io/dashboards/dashboards/#reorganizing-items-in-the-sidebar).
:::

::: info Verhalten der Weiterleitung
Ein eigenes Seitenleisten-Panel ist eine Weiterleitung, keine Kopie der Zielseite. Beim Auswählen ersetzt UIX die Panel-URL durch das konfigurierte Ziel. Dadurch entsteht im Browserverlauf kein zusätzlicher Weiterleitungsschritt.
:::
