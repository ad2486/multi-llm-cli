from abc import ABC, abstractmethod
from typing import List, Dict

class BaseProvider(ABC):
    @abstractmethod
    def ask(self, model: str, messages: List[Dict[str, str]]) -> str:
        pass

    @abstractmethod
    def get_available_models(self) -> list:
        pass