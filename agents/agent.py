from google.adk.agents import Agent
from tools.open_library import search_book, search_author_id, search_author_works

root_agent = Agent(
    name="book_agent",
    model="gemini-2.5-flash",
    description="A simple assistant that answers questions about books.",
    instruction=(
        "You are a helpful book assistant. "
        "Use the get_book_info tool when the user asks about a specific book. "
        "Be concise and friendly."
    ),
    tools=[search_book, search_author_id, search_author_works],
)