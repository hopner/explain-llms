---
slide: 0
---

Previously we upgraded our tokenization from whitespace to punctuation aware tokenization.

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

We would get a lot more information if we tokenized it together with the rest of the abbreviation in 'N.A.S.A.'. This is when we introduce NLTK, which is a natural language toolkit. In this toolkit, the tokenization is aware of special cases like abbreviations and ellipses.

---
slide: 4
---

The toolkit is also aware of language specific cases like contractions in French and Spanish.

---
slide: 5
---

Also, by handling periods correctly, it can distinguish between end of sentence and abbreviations. Knowing when a period signifies the end of a sentence is crucial when generating larger texts.
