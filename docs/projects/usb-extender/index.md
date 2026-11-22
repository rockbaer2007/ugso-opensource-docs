---
title: USB Extender für Home Assistant
description: USB-Tasten, Stream Decks und Makropads über bis zu drei MQTT-Broker verbinden. Installation, Anlernen, Topics und Praxistest mit Bildern.
---

# USB Extender für Home Assistant

**0.1.35 · Öffentliches Testrelease · Raspberry Pi · Stand 22. November 2026**

Eine USB-Tastatur am Raspberry Pi kann zum Bedienteil für Home Assistant oder
ioBroker werden. Der USB Extender erkennt Eingaben und sendet sie über MQTT an
bis zu **drei Broker gleichzeitig**. Die Weboberfläche dient zum Einrichten und
kann danach abgeschaltet werden; USB und MQTT laufen unabhängig weiter.

[GitHub / README DE und EN](https://github.com/rockbaer2007/usb-extender-home-assistant)
· [ZIP 0.1.35 und SHA256](https://github.com/rockbaer2007/usb-extender-home-assistant/releases/tag/v0.1.35)
· [Änderungen](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/CHANGELOG.md)

Dies ist ein eigenständiges Raspberry-Pi-Programm, keine HA-App zum Installieren
im App-Store und keine offizielle Software von Home Assistant oder Elgato.
Es ist **kein USB-over-IP-Tunnel**: Drucker oder Kameras werden damit nicht als
entfernte USB-Geräte an HA durchgereicht.

Die Bilder stammen aus dem echten Nutzeraufbau mit 0.1.5. Die Oberfläche ist
derzeit deutsch. Breite Bilder lassen sich durch Anklicken in Originalgröße öffnen.

[![Breite Tastenliste mit MQTT-Kanälen](/images/usb-extender/key-list.png)](/images/usb-extender/key-list.png)

## Neu in 0.1.35: Barcode-/QR-Scanner und HA-Tags {#release-035}

USB-HID-Tastaturscanner erhalten einen eigenen, zunächst ausgeschalteten Modus.
Unter **USB / Virtuelle Geräte** das Gerät freigeben, Scanner-Modus aktivieren,
**DE/US-Layout**, Abschluss **Enter/Tab/Scanpause**, eigenes Topic und Zielbroker
wählen, dann speichern. Beispiel: `barcodescanner`. Eine Pause von 500 ms ist
vorbelegt; lange oder unvollständige Eingaben werden verworfen. Serielle Scanner,
beliebige Unicode-Eingaben und GS1-Steuersequenzen sind nicht unterstützt.

Jeder vollständige Scan wird als reiner Text ohne Retain gesendet. Gleiche Codes
lösen bei jedem Scan erneut aus; vom Gerät gelieferte führende Nullen bleiben
erhalten. QR-Links werden nicht geöffnet und enthaltene Befehle nicht ausgeführt.
Die Vorschau zeigt den letzten Rohtext. Vorhandene Tastenaktionen dieses Geräts
pausieren im Scanner-Modus; ihre Belegungen bleiben gespeichert.

### Wo kommen die Scans in Home Assistant an? {#scanner-ha}

Am HA-Zielbroker Discovery einschalten. Der Scanner wird über die native
[MQTT-Tag-Integration](https://www.home-assistant.io/integrations/tag.mqtt/)
angemeldet. Scans erscheinen als **`tag_scanned`-Ereignisse**, nicht als normale
Sensorentitäten. Unter **Einstellungen → Tags** den Tag benennen und eine
Tag-Automation anlegen, etwa zum Umschalten einer Lampe. Die Aktion wird in HA
festgelegt. Dafür braucht USB Extender keinen HA-Zugriffstoken.

Optional wird `https://www.home-assistant.io/tag/werkstattlicht` als Tag-ID
`werkstattlicht` gesendet. Andere Texte bleiben unverändert. ioBroker erhält auf
dem gewählten Topic den Textwert; dort kann Discovery ausgeschaltet bleiben.

### Erfolgreicher Aplic-305045-Praxistest {#scanner-test}

Am **22. November 2026** wurden auf Raspberry Pi .112 mit 0.1.35 vier echte Scans
ausgeführt: Barcode zweimal, Text-QR und HA-Tag-QR. Jeder Scan wurde an drei Broker
übergeben; auf HA .193 wurden vier getrennte native Ereignisse empfangen.
ioBroker-Empfang auf `barcodescanner` ist ebenfalls bestätigt. Wiederholte Codes
werden nicht verschluckt. Abschluss: USB-/MQTT- und Webdienst aktiv, keine Neustarts
oder gemeldeten Fehler. Keine HA-Aktion wurde beim Test ausgeführt.

[Vollständiger Test und Prüfgrenzen](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/v0.1.35/docs/tests/scanner-live-0.1.35-20261122.md).
Die vor Beginn geprüfte Sicherung war beim Abschlussvergleich nicht mehr am
aufgezeichneten Pfad; ein abschließender Hashnachweis der Metadaten ist daher
nicht Bestandteil dieses Tests. Einstellungen und Kopplungen wurden vom Agenten
nicht verändert. Neustart-/Abschaltprüfung der Scanner-Discovery bleibt ergänzend offen.

### Weitere enthaltene Funktionen aus 0.1.32–0.1.34 {#values-gamepad}

- **Logitech Touchpad T650:** acht einzeln aktivierbare Richtungswerte und X/Y mit eigenen Topics
  und HA-Sensoren, reine Zahlen 0–100. Alle zehn Live-Werte auf HA bestätigt.
- **Alternativer Flächenmodus:** fünf senkrechte Regler. Aufsetzen wählt den
  Streifen, der bis zum Abheben fest bleibt; oben 100, unten 0. Richtungsaktionen
  pausieren, ihre Einstellungen bleiben erhalten. X/Y bleibt unabhängig. Aktive
  Regler sind türkis, Richtungen goldfarben, pausierte Bereiche grau; Werte und
  letzter Trigger werden sichtbar. Fünf echte Werte in ioBroker bestätigt.
- **DragonRise-Gamepad `0079:0006`:** linker Stick `ABS_X/ABS_Y`, rechter Stick
  `ABS_RX/ABS_RZ`, je 0–100 und Mitte 50, eigene Topics und HA-Sensoren. Ausgabe
  ausdrücklich einschalten; Rate 1–30/s je Achse. `ABS_Z` wird ignoriert. L1/R1,
  L2/R2 und Stick-Klicks wie normale Tasten anlernen; L2/R2 sind digital. Zuordnung
  am Gerät gemessen, neue MQTT-Verarbeitung lokal geprüft; kein allgemeines Profil
  für jedes Gamepad. Weitere Praxisprüfungen sind in der Roadmap dokumentiert.

## Bereits in 0.1.31: Logitech Touchpad T650, Geräte und sicherer Installer {#release-031}

0.1.31 enthält auch die zuvor lokalen Änderungen aus 0.1.29 und 0.1.30.
Unter **Tasten & Anzeigen** sind Geräte alphabetisch gruppiert und zunächst
eingeklappt. Jeweils nur eine Gerätegruppe und eine Taste ist geöffnet.
Lautstärke-, Bildschirmhelligkeits- und Tastaturlichttasten bieten unter
**Bearbeiten** den Schrittfilter 1–5: bei 3 werden Schritt 3, 6, 9 usw. gesendet.
Loslassen stoppt die Lautstärke-Haltewiederholung auch bei übersprungenen Schritten.

Eindeutige Seriennummern und verfügbare Logitech-HID++-Kennungen erhalten die
Gerätezuordnung beim Umstecken. Ohne eindeutige Kennung das neue USB-Gerät einem
gespeicherten Offline-Gerät zuordnen; vorhandene Tasten, Seiten und Topics bleiben.
Entfernen über den Papierkorb verlangt eine Bestätigung und sichert Metadaten;
gemeinsame Icons bleiben erhalten. Mobile-Vertrauen wird separat widerrufen.

### Logitech Touchpad T650: Ein-Finger-Slide und X/Y {#t650}

Unter **USB / Virtuelle Geräte** das T650 freigeben, **Touchpad-Gesten auswerten**
einschalten und **Ein-Finger-Slide und optionale X/Y-Werte** öffnen. Empfindlichkeit
und Senderate einstellen, speichern und danach die gewünschten Richtungen anlernen.
Der Linux-Treiber muss Type-B-Multitouch liefern; ein bloßes Klickereignis reicht nicht.

| Bewegung | Anlernbare Aktion |
| --- | --- |
| Links / rechts | `TOUCHPAD_SLIDE_LEFT` / `TOUCHPAD_SLIDE_RIGHT` |
| Oben / unten | `TOUCHPAD_SLIDE_UP` / `TOUCHPAD_SLIDE_DOWN` |
| Links oben / rechts oben | `TOUCHPAD_SLIDE_UP_LEFT` / `TOUCHPAD_SLIDE_UP_RIGHT` |
| Links unten / rechts unten | `TOUCHPAD_SLIDE_DOWN_LEFT` / `TOUCHPAD_SLIDE_DOWN_RIGHT` |

Acht 45°-Sektoren unterscheiden die Richtungen. Die **Empfindlichkeit 1–10** legt
die nötige Bewegung fest: 10 empfindlicher, 1 größere Bewegung; Standard 5.
Die **Senderate 1–30/s** ist eine Obergrenze je Richtungsaktionsstrom und X/Y-Paar,
Standard 10/s. Ein X/Y-Paar sind zwei MQTT-Nachrichten je Zielbroker; zusätzliche
aktivierte Tastenkanäle können weitere Nachrichten erzeugen.

**X/Y ist standardmäßig aus.** Bei Aktivierung werden beim Speichern lesbare Topics
angelegt, etwa `t650-touchpad/x` und `t650-touchpad/y`. Eigene Topics sind möglich;
gespeicherte Topics bleiben bei Umbenennung erhalten. Beide Achsen nutzen die
Geräte-Zielbroker und senden reine ganze Zahlen **0–100**, kein JSON. X: links 0,
rechts 100; Y: oben 0, unten 100. Das ist die absolute Touchpad-Position.

Nach erkanntem Slide entsteht beim Abheben kein zusätzlicher Tipp. Unveränderte
Positionen werden nicht erneut gesendet. Ein letzter ausstehender Wert darf nach
dem Abheben im nächsten erlaubten Intervall folgen. Mehrfingerkontakt, mechanischer
Klick, Eingabeverlust oder Optionsänderung verwerfen ausstehende Werte. Kein Retain,
kein Nachsenden an zuvor getrennte Broker; im Anlernmodus bleibt X/Y stumm.

### Logitech Touchpad T650: Praxistest und Grenzen {#t650-test}

Am 22. November 2026 auf einem Raspberry Pi 4 (64 Bit) mit echtem T650:

- Alle acht erwarteten Richtungen erkannt; **kein Tipp** in den Slide-Phasen.
  Separates Tippen erzeugte vier Tipps und keine X/Y-Ausgabe.
- Drei lokale MQTT-Testbroker erhielten jeweils **752 identische Nachrichten**,
  darunter 200 X/Y-Paare. Achsenwerte sind reine Zahlen innerhalb 0–100.
- **Live**: Empfindlichkeit 5, Rate maximal 10/s; kleinster Abstand 0,100000 s.
- **Replay derselben echten Aufnahmen**: Empfindlichkeit 1/5/10 ergab bei schnellen
  Bewegungen 33/38/39 Slide-Aktionen. Rate 1/5/30 ergab minimale X/Y-Abstände von
  1,006229 / 0,201979 / 0,037912 s. Das ersetzt keinen zusätzlichen Live-Test der
  Web-Einstellung oder neuer Handbewegungen mit jedem Wert.
- Zwei benachbarte Richtungsereignisse und einmal Halten wurden mitprotokolliert.
  Keine Garantie ausschließlich einer Richtung für jede Handbewegung und kein
  allgemeiner Hardware-Nachweis für andere Mehrfingergesten oder Touchpad-Modelle.
- Nur das T650 wurde ausgewertet; K400/T400 blieben unverändert. Die isolierte
  Messung nutzte temporäre Einstellungen und Loopback-Broker, keine produktiven Ziele.

[Vollständiger T650- und Installationsbericht](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/v0.1.31/docs/tests/t650-0.1.31-20261122.md).
Das Messwerkzeug wurde ebenfalls korrigiert: begrenztes Pufferleeren konsumiert
den evdev-Generator; sichtbarer Start und Sekundenanzeige verhindern unklare Wartephasen.

### Installer-Korrektur und Datenerhalt {#installer-031}

Eine vererbte `umask 077` konnte die neue Python-Umgebung für das Dienstkonto
unzugänglich machen (`Permission denied` in Schritt 6). Der Installer setzt jetzt
`umask 022` für Programmdateien und `umask 077` für private Sicherungsarchive.
Keine pauschale Rechteänderung an Nutzdaten nötig.

Die anschließende Installation ist auf dem Pi bestätigt: CLI und laufender Dienst
melden **0.1.31**, USB/MQTT und Web sind aktiv, beide mit **NRestarts=0**. Mobile
ist aktiv, die Fehlerliste leer. Fünf SHA256-Prüfungen für `config.json`,
`switches.json`, `mobile-identity.json`, `mobile-trust.json` und `mobile-devices.json`
bestätigen bytegleich erhaltene Einstellungen und Kopplungen. Vorab wurde gesichert.
Dies ist eine Dienststartprüfung, kein zusätzlicher Langzeittest nach Installation.

## Welche Geräte werden erkannt? {#hardware}

**Erkannt** bedeutet zunächst: Linux kann das USB-Gerät auflisten. **Bedienbar**
bedeutet zusätzlich: Ein Treiber kann seine Eingaben lesen und das Gerät ist in
der Oberfläche ausdrücklich freigegeben. Das ist nicht dasselbe.

| Gerät | Was bereits vorgesehen ist | Prüfstand |
| --- | --- | --- |
| USB-Tastaturen, auch Windows-Medientastaturen | Tastencodes, Drücken/Loslassen, Umschalter, Tastenzustand, Klick/Doppelklick/Halten | Trust-/HCT-Tastaturen im Praxisaufbau genutzt |
| Lautstärke- und Medientasten | `KEY_VOLUMEUP`, `KEY_VOLUMEDOWN`, `KEY_MUTE`; weitere vom Gerät gelieferte Play-/Titeltasten | Lautstärke/Stumm beobachtet; andere Tasten je Modell testen |
| HID-Makropads und USB-Fußtaster | Gleiche Verarbeitung, wenn Linux normale Tastencodes meldet | Modellabhängig; Rückmeldungen willkommen |
| USB-HID-Barcode-/QR-Scanner | Text-MQTT und native HA-Tag-Discovery | Aplic 305045 mit Barcode-Wiederholung, Text-QR und HA-Tag praktisch bestätigt |
| DragonRise-Gamepad 0079:0006 | Vier Stickwerte 0–100 und normale Tasten | Hardwarezuordnung gemessen, neue MQTT-Verarbeitung lokal geprüft |
| Logitech Touchpad T650 | Acht Slide-Richtungen, optionale Werte/X/Y, alternativ fünf senkrechte Regler | Richtungen/X/Y in HA, fünf Reglerwerte in ioBroker bestätigt; Prüfgrenzen siehe oben |
| Physische Elgato Stream Decks | Eigener HID-Treiber, Display- und Bedienfunktionen unten | Implementiert, noch kein physischer Stream-Deck-Test dieses Projekts |
| Andere Geräte mit LCD-Tasten | Tastencodes eventuell über HID; Displayfunktionen brauchen den passenden Herstellertreiber | Keine allgemeine Kompatibilitätszusage |
| Drucker, Kameras, USB-Speicher, Audiointerfaces, serielle Geräte und weitere Controller | Bestandsanzeige; besondere Nutzfunktionen brauchen eigene Adapter | Keine allgemeine Druck-, Kamera-, Audio-, MIDI- oder serielle Weiterleitung |
| Stream Deck Mobile / Android-App | Optionaler experimenteller Netzwerkserver mit QR-Kopplung, Bildern und MQTT | Kopplung, Iconübertragung, Farben und 8×8-Raster vom Nutzer bestätigt; Langzeitstabilität noch offen |

Ein angezeigtes Gerät ist nicht automatisch aktiviert. Unter **USB / Virtuelle Geräte** kannst
du einen Namen vergeben, **Gerät für Eingaben freigeben** wählen und die Zielbroker
ankreuzen. Eindeutige Serien-/Gerätekennungen sind portunabhängig; ohne solche
Kennung beim Umstecken ausdrücklich einem gespeicherten Offline-Gerät zuordnen.

[![USB-Bestand und ausdrückliche Eingabefreigabe](/images/usb-extender/devices.png)](/images/usb-extender/devices.png)

## Installation auf dem Pi {#installation}

Empfohlen sind Raspberry Pi 4 und Raspberry Pi OS Lite **64 Bit, Bookworm oder
neuer**, Python 3.11+, systemd, sudo sowie Internet für apt/PyPI. Mehrere Geräte
mit Displays benötigen gegebenenfalls einen aktiven USB-Hub mit eigener Versorgung.
32-Bit-Pi-OS ist noch nicht praktisch bestätigt.

ZIP auf den Pi kopieren, im Terminal in den Downloadordner wechseln und ausführen:

```bash
sudo apt-get update && sudo apt-get install -y unzip
unzip USB-Extender-Home-Assistant-0.1.35-Raspi4.zip
cd USB-Extender-Home-Assistant-0.1.35
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
3. Unter **USB / Virtuelle Geräte** Gerät benennen, freigeben, Ziele wählen und speichern.
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
- Bis zu acht eigene Seiten je Deck mit Navigationstasten; zusätzliche Profile bleiben offen. Animierte Tastenicons sind implementiert.

### Grafischer Editor und kompakte Tastenliste {#editor}

Der Tab **Stream Deck** bleibt offline sichtbar und erhält Editor und letztes Raster.
Gerät freigeben und speichern, dann eine Taste auswählen: Beschriftung, Icon,
Hintergrundbild, Textposition und Farben bearbeiten. Für **gedrückt** gibt es ein
zweites Icon und eigene Text-/Hintergrundfarben. Text oben/unten erhält Platz neben
dem eingepassten Icon. Die Vorschau sendet keine MQTT-Aktion. Danach speichern.

[![Editor mit simuliertem Deck](/images/usb-extender/editor-022.png)](/images/usb-extender/editor-022.png)

Dieses Bild zeigt eine **lokale Browser-Demo**, keinen Hardwaretest.
In **Tasten & Anzeigen** steht eingeklappt nur **Gerät – Key – Name**; immer nur
eine Taste ist aufgeklappt. **Speichern** sichert alle ausstehenden Änderungen,
**Abbrechen** verwirft nur die Änderungen dieser Taste. Hinweise markieren
ungespeicherte Änderungen. **Bearbeiten** öffnet erweiterte MQTT- und Zeitoptionen.

## Seiten und Navigation auf dem Deck {#pages}

**USB / Virtuelle Geräte** fasst USB-Geräte und gekoppelte Mobile-Decks zusammen.
Handy und Tablet behalten jeweils ihre eigenen Seiten, Gestaltung und Zuordnungen.

1. Im Tab **Stream Deck** mit **Neue Seite** bis zu acht Seiten je Gerät anlegen.
   Die Tasten zählen weiter: bei 15 Tasten 1–15, danach 16–30; bei 8×8 1–64,
   danach 65–128. Das Raster kommt weiterhin vom Gerät bzw. der Android-App.
2. Taste auswählen und unter **Gestaltung → Tastenfunktion** MQTT, **Vor**,
   **Zurück**, **Home** oder **Gehe zu** wählen. Bei Gehe zu die **Zielseite** wählen.
   Nach **Speichern** navigieren diese Tasten direkt am Tablet, ohne MQTT-Aktion.
3. **Seitennummer anzeigen** ergänzt einen kleinen Zähler. Home führt zu Seite 1;
   Vor/Zurück bleiben an den Grenzen stehen. Die Editorbuttons wechseln nur die
   Vorschau, nicht die tatsächlich am Gerät sichtbare Seite.
4. **Aktuelle Seite löschen** entfernt nach Rückfrage deren Belegungen;
   **Seite 1 ist geschützt**. Erst Speichern übernimmt Änderungen. Andere Seiten
   behalten ihre IDs/Topics, auch wenn sichtbare Nummern nachrücken. Gehe-zu-Ziele
   folgen nachrückenden Seiten; beim Löschen des Ziels führt die Taste zu Seite 1.

Navigation blendet bestehende MQTT-Zuordnungen nur aus; beim Zurückstellen auf
MQTT werden sie wieder aktiv. Neue Seiten erhalten stabile Topics wie
`tablet-page-2-key-0/press`; vorhandene Topics der ersten Seite bleiben erhalten.
Nach Dienstneustart startet jedes Deck auf Seite 1. Seitenwechsel beenden
gehaltene Tasten/Klickfolgen; Rückmeldungen anderer Seiten überschreiben die
sichtbare Seite nicht. Farbfelder und übrige Gestaltungsfelder sind kompakter.

[![Deck-Seiten und kompakte Gestaltung, lokale Simulation](/images/usb-extender/pages-028.png)](/images/usb-extender/pages-028.png)

## Stream Deck Mobile: optional und experimentell {#mobile}

1. Unter **Mobile-Server** aktivieren, erreichbare Pi-Adresse und Port (Standard
   **28198**) eintragen und speichern.
2. **Kopplung starten · QR-Code** wählen und in Android mit **Computer hinzufügen** scannen.
3. Den sechsstelligen Prüfabdruck vergleichen und nur bei Übereinstimmung unter
   **Mobile-Verbindungen** auf **Gerät vertrauen** klicken. Vertrauen bleibt gespeichert.
4. In Android ein Deck öffnen, das Mobile-Gerät im USB Extender freigeben und
   speichern. Im Stream-Deck-Editor Gestaltung und MQTT zuordnen.
5. **Zeilen und Spalten in Android einstellen.** Der Editor übernimmt das gemeldete
   Raster bis 8×8; keine eigene Rasterübersteuerung.

Der Mobile-Dienst läuft unabhängig vom Webdienst. Die Weboberfläche wird zum
Koppeln benötigt und darf danach abgeschaltet werden. Lokaler WebSocket-Port,
keine Cloud-/Bonjour-Erkennung; keine Veränderung der Pro-Kaufberechtigung der App.

**Mobile-Verbindungen** zeigt Bild-/Metadatenzähler, Ping/Pong und letzte Trennung.
Bei unveränderten **statischen** Tasten sollen die Bildzähler stehen bleiben.
Keepalive hält die Verbindung ohne neue Bilder; Animationen senden absichtlich
weitere Bilder. Kopplung, Iconanzeige, Farben und 8×8 wurden vom Nutzer bestätigt.
Der unten dokumentierte 15-Minuten-Test mit Navigation und Leerlauf ist bestanden.

### 0.1.28: erfolgreiche 15-Minuten-Prüfung {#stability}

Bildübertragung wird in kleine Pakete aufgeteilt: maximal vier Bilder je
Durchlauf mit einem weichen 25-ms-Arbeitsbudget. Zwischen Paketen werden
Eingaben und Heartbeat wieder bedient. Ein bereits laufender Socket-Sendevorgang
kann länger dauern; der Heartbeat-Timeout bleibt bei 20 Sekunden. Das Journal
enthält bei Trennung zusätzlich Ping/Pong, letzte Nachrichtenart/Alter und
ausstehende Bilder, aber keine Nachrichteninhalte oder Zugangsdaten.

Am **22. November 2026** wurde das echte **SM-T580 mit 8×8 und zwei Seiten**
über 900 Sekunden beobachtet: zunächst mehrfach Vor/Zurück, anschließend rund
14 Minuten Leerlauf. Der Monitor wurde vom Nutzer per SSH gestartet; seine
16 Messpunkte und das abschließende Journal wurden direkt ausgewertet.

| Messung | Ergebnis |
| --- | --- |
| Zeitraum laut Pi-Uhr | 11:39:17–11:54:17; Dauer über monotone Zeit gesteuert |
| Tablet-Verbindung | In allen 16 Messpunkten geöffnet und autorisiert |
| Ping/Pong | 56/56 → 232/232; zusätzlich 176 Pings vollständig beantwortet |
| Leerlauf | 1.228 Bilder / 19 Metadatenpakete ab Minute 1 unverändert |
| Abschließendes Journal | Kein neuer Heartbeat-Timeout, keine Trennung, kein Dienstneustart |

Ein zusätzlicher „connection open“-Eintrag nennt kein Gerät; Tablet-Zähler
steigen ohne Rücksetzung weiter. [Vollständiger Messbericht](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/docs/tests/mobile-0.1.28-15min-20261122.md).
Der Test ist für diesen Zeitraum bestanden. Bildschirmabschaltung,
App-Hintergrundbetrieb, andere Netze und physische Stream Decks sind damit nicht
geprüft; die Ursache aller früheren Abbrüche ist nicht rückwirkend bewiesen.

## Iconbibliothek, Animationen und Paketimport {#icons}

**Grafische Auswahl statt langer Listen:** Bei normalem/gedrücktem Icon,
Hintergrund und MQTT-Rückmeldung öffnet sich ein gemeinsamer Picker. Paket
aufklappen, suchen, Icon wählen und **Übernehmen** (oder doppelklicken).
**Abbrechen**/Escape behalten die vorige Auswahl; danach oben **Speichern**.
Die Auswahl lädt nur 48×48-PNG-Miniaturen, bei Animationen das erste Bild,
mit höchstens 96 sichtbaren Kacheln je Paketseite. Der Pi erzeugt sie bei Bedarf
unter `icons/.cache/thumbnails/`; Pi und angemeldeter Browser verwenden den Cache.

Gleiche Icon-IDs/Inhalte erscheinen einmal je Paket; alternative Dateinamen
bleiben suchbar. Originale und gespeicherte IDs werden nicht gelöscht oder
umgeschrieben; echte Stilvarianten und schwarze/weiße Pakete bleiben getrennt.
**MDI-Favoriten hinzufügen · 40 Icons** importiert optional das gebündelte
SteelBlue-Paket mit 20 Ein-/Aus-Paaren. Keine automatische Installation oder
MQTT-Zuordnung; Normal/Gedrückt bzw. Rückmeldung selbst auswählen.

[![Grafische Iconauswahl mit Miniaturcache, lokale Demo](/images/usb-extender/picker-028.png)](/images/usb-extender/picker-028.png)

Pakete einzeln aufklappen oder nach Paketname, Dateiname und Unterordner suchen.
Hover/Fokus zeigt Namen und Vorschau. 48×48-Miniaturen in 52×52-Kacheln sparen Platz;
die Lizenz steht einmal im Paketkopf. Freier und gesamter Speicher stehen im Seitenkopf.

[![Iconpakete mit Vorschau, lokale Browser-Demo](/images/usb-extender/icons-022.png)](/images/usb-extender/icons-022.png)

Importiert werden Einzelbilder, Browser-Ordner, Ordner auf dem Pi sowie lokale
ZIP-, `.streamDeckIconPack`- und `.streamDeckPlugin`-Pakete. Bei Plugins werden nur
Bilder aus unterstützten Bildordnern übernommen, kein Programmcode. Unterstützte
JSON-Metadaten liefern den Paketnamen, sonst gilt der Ordner-/Archivname.
Originalnamen und Unterordner bleiben erhalten. Kein automatischer Marketplace-Download;
Nutzungsrechte beachten.

PNG/JPEG und statische SVGs sind unterstützt. GIF/WebP werden **normal und gedrückt**
animiert, bis 120 Bilder und höchstens 10 Bilder/s. SVG-Animationen werden nicht
abgespielt, Hintergründe bleiben statisch. Reale Hardware muss je Modell geprüft werden.

Originale: `/var/lib/ugso-usbhub/icons/IconPacks/`; Index: `icons/index.json`;
abgeleitete Vorschauen: `icons/.cache/`. Paketlöschen erstellt vorher eine Sicherung
und blockiert Pakete mit gespeicherten Zuordnungen.

**Seit 0.1.22:** Index einmal am Ende speichern, Vorschauen und Animationsdaten bei
Bedarf erzeugen. Browser-Ordner werden als ein ZIP hochgeladen, auch mit mehreren
Paketen und ihren Pfaden. Der Ladebalken nutzt echte Serverzählstände.
**Vor einem Update einen laufenden Import fertigstellen lassen.**

| Lokaler Windows-PC-Einzelvergleich | Vorher | 0.1.22 |
| --- | --- | --- |
| Itsyhome, 240 echte PNGs | 4,262 s | 0,395 s |
| 6.800 synthetische PNGs | 458,323 s | 10,464 s |

Indexschreibvorgänge: vorher 240 beziehungsweise 6.800, danach jeweils einer.
Das sind PC-Messwerte, keine Pi-/SD-Kartenmessung. Beim vorherigen Import mit
6.862 Icons erschien bei 2.898 wieder die Loginseite, ohne Fehlermeldung.
Nach Einspielen des Updates meldet der Nutzer, dass es wieder funktioniert.
Der vollständige Abschluss aller 6.862 Icons ist noch nicht bestätigt.

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

Für 0.1.28 bestehen 168 erfolgreiche lokale Python-Tests sowie JavaScript-/DOM-
und Chrome-Prüfungen für Seiten, Speichern, mobile Darstellung, Iconauswahl,
Pakete und Animationen. Dazu kommt der erfolgreiche reale 15-Minuten-Test oben.
Neue/Löschen-Seite, Home und Gehe zu sind lokal geprüft; deren vollständiger
Hardwaretest sowie Tests physischer Stream Decks bleiben weitere Prüfpunkte.

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
