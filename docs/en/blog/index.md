---
title: Blog
description: News, project updates, guides and code snippets by UGSo Software.
---

# UGSo Open Source Blog

This section contains news, development updates, guides and reusable code
snippets.

## Areas

<div class="blog-grid">

<article class="blog-card">

### 📰 Project Reports

News and development updates for HADash, ATLAS, Ultimate Timer and other
projects.

[View posts](./posts/hadash-preview)

</article>

<article class="blog-card">

### 💻 Code Snippets

YAML, JavaScript, Blockly, Lovelace and Home Assistant examples ready to adapt.

[Open code snippets](./snippets/)

</article>

<article class="blog-card">

### 🧰 Guides

Step-by-step explanations with complete examples and notes.

[Open post template](./post-template)

</article>

</div>

## Latest Posts

- [HADash v0.9.4 Preview](./posts/hadash-preview)
- [ATLAS - Runtime Foundation](./posts/atlas-runtime-foundation)
- [Home Assistant YAML examples](./snippets/home-assistant-yaml)
- [JavaScript examples](./snippets/javascript)
- [Blockly examples](./snippets/blockly)
- [Lovelace and Bubble Card examples](./snippets/lovelace)

## Publishing Code

VitePress detects the language of a code block from the identifier after the
three backticks:

````md
```yaml
alias: Example
triggers: []
actions: []
```
````

Supported languages include:

- `yaml`
- `javascript` or `js`
- `typescript` or `ts`
- `json`
- `html`
- `css`
- `csharp`
- `powershell`
- `bash`
- `xml`
- `sql`

Every code block automatically gets a **copy button**.
