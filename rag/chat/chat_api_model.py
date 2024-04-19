from uuid import UUID

from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: UUID


class ChatRequest(BaseModel):
    chat_id: UUID
    question: str


class ChatResponse(BaseModel):
    chat_id: UUID
    response: str
