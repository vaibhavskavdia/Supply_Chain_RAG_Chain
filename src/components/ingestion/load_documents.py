import os
import json
from pypdf import PdfReader
from typing import List,Dict
from logger import logger
from src.components.ingestion.clean_text import TextCleaner
from src.components.ingestion.extract_metadata import MetadataExtractor
from src.components.chunking.clause_chunker import TextChunker

RAW_DATA_PATH="data/raw"
OUTPUT_PATH="data/processed/ingested_documents.json"
""" Core document object used across the entire project.
This same object will later be:
- chunked
- embedded
- stored in vector DB
- retrieved for RAG"""
class Document:
    def __init__(self,content:str,metadata:Dict):
        
        self.content=content
        self.metadata=metadata

#Text extraction

class PdfExtractor:
    def extract_text(self,pdf_path:str)->str:
        
        reader=PdfReader(pdf_path)
        text_chunks=[]
        
        for page in reader.pages:
            page_text=page.extract_text()
            if page_text:
                text_chunks.append(page_text)
                
        return "\n".join(text_chunks)


# Document Loader   
class DocumentLoader:
    #Main ingestion pipeline
    def __init__(self,raw_data_path:str):
        self.raw_data_path=raw_data_path
        self.pdf_extractor=PdfExtractor()
        self.text_cleaner=TextCleaner()
        self.metadata_extractor=MetadataExtractor()
        
    def load_documents(self)->List[Document]:
        documents=[]
        
        folder_mapping={
            "audits":"audit_reports",
            "policies":"policy",
        }
        
        for folder_name,doc_type in folder_mapping.items():
            logger.info(f"Scanning folder: {folder_name} as {doc_type}")
            folder_path=os.path.join(self.raw_data_path,folder_name)
            if not os.path.exists(folder_path):
                continue
            
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".pdf"):
                    
                    file_path=os.path.join(folder_path,file_name)
                    print(f"Processing file:{file_path}")
                    logger.info(f"Processing file: {file_name}")
                    # Extract text
                    raw_text=self.pdf_extractor.extract_text(file_path)
                    
                    # Clean text
                    cleaned_text=self.text_cleaner.clean_text(raw_text)
                    if len(cleaned_text) < 500:
                        print(f"⚠️ Skipping {file_name} (too little content)")
                        logger.info(f"Skipping {file_name} due to insufficient content")
                        continue
                    # Extract metadata
                    metadata=self.metadata_extractor.extract(doc_type=doc_type,file_name=file_name)
                    
                    # Create Document object
                    document=Document(content=cleaned_text,metadata=metadata)
                    documents.append(document)
                    logger.info(f"Loaded document | type={doc_type} | file={file_name} | chars={len(cleaned_text)}")
        return documents


def run_ingestion():
        logger.info("Starting document ingestion pipeline")

        loader=DocumentLoader(raw_data_path=RAW_DATA_PATH)
        documents=loader.load_documents()
        os.makedirs("data/processed", exist_ok=True)

        # Serialize documents to JSON
        serialized_docs=[]
        for doc in documents:
            serialized_docs.append({
                "content":doc.content,
                "metadata":doc.metadata
            })
            
        # Save to output file
        with open(OUTPUT_PATH,"w") as f:
            json.dump(serialized_docs,f,indent=4)
            
        
        logger.info(
        f"Ingestion completed successfully. Total documents ingested: {len(documents)}")

def run_chunking():
    logger.info("Starting ingestion pipeline")

    loader = DocumentLoader(raw_data_path=RAW_DATA_PATH)
    documents = loader.load_documents()

    logger.info("Starting chunking stage")

    chunker = TextChunker(chunk_size=1000, overlap=200)
    chunked_docs = chunker.chunk_document(documents)

    os.makedirs("data/processed", exist_ok=True)

    serialized_chunks = [
        {
            "content": chunk.content,
            "metadata": chunk.metadata
        }
        for chunk in chunked_docs
    ]

    with open("data/processed/chunks.json", "w") as f:
        import json
        json.dump(serialized_chunks, f, indent=4)

    logger.info(
        f"Saved {len(chunked_docs)} chunks to data/processed/chunks.json"
    )