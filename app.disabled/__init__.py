from google.adk.web import FastAPIWrapper
from my_adk_project.agents import root_agent

app = FastAPIWrapper(agent=root_agent)
