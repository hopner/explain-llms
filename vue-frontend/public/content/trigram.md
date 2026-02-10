---
slide: 0
---

Looking just at the previous word does not give much context on what the next word should be.

---
slide: 1
---

So instead of looking at pairs of words, we look at triplets of words.

---
slide: 2
---

In the same way as before, we can now read Alice in Wonderland. However, instead of just finding the probability of the next word based on the previous word, we now consider the previous two words.

---
slide: 3
---

We use this approach for every word we can find in the dataset.

---
slide: 4
---

Now, when given a prompt, we have a bit more context to predict the next word. This should hopefully result in better predictions.

---
slide: 5
---

As we can see on our little example sentence, this amount of context is enough to make a correct prediction. But with larger datasets we will require even more context which takes loads of computation.
