from pydantic import BaseModel


class ChatsRequest(BaseModel):
    question: str
