import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    ADK_WEB_PORT = int(os.getenv("ADK_WEB_PORT", "8000"))
    ADK_WEB_HOST = os.getenv("ADK_WEB_HOST", "0.0.0.0")


config = Config()
