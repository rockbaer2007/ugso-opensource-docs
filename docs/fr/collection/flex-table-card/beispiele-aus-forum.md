---
title: Exemples issus du forum
description: Exemples externes de `flex-table-card` provenant du forum de la communauté Home Assistant, accompagnés d'une image et du code correspondant.
---
<a id="exemples-du-forum"></a>
<a id="orientation-actuelle"></a>

# Exemples issus du forum {#beispiele-aus-forum}

Ces exemples proviennent de la publication [Styling the card](https://community.home-assistant.io/t/flex-table-card/461173/2) d’Ildar_Gabdullin sur le forum de la communauté Home Assistant. Les images sont stockées localement dans cette documentation ; le code est associé à l’exemple correspondant du forum.

::: warning Exemples externes
Ces exemples sont extraits du forum et peuvent nécessiter des ajustements en fonction de la version de Home Assistant, de la version de `flex-table-card`, ou d'autres cartes utilisées, telles que `auto-entities` et `card_mod`.
:::

::: info Versions UIX
La troisième colonne propose une variante UIX du code. Dans ces versions, seul le composant de style est remplacé : `card_mod:` devient `uix:`, tandis que la configuration native `css:` de la carte `flex-table-card` demeure inchangée.
::: :::
## 1. Remplissage par des zéros (zero padding) et bordure de tableau colorée {#_1-zero-padding-und-farbiger-tabellenrahmen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-01.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-01.png" alt="1. Zero padding und farbiger Tabellenrahmen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-01">Copier</button>
</div>
<pre><code id="forum-code-01" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBicmlnaHRuZXNzCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICBzdHJpY3Q6IHRydWUKICAgICAgY3NzOgogICAgICAgIHRhYmxlKzogPi0KICAgICAgICAgIGJvcmRlcjogMXB4IHNvbGlkIGN5YW47CiAgICAgICAgICBwYWRkaW5nOiAwcHg7"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-01">Copier</button>
</div>
<pre><code id="forum-uix-code-01" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBicmlnaHRuZXNzCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICBzdHJpY3Q6IHRydWUKICAgICAgY3NzOgogICAgICAgIHRhYmxlKzogPi0KICAgICAgICAgIGJvcmRlcjogMXB4IHNvbGlkIGN5YW47CiAgICAgICAgICBwYWRkaW5nOiAwcHg7"></code></pre>`
</div></div>`

## 2. Sans bordures internes {#_2-keine-internen-rahmen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-02.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-02.png" alt="2. Keine internen Rahmen"></a>  </div>  <div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-02">Copier</button>
</div>
<pre><code id="forum-code-02" data-code-b64="dHlwZTogdmVydGljYWwtc3RhY2sKY2FyZHM6CiAgLSB0eXBlOiBtYXJrZG93bgogICAgY29udGVudDogfAogICAgICBubyBib3JkZXJzCiAgICBzdHlsZTogfAogICAgICBoYS1jYXJkIHsKICAgICAgICBjb2xvcjogcmVkOwogICAgICB9CiAgLSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBoaGgKICAgICAgICAgIGRhdGE6IGJyaWdodG5lc3MKICAgICAgICAgIGFsaWduOiBjZW50ZXIKICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICBzdHJpY3Q6IHRydWUKICAgICAgY3NzOgogICAgICAgIHRhYmxlKzogJ2JvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7Jw=="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-02">Copier</button>
</div>
<pre><code id="forum-uix-code-02" data-code-b64="dHlwZTogdmVydGljYWwtc3RhY2sKY2FyZHM6CiAgLSB0eXBlOiBtYXJrZG93bgogICAgY29udGVudDogfAogICAgICBubyBib3JkZXJzCiAgICBzdHlsZTogfAogICAgICBoYS1jYXJkIHsKICAgICAgICBjb2xvcjogcmVkOwogICAgICB9CiAgLSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBoaGgKICAgICAgICAgIGRhdGE6IGJyaWdodG5lc3MKICAgICAgICAgIGFsaWduOiBjZW50ZXIKICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICBzdHJpY3Q6IHRydWUKICAgICAgY3NzOgogICAgICAgIHRhYmxlKzogJ2JvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7Jw=="></code></pre>`
</div></div>`

## 3. Cadres internes personnalisés : En-têtes et cellules {#_3-eigene-interne-rahmen-header-und-zellen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-03.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-03.png" alt="3. Eigene interne Rahmen: Header und Zellen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-03">Copier</button>
</div>    <pre><code id="forum-code-03" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0aCs6ICZyZWZfYm9yZGVyX3N0eWxlICdib3JkZXI6IDFweCBzb2xpZCByZWQ7JwogICAgdGQrOiAqcmVmX2JvcmRlcl9zdHlsZQ=="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-03">Copier</button>
</div>
<pre><code id="forum-uix-code-03" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0aCs6ICZyZWZfYm9yZGVyX3N0eWxlICdib3JkZXI6IDFweCBzb2xpZCByZWQ7JwogICAgdGQrOiAqcmVmX2JvcmRlcl9zdHlsZQ=="></code></pre>`
</div></div>`

## 4. Cadres internes personnalisés : cellules de tableau uniquement {#_4-eigene-interne-rahmen-nur-tabellenzellen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-04.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-04.png" alt="4. Eigene interne Rahmen: nur Tabellenzellen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-04">Copier</button>
</div>
<pre><code id="forum-code-04" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0ZCs6ICdib3JkZXI6IDFweCBzb2xpZCByZWQ7Jw=="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">      <span>Version UIX</span>      <button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-04">Copier</button>
</div>
<pre><code id="forum-uix-code-04" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0ZCs6ICdib3JkZXI6IDFweCBzb2xpZCByZWQ7Jw=="></code></pre>`
</div></div>`

## 5. Cadres internes personnalisés : Bord supérieur de la ligne {#_5-eigene-interne-rahmen-zeilenoberkante}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-05.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-05.png" alt="5. Eigene interne Rahmen: Zeilenoberkante"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-05">Copier</button>
</div>
<pre><code id="forum-code-05" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0Ym9keSB0cis6ICdib3JkZXItdG9wOiAxcHggc29saWQgcmVkOyc="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-05">Copier</button>
</div>
<pre><code id="forum-uix-code-05" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0Ym9keSB0cis6ICdib3JkZXItdG9wOiAxcHggc29saWQgcmVkOyc="></code></pre>`
</div></div>`

## 6. Cadres internes personnalisés : Séparateurs de colonnes {#_6-eigene-interne-rahmen-spaltentrenner}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>    <a href="/images/flex-table-card/forum/forum-example-06.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-06.png" alt="6. Eigene interne Rahmen: Spaltentrenner"></a>  </div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-06">Copier</button>
</div>
<pre><code id="forum-code-06" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0aDpudGgtb2YtdHlwZShuKzIpKzogJnJlZl9ib3JkZXJfc3R5bGUgJ2JvcmRlci1sZWZ0OiAxcHggc29saWQgcmVkOycKICAgIHRkOm50aC1vZi10eXBlKG4rMikrOiAqcmVmX2JvcmRlcl9zdHlsZQ=="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-06">Copier</button>
</div>
<pre><code id="forum-uix-code-06" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogY2VudGVyCiAgICAtICpyZWZfY29sdW1uCiAgICAtICpyZWZfY29sdW1uCiAgc3RyaWN0OiB0cnVlCiAgY3NzOgogICAgdGFibGUrOiAnYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsnCiAgICB0aDpudGgtb2YtdHlwZShuKzIpKzogJnJlZl9ib3JkZXJfc3R5bGUgJ2JvcmRlci1sZWZ0OiAxcHggc29saWQgcmVkOycKICAgIHRkOm50aC1vZi10eXBlKG4rMikrOiAqcmVmX2JvcmRlcl9zdHlsZQ=="></code></pre>`
</div></div>`

## 7. Rétablir le remplissage (padding) via card_mod {#_7-padding-per-card-mod-wiederherstellen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-07.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-07.png" alt="7. Padding per card_mod wiederherstellen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-07">Copier</button>
</div>    <pre><code id="forum-code-07" data-code-b64="Y2FyZF9tb2Q6CiAgICBzdHlsZTogfAogICAgICBkaXYgewogICAgICAgIHBhZGRpbmc6IDE2cHg7CiAgICAgIH0="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-07">Copier</button>
</div>
<pre><code id="forum-uix-code-07" data-code-b64="dWl4OgogICAgc3R5bGU6IHwKICAgICAgZGl2IHsKICAgICAgICBwYWRkaW5nOiAxNnB4OwogICAgICB9"></code></pre>`
</div></div>`

## 8. Barre de défilement horizontale {#_8-horizontaler-scrollbalken}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-08.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-08.png" alt="8. Horizontaler Scrollbalken"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-08">Copier</button>
</div>
<pre><code id="forum-code-08" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBicmlnaHRuZXNzCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNzczoKICAgICAgICB0YWJsZSs6ICdwYWRkaW5nOiAwcHgnCiAgICAgIGNhcmRfbW9kOgogICAgICAgIHN0eWxlOiB8CiAgICAgICAgICBoYS1jYXJkIHsKICAgICAgICAgICAgb3ZlcmZsb3c6IGF1dG87CiAgICAgICAgICB9"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>      <button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-08">Copier</button>
</div>
<pre><code id="forum-uix-code-08" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfY29sdW1uCiAgICAgICAgICBuYW1lOiBicmlnaHRuZXNzCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNzczoKICAgICAgICB0YWJsZSs6ICdwYWRkaW5nOiAwcHgnCiAgICAgIHVpeDoKICAgICAgICBzdHlsZTogfAogICAgICAgICAgaGEtY2FyZCB7CiAgICAgICAgICAgIG92ZXJmbG93OiBhdXRvOwogICAgICAgICAgfQ=="></code></pre>`
</div></div>`

## 9. Barre de défilement horizontale et verticale {#_9-horizontaler-und-vertikaler-scrollbalken}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-09.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-09.png" alt="9. Horizontaler und vertikaler Scrollbalken"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-09">Copier</button>
</div>
<pre><code id="forum-code-09" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDEzCiAgICBjYXJkOgogICAgICB0eXBlOiBjdXN0b206ZmxleC10YWJsZS1jYXJkCiAgICAgIGNvbHVtbnM6CiAgICAgICAgLSAmcmVmX2NvbHVtbgogICAgICAgICAgbmFtZTogYnJpZ2h0bmVzcwogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgIHN0cmljdDogdHJ1ZQogICAgICBjc3M6CiAgICAgICAgdGFibGUrOiAncGFkZGluZzogMHB4JwogICAgICBjYXJkX21vZDoKICAgICAgICBzdHlsZTogfAogICAgICAgICAgaGEtY2FyZCB7CiAgICAgICAgICAgIG92ZXJmbG93OiBhdXRvOwogICAgICAgICAgICBtYXgtaGVpZ2h0OiAyMDBweDsKICAgICAgICAgIH0="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-09">Copier</button>
</div>
<pre><code id="forum-uix-code-09" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDEzCiAgICBjYXJkOgogICAgICB0eXBlOiBjdXN0b206ZmxleC10YWJsZS1jYXJkCiAgICAgIGNvbHVtbnM6CiAgICAgICAgLSAmcmVmX2NvbHVtbgogICAgICAgICAgbmFtZTogYnJpZ2h0bmVzcwogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgIHN0cmljdDogdHJ1ZQogICAgICBjc3M6CiAgICAgICAgdGFibGUrOiAncGFkZGluZzogMHB4JwogICAgICB1aXg6CiAgICAgICAgc3R5bGU6IHwKICAgICAgICAgIGhhLWNhcmQgewogICAgICAgICAgICBvdmVyZmxvdzogYXV0bzsKICAgICAgICAgICAgbWF4LWhlaWdodDogMjAwcHg7CiAgICAgICAgICB9"></code></pre>`
</div></div>`

## 10. En-tête : différents styles {#_10-header-verschiedene-styles}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-10.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-10.png" alt="10. Header: verschiedene Styles"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-10">Copier</button>
</div>
<pre><code id="forum-code-10" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0aGVhZCB0aDogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogbWFnZW50YTsKICAgICAgdGV4dC1hbGlnbjogbGVmdCAhaW1wb3J0YW50OwogICAgICBmb250LXdlaWdodDogMzAwOwogICAgICBib3JkZXI6IDFweCBzb2xpZDsKICAgIHRoZWFkIHRoOmZpcnN0LWNoaWxkOiA+LQogICAgICB0ZXh0LWFsaWduOiBjZW50ZXIgIWltcG9ydGFudDsKICAgICAgY29sb3I6IGN5YW47CiAgICB0aGVhZCB0aDpudGgtY2hpbGQoMik6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IGxpZ2h0Z3JlZW47CiAgICB0aGVhZCB0aDpudGgtY2hpbGQoNCk6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwwLDI1NSwwLjIpOwogICAgdGhlYWQgdGg6bnRoLWNoaWxkKDUpOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMjU1LDI1NSwyNTUpOwogICAgICBjb2xvcjogcmVkOwogICAgICBib3JkZXItY29sb3I6IGN5YW47CiAgICB0aGVhZCB0aDpsYXN0LWNoaWxkOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiB5ZWxsb3c7CiAgICAgIGNvbG9yOiBvcmFuZ2U7CiAgICAgIHRleHQtYWxpZ246IHJpZ2h0ICFpbXBvcnRhbnQ7"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-10">Copier</button>
</div>
<pre><code id="forum-uix-code-10" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0aGVhZCB0aDogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogbWFnZW50YTsKICAgICAgdGV4dC1hbGlnbjogbGVmdCAhaW1wb3J0YW50OwogICAgICBmb250LXdlaWdodDogMzAwOwogICAgICBib3JkZXI6IDFweCBzb2xpZDsKICAgIHRoZWFkIHRoOmZpcnN0LWNoaWxkOiA+LQogICAgICB0ZXh0LWFsaWduOiBjZW50ZXIgIWltcG9ydGFudDsKICAgICAgY29sb3I6IGN5YW47CiAgICB0aGVhZCB0aDpudGgtY2hpbGQoMik6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IGxpZ2h0Z3JlZW47CiAgICB0aGVhZCB0aDpudGgtY2hpbGQoNCk6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwwLDI1NSwwLjIpOwogICAgdGhlYWQgdGg6bnRoLWNoaWxkKDUpOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMjU1LDI1NSwyNTUpOwogICAgICBjb2xvcjogcmVkOwogICAgICBib3JkZXItY29sb3I6IGN5YW47CiAgICB0aGVhZCB0aDpsYXN0LWNoaWxkOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiB5ZWxsb3c7CiAgICAgIGNvbG9yOiBvcmFuZ2U7CiAgICAgIHRleHQtYWxpZ246IHJpZ2h0ICFpbXBvcnRhbnQ7"></code></pre>`
</div></div>`

## 11. Masquer les en-têtes {#_11-header-ausblenden}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-11.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-11.png" alt="11. Header ausblenden"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">      <span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-11">Copier</button>
</div>
<pre><code id="forum-code-11" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRoZWFkIHRoOiAnZGlzcGxheTogbm9uZTsn"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-11">Copier</button>
</div>
<pre><code id="forum-uix-code-11" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRoZWFkIHRoOiAnZGlzcGxheTogbm9uZTsn"></code></pre>`
</div></div>`

## 12. Masquer partiellement l'en-tête {#_12-header-teilweise-ausblenden}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-12.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-12.png" alt="12. Header teilweise ausblenden"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-12">Copier</button>
</div>
<pre><code id="forum-code-12" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRoZWFkIHRoOiAnY29sb3I6IHRyYW5zcGFyZW50OycKICAgIHRoZWFkIHRoOmZpcnN0LWNoaWxkOiA+LQogICAgICBjb2xvcjogdW5zZXQ7CiAgICAgIGJhY2tncm91bmQtY29sb3I6IGxpZ2h0Z3JlZW47CiAgICB0aGVhZCB0aDpsYXN0LWNoaWxkOiA+LQogICAgICBjb2xvcjogdW5zZXQ7CiAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzs="></code></pre>`
</div>  <div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-12">Copier</button>
</div>
<pre><code id="forum-uix-code-12" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRoZWFkIHRoOiAnY29sb3I6IHRyYW5zcGFyZW50OycKICAgIHRoZWFkIHRoOmZpcnN0LWNoaWxkOiA+LQogICAgICBjb2xvcjogdW5zZXQ7CiAgICAgIGJhY2tncm91bmQtY29sb3I6IGxpZ2h0Z3JlZW47CiAgICB0aGVhZCB0aDpsYXN0LWNoaWxkOiA+LQogICAgICBjb2xvcjogdW5zZXQ7CiAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzs="></code></pre>`
</div></div>`

## 13. Résumer visuellement les en-têtes {#_13-header-optisch-zusammenfassen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-13.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-13.png" alt="13. Header optisch zusammenfassen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-13">Copier</button>
</div>
<pre><code id="forum-code-13" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0YWJsZSs6ICdib3JkZXItY29sbGFwc2U6IGNvbGxhcHNlOycKICAgIHRoKzogPi0KICAgICAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkIHJnYigxMjcsMTI3LDEyNyk7CiAgICAgIHRleHQtYWxpZ246IGxlZnQgIWltcG9ydGFudDsKICAgIHRoOm50aC1vZi10eXBlKG4rMikrOiAmcmVmX3N0eWxlX2JvcmRlciA+LQogICAgICBib3JkZXItbGVmdDogMXB4IHNvbGlkIHJnYigxMjcsMTI3LDEyNykKICAgIHRkOm50aC1vZi10eXBlKG4rMikrOiAqcmVmX3N0eWxlX2JvcmRlcgogICAgdGg6bnRoLW9mLXR5cGUoMikrOiAmcmVmX3N0eWxlX21lcmdlZF9oZWFkZXIgPi0KICAgICAgYm9yZGVyLWxlZnQ6IG5vbmU7CiAgICAgIGNvbG9yOiB0cmFuc3BhcmVudDsKICAgIHRoOm50aC1vZi10eXBlKDUpKzogKnJlZl9zdHlsZV9tZXJnZWRfaGVhZGVyCiAgY2FyZF9tb2Q6CiAgICBzdHlsZTogfAogICAgICBkaXYgewogICAgICAgIHBhZGRpbmc6IDE2cHg7CiAgICAgIH0="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-13">Copier</button>
</div>    <pre><code id="forum-uix-code-13" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0YWJsZSs6ICdib3JkZXItY29sbGFwc2U6IGNvbGxhcHNlOycKICAgIHRoKzogPi0KICAgICAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkIHJnYigxMjcsMTI3LDEyNyk7CiAgICAgIHRleHQtYWxpZ246IGxlZnQgIWltcG9ydGFudDsKICAgIHRoOm50aC1vZi10eXBlKG4rMikrOiAmcmVmX3N0eWxlX2JvcmRlciA+LQogICAgICBib3JkZXItbGVmdDogMXB4IHNvbGlkIHJnYigxMjcsMTI3LDEyNykKICAgIHRkOm50aC1vZi10eXBlKG4rMikrOiAqcmVmX3N0eWxlX2JvcmRlcgogICAgdGg6bnRoLW9mLXR5cGUoMikrOiAmcmVmX3N0eWxlX21lcmdlZF9oZWFkZXIgPi0KICAgICAgYm9yZGVyLWxlZnQ6IG5vbmU7CiAgICAgIGNvbG9yOiB0cmFuc3BhcmVudDsKICAgIHRoOm50aC1vZi10eXBlKDUpKzogKnJlZl9zdHlsZV9tZXJnZWRfaGVhZGVyCiAgdWl4OgogICAgc3R5bGU6IHwKICAgICAgZGl2IHsKICAgICAgICBwYWRkaW5nOiAxNnB4OwogICAgICB9"></code></pre>`
</div></div>`

## 14. Lignes : couleur d'arrière-plan uniforme {#_14-zeilen-gleiche-hintergrundfarbe}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-14.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-14.png" alt="14. Zeilen: gleiche Hintergrundfarbe"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-14">Copier</button>
</div>
<pre><code id="forum-code-14" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0cis6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwyNTUsMCwwLjQpICFpbXBvcnRhbnQ7"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-14">Copier</button>
</div>
<pre><code id="forum-uix-code-14" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0cis6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwyNTUsMCwwLjQpICFpbXBvcnRhbnQ7"></code></pre>`
</div></div>`

## 15. Lignes : styles alternés et individuels {#_15-zeilen-abwechselnde-und-einzelne-styles}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-15.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-15.png" alt="15. Zeilen: abwechselnde und einzelne Styles"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-15">Copier</button>
</div>
<pre><code id="forum-code-15" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNwpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0cis6ICdjb2xvcjogcmVkJwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKG9kZCkrOiAnYmFja2dyb3VuZC1jb2xvcjogcmdiYSgwLDI1NSwwLDAuNCk7JwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKGV2ZW4pKzogJ2JhY2tncm91bmQtY29sb3I6IHJnYmEoMjU1LDI1NSwwLDAuNCk7JwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogb3JhbmdlOwogICAgICBjb2xvcjogYmx1ZTs="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-15">Copier</button>
</div>
<pre><code id="forum-uix-code-15" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNwpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0cis6ICdjb2xvcjogcmVkJwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKG9kZCkrOiAnYmFja2dyb3VuZC1jb2xvcjogcmdiYSgwLDI1NSwwLDAuNCk7JwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKGV2ZW4pKzogJ2JhY2tncm91bmQtY29sb3I6IHJnYmEoMjU1LDI1NSwwLDAuNCk7JwogICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogb3JhbmdlOwogICAgICBjb2xvcjogYmx1ZTs="></code></pre>`
</div></div>`

## 16. Lignes : Style au survol {#_16-zeilen-hover-styling}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-16.gif" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-16.gif" alt="16. Zeilen: Hover-Styling"></a>
</div>
<div class="forum-example-code">    <div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-16">Copier</button>
</div>
<pre><code id="forum-code-16" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNhcmRfbW9kOgogICAgc3R5bGU6IHwKICAgICAgdGJvZHkgdHI6aG92ZXIgewogICAgICAgIGJhY2tncm91bmQtY29sb3I6IGNvcmFsICFpbXBvcnRhbnQ7CiAgICAgIH0="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-16">Copier</button>
</div>
<pre><code id="forum-uix-code-16" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogNQpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIHVpeDoKICAgIHN0eWxlOiB8CiAgICAgIHRib2R5IHRyOmhvdmVyIHsKICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiBjb3JhbCAhaW1wb3J0YW50OwogICAgICB9"></code></pre>`
</div></div>`

## 17. Colonnes : différents styles {#_17-spalten-verschiedene-styles}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-17.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-17.png" alt="17. Spalten: verschiedene Styles"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-17">Copier</button>
</div>
<pre><code id="forum-code-17" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0ciB0ZCs6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgY29sb3I6IHJlZDsKICAgIHRib2R5IHRyIHRkOm50aC1jaGlsZChvZGQpKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogcGluazsKICAgIHRib2R5IHRyIHRkOmZpcnN0LWNoaWxkKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogY3lhbjsKICAgICAgY29sb3I6IHdoaXRlOwogICAgICBib3JkZXI6IDFweCBzb2xpZCBibGFjazsKICAgICAgdGV4dC1hbGlnbjogbGVmdDsKICAgIHRib2R5IHRyIHRkOmxhc3QtY2hpbGQrOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiBvcmFuZ2U7"></code></pre>`  </div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-17">Copier</button>
</div>
<pre><code id="forum-uix-code-17" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICBhbGlnbjogcmlnaHQKICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICAgIC0gKnJlZl9jb2x1bW4KICBzdHJpY3Q6IHRydWUKICBjc3M6CiAgICB0Ym9keSB0ciB0ZCs6ID4tCiAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgY29sb3I6IHJlZDsKICAgIHRib2R5IHRyIHRkOm50aC1jaGlsZChvZGQpKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogcGluazsKICAgIHRib2R5IHRyIHRkOmZpcnN0LWNoaWxkKzogPi0KICAgICAgYmFja2dyb3VuZC1jb2xvcjogY3lhbjsKICAgICAgY29sb3I6IHdoaXRlOwogICAgICBib3JkZXI6IDFweCBzb2xpZCBibGFjazsKICAgICAgdGV4dC1hbGlnbjogbGVmdDsKICAgIHRib2R5IHRyIHRkOmxhc3QtY2hpbGQrOiA+LQogICAgICBiYWNrZ3JvdW5kLWNvbG9yOiBvcmFuZ2U7"></code></pre>`
</div></div>`

## 18. Ajustement de la largeur des colonnes {#_18-spaltenbreite-anpassen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-18.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-18.png" alt="18. Spaltenbreite anpassen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-18">Copier</button>
</div>
<pre><code id="forum-code-18" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRib2R5IHRyIHRkOmZpcnN0LWNoaWxkKzogJ3dpZHRoOiA1MCU7JwogICAgdGJvZHkgdHIgdGQ6bGFzdC1jaGlsZCs6ICd3aWR0aDogMzAlOyc="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>      <button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-18">Copier</button>
</div>    <pre><code id="forum-uix-code-18" data-code-b64="dHlwZTogY3VzdG9tOmF1dG8tZW50aXRpZXMKZmlsdGVyOgogIGluY2x1ZGU6CiAgICAtIGRvbWFpbjogbGlnaHQKc29ydDoKICBjb3VudDogMgpjYXJkOgogIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICBjb2x1bW5zOgogICAgLSAmcmVmX2NvbHVtbgogICAgICBuYW1lOiBoaGgKICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgLSAqcmVmX2NvbHVtbgogICAgLSAqcmVmX2NvbHVtbgogIHN0cmljdDogdHJ1ZQogIGNzczoKICAgIHRib2R5IHRyIHRkOmZpcnN0LWNoaWxkKzogJ3dpZHRoOiA1MCU7JwogICAgdGJvZHkgdHIgdGQ6bGFzdC1jaGlsZCs6ICd3aWR0aDogMzAlOyc="></code></pre>`
</div></div>`

## 19. Cellules : définition du style d'une ligne et d'une cellule individuelles {#_19-zellen-einzelne-zeile-und-zelle-stylen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-19.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-19.png" alt="19. Zellen: einzelne Zeile und Zelle stylen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-19">Copier</button>
</div>
<pre><code id="forum-code-19" data-code-b64="dHlwZTogdmVydGljYWwtc3RhY2sKY2FyZHM6CiAgLSB0eXBlOiBtYXJrZG93bgogICAgY29udGVudDogfAogICAgICDQvtCx0YDQsNGJ0LXQvdC40LUg0Log0Y/Rh9C10LnQutC1ICsgYWxpZ24KICAgIHN0eWxlOiB8CiAgICAgIGhhLWNhcmQgewogICAgICAgIGNvbG9yOiByZWQ7CiAgICAgIH0KICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNQogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOgogICAgICAgIC0gJnJlZl9jb2x1bW4KICAgICAgICAgIG5hbWU6IGhoaAogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgICAgYWxpZ246IHJpZ2h0CiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNzczoKICAgICAgICB0Ym9keSB0cjpudGgtY2hpbGQoNCkrOiA+LQogICAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogb3JhbmdlOwogICAgICAgICAgY29sb3I6IGJsdWU7CiAgICAgICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpIHRkKzogPi0KICAgICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICB0Ym9keSB0cjpudGgtY2hpbGQoNCkgdGQ6bnRoLWNoaWxkKDMpKzogPi0KICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgICAgIGNvbG9yOiByZWQ7CiAgICAgICAgICB0ZXh0LWFsaWduOiBsZWZ0Ow=="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-19">Copier</button>
</div>
<pre><code id="forum-uix-code-19" data-code-b64="dHlwZTogdmVydGljYWwtc3RhY2sKY2FyZHM6CiAgLSB0eXBlOiBtYXJrZG93bgogICAgY29udGVudDogfAogICAgICDQvtCx0YDQsNGJ0LXQvdC40LUg0Log0Y/Rh9C10LnQutC1ICsgYWxpZ24KICAgIHN0eWxlOiB8CiAgICAgIGhhLWNhcmQgewogICAgICAgIGNvbG9yOiByZWQ7CiAgICAgIH0KICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNQogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOgogICAgICAgIC0gJnJlZl9jb2x1bW4KICAgICAgICAgIG5hbWU6IGhoaAogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgICAgYWxpZ246IHJpZ2h0CiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgICAtICpyZWZfY29sdW1uCiAgICAgICAgLSAqcmVmX2NvbHVtbgogICAgICAgIC0gKnJlZl9jb2x1bW4KICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNzczoKICAgICAgICB0Ym9keSB0cjpudGgtY2hpbGQoNCkrOiA+LQogICAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogb3JhbmdlOwogICAgICAgICAgY29sb3I6IGJsdWU7CiAgICAgICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpIHRkKzogPi0KICAgICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICB0Ym9keSB0cjpudGgtY2hpbGQoNCkgdGQ6bnRoLWNoaWxkKDMpKzogPi0KICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgICAgIGNvbG9yOiByZWQ7CiAgICAgICAgICB0ZXh0LWFsaWduOiBsZWZ0Ow=="></code></pre>`  </div></div>`

## 20. Style dynamique basé sur l'état de l'entité, variante 1 {#_20-dynamisches-styling-per-entity-zustand-variante-1}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-20.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-20.png" alt="20. Dynamisches Styling per Entity-Zustand, Variante 1"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-20">Copier</button>
</div>
<pre><code id="forum-code-20" data-code-b64="LSB0eXBlOiBlbnRpdGllcwogICAgZW50aXRpZXM6CiAgICAgIC0gZW50aXR5OiBpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbgogICAgICAgIG5hbWU6IGNoYW5nZSBjb2xvcgoKICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNAogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOiAqcmVmX2JyaWdodG5lc3NfcmlnaHRfNmNvbHMKICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNhcmRfbW9kOgogICAgICAgIHN0eWxlOiB8CiAgICAgICAgICBoYS1jYXJkIHsKICAgICAgICAgICAgeyUgaWYgaXNfc3RhdGUoJ2lucHV0X2Jvb2xlYW4udGVzdF9ib29sZWFuJywnb24nKSAlfQogICAgICAgICAgICAgIC0tbXktYmFja2dyb3VuZC1jb2xvcjogeWVsbG93OwogICAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgICAgLS1teS1iYWNrZ3JvdW5kLWNvbG9yOiBjeWFuOwogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgfQogICAgICBjc3M6CiAgICAgICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpIHRkOm50aC1jaGlsZCgzKSs6ICdiYWNrZ3JvdW5kLWNvbG9yOiB2YXIoLS1teS1iYWNrZ3JvdW5kLWNvbG9yKTsn"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-20">Copier</button>
</div>
<pre><code id="forum-uix-code-20" data-code-b64="LSB0eXBlOiBlbnRpdGllcwogICAgZW50aXRpZXM6CiAgICAgIC0gZW50aXR5OiBpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbgogICAgICAgIG5hbWU6IGNoYW5nZSBjb2xvcgoKICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNAogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOiAqcmVmX2JyaWdodG5lc3NfcmlnaHRfNmNvbHMKICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIHVpeDoKICAgICAgICBzdHlsZTogfAogICAgICAgICAgaGEtY2FyZCB7CiAgICAgICAgICAgIHslIGlmIGlzX3N0YXRlKCdpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbicsJ29uJykgJX0KICAgICAgICAgICAgICAtLW15LWJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgIC0tbXktYmFja2dyb3VuZC1jb2xvcjogY3lhbjsKICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgIH0KICAgICAgY3NzOgogICAgICAgIHRib2R5IHRyOm50aC1jaGlsZCg0KSB0ZDpudGgtY2hpbGQoMykrOiAnYmFja2dyb3VuZC1jb2xvcjogdmFyKC0tbXktYmFja2dyb3VuZC1jb2xvcik7Jw=="></code></pre>`
</div></div>`

## 21. Style dynamique via l'état de l'entité, variante 2 {#_21-dynamisches-styling-per-entity-zustand-variante-2}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-21.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-21.png" alt="21. Dynamisches Styling per Entity-Zustand, Variante 2"></a>  </div>  <div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-21">Copier</button>
</div>
<pre><code id="forum-code-21" data-code-b64="LSB0eXBlOiBlbnRpdGllcwogICAgZW50aXRpZXM6CiAgICAgIC0gZW50aXR5OiBpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbgogICAgICAgIG5hbWU6IGNoYW5nZSBjb2xvcgoKICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNAogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOiAqcmVmX2JyaWdodG5lc3NfcmlnaHRfNmNvbHMKICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIGNhcmRfbW9kOgogICAgICAgIHN0eWxlOiB8CiAgICAgICAgICBoYS1jYXJkIHsKICAgICAgICAgICAgeyUgaWYgaXNfc3RhdGUoJ2lucHV0X2Jvb2xlYW4udGVzdF9ib29sZWFuJywnb24nKSAlfQogICAgICAgICAgICAgIC0tbXktYmFja2dyb3VuZC1jb2xvcjogeWVsbG93OwogICAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgICAgLS1teS1iYWNrZ3JvdW5kLWNvbG9yOiBjeWFuOwogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgfQogICAgICBjc3M6CiAgICAgICAgdGJvZHkgdHI6bnRoLWNoaWxkKDQpIHRkOm50aC1jaGlsZCgzKSs6ICdiYWNrZ3JvdW5kLWNvbG9yOiB2YXIoLS1teS1iYWNrZ3JvdW5kLWNvbG9yKTsn"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-21">Copier</button>
</div>
<pre><code id="forum-uix-code-21" data-code-b64="LSB0eXBlOiBlbnRpdGllcwogICAgZW50aXRpZXM6CiAgICAgIC0gZW50aXR5OiBpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbgogICAgICAgIG5hbWU6IGNoYW5nZSBjb2xvcgoKICAtIHR5cGU6IGN1c3RvbTphdXRvLWVudGl0aWVzCiAgICBmaWx0ZXI6CiAgICAgIGluY2x1ZGU6CiAgICAgICAgLSBkb21haW46IGxpZ2h0CiAgICBzb3J0OgogICAgICBjb3VudDogNAogICAgY2FyZDoKICAgICAgdHlwZTogY3VzdG9tOmZsZXgtdGFibGUtY2FyZAogICAgICBjb2x1bW5zOiAqcmVmX2JyaWdodG5lc3NfcmlnaHRfNmNvbHMKICAgICAgc3RyaWN0OiB0cnVlCiAgICAgIHVpeDoKICAgICAgICBzdHlsZTogfAogICAgICAgICAgaGEtY2FyZCB7CiAgICAgICAgICAgIHslIGlmIGlzX3N0YXRlKCdpbnB1dF9ib29sZWFuLnRlc3RfYm9vbGVhbicsJ29uJykgJX0KICAgICAgICAgICAgICAtLW15LWJhY2tncm91bmQtY29sb3I6IHllbGxvdzsKICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgIC0tbXktYmFja2dyb3VuZC1jb2xvcjogY3lhbjsKICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgIH0KICAgICAgY3NzOgogICAgICAgIHRib2R5IHRyOm50aC1jaGlsZCg0KSB0ZDpudGgtY2hpbGQoMykrOiAnYmFja2dyb3VuZC1jb2xvcjogdmFyKC0tbXktYmFja2dyb3VuZC1jb2xvcik7Jw=="></code></pre>`
</div></div>`

## 22. Contenu de cellule conditionnel avec « modify », « div » et « span » {#_22-bedingte-zellinhalte-mit-modify-div-und-span}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-22.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-22.png" alt="22. Bedingte Zellinhalte mit modify, div und span"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-22">Copier</button>
</div>    <pre><code id="forum-code-22" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtIG5hbWU6IGJyaWdodG5lc3MKICAgICAgICAgIGRhdGE6IGJyaWdodG5lc3MKICAgICAgICAtIG5hbWU6ICJkaXYiCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgICBtb2RpZnk6IHwtCiAgICAgICAgICAgIGlmICh4ID09IHVuZGVmaW5lZCkKICAgICAgICAgICAgICAibm9uZSIKICAgICAgICAgICAgZWxzZSBpZiAocGFyc2VJbnQoeCkgPj0gMTAwICkKICAgICAgICAgICAgICAnPGRpdiBzdHlsZT0iY29sb3I6Y3lhbjsiPm1vcmU8L2Rpdj4nCiAgICAgICAgICAgIGVsc2UKICAgICAgICAgICAgICAnPGRpdiBzdHlsZT0iY29sb3I6cmVkOyI+bGVzczwvZGl2PicKICAgICAgICAtIG5hbWU6ICJzcGFuIgogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgICAgbW9kaWZ5OiB8LQogICAgICAgICAgICBpZiAoeCA9PSB1bmRlZmluZWQpCiAgICAgICAgICAgICAgIm5vbmUiCiAgICAgICAgICAgIGVsc2UgaWYgKHBhcnNlSW50KHgpID49IDEwMCApCiAgICAgICAgICAgICAgJzxzcGFuIHN0eWxlPSJjb2xvcjpjeWFuOyI+bW9yZTwvc3Bhbj4nCiAgICAgICAgICAgIGVsc2UKICAgICAgICAgICAgICAnPHNwYW4gc3R5bGU9ImNvbG9yOnJlZDsiPmxlc3M8L3NwYW4+JwogICAgICBzdHJpY3Q6IHRydWU="></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">
<span>Version UIX</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-22">Copier</button>
</div>
<pre><code id="forum-uix-code-22" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDUKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtIG5hbWU6IGJyaWdodG5lc3MKICAgICAgICAgIGRhdGE6IGJyaWdodG5lc3MKICAgICAgICAtIG5hbWU6ICJkaXYiCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgICBtb2RpZnk6IHwtCiAgICAgICAgICAgIGlmICh4ID09IHVuZGVmaW5lZCkKICAgICAgICAgICAgICAibm9uZSIKICAgICAgICAgICAgZWxzZSBpZiAocGFyc2VJbnQoeCkgPj0gMTAwICkKICAgICAgICAgICAgICAnPGRpdiBzdHlsZT0iY29sb3I6Y3lhbjsiPm1vcmU8L2Rpdj4nCiAgICAgICAgICAgIGVsc2UKICAgICAgICAgICAgICAnPGRpdiBzdHlsZT0iY29sb3I6cmVkOyI+bGVzczwvZGl2PicKICAgICAgICAtIG5hbWU6ICJzcGFuIgogICAgICAgICAgZGF0YTogYnJpZ2h0bmVzcwogICAgICAgICAgbW9kaWZ5OiB8LQogICAgICAgICAgICBpZiAoeCA9PSB1bmRlZmluZWQpCiAgICAgICAgICAgICAgIm5vbmUiCiAgICAgICAgICAgIGVsc2UgaWYgKHBhcnNlSW50KHgpID49IDEwMCApCiAgICAgICAgICAgICAgJzxzcGFuIHN0eWxlPSJjb2xvcjpjeWFuOyI+bW9yZTwvc3Bhbj4nCiAgICAgICAgICAgIGVsc2UKICAgICAgICAgICAgICAnPHNwYW4gc3R5bGU9ImNvbG9yOnJlZDsiPmxlc3M8L3NwYW4+JwogICAgICBzdHJpY3Q6IHRydWU="></code></pre>`
</div></div>`

## 23. Rendre le texte des cellules de tableau sélectionnable {#_23-text-in-tabellenzellen-auswahlbar-machen}

<div class="forum-example-row">
<div class="forum-example-image">
<div class="forum-example-label">Image</div>
<a href="/images/flex-table-card/forum/forum-example-23.png" target="_blank" rel="noopener noreferrer"><img src="/images/flex-table-card/forum/forum-example-23.png" alt="23. Text in Tabellenzellen auswählbar machen"></a>
</div>
<div class="forum-example-code">
<div class="forum-example-code-header">
<span>Code</span>
<button type="button" class="forum-copy-button" data-copy-target="forum-code-23">Copier</button>
</div>
<pre><code id="forum-code-23" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDIKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfMAogICAgICAgICAgbmFtZTogaGhoCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgICBhbGlnbjogcmlnaHQKICAgICAgICAtICpyZWZfMAogICAgICAgIC0gKnJlZl8wCiAgICAgICAgLSAqcmVmXzAKICAgICAgICAtICpyZWZfMAogICAgICAgIC0gKnJlZl8wCiAgICAgIHN0cmljdDogdHJ1ZQogICAgICBjc3M6CiAgICAgICAgdGJvZHkgdHIrOiAndXNlci1zZWxlY3Q6IHRleHQn"></code></pre>`
</div>
<div class="forum-example-code forum-example-code-uix">
<div class="forum-example-code-header">      <span>Version UIX</span>      <button type="button" class="forum-copy-button" data-copy-target="forum-uix-code-23">Copier</button>
</div>
<pre><code id="forum-uix-code-23" data-code-b64="LSB0eXBlOiBjdXN0b206YXV0by1lbnRpdGllcwogICAgZmlsdGVyOgogICAgICBpbmNsdWRlOgogICAgICAgIC0gZG9tYWluOiBsaWdodAogICAgc29ydDoKICAgICAgY291bnQ6IDIKICAgIGNhcmQ6CiAgICAgIHR5cGU6IGN1c3RvbTpmbGV4LXRhYmxlLWNhcmQKICAgICAgY29sdW1uczoKICAgICAgICAtICZyZWZfMAogICAgICAgICAgbmFtZTogaGhoCiAgICAgICAgICBkYXRhOiBicmlnaHRuZXNzCiAgICAgICAgICBhbGlnbjogcmlnaHQKICAgICAgICAtICpyZWZfMAogICAgICAgIC0gKnJlZl8wCiAgICAgICAgLSAqcmVmXzAKICAgICAgICAtICpyZWZfMAogICAgICAgIC0gKnJlZl8wCiAgICAgIHN0cmljdDogdHJ1ZQogICAgICBjc3M6CiAgICAgICAgdGJvZHkgdHIrOiAndXNlci1zZWxlY3Q6IHRleHQn"></code></pre>`
</div></div>`

<script setup>
import { onMounted } from 'vue'

const decodeCode = (value) => decodeURIComponent(Array.from(atob(value), (char) => `%${char.charCodeAt(0).toString(16).padStart(2, '0')}`).join(''))

onMounted(() => {
  document.querySelectorAll('[data-code-b64]').forEach((code) => {
    code.textContent = decodeCode(code.dataset.codeB64 || '')
  })
  document.querySelectorAll('.forum-copy-button').forEach((button) => {
    button.addEventListener('click', async () => {
      const target = document.getElementById(button.dataset.copyTarget)
      if (!target) return
      try {
        await navigator.clipboard.writeText(target.textContent || '')
        button.textContent = 'Kopiert'
        window.setTimeout(() => { button.textContent = 'Kopieren' }, 1400)
      } catch {
        button.textContent = 'Fehler'
        window.setTimeout(() => { button.textContent = 'Kopieren' }, 1400)
      }
    })
  })
})
</script>

<style>
.forum-example-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 16px;
  align-items: start;
  margin: 14px 0 36px;
}
.forum-example-label,
.forum-example-code-header {
  margin-bottom: 8px;
  font-weight: 600;
}
.forum-example-image {
  grid-column: 1 / -1;
}
.forum-example-image img {
  display: block;
  width: auto;
  max-width: min(100%, 920px);
  height: auto;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
}
.forum-example-code {
  min-width: 0;
}
.forum-example-code-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
}
.forum-copy-button {
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  padding: 4px 10px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  cursor: pointer;
  font-size: 12px;
}
.forum-copy-button:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
.forum-example-code pre {
  max-height: 420px;
  margin: 0;
  overflow: auto;
  padding: 12px;
  border-radius: 6px;
  background: var(--vp-code-block-bg);
}
.forum-example-code code {
  white-space: pre;
  font-size: 12px;
  line-height: 1.45;
}
@media (max-width: 760px) {
  .forum-example-row {
    grid-template-columns: 1fr;
  }
}
</style>
