<script setup lang="ts">
import { ref, watch } from 'vue'
import { fetchPrediction } from '../../api/builder'

const input = ref('')
const prediction = ref('')

watch(input, async (newVal) => {
  if (newVal) {
    prediction.value = await fetchPrediction(newVal)
  } else {
    prediction.value = ''
  }
})

async function submitPrompt() {
if (!input.value) return
prediction.value = await fetchPrediction(input.value)
// Notify parent that a prompt was used
emit('used')
}

const emit = defineEmits(['used'])

</script>

<template>
  <div class="prompt-bar">
    <div class="input-wrapper">
      <input
        v-model="input"
        @keyup.enter="submitPrompt"
        type="text"
        placeholder="Type your prompt..."
        autocomplete="off"
        spellcheck="false"
      />
    </div>
    <div v-if="prediction" class="prediction">
      {{ prediction }}
    </div>
  </div>
</template>

<style scoped>
.input-wrapper {
  width: 100%;
  margin-bottom: 0.5rem;
}
input {
  font-size: 1.2rem;
  padding: 0.5rem 1rem;
  width: 100%;
  box-sizing: border-box;
}
.prediction {
  color: #888;
  font-style: italic;
  font-size: 1.1rem;
  margin-top: 0.25rem;
}
</style>