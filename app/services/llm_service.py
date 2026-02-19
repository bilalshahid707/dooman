from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MORPHEUS_API_KEY = os.environ.get("MORPHEUS_API_KEY")
MORPHEUS_BASE_URL = os.environ.get("MORPHEUS_BASE_URL")


class LLMService:

    def __init__(self):
        self.client = OpenAI(api_key=MORPHEUS_API_KEY, base_url=MORPHEUS_BASE_URL)

    def chat(self, model: str, messages: list[dict]):
        response = self.client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content
