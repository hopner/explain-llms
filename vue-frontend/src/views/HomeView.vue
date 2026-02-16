<script setup lang="ts">
import { useRouter } from 'vue-router';
import { hasSeenIntro } from '../api/user';
const router = useRouter();

const modelBuilder = () => {
    if (hasSeenIntro()) {
        router.push({ name: 'Builder' });
        return;
    }
    router.push({ name: 'Intro' });
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
    gap: 3rem;
    flex-direction: row;
    padding: 0;
    background: var(--color-bg-primary);
}

button {
    flex: 0 1 35vw;
    min-width: 250px;
    max-width: 500px;
    height: 80vh;
    padding: 0;
    font-size: 2.5rem;
    cursor: pointer;
    border-radius: 1.5rem;
    border: none;
    color: white;
    transition: background 0.2s, transform 0.1s;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
}

button:nth-child(1) {
    background: var(--color-primary);
}

button:nth-child(1):hover {
    background: var(--color-primary-hover);
}

button:nth-child(2) {
    background: var(--color-accent);
}

button:nth-child(2):hover {
    background: var(--color-accent-hover);
}

button:active {
    transform: scale(0.98);
}
</style>