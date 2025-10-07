class Predictor:

    def train(self, tokens: list[str], tokenizer=None):
        raise NotImplementedError("Subclasses must implement this method")
    
    def predict(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")