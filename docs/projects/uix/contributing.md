---
description: Beitraege zur UIX-Dokumentation und zum Projekt
---
# Mitwirken

Die folgenden Hinweise beziehen sich auf Beiträge zum originalen UIX-Repository. Diese deutsche Dokumentation wird separat als inoffizielle Übersetzung gepflegt.

UIX-Dokumentation ist ein Bereich, in dem jede Nutzerin und jeder Nutzer helfen kann. Wenn Python in deiner Umgebung installiert ist, kannst du die Dokumentationsquellen bearbeiten und das Ergebnis lokal in Echtzeit ansehen.

## Dokumentation aktualisieren

Die UIX-Dokumentation wird aus Markdown-Dateien mit Zensical gebaut. So startest du die Dokumentationsseite lokal:

1. Repository klonen.
2. Optional eine Python-Umgebung anlegen und `zensical` installieren, falls es nicht global installiert ist.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install zensical
```

3. In den Dokumentationsordner wechseln und Zensical starten.

```bash
cd docs
zensical serve
```

Danach ist die lokale Dokumentationsseite unter `http://localhost:8000` erreichbar.

Du kannst Zensical auch auf einer anderen Adresse oder einem anderen Port starten:

```bash
zensical serve localhost:9000
```

## Pull Requests einreichen

Bitte beachte fuer Pull Requests:

- Fuege `uix.js` nicht zu Commits hinzu. Diese Ressourcendatei wird beim Release gebaut. UIX kann hier nicht einfach Release-Assets nutzen, weil `uix.js` im Ordner `custom_components/uix` liegen muss.
- Fuege Tests fuer neue visuelle Komponenten hinzu. Hinweise stehen in der `README.MD` im Testordner des Repositories.
- Verwende nach Moeglichkeit Conventional-Commit-Namen. Das ist nicht zwingend, weil Pull Requests beim Mergen zusammengefasst und der Titel angepasst werden kann, hilft aber bei der Einordnung.
- Wenn es sich um eine Breaking Change handelt, erwaehne im Commit-Footer oder Pull Request `BREAKING CHANGE: ...`.
- Verweise im Commit-Footer oder Pull Request auf behobene Issues, zum Beispiel `fixes #1234`.

## Externe Dokumentationsuebersetzungen

Direkte Sprachuebersetzungen werden nicht als normale Kopie in das Hauptrepository aufgenommen. Der bevorzugte Weg ist eine extern gepflegte Uebersetzung, die in der Originaldokumentation registriert wird.

Wichtig fuer eine externe Uebersetzung:

- Sie muss klar als Uebersetzung gekennzeichnet sein.
- Sie sollte zur passenden UIX-Version passen.
- Bilder und Animationen sollten nach Moeglichkeit aus der Originaldokumentation referenziert oder nach dem offiziellen Workflow erzeugt werden.
- Bei neuen UIX-Releases muss die Uebersetzung nachgezogen werden, damit Nutzer keine veralteten Informationen fuer aktuell halten.

Der Registrierungsweg fuer externe Uebersetzungen ist in der offiziellen Dokumentation beschrieben: [External documentation translations](https://uix.lf.technology/contributing/#external-documentation-translations).

## Hinweise fuer Dokumentationsuebersetzer

Externe Uebersetzungen sollten sich am aktuellen Originalstand orientieren. Bei UIX ist das besonders wichtig, weil viele Beispiele direkt Home-Assistant-YAML enthalten und kleine Unterschiede das Verhalten aendern koennen.

Empfohlenes Vorgehen:

1. Original-Repository aktualisieren.
2. Aenderungen der Dokumentation seit der letzten uebersetzten Version pruefen.
3. Neue oder geaenderte Seiten uebersetzen.
4. Beispiele mit dem Original vergleichen.
5. Lokalen Build ausfuehren.
6. Versionshinweis und Link zur englischen Originalseite pruefen.

## Version und Originalquelle

Eine externe Uebersetzung sollte sichtbar zeigen:

- fuer welche UIX-Version sie gepflegt wurde
- dass sie eine inoffizielle Uebersetzung ist
- wo die englische Originaldokumentation liegt
- wann die Uebersetzung zuletzt aktualisiert wurde

So koennen Nutzer bei Unsicherheit schnell gegen die Originaldokumentation pruefen.

## Bilder und Animationen

Das UIX-Projekt erzeugt viele Bilder und Animationen aus seinem eigenen visuellen Test- und Dokumentationsworkflow. Eine externe Uebersetzung sollte diese Assets nicht unnoetig duplizieren.

Wenn Bilder benoetigt werden, sind diese Wege sinnvoll:

- Originalbilder extern verlinken, wenn das Projekt es erlaubt.
- Eigene Bilder klar als Beispiele der Uebersetzung kennzeichnen.
- Keine veralteten Screenshots verwenden, wenn sich die UIX-Oberflaeche geaendert hat.

## Abgleich mit neuen Releases

Bei neuen Minor-Versionen sollte die Uebersetzung neu geprueft werden. Besonders kritisch sind:

- neue Konfigurationsoptionen
- geaenderte YAML-Beispiele
- neue Sparks oder Forge-Funktionen
- geaenderte Theme-Variablen
- Hinweise zu Breaking Changes

## Pull-Request-Grenze

Fuer die Registrierung einer externen Uebersetzung soll im UIX-Hauptrepository nur die dafuer vorgesehene Registrierungsdatei geaendert werden. Die eigentliche deutsche Dokumentation bleibt im eigenen Repository.

## Was nicht in einen normalen Beitrag sollte

Bitte vermeide bei Beitraegen zum Originalprojekt:

- automatisch gebaute Dateien, die beim Release erzeugt werden
- doppelte Bilder oder Animationen ohne klaren Grund
- grosse Formatierungsaenderungen ohne fachliche Aenderung
- Uebersetzungsdateien direkt im Hauptrepository, wenn der externe Uebersetzungsweg vorgesehen ist
- Beispiele, die nicht mit dem aktuellen UIX-Verhalten getestet wurden

Damit bleiben Pull Requests kleiner und fuer Maintainer leichter pruefbar.
