import re
try:
    import nltk
    from nltk.tokenize import word_tokenize
except ImportError:
    nltk = None


class Tokenizer:
    def __init__(self, tokenizer_type="whitespace"):
        self.tokenizer_type = tokenizer_type

    def tokenize(self, text: str):
        if self.tokenizer_type == "whitespace":
            return text.split()

        if self.tokenizer_type == "regex":
            return re.findall(r"\w+|[^\w\s]", text, re.UNICODE)

        if self.tokenizer_type == "nltk" and nltk:
            return word_tokenize(text)

        # fallback
        return text.split()
