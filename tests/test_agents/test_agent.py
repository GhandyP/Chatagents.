import pytest
from my_adk_project.agents.agent import root_agent


def test_root_agent_exists():
    """Test that root_agent is defined."""
    assert root_agent is not None


def test_root_agent_has_name():
    """Test that root_agent has a name."""
    assert root_agent.name == "my_assistant"


def test_root_agent_has_description():
    """Test that root_agent has a description."""
    assert root_agent.description is not None
    assert len(root_agent.description) > 0


def test_root_agent_has_instruction():
    """Test that root_agent has instructions."""
    assert root_agent.instruction is not None
    assert len(root_agent.instruction) > 0


def test_root_agent_has_model():
    """Test that root_agent has a model."""
    assert root_agent.model is not None


def test_root_agent_is_agent():
    """Test that root_agent is an Agent instance."""
    from google.adk.agents import Agent
    assert isinstance(root_agent, Agent)
