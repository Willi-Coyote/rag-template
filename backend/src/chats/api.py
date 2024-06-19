from fastapi import APIRouter
from chats.api_models import ChatRequest

chats_router = APIRouter()


@chats_router.post("/v1/chats/")
async def ask_question(question_input: ChatRequest):
    return {"question": f"Your question was {question_input.question}"}
