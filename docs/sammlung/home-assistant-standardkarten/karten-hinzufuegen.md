---
title: Karten hinzufuegen
description: Deutsche Arbeitsuebersetzung zum Hinzufuegen von Karten in Home Assistant.
---
# Karten Hinzufuegen

Eine Karte kann direkt aus der Ansicht heraus hinzugefuegt werden, in der sie erscheinen soll. Alternativ kann eine Karte auch von der Geraeteseite erzeugt werden.

## Karte Aus Einer Ansicht Hinzufuegen

1. Oeffne in Home Assistant **Einstellungen** > **Dashboards**.
2. Waehle dein Dashboard aus.
3. Wenn dein Dashboard mehrere Ansichten hat, waehle die gewuenschte Ansicht.
4. Waehle oben rechts den Bearbeiten-Button.
5. Je nach Layout:
   - In der Sections-Ansicht den Plus-Button in der Section verwenden.
   - In anderen Layouts wie Masonry, Panel oder Sidebar unten rechts **Karte hinzufuegen** verwenden.
6. Es gibt zwei Wege:
   - **Nach Entitaet**: Entitaeten auswaehlen und anschliessend eine vorgeschlagene Karte waehlen. Nicht zugewiesene Entitaeten koennen im Bereich **Nicht zugewiesen** erscheinen.
   - **Nach Karte**: Kartentyp aus der Liste waehlen. In der Sections-Ansicht ist die Tile Card oft ein sinnvoller Startpunkt.
7. Optional Sichtbarkeitsbedingungen definieren.
8. In der Sections-Ansicht kann die Karte im Tab **Layout** in der Groesse angepasst werden.
9. Karte anpassen:
   - Aktionen definieren.
   - Kopf- und Fussbereich definieren.
   - Features anpassen.
   - Nicht jede Karte unterstuetzt alle Elemente.
10. Mit **Fertig** speichern.

## Karte Von Der Geraeteseite Hinzufuegen

Dieser Weg ist praktisch, wenn du gerade auf einer Geraeteseite bist und daraus direkt eine Dashboard-Karte erstellen moechtest.

1. Oeffne **Einstellungen** > **Geraete & Dienste**.
2. Waehle bei der passenden Integration **Geraete**.
3. Waehle bei mehreren Geraeten das gewuenschte Geraet.
4. Suche den passenden Bereich, zum Beispiel **Sensoren** oder **Ereignisse**, und waehle **Zum Dashboard hinzufuegen**.
5. Waehle im Dialog das Ziel-Dashboard und bei Bedarf die Zielansicht.
6. Waehle **Weiter**.
7. Wenn der Kartenvorschlag passt, waehle **Zum Dashboard hinzufuegen**.
8. Wenn du eine andere Karte moechtest, waehle **Andere Karte auswaehlen** und danach den Kartentyp.
9. Die Karte wird zur gewaehlten Ansicht hinzugefuegt.
10. Zum Bearbeiten die Zielansicht oeffnen und **Karte bearbeiten** waehlen.

## Wichtige Verweise

- [Kartenaktionen](https://www.home-assistant.io/dashboards/actions/)
- [Kartenfeatures](https://www.home-assistant.io/dashboards/features/)
- [Header und Footer](https://www.home-assistant.io/dashboards/header-footer/)
- [Ansichten](https://www.home-assistant.io/dashboards/views/)
