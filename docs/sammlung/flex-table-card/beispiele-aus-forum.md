---
title: Beispiele aus Forum
description: Externe flex-table-card Beispiele aus dem Home-Assistant-Community-Forum mit Bild und passendem Code.
---
# Beispiele aus Forum

Diese Beispiele stammen aus dem Home-Assistant-Community-Beitrag [Styling the card](https://community.home-assistant.io/t/flex-table-card/461173/2) von Ildar_Gabdullin. Die Bilder werden direkt aus dem Forum geladen; der Code ist dem jeweiligen Beispiel zugeordnet.

::: warning Externe Beispiele
Die Beispiele sind Forumsausschnitte und können je nach Home-Assistant-Version, `flex-table-card`-Version oder zusätzlich genutzten Karten wie `auto-entities` und `card_mod` angepasst werden müssen.
:::

## 1. Zero padding und farbiger Tabellenrahmen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/5/5/5/555034367a69f96f1a04b9a2770a41a966cc8742.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/5/5/5/555034367a69f96f1a04b9a2770a41a966cc8742.png" alt="1. Zero padding und farbiger Tabellenrahmen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 5<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_column<br>          name: brightness<br>          data: brightness<br>        - *ref_column<br>      strict: true<br>      css:<br>        table+: &gt;-<br>          border: 1px solid cyan;<br>          padding: 0px;</code> |

## 2. Keine internen Rahmen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/7/e/c/7ece648bf57e6dd08c7c7d2b5a0ddf7281dffcb5.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/7/e/c/7ece648bf57e6dd08c7c7d2b5a0ddf7281dffcb5.png" alt="2. Keine internen Rahmen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: vertical-stack<br>cards:<br>  - type: markdown<br>    content: &#124;<br>      no borders<br>    style: &#124;<br>      ha-card {<br>        color: red;<br>      }<br>  - type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 5<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_column<br>          name: hhh<br>          data: brightness<br>          align: center<br>        - *ref_column<br>        - *ref_column<br>      strict: true<br>      css:<br>        table+: &#x27;border-collapse: collapse;&#x27;</code> |

## 3. Eigene interne Rahmen: Header und Zellen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/d/1/4/d14973d5fae21ebdea537258d44e167656d1cbce.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/d/1/4/d14973d5fae21ebdea537258d44e167656d1cbce.png" alt="3. Eigene interne Rahmen: Header und Zellen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: center<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    table+: &#x27;border-collapse: collapse;&#x27;<br>    th+: &amp;ref_border_style &#x27;border: 1px solid red;&#x27;<br>    td+: *ref_border_style</code> |

## 4. Eigene interne Rahmen: nur Tabellenzellen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/0/2/3/023cd9693fb4b79b30a93602d8d7117c11098447.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/0/2/3/023cd9693fb4b79b30a93602d8d7117c11098447.png" alt="4. Eigene interne Rahmen: nur Tabellenzellen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: center<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    table+: &#x27;border-collapse: collapse;&#x27;<br>    td+: &#x27;border: 1px solid red;&#x27;</code> |

## 5. Eigene interne Rahmen: Zeilenoberkante

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/e/d/5/ed5ecb0939e52dae4d0ec48c92ea4208130d5556.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/e/d/5/ed5ecb0939e52dae4d0ec48c92ea4208130d5556.png" alt="5. Eigene interne Rahmen: Zeilenoberkante" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: center<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    table+: &#x27;border-collapse: collapse;&#x27;<br>    tbody tr+: &#x27;border-top: 1px solid red;&#x27;</code> |

## 6. Eigene interne Rahmen: Spaltentrenner

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/d/a/0/da069db4c7e2f6434d148c9640bf071c7d55d6a8.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/d/a/0/da069db4c7e2f6434d148c9640bf071c7d55d6a8.png" alt="6. Eigene interne Rahmen: Spaltentrenner" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: center<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    table+: &#x27;border-collapse: collapse;&#x27;<br>    th:nth-of-type(n+2)+: &amp;ref_border_style &#x27;border-left: 1px solid red;&#x27;<br>    td:nth-of-type(n+2)+: *ref_border_style</code> |

## 7. Padding per card_mod wiederherstellen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/8/4/4/84408ca1c455bc4c75426131486b1071fa4d21c4.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/8/4/4/84408ca1c455bc4c75426131486b1071fa4d21c4.png" alt="7. Padding per card_mod wiederherstellen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">card_mod:<br>    style: &#124;<br>      div {<br>        padding: 16px;<br>      }</code> |

## 8. Horizontaler Scrollbalken

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/2/f/8/2f850040b806729675cdf30b681c5a198809b65a.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/2/f/8/2f850040b806729675cdf30b681c5a198809b65a.png" alt="8. Horizontaler Scrollbalken" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 5<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_column<br>          name: brightness<br>          data: brightness<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>      strict: true<br>      css:<br>        table+: &#x27;padding: 0px&#x27;<br>      card_mod:<br>        style: &#124;<br>          ha-card {<br>            overflow: auto;<br>          }</code> |

## 9. Horizontaler und vertikaler Scrollbalken

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/8/0/a/80acb18413c3a782df4c13c4c9ee2621fa846c20.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/8/0/a/80acb18413c3a782df4c13c4c9ee2621fa846c20.png" alt="9. Horizontaler und vertikaler Scrollbalken" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 13<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_column<br>          name: brightness<br>          data: brightness<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>      strict: true<br>      css:<br>        table+: &#x27;padding: 0px&#x27;<br>      card_mod:<br>        style: &#124;<br>          ha-card {<br>            overflow: auto;<br>            max-height: 200px;<br>          }</code> |

## 10. Header: verschiedene Styles

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/9/7/f/97fb8976b3aa9ffe30655a8a270a8bd54d741122.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/9/7/f/97fb8976b3aa9ffe30655a8a270a8bd54d741122.png" alt="10. Header: verschiedene Styles" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 2<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: right<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    thead th: &gt;-<br>      background-color: magenta;<br>      text-align: left !important;<br>      font-weight: 300;<br>      border: 1px solid;<br>    thead th:first-child: &gt;-<br>      text-align: center !important;<br>      color: cyan;<br>    thead th:nth-child(2): &gt;-<br>      background-color: lightgreen;<br>    thead th:nth-child(4): &gt;-<br>      background-color: rgba(0,0,255,0.2);<br>    thead th:nth-child(5): &gt;-<br>      background-color: rgb(255,255,255);<br>      color: red;<br>      border-color: cyan;<br>    thead th:last-child: &gt;-<br>      background-color: yellow;<br>      color: orange;<br>      text-align: right !important;</code> |

## 11. Header ausblenden

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/8/7/9/8790eb33443dc7771f66c9e1746ccd5c8c3f85a5.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/8/7/9/8790eb33443dc7771f66c9e1746ccd5c8c3f85a5.png" alt="11. Header ausblenden" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 2<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    thead th: &#x27;display: none;&#x27;</code> |

## 12. Header teilweise ausblenden

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/4/c/8/4c8948aeeb8cc67b1365c238bd190de0f4d273cb.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/4/c/8/4c8948aeeb8cc67b1365c238bd190de0f4d273cb.png" alt="12. Header teilweise ausblenden" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 2<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    thead th: &#x27;color: transparent;&#x27;<br>    thead th:first-child: &gt;-<br>      color: unset;<br>      background-color: lightgreen;<br>    thead th:last-child: &gt;-<br>      color: unset;<br>      background-color: yellow;</code> |

## 13. Header optisch zusammenfassen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/1/c/1/1c17a96bca23ff7850dcbf5c70b1a1da5a6cb740.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/1/c/1/1c17a96bca23ff7850dcbf5c70b1a1da5a6cb740.png" alt="13. Header optisch zusammenfassen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: right<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    table+: &#x27;border-collapse: collapse;&#x27;<br>    th+: &gt;-<br>      border-bottom: 1px solid rgb(127,127,127);<br>      text-align: left !important;<br>    th:nth-of-type(n+2)+: &amp;ref_style_border &gt;-<br>      border-left: 1px solid rgb(127,127,127)<br>    td:nth-of-type(n+2)+: *ref_style_border<br>    th:nth-of-type(2)+: &amp;ref_style_merged_header &gt;-<br>      border-left: none;<br>      color: transparent;<br>    th:nth-of-type(5)+: *ref_style_merged_header<br>  card_mod:<br>    style: &#124;<br>      div {<br>        padding: 16px;<br>      }</code> |

## 14. Zeilen: gleiche Hintergrundfarbe

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/c/5/d/c5dbd2d971c3f325d9e8b40c9ef03da3b328ce4b.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/c/5/d/c5dbd2d971c3f325d9e8b40c9ef03da3b328ce4b.png" alt="14. Zeilen: gleiche Hintergrundfarbe" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: right<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    tbody tr+: &gt;-<br>      background-color: rgba(0,255,0,0.4) !important;</code> |

## 15. Zeilen: abwechselnde und einzelne Styles

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/3/9/a/39abb7a23bbcc2ccb66817bc2534937492b4d126.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/3/9/a/39abb7a23bbcc2ccb66817bc2534937492b4d126.png" alt="15. Zeilen: abwechselnde und einzelne Styles" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 7<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: right<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    tbody tr+: &#x27;color: red&#x27;<br>    tbody tr:nth-child(odd)+: &#x27;background-color: rgba(0,255,0,0.4);&#x27;<br>    tbody tr:nth-child(even)+: &#x27;background-color: rgba(255,255,0,0.4);&#x27;<br>    tbody tr:nth-child(4)+: &gt;-<br>      background-color: orange;<br>      color: blue;</code> |

## 16. Zeilen: Hover-Styling

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/0/f/3/0f385e56c8f5e426530f67373ceb8c4c96e503ab.gif" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/0/f/3/0f385e56c8f5e426530f67373ceb8c4c96e503ab.gif" alt="16. Zeilen: Hover-Styling" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 5<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  card_mod:<br>    style: &#124;<br>      tbody tr:hover {<br>        background-color: coral !important;<br>      }</code> |

## 17. Spalten: verschiedene Styles

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/8/b/2/8b2a34e278acd5bcb609f2a723f545cedd660e03.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/8/b/2/8b2a34e278acd5bcb609f2a723f545cedd660e03.png" alt="17. Spalten: verschiedene Styles" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 2<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>      align: right<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    tbody tr td+: &gt;-<br>      background-color: yellow;<br>      color: red;<br>    tbody tr td:nth-child(odd)+: &gt;-<br>      background-color: pink;<br>    tbody tr td:first-child+: &gt;-<br>      background-color: cyan;<br>      color: white;<br>      border: 1px solid black;<br>      text-align: left;<br>    tbody tr td:last-child+: &gt;-<br>      background-color: orange;</code> |

## 18. Spaltenbreite anpassen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/f/8/1/f8191e0b9518cc82cb7e6cef23688e50897add75.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/f/8/1/f8191e0b9518cc82cb7e6cef23688e50897add75.png" alt="18. Spaltenbreite anpassen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: custom:auto-entities<br>filter:<br>  include:<br>    - domain: light<br>sort:<br>  count: 2<br>card:<br>  type: custom:flex-table-card<br>  columns:<br>    - &amp;ref_column<br>      name: hhh<br>      data: brightness<br>    - *ref_column<br>    - *ref_column<br>  strict: true<br>  css:<br>    tbody tr td:first-child+: &#x27;width: 50%;&#x27;<br>    tbody tr td:last-child+: &#x27;width: 30%;&#x27;</code> |

## 19. Zellen: einzelne Zeile und Zelle stylen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/4/1/4/41410b7e83f1247cf98977601f05356e7cab1cf4.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/4/1/4/41410b7e83f1247cf98977601f05356e7cab1cf4.png" alt="19. Zellen: einzelne Zeile und Zelle stylen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">type: vertical-stack<br>cards:<br>  - type: markdown<br>    content: &#124;<br>      обращение к ячейке + align<br>    style: &#124;<br>      ha-card {<br>        color: red;<br>      }<br>  - type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 5<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_column<br>          name: hhh<br>          data: brightness<br>          align: right<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>        - *ref_column<br>      strict: true<br>      css:<br>        tbody tr:nth-child(4)+: &gt;-<br>          background-color: orange;<br>          color: blue;<br>        tbody tr:nth-child(4) td+: &gt;-<br>          text-align: center;<br>        tbody tr:nth-child(4) td:nth-child(3)+: &gt;-<br>          background-color: yellow;<br>          color: red;<br>          text-align: left;</code> |

## 20. Dynamisches Styling per Entity-Zustand, Variante 1

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/7/f/4/7f4084b62780bb2c45cf2d9d712d125e5b3f3a8c.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/7/f/4/7f4084b62780bb2c45cf2d9d712d125e5b3f3a8c.png" alt="20. Dynamisches Styling per Entity-Zustand, Variante 1" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: entities<br>    entities:<br>      - entity: input_boolean.test_boolean<br>        name: change color<br><br>  - type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 4<br>    card:<br>      type: custom:flex-table-card<br>      columns: *ref_brightness_right_6cols<br>      strict: true<br>      card_mod:<br>        style: &#124;<br>          ha-card {<br>            {% if is_state(&#x27;input_boolean.test_boolean&#x27;,&#x27;on&#x27;) %}<br>              --my-background-color: yellow;<br>            {% else %}<br>              --my-background-color: cyan;<br>            {% endif %}<br>          }<br>      css:<br>        tbody tr:nth-child(4) td:nth-child(3)+: &#x27;background-color: var(--my-background-color);&#x27;</code> |

## 21. Dynamisches Styling per Entity-Zustand, Variante 2

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/b/5/2/b52d9f8933c0d3a6507bebfa37793c1247236118.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/b/5/2/b52d9f8933c0d3a6507bebfa37793c1247236118.png" alt="21. Dynamisches Styling per Entity-Zustand, Variante 2" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: entities<br>    entities:<br>      - entity: input_boolean.test_boolean<br>        name: change color<br><br>  - type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 4<br>    card:<br>      type: custom:flex-table-card<br>      columns: *ref_brightness_right_6cols<br>      strict: true<br>      card_mod:<br>        style: &#124;<br>          ha-card {<br>            {% if is_state(&#x27;input_boolean.test_boolean&#x27;,&#x27;on&#x27;) %}<br>              --my-background-color: yellow;<br>            {% else %}<br>              --my-background-color: cyan;<br>            {% endif %}<br>          }<br>      css:<br>        tbody tr:nth-child(4) td:nth-child(3)+: &#x27;background-color: var(--my-background-color);&#x27;</code> |

## 22. Bedingte Zellinhalte mit modify, div und span

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/f/5/a/f5a330f7764471bb46af866cac91c69f28155365.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/f/5/a/f5a330f7764471bb46af866cac91c69f28155365.png" alt="22. Bedingte Zellinhalte mit modify, div und span" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 5<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - name: brightness<br>          data: brightness<br>        - name: &quot;div&quot;<br>          data: brightness<br>          modify: &#124;-<br>            if (x == undefined)<br>              &quot;none&quot;<br>            else if (parseInt(x) &gt;= 100 )<br>              &#x27;&lt;div style=&quot;color:cyan;&quot;&gt;more&lt;/div&gt;&#x27;<br>            else<br>              &#x27;&lt;div style=&quot;color:red;&quot;&gt;less&lt;/div&gt;&#x27;<br>        - name: &quot;span&quot;<br>          data: brightness<br>          modify: &#124;-<br>            if (x == undefined)<br>              &quot;none&quot;<br>            else if (parseInt(x) &gt;= 100 )<br>              &#x27;&lt;span style=&quot;color:cyan;&quot;&gt;more&lt;/span&gt;&#x27;<br>            else<br>              &#x27;&lt;span style=&quot;color:red;&quot;&gt;less&lt;/span&gt;&#x27;<br>      strict: true</code> |

## 23. Text in Tabellenzellen auswählbar machen

| Bild | Code |
| --- | --- |
| <a href="https://community-assets.home-assistant.io/original/4X/a/d/3/ad3b787754bccfcf2ef59a908ef7ae3355bcca4c.png" target="_blank" rel="noopener noreferrer"><img src="https://community-assets.home-assistant.io/original/4X/a/d/3/ad3b787754bccfcf2ef59a908ef7ae3355bcca4c.png" alt="23. Text in Tabellenzellen auswählbar machen" style="max-width: 320px; width: 100%; height: auto; border: 1px solid var(--vp-c-divider);"></a> | <code class="forum-inline-code">- type: custom:auto-entities<br>    filter:<br>      include:<br>        - domain: light<br>    sort:<br>      count: 2<br>    card:<br>      type: custom:flex-table-card<br>      columns:<br>        - &amp;ref_0<br>          name: hhh<br>          data: brightness<br>          align: right<br>        - *ref_0<br>        - *ref_0<br>        - *ref_0<br>        - *ref_0<br>        - *ref_0<br>      strict: true<br>      css:<br>        tbody tr+: &#x27;user-select: text&#x27;</code> |

<style>
.forum-inline-code {
  display: block;
  max-height: 420px;
  overflow: auto;
  padding: 10px;
  border-radius: 6px;
  white-space: pre;
  font-size: 12px;
  line-height: 1.45;
}
</style>
