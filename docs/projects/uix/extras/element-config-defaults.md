---
title: Standardwerte für Elementkonfigurationen
description: Statische Standardwerte auf passende Elemente in Home-Assistant-Dashboards anwenden.
---
> Nach der englischen UIX-Dokumentation von [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Geprüft am 08.11.2026 bis `dev e28976f`, Vorschau **9.1.0-beta.1**. Stabile Basis: **9.0.0 / Home Assistant ab 2026.11.0**.

# Standardwerte für Elementkonfigurationen

UIX kann passende Dashboard-Elemente um statische Konfigurationsvorgaben ergänzen, ohne das Dashboard zu bearbeiten. Ein Anwendungsfall sind die Geräte- und Entitätsnamen von Home Assistant 2026.11: Ein Standardwert kann bewirken, dass passende Elemente nur den Entitätsanteil des Namens anzeigen. Auch fehlende Konfigurationsschlüssel oder Objektpfade wie `state_color` oder `group_config.name` lassen sich ergänzen.

## Regelliste konfigurieren

Öffne **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren** und wähle **Configure element defaults**. Mit **Configure using UI** fügst du Vorgaben über Formularfelder hinzu.

Lege für jeden fehlenden Schlüssel einen Eintrag an. Ein passendes Element kann mehrere Vorgaben erhalten, beispielsweise für `name` und `state_color`.

Mit **Configure using YAML** kannst du die vollständige kanonische Konfiguration einfügen oder bearbeiten. Beide Editoren lesen und schreiben dieselben Regeln; du kannst jederzeit zwischen ihnen wechseln.

```yaml
element_config:
  - uix_type: row
    element_type: entity
    config_key: name
    value:
      type: entity
```

Jede Regel hat vier Schlüssel:

| Schlüssel | Beschreibung |
| --- | --- |
| `uix_type` | Die UIX-Konfigurationsgrenze: `card`, `badge`, `heading-badge`, `row`, `glance` oder `element`. |
| `element_type` | Der passende Home-Assistant-Konfigurationstyp `type`, etwa `tile` oder `entity`. |
| `config_key` | Ein fehlender Schlüssel oder ein durch Punkte getrennter Objektpfad. Array-Indizes werden nicht unterstützt. |
| `value` | Der zu verwendende statische Wert. |

Füge beispielsweise diese vollständige Konfiguration unter **Configure using YAML** ein, damit passende Tile-Karten, Entitätszeilen, Glance-Entitäten und Entitäts-Badges nur den Entitätsanteil des Anzeigenamens verwenden:

```yaml
element_config:
  - uix_type: card
    element_type: tile
    config_key: name
    value: { type: entity }
  - uix_type: row
    element_type: entity
    config_key: name
    value: { type: entity }
  - uix_type: glance
    element_type: entity
    config_key: name
    value: { type: entity }
  - uix_type: badge
    element_type: entity
    config_key: name
    value: { type: entity }
```

## Verhalten und Grenzen

UIX ergänzt einen Wert nur, wenn der Schlüssel fehlt. Jeder ausdrücklich gesetzte Wert hat Vorrang vor der globalen Vorgabe, einschließlich `null`, `false`, einer leeren Zeichenfolge, einer leeren Liste oder einer leeren Map.

Durch Punkte getrennte Pfade erzeugen fehlende Objekt-Maps, ersetzen aber niemals vorhandene Werte. Beispielsweise ergänzt `config_key: group_config.name` den Schlüssel `name`, wenn `group_config` fehlt oder ein Objekt ist. Bei `null`, einem skalaren Wert oder einem Array bleibt `group_config` unverändert. Regeln für denselben UIX-Typ und Elementtyp dürfen sich nicht überschneiden: Konfiguriere entweder `group_config` oder `group_config.name`, nicht beides.

Dieses Beispiel setzt einen Standardnamen für jedes untergeordnete Element einer Fold Entity Row und erhält eine vorhandene Einstellung `group_config.secondary_info`:

```yaml
element_config:
  - uix_type: row
    element_type: custom:fold-entity-row
    config_key: group_config.name
    value: { type: entity }
```

Entitätszeilen und Glance-Entitäten unterstützen sowohl die normale Mapping-Form als auch die kompakte Zeichenfolgenform von Home Assistant. Bei einer passenden Regel für `row`/`entity` oder `glance`/`entity` wird `- sensor.kitchen_temperature` vorübergehend als Entitäts-Mapping mit dem konfigurierten Wert an Home Assistant übergeben. Im Dashboard-Quelltext bleibt die kompakte Zeichenfolge erhalten.

Die Werte sind statisch. UIX verarbeitet in solchen Vorgaben keine Jinja-Templates, UIX-Templates, Makros oder Billets. Regeln gelten an den direkten Konfigurationsgrenzen von Karten, Badges, Überschriften-Badges, Zeilen einer Entities-Karte, Glance-Entitäten und Picture-Elements, einschließlich passender nativer Elemente, die UIX Forge rendert. Pfade ergänzen Daten nur innerhalb einer passenden Konfiguration; sie wählen keine weiteren verschachtelten Elementgrenzen aus. Abgesehen von Glance-Entitäten sind Dialoge, Kartenfunktionen, Kartenmarker und andere verschachtelte Elementgrenzen nicht eingeschlossen.

Änderungen gelten für verbundene Dashboards, sobald die aktualisierte UIX-Konfiguration eintrifft. UIX baut nur die betroffene Konfigurationsgrenze aus der ursprünglichen Dashboard-Konfiguration neu auf; erzeugte Werte werden nicht in deinem Dashboard gespeichert.
