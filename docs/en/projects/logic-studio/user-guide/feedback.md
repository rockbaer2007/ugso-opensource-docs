<script setup>
import LogicStudioFeedback from '../../../../.vitepress/theme/LogicStudioFeedback.vue'

const labels = {"subject":"Subject","version":"App version","editor":"Editor","message":"Message","reply":"Reply email (optional)","open":"Open email draft","directIntro":"The form sends your report by email. A reply address is optional.","draftIntro":"The form opens a draft in your email app. You can review and send the report there.","send":"Send report","sent":"Your report was sent.","failed":"Sending failed. Your entries are still in the form."}
</script>

# Report issues and contribute

## Report publicly on GitHub

Open an issue in the shared repository so others can find the report and add their experience. [Open a GitHub issue](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues/new)

## Report privately by email

Include the app version, the affected editor, steps to reproduce, the expected result and what happened. Remove credentials and personal details from screenshots and logs.

<LogicStudioFeedback :labels="labels" />

## Contribute

You can test new versions, share examples, or help with the guide, translations and code. Tell us about your idea through either channel.
