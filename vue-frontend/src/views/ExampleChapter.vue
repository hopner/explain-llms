<script setup>
import ScrollytellingContainer from '../components/ScrollytellingContainer.vue';

const steps = [
  { title: "Introduction", text: "Welcome to LLMs", slide: 0 },
  { title: "What are LLMs?", text: "AI systems...", slide: 1 },
  { title: "How they work", text: "Through attention...", slide: 2 },
  { title: "Build your own", text: "Start simple...", slide: 3 },
  { title: "Ready to explore?", text: "Let's begin!", slide: 4 }
]
</script>

<template>
  <ScrollytellingContainer 
    slides-src="/slides/SimpleSlideshow.html"
    :steps="steps"
  />
</template>