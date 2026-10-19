# Tablet-Test: sicher von klein nach groß

Stand: 19.10.2026, App 0.1.327 und HA 2026.10.2. **Vorbereitet, noch kein
bestandener Tablet-Test.** Die PC-Vorprüfung ersetzt keine Messung am Tablet.
Tests ausschließlich auf `192.168.178.177` und `192.168.178.68`.

## Zuerst der Browsercheck

Für ein älteres Galaxy Tab A, das schon bei normalen Dashboards kaum reagiert,
keinen Lasttest sofort starten. Die vorhandene Stream-Deck-Einrichtung bleibt
unverändert. In einem separaten Browser-Tab zunächst öffnen:

- [.177: leichter Browsercheck](http://192.168.178.177/local/atlas-tablet-20261019/index.html)
- [.68: leichter Browsercheck](http://192.168.178.68/local/atlas-tablet-20261019/index.html)

Diese eigenen temporären Seiten laden kein HA-Frontend und keine großen Karten.
Sie zeigen verfügbare Browserfunktionen und den Browsernamen, senden keine
Telemetrie und verändern keine Einstellungen. „Vorhanden“ ist kein Nachweis
vollständiger HA-Kompatibilität oder ausreichender Leistung. Alter des Geräts,
Android-Version und Browser-Version sind unterschiedliche Angaben; die genaue
Android-/Browser-Version ist bei diesem Gerät noch nicht bestätigt.

Fehlt eine Funktion oder stockt bereits diese Seite: hier stoppen und die
angezeigte Meldung nennen. Keine Browserdaten löschen, keine Sicherheitsprüfung
abschalten und die laufende Stream-Deck-Konfiguration nicht ersetzen.

## Kleiner Einstieg

Nur wenn die Prüfseite flüssig läuft, dort „Kleinen HA-Einstieg öffnen“ wählen.
Die eigenen Dashboards sind nur für Administratoren freigegeben und nicht in
der Seitenleiste. Bei Bedarf selbst mit dem bestehenden HA-Konto anmelden;
Zugangsdaten oder Tokens nicht weitergeben.

1. **Start:** „Testzustand 18“ wählen; „HA verbunden“ kontrollieren.
2. **12 Karten:** hochkant und quer prüfen. Bis unten und zurück scrollen.
   Auf überlappende Texte, abgeschnittene Knöpfe und verzögerte Reaktion achten.
3. „Testzustand 28“, „Hell“ und „Dunkel“ wählen. Nach dem Übergang sollen die
   Anzeigen reagieren; danach „Theme zurück“ wählen. Die vorab erfasste Auswahl
   auf beiden Testhosts ist das Standardtheme mit automatischem Modus.
4. „Wiederverbindung testen“ einmal wählen, nicht neu laden. Danach soll
   „HA verbunden“, eine erhöhte Wiederverbindungszahl und „alter Socket
   geschlossen“ erscheinen. Erneut „Testzustand 18“ ausprobieren.

Bei stockender Bedienung stoppen. Für die Stream-Deck-Nutzung ist die kleine
Stufe aussagekräftiger als ein erzwungener Großprojekt-Test auf diesem Gerät.

## Optionale große Stufen

Erst nach flüssiger kleiner Stufe auf **360 Karten**, danach auf **720 Karten**
wechseln. Die gleiche Folge aus Drehen, Scrollen, 18/28, Hell/Dunkel und einer
Wiederverbindung wiederholen. Mushroom wechselt „Kühl“/„Warm“, Schneeflocke/Feuer
und Blau/Rot. Alle Karten beziehen sich nur auf eine eigene synthetische
Testentität; reale Geräte werden nicht geschaltet. Diese Vorbereitung verwendet
**Card-Mod 4.2.1 allein**, kein paralleles UIX. Eine neue Tablet-UIX-Prüfung ist
damit nicht abgedeckt.

## Rückmeldung und Abschluss

Je Host und erreichter Stufe melden: Hochkant/Querformat, Scrollen, Theme,
Wiederverbindung und ob die Bedienung flüssig, merklich verzögert oder blockiert
war. Nicht in nicht getestete Stufen hochrechnen. Hilfreich sind Browser und
Android-Version. Ein Hänger eines alten Browsers ist noch keine Diagnose seiner
Ursache und kein Nachweis eines ATLAS-Fehlers.

Frische Vollbackups und Bestandsabzüge liegen vor; vorhandene Editoren werden
nicht verändert. Eigene Testansichten bleiben bis zur Tablet-Rückmeldung stehen.
Danach eigene Testzustände/Ressourcen/Dashboards entfernen und WWW-Dateien in
den File-Studio-Papierkorb verschieben. Auf jedem Testhost die drei neuesten
erfolgreich abgeschlossenen Vollbackups behalten; PC-Sicherungen bleiben erhalten.
