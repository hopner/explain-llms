import hashlib
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
        self.initialized = False
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.models_dir = os.path.join(base_dir, 'data', 'precomputed_models')
        os.makedirs(self.models_dir, exist_ok=True)

    def initialize(self):
        if self.initialized:
            return
        
        print("\n" + "="*70)
        print("Starting pre-computation of models...")
        print("="*70 + "\n")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'data', 'book_info.json')

        with open(json_path, 'r') as f:
            book_data = json.load(f)

        book_ids = [book['id'] for book in book_data if book.get('id')]

        tokenizers = ['whitespace', 'regex', 'nltk']
        depths = [1, 2, 3]

        corpus_combos = []

        for book_id in book_ids:
            corpus_combos.append([book_id])
        for pair in itertools.combinations(book_ids, 2):
            corpus_combos.append(list(pair))

        total_models = len(corpus_combos) * len(tokenizers) * len(depths)

        print(f"Total models to compute: {total_models}")
        print(f"Books: {len(book_ids)}")
        print(f"Corpus combinations: {len(corpus_combos)}")
        print(f"Tokenizers: {len(tokenizers)}")
        print(f"Depths: {len(depths)}")
        print("-" * 70+"\n")

        computed_models = 0
        skipped_models = 0

        with tqdm(total=total_models, desc="Computing models", unit="model") as pbar:
            for corpus_ids in corpus_combos:
                for tokenizer_mode in tokenizers:
                    tokenizer = Tokenizer(tokenizer_mode)
                    tokens = self._load_corpus_tokens(corpus_ids, tokenizer, book_data)

                    for depth in depths:
                            model_path = self._get_model_path(corpus_ids, tokenizer_mode, depth)
                            if os.path.exists(model_path):
                                skipped_models += 1
                                pbar.update(1)
                                continue

                            model = NGramPredictor(depth=depth)
                            model.train(tokens, tokenizer)

                            with open(model_path, 'w', encoding='utf-8') as f:
                                json.dump(model.model, f)
                            
                            computed_models += 1
                            corpus_key = self._make_corpus_key(corpus_ids)
                            pbar.set_postfix_str(f"{corpus_key} | {tokenizer_mode} | {depth}-gram")
                            pbar.update(1)
        self.initialized = True
        print("\n" + "="*70)
        print(f"✅ Pre-computation complete!")
        print(f"Computed models: {computed_models}")
        print(f"Skipped models (already exist): {skipped_models}")
        print(f"Total models (computed + skipped): {total_models}")
        print("="*70 + "\n")

    def get_model(self, corpus_ids: list, tokenizer_type: str, depth: int) -> Optional[dict]:
        """Retrieve a pre-computed model."""
        model_path = self._get_model_path(corpus_ids, tokenizer_type, depth)
        if not os.path.exists(model_path):
            return None
        
        try:
            with open(model_path, 'r', encoding='utf-8') as f:
                model_data = json.load(f)
            return model_data
        except Exception as e:
            print(f"Error loading model from {model_path}: {e}")
            return None


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
    
    def _get_model_path(self, corpus_ids: list, tokenizer_type: str, depth: int) -> str:
        """Generate file path for a model."""
        corpus_key = self._make_corpus_key(corpus_ids)
        # Use hash to avoid filesystem issues with long names
        key_hash = hashlib.md5(corpus_key.encode()).hexdigest()[:8]
        filename = f"{key_hash}_{tokenizer_type}_{depth}gram.json"
        return os.path.join(self.models_dir, filename)

model_store = ModelStore()