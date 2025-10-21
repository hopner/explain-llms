<script setup lang="ts">
import { ref } from 'vue'
import { fetchPrediction } from '../../api/builder'

const input = ref('')
const prediction = ref('')
const suggestion = ref('')

async function handleKeyup(e: KeyboardEvent) {
  const target = e.target as HTMLInputElement | null
  const caretAtEnd = !!target && target.selectionStart === target.selectionEnd && target.selectionStart === input.value.length

  if (e.key === 'ArrowRight' && suggestion.value && caretAtEnd) {
    e.preventDefault()
    input.value += suggestion.value
    prediction.value = ''
    suggestion.value = ''
    return
  }

  if (input.value.endsWith(' ')) {
    prediction.value = await fetchPrediction(input.value)
    if (prediction.value.startsWith(input.value)) {
      suggestion.value = prediction.value.slice(input.value.length)
    } else {
      suggestion.value = prediction.value
    }
    emit('used')
  } else {
    prediction.value = ''
    suggestion.value = ''
  }
}

async function submitPrompt() {
  if (!input.value) return
  prediction.value = await fetchPrediction(input.value)
  emit('used')
}

const emit = defineEmits(['used'])
</script>

<template>
  <div class="prompt-bar">
    <div class="input-wrapper">
      <div class="input-overlay">
        <span class="mirror">{{ input }}</span><span v-if="suggestion" class="ghost">{{ suggestion }}</span>
      </div>
      <input v-model="input" @keyup="handleKeyup" @keyup.enter="submitPrompt" type="text"
        placeholder="Type your prompt..." autocomplete="off" spellcheck="false" />
    </div>
  </div>
</template>

<style scoped>
.input-wrapper {
  position: relative;
  width: 100%;
}

.input-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  font-family: inherit;
  line-height: 1.5;
  pointer-events: none;
  white-space: pre-wrap;
  overflow: hidden;
}

.mirror {
  color: transparent;
  user-select: none;
  line-height: 1.75;
}

.ghost {
  color: #aaa;
}

input {
  position: relative;
  font-size: 1.2rem;
  line-height: 1.5;
  padding: 0.5rem 1rem;
  width: 100%;
  box-sizing: border-box;
  font-family: inherit;
  background: transparent;
}
</style>
