<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ref } from 'vue';
import ScrollytellingContainer from './ScrollytellingContainer.vue';
import { defineProps } from 'vue';
import { hasSeenAutoplayPromptGlobal, dismissAutoplayPromptGlobal } from '../api/user';

const props = defineProps({
  slidesSrc: { type: String, required: true },
  steps: { type: Array, required: true },
  nextPage: { type: String, required: false },
});

const emit = defineEmits(['complete']);
const router = useRouter();
const route = useRoute();

const autoplayReady = ref(hasSeenAutoplayPromptGlobal());

const showAutoplayPrompt = () => !autoplayReady.value;

const scrollytellingRef = ref(null);

function dismissAutoplayPromptPopup() {
  dismissAutoplayPromptGlobal();
  autoplayReady.value = true;
  scrollytellingRef.value?.attemptAutoplay();
}

function goToNextPage() {
  emit('complete');

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
    <div v-if="showAutoplayPrompt()" class="autoplay-overlay">
      <div class="autoplay-popup">
        <h2>Start scrolling!</h2>
        <p>Scroll to progress through the story—each text box has a matching animation. If an animation doesn’t play, click the screen once to enable it.</p>
        <button @click="dismissAutoplayPromptPopup" class="dismiss-btn">
          Let's go →
        </button>
      </div>
    </div>

    <ScrollytellingContainer ref="scrollytellingRef" :slides-src="slidesSrc" :steps="steps" />
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
  position: relative;
}

.autoplay-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.autoplay-popup {
  background: var(--color-bg-primary);
  border-radius: 1.5rem;
  padding: 3rem;
  max-width: 500px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.autoplay-popup h2 {
  margin: 0 0 1rem 0;
  font-size: 2rem;
  color: var(--color-primary);
  font-weight: 700;
}

.autoplay-popup p {
  margin: 0 0 2rem 0;
  font-size: 1.125rem;
  color: var(--color-text);
  line-height: 1.6;
}

.dismiss-btn {
  padding: 1rem 2rem;
  font-size: 1.125rem;
  font-weight: 600;
  background: var(--color-primary);
  color: white;
  border: none;
  border-radius: 0.75rem;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
}

.dismiss-btn:hover {
  background: var(--color-primary-hover);
}

.dismiss-btn:active {
  transform: scale(0.98);
}

.next-page {
  text-align: center;
  margin: 5rem 0 3rem;
  position: relative;
  z-index: 10;
}

.next-page button {
  background: var(--color-primary);
  color: var(--color-bg-primary);
  border: none;
  padding: 1rem 2rem;
  border-radius: 9999px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.next-page button:hover {
  background: var(--color-accent);
  transform: translateY(-2px);
}
</style>
