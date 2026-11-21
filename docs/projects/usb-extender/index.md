---
title: USB Extender für Home Assistant
description: USB-Tasten, Stream Decks und Makropads über bis zu drei MQTT-Broker verbinden. Installation, Anlernen, Topics und Praxistest mit Bildern.
---

# USB Extender für Home Assistant

**0.1.5 · Raspberry Pi · Stand 21. November 2026**

Eine USB-Tastatur am Raspberry Pi kann zum Bedienteil für Home Assistant oder
ioBroker werden. Der USB Extender erkennt Eingaben und sendet sie über MQTT an
bis zu **drei Broker gleichzeitig**. Die Weboberfläche dient zum Einrichten und
kann danach abgeschaltet werden; USB und MQTT laufen unabhängig weiter.

[GitHub / README DE und EN](https://github.com/rockbaer2007/usb-extender-home-assistant)
· [ZIP 0.1.5](https://github.com/rockbaer2007/usb-extender-home-assistant/releases/tag/v0.1.5)
· [Änderungen](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/CHANGELOG.md)

Dies ist ein eigenständiges Raspberry-Pi-Programm, keine HA-App zum Installieren
im App-Store und keine offizielle Software von Home Assistant oder Elgato.
Es ist **kein USB-over-IP-Tunnel**: Drucker oder Kameras werden damit nicht als
entfernte USB-Geräte an HA durchgereicht.

Die Bilder stammen aus dem echten Nutzeraufbau mit 0.1.5. Die Oberfläche ist
derzeit deutsch. Breite Bilder lassen sich durch Anklicken in Originalgröße öffnen.

[![Breite Tastenliste mit MQTT-Kanälen](/images/usb-extender/key-list.png)](/images/usb-extender/key-list.png)

## Welche Geräte werden erkannt? {#hardware}

**Erkannt** bedeutet zunächst: Linux kann das USB-Gerät auflisten. **Bedienbar**
bedeutet zusätzlich: Ein Treiber kann seine Eingaben lesen und das Gerät ist in
der Oberfläche ausdrücklich freigegeben. Das ist nicht dasselbe.

| Gerät | Was bereits vorgesehen ist | Prüfstand |
| --- | --- | --- |
| USB-Tastaturen, auch Windows-Medientastaturen | Tastencodes, Drücken/Loslassen, Umschalter, Tastenzustand, Klick/Doppelklick/Halten | Trust-/HCT-Tastaturen im Praxisaufbau genutzt |
| Lautstärke- und Medientasten | `KEY_VOLUMEUP`, `KEY_VOLUMEDOWN`, `KEY_MUTE`; weitere vom Gerät gelieferte Play-/Titeltasten | Lautstärke/Stumm beobachtet; andere Tasten je Modell testen |
| HID-Makropads und USB-Fußtaster | Gleiche Verarbeitung, wenn Linux normale Tastencodes meldet | Modellabhängig; Rückmeldungen willkommen |
| Physische Elgato Stream Decks | Eigener HID-Treiber, Display- und Bedienfunktionen unten | Implementiert, noch kein physischer Stream-Deck-Test dieses Projekts |
| Andere Geräte mit LCD-Tasten | Tastencodes eventuell über HID; Displayfunktionen brauchen den passenden Herstellertreiber | Keine allgemeine Kompatibilitätszusage |
| Drucker, Kameras, USB-Speicher, Audiointerfaces, serielle Geräte und weitere Controller | Bestandsanzeige; besondere Nutzfunktionen brauchen eigene Adapter | Keine allgemeine Druck-, Kamera-, Audio-, MIDI- oder serielle Weiterleitung |
| Stream Deck Mobile / Tablet-App | Kein direktes USB-Gerät am Pi | Derzeit nicht angebunden |

Ein angezeigtes Gerät ist nicht automatisch aktiviert. Unter **USB-Geräte** kannst
du einen Namen vergeben, **Gerät für Eingaben freigeben** wählen und die Zielbroker
ankreuzen. Geräte ohne Seriennummer werden anhand ihres USB-Ports zugeordnet;
beim Umstecken kann eine neue Zuordnung nötig sein.

[![USB-Bestand und ausdrückliche Eingabefreigabe](/images/usb-extender/devices.png)](/images/usb-extender/devices.png)

## Installation auf dem Pi {#installation}

Empfohlen sind Raspberry Pi 4 und Raspberry Pi OS Lite **64 Bit, Bookworm oder
neuer**, Python 3.11+, systemd, sudo sowie Internet für apt/PyPI. Mehrere Geräte
mit Displays benötigen gegebenenfalls einen aktiven USB-Hub mit eigener Versorgung.
32-Bit-Pi-OS ist noch nicht praktisch bestätigt.

ZIP auf den Pi kopieren, im Terminal in den Downloadordner wechseln und ausführen:

```bash
sudo apt-get update && sudo apt-get install -y unzip
unzip USB-Extender-Home-Assistant-0.1.5-Raspi4.zip
cd USB-Extender-Home-Assistant-0.1.5
sudo bash install.sh
```

Der Installer zeigt neun Schritte, prüft Abhängigkeiten und installiert Fehlendes.
Bei Updates sichert er vorhandene Daten unter `/var/backups/`; Einstellungen und
Icons bleiben erhalten. Das ZIP ist kein vollständig offline nutzbares Systemabbild.
Für spätere Updates das neue ZIP separat entpacken und dessen Installer ausführen.

Beim ersten Einrichten ein Webpasswort setzen; es gibt kein installiertes
Standardpasswort. Falls nötig: `sudo usb-extender password`. Dann:

```bash
sudo usb-extender web start
```

Im Browser `http://<IP-des-Pi>:8098` öffnen und anmelden. Die Beispieladressen auf
den Bildern durch die eigenen Brokeradressen ersetzen. HTTP nur im vertrauten
lokalen Netz verwenden, ansonsten VPN/HTTPS davor setzen; nicht ins Internet freigeben.

## Broker einrichten und Tasten anlernen {#setup}

1. Unter **MQTT-Broker** Host, Port und gegebenenfalls Zugangsdaten eintragen.
   Gewünschte Verbindungen aktivieren und speichern. Pro Broker arbeitet eine
   eigene Verbindung; eine Taste kann alle drei Ziele erreichen.
2. Auf HA-Brokern Discovery aktivieren. Für ioBroker **Aus – nur MQTT-Daten senden**
   wählen, damit der HA-Discovery-Adapter nicht über Geräteauslöser klagt.
3. Unter **USB-Geräte** Gerät benennen, freigeben, Ziele wählen und speichern.
4. Unter **Tasten & Anzeigen** das Gerät wählen und **Anlernen starten** drücken.
   Jede gewünschte Taste einmal drücken und loslassen. Wiederholte und bereits
   vorhandene Tasten werden nicht doppelt angelegt.
5. **Anlernen beenden → Tasten übernehmen → Speichern**. Erst jetzt sind neue
   Zeilen aktiv. Während des Anlernens sendet das ausgewählte Gerät keine Aktionen.
6. Pro Zeile Kanäle abwählen oder Topics/Namen ändern. **Bearbeiten** öffnet
   Brokerwahl, Switch-Verhalten und Zeitwerte. Neue Zusatzkanäle vorhandener
   Zeilen bleiben zunächst aus; neu angelernte Zeilen haben alle Kanäle vorbereitet.

[![Drei Brokerplätze im Praxisaufbau](/images/usb-extender/brokers.png)](/images/usb-extender/brokers.png)

[![Anlernmodus mit gewähltem USB-Gerät](/images/usb-extender/learning.png)](/images/usb-extender/learning.png)

Wird das Browserfenster während des Anlernens geschlossen, endet die Pause
spätestens nach 15 Sekunden ohne Rückmeldung. Anlernentwürfe liegen bis zum
Übernehmen/Speichern nur im Browser. Bereits gespeicherte Belegungen bleiben erhalten.

## Topics und Tastenfunktionen {#topics}

Aus Gerätename **Trust1** und Taste **F1** entsteht beispielsweise
`trust1-key-f1/press`. Namen werden MQTT-tauglich geschrieben; Umlaute wie in
„Büro“ werden zu `buero`. Doppelte Gerätenamen bekommen bei Bedarf `-2`, `-3` usw.
Gespeicherte Topics bleiben bei späterer Umbenennung stabil und haben an allen
ausgewählten Brokern denselben Namen. Sie lassen sich einzeln bearbeiten.

| Endung hinter `trust1-key-f1` | Nachricht und Funktion |
| --- | --- |
| `/press` | `press` sofort beim Drücken |
| `/release` | `release` beim Loslassen |
| `/press-plus`, `/release-plus` | Gleiche Aktion, nach 50 ms leere Nachricht auf genau diesem Kanal |
| `/switch` | Erster Druck `ON`, nächster Druck `OFF`; Loslassen ändert nichts |
| `/state` | Gedrückt `ON`, losgelassen `OFF` |
| `/button` | Je nach Bedienung `click`, `double_click` oder `hold` |
| `/button-plus` | Gleiche Button-Aktion, danach nach 50 ms leer |
| `/click`, `/double-click`, `/hold` | Die jeweilige einzelne Geste |

`plus` wird ausgeschrieben, weil `+` in MQTT ein Platzhalter ist. Alle elf Kanäle
sind einzeln aktivierbar. Nur die Plus-Kanäle werden leer zurückgesetzt; leer
bedeutet **nicht** Loslassen. Der Switch-Wert bleibt in `switches.json` über
App-Neustarts erhalten und wird beim Wiederverbinden erneut synchronisiert.

**Klick/Doppelklick/Halten:** Ein Klick wartet das Doppelklick-Fenster ab
(Vorgabe 300 ms nach Loslassen). Ein zweiter Klick darin ergibt nur `double_click`.
Halten ab 700 ms ergibt einmal `hold`, ohne Klick beim Loslassen. Wird der zweite
Druck gehalten, ersetzt Hold die wartende Klickfolge. Zeiten sind pro Taste einstellbar.
Normale Tastaturwiederholungen zählen nicht als weitere Klicks oder Switch-Betätigungen.

**Lauter/Leiser:** Aktive Press-/Press+-Kanäle können beim Halten wiederholt werden,
standardmäßig nach 500 ms alle 150 ms. Loslassen beendet die Wiederholung; zusätzlich
gilt ein Sicherheitsstopp nach 30 Sekunden. Die Lautstärkeschrittweite bestimmt
deine HA-Automation bzw. ioBroker-Logik. Normale Press-/Release-Kanäle bleiben
unabhängig von der verzögerten Button-Erkennung sofort verfügbar.

Die App sendet Tastenmeldungen mit QoS 0 und ohne Retain. Offline-Eingaben werden
nicht nachgesendet. Mehrere aktive Kanäle können mehrere zugeordnete Automationen
auslösen; für eine einzelne Funktion den passenden Kanal auswählen.

## Anzeige in Home Assistant und ioBroker {#integration}

HA-Discovery fasst alle Tasten unter dem gewählten Gerätenamen mit einer gemeinsamen
stabilen Gerätekennung zusammen. Aktionen werden als Geräteauslöser mit Payloadfilter
angeboten. Switch und Tastenzustand sind **Binärsensoren**, die Zustände anzeigen;
zum Schalten anderer Geräte braucht es eine Automation oder Zuordnung.

<img src="/images/usb-extender/ha-states.png" alt="HA zeigt Switch Ein und Tastenzustand Aus nach dem Loslassen" width="280">

Im Nutzerbild ist Switch nach der Betätigung **Ein**, der Tastenzustand nach dem
Loslassen **Aus**. Zunächst unbekannte Werte können vor der ersten empfangenen
Zustandsmeldung auftreten; das ist kein Nachweis einer defekten Tastenerkennung.

<details><summary>Bild vor den ersten Zustandsmeldungen</summary>

<img src="/images/usb-extender/ha-before.png" alt="HA-Zustände vor den ersten empfangenen Tastenwerten" width="280">

</details>

In ioBroker entstehen unter dem MQTT-Adapter einzelne Datenpunkte, sobald die
jeweiligen Topics erstmals empfangen werden. Das Praxisbild zeigt einfache Werte
wie `press`, `release`, `click`, `hold`, `ON` und `OFF`. Plus-Kanäle stehen nach der
leeren Rücksetzung hier auf `(null)`. Das ist erwartbar; der Datenpunkt bleibt bestehen.
Ein Doppelklick-Datenpunkt erscheint erst, wenn tatsächlich eine passende Nachricht
gesendet wurde. Alte Datenpunkte mit dem früheren JSON-Ereigniswert ändern sich
nicht automatisch. Discovery-Konfigurationen bleiben absichtlich JSON.

[![Einzelne Datenpunkte mit einfachen Werten in ioBroker](/images/usb-extender/iobroker-states.png)](/images/usb-extender/iobroker-states.png)

## Stream Deck und ähnliche Geräte {#stream-deck}

Der integrierte `python-elgato-streamdeck`-Treiber 0.10.0 kennt unter anderem
Original/MK.2, Mini, XL, Neo, Pedal und Plus. Diese Modellliste beschreibt den
Treiberumfang, **keinen bereits durchgeführten Hardwaretest** dieses Projekts.

- Displaytasten: eigene Icons und Text, Helligkeit pro Gerät, MQTT-Zustandsrückmeldung
  zum Wechseln eines Icons und gezielte Displayaufträge.
- Tasten: Press/Release, Klick/Doppelklick/Hold, Switch und Tastenzustand wie oben.
- Drehregler, wenn vorhanden: Drehrichtung und Druck als Eingaben.
- Touchscreen, wenn vorhanden: Touch-Ereignisse; kein frei gestaltbarer Touchscreen-Editor.
- Pedal und andere Modelle ohne Display: Eingaben, aber keine Display-Icons.
- Eine feste Belegung; Profil-/Seitenwechsel und animierte Tastenicons sind noch offen.

Unter **Iconbibliothek** eigene Bilddateien oder einen Ordner auf dem Pi einlesen.
Auch lokal gespeicherte ZIP- und `.streamDeckIconPack`-Pakete sind möglich. Es wird
nichts automatisch aus dem Elgato Marketplace heruntergeladen. Rechte des jeweiligen
Iconpacks beachten; bei Animationen nutzt die App das erste Bild.

Bei Fremdgeräten mit ähnlicher Optik kann der Tastaturteil bereits über HID
funktionieren. LCDs, Touch und herstellerspezifische Befehle benötigen eventuell
einen eigenen Adapter. Bitte ein konkretes Modell testen und berichten, statt
von der äußeren Ähnlichkeit auf vollständige Kompatibilität zu schließen.

## Weboberfläche abschalten und sichern {#operation}

```bash
sudo usb-extender web start
sudo usb-extender web stop
sudo usb-extender web status
sudo usb-extender web enable
sudo usb-extender web disable
sudo usb-extender backup
sudo journalctl -u ugso-usbhub -n 50
```

`web stop` beendet den HTTP-Listener; das Schließen des Browsers allein tut das
nicht. Der USB-/MQTT-Dienst läuft weiter. Einstellungen, Icons und Switch-Werte
liegen unter `/var/lib/ugso-usbhub/`. Die letzten zehn Konfigurationsstände werden
automatisch gesichert; eine vollständige CLI-Sicherung enthält auch Icons und
Switch-Werte. Backups nicht öffentlich hochladen.

[![Systembefehle und Diagnoseseite](/images/usb-extender/system.png)](/images/usb-extender/system.png)

## Was ist praktisch nachgewiesen? {#tests}

Die Nutzerbilder zeigen 0.1.5, drei online gemeldete Brokerplätze, angelernte
Funktionstasten, HA-Zustände und einzelne ioBroker-Datenpunkte. Im Verlauf ist die
Übergabe an HA, IOB und Testserver sichtbar. Die Übergabeanzeige allein beweist
keinen Empfang bei jedem Broker; HA-/ioBroker-Bilder liefern den zusätzlichen
sichtbaren Nachweis. Nicht jede Funktion ist dadurch an jeder Hardware geprüft.

[![F12-Ereignisse mit ausgewählten Topics und drei MQTT-Zielen](/images/usb-extender/events.png)](/images/usb-extender/events.png)

Zusätzlich bestehen 61 lokale Python-Prüfungen und zwei JavaScript-/DOM-Prüfläufe,
unter anderem für Doppelklick, Switch-Neustartpersistenz, Routing und Fehlerfälle.
Ein physischer Stream-Deck-Test bleibt offen.

## Eigene Hardware testen und Rückmeldung geben {#feedback}

Besitzt du ein Stream Deck, ein ähnliches LCD-Tastengerät, Makropad oder USB-Pedal?
Teste es gern und [melde deine Ergebnisse auf GitHub](https://github.com/rockbaer2007/usb-extender-home-assistant/issues/new?template=hardware-test.yml).
Fehlerberichte und Mitarbeit sind willkommen.

Bitte Modell/Revision, Pi-Modell, Betriebssystem und App-Version nennen. Unterscheide
Bestandsanzeige und echte Tastencodes. Berichte getrennt über Drücken/Loslassen,
Klick/Doppelklick/Halten, Icons/Text, Helligkeit, Drehregler, Touch und Wiederanstecken;
nicht geprüfte Funktionen ausdrücklich so markieren. Nutze zuerst ein unkritisches
MQTT-Topic ohne echte Geräteaktionen. Screenshots von Bestand und Ereignissen helfen.
Keine Passwörter, Tokens, `config.json` oder Sicherungsarchive veröffentlichen.
