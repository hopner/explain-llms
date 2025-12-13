<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "When just selecting random words from the dictionary, the output isn't very human-like.", slide: 0},
    { title: "", text: "To try to make it more coherent, we can try to show the AI model some real text, like Moby Dick by Herman Melville. This is called training data.", slide: 1},
    { title: "", text: "Now, we can pick words based on the training data in hopes that it produces more coherent text.", slide: 2},
    { title: "", text: "However, since we still pick words at random, the output can still be nonsensical.", slide: 3},
]
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/ReadBook.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>