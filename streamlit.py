import streamlit as st
import time
import logging

from src.components.retrieval.retriever import Retriever
from src.components.retrieval.context_builder import ContextBuilder
from src.components.retrieval.prompt_builder import PromptTemplate
from src.components.llm.generator import GroqLLM
from src.utils.db_logger import RAGDatabaseLogger
from src.utils.document_uploader import DocumentUploader
import streamlit as st
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_embedding_model()
# ----------------------------
# Logging
# ----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Starting Supply Chain Copilot UI")


# ----------------------------
# Page Setup
# ----------------------------

st.set_page_config(
    page_title="Supply Chain Risk Copilot",
    page_icon="📦",
    layout="wide"
)


# ----------------------------
# Blue Enterprise Theme
# ----------------------------
st.sidebar.title("Knowledge Base")

uploaded_file = st.sidebar.file_uploader(
    "Upload a new PDF document",
    type=["pdf"]
)

if uploaded_file:

    uploader = DocumentUploader()

    if st.sidebar.button("Process Document"):

        with st.spinner("Indexing document..."):

            num_chunks = uploader.add_document(
                uploaded_file,
                uploaded_file.name
            )

        st.sidebar.success(
            f"Document indexed successfully ({num_chunks} chunks added)"
        )
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: #f1f5f9;
}

.header-title {
    font-size: 36px;
    font-weight: 700;
    color: #3b82f6;
}

.subtitle {
    color: #94a3b8;
    font-size: 16px;
}

.source-card {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
    border-left: 4px solid #3b82f6;
}

.chat-user {
    background-color: #1e293b;
    padding: 10px;
    border-radius: 10px;
}

.chat-ai {
    background-color: #0b2447;
    padding: 10px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------
# Header
# ----------------------------

st.markdown(
    '<div class="header-title">📦 Supply Chain Policy & Vendor Risk Copilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask questions about corporate sustainability, supply chain governance, and vendor policies.</div>',
    unsafe_allow_html=True
)

st.divider()


# ----------------------------
# Initialize backend
# ----------------------------

retriever = Retriever()
context_builder = ContextBuilder()
prompt_builder = PromptTemplate()
llm = GroqLLM()
db_logger = RAGDatabaseLogger()


# ----------------------------
# Chat Memory
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ----------------------------
# Display Chat History
# ----------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)


# ----------------------------
# Chat Input
# ----------------------------

query = st.chat_input("Ask a question about supply chain policies...")


if query:

    logger.info(f"User query: {query}")
    print(f"User query: {query}")

    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(f'<div class="chat-user">{query}</div>', unsafe_allow_html=True)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing supply chain documents..."):

            start = time.time()

            logger.info("Running retrieval")
            retrieved_chunks = retriever.search(query)

            logger.info(f"Retrieved {len(retrieved_chunks)} chunks")

            context, sources = context_builder.build_context(retrieved_chunks)

            prompt = prompt_builder.build_prompt(query, context)

            logger.info("Calling LLM")

            answer = llm.generate(prompt)

            latency = time.time() - start

            logger.info(f"LLM completed in {latency:.2f}s")

        st.markdown(f'<div class="chat-ai">{answer}</div>', unsafe_allow_html=True)

        st.markdown("### Sources")

        for s in sources:

            st.markdown(
                f"""
                <div class="source-card">
                📄 <b>{s['document']}</b> — chunk {s['chunk']} <br>
                Similarity: {s['similarity']:.2f}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.caption(f"Response time: {latency:.2f} seconds")

        st.session_state.messages.append({"role": "assistant", "content": answer})

        logger.info("Saving query to PostgreSQL")

        db_logger.log_query(
            query=query,
            retrieved_chunks=retrieved_chunks,
            sources=sources,
            answer=answer,
            latency=latency
        )