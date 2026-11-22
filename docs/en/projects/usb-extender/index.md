---
title: USB Extender for Home Assistant
description: Connect USB keys, Stream Decks and macro pads to up to three MQTT brokers. Illustrated installation, learning, topics and practical results.
---

# USB Extender for Home Assistant

**0.1.35 · Public test release · Raspberry Pi · Updated 22 November 2026**

A USB keyboard connected to a Raspberry Pi can become a control panel for Home
Assistant or ioBroker. USB Extender reads inputs and publishes them to up to
**three MQTT brokers simultaneously**. Its configuration web interface can then
be stopped; the USB/MQTT service continues independently.

[GitHub / German and English README](https://github.com/rockbaer2007/usb-extender-home-assistant)
· [ZIP 0.1.35 and SHA256](https://github.com/rockbaer2007/usb-extender-home-assistant/releases/tag/v0.1.35)
· [Changelog](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/CHANGELOG.md)

This is a standalone Raspberry Pi program, not an HA app installed through the
app store and not official Home Assistant or Elgato software. It is **not a
USB-over-IP tunnel**: printers and cameras are not forwarded as remote USB devices.

The screenshots are supplied by the user from the real 0.1.5 setup. The interface
currently uses German labels. Click wide images to open their original size.

[![Wide key list with MQTT channel groups](/images/usb-extender/key-list.png)](/images/usb-extender/key-list.png)

## New in 0.1.35: barcode/QR scanners and HA tags {#release-035}

USB HID keyboard scanners have a separate mode, disabled by default. In
**USB / Virtuelle Geräte**, enable the device and scanner mode, choose the
**DE/US layout**, **Enter/Tab/idle-gap** completion, topic and target brokers,
then save. Example topic: `barcodescanner`. The default gap is 500 ms; incomplete
or oversized inputs are rejected. Serial scanners, arbitrary Unicode input and
GS1 control sequences are not supported.

Each complete scan publishes plain text without retain. Identical codes trigger
separate events on every scan; leading zeroes delivered by the device are retained.
Scanned links are not opened and commands are not executed. The preview shows the
last raw input. Existing key actions on this device pause in scanner mode while
their bindings remain saved.

### Where do scans appear in Home Assistant? {#scanner-ha}

Enable discovery for the HA target broker. The scanner is announced through the
native [MQTT tag integration](https://www.home-assistant.io/integrations/tag.mqtt/).
Scans appear as **`tag_scanned` events**, rather than regular sensor entities.
Under **Settings → Tags**, name the tag and create a tag automation, for example
to toggle a light. HA defines the action. USB Extender needs no HA access token.

Optionally, `https://www.home-assistant.io/tag/workshoplight` becomes the tag ID
`workshoplight`. Other text remains unchanged. ioBroker receives the text value
on the selected topic; discovery can remain disabled for its broker.

### Successful Aplic 305045 practical test {#scanner-test}

On **22 November 2026**, four real scans were performed on Raspberry Pi .112 with
0.1.35: the same barcode twice, a plain-text QR and an HA tag QR. Each scan was
handed to three brokers; HA .193 received four separate native events. ioBroker
reception on `barcodescanner` was also confirmed. Repeated codes are not suppressed.
Both USB/MQTT and web services were active at completion, with no restarts or
reported errors. No HA action was executed during this test.

[Full test and limitations](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/v0.1.35/docs/tests/scanner-live-0.1.35-20261122.md).
The backup verified before testing was no longer at its recorded path during the
final comparison; this test therefore provides no final metadata hash proof.
The agent did not change settings or pairings. Scanner discovery after restart
and disabling remains an additional practical check.

### Also included from 0.1.32–0.1.34 {#values-gamepad}

- **Logitech Touchpad T650:** eight individually enabled directional values plus X/Y, with separate
  topics and HA sensors, plain numbers 0–100. All ten live values confirmed in HA.
- **Alternative surface mode:** five vertical faders. Touch-down selects a strip
  locked until lift-off; top 100, bottom 0. Directional actions pause with their
  settings preserved. X/Y remains independent. Active faders are turquoise,
  directions gold and paused controls grey; values and the latest trigger are
  visible. Five real values confirmed in ioBroker.
- **DragonRise `0079:0006` gamepad:** left stick `ABS_X/ABS_Y`, right stick
  `ABS_RX/ABS_RZ`, each 0–100, centre 50, with individual topics and HA sensors.
  Explicitly enable output; rate 1–30/s per axis. `ABS_Z` is ignored. Learn L1/R1,
  L2/R2 and stick clicks as ordinary keys; L2/R2 are digital. Mapping measured on
  real hardware, new MQTT processing tested locally; not a universal gamepad
  profile. Additional practical checks are recorded in the roadmap.

## Previously in 0.1.31: Logitech Touchpad T650, devices and installer permissions {#release-031}

0.1.31 includes the previously local 0.1.29 and 0.1.30 changes. **Tasten & Anzeigen**
now groups devices alphabetically, initially collapsed. Only one device group and
one key are expanded at a time. Volume, display-brightness and keyboard-light keys
offer a 1–5 step filter under **Bearbeiten**: setting 3 sends steps 3, 6, 9, etc.
Release stops volume auto-repeat even when steps are skipped.

Unique serial numbers and available Logitech HID++ identifiers preserve device
identity across port changes. Without a unique identifier, explicitly assign the
new USB device to a saved offline entry; keys, pages and topics remain intact.
The confirmed trash action backs up metadata and retains shared icons. Revoke
Mobile trust separately.

### Logitech Touchpad T650: one-finger slide and X/Y {#t650}

In **USB / Virtuelle Geräte**, enable the T650 and **Touchpad-Gesten auswerten**,
then open **Ein-Finger-Slide und optionale X/Y-Werte**. Set sensitivity and rate,
save, then learn the desired directions. The Linux driver must provide type-B
multitouch; a plain click event is insufficient.

| Movement | Learnable action |
| --- | --- |
| Left / right | `TOUCHPAD_SLIDE_LEFT` / `TOUCHPAD_SLIDE_RIGHT` |
| Up / down | `TOUCHPAD_SLIDE_UP` / `TOUCHPAD_SLIDE_DOWN` |
| Upper left / upper right | `TOUCHPAD_SLIDE_UP_LEFT` / `TOUCHPAD_SLIDE_UP_RIGHT` |
| Lower left / lower right | `TOUCHPAD_SLIDE_DOWN_LEFT` / `TOUCHPAD_SLIDE_DOWN_RIGHT` |

Eight 45° sectors distinguish directions. **Sensitivity 1–10** sets the required
movement: 10 is more sensitive, 1 needs a larger movement; default 5. **Rate 1–30/s**
is an upper limit per direction-action stream and X/Y pair, default 10/s. Each
X/Y pair is two MQTT messages per target broker; additional enabled key channels
can generate further messages.

**X/Y is off by default.** Enabling it and saving creates readable topics, e.g.
`t650-touchpad/x` and `t650-touchpad/y`. Custom topics are supported; saved topics
survive renaming. Both axes use device target brokers and plain integer payloads
**0–100**, no JSON. X: left 0, right 100; Y: top 0, bottom 100. This is absolute
position on the touchpad.

A recognized slide produces no additional tap on release. Unchanged positions
are not retransmitted. One pending final pair may follow release at the next
allowed interval. Multiple fingers, a mechanical click, input loss or changed
options cancel pending values. No retain or replay to previously disconnected
brokers; X/Y remains silent during learning.

### Logitech Touchpad T650: practical test and limits {#t650-test}

Tested on 22 November 2026 using a real T650 and a 64-bit Raspberry Pi 4:

- All eight expected directions detected; **no taps** in slide phases. A separate
  tap phase produced four taps and no X/Y output.
- Three local MQTT test brokers each received **752 identical messages**, including
  200 X/Y pairs. Axis values were plain integers within 0–100.
- **Live**: sensitivity 5 and a maximum rate of 10/s; minimum interval 0.100000 s.
- **Replay of the same real recordings**: sensitivity 1/5/10 produced 33/38/39 slide
  actions during rapid movement. Rates 1/5/30 gave minimum X/Y intervals of
  1.006229 / 0.201979 / 0.037912 s. This does not replace another live test of
  Web settings or new physical movements at every value.
- Two adjacent-direction events and one hold were also recorded. No guarantee
  of exactly one exclusive direction for every hand movement, nor a general
  hardware verification of other multitouch gestures or touchpad models.
- Only the T650 was evaluated; K400/T400 were unchanged. The isolated measurement
  used temporary settings and loopback brokers, not production destinations.

[Full T650 and installation report](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/v0.1.31/docs/tests/t650-0.1.31-20261122.md).
The measurement tool was also fixed: bounded draining consumes the evdev generator;
a visible start and countdown make the capture window clear.

### Installer correction and data preservation {#installer-031}

An inherited `umask 077` could make the new Python environment inaccessible to the
service account (`Permission denied` in step 6). The installer now sets `umask 022`
for program files and `umask 077` for private backup archives. No blanket permission
change to user data is required.

The subsequent Pi installation was verified: CLI and running service report
**0.1.31**, USB/MQTT and Web are active, both with **NRestarts=0**. Mobile is active
and the error list is empty. Five SHA256 checks for `config.json`, `switches.json`,
`mobile-identity.json`, `mobile-trust.json` and `mobile-devices.json` confirm
byte-identical settings and pairings. A backup was created first. This verifies
service startup, not an additional post-installation endurance test.

## Which devices are detected? {#hardware}

**Detected** initially means that Linux can list the USB device. **Usable** also
requires a driver that reads its input and your explicit permission in the app.
Those are separate capabilities.

| Device | Implemented functionality | Verification |
| --- | --- | --- |
| USB keyboards, including Windows multimedia keyboards | Key codes, press/release, toggling switch, pressed state, click/double-click/hold | Trust/HCT keyboards used in the practical setup |
| Volume and media keys | `KEY_VOLUMEUP`, `KEY_VOLUMEDOWN`, `KEY_MUTE`; other reported playback/track keys | Volume/mute observed; test other keys per model |
| HID macro pads and USB pedals | Same processing if Linux reports ordinary key codes | Model-dependent; reports welcome |
| USB HID barcode/QR scanners | Plain-text MQTT and native HA tag discovery | Aplic 305045 repeated barcode, text QR and HA tag confirmed on hardware |
| DragonRise 0079:0006 gamepad | Four stick values 0–100 and ordinary buttons | Hardware mapping measured, new MQTT processing tested locally |
| Logitech Touchpad T650 | Eight slide directions, optional values/X/Y, alternative five vertical faders | Directions/X/Y confirmed in HA, five fader values in ioBroker; limits above |
| Physical Elgato Stream Decks | Dedicated HID driver; display/input features below | Implemented; no physical Stream Deck tested in this project yet |
| Other LCD-key devices | Keyboard input may work through HID; displays need the appropriate vendor driver | No blanket compatibility claim |
| Printers, cameras, storage, audio interfaces, serial devices and other controllers | Inventory listing; specific functionality needs separate adapters | No general print/camera/audio/MIDI/serial forwarding |
| Stream Deck Mobile / Android app | Optional experimental network server with QR pairing, images and MQTT | User confirmed pairing, icon transfer, colours and an 8×8 grid; long-term stability still open |

A listed device is not automatically enabled. Under **USB / Virtuelle Geräte**, assign a
name, select **Gerät für Eingaben freigeben**, and choose destination brokers.
Unique serial/device identifiers survive port changes. Without one, explicitly
assign the reconnected device to a saved offline entry.

[![USB inventory and explicit input permission](/images/usb-extender/devices.png)](/images/usb-extender/devices.png)

## Install on the Pi {#installation}

Recommended: Raspberry Pi 4, Raspberry Pi OS Lite **64-bit Bookworm or newer**,
Python 3.11+, systemd, sudo, and internet access for apt/PyPI. Multiple display
devices may need a separately powered USB hub. 32-bit Pi OS has not been practically verified.

Copy the ZIP to the Pi, open a terminal in its download directory, and run:

```bash
sudo apt-get update && sudo apt-get install -y unzip
unzip USB-Extender-Home-Assistant-0.1.35-Raspi4.zip
cd USB-Extender-Home-Assistant-0.1.35
sudo bash install.sh
```

The installer shows nine steps, checks dependencies and installs missing
packages. Updates back up existing data under `/var/backups/` and retain settings
and icons. The ZIP is not a fully offline system image. For later updates, extract
the new ZIP separately and run its installer.

Set a web password during initial setup; there is no installed default password.
If necessary, run `sudo usb-extender password`. Then:

```bash
sudo usb-extender web start
```

Open `http://<pi-address>:8098` in your browser and sign in. Replace screenshot
example addresses with your own brokers. Use HTTP only in a trusted local
network; otherwise put VPN/HTTPS in front. Do not expose the UI to the internet.

## Configure brokers and learn keys {#setup}

1. Under **MQTT-Broker**, enter host, port and any credentials. Enable wanted
   connections and save. Each broker has an independent connection; a key can use all three.
2. Enable discovery on HA brokers. For ioBroker select **Aus – nur MQTT-Daten senden**
   so its HA-discovery adapter does not complain about device triggers.
3. Under **USB / Virtuelle Geräte**, name and enable the device, choose its targets and save.
4. Under **Tasten & Anzeigen**, select the device and click **Anlernen starten**.
   Press and release each wanted key once. Repeated or existing keys are not duplicated.
5. Select **Anlernen beenden → Tasten übernehmen → Speichern**. New rows are now
   active. During learning, the selected device does not send MQTT actions.
6. Change channel checkboxes, topics or names per row. **Bearbeiten** opens broker
   selection, switch behaviour and timing. New extra channels on existing rows
   initially remain off; newly learned rows have all channels prepared.

[![Three broker profiles in the practical setup](/images/usb-extender/brokers.png)](/images/usb-extender/brokers.png)

[![Learning mode with the selected USB device](/images/usb-extender/learning.png)](/images/usb-extender/learning.png)

If the browser closes during learning, the input pause expires within 15 seconds
without further heartbeats. Learning drafts remain in the browser until applied
and saved. Already saved assignments remain intact.

## Topics and key functions {#topics}

Device name **Trust1** and key **F1** produce, for example, `trust1-key-f1/press`.
Names are made MQTT-safe; German umlauts such as “Büro” become `buero`. Duplicate
device names receive `-2`, `-3` etc. when needed. Saved topics remain stable after
renaming and have the same name on every selected broker. Each can be edited.

| Suffix after `trust1-key-f1` | Payload and function |
| --- | --- |
| `/press` | `press` immediately when pressed |
| `/release` | `release` when released |
| `/press-plus`, `/release-plus` | Same action, then an empty message after 50 ms on that channel |
| `/switch` | First press `ON`, next press `OFF`; release does not change it |
| `/state` | Pressed `ON`, released `OFF` |
| `/button` | `click`, `double_click` or `hold`, depending on operation |
| `/button-plus` | Same button action, then empty after 50 ms |
| `/click`, `/double-click`, `/hold` | The respective individual gesture |

The word `plus` is used because `+` is an MQTT wildcard. All eleven channels can
be enabled separately. Only plus channels are reset to empty; empty does **not**
mean physical release. Switch values persist in `switches.json` across app
restarts and are synchronized again after reconnection.

**Click/double-click/hold:** A click waits for the double-click window (default
300 ms after release). A second click within it produces only `double_click`.
Holding for 700 ms produces `hold` once, without a click on release. Holding the
second press replaces the pending click sequence with hold. Times are adjustable
per key. Native keyboard repeat is not another click or switch operation.

**Volume up/down:** Active Press/Press+ channels can repeat while held, by default
after 500 ms every 150 ms. Release stops repetition; a 30-second safety limit also
applies. Your HA automation or ioBroker logic determines the volume step. Ordinary
Press/Release channels remain immediate, independent of delayed button recognition.

Key messages use QoS 0 and no retain. Offline input is not replayed. Multiple
active channels can trigger multiple mapped automations; select the channel
appropriate for the intended single function.

## Home Assistant and ioBroker {#integration}

HA discovery groups all keys under the selected device name and one stable
device identifier. Actions are device triggers with payload filters. Switch and
pressed state are **binary sensors** showing state; controlling another device
requires an automation or mapping.

<img src="/images/usb-extender/ha-states.png" alt="HA shows Switch on and pressed state off after release" width="280">

In the user screenshot, Switch is **on** after operation, and pressed state is
**off** after release. Unknown values can occur before the first received state
message; that alone does not prove a broken input detector.

<details><summary>Before the first state messages</summary>

<img src="/images/usb-extender/ha-before.png" alt="HA states before receiving the first key values" width="280">

</details>

In ioBroker, separate states appear below the MQTT adapter when each topic is
first received. The practical screenshot shows simple values: `press`, `release`,
`click`, `hold`, `ON` and `OFF`. Plus channels show `(null)` after their empty reset
in this setup. That is expected; the state object remains. A double-click state
appears only after an appropriate message is actually sent. Old state objects
containing the former JSON event are not automatically changed. Discovery
configuration messages intentionally remain JSON.

[![Separate ioBroker data points with simple values](/images/usb-extender/iobroker-states.png)](/images/usb-extender/iobroker-states.png)

## Stream Deck and similar devices {#stream-deck}

The integrated `python-elgato-streamdeck` 0.10.0 driver includes models such as
Original/MK.2, Mini, XL, Neo, Pedal and Plus. This describes driver scope, **not
completed physical hardware testing** by this project.

- Display keys: custom icons/text, device brightness, MQTT state feedback to
  change an icon, and targeted display commands.
- Keys: Press/Release, click/double-click/hold, switch and pressed state as above.
- Dials, where present: rotation direction and presses as input.
- Touchscreen, where present: touch events; no freely designed touchscreen editor.
- Pedal and other non-display models: input, but no display-key icons.
- Up to eight independent pages per deck with navigation keys; additional profiles remain open. Animated key icons are implemented.

### Graphical editor and compact key list {#editor}

The **Stream Deck** tab stays visible offline and retains its editor and last grid.
Enable the device and save, then select a key to edit its label, icon, background
image, text position and colours. The **pressed** state supports a second icon and
separate text/background colours. Top/bottom labels reserve space beside the fitted
icon. Previewing sends no MQTT action. Save afterwards.

[![Editor with a simulated deck](/images/usb-extender/editor-022.png)](/images/usb-extender/editor-022.png)

This image is a **local browser demo**, not a hardware test.
In **Tasten & Anzeigen**, collapsed rows show **Device – Key – Name**; only one key
is expanded at a time. **Speichern** saves all pending changes; **Abbrechen** discards
changes to that key only. Indicators identify unsaved changes.
**Bearbeiten** opens advanced MQTT and timing options.

## Pages and navigation on the deck {#pages}

**USB / Virtuelle Geräte** groups USB devices and paired virtual Mobile decks.
Each phone/tablet keeps its own pages, artwork and assignments.

1. In **Stream Deck**, choose **Neue Seite** to add up to eight pages per device.
   Key numbers continue: 1–15 then 16–30 for a 15-key deck, or 1–64 then 65–128
   for 8×8. The device/Android app still supplies the grid.
2. Select a key. Under **Gestaltung → Tastenfunktion**, choose MQTT, **Vor**
   (next), **Zurück** (previous), **Home**, or **Gehe zu** (go to) with a **Zielseite**
   (target page). After **Speichern**, navigation works on the tablet without MQTT.
3. **Seitennummer anzeigen** adds a page counter. Home returns to page 1;
   next/previous stop at the boundaries. Editor navigation changes only the
   preview, not the actual page displayed on the device.
4. **Aktuelle Seite löschen** removes a page's assignments after confirmation;
   **page 1 is protected**. Save to apply. Remaining IDs/topics stay stable even
   if displayed numbers change. Go-to targets follow their pages when renumbered;
   deleting the target redirects that key to page 1.

Navigation preserves existing MQTT assignments; switching back to MQTT enables
them again. New-page topics include a stable page component, e.g.
`tablet-page-2-key-0/press`; existing page-1 topics are preserved. A service
restart opens page 1. Page changes clear held keys/pending click sequences;
feedback for another page cannot overwrite the visible page. Artwork controls,
especially colour fields, are more compact.

[![Deck pages and compact artwork, local simulation](/images/usb-extender/pages-028.png)](/images/usb-extender/pages-028.png)

## Stream Deck Mobile: optional and experimental {#mobile}

1. Enable **Mobile-Server**, enter the reachable Pi address and port (default
   **28198**) and save.
2. Choose **Kopplung starten · QR-Code** and scan using **Add computer** in Android.
3. Compare the six-digit fingerprint. Only if it matches, click **Gerät vertrauen**
   under **Mobile-Verbindungen**. Trust remains saved.
4. Open a deck in Android, enable the Mobile device in USB Extender and save.
   Assign its appearance and MQTT in the Stream Deck editor.
5. **Set rows and columns in Android.** The editor follows the reported grid up to
   8×8; there is no editor-side grid override.

The Mobile service runs independently of the web service. Pairing requires the
web interface; afterwards it may be stopped. A local WebSocket port is used,
without cloud/Bonjour discovery or changes to the app's Pro purchase entitlement.

**Mobile-Verbindungen** shows image/metadata counters, ping/pong and the last
disconnect. For unchanged **static** keys, image counters should stop increasing.
Keepalive maintains the connection without new images; animations intentionally
send frames. The user confirmed pairing, icons, colours and 8×8.
The 15-minute navigation/idle test on a real tablet documented below has passed.

### 0.1.28: successful 15-minute test {#stability}

Mobile images are sent in small batches: at most four images per loop with a
soft 25-ms work budget. Input and heartbeat handling run between batches.
An in-progress socket send can take longer; the heartbeat timeout remains
20 seconds. Disconnect logs now include Ping/Pong, the last packet type/age
and queued images, without message contents or credentials.

On **22 November 2026**, a real **SM-T580 with an 8×8 grid and two pages** was
observed for 900 seconds: repeated next/previous navigation, then about 14 minutes
idle. The user started the read-only SSH monitor; its 16 samples and final
journal were inspected directly.

| Measurement | Result |
| --- | --- |
| Interval on the Pi clock | 11:39:17–11:54:17; duration controlled by a monotonic timer |
| Tablet connection | Open and authorised in all 16 samples |
| Ping/Pong | 56/56 → 232/232; all 176 additional pings answered |
| Idle | 1,228 images / 19 metadata packets unchanged from minute 1 |
| Final journal | No new heartbeat timeout, disconnect or service restart |

One extra “connection open” entry does not identify a device; tablet counters
keep increasing without resetting. [Full readings, German report](https://github.com/rockbaer2007/usb-extender-home-assistant/blob/master/docs/tests/mobile-0.1.28-15min-20261122.md).
This interval passed. Screen-off, background operation, other networks and
physical Stream Decks were not tested here; the result does not retrospectively
prove the cause of every earlier disconnect.

## Icon library, animation and package import {#icons}

**Visual picker instead of long dropdowns:** Normal/pressed icons, backgrounds
and MQTT feedback share one picker. Expand a package, search and select an icon;
choose **Übernehmen** or double-click. **Abbrechen**/Escape preserve the previous
choice. Use **Speichern** afterwards. Only 48×48 PNG thumbnails are loaded,
using the first animation frame, with at most 96 visible tiles per package page.
The Pi generates them on demand in `icons/.cache/thumbnails/`; the Pi and
authenticated browser reuse the cache.

Identical icon IDs/content appear once per package; alternative filenames remain
searchable. Originals and stored IDs are not deleted or rewritten. Distinct
styles and black/white packages stay separate. **MDI-Favoriten hinzufügen · 40
Icons** optionally imports the bundled SteelBlue pack with 20 on/off pairs.
Nothing is installed or mapped to MQTT automatically; choose normal/pressed
icons or feedback mappings yourself.

[![Visual icon picker and thumbnail cache, local demo](/images/usb-extender/picker-028.png)](/images/usb-extender/picker-028.png)

Expand packages individually or search package names, filenames and subfolders.
Hover/focus displays a filename and preview. 48×48 thumbnails use compact 52×52
tiles; the licence appears once in the package header. Free and total storage
are shown in the page header.

[![Icon packages with preview, local browser demo](/images/usb-extender/icons-022.png)](/images/usb-extender/icons-022.png)

Import individual images, browser folders, folders on the Pi, and local ZIP,
`.streamDeckIconPack` or `.streamDeckPlugin` packages. Plugins contribute images
from supported image folders only, never executable code. Supported JSON metadata
provides the package name; otherwise the folder/archive name is used.
Original filenames and subfolders are preserved. No automatic Marketplace download;
respect usage rights.

PNG/JPEG and static SVGs are supported. GIF/WebP animate in **normal and pressed**
states, up to 120 frames and 10 frames/s. SVG animation is not played; backgrounds
remain static. Real hardware playback needs model-specific verification.

Originals: `/var/lib/ugso-usbhub/icons/IconPacks/`; index: `icons/index.json`;
derived previews: `icons/.cache/`. Package deletion first creates a backup and
blocks packages referenced by saved assignments.

**Since 0.1.22:** Save the index once at the end and generate previews/animation
data on demand. Browser folders upload as one ZIP, preserving multiple packages
and their paths. Progress uses actual server processing counts.
**Finish an active import before installing an update.**

| Single local Windows PC comparison | Before | 0.1.22 |
| --- | --- | --- |
| Itsyhome, 240 real PNGs | 4.262 s | 0.395 s |
| 6,800 synthetic PNGs | 458.323 s | 10.464 s |

Index writes: previously 240 or 6,800, now one per import.
These are PC measurements, not Pi/SD-card timings. During the previous 6,862-icon
import, the login page reappeared at 2,898 without an error message. After installing
the update, the user reports that it works again. Completion of all 6,862 icons
has not yet been confirmed.

For other similarly shaped devices, the keyboard part may already work through
HID. LCDs, touch and vendor-specific commands may require a separate adapter.
Please test and report an exact model rather than assuming full compatibility
from its appearance.

## Stop the web UI and back up {#operation}

```bash
sudo usb-extender web start
sudo usb-extender web stop
sudo usb-extender web status
sudo usb-extender web enable
sudo usb-extender web disable
sudo usb-extender backup
sudo journalctl -u ugso-usbhub -n 50
```

`web stop` closes the HTTP listener; merely closing the browser does not. The
USB/MQTT service continues. Settings, icons and switch values live under
`/var/lib/ugso-usbhub/`. The previous ten configuration versions are backed up
automatically; a full CLI backup also includes icons and switch values. Do not
upload backups publicly.

[![System commands and diagnostics](/images/usb-extender/system.png)](/images/usb-extender/system.png)

## What has been demonstrated? {#tests}

The user screenshots show 0.1.5, three broker profiles reporting online, learned
function keys, HA states and individual ioBroker data points. The event list shows
publication to HA, IOB and Testserver. That publication indication alone does not
prove receipt at every broker; the HA/ioBroker screenshots provide additional
visible evidence. This does not test every function on every device.

[![F12 events with selected topics and three MQTT targets](/images/usb-extender/events.png)](/images/usb-extender/events.png)

Version 0.1.28 passes 168 local Python tests plus JavaScript/DOM and Chrome checks
for pages, saving, mobile layout, icon selection, packages and animation. The
real 15-minute tablet test above has also passed. New/delete page, Home and Go to
have local coverage; their full hardware verification and physical Stream Deck
tests remain further checks.

## Test your hardware and send feedback {#feedback}

Do you have a Stream Deck, similar LCD-key device, macro pad or USB pedal?
Please test it and [report results on GitHub](https://github.com/rockbaer2007/usb-extender-home-assistant/issues/new?template=hardware-test.yml).
Bug reports and contributions are welcome.

Include model/revision, Pi model, OS and app version. Distinguish inventory
listing from actual key codes. Report press/release, click/double-click/hold,
icons/text, brightness, dials, touch and replug separately; explicitly mark
untested features. Start with a harmless MQTT topic without real device actions.
Inventory/event screenshots help. Do not publish passwords, tokens,
`config.json` or backup archives.
