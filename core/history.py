from typing import List, Dict

class ChatMemory:
    def __init__(self, system_prompt: str = " ") -> None:
        self.system_prompt = system_prompt
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    def add_message(self, role: str, content: str):
        """Adds a messsage (user or assistant) to the history."""
        self.history.append({"role": role, "content": content})

    def get_context(self):
        context = []

        if self.system_prompt.strip():
            context.append({"role": "system", "content": self.system_prompt})

        context.extend(self.history)
        return context

    def clear(self):
        """Resets the chat, mantaining only the system prompt."""
        self.history = [{"role": "system", "content": self.system_prompt}]

    def set_system_prompt(self, new_prompt: str):
        self.system_prompt = new_prompt
        self.clear()

    def get_last_assistant_message(self):
        for msg in reversed(self.history):
            if msg["role"] == "assistant":
                return msg["content"]
        return None
