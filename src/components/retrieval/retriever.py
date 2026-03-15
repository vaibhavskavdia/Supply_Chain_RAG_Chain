import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from logger import logger
from src.configs import FAISS_INDEX_PATH



class Retriever:
    """Retrieves relevant document chunks from FAISS vector database."""

    def __init__(self):

        logger.info("Loading FAISS index")

        self.index = faiss.read_index(FAISS_INDEX_PATH)

        logger.info("Loading chunk metadata")

        with open("data/db/chunk_metadata.json", "r") as f:
            self.metadata = json.load(f)

        logger.info("Loading embedding model for queries")
        self.model =SentenceTransformer("paraphrase-MiniLM-L3-v2")

    def load_model(self):
        if self.model is None:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

    def search(self, query):

        self.load_model()

        query_embedding = self.model.encode([query])

    def search(self, query, top_k=5, similarity_threshold=0.65):

        logger.info(f"Searching for query: {query}")

        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        faiss.normalize_L2(query_embedding)

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(distances[0], indices[0]):

            similarity = float(score)

            if similarity >= similarity_threshold:

                chunk = self.metadata[idx]

                chunk["similarity"] = similarity

                results.append(chunk)

        logger.info(f"{len(results)} chunks passed similarity filtering")

        return results