import unittest
from unittest.mock import create_autospec
from uuid import uuid4

from chat.chat_agent import ChatAgent
from chat.chat_api_model import ChatRequest, ChatResponse
from llm.llm import LLM


class TestChatAgent(unittest.TestCase):
    def setUp(self):
        self._llm = create_autospec(LLM)

    def test_given_valid_question_answer_is_correct(self):
        self._llm.generate_response.return_value = "The weather is sunny."
        chat_agent = ChatAgent(self._llm)
        chat_request = ChatRequest(chat_id=uuid4(), question="What is the weather like?")

        response: ChatResponse = chat_agent.chat(chat_request)

        assert response.response == "The weather is sunny."
        assert response.chat_id == chat_request.chat_id
