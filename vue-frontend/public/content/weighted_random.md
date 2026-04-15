---
slide: 0
---

As the model is now, we are picking the most frequent word from the training data. On the left you can see an example histogram for the words that were found following the word "the".

---
slide: 1
---

This is what we call a deterministic model as it will always pick the most likely word. However, this can lead to repetitive and boring text. So we need to introduce some randomness to make the text more nuanced. Imagine turning the probability distribution into a wheel of fortune where the wedge sizes correspond to word probabilities.

---
slide: 2
---

Now we can select a word by spinning the wheel and pick the word the wheel lands on.

---
slide: 3
---

By doing it this way we have introduced some unpredictability into the model which hopefully will make it choose more varied words and ensure that it will not get stuck repeating the same phrases. But it is still not completely random as the following words with the higher frequency have a larger wedge and are more likely to be picked. Finding a balance between so called creativity and coherence is key.
