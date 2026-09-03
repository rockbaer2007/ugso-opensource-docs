---
title: Calendar Card Pro Konfiguration
description: Deutsche Konfigurationsreferenz für Calendar Card Pro.
---
# Konfigurationsreferenz

Diese Seite bildet die Optionsgruppen der Originalreferenz ab. Für Detailbeispiele bleibt die englische Originalreferenz maßgeblich.

## Neu In v4.1.0

Version `4.1.0` ergänzt mehrere kalenderbezogene Steuerungen:

- `event_type` trennt Termine mit Uhrzeit von ganztägigen Terminen.
- `filter_field` lässt `blocklist` und `allowlist` auf Titel, Ort oder Beschreibung arbeiten.
- `replace_field`, `replace_pattern` und `replace_with` verändern den angezeigten Text, ohne den Kalendertermin selbst zu ändern.
- `allday_expires_at` lässt ganztägige Termine eines Kalenders früher am Tag auslaufen.
- `days_of_week` begrenzt einen Kalender auf Werktage oder Wochenende.
- `allday_badge`, `allday_badge_style` und `allday_badge_color` steuern die neue Badge-Darstellung für ganztägige Termine.

## Grundeinstellungen

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `entities` | array | Pflicht | Liste der Kalenderentitäten, optional mit eigenen Einstellungen pro Kalender. |
| `view` | string | `list` | Layout: `list` für Tage untereinander, `column` für Tage nebeneinander. |
| `start_date` | string | heute | Startdatum als `YYYY-MM-DD` oder relativer Ausdruck wie `today+7`, `start_of_week`, `monday+1w`. |
| `days_to_show` | number | `3` | Anzahl der angezeigten Tage. |
| `event_type` | string | `all` | Terminart: `all`, `timed` oder `all_day`. Kann global oder pro Kalender gesetzt werden. |
| `compact_days_to_show` | number | - | Anzahl der Tage im kompakten Modus. |
| `compact_events_to_show` | number | - | Anzahl der Termine im kompakten Modus. |
| `compact_events_complete_days` | boolean | `false` | Zeigt alle Termine für Tage, an denen mindestens ein Termin sichtbar ist. |
| `show_empty_days` | boolean | `false` | Tage ohne Termine anzeigen. In der Spaltenansicht standardmäßig `true`. |
| `hide_when_empty` | boolean | `false` | Karte ausblenden, wenn keine kommenden Termine vorhanden sind. |
| `empty_day_text` | string | übersetzter Standard | Eigener Text für leere Tage oder komplett leere Karten. |
| `filter_duplicates` | boolean | `false` | Doppelte Termine ausblenden, wenn Titel, Start, Ende und Ort identisch sind. |
| `split_multiday_events` | boolean | `false` | Mehrtägige Termine auf jedem betroffenen Tag anzeigen. In der Spaltenansicht standardmäßig `true`. |
| `language` | string | System, Fallback `en` | Sprache der Kartentexte, automatisch aus Home Assistant erkennbar. |
| `column` | object | erbt Top-Level-Werte | Spezielle Darstellungsoptionen für `view: column`. |

## Nur Für Die Spaltenansicht

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `column.day_header_gap` | string | `8px` | Abstand zwischen Tageskopf und erstem Termin. |
| `column.day_header_separator_width` | string | `0px` | Breite der Linie unter dem Tageskopf. |
| `column.day_header_separator_color` | string | `var(--divider-color)` | Farbe der Linie unter dem Tageskopf. |
| `column.min_day_width` | number | `140` | Kleinste Spaltenbreite in Pixeln. |
| `column.min_days_to_show` | number | `days_to_show` | Mindestanzahl sichtbarer Spalten. |
| `column.min_days_fallback` | string | `list` | Verhalten bei zu wenig Platz: `list` oder `cramp`. |

## Optionen Ohne Wirkung In Der Spaltenansicht

Diese Optionen bleiben für die Listenansicht relevant, wirken aber nicht direkt in der Spaltenansicht:

`date_vertical_alignment`, `today_indicator_position`, `compact_events_to_show`, `compact_days_to_show`, `compact_events_complete_days`, kalenderbezogenes `split_multiday_events`.

## Kalenderbezogene Optionen

Ein Eintrag in `entities` kann nur eine Entity-ID sein oder ein Objekt mit eigenen Einstellungen.

| Option | Beschreibung |
| --- | --- |
| `entity` | Kalenderentität, zum Beispiel `calendar.family`. |
| `label` | Eigene Beschriftung des Kalenders. |
| `label_type` | Steuert, wie die Beschriftung gelesen wird. |
| `color` | Kalenderfarbe. |
| `accent_color` | Akzentfarbe für Linie und optionale Hintergründe. |
| `label_icon_color` | Farbe für Label/Icon. |
| `show_time` | Zeit für diesen Kalender anzeigen. |
| `show_location` | Ort für diesen Kalender anzeigen. |
| `location_icon` | Icon für Ortsangaben dieses Kalenders, zum Beispiel `mdi:office-building`; kann automatische Teams-Erkennung überschreiben. |
| `show_description` | Beschreibung für diesen Kalender anzeigen. |
| `compact_events_to_show` | Kompaktes Limit für diesen Kalender. |
| `blocklist` | Begriffe oder Muster ausschließen. |
| `allowlist` | Nur passende Begriffe oder Muster anzeigen. |
| `filter_field` | Feld für `blocklist`/`allowlist`: `title`, `location` oder `description`. |
| `replace_field` | Feld für Textersetzung: `title`, `location` oder `description`. |
| `replace_pattern` | Regex-Muster, das im gewählten Feld ersetzt oder entfernt wird. |
| `replace_with` | Ersatztext; ohne `replace_pattern` wird das ganze Feld ersetzt. |
| `split_multiday_events` | Mehrtägige Termine für diesen Kalender splitten. |
| `event_type` | Kalenderbezogene Terminart: `all`, `timed` oder `all_day`. |
| `allday_expires_at` | Uhrzeit im Format `HH:MM`, ab der ganztägige Termine dieses Kalenders als vergangen gelten. |
| `days_of_week` | Beschränkung auf `weekdays` oder `weekends`. |

## Header

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `title` | string | - | Kartentitel, kann Home-Assistant-Templates enthalten. |
| `title_font_size` | string | `--calendar-card-font-size-title` | Schriftgröße des Titels. |
| `title_color` | string | `--calendar-card-color-title` | Titelfarbe. |

## Layout Und Abstände

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `background_color` | string | `--ha-card-background` | Hintergrundfarbe der Karte. |
| `accent_color` | string | `#03a9f4` | Akzentfarbe der vertikalen Linie und optionaler Termin-/Ganztags-Badges. |
| `vertical_line_width` | string | `2px` | Breite der vertikalen Linie. |
| `day_spacing` | string | `10px` | Abstand zwischen Tagen oder Spalten. |
| `event_spacing` | string | `4px` | Innenabstand innerhalb eines Termins. |
| `additional_card_spacing` | string | `0px` | Zusätzlicher Abstand oben/unten in der Karte. |
| `height` | string | `auto` | Exakte feste Kartenhöhe. |
| `max_height` | string | `none` | Maximale Kartenhöhe bei wachsendem Inhalt. |

## Wochennummern Und Trennlinien

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `show_week_numbers` | string | `null` | Wochennummern anzeigen: `iso`, `simple` oder deaktiviert. |
| `show_current_week_number` | boolean | `true` | Wochennummer für aktuelle/erste Woche anzeigen. |
| `week_number_font_size` | string | `12px` | Schriftgröße der Wochennummer. |
| `week_number_color` | string | `var(--primary-text-color)` | Textfarbe der Wochennummer. |
| `week_number_background_color` | string | `#03a9f450` | Hintergrundfarbe der Wochennummer. |
| `first_day_of_week` | string | `system` | Wochenstart: `monday`, `sunday` oder `system`. |
| `day_separator_width` | string | `0px` | Trennlinie zwischen Tagen. |
| `day_separator_color` | string | `var(--secondary-text-color)` | Farbe der Tag-Trennlinie. |
| `week_separator_width` | string | `0px` | Trennlinie zwischen Wochen. |
| `week_separator_color` | string | `#03a9f450` | Farbe der Wochen-Trennlinie. |
| `month_separator_width` | string | `0px` | Trennlinie zwischen Monaten. |
| `month_separator_color` | string | `var(--primary-text-color)` | Farbe der Monats-Trennlinie. |

## Heute-Markierung

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `today_indicator` | boolean/string | `false` | Heute-Markierung: `true`, `dot`, `pulse`, `glow`, MDI-Icon, Emoji oder Bildpfad. |
| `today_indicator_position` | string | `15% 50%` | Position im CSS-Format. |
| `today_indicator_color` | string | `#03a9f4` | Farbe der Markierung. |
| `today_indicator_size` | string | `6px` | Größe der Markierung. |

## Datumsspalte

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `date_vertical_alignment` | string | `middle` | Vertikale Ausrichtung: `top`, `middle`, `bottom`. |
| `weekday_font_size` | string | `14px` | Schriftgröße des Wochentags. |
| `weekday_color` | string | `--primary-text-color` | Farbe des Wochentags. |
| `day_font_size` | string | `26px` | Schriftgröße der Tageszahl. |
| `day_color` | string | `--primary-text-color` | Farbe der Tageszahl. |
| `show_month` | boolean | `true` | Monatsnamen anzeigen. |
| `month_font_size` | string | `12px` | Schriftgröße des Monats. |
| `month_color` | string | `--primary-text-color` | Monatsfarbe. |
| `weekend_weekday_color` | string | erbt `weekday_color` | Wochentagsfarbe am Wochenende. |
| `weekend_day_color` | string | erbt `day_color` | Tageszahlfarbe am Wochenende. |
| `weekend_month_color` | string | erbt `month_color` | Monatsfarbe am Wochenende. |
| `today_weekday_color` | string | erbt Wochenende/Standard | Wochentagsfarbe für heute. |
| `today_day_color` | string | erbt Wochenende/Standard | Tageszahlfarbe für heute. |
| `today_month_color` | string | erbt Wochenende/Standard | Monatsfarbe für heute. |

## Terminspalte

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `event_background_opacity` | number | `0` | Hintergrunddeckkraft für Termine mit Akzentfarbe, 0-100. |
| `event_icon_vertical_alignment` | string | `top` | Vertikale Icon-Ausrichtung: `top`, `middle`, `bottom`. |
| `show_past_events` | boolean | `false` | Bereits beendete Termine anzeigen. |
| `show_countdown` | boolean | `false` | Countdown bis zum Termin anzeigen. |
| `show_countdown_allday` | boolean | `true` | Countdown auch für ganztägige Termine anzeigen. |
| `show_multiday_allday_time` | boolean | `true` | Zeitzeile bei mehrtägigen ganztägigen Terminen anzeigen; sie trägt die Enddatums-Information. |
| `allday_badge` | string | `off` | Position des Ganztags-Badges: `off`, `title` oder `time`. |
| `allday_badge_style` | string | `subtle` | Badge-Stil: `subtle`, `outline`, `tinted` oder `filled`. |
| `allday_badge_color` | string | `accent` | Badge-Farbe: `accent`, `text` oder eine CSS-Farbe. |
| `show_progress_bar` | boolean | `false` | Fortschrittsbalken für laufende Termine anzeigen. |
| `progress_bar_color` | string | `var(--secondary-text-color)` | Farbe des Fortschrittsbalkens. |
| `progress_bar_height` | string | berechnet | Höhe des Fortschrittsbalkens. |
| `progress_bar_width` | string | je Layout | Breite des Fortschrittsbalkens. |
| `empty_day_color` | string | `--primary-text-color` | Farbe für Text an leeren Tagen. |
| `event_font_size` | string | `14px` | Schriftgröße des Termintitels. |
| `title_max_lines` | number | `0` | Maximale Zeilen für Termintitel, `0` = unbegrenzt. |
| `event_color` | string | `--primary-text-color` | Farbe des Termintitels. |
| `show_time` | boolean | `true` | Terminzeit anzeigen. |
| `show_single_allday_time` | boolean | `true` | Zeitdarstellung für einzelne ganztägige Termine anzeigen. |
| `time_24h` | boolean | System | 24-Stunden-Format nutzen. |
| `time_two_digit_hours` | boolean | `false` | Stunden zweistellig anzeigen. |
| `show_end_time` | boolean | `true` | Endzeit anzeigen. |
| `time_icon_size` | string | `14px` | Größe des Uhr-Icons. |
| `time_font_size` | string | `12px` | Schriftgröße der Zeit. |
| `time_color` | string | `--secondary-text-color` | Farbe der Zeit. |
| `time_max_lines` | number | `0` | Maximale Zeilen für Zeittext. |
| `show_location` | boolean | `true` | Ort anzeigen. |
| `show_location_allday` | boolean | `true` | Orte auch bei ganztägigen Terminen anzeigen, wenn `show_location` aktiv ist. |
| `remove_location_country` | boolean/string | `false` | Ländernamen aus Orten entfernen, optional per Regex-String. |
| `location_icon_size` | string | `14px` | Größe des Orts-Icons. |
| `location_font_size` | string | `12px` | Schriftgröße des Orts. |
| `location_color` | string | `--secondary-text-color` | Farbe des Orts. |
| `location_max_lines` | number | `0` | Maximale Zeilen für Ort. |
| `show_description` | boolean | `false` | Beschreibung anzeigen. |
| `show_description_allday` | boolean | `true` | Beschreibungen auch bei ganztägigen Terminen anzeigen, wenn `show_description` aktiv ist. |
| `description_icon_size` | string | `14px` | Größe des Beschreibungs-Icons. |
| `description_font_size` | string | `12px` | Schriftgröße der Beschreibung. |
| `description_color` | string | `--secondary-text-color` | Farbe der Beschreibung. |
| `description_max_lines` | number | `0` | Maximale Zeilen für Beschreibung. |

## Wetter

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `weather` | object | - | Wetterkonfiguration. |
| `weather.entity` | string | - | Wetterentität für Forecasts. |
| `weather.position` | string | `date` | Position: `none`, `date`, `event`, `both`. |
| `weather.date` | object | - | Wetteranzeige im Tageskopf. |
| `weather.event` | object | - | Wetteranzeige neben Terminen. |

`weather.date` akzeptiert: `show_conditions`, `show_high_temp`, `show_low_temp`, `show_uv_index`, `uv_index_threshold`, `icon_size`, `font_size`, `color`.

`weather.event` akzeptiert: `show_conditions`, `show_temp`, `show_uv_index`, `uv_index_threshold`, `daily_forecast_fallback`, `max_lines`, `icon_size`, `font_size`, `color`.

## Aktionen

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `tap_action` | object | `none` | Aktion beim Tippen auf die Karte. |
| `hold_action` | object | `none` | Aktion beim Halten der Karte. |

Aktionsparameter können je nach Aktion sein:

`action`, `navigation_path`, `service`, `service_data`, `url_path`, `open_tab`.

## Cache Und Aktualisierung

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `refresh_interval` | number | `30` | Minuten zwischen Datenaktualisierungen. |
| `refresh_on_navigate` | boolean | `true` | Beim Wechsel zwischen Dashboard-Ansichten neu laden. |
