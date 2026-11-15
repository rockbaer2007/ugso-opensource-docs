# TypeScript

## Erstes Beispiel

Im Bild ist absichtlich ein Typfehler eingebaut. Eine Variable vom Typ `number` erhält den Text `'42'`.

1. Wähle **Neues Projekt → TypeScript** und gib den Code aus dem Bild ein. Die zweite Zeile gibt den Wert mit `ha.log(String(zahl));` als Text aus.
2. Klicke auf **Testlauf starten**. Das Protokoll meldet, dass ein Text keiner Zahlvariablen zugewiesen werden kann. Über **Zeile 1** springst du zur betroffenen Stelle.
3. Entferne nur die Anführungszeichen um `42`. Starte erneut. Im Protokoll erscheint `42` als Meldung.

[![TypeScript mit markiertem Typfehler und Link zu Zeile 1](/images/logic-studio/user-guide/typescript-de.png)](/images/logic-studio/user-guide/typescript-de.png)

## Funktionen

### Typen

Ein Typ beschreibt, welche Werte zulässig sind. `number` erwartet eine Zahl und `string` einen Text.

### Typprüfung

Sie prüft Deklarationen, Zuweisungen und Aufrufe. Korrigiere die markierte Stelle und prüfe erneut.

### Autovervollständigung und Signaturen

Nutze die Vorschläge der Skript-API. Die Signatur zeigt, welche Argumente erwartet werden.

### Testlauf und Runtime-Fehler

Der Testlauf arbeitet mit simulierten Werten. Fehler beim Ausführen verweisen auf die ursprüngliche TypeScript-Zeile.

### Globale Funktionen und Autostart

Wähle exportierte Funktionen aus globalen Skripten. Autostart wird pro Projekt eingestellt.

### Play und Protokoll

Speichere zuerst. Play startet die Runtime. Das Protokoll zeigt Ausgaben und Fehlermeldungen.

## Wenn etwas nicht klappt

Wenn du eine Zahl aus einem HA-Zustand erwartest, prüfe und konvertiere den Zustand vor der Rechnung.
