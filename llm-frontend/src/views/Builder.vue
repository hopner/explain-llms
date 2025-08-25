<script lang="ts" setup>
import { ref } from 'vue'
import PromptBar from '../components/builder/PromptBar.vue'
import ImprovementSelection from '../components/builder/ImprovementSelection.vue'

const showImprovements = ref(false)

function handlePromptUsed() {
  showImprovements.value = true
}
</script>

<template>
  <div>
    <h1>Build Your Own AI</h1>
    <PromptBar @used="handlePromptUsed" />
    <ImprovementSelection v-if="showImprovements" />
  </div>
</template>