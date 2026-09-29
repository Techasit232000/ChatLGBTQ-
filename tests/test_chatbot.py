"""
Unit tests for the chatbot module.
"""

import pytest
from src.chatbot import Chatbot


class TestChatbot:
    """Test cases for the Chatbot class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.chatbot = Chatbot()
    
    def test_chatbot_initialization(self):
        """Test that chatbot initializes correctly."""
        assert self.chatbot.conversation_history == []
    
    def test_reset_conversation(self):
        """Test conversation reset."""
        self.chatbot.conversation_history = ["test"]
        self.chatbot.reset_conversation()
        assert self.chatbot.conversation_history == []
    
    def test_respond(self):
        """Test chatbot response."""
        response = self.chatbot.respond("Hello")
        assert response is not None
        assert isinstance(response, str)
