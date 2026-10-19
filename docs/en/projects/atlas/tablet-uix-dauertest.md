# UIX tablet soak: 720 Cards

As of 19 October 2026. **User confirms 60 minutes on each host, .177 and .68,
with working theme changes and reconnection.**
App 0.1.327, HA 2026.10.2, UIX 8.4.0; Card-Mod is not loaded.
User-reported device: Samsung Galaxy Tab A6, Android 11 / LineageOS,
Chrome Mobile 155.

Fresh full backups and existing-data captures precede setup. Owned dashboards
are sidebar-visible without Admin-only; existing Editors, projects, plugins and
settings are preserved.

This is user-reported functional qualification. No separately collected tablet
JSON logs, FPS/memory measurements or detailed rotation/scrolling results are
supplied. Desktop preflight and local simulation remain separate.

## Historical procedure

Run a complete 60 minutes per host, sequentially:

Owned views at `/atlas-tablet-uix-soak-20261019/720` are removed after completion
and are no longer active test links. Prepare new backups and owned views before
any future repeat.

1. Connect power, keep the screen awake and close other Apps as in the earlier
   test. Keep only the current test page in the foreground. Sign in yourself
   with the existing HA account; do not share credentials.
2. Check “HA verbunden”, then press **60 Minuten starten** once. Verify the
   timer advances; do not reload or leave the dashboard view.
3. Every ten minutes alternate portrait/landscape and scroll down/back. Look
   for stalls, overlaps, clipped text and error Cards. Mushroom text/icon/color
   change with the synthetic state.
4. The helper toggles 18/28 approximately every ten seconds, light/dark at
   minutes 10/20/30/40/50 and reconnects at 15/30/45. Brief disconnection is
   expected, followed by “HA verbunden”. Do not reload.
5. At **60 Minuten beendet**, record the result. **Ergebnis markieren** selects
   the local JSON for normal copying. If awkward on the tablet, first report
   host, final time, reconnection count and observed errors.
6. Repeat on the second host. If stalled or persistently disconnected, use
   **Stoppen / Theme zurück** and report how long it ran.

Only owned synthetic states change; no real device is controlled. Timer gaps
and HA request times do not measure FPS/rendering latency. Report screen sleep
or background pauses as interruptions. Finish/Stop restores the original theme.
Reload does not automatically resume the run.

## Completion

Owned dashboards, resources, synthetic states and temporary UIX are removed;
WWW files are in recoverable File Studio Trash. All seven projects and six plugins
per host, 551 captured existing files on .177 and nine on .68, original settings
and old trash entries are unchanged. Three full backups remain per host. PC
backups and installed updates are preserved. Never load Card-Mod and UIX together.
