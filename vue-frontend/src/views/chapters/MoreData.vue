<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Right now the AI reads from just one source which can mean it is biased towards that source.", slide: 0},
    { title: "", text: "Since this source is the only one, the AI cant gather diverse perspectives and it will generalize poorly.", slide: 1},
    { title: "", text: "In hopes of improving, we add more data sources.", slide: 2},
    { title: "", text: "Now, the model will predict tokens from multiple sources, hopefully providing a more generalized text output." , slide: 3},
];
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/MoreData.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>