from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_should_return_200_with_question():
    response = client.post("/v1/chats/", json={"question": "How to test python code?"})

    assert response.status_code == 200
    assert response.json() == {"question": "Your question was How to test python code?"}


def test_should_return_422_when_question_is_missing():
    response = client.post("/v1/chats/")

    assert response.status_code == 422
