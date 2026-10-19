# Tablet-Dauertest mit UIX: 720 Karten

Stand: 19.10.2026. **Nutzerbestätigung: je 60 Minuten auf .177 und .68 bestanden,
einschließlich Theme-Wechsel und Wiederverbindung.**
App 0.1.327, HA 2026.10.2, UIX 8.4.0; Card-Mod wird nicht geladen.
Gerät laut Nutzer: Samsung Galaxy Tab A6, Android 11 / LineageOS,
Chrome Mobile 155.

Frische vollständige HA-Sicherungen und Bestandsabzüge sind vorhanden. Eigene
Dashboards sind ohne Admin-only in der Seitenleiste sichtbar. Bestehende
Editoren, Projekte, Plugins und Einstellungen bleiben erhalten.

Dies ist eine funktionale Nutzerrückmeldung. Es liegen keine separat erhobenen
Tablet-JSON-Protokolle, FPS-/Speicherwerte oder detaillierten Dreh-/Scrollresultate vor.
PC-Vorprüfung und lokale Simulation bleiben davon getrennt.

## Historischer Prüfablauf

Je Host einen eigenen vollständigen 60-Minuten-Lauf durchführen, nacheinander:

Die eigenen Ansichten unter `/atlas-tablet-uix-soak-20261019/720` sind nach
dem Abschluss entfernt. Sie sind keine aktiven Testlinks mehr. Für eine spätere
Wiederholung zuerst neue Sicherungen und eigene Testansichten vorbereiten.

1. Tablet ans Ladegerät anschließen, Bildschirm wach halten, andere Apps wie
   beim bisherigen Test schließen. Nur die jeweilige Testseite im Vordergrund
   lassen. Mit dem vorhandenen HA-Konto anmelden; keine Zugangsdaten weitergeben.
2. Nach dem Aufbau „HA verbunden“ prüfen und **60 Minuten starten** einmal
   drücken. Der Zähler muss laufen. Währenddessen nicht neu laden oder die
   Dashboard-Ansicht verlassen.
3. Alle zehn Minuten abwechselnd hochkant/quer drehen, bis unten und zurück
   scrollen. Auf Ruckeln, Überlappungen, abgeschnittene Texte und Fehlerkarten
   achten. Mushroom wechselt Text/Symbol/Farbe mit dem synthetischen Zustand.
4. Der Helfer wechselt etwa alle zehn Sekunden 18/28, bei Minute 10/20/30/40/50
   Hell/Dunkel und bei 15/30/45 automatisch die Verbindung. Kurz „getrennt“ ist
   dabei erwartet; anschließend muss „HA verbunden“ zurückkommen. Nicht neu laden.
5. Bei **60 Minuten beendet** Endstand notieren. Mit **Ergebnis markieren**
   lässt sich das lokale JSON-Protokoll auswählen und über die normale
   Kopierfunktion kopieren. Falls das auf dem Tablet unpraktisch ist, reichen
   zunächst Host, Endzeit, angezeigte Wiederverbindungen und beobachtete Fehler.
6. Danach denselben Ablauf auf dem zweiten Host durchführen. Bei Hängern oder
   dauerhaft getrennter Verbindung „Stoppen / Theme zurück“ wählen und melden,
   wie lange der Lauf zuvor funktionierte.

Es werden nur eigene Testzustände geändert, keine realen Geräte geschaltet.
Laufzeit, Timerlücken und HA-Anfragezeiten sind keine FPS- oder
Darstellungszeitmessung. Schlafmodus/Hintergrundpausen als Unterbrechung melden.
Die automatische Theme-Wiederherstellung am Ende beziehungsweise beim Stoppen
erhält die ursprüngliche Auswahl. Ein Neuladen startet den Lauf nicht automatisch neu.

## Abschluss

Eigene Dashboards, Ressourcen, synthetische Zustände sowie temporäres UIX sind
entfernt; WWW-Dateien liegen im wiederherstellbaren File-Studio-Papierkorb. Alle
sieben Projekte, sechs Plugins je Host, 551 erfasste Bestandsdateien auf .177 und
neun auf .68 sowie ursprüngliche Einstellungen und alte Papierkorbeinträge sind
unverändert. Auf jedem Host bleiben drei Vollbackups. PC-Sicherungen und
installierte Updates bleiben erhalten. Card-Mod und UIX niemals parallel laden.
