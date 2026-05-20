from google.adk.tools import ToolContext

def get_preferences(tool_context: ToolContext) -> dict:
    """Returns the user's saved book genre preferences.
    Call this before making any recommendations.
    Returns an empty list if no preferences have been set yet.
    """
    genres = tool_context.state.get("user_genres", [])
    return {"status": "ok", "genres": genres}

def set_preferences(genres: list[str], tool_context: ToolContext) -> dict:
    """Adds genres to the user's saved preferences without removing existing ones.
    Args:
        genres: A list of genre strings to add, e.g. ["fantasy"]
    """
    existing = tool_context.state.get("user_genres", [])
    updated = list(set(existing + genres))  # set() removes duplicates
    tool_context.state["user_genres"] = updated
    return {"status": "saved", "genres": updated}

def remove_preferences(genres: list[str], tool_context: ToolContext) -> dict:
    """Removes specific genres from the user's saved preferences.
    Args:
        genres: A list of genre strings to remove, e.g. ["sci-fi"]
    """
    existing = tool_context.state.get("user_genres", [])
    updated = [g for g in existing if g not in genres]
    tool_context.state["user_genres"] = updated
    return {"status": "updated", "genres": updated}