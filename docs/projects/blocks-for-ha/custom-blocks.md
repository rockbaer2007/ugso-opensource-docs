---
title: Eigene Blocks und Template-Pakete
---
# Eigene Blocks und Template-Pakete

Seit **0.1.18** öffnet **Block-/Template-Editor** neben dem Automationsnamen einen Dialog mit 95 % Fensterbreite und -höhe. Auf Mobilgeräten nutzt er 98 % und scrollt intern. Felder gestalten den Block; rechts stehen eine echte Blockly-Vorschau, die HA-Ausgabe mit Beispielwerten und kopierbares Paket-JSON.

## Erstellen und übernehmen

1. Paket-ID, Version, Name, Autor, Lizenz und Beschreibung eintragen oder **Beispiel laden** wählen.
2. Einen oder mehrere Blocks hinzufügen: **Wert/Jinja**, **Bedingung/Jinja**, **Aktion/HA-YAML** oder **Auslöser/HA-YAML**.
3. Felder für Text, Zahl, Boolean oder Entität und Werteingänge für Number, String, Boolean oder Value anlegen.
4. Jinja-Ausdruck beziehungsweise deklarative HA-Zuordnung eintragen und Vorschau prüfen.
5. **Übernehmen** installiert das Paket lokal. Seine Blocks stehen unter **Benutzerdefiniert** unmittelbar vor der Suche.

Jinja-Ausdrücke werden ohne äußere Template-Klammern angegeben. Platzhalter wie `${ENTITY}` verweisen auf Feld- oder Eingangsnamen. Felder werden typgerecht eingesetzt; Werteingänge werden als Ausdrücke geklammert. Die HA-Zuordnung verwendet ganze JSON-Werte wie `{"$field":"ENTITY"}` oder `{"$input":"VALUE"}`. Das [Beispiel Sensor und Licht](./catalog/sensor-light) zeigt alle Zuordnungen.

## Zwei Importwege und Veröffentlichung

- **Code einfügen:** Paket-JSON unter „JSON-Code oder ZIP importieren“ einfügen, **JSON prüfen**, Vorschau ansehen, **Übernehmen**.
- **ZIP einlesen:** Paketdatei auswählen, Vorschau ansehen, **Übernehmen**.

**JSON herunterladen**, **Code kopieren** und **Katalog-ZIP herunterladen** exportieren dasselbe Paket. Das ZIP enthält `block-package.json` und `README.md`. Die Open-Source-Seiten erklären die Pakete und bieten Code und Downloads; der separate [Katalog](https://visualstudio.ugso-software.de/blocks) erhält eine eigene Blockpaket-Seite. Neue Veröffentlichungen werden manuell geprüft; der Editor lädt nichts automatisch hoch. [Katalog und Beispiel](./catalog/).

## Speicherung und Konflikte

Paketformat `ugso-ha-block-package`, `schemaVersion: 1`; Paket-/Block-IDs bestehen aus Kleinbuchstaben, Ziffern und einzelnen Unterstrichen. Installierte Pakete bleiben in diesem Browser gespeichert. Projektformat **3** bettet verwendete Pakete samt Abhängigkeiten ein. Projektformate 1 und 2 bleiben lesbar. Ein fehlerhafter Projektimport installiert keine neuen Paketdefinitionen.

Identische Pakete können erneut importiert werden. Eine bestehende Paket-ID mit anderem Inhalt oder anderer Version wird zurückgewiesen. Für eine eigene Variante eine neue Paket-ID verwenden; automatische Updates und Deinstallation folgen später. Abhängigkeiten müssen mit passender exakter Version vorhanden sein oder gemeinsam im Projekt eingebettet werden. Zyklische Abhängigkeiten werden abgelehnt.

Grenzen: 16 installierte Pakete, 32 Blocks je Paket, 12 Felder und 8 Werteingänge je Block; JSON höchstens 500.000 Zeichen, ZIP höchstens 1 MB komprimiert und entpackt. ZIPs erlauben ausschließlich die beiden beschriebenen Dateien.

## Grenzen des ersten Editors

Der Editor ist eine eigene HA-orientierte Oberfläche mit Blockly-Vorschau. Der originale [Blockly Block Factory](https://docs.blockly.com/guides/create-custom-blocks/blockly-developer-tools/) ist noch nicht eingebettet. Dessen rohes Block-JSON allein enthält keine HA-Funktion und ist kein importierbares UGSo-Paket. JavaScript-/Python-/PHP-/Lua-/Dart-Generatoren werden nicht importiert oder ausgeführt.

Dropdowns, Variablenfelder, Bilder, Statement-Container, Mutatoren und dynamische Anschlüsse im eigenen Editor bleiben auf der Roadmap. Werteingänge sind typgeprüft; vorhandene Blocks mit ausschließlich festen Zahlenfeldern nehmen weiterhin keine dynamischen Zahlenwerte an.

Die Vorschau prüft Paket- und unterstützte HA-Strukturen, führt Jinja aber nicht aus. Geräteeigenschaften und gültige Parameterbereiche müssen in HA geprüft werden; numerische Felder bieten derzeit keine frei definierbaren Min-/Max-Grenzen. Der Editor führt keine HA-Aktionen aus. Ein YAML-Export enthält native HA-Strukturen; beim YAML-Reimport entsteht die entsprechende native Darstellung. Die ursprünglichen benutzerdefinierten Blockformen bleiben über die JSON-Projektdatei erhalten.
