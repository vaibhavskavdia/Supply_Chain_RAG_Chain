import faiss
import json
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

from src.configs import FAISS_INDEX_PATH, METADATA_PATH
class DocumentUploader:

    def __init__(self):

        self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")
        self.index_path = FAISS_INDEX_PATH
        self.meta_path = METADATA_PATH
        self.index = faiss.read_index(self.index_path)

        with open(self.meta_path, "r") as f:
            self.metadata = json.load(f)

    def extract_text(self, pdf_file):

        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    def chunk_text(self, text, chunk_size=500, overlap=100):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size
            chunk = text[start:end]

            chunks.append(chunk)

            start += chunk_size - overlap

        return chunks

    def add_document(self, pdf_file, filename):

        text = self.extract_text(pdf_file)

        chunks = self.chunk_text(text)

        embeddings = self.model.encode(chunks)

        self.index.add(embeddings)

        start_id = len(self.metadata)

        for i, chunk in enumerate(chunks):

            meta = {
                "content": chunk,
                "metadata": {
                    "source_file": filename,
                    "chunk_index": start_id + i
                }
            }

            self.metadata.append(meta)

        faiss.write_index(self.index, self.index_path)

        with open(self.meta_path, "w") as f:
            json.dump(self.metadata, f)

        return len(chunks)