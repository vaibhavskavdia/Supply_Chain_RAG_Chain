# Supply_Chain_RAG_Chain
# 📦 Supply Chain Policy & Vendor Risk Intelligence Copilot

An AI-powered **Retrieval-Augmented Generation (RAG) system** that enables natural language querying over corporate sustainability and supply chain policy documents.

Built using real-world data from **Nestlé’s sustainability and policy reports**, this project transforms long, unstructured documents into an interactive knowledge system.

---

## 🚀 Problem Statement

Corporate documents such as:

- Sustainability reports  
- Supplier guidelines  
- Compliance policies  
- Governance frameworks  

are often **hundreds of pages long**, making it difficult to quickly extract relevant insights.

Answering questions like:

- What are supplier human rights requirements?  
- How are environmental risks assessed?  
- What governance mechanisms ensure ethical sourcing?  

requires **manual searching across multiple documents**, which is time-consuming and inefficient.

---

## 💡 Solution

This project uses **Retrieval-Augmented Generation (RAG)** to:

1. Retrieve relevant sections from documents  
2. Generate answers grounded in that context  
3. Provide accurate responses with source citations  

---

## 🧠 System Overview
User Query

↓

Query Embedding

↓

FAISS Vector Search

↓

Relevant Document Chunks

↓

Context Builder

↓

LLM (Groq Llama-3)

↓

Answer + Source Citations

↓

PostgreSQL Logging


---

## ⚙️ Features

- Semantic search using **FAISS vector database**
- Document ingestion and preprocessing pipeline  
- Smart chunking with overlap for context preservation  
- LLM-based answer generation using **Groq Llama-3**  
- Source citations for transparency  
- PostgreSQL telemetry logging (queries, latency, sources)  
- Streamlit-based interactive UI  
- Dynamic PDF upload and indexing  

---

## 📊 Dataset & Scale

- **4 enterprise policy reports (Nestlé)**  
- ~**1.07M characters processed**  
- **1,352 semantic chunks**  
- Chunk size: 1000 tokens  
- Overlap: 200 tokens  
- Average response latency: **~2.29 seconds**

---

## 🧩 Tech Stack

**Core AI / ML**
- Python  
- Retrieval-Augmented Generation (RAG)  
- SentenceTransformers (Embeddings)  
- Cross-Encoder Reranking  

**Vector Database**
- FAISS (384-dimensional embeddings)

**LLM**
- Groq API (Llama-3)

**Backend**
- Modular pipeline architecture (8+ components)

**Database**
- PostgreSQL (Telemetry logging)

**Frontend**
- Streamlit

---

## 🏗️ Project Structure
src/

│

├── 
ingestion/
├── 
chunking/
├── 
embeddings/
├── 
retrieval/
├── 
reranker/
├── 
context_builder/
├── 
prompt_builder/
├──
 llm/
├──
 utils/
│
├──
 config.py


---

## 🔄 Pipeline Breakdown

### 1. Document Ingestion
- Extract text from PDF reports  
- Clean and preprocess content  

### 2. Chunking
- Split text into semantic chunks  
- Maintain context using overlap  

### 3. Embeddings
- Convert chunks into vector representations  

### 4. Vector Search
- Store embeddings in FAISS  
- Retrieve top-k relevant chunks  

### 5. Reranking
- Improve retrieval accuracy using cross-encoder  

### 6. Context Building
- Combine retrieved chunks into structured context  

### 7. LLM Generation
- Generate grounded responses using Groq Llama-3  

### 8. Logging
- Store query, sources, and latency in PostgreSQL  

---

## 📈 Observability

The system logs:

- User queries  
- Retrieved chunks  
- Source documents  
- Response latency  
- Generated answers  

This enables monitoring, debugging, and evaluation of the system.

---

## 🌐 Deployment

- Built using Streamlit for interactive UI  
- Integrated with PostgreSQL for logging  
- Optimized for cloud deployment  

---

## 📸 Example Use Cases

- Supply chain risk analysis  
- Vendor compliance verification  
- ESG policy exploration  
- Corporate governance insights  

---

## 🔮 Future Improvements

- RAG evaluation dashboard  
- Multi-document comparison queries  
- Knowledge graph integration  
- Advanced query rewriting  

---

## 🤝 Acknowledgements

- Nestlé sustainability & policy reports (public data)  
- FAISS (Facebook AI)  
- SentenceTransformers  
- Groq API  

---

## 📬 Contact

- LinkedIn: Your LinkedIn  
- GitHub: Your GitHub  

---

⭐ If you found this useful, consider giving the repo a star!