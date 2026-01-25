import logging.handlers
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="Supply_Chain_RAG_Copilot"
list_of_files=[
    #".github/workflows/.gitkeep",
    f"data/raw/contracts/contracts",
    f"data/raw/policies/policies",
    f"data/raw/audits/audits",
    f"data/processed/processed",
    f"data/db/db",
    f"src/__init__.py",
    f"src/components/ingestion/__init__.py",
    f"src/components/ingestion/load_documents.py",
    f"src/components/ingestion/clean_text.py",
    f"src/components/ingestion/extract_metadata.py",
    f"src/components/chunking/clause_chunker.py",
    f"src/components/embeddings/embed_text.py",
    f"src/components/embeddings/vector_store.py",
    f"src/components/storage/__init__.py",
    f"src/components/storage/db.py",
    f"src/components/storage/models.py",
    f"src/components/storage/repository.py",
    f"src/components/retrieval/retriever.py",
    f"src/components/llm/prompts.py",
    f"src/components/llm/generator.py",
    f"src/components/llm/__init__.py",
    f"src/components/ui/streamlit_app.py",
    f"src/configs/settings.yaml",
    f"src/utils.py",
    f"Dockerfile",
    "requirements.txt",
    "app.py",
    "logger.py",
    "exception.py",
    "setup.py",
    ".gitignore"
    
    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file {filename}")
        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    
    else:
        logging.info(f"{filename}: already exists")