import google.generativeai as genai

class GoogleProvider:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.api_key = api_key

    def ask(self, question, chat_memory, system_prompt=""):
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction=system_prompt if system_prompt else None
        )
        history = []
        for msg in chat_memory:
            if msg["role"] == "system":
                continue
            role = "user" if msg["role"] == "user" else "model"
            history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=history)
        response = chat.send_message(question)
        return response.text

    def get_available_models(self):
        models = []
        try:
            for m in genai.list_models():
                if "generateContent" in m.supported_generation_methods:
                    models.append(m.name.replace("models/", ""))
            return sorted(models)
        except Exception:
            return ["gemini-1.5-flash", "gemini-1.5-pro"]
