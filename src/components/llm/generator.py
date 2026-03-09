import os
from dotenv import load_dotenv
from groq import Groq
from logger import logger

load_dotenv()


class GroqLLM:

    def __init__(self):

        logger.info("Initializing Groq LLM")

        api_key = os.getenv("GROQ_API_KEY")

        self.client = Groq(api_key=api_key)

        self.model = "llama-3.1-8b-instant"

    def generate(self, prompt):

        logger.info("Sending prompt to Groq")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content

        logger.info("Received response from Groq")

        return answer