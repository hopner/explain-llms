import random
from collections import Counter, defaultdict
from .base import Predictor

class NGramPredictor(Predictor):
    def __init__(self, depth: int = 1, mode: str = 'deterministic'):
        super().__init__()
        self.depth = depth
        self.mode = mode
        self.model = {"counts": {}}
        self.tokenizer = None

    def train(self, tokens: list[str], tokenizer=None) -> dict:
        if tokenizer:
            self.tokenizer = tokenizer

        all_counts = {d: defaultdict(Counter) for d in range(1, self.depth + 1)}
        for d in range(1, self.depth + 1):
            for i in range(len(tokens) - d):
                key = " ".join(tokens[i:i + d])
                next_word = tokens[i + d]
                all_counts[d][key][next_word] += 1

        self.model = {
            "ngram": self.depth,
            "counts": {
                d: {k: dict(v) for k, v in all_counts[d].items()} for d in range(1, self.depth + 1)
            },
            "tokenizer": getattr(self.tokenizer, 'tokenizer_type', 'whitespace') if self.tokenizer else 'whitespace',
        }
        return self.model
    
    def load(self, model: dict):
        self.depth = model.get('ngram', self.depth)
        self.model = model

    def predict(self, prompt: str, config: dict | None = None) -> str:
        if not self.model or 'counts' not in self.model:
            raise ValueError("Model is not trained or loaded properly.")
        
        tokens = self.tokenizer.tokenize(prompt) if self.tokenizer else prompt.strip().split()

        if not tokens:
            vocab = self._get_vocabulary()
            return random.choice(vocab) if vocab else ""
        
        for d in range(min(self.depth, len(tokens)), 0, -1):
            key = " ".join(tokens[-d:])
            options = self.model['counts'].get(d, {}).get(key)

            if options:
                if self.mode == 'deterministic':
                    return max(options.items(), key=lambda x: x[1])[0]
                else:
                    words, weights = zip(*options.items())
                    return random.choices(words, weights=weights)[0]
                
        vocab = self._get_vocabulary()
        return random.choice(vocab) if vocab else ""
        
    def _get_vocabulary(self) -> list[str]:
        """Collects all possible next tokens from the model."""
        vocab = set()
        for options in self.model.get("counts", {}).values():
            vocab.update(options.keys())
        return list(vocab)