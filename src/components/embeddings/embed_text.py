from sentence_transformers import SentenceTransformer
from logger import logger


class TextEmbedder:
    def __init__(self,model_name:str="all-MiniLM-L6-v2"):
        logger.info(f"Initializing TextEmbedder with model: {model_name}")
        self.model=SentenceTransformer(model_name)
        
    def embed_text(self,text:str)->list:
        
        #generate embedding for the input text
        logger.info(f"Embedding text of length: {len(text)}")
        embeddings=self.model.encode(text,show_progress_bar=True)
        logger.info(f"Generated embedding of length: {len(embeddings)}")
        return embeddings
    
#this does not store the embeddings, it just generates them. 
# The storage and retrieval of embeddings will be handled in the retrieval stage using a vector database like FAISS or Pinecone.