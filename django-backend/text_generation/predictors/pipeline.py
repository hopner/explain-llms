import os
import json

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

            if pretrained_model and self._is_model_compatible(pretrained_model, requested_depth):
                self.predictor.load(pretrained_model)
            else:
                self.predictor.train(self.corpus, self.tokenizer)
        else:
            self.predictor = RandomPredictor()
            self.predictor.train(self.corpus, self.tokenizer)

    def load_corpus(self, config: dict):
        corpus = []
        id_to_path = self._resolve_knowledge_paths()
        knowledge = config.get("knowledge", [])
        for entry in knowledge:
            bid = entry.get("id")
            path = id_to_path.get(bid)
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

    def _is_model_compatible(self, model: dict, requested_depth: int) -> bool:
        if not model:
            return False
        
        if model.get("ngram") != requested_depth:
            return False
        
        pretrained_tokenizer = model.get("tokenizer")
        current_tokenizer = self.config.get("capabilities", {}).get("tokenizer", {}).get("type", "whitespace")
        if pretrained_tokenizer != current_tokenizer:
            return False
        
        pretrained_ids = model.get("knowledge", [])
        current_ids = [entry.get("id") for entry in self.config.get("knowledge", []) if entry.get("id")]
        if sorted(pretrained_ids) != sorted(current_ids):
            return False
        
        return True

    
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
    
    def _resolve_knowledge_paths(self) -> dict:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'data', 'book_info.json')
        try:
            with open(json_path, 'r') as f:
                book_data = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Knowledge file {json_path} not found.")
            return {}
        mapping = {}
        for item in book_data:
            bid = item.get('id')
            path = item.get('path')
            if bid and path:
                mapping[bid] = path
        return mapping