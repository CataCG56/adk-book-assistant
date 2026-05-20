from google.adk.agents.llm_agent import Agent
from tools.open_library import search_book, search_author_id, search_author_works


researcher_agent = Agent(
    model='gemini-2.5-flash',
    name='researcher_agent',
    description='An agent that can search for books and authors using the Open Library API.' \
    'Use the search_book tool to find information about a specific book, the search_author_id tool to find the id of an author, and the search_author_works tool to find the works of an author. ' \
    'Be concise and provide relevant information to the user.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[search_book, search_author_id, search_author_works],
)
