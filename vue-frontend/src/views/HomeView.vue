<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();

const modelBuilder = () => {
    router.push({ name: 'Builder' });
};

const chapterOverview = () => {
    router.push({ name: 'ChapterOverview' });
};
</script>

<template>
    <div class="overview">
        <button @click="modelBuilder">
            Build your own AI
        </button>
        <button @click="chapterOverview">
            Chapter Overview
        </button>
    </div>
</template>

<style scoped>
.overview {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 3rem; /* Adds space between buttons */
  flex-direction: row;
  padding: 0;
}

button {
  flex: 0 1 35vw;         /* Each button takes up to 35% of viewport width */
  min-width: 250px;
  max-width: 500px;
  height: 80vh;           /* Not full height */
  padding: 0;
  font-size: 2.5rem;
  cursor: pointer;
  border-radius: 1.5rem;
  border: none;
  background: #4f8cff;
  color: white;
  transition: background 0.2s, transform 0.1s;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  justify-content: center;
}
button:hover {
  background: #2563eb;
  transform: scale(1.03);
}
</style>