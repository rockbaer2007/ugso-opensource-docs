---
title: ioBroker Blockly
description: Einführung in Blockly des ioBroker-JavaScript-Adapters mit einem offiziellen Einstiegsbeispiel.
---

# ioBroker Blockly

Blockly ist der grafische Skripteditor des **ioBroker-JavaScript-Adapters**. Automationen werden aus Blöcken zusammengesetzt, ohne dass der JavaScript-Code vollständig von Hand geschrieben werden muss.

::: info Offizielle Dokumentation
Diese Seite gibt nur einen kurzen Einstieg. Die vollständige Beschreibung aller Blöcke und weitere Beispiele befinden sich in der offiziellen ioBroker-Dokumentation.
:::

## Home Assistant per MQTT mit ioBroker und VIS 2 verbinden {#mqtt-vis2-helper}

Dieses eigene UGSo-Beispiel ergänzt den Blockly-Einstieg: Der **MQTT-Client für Home Assistant** überträgt ausgewählte Entitäten an einen externen MQTT-Broker. Der hier gezeigte **ioBroker-JavaScript-Helfer 0.1.33** bereitet diese Werte für VIS 2 auf und bietet eine wählbare flache Struktur mit kurzen Namen. Für die neue Option den vollständigen Helfer ersetzen und eigene Einstellungen übernehmen.

::: warning JavaScript, kein Blockly-Import
Das vollständige Skript wird im **ioBroker-JavaScript-Adapter** als JavaScript eingefügt. Es gehört weder in Home Assistant noch in den Blockly-XML-Import. Die vorhandenen Blockly-Beispiele weiter unten bleiben davon unabhängig.
:::

### Wozu ist der Helfer gedacht? {#mqtt-helper-purpose}

MQTT verwendet für Rückmeldung und Bedienung getrennte Topics. Der Helfer verbindet beide über **einen virtuellen Datenpunkt pro Wert** unter `0_userdata.0.ugso_mqtt`. In VIS 2 genügt dann dieser eine Datenpunkt für Anzeige und Bedienung.

```text
HA -> MQTT state -> 0_userdata.0.ugso_mqtt -> VIS 2
VIS 2 -> 0_userdata.0.ugso_mqtt -> MQTT set -> HA
```

- HA-Rückmeldungen aktualisieren den virtuellen Datenpunkt mit `ack: true`.
- Eine Bedienung in VIS 2 schreibt mit `ack: false`; nur ein freigegebener Rückkanal wird verwendet. Ein Broker-Auftrag gilt erst nach einer neuen tatsächlichen HA-Rückmeldung als bestätigt.
- Unterstützte Light-Werte werden passend normalisiert, etwa Helligkeit auf 0–100 %. Messwerte und Datum bleiben lesend.
- Geeignete HA-Metadaten liefern Datentyp, Einheit und eindeutige Rollen. Vorhandene Werte, manuelle Rollen und fremde Objekte bleiben geschützt.
- Das Skript verarbeitet betroffene MQTT-Änderungen gezielt. Es führt nicht bei jeder beliebigen Messwertänderung einen vollständigen Neuaufbau aus.

### Voraussetzungen und Einrichtung {#mqtt-helper-setup}

1. MQTT-Client in HA und ioBroker-MQTT-Adapter einrichten. Die App überträgt an den externen Broker; für den hier beschriebenen Rückkanal wird der ioBroker-MQTT-Adapter im Modus **Server/Broker** verwendet.
2. Entitäten auswählen oder das konfigurierte HA-Label setzen. **Zusätzliche Gerätemesswerte benötigen ausdrücklich den Haken „Zugehörige Mess- und Batteriewerte desselben Geräts automatisch einbeziehen“ und anschließend „Speichern und verbinden“.** Nur vorhandene, unterstützte Sensoren desselben HA-Geräts werden ergänzt.
3. Im ioBroker-JavaScript-Adapter ein neues JavaScript-Skript anlegen und den vollständigen Code unten einfügen. Der Helfer ist für Adapter **10.4.10** geprüft.
4. In den Adaptereinstellungen **setObject erlauben** und **Do not subscribe to all states on start** deaktivieren. Das Skript benötigt synchrone Objekt-/Zustandscaches. Für das reine Ansehen des Codes sind keine Freigaben erforderlich.
5. Pfade im Einstellungsblock prüfen und zunächst `mode: 'preview'` lassen. Die Vorschau legt nur fehlende eigene Basisordner/Sicherungsdatenpunkte an und protokolliert geplante Zuordnungen; sie erzeugt keine bedienbaren virtuellen Werte und sendet keine Schaltbefehle.
6. Nach Prüfung `mode: 'apply'` einstellen und das Skript neu starten. Nun werden die virtuellen Datenpunkte angelegt und synchronisiert.
7. In VIS 2 den passenden virtuellen Datenpunkt auswählen, **nicht den rohen MQTT-`set`-Datenpunkt**.

### Einstellungsblock und Sicherung {#mqtt-helper-settings}

| Einstellung | Bedeutung |
| --- | --- |
| `mqttRoot` | Eingehender MQTT-Baum, standardmäßig `mqtt.0.ha_external`. |
| `mode` | `preview`: prüfen; `apply`: anwenden; `restore`: eigene gesicherte Änderungen geschützt zurücknehmen. |
| `outputMode` | `virtual` für VIS-2-Datenpunkte; `roles` für die alternative Rollen-/Alias-Zuordnung. |
| `virtualLayout` | `nested`: bisherige IDs (Standard); `flat`: kurze Datenpunkte direkt im Geräteordner. |
| `virtualRoot` | Zielbaum der virtuellen Werte. |
| `virtualBackupId`, `backupId` | Eigene Sicherungsjournale; vorhandene Sicherungen werden erhalten. |
| `aliasRoot` | Ziel für lesende Aliase im Rollenmodus. |
| `excludeIds` | Exakte Quell-IDs, die nicht bearbeitet werden sollen. |

Bei bereits vorhandenem Skript die eigenen Einstellungen übernehmen. `restore` ist keine Wiederherstellung der gesamten ioBroker-Installation: Später manuell veränderte Objekte bleiben geschützt, virtuelle Werte/Referenzen werden erhalten und ihre Steuerung wird deaktiviert. Für die Details gilt die [vollständige Helfer-Anleitung](/projects/mqtt-client/iobroker-roles), einschließlich Rollentabelle, Sicherung und Grenzen.

### Wählbare flache Struktur mit kurzen Namen {#mqtt-helper-flat-layout}

Im **vollständigen Helfer 0.1.33** kann im Einstellungsblock `virtualLayout: 'flat'` gewählt werden. Standard bleibt `virtualLayout: 'nested'`; fehlt die neue Einstellung in übernommenen Optionen, gilt ebenfalls die bisherige Struktur. Prüfen Sie zuerst die Vorschau und wechseln Sie danach zu `mode: 'apply'`.

```text
0_userdata.0.ugso_mqtt.pc_tv_wohnzimmer
  schalter
  energie
  leistung
  spannung
  stromstaerke
```

Die technischen IDs verwenden diese kurzen deutschen Namen in allen Sprachen. Energie, Leistung, Spannung und Stromstärke werden aus der Geräteklasse erkannt; sonst wird ein geeigneter Teil der Entitäts-ID verwendet. Die Anzeigenamen lauten entsprechend etwa **Energie** oder **Stromstärke**. Für Lampen sind **licht**, **helligkeit**, **farbe**, **effekt** und **farbtemperatur** vorgesehen.

Mehrere passende Werte erhalten **leistung**, **leistung_2**, **leistung_3** usw. Einmal vergebene Namen werden im vorhandenen Journal gespeichert und bleiben bei späteren Auswahländerungen erhalten. Bereits belegte Ordner, fremde Datenpunkte oder Sicherungs-IDs werden nicht überschrieben; stattdessen wird ein freier Zusatz vergeben.

**Vorhandene Helfer-Datenpunkte werden weder gelöscht noch verschoben:** Alte und neue IDs bleiben synchronisiert und ihre freigegebenen Rückkanäle erhalten. Bestehende VIS-2-Verknüpfungen müssen deshalb nicht geändert werden. Für neue Widgets können die kurzen IDs gewählt werden; alte Ordner bleiben zunächst sichtbar. Zurückschalten erfolgt mit `virtualLayout: 'nested'` im neuen Helfer. Die alte Datei 0.1.27 kann Journale mit flachen Einträgen nicht lesen.

MQTT-Objekte, Topic-Pfade, Werte und manuelle Rollen bleiben unverändert. Kann beim Zurückschalten ein benötigter Ordner wegen eines bestehenden Datenpunkts nicht angelegt werden, wird dieser neue Zielpfad ausgelassen und protokolliert; vorhandene Werte werden nicht ersetzt.


### Vollständiges Skript mit Kopierbutton und Download {#mqtt-helper-code}

<a href="/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.33.js" download>JavaScript-Helfer 0.1.33 herunterladen (.js)</a>

Der Kopierbutton rechts oben im Codefeld übernimmt das **gesamte Skript**. Codefeld und Download verwenden dieselbe unveränderte Datei; sie enthält keine persönlichen Zugangsdaten. Die Pfade und den Modus anschließend für die eigene Installation prüfen.

<div class="mqtt-helper-code">

<<< @/public/downloads/mqtt-client/ugso-mqtt-role-mapper-0.1.33.js

</div>

### Wenn Werte oder Bestätigungen fehlen {#mqtt-helper-troubleshooting}

- **Nur „Preview VIS 2“ im Log:** Erst nach Prüfung auf `mode: 'apply'` wechseln.
- **Fehler „setObject is not allowed“:** Die oben beschriebene Adapterfreigabe fehlt.
- **Energie, Spannung, Strom oder Leistung fehlen:** Messwerte-Haken aktivieren, speichern und in der HA-App **„Zugehörige Messwerte prüfen“** öffnen. Ähnliche Namen ersetzen keine HA-Gerätezuordnung.
- **Schalten möglich, Bestätigung fehlt:** Zuerst den rohen MQTT-Status prüfen. Bleibt er alt, fehlt die HA-Rückmeldung bereits vor dem Helfer. Der Helfer bestätigt nicht künstlich und wiederholt Befehle nicht automatisch.
- **Roher MQTT-`set`-Wert ändert sich nicht:** Der Helfer veröffentlicht Befehle über die Broker-Schnittstelle ohne Retain; der gespeicherte rohe Wert muss dabei nicht wechseln.

[MQTT-Client-Doku und App-Update](/projects/mqtt-client/) · [Helfer-Anleitung und vollständige Rollenzuordnung](/projects/mqtt-client/iobroker-roles)

<style scoped>
.mqtt-helper-code :deep(pre) { max-height: 36rem; overflow: auto; }
</style>


## Offizielle Quellen

- [ioBroker.javascript – offizielles Repository](https://github.com/ioBroker/ioBroker.javascript)
- [Deutsche Dokumentation des JavaScript-Adapters](https://github.com/ioBroker/ioBroker.javascript/tree/master/docs/de)
- [Vollständige Blockly-Dokumentation](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md)

## Beispiel 1: Datenpunkt abhängig von einem anderen Datenpunkt schalten

Das offizielle Einstiegsbeispiel zeigt eine typische Bewegungserkennung:

- Ein Bewegungs-Datenpunkt dient als Auslöser.
- Bei einer Zustandsänderung wird ein Licht-Datenpunkt gesteuert.
- Der aktuelle Wert des Bewegungsmelders wird an den Licht-Datenpunkt weitergegeben.
- Bewegung schaltet das Licht ein.
- Keine Bewegung schaltet das Licht wieder aus.

[![Offizielles ioBroker-Blockly-Beispiel 1](https://raw.githubusercontent.com/ioBroker/ioBroker.javascript/master/docs/de/img/getting_started_1_de.png)](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

<small>
Bildquelle und Rechtehinweis: Das Bild stammt aus dem offiziellen
<a href="https://github.com/ioBroker/ioBroker.javascript" target="_blank" rel="noopener">ioBroker.javascript-Repository</a>.
Die Rechte und Lizenzbedingungen richten sich nach dem dort veröffentlichten Projekt und dessen Lizenz.
</small>

## Benötigte Blockly-Blöcke

### 1. Trigger

Aus dem Bereich **Trigger** wird der Block **Falls Objekt** verwendet.

Dort wird der Datenpunkt des Bewegungsmelders ausgewählt.

### 2. Datenpunkt steuern

Aus dem Bereich **System** wird der Block **Steuere** eingefügt.

Als Ziel wird der Datenpunkt des Lichts ausgewählt.

### 3. Wert übernehmen

In den Steuere-Block wird **Wert von Objekt-ID** eingesetzt.

Dort wird erneut der Bewegungs-Datenpunkt ausgewählt. Dadurch übernimmt das Licht den aktuellen Wahr/Falsch-Zustand des Bewegungsmelders.

## Vereinfachter Ablauf

```text
Falls sich der Bewegungsmelder ändert
    setze den Zustand des Lichts
    auf den aktuellen Wert des Bewegungsmelders
```

## Blockly importieren

Den vollständigen importierbaren XML-Code stellt die offizielle Dokumentation direkt unter **Beispiel 1** bereit:

[Beispiel 1 mit Blockly-XML öffnen](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

Dort kann der XML-Code kopiert und im Blockly-Editor über die Importfunktion eingefügt werden.

## Weitere offizielle Beispiele

Die offizielle Dokumentation enthält zusätzlich:

- **Beispiel 2:** Licht bei Bewegung einschalten und nach zehn Minuten ohne weitere Bewegung wieder ausschalten.
- **Beispiel 3:** E-Mail senden, wenn die Außentemperatur einen Grenzwert überschreitet.

[Alle offiziellen Blockly-Beispiele ansehen](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#getting-started)

## Eigene Blockly-Beiträge im Blog

Für eigene Beispiele empfiehlt sich folgender Aufbau:

1. Aufgabe beschreiben
2. benötigte Objekt-IDs nennen
3. Screenshot des Blockly-Aufbaus einfügen
4. exportierten Blockly-XML-Code bereitstellen
5. Anpassungen und Voraussetzungen erklären

Screenshots werden im Dokumentationsprojekt hier abgelegt:

```text
docs/public/images/blog/
```

Einbindung im Beitrag:

```md
![ioBroker Blockly](/images/blog/mein-blockly.png)
```

::: warning
Objekt-IDs aus Beispielen müssen immer an das eigene ioBroker-System angepasst werden.
:::
