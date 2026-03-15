import os
from dotenv import load_dotenv
from groq import Groq
from logger import logger
import time
load_dotenv()


class GroqLLM:

    def __init__(self):

        logger.info("Initializing Groq LLM")

        api_key = os.getenv("GROQ_API_KEY")

        self.client = Groq(api_key=api_key)

        self.model = "llama-3.1-8b-instant"

    def generate(self, prompt):

        try:

            start = time.time()

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],max_tokens=2000
            )

            answer = response.choices[0].message.content

            if not answer or answer.strip() == "":
                raise ValueError("Empty LLM response")

            return answer

        except Exception as e:

            print(f"LLM Error: {str(e)}")

            return (
                "The AI system encountered an issue while generating the response. "
                "Please try again."
            )