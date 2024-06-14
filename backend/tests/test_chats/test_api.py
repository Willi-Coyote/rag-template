from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_should_return_422_when_field_is_missing():
    response = client.post("/v1/chats", json={})

    assert response.status_code == 422


def test_should_return_chat_question():
    question = "How are you?"

    response = client.post("/v1/chats", json={"question": question})

    assert response.status_code == 200
    assert response.json() == {"message": f"Your question was {question}"}
