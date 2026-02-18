from typing import List
from src.components.core.documents import Document
from logger import logger

class TextChunker:
    #split large documents into smaller chunks
    
    def __init__(self,chunk_size:int=1000,overlap:int=200):
        self.chunk_size=chunk_size
        self.overlap=overlap
        
    def chunk_document(self,documents:List[Document])->List[Document]:
        logger.info(f"Statrting chunking | chunk_size={self.chunk_size} | overlap={self.overlap}")
        chunked_documents=[]
        for doc in documents:
            text=doc.content
            start=0
            chunk_index=0
            
            while start<len(text):
                end=start+self.chunk_size
                chunk_text=text[start:end]
                
                chunk_metadata=doc.metadata.copy()
                chunk_metadata["chunk_index"]=chunk_index
                chunk_metadata["chunk_id"]=(f"{doc.metadata['source_file']}_chunk_{chunk_index}")
                chunked_documents.append(Document(content=chunk_text, metadata=chunk_metadata))
                start += self.chunk_size - self.overlap
                chunk_index += 1
        logger.info(f"Chunked document | file={doc.metadata['source_file']} | total_chunks={chunk_index}")
        logger.info(f"Chunking completed successfully. Total chunks created: {len(chunked_documents)}")
        return chunked_documents