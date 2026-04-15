---
slide: 0
---

The model is trained on text without understanding the meaning behind the words.
They are saved to its vocabulary without any sense of which words usually appear together.

---
slide: 1
---

We can improve the model a bit by counting individual words and how often they occur (their frequencies).

---
slide: 2
---

If we have the frequency of each word, we can estimate the probability of this word appearing in a text.

---
slide: 3
---

The model should select the word with the highest probability more often, so let us have it pick only that.

---
slide: 4
---

This quickly becomes repetitive as it is deterministic. The model is still too simple to capture the context of each word.

---
slide: 5
---

The frequency of each token matters, but words alone aren't enough to generate text that is meaningful.
