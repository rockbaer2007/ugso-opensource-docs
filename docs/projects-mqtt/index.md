# UGSo HA Apps

Das gemeinsame Repository ist die zentrale Veröffentlichung für alle Home-Assistant-Apps von UGSo Software: MQTT-Apps, Grafik Visual Studio, Blocks for HA und zukünftige Projekte. Jede App hat ein eigenes Unterverzeichnis, eine eigene Version und Dokumentation. Die bestehende Repository-URL bleibt erhalten.

## UGSo HA Apps und weitere Projekte

| Projekt | Dokumentation |
| --- | --- |
| <img class="package-icon" src="/images/packages/projects-dashboard-user-manager.png" width="32" height="32" alt="" aria-hidden="true"> [Dashboard-Benutzerverwaltung](/projects/dashboard-user-manager/) | 0.1.4: Benutzer als Checkbox-Spalten, Sammel-/Einzelzuordnung, automatische DE/EN/FR-Oberfläche und Dashboard-Sicherung vor dem Speichern. |
| <img class="package-icon" src="/images/packages/projects-callmebot.png" width="32" height="32" alt="" aria-hidden="true"> [CallMeBot Whatsapp](/projects/callmebot/) | Experimentelle HA-App 0.1.4: Empfängerprofile, WhatsApp-Texte über MQTT, DE/EN/FR und passende Blockly-Bausteine. |
| <img class="package-icon" src="/images/packages/projects-callmebot-signal.png" width="32" height="32" alt="" aria-hidden="true"> [CallMeBot Signal](/projects/callmebot-signal/) | Experimentelle HA-App 0.1.0: Signal-Texte, Telefon-/UUID-Profile, eigener MQTT-Namensraum und Blockly mit Profilauswahl in DE/EN/FR. |
| <img class="package-icon" src="/images/packages/projects-blocks-for-ha.png" width="32" height="32" alt="" aria-hidden="true"> [Blocks for HA](/projects/blocks-for-ha/) | Experimentelle HA-App 0.1.3: visuelle Blocks für native Automationen, YAML-Import/-Export und erweiterbare Falls-Zweige; Editor über HA-Ingress. |
| <img class="package-icon" src="/images/packages/projects-grafik-visual-studio.png" width="32" height="32" alt="" aria-hidden="true"> [Grafik Visual Studio](/projects/grafik-visual-studio/) | Grafischer Editor und Runtime für HA-Visualisierungen. |

Diese Projekte liegen im selben Repository wie die folgenden MQTT-Apps.

## Gemeinsames Add-on-Repository

Die MQTT-Projekte werden jetzt primär über ein gemeinsames Home-Assistant-Add-on-Repository bereitgestellt. In Home Assistant muss nur eine Repository-URL eingetragen werden; danach erscheinen die einzelnen Projekte separat im Add-on Store.

Repository-URL für Home Assistant:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Enthaltene Add-ons:

- FRITZ!Box to MQTT
- Heizöl to MQTT
- Parcel to MQTT (Entwicklung eingestellt)
- <img class="package-icon" src="/images/packages/projects-mqtt-client.png" width="32" height="32" alt="" aria-hidden="true"> [MQTT-Client](/projects/mqtt-client/): ausgewählte Home-Assistant-Geräte und Werte an ioBroker oder einen externen MQTT-Broker übertragen. **0.1.16** ergänzt Live-Zustandsänderungen mit Abfrage-Fallback, detaillierten Status, bestätigte Bereinigung eigener veralteter Retain-Topics, zusätzliche Steuerbefehle, JSON-Einstellungssicherung und eigene TLS-Zertifikate. Bestehende Einstellungen bleiben gültig; Retain-Daten werden nicht automatisch gelöscht. Der vorhandene HA-Broker bleibt bestehen.

- [Gemeinsames Add-on-Repository auf GitHub öffnen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons)

Die früheren Einzel-Repositories bleiben als archivierte Historie sichtbar und verweisen auf dieses gemeinsame Repository.

## <img class="package-icon" src="/images/packages/projects-fritzbox-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> FRITZ!Box to MQTT

**FRITZ!Box to MQTT**

Eine Home-Assistant-App, die FRITZ!Box-Daten per MQTT Discovery als Entitäten bereitstellt. Sie kombiniert TR-064, FRITZ!Box-Web-/Lua-Abfragen und den Live-Anrufmonitor.

- <img class="package-icon" src="/images/packages/projects-fritzbox-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [FRITZ!Box-to-MQTT-Dokumentation öffnen](/projects/fritzbox-to-mqtt/)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/fritzbox-to-mqtt)

## <img class="package-icon" src="/images/packages/projects-heizoel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> Heizöl to MQTT

**Heizöl to MQTT**

Eine Home-Assistant-App, die Heizölpreise von Esyoil und Heizöl24 per MQTT Discovery als Entitäten bereitstellt. Aktuell werden Bestpreise und bis zu sechs Anbieter-Angebote pro Quelle und Menge veröffentlicht.

- <img class="package-icon" src="/images/packages/projects-heizoel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [Heizöl-to-MQTT-Dokumentation öffnen](/projects/heizoel-to-mqtt/)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/heizoel-to-mqtt)
- Adaptiert von: [TA2k/ioBroker.heizoel](https://github.com/TA2k/ioBroker.heizoel)

## <img class="package-icon" src="/images/packages/projects-parcel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> Parcel to MQTT

**Parcel to MQTT**

**Entwicklung eingestellt:** Parcel Tracker ist bereits deutlich weiter entwickelt. Deshalb stellen wir die Weiterentwicklung unseres Pakets ein. Wir empfehlen einen Blick auf [Parcel Tracker von SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker). Unsere bisherige Dokumentation bleibt als Archiv erhalten.

Eine Home-Assistant-App, die Paketverfolgung per MQTT Discovery als Entitäten bereitstellt. Die aktuelle Version nutzt DHL-Konto-Paketlisten, optionale DHL-Sendungsnummern und Hermes-Paketverfolgung.

- <img class="package-icon" src="/images/packages/projects-parcel-to-mqtt.png" width="32" height="32" alt="" aria-hidden="true"> [Parcel-to-MQTT-Dokumentation öffnen](/projects/parcel-to-mqtt/)
- [Paket im gemeinsamen Add-on-Repository öffnen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt)
- [Archiviertes Einzel-Repository auf GitHub öffnen](https://github.com/rockbaer2007/parcel-to-mqtt)
- Adaptiert von: [TA2k/ioBroker.parcel](https://github.com/TA2k/ioBroker.parcel)

## Weitere Projektbereiche

- [C# Projekte öffnen](/projects/)
- [Diverse Projekte öffnen](/projects-diverse/)
- <img class="package-icon" src="/images/packages/projects-atlas.png" width="32" height="32" alt="" aria-hidden="true"> [ATLAS öffnen](/projects/atlas/)
