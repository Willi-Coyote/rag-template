from fastapi import APIRouter
from .payloads import ChatsRequest
chat_router = APIRouter()


@chat_router.post("/v1/chats")
async def process_question(question: ChatsRequest):
    return {"message": f"Your question was {question.question}"}
