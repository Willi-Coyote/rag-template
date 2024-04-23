from chat.chat_api_model import ChatRequest, ChatResponse
from llm.llm import LLM


class ChatAgent:

    def __init__(self, llm: LLM):
        self.llm = llm

    def chat(self, chat_request: ChatRequest) -> ChatResponse:
        llm_response = self.llm.generate_response(chat_request.question)

        return ChatResponse(chat_id=chat_request.chat_id, response=llm_response)
