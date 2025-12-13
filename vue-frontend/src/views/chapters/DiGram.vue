<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Remeber how we can count word frequencies?", slide: 0},
    { title: "", text: "However, the word that comes before often matters to what the next word is.", slide: 1},
    { title: "", text: "We can map our entire text in this way.", slide: 2},
    { title: "", text: "This can be stored in table, like how dictionaries have definitions for each word we will have the distribution of following words for each word.", slide: 3},
    { title: "", text: "Given larger data, we need to store a lot more information." , slide: 4},
    { title: "", text: "Each token that appears in the text has its own set of possible following tokens.", slide: 5},
    { title: "", text: "This gives us more context, and allows for more varied text generation.", slide: 6},
    { title: "", text: "However, this is still limited to only looking at one previous word.", slide: 7}
]
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/DiGram.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>