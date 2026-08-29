---
description: Beitraege zur UIX-Dokumentation und zum Projekt
---
# Mitwirken

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
