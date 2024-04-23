from uuid import uuid4, UUID

from fastapi import APIRouter, Depends

from chat.chat_api_model import Chat, ChatRequest
from llm.llm import LLM

chat_router = APIRouter()


@chat_router.post("/v1/chat", response_model=Chat)
def create_chat():
    return Chat(chat_id=uuid4())


@chat_router.post("/v1/chat/{id}", response_model=Chat)
def get_chat(id: UUID, chat: ChatRequest, llm: LLM = Depends(get_llm)):
    pass
