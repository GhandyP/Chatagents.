from google.adk.agents import Agent
from .models import get_model


root_agent = Agent(
    name="my_assistant",
    model=get_model(),
    description="A helpful AI assistant powered by OpenRouter and Google ADK.",
    instruction="""You are a helpful, friendly AI assistant.
Your goal is to assist users with their questions and tasks to the best of your ability.

Guidelines:
- Be concise and clear in your responses
- If you don't know something, say so honestly
- Ask clarifying questions if needed
- Be polite and professional
- Focus on being genuinely helpful""",
)
