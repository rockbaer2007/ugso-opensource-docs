# Entitäten

Die Entitäten werden per MQTT Discovery erstellt.

## Anrufbeantworter

Für erkannte Anrufbeantworter werden Entitäten von `AB0` bis `AB4` angelegt:

- neue Nachrichten
- alte Nachrichten
- Status
- Ein/Aus-Schalter

Der FRITZ!Box-Name des Anrufbeantworters wird als Attribut geführt, aber nicht für die Entitätsnamen verwendet.

## WLAN

Je nach FRITZ!Box werden angelegt:

- WLAN 2,4 GHz Ein/Aus
- WLAN 2,4 GHz Status
- WLAN 5 GHz Ein/Aus
- WLAN 5 GHz Status
- WLAN Gast Ein/Aus
- WLAN Gast Status

## WAN und Box-Status

- Verbindung Download
- Verbindung Upload
- Downloadrate
- Uploadrate
- WAN Link Status
- Box Mesh Rolle
- Box PPP Verbindung
- Box PPP IPv4 Extern
- Box IPv6 Extern
- Box DECT
- Box DNS over TLS

Nicht von der FRITZ!Box gelieferte optionale Werte werden ausgeblendet oder als `unknown` veröffentlicht.

## Anruflisten und Live-Anrufmonitor

Konfigurierbare Anruflisten:

- alle Anrufe
- eingehende Anrufe
- ausgehende Anrufe
- verpasste Anrufe
- abgewiesene Anrufe
- gesperrte Anrufe

Der Live-Anrufmonitor liefert Ereignisse wie `RING`, `CALL`, `CONNECT` und `DISCONNECT`.

## Telefonbücher

Telefonbücher werden mit den erkannten FRITZ!Box-Namen angezeigt. Tellows-Sperrlisten können über Namensfilter ausgeblendet oder über `phonebook_names` sinnvoll benannt werden.

## DECT

Optional werden pro erkanntem DECT-Handset veröffentlicht:

- interne Nummer
- Geräte-ID

`NoRingTime` wird bewusst nicht mehr veröffentlicht.
