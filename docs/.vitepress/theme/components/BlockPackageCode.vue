<script setup>
import { ref } from 'vue'
const props = defineProps({ code: { type: String, required: true }, english: Boolean, french: Boolean })
const message = ref('')
const field = ref(null)
async function copy() {
  try { await navigator.clipboard.writeText(props.code); message.value = props.french ? 'Code copié.' : props.english ? 'Code copied.' : 'Code kopiert.' }
  catch { field.value.focus(); field.value.select(); message.value = props.french ? 'Appuyer sur Ctrl+C pour copier.' : props.english ? 'Press Ctrl+C to copy.' : 'Mit Strg+C kopieren.' }
}
</script>
<template>
  <div class="block-package-code">
    <button type="button" @click="copy">{{ french ? 'Copier le code JSON' : english ? 'Copy JSON code' : 'JSON-Code kopieren' }}</button>
    <textarea ref="field" :value="code" readonly spellcheck="false" :aria-label="french ? 'JSON du paquet importable' : english ? 'Importable package JSON' : 'Importierbares Paket-JSON'"></textarea>
    <p role="status">{{ message }}</p>
  </div>
</template>
<style scoped>
.block-package-code button{border:1px solid var(--vp-c-divider);border-radius:6px;padding:8px 14px;background:var(--vp-c-bg-soft);font-weight:600}
.block-package-code textarea{display:block;width:100%;height:360px;resize:vertical;margin-top:12px;padding:14px;border:1px solid var(--vp-c-divider);border-radius:6px;background:var(--vp-c-bg-soft);color:var(--vp-c-text-1);font:12px/1.6 monospace;white-space:pre;overflow:auto}
.block-package-code p{min-height:24px}
</style>
