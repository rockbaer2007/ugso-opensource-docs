<script setup>
import LogicStudioFeedback from '../../../.vitepress/theme/LogicStudioFeedback.vue'

const labels = {"subject":"Betreff","version":"App-Version","editor":"Editor","message":"Nachricht","reply":"E-Mail für Rückfragen (optional)","open":"E-Mail-Entwurf öffnen","directIntro":"Das Formular sendet deine Meldung direkt per E-Mail. Deine Antwortadresse ist freiwillig.","draftIntro":"Das Formular öffnet einen Entwurf im E-Mail-Programm. Dort kannst du deine Meldung prüfen und absenden.","send":"Meldung senden","sent":"Deine Meldung wurde gesendet.","failed":"Der Versand ist fehlgeschlagen. Deine Eingaben bleiben erhalten."}
</script>

# Fehler melden und mitarbeiten

## Öffentlich auf GitHub melden

Erstelle ein Issue im Sammelrepo, damit andere den Fehler finden und ihre Erfahrungen ergänzen können. [GitHub-Issue erstellen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues/new)

## Privat per E-Mail melden

Nenne die App-Version, den betroffenen Editor, die Schritte zum Nachstellen, das erwartete und das tatsächliche Ergebnis. Entferne Zugangsdaten und persönliche Informationen aus Screenshots und Protokollen.

<LogicStudioFeedback :labels="labels" />

## Mitmachen

Du kannst neue Versionen testen, Beispiele beisteuern oder bei Anleitung, Übersetzungen und Code helfen. Melde dich mit deiner Idee über einen der beiden Wege.
