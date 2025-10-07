<script setup>
import ChapterWrapper from '../components/ChapterWrapper.vue';

const steps = [
  { title: "", text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia enim sit accusantium corporis nisi maiores, eius provident perferendis dolore beatae reiciendis incidunt aliquid nemo laboriosam autem recusandae, eveniet molestias quaerat?", slide: 0 },
  { title: "What are LLMs?", text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia enim sit accusantium corporis nisi maiores, eius provident perferendis dolore beatae reiciendis incidunt aliquid nemo laboriosam autem recusandae, eveniet molestias quaerat?", slide: 1 },
  { title: "How they work", text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia enim sit accusantium corporis nisi maiores, eius provident perferendis dolore beatae reiciendis incidunt aliquid nemo laboriosam autem recusandae, eveniet molestias quaerat?", slide: 2 },
  { title: "Build your own", text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia enim sit accusantium corporis nisi maiores, eius provident perferendis dolore beatae reiciendis incidunt aliquid nemo laboriosam autem recusandae, eveniet molestias quaerat?", slide: 3 },
  { title: "Ready to explore?", text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia enim sit accusantium corporis nisi maiores, eius provident perferendis dolore beatae reiciendis incidunt aliquid nemo laboriosam autem recusandae, eveniet molestias quaerat?", slide: 4 }
];
</script>

<template>
  <ChapterWrapper
    :slides-src="'/slides/SimpleSlideshow.html'"
    :steps="steps"
    next-page="/builder"
  />
</template>
