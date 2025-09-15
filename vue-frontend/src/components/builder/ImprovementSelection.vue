<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { fetchAlternatives, addFeatureToConfig } from '../../api/builder' // Adjust path as needed

const alternatives = ref<{ id: string, label: string }[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const router = useRouter()

onMounted(async () => {
  try {
    alternatives.value = await fetchAlternatives()
  } catch (e) {
    error.value = 'Could not load improvements.'
  } finally {
    loading.value = false
  }
})

async function selectAlternative(featureId: string) {
  try {
    router.push({ name: 'Example' })
    await addFeatureToConfig(featureId)
  } catch (e) {
    error.value = 'Could not add improvement.'
  }
}
</script>

<template>
  <div class="improvement-selection">
    <h2>Choose an improvement for your model:</h2>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="buttons">
      <button
        v-for="alt in alternatives"
        :key="alt.id"
        @click="selectAlternative(alt.id)"
      >
        {{ alt.label }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.improvement-selection {
  margin-top: 2rem;
}
.buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
button {
  padding: 1rem 2rem;
  font-size: 1.1rem;
  border-radius: 0.5rem;
  border: none;
  background: #4f8cff;
  color: white;
  cursor: pointer;
  transition: background 0.2s;
}
button:hover {
  background: #2563eb;
}
.error {
  color: #d32f2f;
  margin-top: 1rem;
}
</style>