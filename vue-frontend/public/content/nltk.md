---
slide: 0
---

Previously we upgraded our tokenization from whitespace to punctuation-aware tokenization.

---
slide: 1
---

However, in natural languages, punctuation can be ambiguous and requires special handling.

---
slide: 2
---

As you can see, the current tokenizer will treat 'N' as its own token, which does not give us a lot of information.

---
slide: 3
---

We would get a lot more information if we tokenized it together with the rest of the abbreviation in 'N.A.S.A.'.
The tokenization should be aware of special cases like abbreviations and ellipses.
We can achieve this by introducing a more language-aware tokenizer, here we use NLTK, the natural language toolkit library.

---
slide: 4
---

The toolkit can also distinguish language specific cases like contractions in French and Spanish.

---
slide: 5
---

It can distinguish between end-of-sentence and abbreviations. Knowing when a period signifies the end of a sentence is crucial when generating larger texts.
