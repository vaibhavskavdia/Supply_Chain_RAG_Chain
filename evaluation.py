evaluation_queries = [
    {
        "query": "What are Nestlé supplier human rights requirements?",
        "expected_doc": "nestle-responsible-sourcing-standard-english.pdf"
    },
    {
        "query": "How does Nestlé handle human rights due diligence?",
        "expected_doc": "non-financial-statement-2024.pdf"
    },
    {
        "query": "What policies address child labor in Nestlé supply chains?",
        "expected_doc": "creating-shared-value-sustainability-report-2023-en.pdf"
    }
]

from src.components.retrieval.retriever import Retriever
from evaluation import evaluation_queries


retriever = Retriever()

correct = 0
total = len(evaluation_queries)


for item in evaluation_queries:

    query = item["query"]
    expected_doc = item["expected_doc"]

    results = retriever.search(query, top_k=5)

    found = False

    for r in results:
        source = r["metadata"]["source_file"]

        if expected_doc in source:
            found = True
            break

    if found:
        correct += 1
        print(f"✓ Query succeeded: {query}")
    else:
        print(f"✗ Query failed: {query}")


recall = correct / total

print("\nRetrieval Recall@5:", recall)