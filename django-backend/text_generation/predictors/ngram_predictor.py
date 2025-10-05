import random
from collections import Counter, defaultdict
from .base import Predictor

class NGramPredictor(Predictor):
    def __init__(self, depth: int = 1, mode: str = 'deterministic'):
        super().__init__()
        self.depth = depth
        self.mode = mode
        self.model = {}
        self.tokenizer = None

    def train(self, tokens: list[str], tokenizer=None) -> dict:
        if tokenizer:
            self.tokenizer = tokenizer
        model = {'ngram': self.depth, "counts": defaultdict(Counter)}
        for i in range(len(tokens) - self.depth):
            key = " ".join(tokens[i:i + self.depth])
            next_word = tokens[i + self.depth]
            model["counts"][key][next_word] += 1

        model["counts"] = {k: dict(v) for k, v in model["counts"].items()}
        self.model = model
        return model
    
    def load(self, model: dict):
        self.depth = model.get('ngram', self.depth)
        self.model = model

    def predict(self, prompt: str, config: dict | None = None) -> str:
        if not self.model or 'counts' not in self.model:
            raise ValueError("Model is not trained or loaded properly.")
        
        tokens = self.tokenizer.tokenize(prompt) if self.tokenizer else prompt.strip().split()
        if len(tokens) < self.depth:
            raise ValueError(f"Prompt must have at least {self.depth} tokens.")
        
        key = " ".join(tokens[-self.depth:])
        options = self.model['counts'].get(key)
        if not options:
            return None
        if self.mode == 'deterministic':
            return max(options.items(), key=lambda x: x[1])[0]
        else:
            words, weights = zip(*options.items())
            return random.choices(words, weights=weights)[0]
        
