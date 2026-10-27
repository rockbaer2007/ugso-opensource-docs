---
title: flex-table-card reference
description: Compact English configuration reference for the flex-table-card.
---
<a id="flex-table-card-reference"></a>
<a id="current-focus"></a>

# Reference {#referenz}

## Top level {#top-level}

| Option | Required | Description |
| --- | --- | --- |
| `type` | yes | Always `custom:flex-table-card` |
| `title` | no | Title of the card |
| `entities` | yes | Entities or filters for data source |
| `columns` | yes | Column definitions |
| `strict` | no | Hide rows without matches |
| `sort_by` | no | Sort by column, for example `state+` |
| `disable_header_sort` | no | Disable manual sorting via header |
| `max_rows` | no | Maximum visible number of lines |
| `clickable` | no | Open entity dialog on click |
| `selectable` | no | Allow text selection |
| `enable_search` | no | Show search field above table |
| `auto_format` | no | Use Home Assistant Formatting for Values |
| `display_footer` | no | Show summary row |
| `css` | no | CSS rules for this table |
| `action` | no | Action/script as data source |
| `action_data` | no | Data for the action |
| `static_data` | no | Static data within the card |

## Entities {#entities}

| Option | Required | Description |
| --- | --- | --- |
| `include` | yes | Regex or list of regex expressions for entities |
| `exclude` | no | Regex or list to exclude |

If `static_data`, `entities: []` is set.

## Columns {#columns}

| Option | Required | Description |
| --- | --- | --- |
| `name` | no | Column heading |
| `id` | no | stable column ID, important for `sort_by` |
| `data` | yes | Data selector |
| `hidden` | no | Hide column |
| `icon` | no | Icon in the header |
| `modify` | no | JavaScript expression for cell value |
| `align` | no | `left`, `center` or `right` |
| `prefix` | no | Text before cell value |
| `suffix` | no | Text after cell value |
| `no_auto_format` | no | Disable autoformatting for column |
| `multi_delimiter` | no | Separator for multiple data values |
| `fmt` | no | Built-in formatter |
| `sort_unmodified` | no | Sort with original value |
| `footer_type` | no | `sum`, `average`, `count`, `max`, `min` or `text` |
| `footer_text` | no | Text in the footer line |
| `footer_colspan` | no | Footer text across multiple columns |
| `footer_modify` | no | JavaScript for footer value |
| `tap_action` | no | Action when typing |
| `hold_action` | no | Action on Hold |
| `double_tap_action` | no | Action on double tap |
| `edit_action` | no | Edit and save from cell |

## Original reference {#originalreferenz}

The full technical reference is in the original repository:

- [Configuration Reference](https://github.com/custom-cards/flex-table-card/blob/master/docs/config-ref.md)
