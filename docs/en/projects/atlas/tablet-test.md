# Tablet test: start small

As of 19 October 2026, App 0.1.327 and HA 2026.10.2. **Prepared, not a passed
tablet qualification.** Desktop checks do not establish tablet performance.
Only `192.168.178.177` and `192.168.178.68` are authorized test hosts.

## Browser check first

For an older Galaxy Tab A already struggling with ordinary dashboards, do not
start a large load test. Preserve its existing Stream Deck setup. In a separate
browser tab open the owned temporary check:

- [.177 browser check](http://192.168.178.177/local/atlas-tablet-20261019/index.html)
- [.68 browser check](http://192.168.178.68/local/atlas-tablet-20261019/index.html)

These lightweight pages load neither HA nor large Cards. They show browser
features and identification, with no telemetry or settings changes. Available
features do not prove complete HA compatibility or adequate performance. Device
age, Android version and browser version are different; exact versions of this
tablet are still unconfirmed. Stop if a feature is missing or the page is slow.
Do not clear browser data, disable security checks or replace the Stream Deck setup.

The first test dashboards were created admin-only and hidden from the sidebar.
The user has enabled their sidebar entries for tablet access. Future owned test
dashboards should be created without Admin-only and shown in the sidebar.

## Small entry test

Only when the check is responsive, choose “Kleinen HA-Einstieg öffnen”. These
separate initial dashboards retain their original admin restriction unless changed.
Sign in yourself
with an existing HA account if needed; do not share credentials or tokens.

1. **Start:** choose “Testzustand 18”; check “HA verbunden”.
2. **12 Karten:** try portrait/landscape, scroll to the bottom and back; look for
   overlapping text, clipped buttons and delayed input.
3. Choose “Testzustand 28”, “Hell”, “Dunkel”; wait for transitions, then use
   “Theme zurück”. The captured baseline is the default theme in automatic mode.
4. Choose “Wiederverbindung testen” once without reload. Expect “HA verbunden”,
   an increased reconnection count and “alter Socket geschlossen”. Try state 18 again.

Stop when interaction stalls. For Stream Deck use, the small stage is more
relevant than forcing a large project onto this device.

## Optional large stages

Only after a responsive small stage, select **360 Karten**, then **720 Karten**.
Repeat rotation, scrolling, states 18/28, light/dark and one reconnect. Mushroom
changes Kühl/Warm, snowflake/fire and blue/red. Only an owned synthetic entity
changes; no real device is controlled. This preparation uses **Card-Mod 4.2.1
alone**, without UIX. It does not qualify UIX on a tablet.

## Report and cleanup

Report host/stage, portrait/landscape, scrolling, themes, reconnection and whether
input was responsive, delayed or blocked. Do not extrapolate to untested stages.
Android/browser versions help; an old-browser stall alone does not identify its
cause or establish an ATLAS defect.

Fresh full backups and existing-data captures precede setup; existing Editors
are not modified. Owned test views stay until the tablet report. Afterwards
remove owned states/resources/dashboards and move WWW files to File Studio Trash.
Retain the newest three successful full backups per host; preserve PC backups.
