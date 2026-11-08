---
title: Logic Studio
description: Erste öffentliche Testversion des grafischen Funktionsplan-Editors für Home Assistant.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.6 – erste öffentliche Testversion, 8. November 2026.** Logic Studio ist eine eigene HA-App für grafische Funktionspläne. Sie ist unabhängig von Grafik Visual Studio und Blocks for HA. Die Oberfläche ist derzeit **Deutsch**; diese Anleitung gibt es in **DE/EN/FR**.

::: warning Testversion
Zuerst auf einem Testsystem installieren und vorher ein vollständiges Backup erstellen. Native Detailoptionen werden zunächst als JSON bearbeitet. Die App schreibt keine Automationen oder Skripte in HA zurück und schaltet keine Geräte. Erzeugte Ausgaben immer prüfen und selbst in HA installieren.
:::

[GitHub-Testrelease und ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.6) · [Quellcode im Sammel-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## Testinstallation aus GitHub

[![Repository in Home Assistant hinzufügen](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. In **Einstellungen → Apps → App-Store → Repositorys** die folgende Adresse eintragen. Ist „UGSo HA Apps“ schon eingerichtet, nur nach Updates suchen.
2. **UGSo Logic Studio** auswählen und installieren. Falls experimentelle Apps ausgeblendet sind, im HA-Profil den erweiterten Modus aktivieren.
3. Starten und die Benutzeroberfläche öffnen. Unterstützt werden **HA OS/Supervised**, **amd64 und aarch64**. Der erste Container-Build kann einige Minuten dauern. Dies ist kein HACS-/Marketplace-Frontend-Paket.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Vorhandene lokale Testinstallation erhalten:** GitHub- und lokale App haben verschiedene Repository-IDs und getrennte Daten. Den alten Plan über **Projekt** als JSON exportieren und in der GitHub-App über **Öffnen** importieren. Es gibt keine automatische Migration oder Deinstallation. Projekt und Paletteinstellungen der jeweiligen App bleiben unter `/data` gespeichert.

## Zwei Arten von Plänen

| Plan | Zweck und Ausgabe |
| --- | --- |
| Wertplan | Typisierte Ein-/Ausgänge, Logik, Mathematik, Auswahl sowie Speicher, Flanken, Timer und Zähler. 33 implementierte Typen; weitere Referenztypen sind als Vorlagen gekennzeichnet. Ausgabe als HA-Automation, HA-Skript oder JavaScript-Funktion mit Host-Schnittstelle. |
| Nativer HA-Ablauf | Automationen, Skripte und Blueprints importieren und als verschachtelte Bausteine bearbeiten. 53 zusätzliche HA-Typen für Auslöser, Bedingungen, Zweige, Schleifen, Warteaktionen, Variablen und Blueprint-Eingaben. Ausgabe ausschließlich als native HA-YAML. |

Wertpläne können mit Demo-/Momentaufnahmewerten simuliert werden. Persistente Wertbausteine benötigen die dokumentierten HA-Texthelfer bzw. einen JavaScript-Speicher-Host. Native HA-Abläufe werden im Editor weder ausgeführt noch automatisch in JavaScript umgerechnet. Die JavaScript-Ausgabe ist kein ioBroker-Skript.

## Import und Bearbeitung

**HA importieren** öffnen, Automationen/Skripte/Blueprints auswählen und **Aus HA einlesen**, eine YAML-/JSON-Datei oder eingefügten Text verwenden. Eintrag und Vorschau prüfen, dann **Import übernehmen**. Vorher den eigenen Plan als JSON sichern; zusätzlich entstehen Projekt- und Quelldateisicherungen.

Der HA-Konfigurationsordner ist **schreibgeschützt** eingebunden. Gelesen werden `automations.yaml`, `scripts.yaml` und Blueprint-Dateien. Vor dem Parsen kopiert die App Quellen unter `/data/ha-source-backups/<Zeitstempel>/` mit ursprünglichem Namen. `secrets.yaml` wird nicht geöffnet; `!secret` und `!include` bleiben unaufgelöst. Bei ausgelagerten Include-Dateien die tatsächliche Datei selbst importieren.

Orange **FLOW**-Leitungen bilden Reihenfolge und Zweige ab: Zweigausgang → **DO**, anschließend **NEXT → DO**. Gelbe **VALUE/REF**-Leitungen zeigen Blueprint-Parameter und deren `!input`-Verwendung. Eigenschaften enthalten HA-Konfiguration und Zweigpfade als JSON. Parameter-/Feldschlüssel müssen eindeutig sein. Unbekannte Abschnitte bleiben als **YAML_ORIGINAL** erhalten; fehlende Verbindungen können den Export sperren.

![Importvorschau vorhandener HA-Blueprints](/images/logic-studio/blueprint-import.png)

Das **⋮-Menü** jedes Bausteins bietet **Eigenschaften, Duplizieren und Löschen**. Duplizieren übernimmt Eigenschaften ohne Leitungen. Löschen entfernt zugehörige Leitungen; **Rückgängig** stellt sie wieder her. Suche, Favoriten und zuletzt benutzte Bausteine erleichtern die Auswahl.

![Drei-Punkte-Menü im Funktionsplan](/images/logic-studio/block-menu.png)

## Prüfstand und Grenzen

Der Funktionsstand **0.1.5** wurde auf **.193 / HA Core 2026.10.4** geprüft: echter Blueprint-Import, Automation-/Skript-/Blueprint-Beispiele, inhaltlich gleiche YAML-Ausgabe und Menüaktionen. **0.1.6** ist dessen erste öffentliche Paketierung. 22 Node- und acht Python-Tests prüfen unter anderem Export, Persistenz, verschachtelte Abläufe und sicheren Quelldateiimport; die GitHub-Prüfung baut zusätzlich den Container.

Keine vollständige HA-Semantikprüfung im Editor: Ziele, Templates und Selektoren in HA kontrollieren. Kommentare, YAML-Anker und Formatierung werden nicht originalgetreu rekonstruiert. Importgrenzen: **1 MB, 200 Bausteine, 500 Leitungen**, begrenzte Verschachtelung und bis zu 250 Blueprint-Dateien in üblichen Ordnern. Regler, Kalender und eigene Unterpläne sind teilweise noch Vorlagen.

Für lokale Tests das Release-ZIP vollständig entpacken, Python 3.10+ und die Pakete aus `requirements.txt` installieren; unter Windows danach **Start-Demo.cmd** starten. `http://127.0.0.1:4180/` zeigt Demo-Entitäten ohne HA-Verbindung. Das ZIP enthält außerdem `addon/logic_studio/` für lokale App-Installationen.

Fehler bitte mit Versionen, Architektur und einem kleinen anonymisierten Beispiel [auf GitHub melden](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues). Keine Zugangsdaten, persönlichen Automationen oder Vollbackups veröffentlichen. Weitere Anleitungen und Prüfbericht liegen im Paket. Lizenz: MIT; Herkunft der übernommenen Block-Metadaten siehe `THIRD-PARTY.txt`.
