---
title: Widget-Sprachen, HA-Quellen und Climate
description: DE/EN/FR, Attributquellen, Einheiten und optionale Climate-Steuerung ab Studio 0.1.296.
---

# Widget-Sprachen, HA-Quellen und Climate

Ab **Studio 0.1.296** erhalten die restlichen **62 Widgettypen** (Spezial, Messinstrumente, Datenfluss und sieben mitgelieferte Pakete) Widget-Eigenschaften und Laufzeitmeldungen in **DE/EN/FR**. Die allgemeine Studio-Oberfläche bleibt DE/EN. [English](/en/projects/grafik-visual-studio/ha-quellen-climate) · [Français](/fr/projects/grafik-visual-studio/ha-quellen-climate).

## Sprache wählen

In den Projekteinstellungen legt **Widget-Sprache** den Standard fest. Die gleichnamige Widget-Gruppe kann ihn überschreiben. Calendar+, Energy, Industrial, Printer, Solar, Technic und Weather/Heating funktionieren mit ihren bisherigen Paketversionen. Eigene Beschriftungen, Entitäts-IDs und gespeicherte Schlüssel werden nicht übersetzt oder umgeschrieben.

## HA-Quelle prüfen

Bei gebundenen lesenden Entitäten erscheint die zunächst deaktivierte Gruppe **HA-Quellen und Einheiten**. Ein leeres Attribut liest den Zustand; alternativ kann ein Attribut eingetragen werden. **Quelle prüfen** aktualisiert den Wert, entdeckt verfügbare Attributnamen und zeigt Einheit, fehlende Daten oder inkompatible Umrechnung an. Bei strukturierten Werten wird auf die JSON-Struktur hingewiesen. Das ausgewählte Attribut muss zur erwarteten Widget-Struktur passen.

Automatische Einheitenumrechnung ist freiwillig. Bei Energy ersetzt sie den bisherigen Faktor für diese Quelle, ohne die alte Einstellung zu löschen. Feste Anzeigen/Berechnungen richten sich nach der Widget-Einheit: Solar W/°C/%, Batterieenergie kWh, Climate native Temperatur-Einheit. Dort ist das Zieleinheitenfeld gesperrt. Bei frei konfigurierbaren Quellen sind kompatible Leistungs-, Energie-, Temperatur-, Preis-, Längen-, Volumen-, Geschwindigkeits- und Druckeinheiten möglich. Fehlende Metadaten und inkompatible Einheiten ergeben einen unbekannten Wert. Native HA-Schreibziele bleiben unverändert.

Energy kann ausgewählte numerische Recorder-Attribute lesen. Fehlende Attribute erzeugen Lücken. Unterschiedliche Verlaufsattribute derselben Entität benötigen getrennte Verlaufwidgets. C/F-Umrechnung mit Offset wird auf Energy-Verläufe nicht angewendet. Die separate Thermostat-Verlaufansicht behält ihre nativen HA-Quellen; Quellenoptionen wirken dort auf die Live-Anzeige. Recorder ersetzt nicht die vollständige native Energieverwaltung oder deren Langzeitstatistiken.

## Climate-Steuerung

Beim **Technic Thermostat – Temperature** zunächst **Climate-Steuerung** aktivieren und die benötigten Optionen einschalten:

- Heiz-/Kühlbereich mit zwei Sollwerten und gemeinsamem Übernehmen.
- Betriebsart und Voreinstellung.
- Lüftermodus, vertikales und horizontales Schwenken.
- Soll-Feuchtigkeit sowie Ein/Aus.

Die Runtime bietet ausschließlich vom Gerät gemeldete Funktionen/Werte an. Grenzen und Schrittweite werden auch serverseitig erneut geprüft. Der vorhandene einzelne Sollwert bleibt erhalten; Geräte mit ausschließlich zwei Sollwerten verwenden die Bereichssteuerung. Im Editor, bei Schreibschutz und unbekannten Zuständen bleiben die Bedienelemente gesperrt. Bei vielen Optionen das Widget ausreichend vergrößern; im kleinen Widget scrollt der Zusatzbereich.

Neue Gruppen starten deaktiviert. Bestehende Projekte, Gruppen und Faktoren bleiben gültig. Ein erfolgreicher Serviceaufruf bestätigt die Übergabe an HA, nicht den physischen Gerätezustand. Reale Geräte, Ingress/Companion, externe Einbettungen und Benachrichtigungszustellung müssen an der Installation geprüft werden.

[HA Climate](https://www.home-assistant.io/integrations/climate/) · [Gerätefähigkeiten](https://developers.home-assistant.io/docs/core/entity/climate/) · [Prüfbericht](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/remaining-widget-audit-2026-10-12.md)
