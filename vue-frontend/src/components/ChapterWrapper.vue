<script setup>
import { useRouter } from 'vue-router';
import ScrollytellingContainer from './ScrollytellingContainer.vue';
import { defineProps } from 'vue';

const props = defineProps({
  slidesSrc: { type: String, required: true },
  steps: { type: Array, required: true },
  nextPage: { type: String, required: false } // optional, last chapter may not have next
});

const router = useRouter();

function goToNextPage() {
  if (props.nextPage) {
    router.push(props.nextPage);
  }
}
</script>

<template>
  <div class="chapter">
    <ScrollytellingContainer :slides-src="slidesSrc" :steps="steps" />
    <div v-if="nextPage" class="next-page">
      <button @click="goToNextPage">Next →</button>
    </div>
  </div>
</template>

<style scoped>
.chapter {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.next-page {
  text-align: center;
  margin: 5rem 0 3rem;
}

.next-page button {
  background: #333;
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 9999px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.next-page button:hover {
  background: #555;
  transform: translateY(-2px);
}
</style>
