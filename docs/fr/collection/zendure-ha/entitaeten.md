---
title: Entités HA pour Zendure
description: Capteurs, champs numériques, sélecteurs, interrupteurs et boutons importants de l'intégration Zendure.
---
<a id="zendure-ha-entites"></a>
<a id="orientation-actuelle"></a>

# Entités {#entitaten}

L'intégration génère des entités différentes selon l'appareil. Tous les modèles ne prennent pas en charge toutes les entités.

## Capteurs importants {#wichtige-sensoren}

| Entité / Traduction | Utilité |
| --- | --- |
| `Batterieladezustand (SoC)` | Niveau de charge de la batterie (en pourcentage) |
| `Verfügbare Energie` | Énergie disponible au-dessus du SoC (état de charge) minimal |
| `Gesamtkapazität Batterie` | Capacité de batterie détectée |
| `Solarleistung` | Puissance d'entrée solaire totale |
| `PV1` à `PV4 Solarleistung` | Puissance solaire des entrées individuelles |
| `Haus-Ausgangsleistung` | Puissance vers la maison |
| `Netz-Eingangsleistung` | Puissance du réseau vers l'appareil |
| `Batterieleistung` | Puissance de charge/décharge calculée |
| `Batterieladeleistung` | Puissance vers la batterie |
| `Batterieentladeleistung` | Puissance provenant de la batterie |
| `Verbleibende Zeit` | Temps de charge ou de décharge calculé |
| `Verbindungsstatus` | Cloud, Local, zenSDK, HEMS ou groupe de fusibles (Fuse Group) manquant |
| `BMS-Firmware` | Firmware de la batterie |
| `AC-Firmware` | Firmware AC |
| `Master-Firmware` | Firmware maître (Master) |
| `Roundtrip-Wirkungsgrad` | Rapport entre l'énergie déchargée et l'énergie chargée |

## Compteurs d'énergie {#energiezahler}

| Entité / Traduction | Objectif |
| --- | --- |
| `Gesamte Ladeenergie` | Énergie de charge cumulée |
| `Gesamte Entladeenergie` | Énergie de décharge cumulée |
| `Gesamte Hausenergie` | Énergie vers la maison |
| `Gesamte Solarenergie` | Énergie solaire produite |
| `Gesamte Netzenergie` | Énergie provenant du réseau |
| `Gesamte Off-Grid-Energie` | Énergie en mode hors réseau (Off-Grid), si pris en charge |
| `Schaltvorgänge` | Changement d'état |

## Champs numériques {#zahlenfelder}

| Entité / Traduction | Objectif |
| --- | --- |
| `AC-Eingangsgrenze` | Puissance de charge AC maximale |
| `AC-Ausgangsgrenze` | Puissance de sortie CA maximale |
| `Manuelle Leistung` | Consigne pour le mode gestionnaire manuel |
| `SoC-Minimum` | Limite inférieure de charge |
| `SoC-Zielwert` | SoC cible supérieur |

## Champs de sélection {#auswahlfelder}

| Entité / Traduction | Options / Usage |
| --- | --- |
| `AC-Betriebsmodus` | Entrée CA ou sortie CA |
| `DC Anschluss` | Entrée/Sortie ou Sortie/Entrée |
| `Hub-Modus` | Couplé ou autonome |
| `HEMS-Status` | Activé ou désactivé |
| `Auto. Batterieheizung` | Activé ou désactivé |
| `Geräte-Sicherungsgruppe` | Sélection du groupe de fusibles |
| `Verbindungsart` | Cloud, local ou zenSDK (selon l'appareil) |
| `Betriebsmodus` | Arrêt, manuel, intelligent, charge uniquement, décharge uniquement, stockage solaire |
| `Bypass-Modus` | Automatique, toujours éteint, toujours allumé |
| `Energie Export` | Désactivé, autorisé, interdit |
| `Lüftergeschwindigkeit` | Automatique, normal, rapide |

## Commutateurs et boutons {#schalter-und-buttons}

| Entité / Traduction | Usage |
| --- | --- |
| `LED` | Commande de la LED/lampe |
| `AC Anschluss` | Commande de la connexion CA |
| `Bestätigungston` | Activer/désactiver le son |
| `Bypass-Modus zurücksetzen` | Réinitialiser le bypass automatique |
| `Lüfter` | Commande du ventilateur |
| `Reset Verbindung` | Relancer la configuration de la connexion/MQTT |

## Capteurs binaires {#binarsensoren}

| Entité / Traduction | Fonction |
| --- | --- |
| `Hauptschalter` | État principal |
| `WLAN-Status` | Wi-Fi accessible |
| `Batterieheizung` | Chauffage actif |
| `Energiesparmodus` | Mode repos / économie |
| `Rückflussstatus` | Retour de courant détecté |
| `Lokale Verbindung` | Connexion locale active |
| `CT getrennt` | Capteur CT déconnecté |
| `Niedrige Temperatur` | Basse température détectée |
| `HEMS aktiv` | HEMS actif |

## Dépendance aux appareils {#gerateabhangigkeit}

Les entités sont générées en fonction de la classe de l'appareil, du firmware, du type de connexion et des données transmises via MQTT ou HTTP. L'absence d'une entité ne signifie pas nécessairement qu'il y a une erreur ; il est possible que l'appareil ou la connexion ne fournisse tout simplement pas cette valeur.
