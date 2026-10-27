---
title: Interaktive Widgets
description: Universal, Radialregler und Inventwo-Vergleich ab Studio 0.1.295.
---

# Interaktive Widgets

**Studio 0.1.296:** Auch die übrigen 62 Widget-Typen bieten Eigenschaften und Meldungen in DE/EN/FR, optionale Climate-Steuerung sowie die Prüfung von HA-Quellen, Attributen und Einheiten. Vorhandene Projekte und Paketversionen bleiben gültig; neue Gruppen sind zunächst deaktiviert. [Anleitung und Grenzen](./ha-quellen-climate). Simulierte Prüfungen ersetzen keine Tests mit echten Geräten oder der Companion-App.

**Studio 0.1.295** ergänzt die wichtigsten Funktionsgruppen aus dem [Inventwo-VIS-2-Vergleich](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/inventwo-interactive-audit-2026-10-12.md). [English](/en/projects/grafik-visual-studio/interaktiv) · [Français](/fr/projects/grafik-visual-studio/interaktiv).

## Universal

Neben Schalten und dem bisherigen Zustandzyklus gibt es feste Tastwerte, Haltewerte mit Wiederherstellung des vorherigen Werts, Erhöhen/Verringern mit Grenzen, Navigation auf Studio-Seiten, konfigurierbare Dialogansichten und HTTP-Aufrufe. Alte Taster behalten den Zyklusmodus, bis ausdrücklich eine neue Option gewählt wird. Eigenschaftsgruppen und gespeicherte Einstellungen bleiben erhalten.

Im Standardzustand oder einem einzelnen Zustand lassen sich außerdem **Eingebettete Ansicht**, **Farbwähler** und **Analoguhr** auswählen. Ansichten können eingepasst werden; rekursive Einbettungen werden verhindert. Der Farbwähler bietet Farbfläche/Farbkreis, HSV-/RGB-Regler und optional Alpha/Kelvin. HEX, HEX8, RGB, HSL, HSV und CIE-xy gehen an einen Texthelfer; HA-Lichter erhalten geprüfte RGB-/Kelvin-Befehle. Alpha betrifft HEX8, nicht den RGB-Befehl. Die Analoguhr nutzt die Browserzeit mit optionalen Ziffern/Sekunden und einstellbaren Farben.

**Interaktiv-Sprache** wählt DE/EN/FR für Universal und Radialregler unabhängig von der Oberfläche. Eigene Texte, Entitäts-/Seitennamen und technische Werte werden nicht übersetzt.

## Radialregler und Vorschaubilder

Spur, aktive Spur und Daumen unterstützen CSS-Farben und `linear-gradient(90deg, red, rgb(255,200,0) 50%, green)`. Prozentpositionen und Richtungen wie `to top` funktionieren; Stilübernahme bleibt gültig. Bestehende einfache Farben ändern sich nicht.

Interaktiv-Vorschauen füllen seit 0.1.294 den Rahmen. Ab 0.1.295 werden auch Material-Design-Icons samt Symbolbereich größer angezeigt, in Seitenleiste und Widget-Auswahl. Dafür genügt das Studio-Update.

## Verhalten und Grenzen

HTTP GET läuft im Browser mit 15 Sekunden Timeout, ohne Studio-Anmeldedaten und ohne Serverproxy. CORS und Mixed-Content-Regeln gelten. Die Navigations-PIN ist nur eine Bedienungshürde im Projekt, keine Zugriffsberechtigung. Bei Browserabsturz oder Netzverlust kann ein Haltewert nicht zuverlässig zurückgestellt werden; kritische Verbraucher brauchen einen HA-seitigen Timeout.

Studio verwendet HA-Entitäten und Projektseiten. Separat frei gebundene ioBroker-Farbkomponenten und sämtliche Inventwo-Uhrdetails sind nicht nachgebildet; eine vollständige 1:1-Pixelgleichheit wird nicht behauptet. Die Gesamtoberfläche bleibt DE/EN. [Ausführliche Anleitung DE/EN/FR](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/universal-0.1.295.md).
