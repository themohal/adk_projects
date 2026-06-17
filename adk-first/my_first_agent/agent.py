from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.llm_agent import Agent


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[google_search],
)
search_tool = AgentTool(root_agent)