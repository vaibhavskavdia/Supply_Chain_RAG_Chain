from src.components.retrieval.retriever import Retriever
from src.components.retrieval.context_builder import ContextBuilder
from src.components.retrieval.prompt_builder import PromptTemplate


retriever = Retriever()
context_builder = ContextBuilder()
prompt_builder = PromptTemplate()

query = "What are Nestlé supplier human rights requirements?"

retrieved_chunks = retriever.search(query)

context = context_builder.build_context(retrieved_chunks)

prompt = prompt_builder.build_prompt(query, context)

print("\n===== FINAL PROMPT =====\n")
print(prompt)