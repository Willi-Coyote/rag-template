import uvicorn
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from chat.chat_api_router import chat_router


def init_application():
    chat_app = FastAPI()
    chat_app.include_router(chat_router)

    FastAPIInstrumentor.instrument_app(chat_app)

    return chat_app


fast_api_app = init_application()

if __name__ == "__main__":
    uvicorn.run(fast_api_app, host="0.0.0.0", port=8000)
