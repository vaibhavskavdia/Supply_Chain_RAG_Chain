import os
import json
from logger import logger
import numpy as np
import faiss
from src.configs import FAISS_INDEX_PATH

faiss.read_index(FAISS_INDEX_PATH)
class VectorStore:
    #handles the faiss vector storage 
    def __init__(self):
        self.index=None
        
    def create_index(self,embeddings):
        embeddings=np.array(embeddings).astype("float32")
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)

        dimension=embeddings.shape[1]
        logger.info(f"Creating FAISS index with embedding dimension: {dimension}")
        
        self.index=faiss.IndexFlatIP(dimension)   
        self.index.add(embeddings)
        logger.info(f"FAISS index created and {len(embeddings)} embeddings added successfully.")
        
    def save_index(self,index_path="data/db/faiss_index.bin"):
        os.makedirs("data/db", exist_ok=True)
        faiss.write_index(self.index, index_path)
        logger.info(f"FAISS index saved at {index_path}")
        
    def save_metadata(self, metadata, path="data/db/chunk_metadata.json"):
        with open(path, "w") as f:
            json.dump(metadata, f, indent=4)
        logger.info("Chunk metadata saved")
    