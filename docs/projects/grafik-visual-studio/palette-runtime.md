---
title: Palette, zuletzt benutzt und Runtime
description: Miniaturen, gespeicherte zuletzt benutzte Widgets und Runtime-Start/Stopp ab Studio 0.1.299.
---

# Palette, zuletzt benutzt und Runtime

**Studio 0.1.299** enthält die neue Palette und die zuvor lokal als 0.1.298 geprüfte eingebettete Runtime. [GitHub-Update](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-visual-studio-v0.1.299).

## Miniaturen und Beschreibungen

Die Palette zeigt drei gleichmäßige Kacheln pro Zeile: Miniatur oben, Name darunter. Messinstrumente verwenden ihren eigenen Renderer mit Vorschauwerten, Geräte und Uhr eigene statische Miniaturen. Vorhandene Paketbilder bleiben erhalten. Beim Darüberfahren oder Tastaturfokus erscheint eine größere Vorschau mit kurzer Beschreibung. UGSo-Sets und SVG-Line/LineBox/Math zeigen ausschließlich den Namen. Die Vorschau schaltet keine Geräte.

## Zuletzt benutzt

Direkt unter der Suche steht der unabhängig einklappbare Bereich **Zuletzt benutzt**. Er enthält bis zu **zwölf unterschiedliche Widgettypen**, den zuletzt eingefügten zuerst. Ein erneutes Einfügen verschiebt denselben Typ nach vorn; es entsteht kein zweiter Eintrag. Kacheln, Miniaturen und Beschreibungen entsprechen der normalen Palette.

Ein Klick fügt ein neues Widget mit den Standardwerten des Typs ein, **keine Kopie des zuletzt bearbeiteten Widgets**. Importieren, Einfügen aus der Zwischenablage und bloßes Auswählen ändern die Liste nicht. Die Palettensuche filtert auch die zuletzt benutzten Einträge. Nicht mehr installierte Pakettypen werden nicht angeboten; nach einer erneuten Installation können sie wieder erscheinen.

Liste und Klappzustand bleiben beim Neuladen und App-Update im **gleichen Browserprofil und derselben Webadresse** erhalten. Sie werden nicht zwischen Geräten synchronisiert und nicht in Projekte exportiert. Browserdaten löschen setzt sie zurück. Bei blockiertem Browserspeicher bleibt die Liste für die aktuelle Sitzung nutzbar. Andere Einstellungen und Projektdateien werden nicht verändert.

![Zuletzt benutzte Widgets auf dem Testsystem ARM (Pi 5)](/images/grafik-visual-studio/recent-177-299.jpg)

## Runtime direkt über der Arbeitsfläche

**▶** neben den Seitenreitern speichert das aktuelle Projekt und startet eine isolierte Runtime über der Arbeitsfläche. **■** stoppt sie. Palette, Eigenschaften und Bearbeitungswerkzeuge sind währenddessen ausgegraut und gesperrt, einschließlich Tastenkürzeln. Seitenwechsel und das separate Runtime-Fenster bleiben bedienbar. Eine fehlgeschlagene Speicherung startet keine Runtime.

Stoppen stellt die bisherige Editorseite mit Auswahl, Verlauf und Scrollposition wieder bereit. Seitenwechsel der Vorschau ändern nicht die Editorseite. Eigene eingebettete Tabs behalten beim Start ihren Kontext. Die bisherigen Editor/Runtime-Moduslinks oben entfallen; **Neuer Tab** öffnet weiterhin die eigenständige Runtime. In der Runtime können vorhandene Widgets wie bisher echte HA-Geräte steuern.

![Inline-Runtime mit ausgegrauten Editorwerkzeugen](/images/grafik-visual-studio/inline-runtime-298.jpg)

## Erhalt und Prüfung

Bestehende Projekte, Widgettypen, CSS- und Farbeinstellungen bleiben erhalten. Neue Browserpräferenzen erhalten einen eigenen Speicherschlüssel. Kein VIS-2-Code oder -Bild wurde für diese Funktionen kopiert.

Am 8. November 2026 wurde 0.1.299 auf dem [Testsystem ARM (Pi 5)](/sammlung/testsysteme#testsystem-arm) (HA 2026.11.0/ARM64) und [Testsystem PC (64)](/sammlung/testsysteme#testsystem-pc) (HA 2026.10.4/amd64) geprüft: zuletzt verwendete Miniaturen, Reihenfolge ohne Duplikate, Einfügen, Einklappen und Erhalt nach Neuladen sowie die Sperre während der Inline-Runtime. Testeinfügungen wurden rückgängig gemacht; die bestehenden 13 beziehungsweise 11 Widgets blieben erhalten. Palette und Start/Stopp waren zusätzlich mit Speichern, Seitenwechsel und Rückkehr zum Editor geprüft. 23 JavaScript- und 17 Python-Tests bestanden. Details: [Quellcode und Prüfberichte](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/docs).
