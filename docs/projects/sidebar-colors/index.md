---
title: Seitenleistenfarben
description: Eigene Farben und Transparenz für HA-Menüeinträge, direkt in Seitenleiste bearbeiten. HACS und Marketplace, DE/EN/FR.
---
# Seitenleistenfarben / Sidebar Colors

::: info HA 2026.11: Selektor korrigiert
Version **0.1.1** berücksichtigt im nativen Bearbeitungsdialog sowohl `ha-md-list-item` als auch `ha-list-item-button`. 27 lokale Tests bestehen, darunter DOM-Regressionen für beide HA-Zeilentypen, Transparenz, Abbrechen, Speichern, erneutes Öffnen und Theme-Rücksetzung. Der entsprechende Manager-Fix wurde auf .177 live geprüft; Sidebar Colors wurde nicht parallel installiert. Bestehende Farben und Speicherschlüssel bleiben erhalten.
:::

[Prüfumfang, Ergebnisse und offene Punkte](/sammlung/ha-2026-11-kompatibilitaet).

<img src="/images/packages/projects-sidebar-colors.svg" width="80" height="80" alt="Sidebar Colors" />

**0.1.1 · Frontend-Erweiterung · DE / EN / FR · MIT**

Symbol und Beschriftung jedes Eintrags in der Home-Assistant-Seitenleiste individuell einfärben. Das neue Farbfeld sitzt direkt im vorhandenen Dialog **„Seitenleiste bearbeiten“**, zwischen Name und Auge. Sichtbarkeit und Reihenfolge bleiben über die gewohnten Bedienelemente einstellbar.

[GitHub](https://github.com/rockbaer2007/ha-sidebar-colors) · [Download / Releases](https://github.com/rockbaer2007/ha-sidebar-colors/releases/latest) · [In HACS öffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=ha-sidebar-colors&category=plugin)

## Farbwähler

Farbfläche für Sättigung und Helligkeit, Farbtonregler, HEX-Eingabe und Deckkraft mit Live-Vorschau. Das Schachbrett steht für Transparenz. **„Übernehmen“** schließt den Farbwähler; erst **„Speichern“** im HA-Dialog sichert dauerhaft. **„Abbrechen“** verwirft den jeweiligen Farbentwurf. **„Theme-Farbe“** entfernt die eigene Farbe des Eintrags.

![Farbwähler für ATLAS mit 70 Prozent Deckkraft](/images/sidebar-colors/farbwaehler.png)

## Beispiele des Nutzers

Die Ergebnisbilder zeigen individuell gewählte Farben für Symbole und Texte. Gleiche Anzeigenamen bleiben über unterschiedliche Panel-Pfade getrennt. Es wird keine feste Farbpalette erzwungen.

<div class="sidebar-color-examples">
<figure><a href="/images/sidebar-colors/beispiel.png" target="_blank" rel="noopener noreferrer"><img src="/images/sidebar-colors/beispiel.png" alt="Farbige Seitenleiste mit Übersicht, ATLAS und HACS" /></a><figcaption>Erstes Ergebnis mit frei gewählten Farben.</figcaption></figure>
<figure><a href="/images/sidebar-colors/weiteres-beispiel.png" target="_blank" rel="noopener noreferrer"><img src="/images/sidebar-colors/weiteres-beispiel.png" alt="Weiteres Beispiel mit ATLAS-Werkzeugen und Zigbee2MQTT" /></a><figcaption>Weitere Zusammenstellung mit ATLAS-Werkzeugen.</figcaption></figure>
</div>

## Voraussetzungen und Prüfstand

Vorgesehene Mindestversion: **Home Assistant Core 2026.10.3**. Real geprüft auf **2026.10.4**: Farbauswahl, 70 % und 0 % Deckkraft, Vorschau, Speichern/Abbrechen, Neuladen, Theme-Rücksetzen, Zweittab-Synchronisierung sowie vorhandene Augen- und Sortierfunktionen. Der Nutzer bestätigt das Ergebnis. Die frühere Testfarbe wurde entfernt, seine eigenen Farben wurden erhalten.

Die Mindestversion beruht auf den vorhandenen Schnittstellen; ein separater Live-Test unter 2026.10.3 wird nicht behauptet. Marketplace ab **2026.11** verwendet das gleiche HACS-kompatible Paketformat; dafür liegt noch kein eigener Laufzeittest vor. [Offizielle Marketplace-Beschreibung](https://contributors.home-assistant.io/marketplace/how-it-works/)

## HACS / Marketplace installieren

Vorher ein vollständiges HA-Backup erstellen. Es handelt sich um ein **Frontend-Plugin**, keine Supervisor-App und keine Karte zum Einfügen. Das eigene Repo ist zunächst als benutzerdefiniertes Repository verfügbar; eine Veröffentlichung ist keine automatische Aufnahme in den Standardkatalog.

1. In HACS über **Benutzerdefinierte Repositories** `https://github.com/rockbaer2007/ha-sidebar-colors` hinzufügen, Kategorie **Dashboard** (`plugin`), anschließend **Sidebar Colors** herunterladen.
2. Ab 2026.11 über **Einstellungen → Marketplace** den entsprechenden Weg für benutzerdefinierte Repositories verwenden. Marketplace übernimmt die HACS-Einstellungen; ein eigenes Migrationsformat ist nicht erforderlich.
3. Im vorhandenen `frontend:`-Abschnitt ergänzen. Vorhandene Themes und weitere Module beibehalten; keinen zweiten Block anlegen:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/ha-sidebar-colors/ha-sidebar-colors.js
```

4. Konfiguration prüfen, HA neu starten und Browser neu laden. Nur eine Dashboard-Ressource reicht nicht, wenn zuerst eine andere HA-Seite geöffnet wird. Der Moduleintrag lädt die Erweiterung auch dort.
5. Den Kopf **Home Assistant** in der Seitenleiste länger gedrückt halten und ein Farbfeld anklicken.

## Manuell installieren oder umsteigen

Die einzelne Datei `ha-sidebar-colors.js` aus dem Release nach `/config/www/ha-sidebar-colors.js` kopieren und stattdessen `/local/ha-sidebar-colors.js` als Modul verwenden. Das Release-ZIP enthält dieselbe Datei, Lizenz und Dokumentation. Nicht beide Installationswege gleichzeitig laden.

Beim älteren Drei-Dateien-Prototyp den Eintrag `/local/ugso-sidebar-colors/0.1.0/sidebar-colors.js` durch den neuen Pfad ersetzen, HA neu starten und den Browser neu laden. Die Farbablage bleibt gleich; alte Dateien können als Sicherung erhalten bleiben.

## Einstellungen erhalten und aktualisieren

Farben werden pro HA-Benutzer im eigenen Schlüssel `ugso_sidebar_colors_v1` gespeichert und auf Geräten mit geladener Erweiterung synchronisiert. Panel-Pfade statt Namen verhindern Verwechslungen. Nur Farben zu speichern überschreibt weder native Reihenfolge noch ausgeblendete Einträge oder Theme. Dashboard-Konfigurationen und Berechtigungen werden nicht verändert.

Vor dem Farbspeichern wird ein vorheriger Stand der Farben und Sidebar-Präferenzen lokal unter `ugso-sidebar-colors-backup:<user-id>` gesichert. Das ersetzt kein HA-Vollbackup. Ist der Browserspeicher voll oder gesperrt, wird nicht gespeichert. Keine neuen Zugangsdaten, externen Skripte oder Cloud-Übersetzungen erforderlich.

Updates über dasselbe HACS-/Marketplace-Repo installieren, Modulpfad erhalten und Browser neu laden. Für den Rückbau nur den eigenen Moduleintrag entfernen, HA neu starten und Browser neu laden. Die Theme-Farben kehren zurück; native Einstellungen bleiben erhalten.

## Grenzen

Die Erweiterung nutzt interne HA-Dialogmethoden und muss nach Frontend-Updates erneut geprüft werden. Konflikte oder unklare Speicherbestätigungen halten den Entwurf offen; keine blinden Schreibwiederholungen. Es gibt keine serverseitige atomare Vergleich-und-Speichern-Funktion für diesen Benutzerspeicher. Farb- und native Reihenfolgeänderungen sind getrennte Vorgänge mit geprüftem bestmöglichem Rücksetzen bei Fehlern.

Bei 0 % Deckkraft können Symbol und Text unsichtbar sein, das Farbfeld bleibt erreichbar. Auswahlhintergrund, Titel und Zugriffsschutz bleiben unverändert. Ausfall-/Konflikttests wurden lokal simuliert; kein echter Handy-/Tablettest oder Netzabbruch unter Marketplace behauptet. [Prüfdetails und Quellcode](https://github.com/rockbaer2007/ha-sidebar-colors/blob/main/docs/TESTING.md).

<style>
.sidebar-color-examples{display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start}.sidebar-color-examples figure{margin:0;max-width:100%}.sidebar-color-examples img{max-height:720px;width:auto;max-width:100%;display:block;border-radius:8px}.sidebar-color-examples figcaption{font-size:.85em;max-width:300px;margin-top:8px}
</style>
