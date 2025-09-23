class Predictor:
    def predict(self, prompt: str, config: dict) -> str:
        raise NotImplementedError("Subclasses must implement this method")