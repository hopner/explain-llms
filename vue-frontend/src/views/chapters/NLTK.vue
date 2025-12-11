<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Previously we upgraded our tokenization from whitespace to punctuation aware tokenization.", slide: 0},
    { title: "", text: "However, in natural languages, punctuation can be ambiguous and requires special handling.", slide: 1},
    { title: "", text: "As you can see, the current tokenizer will treat 'N' as its own token, which does not give us a lot of information.", slide: 2},
    { title: "", text: "We would get a lot more information if we tokenized it together with the rest of the abbreviation in 'N.A.S.A.'. This is when we introduce NLTK, which is a natural language toolkit. In this toolkit, the tokenization is aware of special cases like abbreviations and ellipses.", slide: 3},
    { title: "", text: "The toolkit is also aware of language specific cases like contractions in French and Spanish.", slide: 4},
    { title: "", text: "Also, by handling periods correctly, it can distinguish between end of sentence and abbreviations. Knowing when a period signifies the end of a sentence is crucial when generating larger texts.", slide: 5}
]
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/nltk.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>