<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();

const backToHome = () => {
    router.push({ name: 'Overview' });
};
</script>

<template>
    <div>
        <h1>This is a work in progress</h1>
        <button @click="backToHome">
            Back to Home
        </button>
    </div>
</template>