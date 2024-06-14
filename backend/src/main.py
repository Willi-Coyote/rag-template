from fastapi import FastAPI
from .chats.api import chat_router

app = FastAPI()

app.include_router(chat_router)
