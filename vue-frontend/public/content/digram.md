---
slide: 0
---

Remember how we can count word frequencies? So far we counted words individually. Let's extend that to include a little bit of context. 

---
slide: 1
---

The word that comes before influences how likely the possibilities for the next word are.

---
slide: 2
---

We can map our entire text in this way.

---
slide: 3
---

For each word we count how often each following word occurs and save the distributions in a table.

---
slide: 4
---

Given larger data, we need to store a lot more information.

---
slide: 5
---

Each word that appears in the text has its own set of possible following words.

---
slide: 6
---

This gives us more context, and allows for more varied text generation.

---
slide: 7
---

However, this is still limited to only looking at one previous word.
