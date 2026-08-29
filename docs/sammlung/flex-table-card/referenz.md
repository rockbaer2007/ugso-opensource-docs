---
title: flex-table-card Referenz
description: Kompakte deutsche Konfigurationsreferenz zur flex-table-card.
---
# Referenz

## Top-Level

| Option | Pflicht | Beschreibung |
| --- | --- | --- |
| `type` | ja | Immer `custom:flex-table-card` |
| `title` | nein | Titel der Karte |
| `entities` | ja | Entitäten oder Filter für Datenquelle |
| `columns` | ja | Spaltendefinitionen |
| `strict` | nein | Zeilen ohne Treffer ausblenden |
| `sort_by` | nein | Nach Spalte sortieren, zum Beispiel `state+` |
| `disable_header_sort` | nein | Manuelle Sortierung über Kopfzeile deaktivieren |
| `max_rows` | nein | Maximale sichtbare Zeilenzahl |
| `clickable` | nein | Entity-Dialog beim Klick öffnen |
| `selectable` | nein | Textauswahl erlauben |
| `enable_search` | nein | Suchfeld oberhalb der Tabelle anzeigen |
| `auto_format` | nein | Home-Assistant-Formatierung für Werte nutzen |
| `display_footer` | nein | Zusammenfassungszeile anzeigen |
| `css` | nein | CSS-Regeln für diese Tabelle |
| `action` | nein | Aktion/Skript als Datenquelle |
| `action_data` | nein | Daten für die Aktion |
| `static_data` | nein | Statische Daten innerhalb der Karte |

## Entities

| Option | Pflicht | Beschreibung |
| --- | --- | --- |
| `include` | ja | Regex oder Liste von Regex-Ausdrücken für Entitäten |
| `exclude` | nein | Regex oder Liste zum Ausschließen |

Bei `static_data` wird `entities: []` gesetzt.

## Columns

| Option | Pflicht | Beschreibung |
| --- | --- | --- |
| `name` | nein | Spaltenüberschrift |
| `id` | nein | stabile Spalten-ID, wichtig für `sort_by` |
| `data` | ja | Daten-Selektor |
| `hidden` | nein | Spalte ausblenden |
| `icon` | nein | Icon in der Kopfzeile |
| `modify` | nein | JavaScript-Ausdruck für Zellwert |
| `align` | nein | `left`, `center` oder `right` |
| `prefix` | nein | Text vor dem Zellwert |
| `suffix` | nein | Text nach dem Zellwert |
| `no_auto_format` | nein | Autoformatierung für Spalte deaktivieren |
| `multi_delimiter` | nein | Trenner für mehrere Datenwerte |
| `fmt` | nein | Eingebauter Formatierer |
| `sort_unmodified` | nein | Mit Originalwert sortieren |
| `footer_type` | nein | `sum`, `average`, `count`, `max`, `min` oder `text` |
| `footer_text` | nein | Text in der Footer-Zeile |
| `footer_colspan` | nein | Footer-Text über mehrere Spalten |
| `footer_modify` | nein | JavaScript für Footer-Wert |
| `tap_action` | nein | Aktion beim Tippen |
| `hold_action` | nein | Aktion bei Halten |
| `double_tap_action` | nein | Aktion bei Doppeltippen |
| `edit_action` | nein | Bearbeiten und Speichern aus der Zelle |

## Originalreferenz

Die vollständige technische Referenz liegt im Original-Repository:

- [Configuration Reference](https://github.com/custom-cards/flex-table-card/blob/master/docs/config-ref.md)

