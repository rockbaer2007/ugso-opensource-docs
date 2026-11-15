<script setup>
const props = defineProps({ labels: { type: Object, required: true } })

function openEmail(event) {
  const fields = new FormData(event.currentTarget)
  const subject = 'HA Logic Studio Pro – ' + fields.get('subject').trim()
  const body = ['version', 'editor', 'message', 'reply']
    .filter(key => fields.get(key).trim())
    .map(key => props.labels[key] + '\n' + fields.get(key).trim())
    .join('\n\n')
  window.location.href = 'mailto:info@ugso-software.de?subject='
    + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body)
}
</script>

<template>
  <form class="logic-feedback" @submit.prevent="openEmail">
    <label>{{ labels.subject }} <input name="subject" required maxlength="120"></label>
    <label>{{ labels.version }} <input name="version" maxlength="40"></label>
    <label>{{ labels.editor }} <input name="editor" maxlength="80"></label>
    <label>{{ labels.message }} <textarea name="message" required rows="6" maxlength="1200"></textarea></label>
    <label>{{ labels.reply }} <input name="reply" type="email" autocomplete="email" maxlength="120"></label>
    <button type="submit">{{ labels.open }}</button>
  </form>
</template>

<style scoped>
.logic-feedback {
  display: grid;
  gap: 0.75rem;
  max-width: 34rem;
}
.logic-feedback label {
  display: grid;
  gap: 0.25rem;
  font-weight: 600;
}
.logic-feedback input,
.logic-feedback textarea {
  width: 100%;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  border-radius: 6px;
  padding: 0.45rem 0.65rem;
  font-weight: 400;
}
.logic-feedback button {
  justify-self: start;
  background: var(--vp-button-brand-bg);
  color: var(--vp-button-brand-text);
  border-radius: 6px;
  padding: 0.5rem 0.85rem;
}
.logic-feedback :is(input, textarea, button):focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 2px;
}
</style>
