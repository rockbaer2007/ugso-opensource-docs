---
title: Eigene Seitenleisten-Verknüpfungen
description: UIX-Verknüpfungen zu Home-Assistant-Seiten und externen Webseiten erstellen.
---
# Eigene Seitenleisten-Verknüpfungen

::: info UIX 9.0.0
Interne und externe Seitenleisten-Verknüpfungen sowie **Open in new tab** gehören zur stabilen Version **9.0.0** und benötigen **Home Assistant 2026.11.0 oder neuer**.
:::

UIX kann eigene Einträge in der Home-Assistant-Seitenleiste hinzufügen, die eine andere Home-Assistant-Seite oder eine Webseite öffnen. Das erleichtert den Zugriff auf häufig verwendete Seiten unter „Einstellungen“ und auf zugehörige Webdienste.

Öffne **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren** und wähle **Manage custom sidebar panels**. Wähle das Icon und gib Titel und Ziel ein.

Aktiviere **Admin required**, um den Eintrag auf Administratorkonten zu beschränken.

Als Ziel sind Home-Assistant-Pfade mit führendem `/`, etwa `/config/dashboard`, oder absolute `http`- und `https`-URLs erlaubt. Andere URL-Schemata werden nicht akzeptiert.

Mit **Open in new tab** öffnet sich das Ziel in einem neuen Tab. Der bisherige Home-Assistant-Tab kehrt zur zuvor angezeigten Seite zurück. Blockiert der Browser den neuen Tab, öffnet UIX das Ziel stattdessen im aktuellen Tab. Ohne diese Option öffnen externe Webseiten im aktuellen Tab; Home-Assistant-Pfade verwenden weiterhin die Navigation innerhalb der Anwendung.

::: info Neuer Tab und Popup-Sperre
Ob ein neuer Tab geöffnet werden darf, entscheidet die Popup-Sperre des Browsers. UIX versucht dies bei Auswahl des Seitenleisteneintrags, kann es aber nicht garantieren. Bei einer Blockierung wird das Ziel im aktuellen Tab geöffnet.
:::

Jeder Eintrag erhält eine feste interne URL, die UIX verwaltet. Titel, Icon und Ziel lassen sich deshalb ändern, ohne den Eintrag neu anzulegen. Löschen entfernt ihn sofort aus der Seitenleiste.

::: tip Reihenfolge der Seitenleiste
Jeder Benutzer kann Einträge über sein Profil [sortieren und ausblenden](https://www.home-assistant.io/dashboards/dashboards/#reorganizing-items-in-the-sidebar).
:::

::: info Weiterleitung
Ein eigenes Panel ist eine Weiterleitung, keine zweite Kopie der Zielseite und kein iframe. Bei internen Zielen ersetzt UIX die Panel-URL durch das konfigurierte Ziel. Dadurch entsteht im Browserverlauf kein zusätzlicher Weiterleitungsschritt.
:::

Quelle: [englische UIX-Originaldokumentation](https://uix.lf.technology/extras/custom-sidebar-panels/), Lint-Free-Technology/uix, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
