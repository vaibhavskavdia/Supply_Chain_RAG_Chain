import json
from logger import logger
from src.components.embeddings.embed_text import TextEmbedder
from src.components.embeddings.vector_store import VectorStore

def run_embedding():
    logger.info("Starting Embedding")
    with open ("data/processed/chunks.json","r") as f:
        chunks=json.load(f)
    
    texts=[chunk["content"] for chunk in chunks]  
    embedder=TextEmbedder()
    embeddings=embedder.embed_text(texts)
    
    store=VectorStore()
    store.create_index(embeddings)
    store.save_index()
    store.save_metadata(chunks)
    
    logger.info("Embedding stage completed successfully")