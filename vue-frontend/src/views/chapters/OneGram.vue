<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "The AI reads text without understanding the meaning", slide: 0},
    { title: "", text: "The AI counts how often each word appears", slide: 1},
    { title: "", text: "Estimate the probability of each word", slide: 2},
    { title: "", text: "The model select the highest probability word" , slide: 3},
    { title: "", text: "This quickly becomes repetitive, deterministic, too simple to capture context" , slide: 4},
    { title: "", text: "frequency matters, but words alone aren’t enough to make language meaningful" , slide: 5}
];
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/OneGram.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>