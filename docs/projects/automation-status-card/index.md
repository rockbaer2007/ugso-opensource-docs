---
title: Automation Status Card
description: Automatische Automationsliste, Auswahl per Checkbox, Laufstatus und Trace-Diagnose. Version 0.1.3, DE/EN/FR.
---
# Automation Status Card

<img src="/images/automation-status-card/icon.svg" width="80" height="80" alt="Automation Status Card" />

**0.1.3 · DE / EN / FR · MIT**

[GitHub](https://github.com/rockbaer2007/automation-status-card) · [Download 0.1.3](https://github.com/rockbaer2007/automation-status-card/releases/tag/v0.1.3) · [Open-Source-Doku](https://opensource.ugso-software.de/projects/automation-status-card/)

Listet automatisch alle für den angemeldeten HA-Benutzer verfügbaren `automation.*`-Entitäten alphabetisch auf. Standardmäßig sind acht Zeilen sichtbar; weitere Einträge werden vertikal gescrollt. Neue und entfernte Automationen werden automatisch berücksichtigt. Die Karte benötigt keine zusätzliche Kartenbibliothek.

[English](/en/projects/automation-status-card/) · [Français](/fr/projects/automation-status-card/)

Auf .177 mit HA 2026.10.4 geprüft: Grundversion 0.1.0 sowie Auswahl und Laufdiagnose in der korrigierten Fassung 0.1.3. Echte HA-Traces, Fehler, normaler Abschluss, Laufzeitwarnung, ausgeschaltete Warnung, Checkboxen und gespeicherte Auswahl erfolgreich geprüft. [Prüfbericht mit Bildern](https://github.com/rockbaer2007/automation-status-card/blob/main/docs/TESTING.md).

## Installation

### HACS / Marketplace

`https://github.com/rockbaer2007/automation-status-card` als benutzerdefiniertes Repository in Kategorie **Dashboard** (`plugin`) hinzufügen und herunterladen. Kartenressource: `/hacsfiles/automation-status-card/automation-status-card.js`. Das Paket ist HACS-kompatibel, aber noch nicht in den Standardkatalog aufgenommen; ein eigener Marketplace-Installationstest wurde nicht durchgeführt. Keine Supervisor-App. HACS und manuelle Kopie nicht gleichzeitig laden.

### Manuell

1. Vorher HA sichern. `dist/automation-status-card.js` bzw. die JS-Datei aus dem Paket nach `/config/www/automation-status-card/automation-status-card.js` kopieren.
2. Unter **Einstellungen → Dashboards → Ressourcen** als **JavaScript-Modul** hinzufügen: `/local/automation-status-card/automation-status-card.js`. Bestehende Ressourcen erhalten.
3. Dashboard neu laden und **Automation Status Card** im Kartenwähler auswählen oder die YAML-Konfiguration unten verwenden.

Die Oberfläche folgt automatisch der HA-Sprache, unterstützt DE/EN/FR und verwendet ansonsten Englisch. Im visuellen Editor sind Titel, sichtbare Zeilen, Schalten und Sprache einstellbar.

Unter **Automationen anzeigen** sind zunächst alle Einträge angehakt: **Haken = anzeigen**, Haken entfernen = nur in dieser Karte ausblenden. **Alle auswählen** zeigt alle Einträge; **Alle abwählen** blendet alle derzeit aufgeführten Einträge aus. Neue Automationen erscheinen standardmäßig wieder ausgewählt. Die Auswahl wird je Karte gespeichert und verändert weder die Automation noch andere Karten. Vorübergehend nicht verfügbare, abgewählte Entitäten bleiben im Editor aufgeführt und können wieder angewählt werden.

Optional in YAML: `hidden_entities: [automation.meine_automation]`. Diese IDs sind abgewählt und werden ausgeblendet. Ohne diese Einstellung bleibt die bisherige Anzeige unverändert.

```yaml
type: custom:automation-status-card
title: Automationen
visible_rows: 8
allow_toggle: false
language: auto
```

| Einstellung | Standard | Bedeutung |
| --- | --- | --- |
| `title` | Automationen, übersetzt | Überschrift; `""` blendet sie aus. |
| `visible_rows` | `8` | Ganze Zahl von 1 bis 50; weitere Zeilen bleiben scrollbar. |
| `allow_toggle` | `false` | Nur Anzeige oder Schalter zum Aktivieren/Deaktivieren. |
| `language` | `auto` | `auto`, `de`, `en`, `fr`. |
| `show_health` | `true` | Laufstatus und Diagnose anzeigen. |
| `check_traces` | `true` | Letzten beendeten Ablauf lesend prüfen; nur für HA-Administratoren. |
| `runtime_warning_seconds` | `300` | Laufzeitwarnung nach dieser Sekundenzahl; `0` schaltet nur die Warnung ab, höchstens 604800 (7 Tage). |

## Laufstatus und Fehlerhinweise

HA meldet manche Abbrüche nur als `aborted`, etwa eine nicht erfüllte Bedingung oder einen expliziten Fehlerstopp. Diese werden neutral als **Letzter Ablauf abgebrochen – Grund in HA-Traces prüfen** angezeigt. Die Karte erfindet dafür weder einen Erfolg noch einen Fehler.

**Ein/Aus bleibt die Aktivierung.** Zusätzlich zeigt die Karte bei `current > 0` **Läuft**, Anzahl der Durchläufe und die Laufzeit. Bei Überschreiten der konfigurierten Grenze erscheint **Läuft ungewöhnlich lange**. Das ist kein Absturznachweis: `delay`, Wartebedingungen und lange Aktionen können beabsichtigt sein. Es wird nichts automatisch beendet oder neu gestartet.

Bei passender vollständiger Trace-Liste verwendet die Karte den Beginn des ältesten laufenden Durchlaufs, begrenzt die Dauer aber immer auf die selbst beobachtete Zeit. So erzeugen abweichende HA-/Browser-Uhren keine verfrühte Warnung. Ansonsten zählt sie konservativ erst ab der Beobachtung, mit entsprechendem Zusatz. `last_triggered` allein wird nicht als Laufzeit verwendet. Bei einer neuen Auslösung nach der letzten Trace-Abfrage wird ebenfalls auf Beobachtungszeit zurückgefallen. Seitenwechsel, Neuladen und Verbindungsabbruch setzen die lokale Beobachtung zurück; dies ist kein Hintergrund-Watchdog.

Für Administratoren liest die Karte höchstens alle 30 Sekunden `trace/list` für Automationen, zusätzlich per **Ablaufdaten aktualisieren**. Nur Zusammenfassungen werden verarbeitet; keine vollständigen Traces, Variablen oder Automationskonfigurationen. Der jüngste beendete Ablauf wird als **fehlerhaft** markiert, wenn HA einen Fehler meldet. Ein normaler Stopp oder eine nicht erfüllte Bedingung gilt nicht automatisch als Fehler. Ein jüngerer beendeter Ablauf ohne gemeldeten Fehler löst den alten Fehlerhinweis ab. Zeitangaben stehen im Tooltip; die Detailansicht ist weiterhin über den Namen erreichbar.

Fehlende Administratorrechte, fehlende Automation-ID, keine gespeicherten Traces, eine nicht unterstützte Schnittstelle und Verbindungsfehler sind **kein Automationsfehler**. Die Karte zeigt fehlende Ablaufdaten entsprechend an. Bei getrennter HA-Verbindung wird kein veralteter Laufstatus als aktuell dargestellt. Trace-Abfragen funktionieren nur, soweit HA dem angemeldeten Benutzer Zugriff gibt; die Karte erweitert keine Rechte. Ein Fehler innerhalb einer mit `continue_on_error` fortgesetzten Aktion kann in der Zusammenfassung fehlen.

Grundlage: [HA-Automationsattribute](https://www.home-assistant.io/docs/automation/basics/), [Trace-WebSocket-API](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/trace/websocket_api.py), [Trace-Zusammenfassungen](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/trace/models.py). Die HA-Schnittstelle kann sich in späteren Versionen ändern.

Ein/Aus bezeichnet **aktiviert/deaktiviert**, nicht „läuft gerade“. Die Karte startet keine Automation und verwendet keinen Trigger-Service. In der Liste öffnet der Name die HA-Detailansicht; bei erlaubtem Schalten aktiviert/deaktiviert der Schalter genau diese Automation. Beim Deaktivieren setzt die Karte `stop_actions: false`, damit ein bereits laufender Durchlauf nicht gezielt gestoppt wird. HA-Rechte gelten weiterhin; die Anzeigeoption ist keine Zugriffssperre.

Nicht verfügbare/unbekannte Automationen und getrennte Verbindungen lassen sich nicht schalten. Bis zur Zustandsbestätigung wird der jeweilige Schalter gesperrt. Fehler werden angezeigt; nach fehlender Bestätigung gibt es keinen automatischen Wiederholungsversuch. Maßgeblich bleibt der von HA gemeldete Zustand.

## Einzelne Automation mit Bubble Card oder Mushroom

Im Ordner `examples` liegen vier unabhängige YAML-Vorlagen, jeweils für **eine einzelne Automation**:

- `bubble-single-readonly.yaml` / `bubble-single-control.yaml`
- `mushroom-single-readonly.yaml` / `mushroom-single-control.yaml`

`automation.replace_me` durch die eigene Entität ersetzen. Die Anzeigevariante deaktiviert die Kartenaktionen, die Bedienvariante schaltet über die normale Toggle-Aktion der jeweiligen Erweiterung. Diese Vorlagen sind keine automatische Liste; sie laufen direkt als Bubble Card bzw. Mushroom Entity Card. Es ist kein zusätzlicher eigener Erweiterungscode nötig. Deren Standard-Aktionsverhalten gilt unabhängig von `allow_toggle` der Automation Status Card.

Die jeweiligen Erweiterungen müssen separat installiert sein. Ressourcenpfade unter Linux sind groß-/kleinschreibungssensitiv:

- Bubble Card: `/hacsfiles/Bubble-Card/bubble-card.js`
- Mushroom: `/hacsfiles/lovelace-mushroom/mushroom.js`

Die Vorlagen verändern keine bestehenden Karten. Fremde Erweiterungen werden nicht mitgeliefert. Quellen: [Bubble Card](https://github.com/Clooos/Bubble-Card), [Mushroom](https://github.com/piitaya/lovelace-mushroom).

## Entwicklung

Node 22 oder neuer: `npm ci`, `npm run check`, `npm run build`, `npm test`. Das Release enthält die gebaute JS-Datei separat und ein vollständiges ZIP mit Anleitungen und Beispielen. Nach einem manuellen Update den vorhandenen Ressourcenpfad beibehalten und `?v=0.1.3` ergänzen beziehungsweise aktualisieren, anschließend den Browser vollständig neu laden. [Testbericht](https://github.com/rockbaer2007/automation-status-card/blob/main/docs/TESTING.md).

MIT-Lizenz. Keine externen Laufzeitdienste, keine eigenen Tokens und keine Telemetrie. Konfiguration wird durch HA im Dashboard gespeichert; vorhandene Automationsdefinitionen werden von der Karte nicht bearbeitet.


![HA test: run warning and failure](/images/automation-status-card/health-177-013.png)

![HA editor: selection](/images/automation-status-card/selection-177-013.png)

![Single-automation examples, initial-version test](/images/automation-status-card/cards-177.png)
