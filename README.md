# My ADK Project

A Google ADK agent powered by Google AI Studio, running locally.

## Setup

1. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env and add your Google AI Studio API key
   ```

3. Get your Google AI Studio API key from https://aistudio.google.com/app/apikey

## Running

### ADK Web Server (Recommended)

```bash
adk web
```

Then open http://localhost:8000 in your browser.

### CLI Mode

```bash
adk run
```

### Direct Python

```bash
python -m my_adk_project.app
```

## Models

This project uses Google AI Studio (Gemini). Default model is `gemini-2.5-flash`.

To use a different model, edit `.env`:

```bash
GEMINI_MODEL=gemini-2.5-pro
GEMINI_MODEL=gemini-2.0-flash
```

See available models at https://ai.google.dev/gemini-api/docs/models

## Project Structure

```
my_adk_project/
├── pyproject.toml              # Project configuration
├── .env                        # API keys (gitignored)
├── .env.example                # Environment template
├── .gitignore
├── README.md
├── src/
│   └── my_adk_project/
│       ├── __init__.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── __pycache__/
│       │   ├── agent.py        # Agent definition
│       │   └── models.py       # Model configuration
│       ├── app/
│       │   ├── __init__.py
│       │   └── __main__.py     # Entry point
│       └── config.py           # Settings
└── tests/
    ├── __init__.py
    └── test_agents/
        └── test_agent.py
```
