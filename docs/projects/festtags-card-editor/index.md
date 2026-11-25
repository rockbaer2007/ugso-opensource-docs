---
title: Festtags-Card-Editor
description: Weihnachtssteuerung mit fünf Zeitplänen, Festtagsbildern, GIF-Dekoration und Schneefall.
---

# Festtags-Card-Editor

**Version 0.1.12** · Editor DE/EN · Dokumentation DE/EN/FR.

[English](/en/projects/festtags-card-editor/) · [Français](/fr/projects/festtags-card-editor/)

![Weihnachtssteuerung mit eigenem Hintergrund, Schneefall und zwei Lichtsteuerungen](/images/festtags-card-editor/weihnachtssteuerung-card.png)

Beispiel aus einem eingerichteten Dashboard. Das Hintergrundmotiv wird vom Nutzer bereitgestellt und gehört nicht zum App-Paket. Die Schneefallbewegung ist im Bildschirmfoto nicht sichtbar.

## Funktionen

- Region und Land auswählen: 47 Länder und eigene Termine, westliche/julianische Traditionen.
- Bis zu fünf Ziele (`light`, `switch`, `input_boolean`), jeweils mit eigener Ein-/Ausschaltzeit.
- Täglich im Zeitraum oder nur an ausgewählten Festtagen; Jahreswechsel und Advent werden automatisch berechnet.
- Vorgabe: 1. Advent bis einschließlich 10. Januar. Pausenschalter erhalten ihren Zustand nach Neustart.
- Sensoren für aktuelle/nächste Festtage und nächste Schaltung; eigene Dashboard-Card.
- Optionales Statussymbol: `mdi:lightbulb` für Ein, `mdi:lightbulb-outline` für Aus. Anzeige folgt dem tatsächlichen Zielzustand.

Die Länderlisten sind Vorschläge für Fest- und Brauchtumstage, kein vollständiger gesetzlicher Feiertagskalender.
1. und 2. Weihnachtstag, Stephanstag, Sinterklaas, Pakjesavond, Heilige Drei Könige und Epiphanias sind separate Einträge. Einige liegen am selben Tag.

## Installation und Update

1. Vollständiges HA-Backup erstellen und das [UGSo-App-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons) hinzufügen/aktualisieren.
2. **Festtags-Card-Editor** installieren bzw. aktualisieren und starten. Architekturen: aarch64 und amd64.
3. **Home Assistant vollständig neu starten**, nicht nur die Editor-App. Dadurch wird die aktualisierte Integration geladen.
4. Editor öffnen. Bei Erstinstallation **Integration einrichten** wählen. Region/Land, Ziele und Zeiten einstellen und speichern.
5. **Card-Ressource einrichten** anklicken und das Dashboard vollständig neu laden.

```yaml
type: custom:weihnachtssteuerung-card
title: Weihnachtssteuerung
```

Bestehende Einstellungen und Nutzerbilder bleiben erhalten. Die Steuerung läuft im HA-Core weiter, wenn die Editor-App gestoppt wird. Der Editor ist für HA-Administratoren über Ingress erreichbar. Die Entitätsauswahl lässt sich nach Name, ID, Bereich und Gerät durchsuchen.

## Eigene Bilder und Hintergründe

Es werden keine Bilder mitgeliefert. Nur eigene Dateien mit passenden Nutzungsrechten verwenden.

| Zweck | HA-Ordner | URL-Pfad |
| --- | --- | --- |
| Festtagsbilder pro Land/Tag | `/config/www/weihnachtssteuerung/bilder` | `/local/weihnachtssteuerung/bilder` |
| Hintergründe und Dekorationen | `/config/www/weihnachtssteuerung/background` | `/local/weihnachtssteuerung/background` |

PNG, JPG, WebP und GIF hochladen (maximal 5 MiB/16 Megapixel); Animationen bleiben unverändert. Vorhandene SVG-Dateien können zugeordnet, aber nicht hochgeladen werden. Doppelte Dateinamen werden ergänzt, nicht überschrieben. **Lösen** bzw. **Keine Datei** entfernt nur die Zuordnung.

Festtagsbilder erscheinen in der Card 110 px hoch, proportional skaliert; Vorschau im Editor 90 × 90 px. Mehrere Motive können gleichzeitig erscheinen. Hintergrund und Dekoration lassen sich getrennt mit Transparenz, Größe und X/Y-Position einstellen. 0 % Transparenz = sichtbar, 100 % = unsichtbar; X/Y 0/0 = links oben, 100/100 = rechts unten. Abdunklung verbessert die Lesbarkeit. Texte und Buttons bleiben über den Effekten bedienbar.

## Schneefall

- Modus **Schneefall** oder **Bild + Schneefall** wählen. Eine separate GIF-Dekoration kann zusätzlich aktiv sein.
- 6–40 Flocken; tatsächlicher Kreisdurchmesser 1–20 CSS-Pixel, Standard 4 px.
- **Schneefall trotzdem animieren** ist eine bewusste Ausnahme von **Bewegung reduzieren**, nur für diese Card. Standardmäßig ausgeschaltet.
- Außerhalb des sichtbaren Bereichs und bei ausgeblendeter Seite pausiert die Animation weiterhin.
- Nach Konfiguration speichern; für geänderte Card-Dateien die Ressource einrichten und Dashboard neu laden.

## Bestätigter Chrome-Test am 25. November 2026

Auf einer HA-Installation mit Card **0.1.12** wurden ein geladenes GIF und **30 gleichzeitig animierte Schneeflocken** bestätigt. Die Flockenposition änderte sich zwischen zwei Beobachtungen; Animation `snow-fall`, Zustand `running`. Es wurden bei diesem Kombinationstest keine Einstellungen geändert. Dies ist kein allgemeiner Leistungstest für alle Tablets.

**Wenn Firefox animiert und Chrome nicht:** Im beobachteten Fall lud Chrome noch die Ressource von **0.1.8**. Ein Neuladen allein ersetzte den alten Ressourcenverweis nicht. Im aktuellen Editor **Card-Ressource einrichten** ausführen, dann das Dashboard vollständig neu laden. Zusätzlich muss bei aktivem Bewegung reduzieren die Ausnahme gespeichert sein. Die sichtbare Card pausiert nicht mehr, sobald die aktuelle Datei und die ausdrückliche Ausnahme wirksam sind.

## Links

- [Release mit ZIPs](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/festtags-card-editor-v0.1.12)
- [Quellcode und ausführliche Anleitung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/festtags_card_editor)
- [UGSo HA Apps](/projects-mqtt/)
