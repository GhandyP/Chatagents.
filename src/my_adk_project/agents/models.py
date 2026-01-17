import os
from typing import Optional

from dotenv import load_dotenv
from google.adk.models import Gemini

load_dotenv(override=True)


def get_model(model_string: Optional[str] = None) -> Gemini:
    """Create a Gemini model configured for Google AI Studio.

    Args:
        model_string: Optional model identifier. Defaults to GEMINI_MODEL env var.
                     Examples: "gemini-2.5-flash"
                               "gemini-2.5-pro"
                               "gemini-2.0-flash"

    Returns:
        Configured Gemini instance for use with ADK agents.
    """
    model = model_string or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Missing Google AI Studio API key. Set GOOGLE_API_KEY in .env."
        )

    return Gemini(model=model)
