import os
import requests
from dotenv import load_dotenv
load_dotenv()

class GroqProvider:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def ask(self, model, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": messages
        }

        response = requests.post(self.url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Groq Error {response.status_code}: {response.text}")

        return response.json()["choices"][0]["message"]["content"]

    def get_available_models(self):
        url_models = "https://api.groq.com/openai/v1/models"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url_models, headers=headers)
            if response.status_code == 200:
                data = response.json()
                models = [model["id"] for model in data["data"]]
                return sorted(models)
            else:
                return ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]  # Fallback caso falhe

        except Exception:
            return ["llama-3.3-70b-versatile"]