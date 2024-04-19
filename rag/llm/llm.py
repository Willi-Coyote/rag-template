from typing import Protocol


class LLM(Protocol):
    def generate_response(self, prompt: str) -> str:
        ...
