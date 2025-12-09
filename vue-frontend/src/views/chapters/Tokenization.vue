<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Given some text there are many ways to split it into tokens.", slide: 0},
    { title: "", text: "Right now we are just splitting based on where the spaces are.", slide: 1},
    { title: "", text: "But this may not be the best approach as this does not handle punctuation well. For instance, 'mat.' is treated as one token rather than 'mat' and '.'", slide: 2},
    { title: "", text: "Let us instead split the tokens based on punctuation and spaces.", slide: 3},
    { title: "", text: "We will stick to this simple idea for now, but in the future we might consider more advanced tokenization methods. A word might make more sense to split into multiple tokens to capture more meaning." , slide: 4},
    { title: "", text: "The tokens are not actually text, but rather some kind of numerical representation. In real LLMs, tokens are multi-dimensional vectors, but we will simplify this for now. Using numerical values instead of text allows us to learn some meaning in the words in the future by using machine learning techniques.", slide: 5},
    { title: "", text: "This way we can represent text as a sequence of numerical values, which is the very speciality of computers.", slide: 6},
]
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/Tokenization.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>