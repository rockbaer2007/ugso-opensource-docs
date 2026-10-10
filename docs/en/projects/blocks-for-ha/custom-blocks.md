---
title: Custom blocks and template packages
---
# Custom blocks and template packages

Since **0.1.18**, **Block-/Template-Editor** beside the automation name opens a dialog occupying 95% of the viewport width and height. On phones it uses 98% with internal scrolling. Forms define the block; the right side shows a real Blockly preview, HA output with sample values and copyable package JSON. The app editor currently uses German labels.

## Create and apply

1. Enter package ID, version, name, author, licence and description, or select **Beispiel laden**.
2. Add one or several blocks: **value/Jinja**, **condition/Jinja**, **action/HA YAML** or **trigger/HA YAML**.
3. Add text, number, Boolean or entity fields and Number, String, Boolean or Value inputs.
4. Enter the Jinja expression or declarative HA mapping and review the preview.
5. **Übernehmen** installs the package locally. Blocks appear in **Benutzerdefiniert**, immediately before Search.

Enter Jinja expressions without outer template delimiters. Placeholders such as `${ENTITY}` refer to field or input names. Fields are substituted using their types; value inputs are parenthesised expressions. HA mappings use entire JSON values such as `{"$field":"ENTITY"}` or `{"$input":"VALUE"}`. [Sensor and light](./catalog/sensor-light) provides complete examples.

## Import and publication

- **Paste code:** paste package JSON into “JSON-Code oder ZIP importieren”, select **JSON prüfen**, review and **Übernehmen**.
- **Read ZIP:** select the package file, review and **Übernehmen**.

**JSON herunterladen**, **Code kopieren** and **Katalog-ZIP herunterladen** export the same package. ZIP contains `block-package.json` and `README.md`. Open-source pages explain packages and provide code/downloads. The separate [catalog](https://visualstudio.ugso-software.de/blocks) receives a dedicated block-package page. Publication requires manual review; the editor does not upload automatically. [Catalog and sample](./catalog/).

## Storage and conflicts

Package format: `ugso-ha-block-package`, `schemaVersion: 1`. IDs use lowercase letters, digits and single underscores. Installed packages persist in the current browser. Project format **3** embeds used packages and their dependencies. Formats 1 and 2 remain readable. Failed project imports do not install new definitions.

Identical packages can be imported again. Existing IDs with different content or versions are rejected. Give a fork a new package ID; automatic updates and uninstall remain future work. Dependencies must match exact versions and be installed or embedded together in a project. Cycles are rejected.

Limits: 16 installed packages, 32 blocks per package, 12 fields and 8 inputs per block; JSON up to 500,000 characters, ZIP up to 1 MB compressed and decompressed. Only the two specified ZIP entries are allowed.

## Initial editor limits

This is an original HA-oriented form editor with Blockly preview. The original [Blockly Block Factory](https://docs.blockly.com/guides/create-custom-blocks/blockly-developer-tools/) is not embedded yet. Its raw block JSON alone has no HA mapping and is not a UGSo package. JavaScript/Python/PHP/Lua/Dart generators are neither imported nor executed.

Custom-editor dropdowns, variable fields, images, statement containers, mutators and dynamic connections remain on the roadmap. Value connections are type checked; existing blocks accepting only fixed numeric fields still reject dynamic numeric values.

Preview validates the package and supported HA structures without executing Jinja. Check device capabilities and valid parameters in HA. Numeric fields currently have no configurable min/max limits. The editor executes no HA actions. YAML exports native structures; YAML reimport creates the corresponding native representation. JSON project files preserve custom block shapes.
