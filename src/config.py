"""
Configuration settings for the ChatLGBTQ+ chatbot.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))

# Chatbot Configuration
SYSTEM_PROMPT = """You are ChatLGBTQ+, a friendly and inclusive AI chatbot dedicated to 
providing support and information to the LGBTQ+ community."""

TEMPERATURE = 0.7
TOP_P = 0.9

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
