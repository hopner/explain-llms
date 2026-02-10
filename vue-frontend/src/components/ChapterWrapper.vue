<script setup>
import { useRouter, useRoute } from 'vue-router';
import ScrollytellingContainer from './ScrollytellingContainer.vue';
import { defineProps } from 'vue';

const props = defineProps({
  slidesSrc: { type: String, required: true },
  steps: { type: Array, required: true },
  nextPage: { type: String, required: false },
});

const router = useRouter();
const route = useRoute();

function goToNextPage() {
  // If user came from ChapterOverview, go back there
  if (route.query.from === 'overview') {
    router.push({ name: 'ChapterOverview' });
  } else if (props.nextPage) {
    router.push(props.nextPage);
  }
}
</script>

<template>
  <div class="chapter">
    <ScrollytellingContainer :slides-src="slidesSrc" :steps="steps" />
    <div v-if="props.nextPage" class="next-page">
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
  position: relative;
  z-index: 10;
}

.next-page button {
  background: #215E61;
  color: #F5FBE6;
  border: none;
  padding: 1rem 2rem;
  border-radius: 9999px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.next-page button:hover {
  background: #FE7F2D;
  transform: translateY(-2px);
}
</style>
