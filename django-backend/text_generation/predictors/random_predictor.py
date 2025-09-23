import random
from .base import Predictor

class RandomPredictor(Predictor):
    def __init__(self, vocab_file='./text_generation/predictors/data/words_alpha.txt'):
        with open(vocab_file, "r", encoding="utf-8") as f:
            self.vocabulary = [line.strip() for line in f if line.strip()]

    def predict(self, prompt: str, config: dict) -> str:
        return random.choice(self.vocabulary)
