# Karten debuggen

Die DOM-Navigation wirkt am Anfang schnell etwas sperrig. Nach ein paar Durchlaeufen wird aber klar, welche Schritte UIX intern geht.

Du kannst den Element-Inspektor deines Browsers nutzen, um die UIX-Kette sichtbar zu machen:

- Oeffne den Element-Inspektor und suche das Basiselement, zum Beispiel `#shadow-root`, die Karte in `<hui-card>` oder ein `<ha-card>` innerhalb einer Custom Card. Mehr dazu steht unter [Konzepte - Anwendung](../concepts/application).
- In diesem Bereich sollte ein `<uix-node>` liegen, auch wenn du keinen Style angegeben hast.
- Waehle das `<uix-node>`-Element aus.
- Oeffne die Browser-Konsole. In Chrome kannst du mit `Esc` Konsole und Inspektor gleichzeitig anzeigen.
- Gib `$0.uix_input` ein und bestaetige mit Enter. Das ist die Styling-Information, die dieser Schritt der Kette erhalten hat. Ist es ein String, bist du am Ende der Kette. Ist es ein Objekt, kannst du den naechsten Schritt untersuchen.
- Gib `$0.uix_children` ein und bestaetige mit Enter. Das ist die Menge der `<uix-node>`-Elemente im naechsten Schritt einer Kette. Wenn du im `value:` eines Eintrags auf `uix` klickst, springt der Inspektor zu diesem `<uix-node>` und du kannst weiter pruefen.
- Mit `$0.uix_parent` findest du das Eltern-`<uix-node>` eines Knotens in der Kette.

Fuer etwas mehr Diagnoseausgabe kannst du in der problematischen Karte Debug aktivieren:

```yaml
uix:
  debug: true
```

## Debug ueber Theme-Variablen setzen

Wie bei einer Karte mit `uix:` und `debug: true` kannst du Debug auch ueber Theme-Variablen aktivieren. Das kann der einzige Weg sein, wenn du einen bestimmten Typ oder eine Klasse in einem Panel stylst, das kein Lovelace-Dashboard oder kein Lovelace-Strategy-Dashboard ist.

Debug kann so gesetzt werden:

1. Mit der Theme-Variable `uix-<type>-debug: true`, definiert in deiner Theme-YAML-Datei ohne fuehrendes `--`. Damit debugst du alle Elemente vom Typ `<type>`. In CSS wird diese Variable als `--uix-<type>-debug` referenziert.
2. Mit der Theme-Variable `uix-<type>-<class>-debug: true`, ebenfalls ohne fuehrendes `--` in YAML. Damit debugst du alle Elemente vom Typ `<type>`, die die Klasse `<class>` besitzen. In CSS wird sie als `--uix-<type>-<class>-debug` referenziert. Dazu gehoeren Klassen, die UIX setzt, und Klassen, die du selbst in der UIX-Konfiguration einer Karte oder eines Elements angegeben hast.

Beispiel:

```yaml
my-awesome-theme:
  uix-theme: my-awesome-theme

  uix-card-debug: true # Debug fuer alle Elemente vom UIX-Typ `card`
```

```yaml
my-awesome-theme:
  uix-theme: my-awesome-theme

  uix-card-type-energy-sankey-debug: true # Debug fuer eine Karte mit UIX-Klasse `type-energy-sankey`
  uix-badge-my-class-debug: true # Debug fuer Badges mit der Klasse `my-class`
```

::: warning Theme-Variablen im Home-Assistant-Theme setzen
Theme-Debug-Variablen werden aus dem Home-Assistant-Theme gelesen, das gerade im Kontext ist. Das kann global sein oder lokal ueber eine Dashboard-Ansicht beziehungsweise Karte angewendet werden.

Theme-Debug-Variablen werden nicht aus dem `uix-theme`-Theme gelesen. Wenn diese Themes verschieden sind, setze die Debug-Variablen also im aktiven Home-Assistant-Theme.

```yaml
theme-mods:
  # UIX Theme-Variablen, Styles und Makros stehen hier.

my-awesome-theme:
  uix-card-type-energy-sankey-debug: true
  uix-badge-my-class-debug: true

  uix-theme: theme-mods
```
:::
