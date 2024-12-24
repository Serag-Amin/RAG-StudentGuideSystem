from sentence_transformers import SentenceTransformer

class SentenceTransformerEmbeddingFunction:
    def __init__(self):
        # Load the SentenceTransformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def __call__(self, input_texts):
        return self.model.encode(input_texts, convert_to_tensor=False).tolist()
