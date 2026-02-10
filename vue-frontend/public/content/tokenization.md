---
slide: 0
---

Given some text there are many ways to split it into tokens.

---
slide: 1
---

Right now we are just splitting based on where the spaces are.

---
slide: 2
---

But this may not be the best approach as this does not handle punctuation well. For instance, 'mat.' is treated as one token rather than 'mat' and '.'

---
slide: 3
---

Let us instead split the tokens based on punctuation and spaces.

---
slide: 4
---

We will stick to this simple idea for now, but in the future we might consider more advanced tokenization methods. A word might make more sense to split into multiple tokens to capture more meaning.

---
slide: 5
---

The tokens are not actually text, but rather some kind of numerical representation. In real LLMs, tokens are multi-dimensional vectors, but we will simplify this for now. Using numerical values instead of text allows us to learn some meaning in the words in the future by using machine learning techniques.

---
slide: 6    
---

This way we can represent text as a sequence of numerical values, which is the very speciality of computers.
