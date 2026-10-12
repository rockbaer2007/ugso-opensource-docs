---
title: Basic-Widgets
---

# Basic-Widgets

Ab **Studio 0.1.293** erhalten die 48 Basic-Einträge die Ergänzungen aus dem VIS-2-Abgleich. Die Widgets sind eigenständige HA-Umsetzungen. Bestehende Projekte behalten IDs, gespeicherte Gruppen-Schlüssel, Werte, CSS und bisherige Modi. Neue Darstellungen werden für alte Widgets erst nach ausdrücklicher Auswahl verwendet.

**Basic-Sprache** wählt automatisch aus Studio oder separat DE/EN/FR. Das betrifft Eigenschaften, Hinweise und neue Basic-Runtime-Meldungen. Eigene Texte und Entitätswerte bleiben erhalten; die gesamte Studio-Oberfläche bleibt DE/EN.

## Werte und Aktionen

Number bietet Tausendertrennung, automatische Nachkommastellen, Qualitätsentität und CSS-Klassen. „VIS-2-kompatibel“ aktiviert ausdrücklich numerisches Präfix-Parsing und Singularwahl nach Formatierung; der bisherige Modus bleibt erhalten. Bool HTML/control ergänzt Min-/Max-Sentinels, HTML-Zusätze und zusätzliche HA-Schreibziele für true/false. Der Server prüft unterstützte Entitäten, Verfügbarkeit und Grenzen. Haupt- und Zusatzaktion sind keine atomare Transaktion; nach Fehlern beim Zusatzschreiben folgt keine Zusatz-URL.

**AckFlag HTML** erhält eine ausdrückliche Bestätigungsentität oder ein Attribut. HA besitzt kein ioBroker-ACK-Flag. Alte Projekte behalten die bisherige Zustandsquelle; fehlende Bestätigung wird nicht als bestätigt ausgegeben.

Links bieten Zielfenster. Notizen können bereinigtes HTML anzeigen; der Dialog schreibt weiterhin nur Text an verfügbare input_text-Helfer ohne Attribut. Neue Widgets verwenden inerte HTML-Formatierung. Der bisherige Modus und der gespeicherte HTML-Code alter Projekte bleiben erhalten. Komplexe Webseiten gehören in iFrame; ausführbare ioBroker-Bindings werden nicht übernommen.

## Darstellung und Navigation

Unter **Extrasteuerung → Steuerungsziel** lässt sich „Hauptziel und Zusatzaktion“ oder „Nur separates Ziel“ wählen. Der zweite Modus schreibt ausschließlich an das separate Ziel; eine Richtung ohne konfiguriertes Ziel bleibt deaktiviert und fällt nicht auf das Hauptziel zurück.

Checkbox, Select und Bar bieten bisherige, native und moderne Darstellung. Tabellen erhalten klassische tclass-Hooks und eine moderne Darstellung mit festem Header. JSON, Ereignisse, Auswahl, Bestätigung, Details und Spalten bleiben nutzbar. Eigene VIS-CSS-Regeln können Anpassungen erfordern; der DOM ist nicht pixelgenau identisch.

Neue Vollbild-Widgets verwenden wechselnde Icons, erkennen Escape und sind im Editor deaktiviert. Alte Textbuttons bleiben erhalten. HTML navigation kann gezielt die Seite eines View-in-widget-Containers wechseln, ohne die Hauptseite zu verlassen. Screen Resolution kann Projekt-/Seitendetails zeigen. Gruppierung verwendet die bestehenden Studio-Gruppen.

Lokalisierte Zeiten unterstützen auto, Datums-/Zeitteile, Monats-/Wochentagsnamen, 12-Stunden-Uhr, Millisekunden und `[Literale]`. Für numerische Zeitstempel Sekunden oder Millisekunden ausdrücklich wählen; auto nutzt eine Größenheuristik. Relative Zeit aktualisiert sich jede Sekunde. TimesValue und Timestamp Value bleiben absichtlich zwei Einträge mit gleicher Quellart.

## Spracheingabe, Runtime verlassen und Gruppen

Speech to Text startet nur nach Klick. Es bietet einmal/Start-Stopp/fortlaufend, DE/EN/FR-Erkennungssprache, Schlüsselwortfilter, fünf Statusbilder und Farben. Ausgabe lokal oder an verfügbaren input_text. Browserunterstützung, Mikrofonfreigabe und meist HTTPS sind erforderlich; der Erkennungsdienst des Browsers kann Internet benötigen.

HTML logout verlässt die Runtime zur Rückkehr-URL oder versucht ein per Skript geöffnetes Fenster zu schließen. **Es meldet das HA-Konto nicht ab.**

Gruppen-Sichtbarkeit verwendet HA-Gruppen-IDs wie `system-admin` und `system-users`, getrennt durch Semikolon. Nur aktive, vom Ingress-Proxy bestätigte Benutzer erhalten Gruppen; lokale/unbekannte Benutzer erhalten keine. Bei nicht passender Gruppe oder Zustandsbedingung gilt Ausblenden/Deaktivieren. Dies ist Darstellungslogik, keine zusätzliche API-Zugriffskontrolle.

[Ausführliche Anleitung DE/EN/FR](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/basic-widgets-0.1.293.md) · [VIS-2-Prüfbericht zum vorherigen Stand](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/vis2-basic-audit-2026-10-12.md) · [English](/en/projects/grafik-visual-studio/basic) · [Français](/fr/projects/grafik-visual-studio/basic).
