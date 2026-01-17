import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/google/gemini-2.0-flash")
    ADK_WEB_PORT = int(os.getenv("ADK_WEB_PORT", "8000"))
    ADK_WEB_HOST = os.getenv("ADK_WEB_HOST", "0.0.0.0")


config = Config()
