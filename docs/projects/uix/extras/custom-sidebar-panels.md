---
title: Eigene Seitenleisten-Verknüpfungen
description: UIX-Verknüpfungen zu Home-Assistant-Seiten und externen Webseiten erstellen.
---
# Eigene Seitenleisten-Verknüpfungen

::: info UIX 9.0.0
Interne und externe Seitenleisten-Verknüpfungen gehören zur stabilen Version **9.0.0** und benötigen **Home Assistant 2026.11.0 oder neuer**. Die unten beschriebene neue Desktop-Beschränkung der Tab-Option stammt aus der Vorschau **9.1.0-beta.0** auf `dev`.
:::

UIX kann eigene Einträge in der Home-Assistant-Seitenleiste hinzufügen, die eine andere Home-Assistant-Seite oder eine Webseite öffnen. Das erleichtert den Zugriff auf häufig verwendete Seiten unter „Einstellungen“ und auf zugehörige Webdienste.

Öffne **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren** und wähle **Manage custom sidebar panels**. Wähle das Icon und gib Titel und Ziel ein.

Aktiviere **Admin required**, um den Eintrag auf Administratorkonten zu beschränken.

Als Ziel sind Home-Assistant-Pfade mit führendem `/`, etwa `/config/dashboard`, oder absolute `http`- und `https`-URLs erlaubt. Andere URL-Schemata werden nicht akzeptiert.

::: info Vorschau ab 9.1.0-beta.0
**Open in new tab (desktop only)** ist in dieser Form ab **9.1.0-beta.0** verfügbar.
:::

Mit **Open in new tab (desktop only)** öffnet sich ein interner Home-Assistant-Pfad in einem neuen Tab des Desktop-Browsers. Der bisherige Home-Assistant-Tab kehrt zur zuvor angezeigten Seite zurück. In der Companion-App navigiert UIX stattdessen innerhalb der App zum HA-Pfad. Für externe Webseiten-URLs wird diese Option nicht verwendet; Webseiten können nicht innerhalb der Companion-App geöffnet werden.

::: info Neuer Tab und Popup-Sperre
Ob ein interner HA-Pfad in einem neuen Tab geöffnet werden darf, entscheidet die Popup-Sperre des Desktop-Browsers. UIX versucht dies bei Auswahl des Seitenleisteneintrags, kann es aber nicht garantieren. Bei einer Blockierung wird der HA-Pfad im aktuellen Tab geöffnet.
:::

Jeder Eintrag erhält eine feste interne URL, die UIX verwaltet. Titel, Icon und Ziel lassen sich deshalb ändern, ohne den Eintrag neu anzulegen. Löschen entfernt ihn sofort aus der Seitenleiste.

::: tip Reihenfolge der Seitenleiste
Jeder Benutzer kann Einträge über sein Profil [sortieren und ausblenden](https://www.home-assistant.io/dashboards/dashboards/#reorganizing-items-in-the-sidebar).
:::

::: info Weiterleitung
Ein eigenes Panel ist eine Weiterleitung, keine zweite Kopie der Zielseite und kein iframe. Bei internen Zielen ersetzt UIX die Panel-URL durch das konfigurierte Ziel. Dadurch entsteht im Browserverlauf kein zusätzlicher Weiterleitungsschritt.
:::

Quelle: [englische UIX-Originaldokumentation](https://uix.lf.technology/extras/custom-sidebar-panels/), Lint-Free-Technology/uix, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Ergänzender Quellenabgleich vom 07.11.2026: [`dev e7b5bdd`](https://github.com/Lint-Free-Technology/uix/commit/e7b5bdd811a53960e9559c53a354c7855c537286), einschließlich [`1d53592`](https://github.com/Lint-Free-Technology/uix/commit/1d53592b241ec8666b34d67056671bb37d1c2a1f). Die Vorschauangabe ersetzt keine stabile Versionsfreigabe.
