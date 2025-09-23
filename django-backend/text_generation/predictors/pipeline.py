from .random_predictor import RandomPredictor
from .tokenizer import Tokenizer

class PredictionPipeline:
    def __init__(self, config: dict):
        self.config = config
        self.corpus = self.load_corpus(config)
        self.random_predictor = RandomPredictor()

    def load_corpus(self, config: dict):
        tokenizer_type = config.get("capabilities", {}).get("tokenizer", {}).get("type", "whitespace")
        tokenizer = Tokenizer(tokenizer_type)

        corpus = []
        knowledge = config.get("knowledge", [])
        for entry in knowledge:
            path = entry.get("path")
            if not path:
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                    corpus.extend(tokenizer.tokenize(text))
            except FileNotFoundError:
                print(f"Warning: Corpus file {path} not found.")
                continue
        return corpus
    
    def predict(self, prompt: str) -> str:
        knowledge = self.config.get("knowledge", [])
        if not knowledge or not self.corpus:
            return self.random_predictor.predict(prompt, self.config)

        return self.random_predictor.predict(prompt, self.config)
