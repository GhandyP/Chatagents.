import os
from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()


def get_model(model_string: str = None) -> LiteLlm:
    """Create a LiteLlm model configured for OpenRouter.

    Args:
        model_string: Optional model identifier. Defaults to OPENROUTER_MODEL env var.
                     Examples: "openrouter/google/gemini-2.0-flash"
                               "openrouter/openai/gpt-4o"
                               "openrouter/anthropic/claude-3-5-sonnet"

    Returns:
        Configured LiteLlm instance for use with ADK agents.
    """
    model = model_string or os.getenv("OPENROUTER_MODEL", "openrouter/google/gemini-2.0-flash")

    return LiteLlm(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )
