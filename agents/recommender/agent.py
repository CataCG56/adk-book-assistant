from google.adk.agents.llm_agent import Agent
from tools.preferences import get_preferences, set_preferences, remove_preferences


recommender_agent = Agent(
    model='gemini-2.5-flash',
    name='recommender_agent',
    description='You are the agent responsible for managing user preferences and providing book recommendations based on those preferences. ' \
    'Use the get_preferences tool to retrieve the user\'s current genre preferences and make book suggestions from that preferences if they dont have preferences ask the user for what genres he likes, the set_preferences tool to add new genres to the user\'s preferences, and the remove_preferences tool to remove genres from the user\'s preferences. ' \
    'Be concise and provide relevant information to the user.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_preferences, set_preferences, remove_preferences],
)
