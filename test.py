import time

from src.components.retrieval.retriever import Retriever
from src.components.retrieval.context_builder import ContextBuilder
from src.components.retrieval.prompt_builder import PromptTemplate
from src.components.llm.generator import GroqLLM
from src.utils.db_logger import RAGDatabaseLogger


retriever = Retriever()
context_builder = ContextBuilder()
prompt_builder = PromptTemplate()
llm = GroqLLM()
db_logger = RAGDatabaseLogger()

query = "How do Nestle engage with stakeholders in value chain?"

print("\n====== USER QUERY ======\n")
print(query)

# ----------------------------
# Retrieval
# ----------------------------

start_time = time.time()

retrieved_chunks = retriever.search(query)

print("\n====== RETRIEVED CHUNKS ======\n")

for c in retrieved_chunks:
    meta = c.get("metadata", {})
    print(
        f"{meta.get('source_file')} | "
        f"chunk {meta.get('chunk_index')} | "
        f"score {c.get('similarity'):.2f}"
    )

# ----------------------------
# Context building
# ----------------------------

context, sources = context_builder.build_context(retrieved_chunks)

# ----------------------------
# Prompt building
# ----------------------------

prompt = prompt_builder.build_prompt(query, context)

# ----------------------------
# LLM generation
# ----------------------------

answer = llm.generate(prompt)

end_time = time.time()

# ----------------------------
# Output
# ----------------------------

print("\n====== ANSWER ======\n")
print(answer)

print("\n====== SOURCES ======\n")

for s in sources:
    print(
        f"[{s['id']}] {s['document']} "
        f"{s['chunk']} "
        f"(Score: {s['similarity']:.2f})"
    )

print("\n====== RUNTIME ======\n")
print(f"Total pipeline time: {end_time - start_time:.2f} seconds")

db_logger.log_query(
    query=query,
    retrieved_chunks=retrieved_chunks,
    sources=sources,
    answer=answer,
    latency=end_time-start_time
)