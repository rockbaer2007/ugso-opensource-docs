---
title: INI Edit Translate 2026
description: Features of the Windows editor for EEP model INI files and Installation.eep with ChatGPT translation.
---

# INI Edit Translate 2026

## Version 2.1.54: railway abbreviations in Info_trans

Info_trans adds the **Railway abbreviations** tab with 14 entries:
Bf, Hbf, Hp, Gbf, Rbf, Abzw, BÜ, Stw, EG, OL, Gl., Bstg., DWW and Kr.
The table shows German, English, French and Polish, including documented foreign
abbreviations. The previously empty Kr. row is completed for a track crossing.
Clicking a cell copies its contents, as in the existing reference tables.
The table is read-only, columns can be sorted and long text wraps.
The German tab name is **Bahnabkürzung**; the French name is **Abréviations ferroviaires**.
The table is embedded in Info_trans. An existing external
`help/railway-abbreviations.csv` can still be used. This reference table
does not change automatic translation rules. Backup created before changes;
dictionary, database, settings, credentials and the external constructor list are retained.
The update ZIP uses only paths accepted by the 2.1.53 updater. Download and package
validation are separate phases; 100% is shown only after successful validation.
The dialog shows failure details and allows retrying. Both projects retain .NET
Framework 4.8 and use its out-of-process Visual Studio designer. Info_trans explicitly
references System.Configuration. Reload the solution after these changes.
Design-time compilation and WinForms DesignSurface loading were checked;
Visual Studio itself was not controlled remotely.

114 local checks passed, including table contents and DE/EN/FR layout at
100 and 150 percent scaling, without live API calls.

### User verification of 2.1.54

On 24 October 2026, the user confirmed a successful update to 2.1.54 and the visible
**Railway abbreviations** tab. Opening the Visual Studio designer was initially
confirmed as well. A subsequent report for the INI editor stated that the designer
could not be displayed because none of the classes in the file could be designed.
Designer verification is therefore open again; the successful update and tab checks
remain confirmed.

The project classification of the logic files `Form1.Update.cs` and
`Form1.Translation.cs` was subsequently corrected to “Code”. Open only `Form1.cs`
with “View Designer” for the form layout, rather than its nested logic files.
Reload the solution after updating. The build and DesignSurface checks for both
main forms passed; verification directly in Visual Studio is still pending.


## Version 2.1.53: railway abbreviations and constructor identifiers

20 railway abbreviations now use a fixed local mapping in model names and in
texts translated through the selected provider. EW means single turnout without
requiring an angle. For example, `GK3 DKW DR DB (V8)[e]EEP16.2` becomes
`GK3 TJD DR DB (V8)[e]EEP16.2` in French.

The supplied initial list contains 272 unique three-character constructor identifiers.
The first application start creates an external UTF-8 file:
`%LOCALAPPDATA%\UGSo\IET2026\constructor-codes.txt`.
Add new identifiers with two letters and one digit, one per line, then restart the app.
Updates never overwrite this user file. Additions are merged with the supplied base
list. Blank lines, comments and invalid entries are ignored. Unreadable files are
retained and the base list remains available as a fallback.
Identifiers are retained anywhere, with or without parentheses. Generic recognition
of additional identifiers remains active. DR, DB, type labels, version notes such
as `(V8)` or `(v8.2)`, EEP versions and `[e]` remain unchanged.

| DE | EN | FR | PL |
| --- | --- | --- | --- |
| DKW | DSS | TJD | Rkpd |
| EKW | SS | TJS | Rkp |
| EW | single turnout | BS | Rz |
| ABW | contrary-flexure turnout | ABW* | Rłd |
| IBW | similar-flexure turnout | IBW* | Rłj |
| BW | locomotive depot | dépôt de locomotives | lokomotywownia |
| Bf | station | gare | stacja |
| Hbf | main station | gare principale | dworzec główny |
| Hp | halt | halte ferroviaire | przystanek osobowy |
| Gbf | freight station | gare de marchandises | stacja towarowa |
| Rbf | marshalling yard | gare de triage | stacja rozrządowa |
| Abzw | junction | bifurcation | posterunek odgałęźny |
| BÜ | level crossing | passage à niveau | przejazd kolejowo-drogowy |
| Stw | signal box | poste d’aiguillage | nastawnia |
| EG | station building | bâtiment voyageurs | budynek dworca |
| OL | overhead line equipment | caténaire | sieć trakcyjna |
| Gl. | track | voie | tor |
| Bstg. | platform | quai | peron |
| DWW | three-way turnout | branchement à trois voies | rozjazd potrójny |
| Kr. | diamond crossing | traversée de voies | skrzyżowanie torów |

*French retains ABW/IBW until their equivalents have been reviewed.
Other entries use documented abbreviations or written-out translations, rather
than claiming a universal abbreviation standard.
Additional source abbreviations: DS/DSS/SS, TJD/TJS/BS, Rkpd/Rkp/Rz/Rłd/Rłj,
PO, Jn, PODG, LC, PN, BV and OLE. Ambiguous Polish ST/St is not mapped.
Hp means a passenger halt here; Kr. means a track crossing.
Technical types such as `Hp0`, `DKW190` and identifiers such as `DKW_190` are not split.

Reviewed terms are temporarily replaced with protected placeholders for online
translation and restored in the target language only after validation, including
when English is the intermediate language. Errors or changed placeholders prevent
partial application. Original files, settings and credentials are retained.
Backup created before changes. MyMemory remains the default for new configurations.

111 local checks passed, covering all 272 identifiers, DE/EN/FR/PL, import/save/reload,
version notes and failure cases, without live API calls.
The full ZIP includes `docs/railway-glossary.md` and `docs/constructor-codes.txt`.


## Version 2.1.52: descriptive words in model names

Descriptive words are now translated in model names, including when descriptions
are empty. “Haus Helios Typ4 UD1” becomes **House / Maison / Dom Helios Typ4 UD1**.

Name translation uses a limited, reviewed local word list to protect proper names.
Unknown words and name components are retained and never sent to an online service
for name translation. This is not general automatic proper-name recognition:
additional descriptive words require review. Existing names without a recognized
descriptive component are not overwritten. Type labels, constructor codes, EEP versions,
`[e]`, separators and the spelling of protected components are retained.
The railway abbreviations still being collected are not added in this change.

Descriptions still use the selected provider. Model names and descriptions are
applied together only after success; failures retain existing contents.
The provider-neutral button is now **Translate texts**.

**MyMemory/translated.net is the default for new configurations.**
Existing provider choices, API keys, accounts and models are retained.
To switch deliberately, choose **About → Settings → Translation settings → MyMemory → Save**.

105 local checks passed, covering DE/EN/FR/PL, empty descriptions, protected names and
codes, failure handling and save/reload. Backup created; original files and credentials retained.

## Version 2.1.51: folder-selection hint

Selecting a folder in the tree shows **“Please select an INI file.”** Loaded model
texts, tables, preview and selected file are retained. A directory is no longer
read as a file and no translation is started.

This applies to the root and arbitrary subfolders, including folders named with
an `.ini` extension. Missing files and other file types show the same selection hint.
Only an existing INI file is opened; uppercase `.INI` is supported too.
The selected tree node is used instead of the pointer position, including keyboard
navigation. The hint is available in German, English and French.

101 local checks passed, including retained data on folder selection in all three
languages and opening an INI without pointer hit testing. Backup created;
personal data and credentials are retained.

## Version 2.1.50: protect EEP controls, constructor codes and versions

`[e]` remains an EEP line-break control, never a translated word or an actual newline.
Exact spelling, count and order of protected markers are validated.

Constructor codes are recognized by letter/digit patterns without a fixed name list,
including `(GK3)`, `(AG3)`, `(DL1)` and legacy bare codes at the start, middle or end.
No code is added when none exists. Ordinary additions such as `(Winter)` remain
translatable. Unusual letter-only codes cannot reliably be distinguished from
ordinary words without an additional list.

Game versions such as `EEP16.2`, `eep16.2` and `EEP 16.2` retain their case and punctuation.
MyMemory never receives protected segments for translation; changed or invented codes
and controls in OpenAI/ChatGPT results are rejected. Existing rollback remains active.

A configuration entry introduced in 2.1.49 could prevent application startup.
This is fixed and covered by a test of the shipped configuration.
**If 2.1.49 does not start:** Back up `INI Edit Translate 2026.exe.config`,
download the additional configuration asset from release 2.1.50, rename it to
`INI Edit Translate 2026.exe.config` and replace the file beside the EXE.
Start the editor and install the normal 2.1.50 update. Do not replace INI files,
databases or personal settings.

99 local checks passed. An isolated installation test containing a leading code,
game version, parenthesized code and two `[e]` controls was translated through real
MyMemory calls, saved and reloaded. Original files and credentials are retained.

## Version 2.1.49: keep the last folder

Enable **Keep last folder** under **About → Settings**, then **Save**.
The last selected directory is retained across restarts and updates.
The folder tree and the model INI / Installation.eep file dialogs start there again.
No file is opened or translated automatically.

The option is disabled by default. If a saved folder or network drive is unavailable,
a message is shown and the path is retained for the next start. Existing data and
credentials are retained. 94 local checks passed, including save/reload, opt-out,
unavailable folders and DE/EN/FR layout at 100/150 percent scaling.

**Version 2.1.54.0 · Windows 11 · .NET Framework 4.8**

Edit EEP model descriptions and installation files. Developed by Uwe Grimm / UGSo
Software and published under the MIT licence.

[Source code and README on GitHub](https://github.com/rockbaer2007/ini-edit-translate-2026)

![Version 2.1.37 design with Lime menu bar and no personal data](/eep/ini-edit-translate-2026/editor-v2-1-37-en.png)

## Version 2.1.48: translate installation set titles again

Names and descriptions for all five installation sets, `Install_00` through
`Install_04`, are translated again. Only model names in the model section remain
protected. Source texts are retained; German and French still use English as the
intermediate language.

All five translation buttons and automatic import share the verified field mapping.
The second set button now edits its own fields. A set is applied only after its
complete translation; errors and cancellation retain its names and descriptions.

91 local checks passed. An isolated installation set named “Detailmodell
Großdiesellokomotive V140 001 DRG” was translated through real MyMemory calls,
saved and reloaded; model names and an extra INI field were retained. The file on
the remote gaming computer was not modified.

## Download

[Download Windows ZIP v2.1.54](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/download/v2.1.54/INI-Edit-Translate-2026-v2.1.54-windows.zip) · [GitHub release and SHA-256](https://github.com/rockbaer2007/ini-edit-translate-2026/releases/tag/v2.1.54)

Extract the complete ZIP and run `INI Edit Translate 2026.exe`. Requires Windows 11
and .NET Framework 4.8. Keep DLLs and language folders together.
Visual Studio is only needed to build from source. No installer is required.

## Features

| Area | Capabilities |
| --- | --- |
| Model texts | Edit names and descriptions in EN/DE/FR/PL |
| Metadata | Edit PDF references, generation, deployment years, country and icon |
| Movement axes and signal functions | Display, edit and translate language-specific entries |
| Installation.eep | Edit names and descriptions of supported installation sections |
| Preview | Compare the original file with the generated output preview |
| Table export | Export complete tables as tab-separated UTF-8 files with a BOM |
| Backups | Copy existing INI files before overwriting them, retaining their original filename |

## Translation providers

Select OpenAI API, ChatGPT plan or **MyMemory** under **Options → Translation settings**.
MyMemory requires internet access but no key or account. An optional email address is
sent with each request: the provider allows 5,000 characters daily anonymously, up to
50,000 with a valid email. Each target language counts separately. Long text is split
into sections up to 500 UTF-8 bytes. A temporary cache avoids repeats within one operation.

German is the default. The selected interface language sets the initial source language;
axes/signal functions retain their source selector. German and French are translated
to English first; other target languages use that English intermediate text.
This applies to all providers. The selected source text and model names are retained.

MyMemory may store submitted texts long term. The application uses only the translation
query and does not submit additional dictionary entries. There is no automatic provider
switch. Existing API keys, ChatGPT connections, models and dictionaries are retained.
INI saving retains Polish characters through Unicode; when necessary, the backed-up
output is saved as UTF-16 with BOM. Actual EEP processing of this encoding was not tested.

90 local checks passed. The supplied sample INI was imported, translated through real
MyMemory calls and saved as a copy; the original remains unchanged. Review machine
translations of technical terminology before use.

[MyMemory API](https://mymemory.translated.net/doc/spec.php) ·
[Usage limits](https://mymemory.translated.net/doc/usagelimits.php) ·
[Data usage](https://mymemory.translated.net/terms-and-conditions)

## Setup and workflow

1. Download the Windows ZIP above and extract all files.
2. Start `INI Edit Translate 2026.exe` from the extracted directory, keeping its DLLs and language directories together.
3. Open **About → Settings → Translation settings**. Select MyMemory, OpenAI API or ChatGPT plan. MyMemory needs no login; email is optional.
4. Open a backed-up file in **Read only** mode first.
5. Use **Read and translate** or a translation button. Select the source language for axes and signal functions.
6. Review the preview and model texts, then save explicitly.

The information dialog selects the reviewed `Info.de.rtf`, `Info.en.rtf` or `Info.fr.rtf` to match the interface language. The historical `Info.rtf` is retained unchanged. Current help describes OpenAI translation and the restored reference program.

## GitHub updates

Choose **About → Check for updates** to query the latest public GitHub release.
There is no automatic startup check. Only a newer stable version is offered,
with its version number and release notes.

**Download and install** downloads the Windows ZIP and SHA-256 checksum.
Download and package validation can be cancelled and finish before the application closes.
Save open files and close Info_trans before installation. Installation requires confirmation.
A separate helper waits for the editor to exit, backs up existing files and installs the package.

Settings and the encrypted OpenAI key are retained. Existing reference-help FDB, CSV,
DAT and configuration files, plus the original Info.rtf, are backed up and not replaced.
Your model files are left intact. On installation failure, the updater attempts to restore
files already replaced and records the result. Backups and reports are stored under
`%LOCALAPPDATA%/UGSo/IET2026/updates/<identifier>/`.

No server credentials are needed. Checksums verify integrity; no additional digital
package signature is implemented. 36 isolated update checks cover downloads,
cancellation, package paths, retained data, locked files and rollback after partial writes.

### Updater fix in 2.1.48

Process handoff now uses a stable Windows process handle instead of reading
modules from an editor that is already closing. Four additional checks cover
x86/x64, exited processes, identity mismatches and timeouts. If the old 2.1.37
helper fails before installation, extract the complete 2.1.48 ZIP into a new
folder first. Back up your data and do not replace existing databases or
dictionaries with package files.

The complete update from published 2.1.37 to 2.1.48 passed in a backed-up test
copy: GitHub download, installation and automatic restart. All 32 previous
setting values, 17 checked data/model files and 18 existing user configurations
were preserved. A synthetic DPAPI test key remained unchanged and decryptable;
the original state without a key was restored afterwards. No OpenAI request was
made. Restart was confirmed through process ID, versions, hashes and configuration;
Windows window capture failed afterwards. A fresh read-only GitHub dialog test
correctly detected 2.1.48.

## Second program: Info_trans

The package also includes `help/Info_trans.exe`. **Reference help** in the main
editor opens it in the selected language. The actual `IET2.FDB` and its native
Firebird 2.5.8 runtime were restored from the 2019 archive.
No separate Firebird server installation is required.

The database contains 5 building entries, 2 goods entries and 2 update entries.
Signals, rolling stock, track objects and landscape tables are empty in the
original. Also included: 236 icon entries, 369 technical terms and 2,428 reviewed
entries in the **DE/EN/FR dictionary**. English is the reference; confirmed German
corrections and French translations are included. Continuation rows were merged
and mixed terms were separated. American and British terminology retains its
original labels. All dictionary review questions are resolved. The original DE/EN
file and source database remain unchanged in the complete package.

![Info_trans 2.1.37 with Lime tabs and the loaded original database](/eep/ini-edit-translate-2026/info-trans-v2-1-37-en.png)

![Three-language Info_trans dictionary with readable German, English and French columns](/eep/ini-edit-translate-2026/dictionary-v2-1-37-en.png)

`Info_trans` is built for x86 to match the native DLLs. The managed provider
FirebirdSql.Data.FirebirdClient 7.5.0.0 was verified with the real Firebird 2.5.8
database. Tests read separate database copies and compare all seven tables with
the DE/EN/FR interface. Packaging includes the unchanged source database.

Missing or unloadable components are reported and SQL import is then disabled.
A local database backup precedes an available manual SQL import.
Automatic application updates remain disabled.

## Data and privacy

Old registrations and personal databases are not imported. Settings are stored
separately for each Windows user. OpenAI configuration and file backups are under
`%LOCALAPPDATA%/UGSo/IET2026/`.

Windows DPAPI encrypts the API key for the current Windows account. Selected texts
are sent to OpenAI with `store: false`. Internet access and separate API billing are
required; a ChatGPT subscription does not replace API billing.

## Updates and verification

**GitHub updates are started manually and require installation confirmation.** The old update server is not used. Google, LEO, Linguee and DeepL are no longer offered.

41 local checks with mocked API responses and Debug/Release builds cover failures,
cancellation, restoration, export and rendered DE/EN/FR interfaces. Tests do not send
texts to OpenAI. A live API request and generated translation quality still need
verification with your own account. Not every possible INI schema is supported;
review the resulting model data before use.

The user reviewed the complete local 2.1.37 release and confirmed it works before
publication. The ZIP includes both programs, the native Firebird runtime, original
database and corrected dictionary. ZIP integrity and SHA-256 were verified; all
seven database tables were compared with the DE/EN/FR interface using separate
copies. Screenshots show the current design with neutral data and no private settings.
