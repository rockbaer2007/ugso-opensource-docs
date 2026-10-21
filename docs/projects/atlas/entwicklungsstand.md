# Entwicklungsstand

## Getestete Hardwarevarianten

| Variante | Testumgebung |
| --- | --- |
| amd64 | Home Assistant in einer virtuellen Maschine unter Proxmox |
| ARM64 | Home Assistant auf einem echten Raspberry Pi 5 mit 8 GB RAM |

Diese Angaben beschreiben die getesteten Installationen; der Umfang und die
noch offenen Prüfungen sind im folgenden Entwicklungsstand dokumentiert.

## Aktueller Stand

**Stand: 21.10.2026 · HA-App 0.1.331 · HACS-Integration 0.1.306.**
App und Integration haben unabhängige Versionsnummern.

**App 0.1.331 sichert Dateiimporte als eigene Tab-Entwürfe.** Bestätigte JSON-
Gesamtkonfigurations-Importe benötigen dafür kein vorher geöffnetes gemeinsames
Projekt mehr. Ein erneuter Import erzeugt eine neue Quelle und erhält den
Vorgänger. Nach Neuladen wird die eigene Quelle vorausgewählt; Prüfung und
gesicherte Übernahme bleiben ausdrücklich. Die globale Arbeitsfläche ist davon
getrennt und kann den letzten Import zeigen. Einstellungsübernahme und die
getrennten Hinweise für lokale und Sitzungsfehler bleiben erhalten. Der Befund
aus dem frischen Profil unter 0.1.330 ist damit korrigiert; damalige Quelldateien
und 46 alte Quellen waren erhalten. Details: [Card Editor](card-editor.md).

Das Update auf .68 (HA 2026.10.2) und der gezielte native Import-/Neulade-Durchlauf
bestehen in beiden Reihenfolgen, mit erneutem Import, Abbrechen/ungültiger Datei
und blockierten lokalen/Sitzungs-Schreibzugriffen samt sicheren Folgeversuchen.
Vollständige Exportvergleiche und alle 48 alten Quellen bestehen, Ausgangsstände
und Daten sind erhalten, Testdateien bereinigt und drei Vollbackups behalten.
.177 unverändert. Die Übernahme des vorausgewählten Entwurfs bleibt ausdrücklich.

**Kombinierter Zwei-Tab-Test bestanden:** Auf .68 bleiben bei blockierten
Sitzungsmethoden zwei unterschiedliche Entwürfe während eines echten HA-Neustarts
editier- und exportierbar. Automatische Wiederverbindung, ausdrückliche getrennte
Wiederherstellung nach Neuladen und bestätigte Folgesicherung bestehen mit
vollständigem Exportvergleich. Alle 40 vorherigen Quellen und Bestandsdaten sind
erhalten, beide Originaleditoren wiederhergestellt, Testobjekte bereinigt und drei
Vollbackups behalten. .177 unverändert. App 0.1.330 bleibt unverändert; Grenzen
und Bedienhinweise stehen im [Card Editor](card-editor.md).

**App 0.1.330 behebt den fehlenden Hinweis bei Sitzungsfehlern.** Nach erfolgreichem
lokalem Schreiben werden Schreibmarkierung und Tab-Zeiger bestätigt. Schlägt dies
fehl, zeigt der Editor einen eigenen DE/EN/FR-Hinweis: Entwurf lokal gespeichert,
Tab-Wiederherstellung nicht zuverlässig gesichert, vor Neuladen/Schließen exportieren
und später manuell auswählen. Sprachwechsel und Projektlisten-Aktualisierung
erhalten die Meldung; erst vollständig bestätigtes Speichern entfernt sie.
Ein blockierter Sitzungs-Getter verhindert lokale Sicherung nicht mehr.
Lokale Datensatzfehler bleiben getrennt. Der Befund aus der 0.1.329-Prüfung mit
20 erhaltenen Quellen ist damit korrigiert. Details: [Card Editor](card-editor.md).

Die native Nachprüfung auf .68 (HA 2026.10.2) besteht mit voller Sitzungsablage,
blockierten Methoden/Getter, Export und manueller Wiederherstellung. Sprachwechsel
und Listenaktualisierung erhalten die Warnung; bestätigtes Folgespeichern entfernt
sie. Lokale Fehler bleiben getrennt. Alle 31 alten Entwurfsquellen sind bytegleich,
fünf Originaleditoren und Bestandsdaten wiederhergestellt. Testobjekte bereinigt,
drei Vollbackups erhalten, .177 unverändert. Kein erneuter Prozessabbruch oder
Betriebssystem-Datenträgerfülltest; die Grenzen stehen im Card-Editor-Abschnitt.

**App 0.1.329 bietet den neueren Entwurf nach unterbrochener Sicherung an.**
Eine vorab gespeicherte tabgebundene Schreibmarkierung erkennt den vollständigen
Datensatz, falls die Aktualisierung des Tab-Zeigers ausbleibt. Vorschau und
gesicherte Übernahme bleiben ausdrücklich; die Arbeitsfläche wird nicht automatisch
ersetzt. Fremde Tabs, Vorgänger und ältere Quellen bleiben erhalten. Fehlerhafte
Markierungen ändern die Auswahl nicht; ältere Versionen benötigen weiter manuelle
Quellenwahl. Verwendung und Grenzen: [Card Editor](card-editor.md).

Update und gezielte Unterbrechung nach Datensatzschreiben/vor Tab-Zeiger bestehen
auf .68 mit HA 2026.10.2: Angebot/Vorschau in DE/EN/FR, Abbrechen ohne Änderung,
exakte bestätigte Wiederherstellung und keine Verwechslung mit einem neueren
fremden Entwurf. Alle 13 vorhandenen Quellen und beide Originaleditoren sind
unverändert; Bestandsvergleich bestanden, eigene Testobjekte bereinigt und drei
Vollbackups erhalten. .177 unberührt. Dieser Lauf nutzt eine kontrollierte
Ausnahme an der Schreibgrenze, keinen neuen Browserprozessabbruch.

**Entwurfskollision mit App 0.1.328 behoben (21.10.2026, .68):** Zwei Tabs
sichern unabhängig und finden nach Neuladen jeweils ihren eigenen Entwurf.
Vollständige Exporte stimmen vor/nach Wiederherstellung überein, ebenso nach
lokalen Änderungen während eines echten App-Ausfalls. Ein geschlossener Entwurf
lässt sich im neuen Tab gezielt auswählen. Alte Quellen und der bisherige globale
Entwurf bleiben erhalten; veraltetes Serverspeichern bleibt gesperrt.
DE/EN/FR-Auswahl und Vorschau sind geprüft. Siehe [Card Editor](card-editor.md)
für Verwendung und Grenzen. Testprojekt bereinigt, Originaleditoren und erfasste
Daten erhalten, drei Vollbackups auf .68; .177 unverändert. Der anschließende
vollständige Chrome-Neustart mit Sitzungswiederherstellung besteht ebenfalls:
neuer Hauptprozess, getrennte wiederhergestellte Tab-Zeiger, vollständige
Entwurfsvergleiche und manuelle Quellenwahl. Auch der anschließende harte Abbruch
aller Chrome-Prozesse besteht: beide Entwürfe samt unterschiedlichen Kartentiteln
vollständig wiederhergestellt, vier ältere Entwurfsquellen unverändert. Originale
erhalten, Testprojekt entfernt, drei Vollbackups. Abbruch nach lokaler Sicherung;
kein Schreibabbruch-, Stromausfall- oder Datenträgertest. .177 bleibt unberührt.

Anschließend ist der Abbruch innerhalb der lokalen Sicherung nach Schreiben
des Datensatzes und vor Aktualisierung des Tab-Zeigers gezielt geprüft: der
vollständige neue Entwurf bleibt manuell auswählbar, der bestätigte Vorgänger
bleibt vorausgewählt. Tab B und acht ältere Quellen stimmen mit den Sicherungen
überein. Die eigene Testinstrumentierung lässt installierte App-Dateien unverändert.
Originaleditoren und Bestandsdaten erhalten, aktive Testobjekte bereinigt, drei
Vollbackups auf .68; .177 unverändert. Kein Abbruch innerhalb eines atomaren
nativen Speicheraufrufs, kein Stromausfall-/Datenträgertest. Anleitung und
Testgrenzen stehen im [Card Editor](card-editor.md).

Die [HA-Kompatibilitätsmatrix](frontend.md) enthält jetzt auch HA **2026.10.2**
mit Integration 0.1.306 und App 0.1.327 auf **.68**: Einbettung, Live-Verbindung,
lokales Speichern/Neuladen, bytegleiche JSON-/YAML-HACS-Rundläufe und automatische
Wiederverbindung nach HA-Neustart bestehen. Originaleditor und erfasste Daten
sind erhalten, Runtime-Adresse zurückgestellt und drei Vollbackups vorhanden.
.177 wurde nicht aufgerufen oder verändert. Alle drei CI-Versionen bestehen.

**App 0.1.327 begrenzt und entkoppelt die HACS-Prüfung.** Feste Grenzen vor
Dateilesen/CRC, Worker mit Abbrechen und 15-Sekunden-Prüfwächter sowie eine
ausdrückliche Übernahme erhalten den Editor bis zur Bestätigung. Dieselbe Datei
ist nach Abbruch erneut auswählbar. Alle 431 Pakettests und der Workspace-Build
bestehen. Details und Grenzwerte: [Card-Editor-Handbuch](card-editor.md).
Die native Prüfung auf .177/.68 mit HA 2026.10.2 besteht nach Vollbackups:
20 Grenzfälle, sechs Abbrüche, zwei Wiederholungen derselben Datei und zwei
ausdrückliche Übernahmen. Vollständige Originaleditoren und erfasste Dateien,
Projekte und Plugins sind erhalten; beide Hosts laufen mit 0.1.327.

**Großprojekt-Import unter wiederholter Last mit unveränderter App 0.1.327.**
Rund 25 Minuten auf .177/.68: je 60 Serienübernahmen von 36 Feldern mit 360/720
verschachtelten Karten, zusammen 238 Abbrüche und 116 gleiche Datei-Wiederholungen.
Vier tatsächliche HACS-Rundläufe sind bytegleich; je drei Neuladetests und die
Prüfung eines gültigen 24-MiB-Pakets bestehen. Originaleditoren und erfasste
Bestandsdaten bleiben erhalten. Browserweite Speicherwerte sind kein isolierter
ATLAS-Speichernachweis; die HA-Darstellung ist separat geprüft, siehe unten.

**HA-Darstellung großer Projekte bestanden.** Auf .177/.68 mit App 0.1.327 und
HA 2026.10.2: ursprüngliche und dynamische 360-/720-Karten-Projekte, Card-Mod
4.2.1 und UIX 8.4.0 strikt getrennt. UIX verarbeitet auch `card_mod`. Hell/Dunkel,
CSS-Vererbung, Mushroom-Jinja und acht automatische Wiederverbindungen bestehen:
62 Aufnahmen, 33.120 Vergleiche mit nativen Referenzen, keine Fehlerkarten.
Vorhandene Editoren und erfasste Daten bleiben erhalten; eigene Testobjekte
werden bereinigt. Details und Grenzen im [Card-Editor-Handbuch](card-editor.md).
Der Nutzer bestätigt 720 Karten auf beiden Hosts samt Theme-Wechsel und
Wiederverbindung: Galaxy Tab A6, Android 11 / LineageOS, Chrome Mobile 155.
Nach Stoppen anderer Apps läuft der Browser flüssig. Testobjekte bereinigt,
Bestandsdaten erhalten, je drei Vollbackups. Keine FPS-/Langzeitmessung;
Der frühere Card-Mod-Lauf prüft UIX noch nicht. Siehe [Tablet-Ergebnis](tablet-test.md).

**UIX-Tablet-Dauertest abgeschlossen:** Der Nutzer bestätigt je 60 Minuten mit
720 Karten auf .177/.68 samt Themes und Wiederverbindung. UIX 8.4.0 lief allein.
Testobjekte und temporäres UIX sind entfernt, Bestandsvergleich bestanden und
je drei Vollbackups erhalten. Keine unabhängige FPS-/Speicher- oder Leckmessung.
Siehe [Dauertest-Ergebnis](tablet-uix-dauertest.md).

**Historischer Größenbefund mit App 0.1.324.**
24 echte Importfälle auf .177/.68: 16 Annahmen mit 112/112 bis 30.008 Dateien
beziehungsweise 64 MiB Zusatzinhalt und acht korrekte Ablehnungen komprimierter
oder abgeschnittener Archive. Originaleditoren und geprüfte Bestandsdaten bleiben
erhalten. Neuladen direkt nach Dateiauswahl erhält beide Originale; eine
abbrechbare synchrone Prüfung und allgemeine UI-Reaktionsfähigkeit sind damit
nicht qualifiziert. Einzelheiten stehen im [Card-Editor-Handbuch](card-editor.md).

**App 0.1.324 korrigiert die mehrdeutige HACS-Übernahme.** Projekt-/Scriptanzahl,
sämtliche Scriptidentitäten und vollständige Vorprüfung sperren vor der tatsächlichen
Editorübernahme. 418 Pakettests und 40 neue Handler-/Identitätsregressionen bestehen.
Gültige Exporte und bestehende gespeicherte Daten bleiben erhalten.
Das native Update auf .177/.68 mit HA 2026.10.2 ist nach Vollbackups bestanden:
60 Fälle, 52 korrekte Ablehnungen, acht gültige Importe mit 112/112 und alle
14 früheren Fehlübernahmen gesperrt. Vollständige Originaleditoren und geprüfte
Bestandsdaten sind erhalten.

**Historischer Befund unter 0.1.323: mehrdeutige HACS-Pakete.** Auf .177/.68 mit HA 2026.10.2
werden 46 echte Importe geprüft: 26 korrekte Ablehnungen, sechs gültige Kontrollen,
aber 14 falsche Übernahmen. Mehrere Projekte oder Scripts können trotz blockiertem
Bericht übernommen werden; ein widersprüchlicher Editorplan-Scriptname besteht
sogar mit 112/112. Die Auswahl kann von der ZIP-Reihenfolge abhängen. Original-
editoren und geprüfte Bestandsdaten sind wiederhergestellt bzw. unverändert;
App 0.1.323 wurde damals nicht geändert. Ab 0.1.324 korrigiert, siehe [Card Editor](./card-editor).

App 0.1.322 prüft CRC32 aller gespeicherten ZIP-Einträge und die Header-/
Verzeichniskonsistenz vor der HACS-Übernahme. Beschädigte oder nicht unterstützte
Archive bleiben außerhalb des Editors. 376 Pakettests, darunter 52 neue
Integritätsfälle, und vier bytegleiche Originalarchiv-Rundläufe bestehen.
Das native Update auf .177/.68 mit HA 2026.10.2 besteht nach Vollbackups:
60 korrekte Ablehnungen erhalten die vollständigen Editorstände auch nach
Neuladen; vier gültige JSON/YAML-Kontrollen bestehen mit 112/112. Originaleditoren
und Bestandsdaten sind unverändert. App 0.1.323 korrigiert anschließend die
generischen Dateifehlt-Folgehinweise: ZIP-Fehler blockieren zuerst, abhängige
Datei-/Inhaltsprüfungen bleiben nicht geprüft. Tatsächlich fehlende Dateien in
verifizierten ZIPs bleiben Fehler. Alle 378 Pakettests bestehen; siehe
[Card Editor](./card-editor).

Die native 0.1.323-Qualifikation auf .177/.68 besteht nach frischen Vollbackups:
64 Paketfälle, darunter 26 unverifizierbare ZIPs ohne irreführende Dateifehler,
60 sichere Ablehnungen und vier gültige Importe mit 112/112. Vollständige
Originaleditoren und geprüfte Bestandsdaten sind erhalten.

Die native HACS-Negativprüfung auf .177/.68 ist mit 21 Paketen je Host nach
Vollbackups abgeschlossen: 38 korrekte Ablehnungen erhalten die vollständigen
Editorstände auch nach Neuladen; zwei gültige Kontrollen bestehen. Unter 0.1.321
bestand eine CRC-Lücke: Ein beschädigtes README im ZIP wird zweimal fälschlich mit
112/112 angenommen und ersetzt den lokalen Editorstand. Beide Originalstände
sind exakt wiederhergestellt, Bestandsdaten sind unverändert. Keine vollständige
Integritätsfreigabe für 0.1.321; ab 0.1.322 ist dieser Befund behoben.
Details im [Card Editor](./card-editor).

App 0.1.321 korrigiert die falschen HACS-Titelfehler bei leerem ersten
Entity-Namen, ohne die Namen zu verändern. Beide Prüfungen nutzen den Paketnamen.
324 lokale Pakettests bestehen; die acht gesicherten Original-/Kontrollarchive
erreichen unverändert 112/112 und bytegleiche Rückexporte. Ungültige Manifestnamen
bleiben gesperrt. Das native Update von 0.1.320 auf 0.1.321 ist auf .177/.68
mit HA 2026.10.2 nach Vollsicherungen bestanden: vier ursprüngliche JSON/YAML-
Fehler-ZIPs ohne Kontrollkarte erreichen je 112/112 und bytegleiche Rückexporte.
Originalnamen und Bedingungen bleiben nach Import und Neuladen exakt erhalten;
Bestandsdaten und ursprüngliche lokale Editorstände sind unverändert.
Details im [Card Editor](./card-editor).

App 0.1.320 erhält leere Entity-Namen und äußere Leerzeichen/Tabulatoren
unverändert. 296 lokale Pakettests bestehen; 37 neue Prüfungen vergleichen mit
der unveränderten Originalquelle statt erst nach Normalisierung, einschließlich
JSON/YAML, Entwürfen, Card-Paketen und HACS. Fehlende Namen behalten ihren
Ersatznamen. Das native Update auf .177/.68 ist mit HA 2026.10.2 nach frischen
Vollsicherungen bestanden: 64 Importfälle, 128 quellgetreue Codeproben und 16 echte
Card-Paket-Rundläufe. Einstellungen, Dateien, sieben Projekte und sechs Plugins
je Host sowie Papierkorb und ursprüngliche lokale Editorstände bleiben erhalten.
Das anschließende Update auf 0.1.321 ist oben dokumentiert. Details im [Card Editor](./card-editor).

Der anschließende native HACS-/HA-Vergleich besteht mit benannter Kontrollkarte:
vier ZIP-Rundläufe mit 112/112 und bytegleichen Rückexporten, 72 passende
Export-/Referenzpaare vor/nach Neuladen. Dabei wurde ein Prüfberichtfehler gefunden:
Ein leerer erster Entity-Name führt trotz Paketname zu 110/112 wegen zweier
Titelprüfungen. Die Namensdaten bleiben erhalten; diese HACS-Prüflücke ist
in 0.1.321 korrigiert und nativ bestätigt. Umfang und CSS-Verhalten stehen im [Card Editor](./card-editor).

App 0.1.319 korrigiert die Einzelkartenverluste im tatsächlichen Editor-
Übernahmepfad. Conditional-Bedingungen und eigene Entity-Namen bleiben erhalten;
259 lokale Pakettests mit 19 neuen Editor-/Entwurfs-/Exportprüfungen bestehen.
Das native Update auf .177/.68 mit HA 2026.10.2 ist nach Vollsicherungen geprüft:
32 originalgetreue JSON/YAML-Datei-/Einfügefälle samt Neuladen und acht echte
Card-Paket-Exporte mit Rückimport bestehen. Bestandsdaten, sieben Projekte und
sechs Plugins je Host sowie beide ursprünglichen lokalen Editorstände bleiben
erhalten. 16 zusätzliche Kontrollen zeigten unter 0.1.319 eine Grenze: Leere Entity-Namen
werden ersetzt, äußere Leerzeichen entfernt. Frühere lokale Tests verglichen
erst nach dieser Normalisierung; deren weitergehende Aussage ist korrigiert.
Details und Umfang im [Card Editor](./card-editor).

App 0.1.318 gleicht Import-Vorprüfung und tatsächlichen Parser an: nicht
unterstützte Markdown-Karten werden auch in verschachtelten Strukturen frühzeitig
abgelehnt. 240 lokale Pakettests inklusive 27 neuer Paritätsprüfungen bestehen.
Das Update auf .177/.68 ist mit HA 2026.10.2 nach Vollsicherungen geprüft:
24 Markdown-Ablehnungen erhalten den Editorstand, acht verschachtelte Importe
die Struktur. Bestandsdaten und lokale Editorstände bleiben erhalten. Befund unter 0.1.318:
Einzelne Conditional-Karten verlieren beim Übernehmen in den Editor Bedingungen,
einzelne Entity-Karten ihren eigenen Namen (JSON/YAML auf beiden Hosts).

Die erweiterten Conditionals sind mit HA 2026.10.2 auf den freigegebenen
Testsystemen .177 und .68 geprüft: 1.008 Sichtbarkeitsprüfungen, JSON/YAML,
Speichern/Wiederöffnen und bytegleiche HACS-Rundläufe mit je 112/112 Prüfungen.
Bestandsdaten und ursprüngliche lokale Editorstände bleiben erhalten. Die
gefundene Markdown-Vorprüflücke ist lokal in 0.1.318 korrigiert. Details und Grenzen stehen im
[Card Editor](./card-editor). Neue Netzwerktests sind nur auf diesen beiden
Adressen zulässig; die nachfolgenden Berichte anderer Hosts sind historisch.

0.1.317 korrigiert den Conditional-Import und blockiert numerische Bedingungen
ohne gültige Grenzen. Der isolierte Gesamtprojekt-Test mit Speichern, HACS-Rundlauf,
Jinja, Theme-Wechseln und Wiederverbindung besteht; 972 CSS-Vergleiche stimmen
überein. Auch das Update auf Proxmox und Pi 5 ist nach frischen Sicherungen
geprüft: je 112/112 Paketprüfungen, bytegleiche HACS-Rundläufe, 756 zusätzliche
CSS-Vergleiche, Conditional/Jinja, Theme-Wechsel und automatische Verbindung nach
HA-Core-Neustarts. Proxmox nutzt dabei vorhandenes UIX, der Pi temporäres Card-Mod.
Die ursprünglichen lokalen Editorstände sind wiederhergestellt.
Details: [Card Editor](./card-editor#aktueller-status).

Die Theme-Wechsel ohne Neuladen sind nach frischen Sicherungen auch auf Proxmox
und Pi 5 bestanden: Card-Mod und UIX getrennt, 28 Wechsel, 1.920 CSS-Vergleiche
und unveränderte Karten-/Dokumentidentitäten. Ursprüngliche Themes und
Erweiterungseinstellungen sind wiederhergestellt; Bestandsdaten bleiben erhalten.
Details: [Card Editor](./card-editor#aktueller-status).

Hell-/Dunkel-Wechsel ohne Neuladen sind jetzt isoliert mit Core-, Bubble- und
Mushroom-Karten geprüft: getrennt mit Card-Mod 4.2.1 und UIX 8.4.0, je sieben
Theme-Wechsel, 960 CSS-Vergleiche und unveränderte Karten-/Dokumentidentitäten.
Feste Überschreibungen bleiben erhalten; vererbte Farben und Radien wechseln mit.
Pi 5 und Proxmox bleiben bei dieser zusätzlichen Prüfung unverändert. Details
und Versionsgrenzen: [Card Editor](./card-editor#aktueller-status).

0.1.316 korrigiert den Bubble-CSS-Importverlust und die UIX-Vererbung am
Wurzel-Stack exportierter Scripts. Nach isolierter Prüfung ist auch das Update
auf Proxmox und Pi 5 mit vorherigen HA-Sicherungen bestanden: YAML/JSON,
bytegleicher HACS-Rundlauf mit je 112/112 Paketprüfungen und 240 zusätzliche
CSS-Vergleiche im vorhandenen dunklen Theme samt Neuladen. Ursprüngliche lokale
Editorstände sind wiederhergestellt. Vorhandene Cards erneut exportieren;
bereits verlorenes CSS aus Original oder Sicherung neu importieren. Details:
[Card Editor](./card-editor#aktueller-status).

Die CSS-Prüfung ist nach frischen Sicherungen auch nativ auf Proxmox und Pi 5
mit Card-Mod 4.2.1 und UIX 8.4.0 abgeschlossen: erzeugte Scripts und native
Referenzkarten stimmen bei den geprüften dynamischen und statischen Regeln
überein. Die Erweiterungen wurden getrennt geprüft, mit passiven Sensoren und
ohne Gerätebefehle. Die ursprüngliche Erweiterungskonfiguration ist wiederhergestellt;
vier vorhandene Projekte je Host und sechs Plugins bleiben erhalten. Details
und Versionsgrenzen stehen beim [Card Editor](./card-editor#aktueller-status).

Die tatsächliche CSS-Darstellung ist zusätzlich isoliert mit HA 2026.10.1,
Mushroom 5.2.3, Card-Mod 4.2.1 und separat UIX 8.4.0 geprüft: erzeugte Scripts
und native Referenzen stimmen bei dynamischen Farben/Rahmen, Shadow-DOM-Stilen
und UIX-Rundungen überein. `uix_style` hat keine CSS-Wirkung; CSS-Jinja benötigt
`config.entity`. Einrichtung, Beispiele und Grenzen stehen beim
[Card Editor](./card-editor#aktueller-status). Pi 5 und Proxmox bleiben dabei
unverändert; es gibt keine neue App-Version.

0.1.315 erhält importierte `card_mod`-, `uix`- und `uix_style`-Objekte in
Editor, YAML/JSON, HACS-Paketen und Scripts. UIX-Exportkonvertierung,
Stilzuordnung, Rückimport und Datenerhalt sind isoliert geprüft. Einzelheiten
und Grenzen stehen beim [Card Editor](./card-editor#aktueller-status).

Das Update 0.1.313 → 0.1.315 besteht nach frischen Sicherungen auch auf
Proxmox und Pi 5. YAML/Card-Mod und JSON/UIX bestehen dort jeweils 112/112
Prüfungen und bytegleichen Rückexport. Bestehende Daten, drei bisherige Projekte
je Host und sechs aktive Plugins bleiben erhalten; die ursprünglichen lokalen
Editorstände sind exakt wiederhergestellt. CSS-Ausführung durch die jeweiligen
Stil-Erweiterungen bleibt eine separate Prüfung.

0.1.314 vereinheitlicht YAML-/JSON-HACS-Export, Paketprüfung und Rückimport.
Beide Formate bestehen isoliert den Browser-Rundlauf mit 112/112 Prüfungen
und bytegleichem Rückexport. Vorhandene Testdaten bleiben erhalten.
Bei dieser früheren isolierten Prüfung blieben Pi 5 und Proxmox unverändert.
Die damals fehlende Stilübernahme ist ab 0.1.315 korrigiert.

0.1.313 korrigiert isoliert geprüfte Mushroom-Importverluste bei YAML/JSON und
Einzelkarten: Texte, Symbole und Farbvorlagen bleiben erhalten. Details und
Grenzen stehen beim [Card Editor](./card-editor#aktueller-status). Das Update
auf Proxmox und Pi 5 ist nach frischen Backups ebenfalls geprüft: alle vier
Importwege, Live-Ausgaben und Datenerhalt bestehen. Eigene Testprojekte bleiben
separat; vorhandene lokale Editor-Konfigurationen sind exakt wiederhergestellt.

| Arbeitspaket | Heutiger Status |
| --- | --- |
| A5 – Stabilisierung und Prüfphase | Im dokumentierten Umfang abgeschlossen. Weitere Nutzerprojekte und Langzeitmessungen sind Folgeprüfungen. |
| A6 – Französische Dokumentation | Abgeschlossen; DE/EN/FR werden gemeinsam gepflegt. Teilübersetzungen externer Plugin-Oberflächen bleiben separat gekennzeichnet. |
| A7 – Bereitstellung und Kompatibilität | Linux/systemd und native HA/HACS-Integration umgesetzt und geprüft. Weitere HA-Versionen, Plattformen und bei Bedarf Datenformatmigrationen bleiben offen. |

- Linux-Installation, Update, Rückwechsel und Wiederherstellung sind auf Debian
  12 amd64 im LXC und Raspberry Pi OS aarch64 auf Pi 4 geprüft. Auf Pi 4 bestehen
  auch Betriebssystem-Neustart, Autostart und dauerhafte HA-Verbindung ab 0.1.305.
- Gemeinsame Plugin-Verwaltung, Serverprojekte und HACS-Integrationsupdates mit
  HA-Neustart sind auf Pi 5 und Proxmox geprüft. Die HA-Kompatibilitätsmatrix
  umfasst 2026.10.1, isoliert 2026.9.4 und die genaue 2026.10.2-Kombination
  auf .68, nicht jede HA-Version.
- Card-Export/-Import, echte HACS-Repository-Registrierung, getaggte Releases,
  Updates und Wiederherstellung sind isoliert geprüft. Fehlende Sprachdateien
  und gemischte Paketversionen werden erkannt; die Prüfungen aus 0.1.310/0.1.311
  bestehen auch auf Pi 5 und Proxmox.
- 0.1.312 erhält Papierkorb und Historie über App-Updates hinweg; die Übernahme
  alter Ablagen und das Update sind auf beiden Hosts geprüft. Ein vollständiger
  verschlüsselter HAOS-Restore in frische getrennte amd64-Testinstanzen besteht
  mit gleicher und geänderter IP. 154 geprüfte Dateien, Projekt, sechs Plugins,
  Papierkorb und Historie bleiben erhalten. Bei neuer IP werden HA-URL der App
  und Runtime-URL ausdrücklich angepasst, nicht automatisch umgeschrieben.

Details: [ATLAS-Roadmap](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md)
und [Wiederherstellungsanleitung](/projects/atlas-plugins/file-studio).

## Historische Prüfstände bis 14.10.2026

Die folgenden Berichte bewahren ihren damaligen Umfang. Angaben wie „offen“ oder
„nächste Priorität“ gelten für das jeweilige Datum. Für heutige Aufgaben gelten
der aktuelle Stand oben und die nächsten Ziele unten.

**A7 – HA-Frontend in 0.1.299 (14.10.2026):** Die optionale [Integration ATLAS Runtime](/projects/atlas/frontend) mit HACS-kompatibler Struktur, Konfigurations-/Optionsdialog und eigenem Admin-Seitenleistenpanel ist umgesetzt. Sie bettet die vorhandene Laufzeit ein und überträgt keine HA-Zugangsdaten. Normale Zustandsupdates erhalten das Fenster. Ein isolierter echter HA Core 2026.10.1 bestätigt Einrichtung, Optionen, Panelregistrierung, Neuladen, Neustart und unveränderte andere Panels; die Browserprüfung bestätigt Editorbedienung und Projekterhalt. Sechs Frontend- und sieben Python-Prüfungen bestehen, ebenso HA-/App-Regressionen und Builds. Bestehende Pi-/VM-/LXC-Installationen bleiben unverändert. Download und Update durch HACS auf den realen Pi-/Proxmox-Systemen sowie weitere HA-Versionen bleiben die nächste A7-Qualifikation.

**A7 – Linux/systemd (14.10.2026, ATLAS 0.1.298):** Der optionale [Linux-Installer](/projects/atlas/linux) ist umgesetzt. Auf einem echten Debian-12-amd64-LXC unter Proxmox bestehen Installation, Update, Rückwechsel, Sicherung, Dienstneustart und automatische Rückkehr nach einem fehlerhaften Update. Konfiguration, Installationsidentität und Plugin-/Projekttestdaten bleiben bytegenau erhalten; das vorhandene deaktivierte FHEM und seine Dateien bleiben unverändert. Administration und Expert-Editor sind im LAN in DE/EN/FR geprüft. 17 Installer- und 163 HA-Prüfungen bestehen; App-, Workspace-, Docker- und Dokumentationsprüfungen bestehen. Native ARM64-Linux-Installation, andere Distributionen und Bare Metal sind noch nicht qualifiziert. Die native ATLAS-HA/HACS-Frontend-Integration bleibt als A7 offen. Bestehende HA-Installationen wurden nicht verändert.

**A6 – Dokumentationsabgleich (14.10.2026):** Die 21 ATLAS- und Plugin-Dokumentationsseiten je Sprache wurden in DE/EN/FR abgeglichen. Französische Platzhalter sind durch Anleitungen ersetzt; Navigation, Sprachwechsel, Ressourcenpfade, Beispielpakete und Aussagen zu Übersetzung und Zugangsdaten sind korrigiert. Die französische Oberfläche einzelner externer Plugins bleibt teilweise unvollständig und ist als solche dokumentiert. A7 ist die nächste vereinbarte Priorität: Linux/systemd und native ATLAS-HA/HACS-Frontend-Integration. Keine Änderung der Laufzeit, HA-Installationen oder Plugin-Daten.

**A5-Prüfphase abgeschlossen (14.10.2026, HA-App 0.1.297):** Der Abschlussabgleich deckt Renderer/Themes, größere vorbereitete Projekte, native Core-/Bubble-/Mushroom-Ausführung, Live-Templates, kurze CPU/RAM-Messungen und Wiederverbindung im jeweils dokumentierten Umfang ab. Erneut bestanden: 55 Runtime-, 532 Renderer-, 12 Theme-, 163 HA- und 11 App-/Lebenszyklusprüfungen, insgesamt 773 Regressionen; Workspace- und Doku-Build bestehen. Das ist keine Produktionsfreigabe oder Zusage einer stabilen Plugin-API. Offene Folgequalifikation: vielfältige Nutzerprojekte, Langzeit-/instrumentierte Ausfalltests unter Last, stabile API-/Versionspolitik sowie HACS-Release-Verteilung und vollständige Kartensprachprüfung. Als nächste vereinbarte Priorität folgt A6, der fachliche Abgleich und die Vervollständigung der französischen Dokumentation. Die folgenden älteren Fortschrittsabsätze bewahren den damaligen Testumfang und seine Grenzen.

**Netzunterbrechung von ungefähr drei Minuten bestätigt (14.10.2026):** Der Benutzer bestätigt getrenntes Pi-LAN und eine getrennte VM-Netzwerkkarte in Proxmox für jeweils ungefähr drei Minuten. Beide ATLAS-Editoren verbinden sich laut seiner Beobachtung automatisch wieder, ohne Neuladen oder manuellen Verbindungsstart. Unabhängige Nachprüfungen bestätigen frischen HA-Datenabruf, identische Originalprojekte und Administrationsexporte bis auf Exportzeitstempel sowie jeweils sechs aktive Plugins. Die geplanten 100 Testfelder waren vor der Unterbrechung nicht geladen; ein Konsolenprotokoll mit Socket-Zuständen oder Versuchszahlen liegt nicht vor. Der beobachtete Drei-Minuten-Fall ist damit abgeschlossen; instrumentierte Wiederholungen unter Projektlast bleiben ein eigener Prüfumfang.

**Native CPU-/RAM-Beobachtung (14.10.2026):** HA Core und ATLAS wurden über vorhandene Supervisor-Statistiken mit je 4 Basis-, 14 Last- und 4 Folgemessungen geprüft. Die Last umfasst 120 echte Karten und 40 laufende Uhrzeit-Templates. HA-Core-Mediane (Basis → Last → danach): Pi CPU 0,13 → 0,18 → 0,09 %, RAM 461,10 → 460,55 → 460,71 MiB; VM CPU 2,50 → 1,71 → 1,92 %, RAM 1374,49 → 1390,87 → 1388,90 MiB. Die größte beobachtete VM-CPU-Probe unter Last beträgt 21,71 %. Laufende Integrationen und die Statistikabfragen erzeugen ebenfalls Last; Unterschiede sind nicht eindeutig den Testkarten zuzuordnen. Dies sind kurze Container-Messungen, keine Gesamtgeräte-/Browsermessungen, kein Hardwarevergleich und kein Speicherlecknachweis. Originalprojekte und Administration bleiben bis auf Exportzeitstempel identisch, jeweils sechs Plugins aktiv; eigene Testdashboards sind entfernt.

**40 Live-Templates unter 120 echten HA-Karten geprüft (14.10.2026):** Die geprüfte ATLAS-Konfiguration wurde für diesen nativen Test um 40 unterschiedliche Mushroom-Jinja-Ausgaben für Uhrzeit und Sensorzustand ergänzt. Auf Pi und Proxmox ändern sich alle 40 Uhrzeitausgaben automatisch ohne Neuladen; je 40 Core-, Bubble- und Mushroom-Karten bleiben gemountet, ohne Konfigurationsfehler. Vorschauen wurden verworfen, Originalprojekte und Administration sind bis auf Exportzeitstempel identisch, jeweils sechs Plugins aktiv. Dies belegt einfache serverseitige Template-Auswertung und Live-Zeitänderungen. Es ist kein CPU/RAM-Benchmark, kein Test vieler wechselnder Entitäten und keine neue ATLAS-Template-Builder-Funktion.

**120 tatsächlich gerenderte HA-Karten geprüft (14.10.2026):** Der vollständige gemischte ATLAS-Export wird auf Pi 5 ARM64 und Proxmox amd64 in der echten, ungespeicherten HA-Kartenvorschau ausgeführt. Nach einem Test mit 30 Karten sind bei 120 Karten jeweils 40 Core-, 40 Bubble- und 40 Mushroom-Instanzen mit sichtbarer Größe nachgewiesen, ohne Konfigurationsfehler. Entitätsdetails bleiben bedienbar. Testvorschauen wurden verworfen und eigene leere Testdashboards nach Bestätigung entfernt; Originalprojekte und Administration bleiben bis auf Exportzeitstempel identisch, jeweils sechs Plugins aktiv. Die Prüfung nutzt Windows Chrome und einen gemeinsamen Sensor. Beobachtete Renderabläufe unter einer Sekunde enthalten Browsersteuerung und sind keine Backend- oder Hardware-Benchmarks. CPU/RAM, vielfältige Entitäten, aufwendige Live-Templates und längere Ausfälle bleiben offen.

**Gemischter Editor-Test mit 120 Feldern (14.10.2026):** Auf Pi 5 und Proxmox erhalten je 40 Core-, Bubble- und Mushroom-Felder ihre vollständigen Daten bei Titelbearbeitung, Neuladen, DE/EN/FR, Hell/Dunkel und wiederholten HA-Abfragen. Die Fläche hat keine Überlappungen. Nach Wiederherstellung stimmen Originalprojekte und Administrationsexporte bis auf Zeitstempel exakt überein; alle sechs Plugins bleiben aktiv. Die Editor-Kacheln sind keine vollständig gerenderten Lovelace-Karten. Beobachtete Bedienabläufe von ungefähr ein bis zwei Sekunden enthalten Browsersteuerung und sind keine Backend-Benchmarks. Native CPU-/Speichermessungen, größere gerenderte Dashboards und neue echte Zustandswechsel unter gemischter Last bleiben offen.

**Wiederverbindung nach geschlossenem Transport geprüft (14.10.2026):** Mit ATLAS 0.1.297 schließen wir in getrennten Testtabs auf Pi 5 ARM64 und Proxmox amd64 jeweils den bestehenden HA-WebSocket. Die vom Benutzer ausgeführte Konsolenprüfung bestätigt den alten Socket als geschlossen und den Editor erneut als verbunden, ohne Neuladen. Ein frischer HA-Datenabruf funktioniert; alle 24 Testfelder behalten IDs, Entitäten, Positionen und Größen. Nach Wiederherstellung entsprechen Originalprojekte und Administrationsexporte exakt den Sicherungen, abgesehen von Exportzeitstempeln; jeweils sechs Plugins bleiben aktiv. Diese Prüfung mit Windows Chrome belegt einen begrenzten Socket-Abbruch. Längere Netzausfälle, native Backend-Last und vielfältige Nutzerprojekte bleiben offen. Frühere Hinweise auf die noch offene Prüfung geschlossener Verbindungen sind damit für diesen begrenzten Testumfang erledigt.

**Lokale Bundle-Installation geprüft:** Das aus 0.1.297 exportierte Script wurde auf Pi 5 und Proxmox als eigene HA-Modulressource installiert. Die unveränderte Beispielkonfiguration aus dem ZIP lädt die generierte Custom Card und ihre Core-/Bubble-/Mushroom-Karten ohne Konfigurationsfehler. Die Testkarten wurden nicht gespeichert; eigene Testressourcen, Dateien und das leere Pi-Testdashboard wurden nach Bestätigung entfernt. Administrationsexporte bleiben bis auf Zeitstempel identisch, alle sechs Plugins aktiv. Das bestätigt die manuelle Installation; HACS-Repository-Veröffentlichung, vollständige Sprachprüfung, Last und Wiederverbindung bleiben getrennte Aufgaben.

**Expert-Bundle-Korrektur in 0.1.297:** Generierte Kartenscripte und HACS-Bundles übernehmen jetzt das strukturierte Expert-Layout statt lediglich eine Entitätsliste anzuzeigen. Home-Assistant-Kartenhelfer erzeugen die enthaltenen Core-/Community-Karten; konfigurierte Entitäten werden ersetzt und laufende Zustandsänderungen weitergegeben, ohne die Karten neu aufzubauen. Bestehende Projekte und ältere Scriptexporte bleiben kompatibel. Die Veröffentlichung als HACS-Repository mit Release-Verteilung bleibt ein separater Schritt.

**Native HA-/HACS-Prüfung vom 14.10.2026:** Pi 5 und Proxmox laufen nach Updates mit aktivierter HA-Sicherung auf ATLAS 0.1.296. Nach der HACS-/Bubble-/Mushroom-Installation auf dem Pi werden unveränderte ATLAS-YAML-Exporte mit Core/Bubble/Mushroom auf beiden Systemen in der echten, ungespeicherten HA-Kartenvorschau ohne Konfigurationsfehler ausgeführt. Eine zusätzliche Mushroom-Jinja-Vorschau auf dem Pi wertet den echten HA-Zustand aus. Originalprojekte und Administrationsexporte sind anschließend bis auf die Exportzeitstempel identisch; alle sechs Plugins bleiben aktiv. Testdashboards wurden nach Bestätigung entfernt. Die Vorschauen prüfen keine vollständige Bundle-Installation, Geräte-Schaltaktionen oder Leistung unter Last.

**Renderer/Themes in 0.1.296:** Fehler- und Wartestatus bleiben im Dunkelmodus rot beziehungsweise gelb; die Expert-Feldliste und Löschknöpfe sind in beiden Themes lesbar. Eine isolierte Chrome-Prüfung mit 36 vorbereiteten Entity-/Button-/Sensor-/Thermostat-/Bubble-/Mushroom-Vorschauen bestätigt DE/EN/FR, Hell/Dunkel/Auto, Neuladen sowie vier Bildschirmgrößen ohne Überlappung oder seitlichen Seitenüberlauf. Feldobjekte und Flächengröße bleiben unverändert. Automatische Systemwechsel wurden simuliert; echte HA/HACS-Ausführung und vielfältige Nutzerprojekte bleiben getrennte A5-Prüfungen.

Die nachgeholten Docker-Prüfungen vom 14.10.2026 bestehen für Standalone und HA-Paket auf Linux amd64: Build, echte Administration-/Editor-Laufzeit, Health-Checks, Container-Neustart und Plugin-Update/-Wiederherstellung mit getrennten Testdaten. Neun Backend-/Origin-Regressionsprüfungen bestehen zusätzlich im Linux-Image. Das ersetzt keine echte Supervisor-/Ingress-, ARM64- oder Browserprüfung; bestehende HA-Installationen wurden nicht verändert.

**A5-Fortsetzung vom 14.10.2026:** 0.1.295 berücksichtigt den im Browser gespeicherten Administrationsstatus auch bei direkten Plugin-Startlinks. Deaktivierte oder noch nicht aktivierte Plugins werden über diesen Weg nicht gestartet. Das ist eine Bedienpräferenz, keine Zugriffssperre für Plugin-Dateien. Isolierte Prüfungen des echten App-Servers bestätigen Installation, abgewiesene Updates, Austausch, Neustart, Deinstallation und Paket-Wiederherstellung; andere Plugin-Einträge und Testdaten bleiben erhalten. Die Testumgebung ersetzt keine echte HA-Installation. A5 bleibt für Renderer/Themes, vielfältige Projekte, native Last und geschlossene Verbindungen offen.

**A2 und A3 sind abgeschlossen (13.10.2026).** Der Benutzer hat die aktuellen
ARM64-/Mobilprüfungen als ausreichend akzeptiert. Echte iOS-/Safari-Geräte wurden
nicht getestet; Chrome-Simulatoren sind separat dokumentiert. Der Card Editor
bleibt ausschließlich im Expert-Workflow. Simple-Modus und Umschalter werden
nicht wieder eingeführt; unterstützte ältere Projektimporte bleiben erhalten.

0.1.290 verkürzt die Tablet-Card-Liste auf ein scrollbares Fenster mit zwei
Cards nebeneinander und ordnet die zugehörigen Aktionsbuttons in zwei Spalten an.

0.1.291 klappt „Raster & Zoom“ mobil standardmäßig ein und stellt die
Titelbedienung auf Tablets in eine Reihe; auf Smartphones stehen beide
Titelbuttons nebeneinander unter dem Feld. Alle Werte bleiben erhalten.

0.1.292 entfernt die verbliebene Startmodus-Auswahl aus HA-Konfiguration und
Administration und übernimmt alte Simple-Einstellungen als Expert.

A5 ist gestartet: **0.1.293** korrigiert die Reihenfolge von Snapshots und
Live-Ereignissen sowie den Fehlerstatus beim Socket-Wechsel. Eine isolierte
PC-Prüfung mit HA-Mock bestätigt 100 dargestellte Test-Cards, 2.001 Entitäten,
drei Wiederverbindungen, 150 Live-Updates, Theme-Wechsel und Projekt-Roundtrips
in DE/EN/FR. 162 HA-Tests sind bestanden. Diese Messungen sind synthetisch.

Die native A5-Folgeprüfung lädt auf Pi 5 und Proxmox jeweils 100 kompakte und
24 größere Entitäts-Cards ohne Überlappungen. Theme-Wechsel, Neuladen und
DE/EN/FR erhalten die Felder. Auf dem Pi kommen echte Backup-Statuswechsel
live an; auf Proxmox werden zunächst 3.711 Entitäten und 143 Lovelace-Ressourcen
geladen. Der beobachtete VM-CPU-Wert bleibt konstant, eine Wertänderung ist dort
damit nicht nachgewiesen. Vorher wurden lokale verschlüsselte HA-Backups erstellt.
Die ursprünglichen Editor- und Admin-Konfigurationen sind anschließend exakt
wiederhergestellt, abgesehen vom Exportzeitpunkt; alle sechs Plugins bleiben
aktiv. Nach einem vom Benutzer ausgeführten Proxmox-Neustart verbindet sich der
Editor erneut und das Originalprojekt bleibt unverändert.

Getestet wurden vorbereitete Entitäts-Layouts im Desktop-Browser. Vielfältige
Nutzerprojekte, native Backend-Lastmessungen, Wiederverbindung nach geschlossenem Transport und
breitere Plugin-Lebenszyklusprüfungen bleiben in A5 offen. Desktop-Rendering
ist kein Pi-Leistungsbenchmark; native Neustartprüfung und simulierte
Socket-Abbrüche sind getrennte Nachweise.

**0.1.294** behebt die Wiederverbindung nach längeren Netzwerkausfällen: Der
Editor versucht es nach den bisherigen drei Versuchen weiter, mit höchstens
30 Sekunden Abstand. Authentifizierungs- und Protokollfehler stoppen die
automatischen Versuche, bis die Verbindung korrigiert wird. Ein isolierter
Test mit acht Sekunden nicht erreichbarem Endpunkt bestätigt die Erholung
ohne Neuladen und mit unverändertem Projekt. Beim echten LAN-Test wurde das
Pi-Kabel für etwa zwölf Sekunden getrennt. Alle 100 Testfelder blieben erhalten;
anschließend kamen Live-Daten ohne Neuladen wieder an. Die beobachtete
WebSocket-Verbindung blieb verbunden; eine neu aufgebaute native Verbindung
ist damit nicht nachgewiesen. Beide Systeme laufen mit 0.1.294. Der abschließende
Exportvergleich bestätigt unveränderte Admin-Einstellungen, Verschlüsselungsdaten,
aktive Plugin-IDs und Originalprojekte. Nur das bewusst aktualisierte externe
Icon Studio hat eine neue Version. Ein isolierter Docker-Build und /health
bestätigen außerdem die gemeinsame Administration-/Editor-Laufzeit.
Der Nutzer bestätigt außerdem die Funktion in einer macOS-Ventura-VM direkt auf Proxmox, meldet
aber sehr träges Verhalten. Das ist ein Funktionstest mit Leistungseinschränkung;
die Ursache wurde noch nicht gemessen oder geklärt.

Stand **13.10.2026**: Framework **0.2.0-alpha.88**, HA-App **0.1.294**. Die vier
vereinbarten Stabilisierungspunkte sind abgeschlossen. Die Abschlussprüfung
umfasst 870 Workspace-Tests, fünf ergänzende Tests, alle Typprüfungen und Builds
sowie 15 isolierte Browser-Prüfpunkte in DE/EN/FR. Ältere Admin-Einstellungen,
Repository-Einträge, Darstellung und aktive Plugin-IDs bleiben bei der geprüften
Migration erhalten; Geheimnisse werden verschlüsselt übernommen.

A1 ist an der echten HA-Installation geprüft: Supervisor-Update von 0.1.287 auf
0.1.288, zusätzlicher Neustart und Ingress für alle sechs installierten Plugins.
Administrationseinstellungen, aktive Plugins und die vollständige
Editor-Konfiguration stimmen vor und nach Update und Neustart überein, abgesehen
vom Exportzeitpunkt. Ein lokales verschlüsseltes HA-Backup wurde vorher erstellt.
0.1.288 korrigiert die Laufzeit-Versionsanzeige in Administration; HA-Optionen
und Plugin-Verträge bleiben unverändert. Der Editor verbindet sich erneut und
lädt echte Entitäten und Lovelace-Ressourcen. Der vorhandene Expert-Arbeitsbereich
war leer; größere gefüllte Projekte bleiben A5. Hardware-Aktionen, Mobilbrowser,
ARM64 und sämtliche plugininternen Projektformate sind damit nicht geprüft.
Nur der Card Editor ist das integrierte ATLAS-Referenzplugin; eigenständige
Plugins werden separat gepflegt.

A2 ist in Emulation geprüft: HA-Images für amd64 und ARM64 sowie ein mobiler
Chromium-Touch-Kontext mit 360×800, 390×844, 844×390 und 768×1024 Pixeln in
DE/EN/FR. 0.1.289 behebt Überläufe in Administration und Editor und passt die
Problembericht-, YAML-Import- und Exportdialoge an schmale Bildschirme an.
Einstellungen, gefüllte Testprojekte und Plugin-Daten bleiben durch Sprachwechsel,
JSON/HACS-Import und Neustart erhalten. Ein x86-Host emuliert ARM64; echte
Raspberry-Pi-Leistung sowie Android/iOS, Touch-Drag/Resize, Bildschirmtastatur
und native Datei-/Download-Dialoge bleiben offen. Die reale HA-Installation
wurde für diese isolierten Prüfungen nicht verändert.

Der native A2-Test auf einem **Raspberry Pi 5 / rpi5-64** ist ebenfalls
bestanden: HA OS 18.3, ATLAS 0.1.289, `aarch64` und Node `arm64`. Alle sechs
Plugins öffnen über Ingress; Terminal, File-Studio-Pfade und MDI-Katalog
funktionieren. Vor dem ATLAS-Neustart wurde ein lokales verschlüsseltes
HA-Backup erstellt. Danach stimmen Administrationseinstellungen,
Plugin-Metadaten und vollständiger Editor-Export weiterhin überein, abgesehen
vom Exportzeitpunkt. Der Editor verbindet sich mit 27 echten Entitäten.
Der vorhandene Arbeitsbereich war leer. Desktop-Chrome-Ansichten mit 390×844
und 844×390 passen über den echten Pi-Ingress ohne Seitenüberlauf. Physische
Mobilbrowser, größere gefüllte Projekte und Last-/Leistungsmessungen sind
damit nicht geprüft; ein ARM64-Supervisor-Update wurde hier nicht durchgeführt.

Ergänzend bestätigt der Benutzer auf einem **echten Android-Tablet**: Hub und
Administration funktionieren hoch und quer sowie in DE/EN/FR. Nach dem Wechsel
der HA-URL von `homeassistant.local:80` zur erreichbaren IP-Adresse funktioniert
auch die Verbindung; YAML-Dialog und „Problem melden“ wurden als OK gemeldet.
Dies ist eine Benutzerbestätigung, kein automatisierter Gerätetest.
[Verbindungshinweis für Mobilgeräte](./homeassistant#verbindung-auf-tablet-und-smartphone).
Touch-Drag/Resize, Bildschirmtastatur, native Datei-/Download-Dialoge und iOS
wurden damit nicht unabhängig auf allen Geräten geprüft. A2 ist dennoch mit
der Benutzerfreigabe abgeschlossen; diese Grenzen sind keine offenen A2-Aufgaben.

Die grundlegende Repository- und Dokumentationsstruktur ist eingerichtet.

Abgeschlossen sind unter anderem:

- Monorepo-Struktur mit `pnpm` Workspaces
- Governance- und Architektur-Dokumente
- Bereinigung der Events- und Contracts-Schicht
- öffentliche Event-Verträge
- Referenzimplementierung `DefaultEventBus`
- Heartbeat- und EventBus-Grundlagen
- Atlas Administration mit Plugin-Verwaltung, Capability-Freigaben,
  Home-Assistant-Verbindung, Add-on-Update-Hinweisen und vorbereitetem
  Seitenleisten-Helfer
- Plugin-Hub mit Startlogik fuer 0, 1 oder mehrere aktive Plugins,
  dynamischen Plugin-URLs, URL- und `panel_iframe`-Kopie sowie standardmäßig
  eingeklappten Fähigkeitslisten und Seitenleisten-URLs pro Plugin; Card
  Editor, Administration und Plugin-Assets laufen über App-/Ingress-fähige
  ATLAS-Routen statt nur über separate Entwicklungsports
- Home Assistant Card Editor mit direktem Expert-Workflow, HACS-nahem Export,
  Problembericht, dreispaltigem Import-/Entitätenbereich und getrennten
  `X`-, `Y`- und Zoom-Reglern für das quadratische Expert-Raster
- Snapshot und Pre-Release-Tag für den Event-Stand
- ATLAS File Studio als zweites Plugin mit `/config`-Standard, optionaler
  `/addons`-Freigabe, YAML-Prüfung, Upload/Download, Backups, Verlauf mit
  Vergleich und Wiederherstellung, Suchfiltern, Mehrfachauswahl,
  Drag-and-drop-Upload, Papierkorb, Favoriten, Dateityp-Icons und
  secret-freiem Problembericht mit GitHub-Issue-Link
- ATLAS Automation Exporter / Editor als eigenständiges GitHub-installierbares
  Plugin mit System-`automations.yaml`, YAML-Upload, Zeitstempel-Export,
  Exportübersicht, File-Studio-Anbindung und Analysehinweisen für fehlende oder
  doppelte IDs/Aliasse, fehlende Trigger/Actions und deaktivierte Automationen;
  Service-Aufrufe werden sowohl aus `service:` als auch aus modernem
  `action: domain.service` erkannt, die Detail-YAML wird farbig dargestellt und
  lange Automationslisten scrollen intern

## Aktueller Schwerpunkt

Der aktuelle Entwicklungsschwerpunkt ist:

```text
ATLAS Card Editor, Runtime und Erhalt bestehender Einstellungen und Plugins
```

Der Schwerpunkt liegt auf realistischen Projekten, Dauerlast und den noch
offenen Plattform- und Kompatibilitätsprüfungen.
Der aktuelle Home-Assistant-App/Add-on-Stand ist `0.1.312`. Administration und
Plugin-Hub unterstützen Deutsch, Englisch und Französisch und teilen ihre
gespeicherte Spracheinstellung über die getrennten App-Ports hinweg.

## Bereits vorbereitete Architekturentscheidungen

Zu den vorbereiteten Themen gehören:

- Kernel Contracts
- Service Container
- Dependency Injection
- Service Descriptor
- Event-Verträge
- Referenzimplementierungen

## Nächste Ziele

Offen sind die folgenden ATLAS-Punkte:

1. **Reale Projekte und Dauerlast:** vielfältige Entitäten, Custom Cards und Themes sowie längere CPU-/RAM-Messungen und instrumentierte Netzausfälle unter Projektlast prüfen.
2. **Wiederherstellung auf weiterer Hardware:** den isolierten amd64-HAOS-Restore um physische beziehungsweise ARM64-Hardware erweitern, mit separaten Testsystemen und Sicherungen.
3. **Weitere Kompatibilität:** zusätzliche HA-Versionen, Linux-Distributionen, Plugin-/API-Verträge und bei Bedarf Datenformatmigrationen qualifizieren.

**A1, A4, A5 und A6 sind abgeschlossen; die A7-Bereitstellungswege sind umgesetzt.** Abgeschlossene Funktionen bleiben in
der Historie dokumentiert und sind keine offenen Aufgaben. Eigenständige Plugins
führen ihre Implementierungsaufgaben in ihren eigenen Projekten.
Die verbindliche offene Liste steht in der [ATLAS-Roadmap](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

## Langfristige Perspektive

Nach Abschluss der grundlegenden Runtime soll ATLAS als technische Basis für weitere UGSo-Projekte dienen.

Geplante Folgeprojekte sind:

- **Lovelace UV Card**: eine Home-Assistant-/Lovelace-Card für UV-Index, Schutzstatus, Grenzwerte und visuelle Dashboard-Ausgabe. Als Inspiration ist `filipnet/haos-uv-index` vorgemerkt: relevant sind UV-Index-Sensoren, farbcodierte Risikostufen, WHO-nahe Schutzempfehlungen, Mushroom-kompatible Darstellung und optionale Benachrichtigungs-Automationen. Die Umsetzung soll eine eigene UGSo/ATLAS-Card bleiben.

::: info Hinweis
Die Roadmap kann sich während der Entwicklung ändern. Die Seite beschreibt den aktuellen Planungsstand.
:::
