<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Let us have a look at how our data shapes the AI's predictions.", slide: 0},
    { title: "", text: "Right now the AI reads from just one source which can mean it is biased towards that source.", slide: 1},
    { title: "", text: "Since this source is the only one, the AI cant gather diverse perspectives and it will generalize poorly.", slide: 2},
    { title: "", text: "In hopes of improving, we add more data sources.", slide: 3},
    { title: "", text: "Now, the model will predict tokens from multiple sources, hopefully providing a more generalized text output." , slide: 4},
];
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/MoreData.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>