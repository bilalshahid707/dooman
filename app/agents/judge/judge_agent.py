from services.llm_service import LLMService
from .judge_instructions import instructions
import json


class Judge:
    Model = "llama-3.3-70b"

    def __init__(self):
        self.name = "judge"
        self.instructions = instructions
        self.client = LLMService()

    def evaluate(self, user_message, doorman_reply, history):

        messages = [
            {"role": "system", "content": f"{self.instructions}"},
        ]
        messages.extend(history)
        messages.append({"role": "user", "content": f"{user_message}"})
        messages.append({"role": "system", "content": f"{doorman_reply}"})

        evaluation = self.client.chat(self.Model, messages)
        evaluation_obj = json.loads(evaluation)
        return evaluation_obj
