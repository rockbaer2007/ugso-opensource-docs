---
title: ioBroker Blockly
description: Einführung in Blockly des ioBroker-JavaScript-Adapters mit einem offiziellen Einstiegsbeispiel.
---

# ioBroker Blockly

Blockly ist der grafische Skripteditor des **ioBroker-JavaScript-Adapters**. Automationen werden aus Blöcken zusammengesetzt, ohne dass der JavaScript-Code vollständig von Hand geschrieben werden muss.

::: info Offizielle Dokumentation
Diese Seite gibt nur einen kurzen Einstieg. Die vollständige Beschreibung aller Blöcke und weitere Beispiele befinden sich in der offiziellen ioBroker-Dokumentation.
:::

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

![Offizielles ioBroker-Blockly-Beispiel 1](https://raw.githubusercontent.com/ioBroker/ioBroker.javascript/master/docs/de/img/getting_started_1_de.png)

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
