from llm.llm import LLM


class AzureLLM(LLM):
    def generate_response(self, prompt: str) -> str:
        return "Azure response"