---
title: Zeichnen mit der SVG-Verbindungslinie
---

# Zeichnen: SVG-Verbindungslinie

Das „Zeichnen“-Widget steht in der Palette als **HA Grafik – Spezial → SVG-Verbindungslinie**. Damit kannst du zum Beispiel zwei Solarpanels optisch mit einem Wechselrichter verbinden oder mehrere Ströme an einem Sammelpunkt zusammenführen. Die Linie ist ein grafisches Widget; sie überträgt selbst keine Home-Assistant-Werte.

## Eine Verbindung zeichnen

1. Füge die **SVG-Verbindungslinie** ein und wähle sie aus. Ihre beiden Endpunkte sind als ziehbare Kreise sichtbar. Ziehe einen freien Endpunkt auf einen Andockpunkt eines anderen Widgets. Alternativ kannst du unter **Start** und **Ziel** ein Widget samt Andockpunkt auswählen oder freie X-/Y-Koordinaten eingeben.
2. Aktiviere am Ziel-Widget die Eigenschaftengruppe **Andockpunkte**. Bei neuen Widgets sind alle zwölf Positionen zunächst aus. **Alle Punkte** schaltet sie gemeinsam ein oder aus und zeigt bei einer Teilauswahl einen gemischten Zustand. Die Punkte lassen sich auch einzeln aktivieren: links/rechts jeweils oben, Mitte, unten; oben/unten jeweils bei 1/4, Mitte und 3/4 der Breite. Der Haken in der Gruppenüberschrift aktiviert oder deaktiviert den ganzen Bereich. Mehrfachbelegung, maximale Verbindungen, Spurabstand und dauerhafte Anzeige sind einstellbar.
3. Wähle die **Pfadart**: gerade, automatisch rechtwinklig, Kurve oder manueller Zickzack-/Mehrpunktpfad. Ein Klick auf die Linie öffnet mittig den Dialog **Zwischenpunkt** oder **Sammelpunkt**; „Zwischenpunkt“ ist vorausgewählt. Nach **OK** entsteht ein verschiebbarer Zwischenpunkt und der Pfad wechselt in den manuellen Mehrpunktmodus. Die Punkte lassen sich zusätzlich im Eigenschaften-Editor benennen und per X/Y setzen.

Ein aktivierter **Sammelpunkt** kann von einer anderen Linie als Start oder Ziel gewählt werden. Du kannst auch einen freien Linienendpunkt auf den sichtbaren Sammelpunkt ziehen: Er rastet dort ein und speichert die Kopplung. Eine Kreuzung oder räumliche Nähe allein koppelt Linien niemals. Deaktivierst du den Sammelpunkt, rastet dort keine neue Linie ein. Mehrere Linien können zu einem aktivierten Sammelpunkt führen. Linien, die den Punkt bisher nur optisch berühren, musst du einmal neu andocken.

## Aussehen und Fluss

- **Linie:** Grundfarbe, zweite Animationsfarbe, Dicke, Deckkraft, durchgezogen/gestrichelt/gepunktet, Strich- und Lückenlänge, Linienenden sowie Eckenradius.
- **Pfeilspitzen:** Anfang und Ende getrennt als keine, gefüllter oder offener Pfeil oder Kreis; Größe und Farbe sind einstellbar.
- **Animation:** Zweifarbenfluss, laufende Striche, Puls oder Lichtpunkt. Unter **Richtungsquelle** ist genau eine Option aktiv: **Manuell** mit Richtung und Dauer, **Zahlen-Entität** oder **Bool-Entität**. Bei einer Zahlen-Entität bedeutet positiv Anfang → Ende, negativ Ende → Anfang und null Stillstand. Der Betrag geteilt durch **Teiler** (Standard 1) ergibt die Zyklen pro Sekunde, begrenzt auf 0,05 bis 20. Beispiel: 1000 W ÷ 100 = 10 Zyklen/s. Die Bool-Entität wählt mit `on`/`true`/`1` vorwärts und mit `off`/`false`/`0` rückwärts; die Zuordnung kann umgekehrt werden. Nicht verfügbare oder ungültige Zustände halten die Animation an. Pfeilspitzen folgen der aktiven Richtung. Die Runtime liest die ausgewählte HA-Entität regelmäßig neu. Mit **Animationstakt der Hauptlinie übernehmen** folgt eine Nebenlinie dem Takt ihrer Hauptlinie und behält bei laufender Animation ihre eigenen Farben. Ist sie an deren Sammelpunkt gekoppelt und die Hauptlinie nicht animiert, stoppt auch die Nebenlinie und zeigt die Grundfarbe der Hauptlinie, einschließlich der Pfeilspitzen. Ihre eigenen Farb- und Animationseinstellungen bleiben gespeichert und gelten nach dem Lösen der Kopplung wieder. Die Synchronisierung bietet gleichen Takt oder Ankunft am Sammelpunkt. Bei manueller Richtung zu einem Sammelpunkt richtet sich die Animation automatisch auf diesen Punkt aus.
- **Kreuzung und Stapelung:** Überlagerung, optische Lücke oder Brücke/Bogen sowie z-index-Modus „automatisch“, „darüber“, „darunter“ oder manuell. Ein höherer z-index liegt optisch vor einem niedrigeren; er erzeugt keine Verbindung.

## Bearbeiten

| Aktion | Bedienung |
| --- | --- |
| Freien Endpunkt bewegen | Kreis ziehen oder fokussierten Kreis mit den Pfeiltasten bewegen; `Umschalt` erhöht die Schrittweite von 1 auf 10 Pixel. |
| Angedockten Endpunkt lösen | `Strg` gedrückt halten und den Kreis ziehen; `Strg` plus Pfeiltaste funktioniert ebenfalls. |
| Zwischenpunkt verschieben | Linie auswählen und den Punkt ziehen. |
| Ganze Linie verschieben | Auf die Linie drücken und ziehen. Vorherige Start-/Ziel-Andockungen werden dabei gelöst. |
| Linienpunkt hinzufügen | Linie ohne Ziehen anklicken, Punkttyp wählen und mit **OK** bestätigen. |

Das Widget ist experimentell. Die Darstellung von Kreuzungen und synchronisierten Animationen kann je nach Pfadverlauf und Browser noch verfeinert werden.
