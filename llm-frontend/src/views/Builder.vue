<script lang="ts" setup>
import PromptBar from '../components/builder/PromptBar.vue';
</script>

<template>
  <div>
    <h1>Build Your Own AI</h1>
  </div>
  <PromptBar @used="console.log('Prompt used!')" />
</template>

