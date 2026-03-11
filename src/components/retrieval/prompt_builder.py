class PromptTemplate:

    def build_prompt(self, query, context):

        prompt = f"""
You are an AI assistant helping analyze supply chain sustainability
and corporate responsibility documents.

Answer the question using ONLY the provided context.

Guidelines:
- Base your answer strictly on the context.
- Do not invent information.
- If the answer is not in the context, say:
  "The information is not available in the provided documents."
- Be concise and factual.

Context:
{context}

Question:
{query}

Answer:
"""

        return prompt