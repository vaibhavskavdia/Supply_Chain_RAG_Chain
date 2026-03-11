import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FAISS_INDEX_PATH = os.path.join(BASE_DIR, "../data/db/faiss_index.bin")

METADATA_PATH = os.path.join(BASE_DIR, "../data/db/chunk_metadata.json")