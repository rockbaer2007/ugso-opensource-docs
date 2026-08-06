# Entwicklungsstand

## Aktueller Stand

Die grundlegende Repository- und Dokumentationsstruktur ist eingerichtet.

Abgeschlossen sind unter anderem:

- Monorepo-Struktur mit `pnpm` Workspaces
- Governance- und Architektur-Dokumente
- Bereinigung der Events- und Contracts-Schicht
- öffentliche Event-Verträge
- Referenzimplementierung `DefaultEventBus`
- Heartbeat- und EventBus-Grundlagen
- Snapshot und Pre-Release-Tag für den Event-Stand

## Aktueller Sprint

Der nächste Entwicklungsschritt ist:

```text
Sprint G2.5.3 – Runtime Foundation
```

Der Schwerpunkt liegt auf dem Ausbau der Runtime-Grundlagen.

## Bereits vorbereitete Architekturentscheidungen

Zu den vorbereiteten Themen gehören:

- Kernel Contracts
- Service Container
- Dependency Injection
- Service Descriptor
- Event-Verträge
- Referenzimplementierungen

## Nächste Ziele

Geplant sind:

1. Runtime Foundation stabilisieren
2. Service-Lebenszyklen definieren
3. Dependency Injection vervollständigen
4. Diagnose- und Fehlerpfade ausbauen
5. Plugin-Verträge vorbereiten
6. Separate Plugin-Dokumentation für Erstellung, Lebenszyklus, Extension APIs, Beispiele und Veröffentlichung vorbereiten
7. Home-Assistant-Anbindung entwickeln
8. Renderer- und Theme-Schichten erweitern

## Langfristige Perspektive

Nach Abschluss der grundlegenden Runtime soll ATLAS als technische Basis für weitere UGSo-Projekte dienen.

Geplante Folgeprojekte sind:

- **Lovelace UV Card**: eine Home-Assistant-/Lovelace-Card für UV-Index, Schutzstatus, Grenzwerte und visuelle Dashboard-Ausgabe. Als Inspiration ist `filipnet/haos-uv-index` vorgemerkt: relevant sind UV-Index-Sensoren, farbcodierte Risikostufen, WHO-nahe Schutzempfehlungen, Mushroom-kompatible Darstellung und optionale Benachrichtigungs-Automationen. Die Umsetzung soll eine eigene UGSo/ATLAS-Card bleiben.

Die zuvor angedachte Thread-Card beziehungsweise der UGSo Thread Monitor wird nicht mehr als eigenes Folgeprojekt geführt. Ab Home Assistant 2026.8 stellt der Matter Server die benötigte Thread-/Matter-Übersicht bereits bereit.

::: info Hinweis
Die Roadmap kann sich während der Entwicklung ändern. Die Seite beschreibt den aktuellen Planungsstand.
:::
