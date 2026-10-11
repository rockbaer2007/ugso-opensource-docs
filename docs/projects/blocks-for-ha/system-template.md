---
title: Systemwerte und Template-Baukasten
description: Gemeinsame Entitätswerte, App- und Automationssteuerung und verständliche Templates.
---

# Systemwerte und Template-Baukasten

Seit **0.1.62**, vollständig in DE/EN/FR. Die neuen Systemblocks sind auch die Wertlieferanten für Templates. Vorhandene Text-, Mathematik- und Variablenblocks werden weiterverwendet.

Seit **0.1.63** hat Template direkte Werte-Andockpunkte in untereinander angeordneten Zeilen, ähnlich „Datei schreiben“ bei ioBroker. Alle Template-Bausteine sind ohne Zahnrad; die Eingänge passen zum jeweiligen Typ.

## System

| Baustein | Verwendung |
| --- | --- |
| Entitäts-ID | Entität auswählen und ihre ID an einen anderen Block anschließen. |
| Wert von Entität | Feste HA-Auswahl: Zustand, Name, Einheit, Attribut, zuletzt geändert oder aktualisiert. |
| Wert von Entitäts-ID | Eine ID aus einem Entitäts-ID-, Text- oder Variablenblock anschließen. |
| Einmal lesen in Variable | Momentaufnahme speichern, danach die enthaltenen Aktionen ausführen. Kein Auslöser. Die Variable ist auch für folgende HA-Schritte verfügbar. |
| App steuern | Starten, stoppen oder neu starten. Installierte Apps über Supervisor auswählen oder Kennung manuell eingeben. |
| Automation steuern | Aktivieren, deaktivieren, umschalten oder jetzt ausführen. |

![Entitätswert](/assets/blocks-for-ha/blocks/de/ugso_entity_value.png)
![Dynamischer Entitätswert](/assets/blocks-for-ha/blocks/de/ugso_entity_value_dynamic.png)
![Momentaufnahme](/assets/blocks-for-ha/blocks/de/ugso_entity_snapshot.png)
![Automation steuern](/assets/blocks-for-ha/blocks/de/ugso_automation_control.png)
![App steuern](/assets/blocks-for-ha/blocks/de/ugso_app_control.png)

**Attribut** wählen und den Attributnamen eingeben; die passende Zeile erscheint automatisch. Zustände sind häufig Text. Vor Rechnungen bei Bedarf **Konvertierung → nach Zahl** verwenden. Fehlende Attribute und Zeitstempel liefern `none`; ein fehlender Zustand liefert HA-typisch `unknown`. **Ersatzwert** kann diese Werte auffangen.

Bei **Automation steuern** ergänzt das Zahnrad: **Entitäts-ID anschließen**, **Bedingungen berücksichtigen** und **Laufende Aktionen stoppen**. Die angeschlossene ID ersetzt die feste Auswahl. Bedingungen gelten für „jetzt ausführen“, Stoppen gilt für „deaktivieren“. Ohne explizite Option verwendet HA seine Defaults: Ausführen überspringt Bedingungen, Deaktivieren stoppt laufende Aktionen. Aktivieren startet die Aktionen nicht, sondern schaltet die Auslöser frei.

**App steuern** benötigt Supervisor und Administratorrechte. Die App erhält lesenden Supervisor-Zugriff für die Auswahlliste; Start/Stop/Neustart erfolgen erst durch die exportierte Automation in HA. Ohne Supervisor bleibt die Kennung manuell bearbeitbar, die Aktion steht dort jedoch nicht zur Verfügung. Export: `hassio.app_start`, `hassio.app_stop`, `hassio.app_restart` mit `data.app`.

## Template zusammenstecken

1. **Templates → Template** in einen Werteingang stecken, etwa „Nachricht“.
2. Normalen **Text** direkt an **Teil 1** anschließen.
3. Einen **Entitätswert aus System** oder ein **Zahlenformat** direkt an **Teil 2** anschließen.
4. Wird der letzte Eingang belegt, erscheint automatisch ein weiterer Andockpunkt. Die Reihenfolge von oben nach unten ist die Ausgabereihenfolge. Leere Eingänge werden ausgelassen und behalten ihre Position für Rückgängig/Wiederholen.

Beispiel: Text `Temperatur: ` → Entitätswert `sensor.temperatur` über **Zahlenformat** mit Mathematik-Zahl `1` als Nachkommastellen → Text ` °C`. Ergebnis beispielsweise `Temperatur: 21.6 °C`.

![Template](/assets/blocks-for-ha/blocks/de/ugso_template_builder.png)
![Zeilenumbruch als Wert](/assets/blocks-for-ha/blocks/de/ugso_template_linebreak.png)
![Zahlenformat](/assets/blocks-for-ha/blocks/de/ugso_number_format.png)
![Bedingte Ausgabe](/assets/blocks-for-ha/blocks/de/ugso_template_conditional.png)

| Ergänzung | Bedeutung |
| --- | --- |
| Zahlenformat | 0–10 Nachkommastellen, immer mit Dezimalpunkt. Mathematik-Zahl für die Anzahl verwenden. Ersatzwert direkt am optionalen Werteingang anschließen; sonst leerer Text bei ungültiger Zahl. |
| Wert sonst | Ersatz für `unknown`, `unavailable`, `none` und leeren Text. `0` und `false` bleiben erhalten. |
| Zeilenumbruch | Neue Zeile an dieser Stelle. |
| falls / dann / sonst | An „falls“ eine boolesche Bedingung anschließen; an „dann“ und „sonst“ die entsprechenden Werte. Für mehrere Teile im Zweig ein weiteres Template anschließen. Leere Zweige geben leeren Text aus. |

Formatierung wird direkt um den betroffenen Wert gesteckt. Text, Zahlen, Entitätswerte, Zeilenumbruch und bedingte Werte verwenden Werteanschlüsse; „falls“ akzeptiert nur boolesche Blocks. Aktionsketten passen nicht in diese Eingänge. Jinja-Zeichen in einem normalen Textblock bleiben wörtlicher Text. Ältere Ausgeben-Ketten werden beim Laden im Editor automatisch in direkte Werte umgewandelt, einschließlich Zweigen und deaktivierten Teilen. Die alten Blocktypen bleiben für die Projektkompatibilität lesbar, erscheinen aber nicht mehr im Menü.

**Rechtsklick → Template-Vorschau / Jinja** zeigt den erzeugten Code und lässt HA mit aktuellen Werten rendern. Dies ist eine Momentaufnahme, führt keine Aktionen aus und funktioniert nur bei erreichbarer HA-Verbindung. Ohne Verbindung wird die Vorschau ausdrücklich als nicht verfügbar angezeigt. Zugangsdaten bleiben auf dem Server. Beim Projekt-JSON bleiben Blocks, Verbindungen und Zahnradoptionen erhalten. YAML enthält natives Jinja; beim YAML-Import kann es wieder als freier Templateblock erscheinen. HA kann reine Zahlen oder Listen aus Templateergebnissen als native Werte interpretieren.

Referenzen: [HA-Automationsaktionen](https://www.home-assistant.io/docs/automation/automation_integration_actions/), [Supervisor](https://www.home-assistant.io/integrations/hassio/), [Jinja in HA](https://www.home-assistant.io/docs/templating/).
