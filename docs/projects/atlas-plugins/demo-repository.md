# Demo-Repository

Das Demo-Repository dient als reale Testquelle für den ATLAS-Installationsfluss:

`https://github.com/rockbaer2007/atlas-plugin-repository-demo`

## Zweck

- Plugin-Repository in der Administration hinzufügen
- Repository-Marker prüfen
- verfügbare Plugins im Hub und in der Administration anzeigen
- Versionen vergleichen und Updates sichtbar machen
- Installations-Zwischenseite testen
- ATLAS File Studio als zweiten realen Plugin-Eintrag laden
- Installations- und Update-Verhalten der Home-Assistant-App gegen echte GitHub-Repositories prüfen

## Installationsseite

Die öffentliche Seite liegt auf GitHub Pages:

`https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

Der Button kopiert die ATLAS-Repository-URL und erklärt, dass sie in der ATLAS-Administration eingefügt werden muss. Er öffnet nicht den Home-Assistant-Add-on-Store, weil ATLAS-Plugins und Home-Assistant-Add-ons unterschiedliche Repository-Formate besitzen.

## Update-Test

Bei jeder funktionalen Änderung am Plugin-Paket muss die Plugin-Version erhöht werden. Nur dann kann die Administration ein Update gegenüber der bereits installierten Version erkennen.

Das gilt auch für Testpakete: Wenn sich UI, Manifest, Icons, Paketinhalt oder Verhalten ändern, muss die veröffentlichte Version im Repository hochgezählt werden.
