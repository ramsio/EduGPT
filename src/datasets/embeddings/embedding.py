import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Embedding:
    def __init__(self, vocabulary_size, embedding_dimension=50):
        self.vocabulary_size = vocabulary_size
        self.embedding_dimension = embedding_dimension
        self.embeddings_path = BASE_DIR / "data" / "embeddings" / "embeddings.npy"
        self.weights = None

    def initialize(self):
        self.weights = np.random.randn(self.vocabulary_size, self.embedding_dimension)
        print("========== EMBEDDINGS ==========")
        print(f"Tamaño del vocabulario : {self.vocabulary_size}")
        print(f"Dimensión del embedding : {self.embedding_dimension}")
        print(f"Matriz : {self.weights.shape}")

    def get_vector(self, token_id):
        return self.weights[token_id]

    def save(self):
        self.embeddings_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(self.embeddings_path, self.weights)
        print(f"Embeddings guardados en:\n{self.embeddings_path}")

    def show_example(self, token_id, token):
        vector = self.get_vector(token_id)
        print("Ejemplo de embedding")
        print("--------------------")
        print(f"Token : {token}")
        print(f"ID    : {token_id}")
        print("\nVector:")
        print(vector)
