import itertools
import json
import os
from typing import Optional
from tqdm import tqdm

from .tokenizer import Tokenizer
from .ngram_predictor import NGramPredictor


class ModelStore:
    """
    Stores pre-computed models in RAM for fast access.
    """

    def __init__(self):
        self.models = {}
        self.initialized = False

    def initialize(self):
        if self.initialized:
            return
        
        print("\n" + "="*70)
        print("Starting pre-computation of models...")
        print("="*70 + "\n")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'data', 'temp_book_info.json')

        with open(json_path, 'r') as f:
            book_data = json.load(f)

        book_ids = [book['id'] for book in book_data if book.get('id')]

        tokenizers = ['whitespace', 'regex', 'nltk']
        depths = [1, 2, 3]
        modes = ['deterministic', 'weighted']

        corpus_combos = []

        for book_id in book_ids:
            corpus_combos.append([book_id])
        for pair in itertools.combinations(book_ids, 2):
            corpus_combos.append(list(pair))

        total_models = len(corpus_combos) * len(tokenizers) * len(depths) * len(modes)

        print(f"Total models to compute: {total_models}")
        print(f"Books: {len(book_ids)}")
        print(f"Corpus combinations: {len(corpus_combos)}")
        print(f"Tokenizers: {len(tokenizers)}")
        print(f"Depths: {len(depths)}")
        print(f"Modes: {len(modes)}")
        print("-" * 70+"\n")

        with tqdm(total=total_models, desc="Computing models", unit="model") as pbar:
            for corpus_ids in corpus_combos:
                corpus_key = self._make_corpus_key(corpus_ids)
                for tokenizer_mode in tokenizers:
                    tokenizer = Tokenizer(tokenizer_mode)
                    tokens = self._load_corpus_tokens(corpus_ids, tokenizer, book_data)

                    for depth in depths:
                        for mode in modes:
                            model = NGramPredictor(depth=depth, mode=mode)
                            model.train(tokens, tokenizer)

                            key = (corpus_key, tokenizer_mode, depth, mode)
                            self.models[key] = model.model

                            pbar.set_postfix_str(f"{corpus_key} | {tokenizer_mode} | {depth}-gram | {mode}")
                            pbar.update(1)
        self.initialized = True
        print("\n" + "="*70)
        print(f"✅ Pre-computation complete! {len(self.models)} models ready in RAM")
        print("="*70 + "\n")

    def get_model(self, corpus_ids: list, tokenizer_type: str, depth: int, mode: str) -> Optional[NGramPredictor]:
        """Retrieve a pre-computed model."""
        corpus_key = self._make_corpus_key(corpus_ids)
        key = (corpus_key, tokenizer_type, depth, mode)
        return self.models.get(key)


    def _make_corpus_key(self, corpus_ids: list) -> str:
        """Generate a unique key for a given corpus combination."""
        return ' | '.join(sorted(corpus_ids))
    
    def _load_corpus_tokens(self, corpus_ids: list, tokenizer: Tokenizer, book_data: list) -> list:
        """Load and tokenize corpus from book IDs."""
        id_to_path = {book['id']: book['path'] for book in book_data}
        
        tokens = []
        for book_id in corpus_ids:
            path = id_to_path.get(book_id)
            if not path:
                continue
            
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    tokens.extend(tokenizer.tokenize(text))
            except Exception as e:
                print(f"Warning: Failed to load {path}: {e}")
        
        return tokens

model_store = ModelStore()