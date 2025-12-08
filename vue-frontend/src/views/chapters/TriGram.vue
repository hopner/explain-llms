<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Looking just at the previous word does not give much context on what the next word should be.", slide: 0},
    { title: "", text: "So instead of looking at pairs of words, we look at triplets of words.", slide: 1},
    { title: "", text: "In the same way as before, we can now read Alice in Wonderland. However, instead of just finding the probability of the next word based on the previous word, we now consider the previous two words.", slide: 2},
    { title: "", text: "We use this approach for every word we can find in the dataset." , slide: 3},
    { title: "", text: "Now, when given a prompt, we have a bit more context to predict the next word. This should hopefully result in better predictions." , slide: 4},
    { title: "", text: "As we can see on our little example sentence, this amount of context is enough to make a correct prediction. But with larger datasets we will require even more context which takes loads of computation." , slide: 5}
];
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/TriGram.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>