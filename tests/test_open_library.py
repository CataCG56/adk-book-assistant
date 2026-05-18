from tools.open_library import search_book, search_author_id, search_author_works
import json

def test_found():
    result = search_book("Dune")
    assert result["status"] == "found"
    assert "Frank Herbert" in result["authors"]

def test_not_found():
    result = search_book("xyzzy_this_does_not_exist_99")
    assert result["status"] == "not_found"

def test_author_id():
    result = search_author_id("J.R.R. Tolkien")
    assert result == "OL26320A"

def test_author_works():
    result = search_author_works("OL26320A")
    pretty_json = json.dumps(result, indent=4, sort_keys=True)
    print(pretty_json)
    assert result is not None 
