# UGSo Open Source Docs

VitePress-Dokumentation für:

```text
https://opensource.ugso-software.de/
```

## Lokal starten

```powershell
npm install
npm run docs:dev
```

Lokal öffnen:

```text
http://localhost:5173/
```

## GitHub Pages einrichten

1. Repository zu GitHub pushen.
2. Unter `Settings -> Pages` die Quelle `GitHub Actions` auswählen.
3. Als Custom Domain eintragen:

```text
opensource.ugso-software.de
```

4. Beim Domainanbieter einen CNAME setzen:

```text
opensource -> rockbaer2007.github.io
```

Die Datei `docs/public/CNAME` ist bereits enthalten.
