---
title: Zendure HA entities
description: Important sensors, numbers, selection fields, switches and buttons of the Zendure integration.
---
<a id="zendure-ha-entities"></a>
<a id="current-focus"></a>

# Entities {#entitaten}

The integration creates different entities depending on the device. Not every model supports every entity.

## Important sensors {#wichtige-sensoren}

| Entity/Translation | Purpose |
| --- | --- |
| `Batterieladezustand (SoC)` | Battery charge level in percent |
| `Verfügbare Energie` | available energy above the minimum SoC |
| `Gesamtkapazität Batterie` | detected battery capacity |
| `Solarleistung` | total solar input power |
| `PV1` to `PV4 Solarleistung` | Solar power of individual inputs |
| `Haus-Ausgangsleistung` | Performance towards home |
| `Netz-Eingangsleistung` | Power from the network into the device |
| `Batterieleistung` | calculated charging/discharging power |
| `Batterieladeleistung` | Power into the battery |
| `Batterieentladeleistung` | Power from the battery |
| `Verbleibende Zeit` | calculated charging or discharging time |
| `Verbindungsstatus` | Cloud, Local, zenSDK, HEMS or missing Fuse Group |
| `BMS-Firmware` | Battery firmware |
| `AC-Firmware` | AC firmware |
| `Master-Firmware` | Master Firmware |
| `Roundtrip-Wirkungsgrad` | Ratio of discharged to charged energy |

## Energy meter {#energiezahler}

| Entity/Translation | Purpose |
| --- | --- |
| `Gesamte Ladeenergie` | accumulated charging energy |
| `Gesamte Entladeenergie` | accumulated discharge energy |
| `Gesamte Hausenergie` | Energy towards home |
| `Gesamte Solarenergie` | solar energy generated |
| `Gesamte Netzenergie` | Energy from the grid |
| `Gesamte Off-Grid-Energie` | Off-grid energy if supported |
| `Schaltvorgänge` | Switch between states |

## Number fields {#zahlenfelder}

| Entity/Translation | Purpose |
| --- | --- |
| `AC-Eingangsgrenze` | maximum AC charging power |
| `AC-Ausgangsgrenze` | maximum AC output power |
| `Manuelle Leistung` | Manual Manager Mode Setpoint |
| `SoC-Minimum` | lower loading limit |
| `SoC-Zielwert` | upper target SoC |

## Selection fields {#auswahlfelder}

| Entity/Translation | Options / Purpose |
| --- | --- |
| `AC-Betriebsmodus` | AC input or AC output |
| `DC Anschluss` | On/Output or Off/Input |
| `Hub-Modus` | coupled or standalone |
| `HEMS-Status` | active or deactivated |
| `Auto. Batterieheizung` | active or deactivated |
| `Geräte-Sicherungsgruppe` | Fuse Group Selection |
| `Verbindungsart` | Cloud, local or depending on the device zenSDK |
| `Betriebsmodus` | Off, manual, smart, charge only, discharge only, solar save |
| `Bypass-Modus` | automatic, always off, always on |
| `Energie Export` | disabled, allowed, forbidden |
| `Lüftergeschwindigkeit` | automatic, normal, fast |

## Switches and buttons {#schalter-und-buttons}

| Entity/Translation | Purpose |
| --- | --- |
| `LED` | Switch LED/lamp |
| `AC Anschluss` | Switch AC connection |
| `Bestätigungston` | Enable/disable sound |
| `Bypass-Modus zurücksetzen` | reset automatic bypass |
| `Lüfter` | Switch fan |
| `Reset Verbindung` | Initiate MQTT/connection changeover again |

## Binary sensors {#binarsensoren}

| Entity/Translation | Purpose |
| --- | --- |
| `Hauptschalter` | Main status |
| `WLAN-Status` | Wi-Fi accessible |
| `Batterieheizung` | Heating active |
| `Energiesparmodus` | Rest/Saving Mode |
| `Rückflussstatus` | Backflow detected |
| `Lokale Verbindung` | local connection active |
| `CT getrennt` | CT sensor separated |
| `Niedrige Temperatur` | low temperature detected |
| `HEMS aktiv` | HEMS active |

## Device dependency {#gerateabhangigkeit}

The entities are constructed from device class, firmware, connection type and reported MQTT/HTTP data. If an entity is missing, it is not automatically an error; the device or connection may not provide the value.
