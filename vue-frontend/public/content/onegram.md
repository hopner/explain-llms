---
slide: 0
---

Right now, the AI reads text without understanding the meaning behind the words. It simply adds them to its vocabulary without any sense of which words usually appear together.

---
slide: 1
---

We can make the AI a bit smarter by teaching it to recognize individual words and their frequencies.

---
slide: 2
---

If we have the frequency of each word, we can estimate the probability of each word appearing next.

---
slide: 3
---

The model should be more likely to select the word with the highest probability so let us have it do that.

---
slide: 4
---

This quickly becomes repetitive as it is deterministic. The model is still too simple to capture context of each token.

---
slide: 5
---

The frequency of each token matters, but words alone aren't enough to make language any meaningful.
