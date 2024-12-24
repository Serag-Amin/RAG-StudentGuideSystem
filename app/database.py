import faiss
import numpy as np
from config import Config
from embedding import SentenceTransformerEmbeddingFunction

class FAISSManager:
    def __init__(self):
        self.embed_fn = SentenceTransformerEmbeddingFunction()
        self.embedding_dim = 384  
        self.index = faiss.IndexFlatL2(self.embedding_dim)  
        self.documents = []  

    def add_documents(self, chunks):
        documents = [chunk.page_content for chunk in chunks]
        embeddings = self.embed_fn(documents)
        embeddings = np.array(embeddings).astype('float32')
        
        self.documents.extend(documents)  
        self.index.add(embeddings)  

    def query(self, query_text, n_results=None):
        if n_results is None:
            n_results = Config.N_RESULTS

        # Embed query text
        query_embedding = self.embed_fn([query_text])
        query_embedding = np.array(query_embedding).astype('float32')

        # Perform search
        distances, indices = self.index.search(query_embedding, n_results)

        # Return results
        results = [{"page_content": self.documents[idx]} for idx in indices[0]]
        return results
