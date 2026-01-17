from my_adk_project.agents import root_agent


def main():
    """Entry point for running the agent directly."""
    import uvicorn
    from my_adk_project.config import config

    print(f"Starting ADK web server on {config.ADK_WEB_HOST}:{config.ADK_WEB_PORT}")
    print(f"Agent: {root_agent.name}")
    print(f"Model: Using OpenRouter")
    print("\nOpen http://localhost:8000 in your browser")
    print("Press Ctrl+C to stop the server")

    uvicorn.run(
        "my_adk_project.app:app",
        host=config.ADK_WEB_HOST,
        port=config.ADK_WEB_PORT,
        reload=False,
    )


if __name__ == "__main__":
    main()
