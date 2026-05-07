import requests
import os
from .base import BaseProvider


class OpenRouterProvider(BaseProvider):
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in .env file")

        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def ask(self, model: str, messages: list) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http:localhost:3000",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "messages": messages
        }

        response = requests.post(self.url, headers=headers, json=payload, timeout=30)

        if response.status_code != 200:
            raise Exception(f"OpenRouter Error {response.status_code}: {response.text}")

        return response.json()["choices"][0]["message"]["content"]

    def get_available_models(self):
        # Aquela lógica simples de dar um get no endpoint do OpenRouter
        response = requests.get("https://openrouter.ai/api/v1/models")
        return [m['id'] for m in response.json()['data']] if response.status_code == 200 else []


