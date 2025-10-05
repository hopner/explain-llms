from .random_predictor import RandomPredictor
from .ngram_predictor import NGramPredictor
from .tokenizer import Tokenizer

class PredictionPipeline:
    def __init__(self, config: dict, pretrained_model: dict | None = None):
        self.config = config
        self.tokenizer = Tokenizer(config.get("capabilities", {}).get("tokenizer", {}).get("type", "whitespace"))
        self.corpus = self.load_corpus(config)

        prev_cfg = config.get("capabilities", {}).get("previous", {})
        self.predictor = None
        if prev_cfg.get("enabled"):
            requested_depth = prev_cfg.get("depth", 1)
            self.predictor = NGramPredictor(
                depth=requested_depth,
                mode=prev_cfg.get("mode", "deterministic")
            )

            if pretrained_model and pretrained_model.get("ngram") == requested_depth:
                self.predictor.load(pretrained_model)
            else:
                self.predictor.train(self.corpus, self.tokenizer)
        else:
            self.predictor = RandomPredictor()
            self.predictor.train(self.corpus, self.tokenizer)

    def load_corpus(self, config: dict):
        corpus = []
        knowledge = config.get("knowledge", [])
        for entry in knowledge:
            path = entry.get("path")
            if not path:
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                    corpus.extend(self.tokenizer.tokenize(text))
            except FileNotFoundError:
                print(f"Warning: Corpus file {path} not found.")
                continue
        return corpus
    
    def predict(self, prompt: str) -> str:
        if self.predictor is None:
            fallback = RandomPredictor()
            fallback.train(self.corpus, self.tokenizer)
            return fallback.predict(prompt)
        return self.predictor.predict(prompt)
    
    def get_model(self) -> dict:
        if isinstance(self.predictor, NGramPredictor):
            return self.predictor.model
        elif isinstance(self.predictor, RandomPredictor):
            return {"vocab": self.predictor.corpus_vocab or self.predictor.vocabulary}
        return {}
