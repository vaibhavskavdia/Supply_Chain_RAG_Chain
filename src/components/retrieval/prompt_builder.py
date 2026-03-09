class PromptTemplate:

    """
    Generates the prompt for the LLM
    """

    def build_prompt(self, query, context):

        prompt = f"""
You are a Supply Chain Compliance AI assistant.

Use ONLY the context below to answer the question.

If the answer is not contained in the context,
say that the information is not available.

Context:
{context}

Question:
{query}

Answer:
"""

        return prompt