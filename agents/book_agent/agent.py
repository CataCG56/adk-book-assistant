from google.adk.agents import Agent
from tools.open_library import search_book, get_author_works


def get_book_info(title: str) -> dict:
    """Returns basic info about a book by title.

    Args:
        title: The title of the book to look up.

    Returns:
        A dict with author and genre information.
    """
    # Mock data — will replace with real API in v1
    BOOKS = {
        "dune": {"author": "Frank Herbert", "genre": "Science Fiction", "year": 1965},
        "1984": {"author": "George Orwell", "genre": "Dystopian", "year": 1949},
    }
    key = title.lower().strip()
    if key in BOOKS:
        return {"status": "found", **BOOKS[key]}
    return {"status": "not_found", "title": title}


root_agent = Agent(
    name="book_agent",
    model="gemini-2.5-flash",
    description="A simple assistant that answers questions about books.",
    instruction=(
        "You are a helpful book assistant. "
        "Use the get_book_info tool when the user asks about a specific book. "
        "Be concise and friendly."
    ),
    tools=[get_book_info],
)