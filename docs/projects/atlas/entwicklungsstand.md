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
6. Home-Assistant-Anbindung entwickeln
7. Renderer- und Theme-Schichten erweitern

## Langfristige Perspektive

Nach Abschluss der grundlegenden Runtime soll ATLAS als technische Basis für weitere UGSo-Projekte dienen.

Geplante Folgeprojekte sind:

- **UGSo Thread Monitor**: Darstellung von ESPHome-Thread-Geräten, Rollen, IPv6-Adressen, Statuswerten und Diagnosedaten als ATLAS-basiertes Plugin.
- **Lovelace UV Card**: eine Home-Assistant-/Lovelace-Card für UV-Index, Schutzstatus, Grenzwerte und visuelle Dashboard-Ausgabe.

::: info Hinweis
Die Roadmap kann sich während der Entwicklung ändern. Die Seite beschreibt den aktuellen Planungsstand.
:::
