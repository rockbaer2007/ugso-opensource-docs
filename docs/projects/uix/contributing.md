---
description: Beiträge zur UIX-Dokumentation und zum Projekt
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

Bitte beachte für Pull Requests:

- Füge `uix.js` nicht zu Commits hinzu. Diese Ressourcendatei wird beim Release gebaut. UIX kann hier nicht einfach Release-Assets nutzen, weil `uix.js` im Ordner `custom_components/uix` liegen muss.
- Füge Tests für neue visuelle Komponenten hinzu. Hinweise stehen in der `README.MD` im Testordner des Repositories.
- Verwende nach Möglichkeit Conventional-Commit-Namen. Das ist nicht zwingend, weil Pull Requests beim Mergen zusammengefasst und der Titel angepasst werden kann, hilft aber bei der Einordnung.
- Wenn es sich um eine Breaking Change handelt, erwähne im Commit-Footer oder Pull Request `BREAKING CHANGE: ...`.
- Verweise im Commit-Footer oder Pull Request auf behobene Issues, zum Beispiel `fixes #1234`.

## Externe Dokumentationsübersetzungen

Direkte Sprachübersetzungen werden nicht als normale Kopie in das Hauptrepository aufgenommen. Der bevorzugte Weg ist eine extern gepflegte Übersetzung, die in der Originaldokumentation registriert wird.

Wichtig für eine externe Übersetzung:

- Sie muss klar als Übersetzung gekennzeichnet sein.
- Sie sollte zur passenden UIX-Version passen.
- Bilder und Animationen sollten nach Möglichkeit aus der Originaldokumentation referenziert oder nach dem offiziellen Workflow erzeugt werden.
- Bei neuen UIX-Releases muss die Übersetzung nachgezogen werden, damit Nutzer keine veralteten Informationen für aktuell halten.

Der Registrierungsweg fuer externe Uebersetzungen ist in der offiziellen Dokumentation beschrieben: [External documentation translations](https://uix.lf.technology/contributing/#external-documentation-translations).

## Hinweise für Dokumentationsübersetzer

Externe Übersetzungen sollten sich am aktuellen Originalstand orientieren. Bei UIX ist das besonders wichtig, weil viele Beispiele direkt Home-Assistant-YAML enthalten und kleine Unterschiede das Verhalten ändern können.

Empfohlenes Vorgehen:

1. Original-Repository aktualisieren.
2. Änderungen der Dokumentation seit der letzten übersetzten Version prüfen.
3. Neue oder geänderte Seiten übersetzen.
4. Beispiele mit dem Original vergleichen.
5. Lokalen Build ausführen.
6. Versionshinweis und Link zur englischen Originalseite prüfen.

## Version und Originalquelle

Eine externe Übersetzung sollte sichtbar zeigen:

- für welche UIX-Version sie gepflegt wurde
- dass sie eine inoffizielle Übersetzung ist
- wo die englische Originaldokumentation liegt
- wann die Übersetzung zuletzt aktualisiert wurde

So können Nutzer bei Unsicherheit schnell gegen die Originaldokumentation prüfen.

## Bilder und Animationen

Das UIX-Projekt erzeugt viele Bilder und Animationen aus seinem eigenen visuellen Test- und Dokumentationsworkflow. Eine externe Übersetzung sollte diese Assets nicht unnötig duplizieren.

Wenn Bilder benötigt werden, sind diese Wege sinnvoll:

- Originalbilder extern verlinken, wenn das Projekt es erlaubt.
- Eigene Bilder klar als Beispiele der Übersetzung kennzeichnen.
- Keine veralteten Screenshots verwenden, wenn sich die UIX-Oberfläche geändert hat.

## Abgleich mit neuen Releases

Bei neuen Minor-Versionen sollte die Übersetzung neu geprüft werden. Besonders kritisch sind:

- neue Konfigurationsoptionen
- geänderte YAML-Beispiele
- neue Sparks oder Forge-Funktionen
- geänderte Theme-Variablen
- Hinweise zu Breaking Changes

## Pull-Request-Grenze

Für die Registrierung einer externen Übersetzung soll im UIX-Hauptrepository nur die dafür vorgesehene Registrierungsdatei geändert werden. Die eigentliche deutsche Dokumentation bleibt im eigenen Repository.

## Was nicht in einen normalen Beitrag sollte

Bitte vermeide bei Beiträgen zum Originalprojekt:

- automatisch gebaute Dateien, die beim Release erzeugt werden
- doppelte Bilder oder Animationen ohne klaren Grund
- große Formatierungsänderungen ohne fachliche Änderung
- Übersetzungsdateien direkt im Hauptrepository, wenn der externe Übersetzungsweg vorgesehen ist
- Beispiele, die nicht mit dem aktuellen UIX-Verhalten getestet wurden

Damit bleiben Pull Requests kleiner und für Maintainer leichter prüfbar.
