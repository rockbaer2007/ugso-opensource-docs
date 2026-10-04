---
title: Material Design
description: Externes Material-Design-Widget-Set für Grafik Visual Studio.
---

# Material Design

Das externe [UGSo Material Design](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign) startet mit **Preview Color Schemes**. Paket **0.1.0** benötigt Studio **0.1.210** oder neuer und steht unter MIT. Es ist inspiriert von [ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign); Lizenz und Copyright von typhosj und Scrounger sind enthalten.

Die Vorschau zeigt alle **26 Farbreihen**. Klassisch verwendet eine weiße Oberfläche; Material 3 unterstützt helle und dunkle Oberflächen. Die Farbfelder bleiben in allen Stilen unverändert. Überschrift und Widgetgröße lassen sich einstellen; weitere Reihen und breite Paletten sind per Scrollen erreichbar.

- **Gestaltungsstil:** Klassisch, Material 3 oder Projektstandard.
- **Projektstandard:** unter Einstellungen → Allgemein → Material Design auswählen.
- **Farbschema:** Projektstandard folgt dem hellen/dunklen Seitenthema; Hell und Dunkel überschreiben es für dieses Widget.

Das Widget liest keine Home-Assistant-Entität und schreibt keine Zustände. Die ioBroker-Bindung `__mdwThemeDark` wird durch das Studio-Seitenthema ersetzt. „Thema verwenden“ aus ioBroker ist kein Theme-Import in Studio.

## Paketregistrierung testen

Das fertige `.wg` und SHA-256 liegen im Repository unter `dist/`. Über **Registrierung Widget** im [Paketkatalog](https://visualstudio.ugso-software.de/?lang=de) das Paket mit ID `ugso.materialdesign`, Version `0.1.0`, Lizenz MIT, Repository-Link und Mindestversion `0.1.210` einreichen. Erst nach Prüfung und Freigabe erscheint es im Studio-Katalog. Es wird nicht als mitgeliefertes Paket automatisch eingetragen.

Für die lokale Prüfung: Einstellungen → Widget-Pakete → Lokal. Für GitHub: den direkten Link zur `.wg`-Datei verwenden. Weitere Widgets folgen schrittweise anhand der Screenshots und Exporte.
