import random
from .base import Predictor

class RandomPredictor(Predictor):
    def __init__(self, vocab_file='./text_generation/predictors/data/words_alpha.txt'):
        with open(vocab_file, "r", encoding="utf-8") as f:
            self.vocabulary = [line.strip() for line in f if line.strip()]
        self.corpus_vocab = []

    def train(self, tokens: list[str], tokenizer=None):
        self.corpus_vocab = list(set(tokens))

    def predict(self, prompt: str) -> str:
        if self.corpus_vocab:
            return random.choice(self.corpus_vocab)
        return random.choice(self.vocabulary)
