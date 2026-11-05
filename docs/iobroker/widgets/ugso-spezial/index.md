---
title: UGSo Special
description: Animierte SVG-Linien und Summenknoten für ioBroker VIS 2.
---

# UGSo Special

Mit **UGSo Special** stellst du Datenflüsse in VIS 2 dar, zum Beispiel die Leistung mehrerer Verbraucher. Das Widget-Set enthält zwei Bausteine.

## Widgets

- **SVG-Line** verbindet Punkte gerade, rechtwinklig oder über Zwischenpunkte. Farben, Strichlängen und Pfeilspitzen sind einstellbar. Positive Werte animieren vorwärts, negative rückwärts; bei null stoppt die Animation. Die Geschwindigkeit kann fest oder vom Betrag des Werts abhängig sein.
- **SVG LineBox** addiert bis zu vier Eingangsleitungen und einen optionalen Korrekturwert. Die Summe kann an bis zu zwei Ausgangsleitungen weitergegeben oder in der Laufzeitansicht in einen vorhandenen beschreibbaren numerischen Datenpunkt unter `0_userdata.0` geschrieben werden. Fehlt der Wert eines ausgewählten Eingangs, wartet die Box auf diesen Wert.

Im Editor rasten gelbe Endpunkte beim Ziehen an einer anderen Linie oder LineBox ein. Ein Ende mit Pfeilspitze kann nicht andocken. Das Andocken richtet die Grafik aus; die Werteverbindungen stellst du separat in der LineBox ein.

## Installation

Der technische Paketname lautet jetzt `iobroker.vis-2-widgets-ugso-special`.
Exportiere vorhandene VIS-2-Projekte als Sicherung, installiere das neue Paket
und starte VIS 2 neu. Prüfe die Projekte vor dem Entfernen des bisherigen Pakets.
Die Widget-Template-IDs und der interne Federationsname bleiben erhalten.

Voraussetzung ist eine laufende VIS-2-Installation. Installiere das Widget-Set über die GitHub-URL des Projekts in ioBroker Admin (Expertenmodus). Starte VIS 2 nach Updates neu, damit die neue Version geladen wird. Im Editor findest du beide Widgets in der Palette unter **UGSo Special**.

- [GitHub](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special)
- [Releases](https://github.com/rockbaer2007/ioBroker.vis-2-widgets-ugso-special/releases)
- [npm](https://www.npmjs.com/package/iobroker.vis-2-widgets-ugso-special)
