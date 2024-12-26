from sentence_transformers import SentenceTransformer

class SentenceTransformerEmbeddingFunction:
    def __init__(self):
        #-MiniLM-L6-v2 Embedding model (ignore this comment)
        # Load paraphrase-multilingual-MiniLM-L12-v2' embedding model
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    
    def __call__(self, input_texts):
        return self.model.encode(input_texts, convert_to_tensor=False).tolist()
